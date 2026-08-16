# Decisions group K — Documentation governance

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-091 — ARCHITECTURE.md is the canonical architecture document and wins every disagreement

> **When any doc disagrees with
> this one, this one wins, and a new ratified decision lands here first.**

**In plain words.** Where two documents disagree about the architecture, this one is right, and a new ruling must be written into it before anywhere else.

**Why.** Stated constraint, ARCHITECTURE.md:308-316: the per-layer design documents are the authoritative detail for their own scope but are not rival architecture documents; without one document that wins, a reader has no way to resolve a disagreement between two.

**Status.** LIVE · decided 2026-06-29 · ratifier not stated

**Home.** `ARCHITECTURE.md:565-566`

**Provenance.** ARCHITECTURE.md:308-316 'Doc governance (2026-06-29) - the hierarchy'

### D-092 — A cross-cutting contract is stated once and never redefined in a layer document

> a **cross-cutting contract is stated once, here (§2.15), and never redefined in a
> layer doc**

**In plain words.** Rules that apply to every stage are written down in one place. A stage's own document may use such a rule but may not restate it in its own words.

**Why.** Same passage, ARCHITECTURE.md:312-313: a cross-cutting contract restated in a layer document is a second copy that can drift (#6); a layer document may USE the span typology or the verifiability contract, not redefine them.

**Status.** LIVE · decided 2026-06-29 · ratifier not stated

**Home.** `ARCHITECTURE.md:562-563`

**Provenance.** ARCHITECTURE.md:308-316

### D-109 — The open-items register is the one home for every unresolved issue, and the index is the status of record

> this file is the complete INDEX and
> the **authoritative status surface**

**In plain words.** Every known unresolved problem has exactly one row in one file, and that row - not the longer write-up beside it - is the official statement of where it stands.

**Why.** Measurement, OPEN_ITEMS.md:3-5: the register was created after a full-repository sweep found 91 open items scattered across 12 tracking surfaces with 11 status contradictions.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `OPEN_ITEMS.md:5-10`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** OPEN_ITEMS.md:3-13; the standing rule is in CLAUDE.md 'The open-items register'

### D-110 — The decisions register records what was decided and its status - nothing else

> **The register holds WHAT WAS DECIDED, and its status. Nothing else.** The proposed
>    `conformance` field is REMOVED.

**In plain words.** This decisions register says what was decided and whether it still stands. Whether the code obeys it is tracked separately, in the open-items register, because those two things change on different clocks.

**Why.** Stated constraint, open_items/OI-208.md:49-54 (the user's recorded rationale): a decision's status changes only when someone rules again, whereas whether the code obeys it changes every time the code moves. Holding both in one row produces a register that silently goes stale - the exact failure the issue register was created to end.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `open_items/OI-208.md:48-49`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** open_items/OI-208.md:46-67 (SHAPE RATIFIED, three rulings)

### D-111 — A decision belongs in the owning layer's specification; the register is an index

> **A decision belongs, wherever possible, in the OWNING LAYER'S SPECIFICATION** — that layer's
>    section of `ARCHITECTURE.md` — and the register is the **index and pointer**, never a
>    substitute home.

**In plain words.** A decision about how a stage should work is written into that stage's part of the architecture document. This decisions register only points at it.

**Why.** Stated constraint, open_items/OI-208.md:55-62: the layer specification is where a reader looks for how a layer should work, so a register that held the decision instead of pointing at it would become a second home (#6) and the specification would stay silent.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `open_items/OI-208.md:55-57`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** open_items/OI-208.md:46-67; follows the CLAUDE.md Conventions rule of 2026-07-28

### D-112 — Never work from memory instead of documented facts

> No assertion, design, decision, dispatch or report may rest on recalled or
>   inferred content when a documented source exists. Open the primary source and cite it
>   (file:line).

**In plain words.** If a document records something, read it and quote it rather than remembering it. Being right from memory does not count, because correct memory and incorrect memory look the same until you check.

**Why.** Stated constraint, `CLAUDE.md` Conventions, with its founding instance recorded there: correct memory is indistinguishable from incorrect memory without checking, and the check is what surfaces the parts the memory did not contain - on 2026-07-28 the Layer-2 specification turned out to state explicitly and twice what had been reported as ambiguous.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `CLAUDE.md`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md Conventions, user-directed 2026-07-28; its founding instance is the Layer-2 note-collection reading that this adjudication's method is built to prevent

### D-113 — Music-theory words are reserved for their music-theory meaning

> Any term that coincides even slightly with music theory is used
>   ONLY in its musical sense.

**In plain words.** In this project a score is a piece of music, a key is a tonality, and a measure is a bar. Where a word is needed in its everyday computing sense, it must be qualified - candidate score, map key, measurement.

**Why.** Stated constraint, `CLAUDE.md` Conventions, user-directed 2026-07-28: this is a music-analysis system, so an ambiguous domain vocabulary makes every document harder to read and every specification easier to misapply.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `CLAUDE.md`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md Conventions, user-directed 2026-07-28; open_items/OI-229 records the convention STANDING for new writing and the tree-wide cleanup as an unratified future work item

### D-193 — The writing standards live in one place, and predicates must be qualified

> - **THE WRITING STANDARDS LIVE IN `cowork_design_doc_template.md` — read it before writing any
>   specification, design document, decision surface, or anything presented to the user.** Two
>   standards: **predicates must be qualified** (user, 2026-06-24 — every two-place word names its
>   argument; the mechanical check is to force the word to be followed by the thing it points at,
>   and a phrase the prose cannot supply is a hole), and **defined terms, plain vocabulary, no
>   shorthand** (user, 2026-07-02 — a terms table with nothing used before its row; no invented
>   synonyms; no insider compression, a jargon handle only after its rule has been stated; inherited
>   prose audited as hard as new). That file also carries the fourteen-section document structure,
>   the status-banner convention, and the implementation/test locator rule. It is the ONE home for
>   writing standards; the entry below sharpens its rule 5 and does not replace it (#6).

**In plain words.** Anything written as a specification, a design, a decision surface, or for the user follows two standards. Every word that relates two things must name the second one - the check is to force the word to be followed by the thing it points at, and a phrase the prose cannot supply is a hole in the thinking. And terms are defined before use, in plain vocabulary, with no invented synonyms and no insider shorthand.

**Why.** Stated constraint, CLAUDE.md:821-819: inherited prose is audited as hard as new prose, so the standard is about the document a reader meets rather than about who wrote which sentence. The one-home rule is #6 applied to the standards themselves (CLAUDE.md:820-821).

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `CLAUDE.md:1507`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:821-821; predicate qualification user-directed 2026-06-24, defined terms user-directed 2026-07-02. The ONE home is `cowork_design_doc_template.md`, which also carries the fourteen-section document structure, the status-banner convention and the implementation/test locator rule. Conformance of the existing tree is open at OPEN_ITEMS OI-230.

### D-194 — No self-invented labels, abbreviations, numbering schemes or jargon

> - **No self-invented labels, abbreviations, numbering schemes, or jargon** — in documents,
>   register rows, commit messages, and conversation alike. Use the name a thing already has
>   in the repository; if it has none, describe it in plain words. (User-directed, repeatedly;
>   recorded 2026-07-11.)

**In plain words.** A thing is called by the name it already has in the repository. If it has none, it is described in plain words rather than given a coined label - in documents, rows of the open-items register, commit messages and conversation alike.

**Why.** SEARCHED 2026-08-09 (CC, `cc_instruction_return_continuation_3.md` Task 2). The record holds no derivation. What the home states beside the rule is the STRENGTH of its provenance — user-directed "repeatedly", recorded 2026-07-11 — which says how firmly it is held, not why it holds. The rule's second clause states the REMEDY (use the name a thing already has in the repository; if it has none, describe it in plain words) rather than a ground. No cost of the practice it forbids is named at the home, and no alternative is considered.

**Status.** LIVE · decided 2026-07-11 · ratified by user

**Home.** `CLAUDE.md:1503`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:817-811, user-directed repeatedly and recorded 2026-07-11.

### D-195 — Every design decision carries its defense at its home

> - **EVERY DESIGN DECISION CARRIES ITS DEFENSE AT ITS HOME (user-directed, 2026-08-01, at the
>   decisions-register ratification review).** Wherever a design decision is recorded — the owning
>   layer's specification in `ARCHITECTURE.md` first — the record states WHY the decision was made:
>   the published research or algorithm adopted (#1/#2), the measurement that decided it, or the
>   constraint that forced it. Every design decision must be defendable, and its defense documented
>   where the decision lives. This generalizes `ARCHITECTURE.md` §17.2 (every non-obvious scoring
>   weight or threshold must explain its musical reasoning) from scoring values to design decisions
>   as a class. The decisions register (`DECISIONS.md`) points at the defense; where a decision's
>   derivation is not in the record, the register says **"derivation not recorded"** — the gap is
>   stated, never filled in retroactively from memory (a defense written after the fact without a
>   source is invention, and the never-work-from-memory rule forbids it). Founding instances of the
>   gap: the decode segment cap's value (4), the legacy 16-beats-back/8-forward window, the
>   boundary-tick-belongs-to-the-segment-it-starts convention — each recorded with no derivation.

**In plain words.** Wherever a design decision is written down - the owning layer's specification first - the record says WHY: the published research or algorithm it adopts, the measurement that decided it, or the constraint that forced it. Every design decision must be defendable and its defense written where the decision lives. Where the record has none, the decisions register says 'derivation not recorded' rather than supplying one afterwards.

**Why.** Stated constraint, CLAUDE.md:869-870: this generalizes ARCHITECTURE.md §17.2 - every non-obvious scoring weight or threshold must explain its musical reasoning - from scoring values to design decisions as a class. The reason the gap is stated rather than filled: a defense written after the fact without a source is invention, which the never-work-from-memory rule forbids (CLAUDE.md:873-874).

**Status.** LIVE · decided 2026-08-01 · ratified by user

**Home.** `CLAUDE.md:1583`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:873-876, user-directed 2026-08-01 at the decisions-register ratification review. The register's rationale field is what serves it; the founding instances the entry names are D-004's segment-cap value, D-059's window and D-015's boundary-tick convention.

### D-230 — The decisions register is a mandatory session-start read, and a new ruling lands in the register in the commit that records it

> (c) **a new ratification, shelving or falsification
> gets its register entry (data + regenerated files) IN the commit that records it**

**In plain words.** Every session must read the decisions index at its start, and whenever a decision is made, shelved or overturned, its register entry is part of the very commit that records the event - so rulings bind mechanically instead of by memory.

**Why.** The diagnosed root cause of the Stage-3.1b contradiction: decision history lived in archives outside the session-start read, so a later build contradicted a recorded ruling unknowingly (open_items/OI-208.md). The register existed as a snapshot; this rule is what makes it the living surface (#10 applied to decisions; #6 one home).

**Status.** LIVE · decided 2026-08-02 · ratified by user

**Home.** `CLAUDE.md`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling 2026-08-02 (the living-surface half of OI-208, all recommendations adopted); the CLAUDE.md decisions-register section + the session-start read list, edited in the same commit.

### D-255 — Every design document follows one fourteen-section structure, synthesized from three published standards

> **Standing convention (user, 2026-06-22):** every architecture/design document in this project follows the
> section structure below — a synthesis of **arc42** (the 12-section architecture template) and **IEEE 1016**
> (Software Design Descriptions) + the viewpoints idea of **ISO/IEC/IEEE 42010**. Two arc42 sections —
> **Deployment view** and **Human-interface design** — are **N/A** for our backend analysis modules (no separate
> hardware/runtime deployment; no UI); each doc states that omission once rather than padding.

**In plain words.** Every architecture or design document in this project uses the same section order, taken from arc42, IEEE 1016 and ISO/IEC/IEEE 42010. The two arc42 sections that do not apply to a backend analysis module - deployment view and human-interface design - are declared not applicable once per document instead of being padded out.

**Why.** The sources are cited with the decision: arc42 (the 12-section architecture template), IEEE 1016 (Software Design Descriptions) and the viewpoints idea of ISO/IEC/IEEE 42010 (cowork_design_doc_template.md:4-9) - published standards rather than an invented house style, which is principle #1 applied to documentation.

**Status.** LIVE · decided 2026-06-22 · ratified by user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_design_doc_template.md:3-7`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** cowork_design_doc_template.md:3 states it as a standing convention with the ratifier and date in the text. CLAUDE.md's Conventions entry names this file as the ONE home for writing standards and names this structure among what it carries, so the decision is correctly homed and was simply never in the register. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-256 — Every design document opens with one of four declared status banners

> ## Status-banner convention
> Each doc opens with a one-line status: **DRAFT for sign-off** / **SIGNED (date)** / **AS-BUILT (date + commits)** /
> **SUPERSEDED (→ pointer)**. The all-documentation-in-sync standing rule applies: when the code or a decision
> changes, the doc moves with it.

**In plain words.** A design document states its status in one line at the top: draft for sign-off, signed with a date, as-built with a date and commits, or superseded with a pointer to what replaced it. When the code or a decision moves, the document moves with it.

**Why.** Stated with the rule: it binds the all-documentation-in-sync standing rule (#10) to a visible per-document marker, so a reader can tell at a glance whether what they are reading is a proposal, a ratified contract, or a superseded record.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_design_doc_template.md:161-164`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** cowork_design_doc_template.md:75-78, stated as a convention in the file CLAUDE.md's Conventions entry names as the ONE home for writing standards; no date or ratifier is stated at this home. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-257 — A specification carries a locator to its code and tests; code mechanics never do the explaining

> straight from the architecture to the code and to the tests that protect it. The locator **stays** (user, 2026-06-24).
> What is *not* allowed is code **mechanics** doing explanatory work in the prose — function/type/variable names used to
> *explain the algorithm*, code formulas, or commit hashes woven into the reasoning. The line: the algorithm is
> described in plain architect/music-theory language; the *pointer to where it lives* is a short, clearly-marked
> reference, not prose.
> - **Implementation locator** — the headers and `.cpp` files — in Section 3 (Context & scope), as a labelled pointer.
> - **Test locator** — the unit-test file(s) and any corpus/property validation tool — in Section 10 (Quality &
>   testing).
> (Deferred for layers not yet built; added when they are. A layer mid-rebuild names its current location, marked as
> such. User mandate 2026-06-22, refined 2026-06-24.)

**In plain words.** A specification names the files that hold its implementation and the files that hold its tests, as a short labelled pointer, so a reader can go from the architecture straight to the code. What is not allowed is code mechanics doing the explanatory work: function, type and variable names used to explain the algorithm, code formulas, or commit hashes woven into the reasoning. The algorithm is described in plain architectural and music-theory language.

**Why.** The line is drawn in the rule itself (cowork_design_doc_template.md:84-86): a pointer to where something lives is a reference, while naming code to explain the algorithm makes the prose unreadable to the musician the documentation standard requires it to serve (register entry D-124, the readable-by-a-musician rule).

**Status.** LIVE · decided 2026-06-24 · ratified by user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_design_doc_template.md:170-179`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** cowork_design_doc_template.md:82 ('The locator stays (user, 2026-06-24)') and :91 ('User mandate 2026-06-22, refined 2026-06-24'). Homed in the file CLAUDE.md's Conventions entry names as the ONE home for writing standards, which names the implementation/test locator rule among what it carries. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-307 — A specification cites code by function or section anchor, never by raw line number

> **The locator's FORM: cite by function or by section anchor, never by a raw line number** (ruled 2026-07-02;
> homed here 2026-08-02 from `STATUS_ARCHIVE.md`, `OPEN_ITEMS.md` OI-272 — this is the writing standards' one
> home, and the locator rule above stated no constraint on the locator's shape). A specification points at

**In plain words.** When a design document points at the code, it names the function or the section, not the line. Line numbers go stale as soon as the file above them changes.

**Why.** The defect it answers is measured in the record: the gap analysis found stale line-number citations across the layer specifications, and the rule was made a policy at the same ruling that fixed them (`STATUS_ARCHIVE.md:242`).

**Status.** LIVE · decided 2026-07-02 · ratified by Cowork

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_design_doc_template.md:181-183`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** Recorded in `STATUS_ARCHIVE.md` (session 21e, the gap-analysis rulings). It is NOT in `cowork_design_doc_template.md`, which is the ratified home of the writing standards and states the implementation/test locator rule without this constraint on the locator's form — checked at the source. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue). ★ HOMED 2026-08-02 (CC, phase 1j, executing the user's per-kind ruling on [[OI-272]]): written into `cowork_design_doc_template.md` beside the implementation/test locator rule (D-257) it constrains. Homed THERE rather than in `CLAUDE.md` because `CLAUDE.md`'s own Conventions entry names that file the ONE home for the writing standards (#6), and the phase-1f entry recorded the gap as the locator rule stating no constraint on the locator's form. Former home preserved (#12): `STATUS_ARCHIVE.md:242`, session 21e.

### D-420 — One cross-layer extension specification, and the duplicate written the same day is killed into it

> extension behavior is specified → CODED → REGRESSION-TESTED for L1–L5. ★ CONSOLIDATION (same day, user directive
> against doc sprawl): the pre-existing `cowork_bounded_context_design.md` (DRAFT, never signed — found to already
> specify the request→supply→bounded-recompute protocol, superiorly: "the amount is discovered, not chosen",
> requester-owned convergence loops) is THE one cross-layer extension spec; the day's duplicate
> `cowork_temporal_extension_contract.md` is KILLED into it (merged: L5 discovery rule + PINNED decision-context
> extent [also folded into L5 spec §5.0], L4 decision-relevance sharpening, denial provenance, gate-proof framing,
> the §11 acceptance list = the L6 gate). Sequence: SIGN `cowork_bounded_context_design.md` → coding+test instruction

**In plain words.** Two documents were specifying the same thing — how a layer that has reached the edge of the music it has read asks for more. The older one was kept as the single specification, on the ground that it already stated the protocol better (the amount of extra music is discovered by convergence rather than chosen, and the layer that asked owns the loop), and the same-day duplicate was merged into it and removed.

**Why.** The stated ground is twofold and both halves are recorded: the user's directive against document sprawl, which is guiding principle #6 (one path per concern) applied to specifications rather than code; and a comparison of the two texts that found the surviving one superior on the substance — it already specified the request, supply and bounded-recompute protocol, with the amount discovered rather than chosen and the requester owning the convergence loop. The merge is recorded item by item, so nothing in the killed document was lost (#12).

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Entry ratified.** 2026-08-03 · by user

**Home.** `docs/implementation_roadmap.md:155`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `docs/implementation_roadmap.md`:113-119, recorded as a user directive of 2026-07-02, in the same block as the Layer-6 prohibition it accompanies (register entry D-266, whose home is the surviving document). The surviving specification `cowork_bounded_context_design.md` is a contract home under the fifth home case and carries seven register entries (D-260...D-266); the killed document `cowork_temporal_extension_contract.md` is named here with its merged contents enumerated. Found by the phase-1k continuation wave, 2026-08-03, reading `docs/implementation_roadmap.md` IN FULL (the OI-207 reading list's next document, 18 clusters). The document's own banner records it as the SINGLE TRACKER ensuring every review conclusion is addressed (`:4-8`); it carries none of the four declared status banners (register entry D-256), so it is not a contract home. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1k ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1l queue — ratified AS DRAFTED, with the status exactly as the record states it; the ratification is of each RULE itself, and it supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-424 — A decision surface names the principle behind every pro and con, and rates every option on two axes

> 1. *(second writing)* Every pro and con names the principle/rule/gate it rests on; every option
>    carries a two-axis rating — (a) principles/guardrails, (b) the ultimate objective,
>    **enabling the best possible inference (#4)**.

**In plain words.** When a choice is put to the user, each advantage and each disadvantage has to say which rule or principle makes it one, and every option is scored twice over: once against the rules and safeguards, and once against what the whole project is for — getting the analysis as right as it can be. An argument that names no rule is not an argument the surface may carry.

**Why.** The reason is the correction that produced it: the document's SECOND writing had to be rewritten because its pros and cons rested on grounds the surface never named, and unnamed grounds cannot be checked against the principles. It is the `CLAUDE.md` rule *every design decision carries its defense at its home* applied one step earlier — to the surface on which a decision is still being MADE — and the second axis exists because a design can satisfy every guardrail and still not be the one that analyses music best (#4), which is the axis the guardrails do not measure.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `cowork_notation_adoption_increment.md:18`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **the opening block (above the first section heading)** — `# The notation-layer adoption increment — decision surface (★ USER-RATIFIED 2026-07-26)` (heading at line 1). A delegation at ARCHITECTURE.md:7054 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_notation_adoption_increment.md`:17-20, the first of three rulings the document records the user making at its drafting, each dated 2026-07-26 and each given as a correction to a prior writing. Rulings 2 and 3 of the same list were codified as the decision-neutrality corollary and are registered as D-190, homed in `CLAUDE.md`; ruling 1 was not, and is registered here. Its natural home is `cowork_design_doc_template.md`, which `CLAUDE.md` Conventions makes the ONE home for the writing standards (the same reasoning that placed D-307 there), hence the documentation-gap flag. Found by the phase-1l continuation wave, 2026-08-03, reading `cowork_notation_adoption_increment.md` IN FULL (the OI-207 reading list's next document, 17 unresolved clusters). The document carries a status banner and is user-ratified 2026-07-26, but NO user-ratified surface names it — it is absent from `ARCHITECTURE.md`, `CLAUDE.md` and `cowork_engage_arc_plan.md` alike (measured this session at Task 7) — so it is not a contract home under either the phase-1i criterion or the delegation-specificity criterion the user ruled 2026-08-03. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1l ratification queue.

### D-430 — The contract-home criterion's unit is a SECTION of a document, not the document

> **(h) THE UNIT OF (g) IS A SECTION, NOT A
> DOCUMENT (user, 2026-08-03): a home is a SECTION of a document, admitted when a user-ratified
> surface delegates a stated concern to that section BY NAME and that section STATES RULES rather
> than recording findings.** The surrounding document's kind and its status banner are not the
> test. **GRANULARITY — stated explicitly so it is not re-interpreted (user, 2026-08-03, at the
> phase-1q whole-document reading): a delegation naming a DOCUMENT reaches ALL of its sections; a
> delegation naming SECTIONS reaches only those; and the rule-stating half is judged PER SECTION in
> both cases.**

**In plain words.** Whether a design document counts as the proper home of a decision is decided about the SECTION the decision sits in, not about the document as a whole. A section qualifies when a document the user has ratified points a named concern at that section by name, and when the section lays down rules rather than reporting what was found. What kind of document surrounds the section, and what its status banner says, do not enter the test. Where the pointer names the whole document and no section, it reaches every section of it; where it names sections, it reaches only those. Either way, whether a section lays down rules is asked section by section.

**Why.** Measured, at the case that refutes the document-level form. `ARCHITECTURE.md`:319 delegates the shipped-parameter licence-pool constraint to `cowork_score_census.md` §8c — a block that states three binding rules (the fitting-pool licence constraint, the intake rule, the supersession protocol) — inside a document whose kind is a census, so a test applied to the document excludes the block along with it. That case was found by the phase-1m measurement of the document-kind test, which reported it as the one structural finding the kind ruling did not answer (`OPEN_ITEMS.md` OI-281, second measurement note, §6). **The granularity clause's own defense, stated with it:** the strict reading — that a delegation must name a section or it admits nothing — would evict every document delegated as a whole, signed layer specifications among them, on the accident of how a pointer happens to be phrased, and would make this rule retroactively destructive rather than refining; it was ruled to let a SECTION be a home where the surrounding document is not, never to require every delegation to name sections.

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `CLAUDE.md:509`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-03 (the fifth ruling set of that date), applied at phase 1n; dispatch `cc_instruction_phase1n_criterion_premise_and_reading_regime.md` §2. **It SUPERSEDES, and does not falsify, the two tests that preceded it** — the delegation-specificity criterion ruled and measured earlier the same day (`OPEN_ITEMS.md` OI-281, first measurement note) and the document-kind test ruled and measured later the same day (same row, second note). Both were proxies for this test, and each produced the evidence that located its own error: the specificity criterion's residue turned out to be its third clause used as a judgment, and the kind test's residue turned out to be that kind is a property of the DOCUMENT while a delegation points at a SECTION. Recorded that way so a reader meets one derivation rather than three rival tests. **Applied STAGED, as the ruling directs:** only to the entries where section granularity decides something — the ambiguous population of the kind test plus the `cowork_score_census.md` entries, 46 entries across 5 documents — with everything else migrating as its document is next touched. The staging is stated in the register's own scope note (`header.scope.home_granularity`) so the mixed field cannot be misread. **The tooling cost was measured BEFORE any entry was changed, against a stop criterion declared in the dispatch before the diff existed (#22):** the change is confined to an additive per-entry field plus the generator and checker that read it; `home` itself is untouched, so the quote-verification path, the anchor check and the drift report are byte-unchanged and no existing anchor needed re-aiming. The section is DERIVED from the home document's own headings and the entry's own cited line by `tools/audit/decisions/gen_section_homes.py`, whose `--check` re-derives it, so no section is transcribed and none can go stale when a heading moves. Guard (g) is untouched: the delegation confers, and only the user writes a delegation into `ARCHITECTURE.md`. NOT RATIFIED as an ENTRY — it goes to the user in the phase-1n ratification queue. **THE STAGING ENDED 2026-08-03 (phase 1q):** the user ruled the criterion applied to the whole home population in one pass, so both halves — the delegation half and the states-rules half — now decide every entry the criteria reach, and the register's home field is no longer of mixed granularity. The applier is `tools/audit/decisions/gen_home_classification.py`, which replaces `gen_section_homes.py` (two appliers of one criterion is the duplication #6 forbids). How a WHOLE-DOCUMENT delegation is read — it reaches every section — was, at phase 1q, an interpretation of this ruling's *BY NAME* clause, taken on the record's own precedent at `OPEN_ITEMS.md` OI-290 and recorded, with the strict alternative it rejects, at `backbone_decisions.json` → `section_home_criterion.whole_document_reading`. **THE VERBATIM ABOVE WAS RE-TAKEN 2026-08-03 (phase 1r), because the user WROTE THAT INTERPRETATION INTO THE RULE.** The GRANULARITY clause — a delegation naming a document reaches all its sections, a delegation naming sections reaches only those, and the rule-stating half is judged per section in both cases — was ruled by the **user on 2026-08-03** at the phase-1q whole-document reading and written into `CLAUDE.md` rule (h) itself. It is recorded here as a **SCOPE CLARIFICATION of this decision, not as a separate decision**, and deliberately gets no sibling entry (#6): it fixes what this ruling's own *BY NAME* clause reaches when a delegation names no section, introduces no new criterion, changes nothing about which surfaces may delegate (that is D-432), and reaffirms rather than alters the states-rules half. What it does change is the record's option space — before it, the strict alternative was recorded as available to the user; after it, the strict reading is closed. **The verbatim this replaces, preserved (#12):** *"**(h) THE UNIT OF (g) IS A SECTION, NOT A DOCUMENT (user, 2026-08-03): a home is a SECTION of a document, admitted when a user-ratified surface delegates a stated concern to that section BY NAME and that section STATES RULES rather than recording findings.**"* — the same opening sentence, ending at *recording findings*, without the kind/banner sentence and without the granularity clause. **CONFIRMED BY THE USER, 2026-08-04 (`OPEN_ITEMS.md` OI-326, ruling R4).** BOTH halves are required and the KIND half is DECISIVE: a well-formed delegation to a section that RECORDS FINDINGS rather than STATES RULES admits nothing, and the halves are applied in that order — form first, kind second and last. Recorded as a confirmation of this entry rather than an extension of it, and written into the rule text at `CLAUDE.md` rule (k2) so it is not asked again — see **D-546**. The case that raised it: `ARCHITECTURE.md` names `cowork_evidence_inventory.md` in a subject-is-X form whose predicate delegates, over a document whose own §9 says in terms that nothing in it is a build decision.

### D-432 — What counts as a delegation, graded by form — the clause the section-level criterion did not touch

> **(i) WHAT COUNTS AS A DELEGATION, GRADED BY FORM (user, 2026-08-03).**
> (h) turns on a user-ratified surface DELEGATING a stated concern to a section; (i) fixes which
> wordings do that, and it is the clause (h) deliberately did not touch. **ADMITTED:** an **explicit
> delegation clause** — *"The ratified contract for this layer is X"*, *"The ONE detailed cross-layer
> spec for this contract is X"*, *"formalised as an independent knowledge-base component with its own
> spec (X)"* — or **a named home with sections** — *"Criterion + build home: X §0/§5.3"*. **NOT
> ADMITTED:** a **bare appended citation** — *"Full spec: X."* — or a **provenance attribution**,
> meaning a naming inside a list of citations, or a parenthetical recording where something was
> ratified.

**In plain words.** For a design document to count as the proper home of a decision, some document the user has ratified must DELEGATE a concern to it — and this says which wordings do that. Naming the document as the contract, the spec or the build home for something counts, and so does naming it together with the sections it owns. Merely citing it at the end of a paragraph, listing it among sources, or noting in passing where a ruling was made does not.

**Why.** The canonical document distinguishes the two acts in ADJACENT LINES, and both are quoted from the file in `tools/audit/decisions/phase1p_delegation_bar.json` → `the_defense`: one line ends *"Full spec:"* and names its target on the next, and the line immediately beneath it is a delegation clause naming its target and its sections. The distinction is `ARCHITECTURE.md`'s own, not a preference. The question this settles is the one phases 1l, 1m and 1n each measured and each left open, and which the phase-1m measurement identified as the dominant remaining source of ambiguity (`OPEN_ITEMS.md` OI-281, second measurement note, §4).

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `CLAUDE.md:536`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-03 (the seventh ruling set of that date, W2 — 'grade the forms and set the bar'), homed at phase 1p as rule (i) of the decisions-register section, beside (g) and (h) which it completes. **RECORDED AT PHASE 1p, APPLIED AT PHASE 1q.** The dispatch ordered a check before applying it — *does this bar change the verdict for any document the register currently classifies `contract-home`?* — and predicted no, on the ground that the admitted set was reached on explicit delegation clauses. The check was run in a generator (`tools/audit/decisions/gen_phase1p_delegation_bar.py` → `pre_apply_check`) and the prediction is **REFUTED**: the bar excludes documents the register currently admits. Under the dispatch's own instruction that is a #13 STOP, so no entry's home class was changed and the non-conformance is rowed at `OPEN_ITEMS.md` OI-291. The generator applies nothing — it only reads the backbone. NOT RATIFIED as an ENTRY — it goes to the user in the phase-1p ratification queue. **APPLIED 2026-08-03 (phase 1q, the user's ruling of that date, option A3):** the user ruled ONE re-classification pass over the whole home population rather than a forward-only migration or a revision of the bar, with a WRITE LIST for the homes the record means to keep. The pass is `tools/audit/decisions/gen_home_classification.py` → `home_classification.json`; its `totals` carry the movement and its `write_list` the drafted delegations, which go to the user because only the user writes one. (Both pointers in this field formerly named `phase1q_reclassification.json`, which was REMOVED on 2026-08-09 under the user's Ruling 1 — it held neither the phase-1q record nor the present classes; the record is at the established snapshot and the live view at the file named here, whose blocks are unchanged. See `section_home_criterion.scope_of_application` for the full removal note, which is not restated here, #6.) `OPEN_ITEMS.md` OI-291 flips with that provenance. **THE WRITE LIST CAME BACK WRITTEN, 2026-08-03 (phase 1r).** The user wrote a delegation for each of the six documents the pass emitted, and the pass was re-run against them: all six move, two only in part (`tools/audit/decisions/phase1q_reclassification.json` -> `the_phase_1r_re_run`; `OPEN_ITEMS.md` OI-293 closes). The bar itself is unchanged — what changed is the wordings it reads, which is the outcome the ruling was designed to produce. The pre-apply check still reports STOP over the same three documents: four delegation grades moved today, so the grades the check was run against are frozen at `gen_phase1p_delegation_bar.py` -> `GRADE_AT_PHASE_1P` while `FORMS` stays live for the classifier (#12, and one live grade with one home, #6). **This entry's own defense now cites two line numbers that have moved** — the same act shifted `ARCHITECTURE.md`, and no tool re-aims a line number quoted inside a rule's prose; carried at `OPEN_ITEMS.md` OI-294. **CORRECTED BY THE USER'S RULING, 2026-08-03 (phase 1s, Y2 — option 1B): the defense is CONVERTED FROM LINE NUMBERS TO A DESCRIPTION.** The rule's *Why:* clause now says that one line ends *"Full spec:"* and names its target on the next, and that the delegation clause immediately beneath names its target and its sections — the same evidence, stated so that nothing in it can drift. The reason is written into the rule text because it generalizes: a line number quoted inside a rule's PROSE is not a register anchor, so `reaim_home_anchors.py` cannot maintain it and it goes stale on the next insertion above it. **The FORMER wording is preserved here (#12):** "*Why:* the canonical document distinguishes the two acts in ADJACENT LINES — `ARCHITECTURE.md:1482` ends *\"Full spec:\"* and names its target on the next line, while `:1485` immediately beneath is a delegation clause that names its target AND its sections. The distinction is `ARCHITECTURE.md`'s own, not a preference." **This entry's VERBATIM did not need re-taking and was not re-taken**, which is stated rather than glossed: the quoted block ends at *"…a parenthetical recording where something was ratified."*, and the corrected *Why:* clause sits immediately BELOW it, outside the quote. The `rationale` field above already carried the description form (it cites `tools/audit/decisions/phase1p_delegation_bar.json` → `the_defense`, generated), so it needed no change either. `OPEN_ITEMS.md` OI-294 flips. **CONFIRMED BY THE USER, 2026-08-04 (`OPEN_ITEMS.md` OI-326, ruling R3).** Where a document is named in BOTH an admitting and an excluded form, the STRONGEST NAMING GOVERNS: being cited elsewhere in a weaker form does not undo a delegation. The user's act records this as a confirmation of this entry rather than an extension of it, and it is written into the rule text at `CLAUDE.md` rule (k1) so it is not asked again — see **D-546**. The collision that raised it: the canonical document's opening banner names `cowork_joint_estimator_architecture.md` as where a user-ratified GOVERNING DECISION is read, while a later line names the same document as *"spec: …"*, this bar's not-admitted example word for word.

### D-433 — A shelved section can be a home — shelving is a status, not a kind

> **A SHELVED SECTION CAN BE A HOME — SHELVING IS A STATUS, NOT A KIND (user, 2026-08-03).** A
> section whose rules are shelved still STATES rules, and the register records shelvings with their
> evidence, so a shelved decision needs a home exactly as a live one does (#12).

**In plain words.** A section of a document does not stop being the proper home of a decision because the work it describes was shelved. The kind test asks what a section DOES — state rules, or report findings — and a shelved banner does not change that. Shelved decisions are kept with their evidence, so they need a home just as live ones do.

**Why.** Stated with the ruling: the kind half of the section-level criterion asks what a section DOES, and a status banner does not change that. It also closes a residue the record was still carrying — the phrase *"stable enough to be cited"*, a clause of the superseded delegation-specificity criterion which survived in the tracking prose after the section-level ruling replaced it, and which would otherwise have invited a fourth criterion (`OPEN_ITEMS.md` OI-281, first measurement note, §4).

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `CLAUDE.md:530`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-03 (the seventh ruling set of that date, W3), homed at phase 1p inside the decisions-register section's rule (h), whose kind half it clarifies. **Its one candidate application did NOT follow**, and the reason is recorded rather than left implied: the document it would have admitted, `cowork_joint_key_chord_design.md`, is delegated only by a parenthetical naming inside a bulleted list (`cowork_engage_arc_plan.md:44`), which **D-432** does not admit — so the four entries homed there stay `gap` for a different reason than the one this ruling removes. NOT RATIFIED as an ENTRY — it goes to the user in the phase-1p ratification queue.

### D-435 — Delegating to a document and being a home are different tests with different subjects

> **(j) DELEGATING TO A DOCUMENT AND BEING A HOME ARE DIFFERENT TESTS WITH DIFFERENT SUBJECTS (user,
> 2026-08-03).** To DELEGATE, a surface must itself be user-ratified; to BE a home, a section must be
> delegated to. A document may satisfy one and fail the other, and neither role implies the other. So
> `cowork_engage_arc_plan.md` — a user-ratified surface the criterion USES as a source of delegations
> — is not a delegation TARGET BY THAT FACT: whether any section of it is a home turns on the separate
> question of whether some user-ratified surface delegates a concern to it in a form (i) admits, which
> is answered by reading the delegations that exist and never by the document's standing as a source.
> *Why:* the question was asked in exactly that form, and the two roles had been running together in
> the tracking prose; stating them apart is what keeps (i) a mechanical test rather than one with a
> case-by-case exception.

**In plain words.** Two questions about a document are often run together and are not the same. Whether a document may DELEGATE a concern to another depends on whether the user ratified that document. Whether a document may BE the home of a decision depends on whether some user-ratified surface delegates a concern to it, in a wording the delegation bar admits. A document can pass one test and fail the other, and passing the first never confers the second.

**Why.** The question arose in exactly this form and had to be answered before the delegation bar could be applied: `cowork_engage_arc_plan.md` is one of the three user-ratified surfaces the contract-home criterion reads delegations FROM, and the collision to resolve was whether that standing made it a delegation TARGET as well. Stating the two roles apart is what keeps the bar a mechanical test: the alternative on the table was an exception for this one document, and a mechanical test with a case-by-case exception is not a mechanical test. What the ruling settles is the SHAPE of the answer — read the delegations that exist, in the forms D-432 admits — and not any particular document's standing, which is a fact that can change and did: the user then wrote a delegation for this document (the OI-293 write list), and it became a home by being delegated to, which is the rule working rather than an exception to it.

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `CLAUDE.md:559`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-03 (the eighth ruling set of that date, X2 — 'draft a proper delegation rather than an exception'), homed at phase 1q as rule (j) of the decisions-register section, beside (g), (h) and (i) whose interaction it fixes. It resolves the collision the phase-1p wave reported and did not settle: that wave's own §4 ordered `cowork_engage_arc_plan.md`'s three entries ADMITTED on the test *names it by name for a stated concern*, while **D-432** excludes that naming as a provenance attribution. **The bar governs and the phase-1p §4 admission is superseded on this point**, recorded rather than dropped; the remedy for the arc plan is a drafted delegation on the phase-1q write list (`tools/audit/decisions/home_classification.json` → `write_list`), which goes to the user because only the user writes a delegation. (This pointer formerly named `phase1q_reclassification.json`, REMOVED on 2026-08-09 under the user's Ruling 1; the removal note is at `section_home_criterion.scope_of_application` and is not restated here, #6.) NOT RATIFIED as an ENTRY — it goes to the user in the phase-1q ratification queue. **THIS ENTRY'S RATIONALE IS STALE AT HEAD, and is left standing rather than rewritten (2026-08-03, phase 1r).** It says the bar excludes `cowork_engage_arc_plan.md` as a delegation TARGET "because the only naming of it is inside a list of citations (`CLAUDE.md:129-130`)" — true when the ruling was made, and no longer true: on the user's direction the OI-293 write list wrote an explicit delegation clause into `CLAUDE.md` for exactly this document, so its three entries are now `contract-home`. **The RULING is untouched by that** — (j) says delegating and being a home are different tests, and the arc plan became a home by being delegated to, which is the rule working rather than an exception to it. What is stale is the verbatim's closing clause, *"and today none does"*, a factual statement inside user-ruled text that this session may not edit; it is rowed at `OPEN_ITEMS.md` OI-294 for the user. **CORRECTED BY THE USER'S RULING, 2026-08-03 (phase 1s, Y2 — option 1B).** The user ruled the stale clause struck and this rationale re-taken. The verbatim above is RE-TAKEN from the corrected rule text, which now says the arc plan is not a delegation target BY THE FACT of being a source and that the home question is answered by reading the delegations that exist — a statement of what the two tests ARE, carrying no present-tense claim about any document's current standing, so it cannot go stale the same way again. **The FORMER verbatim clause is preserved here (#12):** "— is not thereby a delegation TARGET: whether any section of it is a home turns on whether some user-ratified surface delegates a concern to it in a form (i) admits, and today none does." **The FORMER rationale is preserved here (#12):** "The question arose in exactly this form and had to be answered before the delegation bar could be applied: `cowork_engage_arc_plan.md` is one of the three user-ratified surfaces the contract-home criterion reads delegations FROM, and the bar excludes it as a delegation TARGET, because the only naming of it is inside a list of citations (`CLAUDE.md:129-130`). Stating the two roles apart is what keeps the bar a mechanical test: the alternative on the table was an exception for this one document, and a mechanical test with a case-by-case exception is not a mechanical test." The RULING is untouched by either correction.

### D-499 — RATIFIED AMENDMENT A-10: four documentation riders — a consolidated ownership page for the notation-derived views, the membership tie-breaker recorded as idiom-calibrated, and the producer-agnostic seam pinned as a design property

> - **A-10 (from F-4, F-12, F-17, F-18). Doc riders**: L1.5 consolidated ownership page; record the membership
>   tie-breaker as an idiom-calibrated constant; pin B-swap readiness as a design property; (optional) STATUS entry
>   header schema.

**In plain words.** Four small documentation debts, ratified together: the notation-derived view layer owns several things and has no one page saying so; the rule that breaks a tie about whether a note belongs to the chord is calibrated to one style and is not recorded as such; the property that a learned component could be dropped in where the hand-built one sits is currently true but written down nowhere; and the status file's entry format is hard to read.

**Why.** Each rider is stated with the finding that produced it: the notation-derived view layer is described across three documents with no consolidated statement (F-4); the one-sided membership tie-breaker inverts between the chorale convention and appoggiatura-normative styles, so it is a per-idiom constant rather than a universal rule (F-12); the producer-agnostic seams that keep a learned emission swappable hold today and are pinned nowhere, so nothing prevents a future change from closing them (F-18).

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_architecture_review_2026_07.md:336-338`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§9** — `## 9. Proposed amendments (ranked; each ratification-gated; none is code)` (heading at line 307). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** Amendment A-10 of the external architecture review, in a document whose banner records amendments A-1…A-10 as RATIFIED by the user on 2026-07-02; the review marks the fourth rider optional. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) ★ NOT A FRESH DECISION, stated so that nothing is counted twice (dispatch cc_instruction_reads_3.md §1.3): the amendment itself was ratified by the user at the 2026-07-02 architecture review, which is what this entry's Status line already records. Ratifying the ENTRY records only that the register transcribes that ratification correctly — it neither re-makes the decision nor adds a second ratification event to it.

### D-546 — A delegation reaches only the members it names explicitly — a glob and a trailing ellipsis confer nothing; with the two confirmations ruled beside it

> **(k) A DELEGATION REACHES ONLY THE MEMBERS IT NAMES EXPLICITLY — AND TWO CONFIRMATIONS THAT CLOSE
> THE QUESTIONS ASKED WITH IT (user, 2026-08-04, at `OPEN_ITEMS.md` OI-326).** `ARCHITECTURE.md`'s
> doc-governance hierarchy clause — the one naming the per-layer and per-component design documents as
> the authoritative detail for their own scope — **IS a delegation under (i), but it delegates only to
> the members it names EXPLICITLY. A glob pattern and a trailing ellipsis CONFER NOTHING.** *Why:* a
> delegation whose membership is indeterminate could be extended by a session, and extending a
> delegation is the authority (g) reserves to the user; a glob is satisfied by any file a later commit
> happens to name that way, and an ellipsis by anything at all. **This APPLIES (i)'s logic rather than
> amending it — (i) is unchanged, and so is D-432.** Two confirmations, ruled in the same act and
> written here so that neither is asked again. **(k1) WHERE A DOCUMENT IS NAMED IN BOTH AN ADMITTING
> AND AN EXCLUDED FORM, THE STRONGEST NAMING GOVERNS**; being cited elsewhere in a weaker form does not
> undo a delegation. **(k2) (h) REQUIRES BOTH HALVES AND THE KIND HALF IS DECISIVE**: a well-formed
> delegation to a section that RECORDS FINDINGS rather than STATES RULES admits nothing, and the halves
> are applied in that order — form first, kind second and last. **What (k) leaves out is settled
> through the OI-293 WRITE LIST, never by reading the clause more generously:** a delegation the user
> writes settles that document without touching the bar. *Measured before it was applied, on the
> user's own condition:* how much of the population the split moves was measured first, and the split
> moves nothing — the enumeration, the reasoning and every count are generated at
> `tools/audit/decisions/reads4_oi326_application.json`, and no figure is restated here (#17f, D-431).

**In plain words.** ARCHITECTURE.md's doc-governance clause, which names the per-layer and per-component design documents as the authoritative detail for their own scope, does delegate — but only to the documents it names by filename. The wildcard pattern and the trailing '…' in its list hand nothing to anyone, because a list whose membership is open could be extended by whoever is reading it, and only the user may extend a delegation. Two related points were confirmed at the same time: when a document is named both strongly and weakly, the strongest naming wins; and a delegation to a section that merely records findings admits nothing, however well worded the delegation is.

**Why.** Stated with the ruling: a delegation whose membership is indeterminate could be extended by a session, and extending a delegation is the authority rule (g) reserves to the user — a glob is satisfied by any file a later commit happens to name that way, and an ellipsis by anything at all. The ruling was also made CONDITIONAL on a measurement rather than applied on the reading: the user required that the population the split moves be measured BEFORE the split landed, with a report-and-stop if it were large (#19). It was measured and it moves nothing — the enumeration and every count are generated at `tools/audit/decisions/reads4_oi326_application.json`, and the reason is in that artifact: every glob-matched and prose-referenced member of the clause was already graded on the STRONGEST naming it has, which for four of them is an explicit delegation clause of their own and for the rest is a form the bar excludes anyway. Only the explicitly-named members were ever graded on this clause, and the ruling keeps exactly those.

**Status.** LIVE · decided 2026-08-04 · ratified by user

**Home.** `CLAUDE.md:575`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-04 at `OPEN_ITEMS.md` OI-326, transmitted in the read-wave-4 dispatch `cc_instruction_reads_4.md` §0a as R1 (the ruling), R2 (the residue goes to the OI-293 write list), R3 and R4 (the two confirmations) and R5 (the measurement condition); homed here as rule (k) of the decisions-register section, beside (g)–(j) whose logic it applies. **(k1) AND (k2) ARE CONFIRMATIONS, NOT NEW DECISIONS.** (k1) — the strongest naming governs — confirms **D-432** and adds nothing to it; (k2) — both halves required, the kind half decisive and applied second — confirms **D-430** and adds nothing to it. Both are written into the rule text so that neither is asked a third time, and both are recorded in the provenance of the entry they confirm; they are carried in this one entry rather than given entries of their own because a register entry restating a decision another entry already holds is the duplication #6 forbids. **WHAT THE RULING DID NOT DO:** it settled no document that the clause reaches by glob, by prose reference or by ellipsis — those go to the OI-293 write list with a drafted delegation each, for the user to write or reject — and it moved no entry's home class, `gen_home_classification.py`'s apply mode staying UNRUN under `OPEN_ITEMS.md` OI-305 / OI-319.

### D-652 — How the decisions register's same-commit rule is discharged once it has already been missed

> **★ HOW RULE (c) IS DISCHARGED ONCE IT HAS ALREADY BEEN MISSED (user-ruled 2026-08-09; the ruling
> record is `cowork_rulings_2026_08_09_second_stop.md`, Ruling 12).** Rule (c) says a new ratification,
> shelving or falsification gets its register entry IN the commit that records it. It does not say what
> happens when a run of rulings has accumulated OUTSIDE the register — which is the state the rule is
> meant to prevent and, once reached, a state the rule alone does not resolve. **The discharge is: the
> accumulated rulings are CLASSIFIED first — per ruling, is this a DECISION the register carries, or
> the exercise of one it already holds — the classification is put to the user as a reading file, and
> the entries then land in ONE COMMIT, late but by the same pattern every on-time register event uses.
> No entry is written before the user rules on the classification.**

**In plain words.** The register's rule is that a new ruling gets its entry in the same commit that records the ruling. When that has already been missed and several rulings have piled up outside the register, the way back is: classify each one first — is it a decision the register should carry, or the exercise of a decision it already holds — put the classification to the user, and then write all the entries in one commit. Nothing is written before the user rules.

**Why.** It closes a shape rule (c) does not itself cover: the rule prevents the state, and once the state is reached the rule alone does not resolve it. Two alternatives are named and forbidden with their reasons — retro-fitting entries ruling by ruling as later dispatches happen to touch them, which leaves the register's completeness depending on what came up next; and abandoning the debt on the ground that every ruling's content is already on disk in a ratified record, which is true and beside the point. What is at risk when rulings sit outside the register is not the rulings but the register's claim to be the one place a session learns what was decided, which is what rule (a) makes a session rely on.

**Status.** LIVE · decided 2026-08-09 · ratified by user

**Home.** `CLAUDE.md:651-665`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-09, Ruling 12 of `cowork_rulings_2026_08_09_second_stop.md` ("Agree with updated recommendations"), whose queue was drafted by `cc_instruction_return_continuation_2.md` Task 1 and extended by `cc_instruction_return_continuation_3.md` Task 0. CLASSIFIED as a DECISION by the user's Ruling 20 of 2026-08-09 (`cowork_rulings_2026_08_09_fourth_stop.md`), queue entry 12, which the queue itself put BOTH WAYS with the downgrade reading given — that as a procedure it is the author-then-review pattern again — and which the user ruled KEPT as a decision, the cheaper insurance. Homed by that same ruling in `CLAUDE.md`'s decisions-register section beside rule (c), the site the queue named; it is written as a marked block at the end of that section, which is the idiom that section already uses for a clause qualifying one of its lettered rules. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14). Cross-ref D-230 (rule (c) itself), D-655 (the other clause that governs when a register-clearing act may be performed).

### D-659 — Document-structure conformance is kind-scoped, and the kind list is enumerated with a STOP on an unlisted kind

> ## Which documents the section structure binds — the KIND LIST (user, 2026-08-09)
>
> The fourteen sections above are a **design-description** standard: arc42 and IEEE 1016 describe how a
> built or planned component is documented. They therefore bind **specifications and design documents**,
> and the project's **working genres are exempt as different genres** — not as unjudged gaps. The list
> below is the enumeration, and it is what a conformance check reads.

**In plain words.** The fourteen-section document structure binds specifications and design documents only. The project's working genres — dispatches, ruling records, ratification queues, returns files, status and handoff surfaces, registers, reports, procedures and inventories — are exempt because they are a different genre, not because anyone failed to write them properly. The list of kinds is enumerated in the writing-standards document, and a document of an unlisted kind stops the conformance check instead of passing it quietly.

**Why.** The structure's own basis is a design-description standard (#1/#2), so applying it to a dispatch or a ruling record would judge those documents against a standard written for something else — and reading the resulting non-conformance as a gap would make the whole conformance question unanswerable. The STOP on an unlisted kind is what keeps the exemption from widening by silence: without it, 'exempt' is whatever a session decides a document is. The membership list is maintained the way the guard population is — a kind is added by a user ruling, in the commit that records it, with the reason it is a different genre.

**Status.** LIVE · decided 2026-08-09 · ratified by user

**Home.** `cowork_design_doc_template.md:75-80`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-09, Ruling 28 of `cowork_rulings_2026_08_09_fifth_stop.md`, which names `cowork_design_doc_template.md` as the kind list's home in its own words and licensed the section; the section was written by `cc_instruction_return_continuation_5.md` Task 0, in that document's own voice, together with the clause the ruling implies rather than states — that the two WRITING standards and the status-banner convention are NOT kind-scoped and bind every document, exempt genres included, only the fourteen-section structure being scoped. CLASSIFIED as a DECISION by the user's Ruling 36 of 2026-08-09 (`cowork_rulings_2026_08_09_sixth_stop.md`), queue §7 entry 28, on the ground that it is a standing rule with a maintained membership list and a failure mode, none of the three being in the register. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14). Cross-ref D-193 (the writing standards and their one home), `OPEN_ITEMS.md` OI-230 (the deferred conformance question this answers) and OI-364 (the owed mechanical check, whose structure test reads this list).

### D-660 — A research-tied name is not renamed but is governed by a two-tier rule, and the terminology cleanup runs in a fixed order with no tree-wide rename

> **★ WHAT HAPPENS TO A NAME BORROWED FROM THE PUBLISHED RESEARCH, AND IN WHAT ORDER THE CLEANUP
>   RUNS (user-ruled 2026-08-09; the ruling record is `cowork_rulings_2026_08_09_fifth_stop.md`,
>   Ruling 30).** The block above says the existing tree is not renamed unilaterally and that the
>   pass is a decision surface rather than a sweep. It does not say what a session does with a term
>   that carries correspondence to the research the design is grounded in, and it does not fix the
>   order — both are settled here. **A RESEARCH-TIED NAME IS NOT RENAMED (#1/#2), AND IS GOVERNED BY
>   TWO TIERS.** *(i)* At the **INTRODUCTION SITE** — where the public research is actually
>   discussed, which is expected to be one or very few places — the collision is EXPLAINED and our
>   decided synonym STATED; the term standing there with that statement is conformant. *(ii)* **Every
>   subsequent use** of the research term outside our own vocabulary carries a **compact inline
>   annotation referencing the research**; such a use is conformant if and only if it is annotated,
>   and an **unannotated repeat use is a flag**.

**In plain words.** A term borrowed from the published research that collides with this project's vocabulary is not renamed. Instead: where the research is actually discussed, the collision is explained and our own synonym stated; and every later use of the borrowed term outside our vocabulary carries a short inline note pointing at the research, so an unannotated repeat use is a flag. The wider terminology cleanup runs in a fixed order — the derived inventory first, then per-word batches the user rules, governing surfaces first — and there is no tree-wide rename.

**Why.** The second tier is the load-bearing half: a rule stated as 'research terms are not renamed' and nothing else reads as a licence to leave them bare, which reproduces the ambiguity the whole convention exists against, since the reader who meets the term at its fiftieth use never meets the introduction site. The order half is what keeps the cleanup a scoped decision surface rather than a sweep — which is what the surrounding convention had already ruled it must be, because some names carry correspondence to the published research the design is grounded in (#1/#2), so each class is a named decision rather than a mechanical pass.

**Status.** LIVE · decided 2026-08-09 · ratified by user

**Home.** `CLAUDE.md:1558-1569`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** User ruling of 2026-08-09, Ruling 30 of `cowork_rulings_2026_08_09_fifth_stop.md`, whose two-tier test for research-tied names is the user's own; recorded on `OPEN_ITEMS.md` OI-229's row by `cc_instruction_return_continuation_5.md` Task 0, which stays OPEN because the cleanup itself is not done. CLASSIFIED as a DECISION by the user's Ruling 36 of 2026-08-09 (`cowork_rulings_2026_08_09_sixth_stop.md`), queue §7 entry 30, on the ground that nothing in the register says what a session may do with a research-tied name while #1/#2 make those names load-bearing. Homed by that same ruling in `CLAUDE.md`'s Conventions reserved-word block beside the disambiguation convention — the site the queue named, and a USER-ONLY text the ratification is the scoped licence for — written in that block's own voice, provenance here and never in the convention text. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14). Cross-ref D-113 (the reserved-vocabulary convention it completes), D-661 (the completeness rule governing the inventory it orders), D-431 (why the inventory's counts stay in the artifact).

### D-662 — Every open-items index status cell begins with one canonical token, with a lint and a parser STOP behind it

> **★ RULE (f) — EVERY INDEX STATUS CELL BEGINS WITH ONE CANONICAL TOKEN (user-ruled 2026-08-09; the
> ruling record is `cowork_rulings_2026_08_09_fifth_stop.md`, Ruling 33).** Rules (a)–(e) above say
> how the register is kept. This is the sixth, and it is about the one cell three separate derivations
> read. **A row's STATE is carried by the first token of its status cell — the resolved mark at the
> head of the cell, or one of the open-state words — and by nothing else.** Two consequences follow
> immediately and both are the point of the rule: a cell may **name any other row's resolution
> freely**, in words or with the mark, because a mention anywhere after the opening is inert; and a
> resolution spelled **only in prose**, with no canonical opening, **is not a state** and will be
> counted open until the opening is written.

**In plain words.** Every status cell in the open-items index starts with one canonical token — the resolved mark, or one of the open-state words — and a row's state is read from that token alone. So a cell may mention any other row's resolution freely, and a resolution written only in prose does not count as a state. A lint reports every non-canonical opening, and the single index parser stops on a row that does not split into six cells instead of skipping it.

**Why.** One cause with three faces, each found separately: a cell mentioning another row's mark made its own row read resolved to every derivation; a cell stating its resolution in words read open although its text said otherwise; and a malformed row was dropped silently into no population at all. The silent drop is the worst of the three, because a mis-read row is at least counted somewhere and a moving count can be noticed — which is why the parser stops rather than skips (#12, #19). The two excluded alternatives are recorded at the ruling: recognising a resolution token anywhere in a bounded opening, which is a hand-picked threshold over varying prose and fixes neither sibling, and forbidding the mark in prose, which is one symptom of three.

**Status.** LIVE · decided 2026-08-09 · ratified by user

**Home.** `CLAUDE.md:410-418`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-09, Ruling 33 of `cowork_rulings_2026_08_09_fifth_stop.md`, over the family `OPEN_ITEMS.md` OI-356 / OI-361 / OI-362; executed by `cc_instruction_return_continuation_5.md` Task 1, whose normalization pass was gated by the both-ways condition D-657 records and which found a fourth member of the family in the process. CLASSIFIED as a DECISION by the user's Ruling 36 of 2026-08-09 (`cowork_rulings_2026_08_09_sixth_stop.md`), queue §7 entry 33, on the ground that it binds every row anyone writes into the index from now on. Homed by that same ruling in `CLAUDE.md`'s open-items register section beside rule (d) — the site the queue named, and a USER-ONLY text the ratification is the scoped licence for; the queue's stated alternative home, `OPEN_ITEMS.md`'s own preamble, was NOT taken because that preamble restates these rules rather than owning them (#6), and it carries a pointer instead. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14). The vocabulary, the row split and the leading-token test have one home at `tools/audit/index_status_lint.py` and no token or count is restated (D-431). Cross-ref D-230 (the register's rules (a)-(e)), D-436 (the mechanism-change reservation the remedy was licensed under), D-657 (the both-ways condition the pass ran under).

### D-664 — Re-homing is the default closing route where no delegation admits an entry's home, and only the user may except a document — before its entries are re-homed, never after

> **(l) WHERE NO DELEGATION ADMITS AN ENTRY'S HOME, RE-HOMING IS THE DEFAULT CLOSING ROUTE — AND WHO
> MAY EXCEPT A DOCUMENT FROM IT, AND WHEN (user-ruled 2026-08-09; the ruling record is
> `cowork_rulings_2026_08_09_sixth_stop.md`, Ruling 38).** Rules (g)–(k) decide which documents and
> sections are homes. This is the rule they lack: what closes an entry whose home is a home under
> none of them. **For every register entry whose home document is named in NO user-ratified surface,
> or only in a form the delegation bar excludes, the closing act is RE-HOMING into the owning layer's
> specification** — rule (e)'s own stated preference, made a rule rather than a preference. **AND THE
> EXCEPTION MECHANISM IS THE HALF THAT BINDS HARDER. A SESSION MAY NOT EXCEPT A DOCUMENT.** An
> exception — a document the user wants kept as a contract home by delegation instead — is a **NEW
> USER RULING NAMING THE DOCUMENT, TAKEN BEFORE THAT DOCUMENT'S ENTRIES ARE RE-HOMED, never after**;
> taken after, it is void, because the entries it would have covered are already gone. **The exception
> list was EMPTY when the rule was made, and that is a ruled state rather than an unfilled field.**

**In plain words.** When a register entry sits in a document that no user-ratified surface names as a home — or names only in a form the delegation bar excludes — the entry is closed by writing its rule into the owning layer's specification, not by obtaining a delegation for the document it happens to sit in. A session may never except a document from that route. An exception is the user's own ruling naming the document, and it is only valid if taken before that document's entries have been re-homed. No document was excepted when the rule was made. The rule chooses between two routes that both exist; it creates neither where the record says there is none.

**Why.** Rule (e) already prefers the owning layer's specification, and re-homing is what makes a decision findable without the register standing in for the specification; the excluded alternative is recorded at the ruling — delegation as the default grows the contract-home class, requires the user's own writing per document under rule (g), and runs against both concrete declinations already on the record. The timing half of the exception mechanism carries its own ground: an exception taken after the fact would be read back onto work already done, and the entries it would have covered are gone, so the ruling makes it void rather than retroactive. That the mechanism is real rather than notional is evidenced by its having been exercised once, at Ruling 39 of the seventh STOP, in the form it requires.

**Status.** LIVE · decided 2026-08-09 · ratified by user

**Home.** `CLAUDE.md:594-605`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-09, Ruling 38 of `cowork_rulings_2026_08_09_sixth_stop.md`, recorded at the finish-line route machinery by `cc_instruction_return_continuation_6.md` Task 0 and exercised once, at Ruling 39 of `cowork_rulings_2026_08_09_seventh_stop.md`, whose predicted outcome was then refuted by measurement and replaced by the three-step procedure of Ruling 40. CLASSIFIED as a DECISION by the user's Ruling 42 of 2026-08-09 (`cowork_rulings_2026_08_09_eighth_stop.md`), queue §9 entry 38 — the ONLY entry that ruling creates; Rulings 36, 37 and 39 stand as EXERCISES and BOTH offered upgrade readings are DECLINED on #6, 37's binding clause being already register data at D-661 with its dispositions on OI-229's row, and 39's decision content being the delegation itself, homed where the user wrote it in `ARCHITECTURE.md`. Homed by that same ruling in `CLAUDE.md`'s decisions-register section beside rule (g), as rule (l) — a USER-ONLY text the ratification is the scoped licence for; the queue's stated alternative home, `cowork_audit_protocol.md` beside D-642, was NOT taken because rules (g)–(k) there are the register's own home rules and this is the one they lack. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14) — the user ruled the classification and the home, and the entry text was written afterwards. Cross-ref D-230 (the register's rules (a)–(e), which rule (e)'s preference this makes a rule), D-432 (the delegation bar whose excluded forms define half the population), D-435 (delegating and being a home as different tests), D-642 (the class where NEITHER route applies, which this rule does not reach), D-654 (the narrow-letter licensing default the exception mechanism is a special case of).

### D-666 — An event a mechanism exists to produce is not a rule needing a home — the entry closes as the event, its evidence pointed at the surface the mechanism wrote to

> **(m) AN EVENT A MECHANISM EXISTS TO PRODUCE IS NOT A RULE NEEDING A HOME (user-ruled 2026-08-11;
> the ruling record is `cowork_rulings_2026_08_11_tenth_stop.md`, Ruling 49, taking Ruling 44 of
> `cowork_rulings_2026_08_09_ninth_stop.md`).** Rule (l) chooses between two available closing routes.
> This is the neighbouring case it does not reach: an entry for which **neither route is owed, because
> there is no rule to write at all.** **Where a register entry's whole content is an EVENT that a
> standing mechanism exists to produce and has produced — an adoption, an admission, a membership
> gained — the entry is CLOSED as that event, its register record standing as the event's index with
> its evidence POINTED at the surface where the mechanism recorded it. No specification home is owed,
> and inventing one is forbidden.**

**In plain words.** Some register entries record that something HAPPENED rather than stating a rule — a ground-truth class admitted to a needs list, an adoption, a membership gained — and the thing that produced the event is a mechanism the project already runs, which wrote the event down where it happened. Such an entry is closed as the event it is: the register record is its index, its evidence points at that surface, and no specification section is owed one. Writing one would be inventing text nothing reads.

**Why.** Writing an adoption event into a rule-stating section produces text nothing consumes and restates on a second surface what the mechanism's own output already carries, which is what #6 forbids. The test is stated in the rule itself so the class is recognised rather than argued — does a mechanism exist whose ordinary operation produces this, and did it? — and the rule states its own two exclusions, a RULE the mechanism operates under and content that is SUPERSEDED. It is general rather than one entry's treatment because three separate waves held entries they could not place, and the founding one turned out to have nothing to write at all: the needs vector's membership, already carried at the table the adoption happened in.

**Status.** LIVE · decided 2026-08-11 · ratified by user

**Home.** `CLAUDE.md:616-634`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-11, Ruling 49 of `cowork_rulings_2026_08_11_tenth_stop.md`, which ratifies the registration queue's §11 and takes Ruling 44 of `cowork_rulings_2026_08_09_ninth_stop.md` as a register entry as proposed. Applied by `cc_instruction_return_continuation_10.md` Task 1. The ruling's own ground for the class is the 20–23 precedent: an event a mechanism exists to obtain is not a rule needing a home, and inventing one writes text nothing consumes. Homed by that same ruling in `CLAUDE.md`'s decisions-register section beside rule (l), as rule (m) — the next letter of that section's own lettered list, which is the section's scheme and not an invented one, and a USER-ONLY text the ratification is the scoped licence for; the queue's stated alternative home, `cowork_audit_protocol.md` beside D-642, was NOT taken because rules (g)–(m) there are the register's own home rules and this is one of them. THE KIND HALF WAS JUDGED BEFORE THE WRITE: the receiving section states its rules as a lettered list this act adds to. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14) — the user ruled the classification and the home, and the entry text was written afterwards. Cross-ref D-664 (rule (l), the default route this is the neighbouring case of), D-667 (the sibling ruled in the same act, the other half of what the homing obligation does NOT reach), D-642 (the class where NEITHER route applies, which this rule sharpens rather than replaces), D-516 (the founding instance, closed as an adoption event), D-668 (the homing procedure whose findings-table STOP produced the hold this answers).

### D-667 — A per-corpus establishment verdict is a STATUS, so the decisions register is its home — and writing one into a rule-stating section is the mirror of the findings-table error

> **(n) A PER-CORPUS ESTABLISHMENT VERDICT IS A STATUS, SO THE DECISIONS REGISTER IS ITS HOME
> (user-ruled 2026-08-11; the ruling record is `cowork_rulings_2026_08_11_tenth_stop.md`, Ruling 49,
> taking Ruling 46 of `cowork_rulings_2026_08_09_ninth_stop.md`).** The phase-1 rule assigns STATUS to
> this register and CONFORMANCE to the specifications; it does not say which of the two an
> establishment verdict is, and this fixes it. **An establishment verdict (#19) about ONE corpus, one
> measurement tool or one gate — that it is established, or that it is not, or that the route to
> establishing it is exhausted — is the same KIND as supersession and shelving: register business.
> Its home is this register itself, its evidence pointed at the record that measured it. No
> specification home is owed.**

**In plain words.** When the record settles whether one particular corpus, measurement tool or gate is established — or that the route to establishing it has been exhausted — that verdict is a statement about standing, of the same kind as saying a decision is superseded or shelved. It belongs in the decisions register, with its evidence pointing at whatever measured it, and no specification section is owed one. Putting a verdict about one collection into a section that states rules would leave a later reader taking the finding for the rule.

**Why.** The phase-1 rule assigns status to this register and conformance to the specifications but never says which of the two an establishment verdict is; the ruling makes that identification, and it decides every future #19 verdict about a corpus, a measurement tool or a gate rather than the one it was taken on. Its converse carries its own ground and is stated with it: writing a one-corpus verdict into a rule-stating section is the mirror of the error the homing procedure's findings-table STOP exists to prevent. The line falls at the KIND rather than at the subject because a verdict about a corpus and a supersession about an entry are both statements about the STANDING of something the record holds, while the rule the verdict bears on lives elsewhere and is unmoved by it.

**Status.** LIVE · decided 2026-08-11 · ratified by user

**Home.** `CLAUDE.md:635-649`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-11, Ruling 49 of `cowork_rulings_2026_08_11_tenth_stop.md`, which ratifies the registration queue's §11 and takes Ruling 46 of `cowork_rulings_2026_08_09_ninth_stop.md` as a register entry as proposed. Applied by `cc_instruction_return_continuation_10.md` Task 1. Homed by that same ruling in `CLAUDE.md`'s decisions-register section beside rule (l) and beside D-666, as rule (n) — the next letter of that section's own lettered list, and a USER-ONLY text the ratification is the scoped licence for; the queue's stated alternative home beside principle #19 was NOT taken, because #19 states what establishment IS and this states where a verdict about it is RECORDED, which is decisions-register business. THE KIND HALF WAS JUDGED BEFORE THE WRITE: the receiving section states its rules as a lettered list this act adds to. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14) — the user ruled the classification and the home, and the entry text was written afterwards. Cross-ref D-666 (the sibling ruled in the same act), D-664 (rule (l), the default route neither reaches), D-475 (the founding instance, a per-corpus establishment verdict recorded as status-class), D-668 (the homing procedure whose step-3 STOP this converse mirrors), D-231 (the phase-1 rule that assigns status here and conformance to the specifications).

### D-674 — The filing convention for a document the record has OVERTAKEN — a dated report is re-bannered and never rewritten, a live governing surface has its body corrected

> ## What is done with a document the record has OVERTAKEN — the FILING CONVENTION, in two branches by KIND (user, 2026-08-11)
>
> The kind list above says which documents the section structure binds. **This says what is done when a
> document, of whatever kind, describes a state the record has since left behind** — the shape three
> open rows arrived at independently, each stopping at the same question and none able to answer it.
> The convention is written under the user's Ruling 62 of `cowork_rulings_2026_08_11_fourteenth_stop.md`
> and it turns on the SAME kind call the list above already makes.
>
> **BRANCH ONE — a DATED REPORT: it is RE-BANNERED as a historical record, and its BODY IS NEVER
> REWRITTEN.** Completed audits, probe reports, dossiers, and design documents whose approach was
> later falsified or superseded. The act is a **top banner** stating what the document is a record OF:
> its **date**, the **fate of its subject**, and the **commit or ruling that superseded or deleted
> it**. Nothing below the banner is touched.
>
> **BRANCH TWO — a LIVE GOVERNING SURFACE: the BODY IS CORRECTED.** A document a session is sent to in
> order to act — a first-read surface, a procedure, an inventory a task must trust. Its job is to be
> **true now**, so a stale statement in it is corrected in place, with the former wording preserved
> where the correction is made (#12).
>
> **THE KIND CALL FOLLOWS THE ENUMERATED KIND LIST ABOVE, AND A HARD CASE STOPS TO THE USER.** A
> document the two branches do not decide is not bannered by stretch and not rewritten by stretch — it
> is reported, exactly as an unlisted kind is.

**In plain words.** When a document describes a state the project has since left behind, what is done about it is decided by what KIND of document it is. A dated report — a completed audit, a probe report, a design whose approach was later ruled out — gets a banner at the top saying what it is a record of, and its body is never rewritten. A document a session is sent to in order to act — a first-read surface, a procedure, an inventory a task must trust — has its body corrected instead, because its job is to be true now. A document the two branches do not decide is reported to the user rather than forced into one of them.

**Why.** Stated at the home, in two halves. A dated report is EVIDENCE ABOUT AN ACT — what was known, when, and what was concluded — so rewriting it destroys the thing it exists to be (#12), and a reader who cannot see what the document said cannot tell a correction from a revision. A live governing surface is the opposite: it is not evidence but an INSTRUCTION, and a false instruction does damage every time it is read, which is what D-231's doc-sync half means by a specification cannot be the compliance standard while it misdescribes the code. The banner half additionally fixes BY CONSTRUCTION the defect the record had by then met three times — a correcting sentence sitting sections away from what it refutes, so that a reader who stops before the last line is told the opposite of HEAD. Measured rather than argued: the convention was ruled at three instances that had each stopped at the same question and none of which could answer it alone — a completed audit describing deleted code (OPEN_ITEMS.md OI-322), a falsified design carrying no supersession note (OI-332 item 3), and a first-read surface stating a superseded acceptance gate as current (OI-320) — and that the same defect splits by kind is exactly what none of the three could settle on its own.

**Status.** LIVE · decided 2026-08-11 · ratified by user

**Home.** `cowork_design_doc_template.md:120-141`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User verdict of 2026-08-11 over the ruling-registration queue's §21, which classified Ruling 62 of `cowork_rulings_2026_08_11_fourteenth_stop.md` as a DECISION and offered a downgrade reading in one line; the user KEPT the decision and DECLINED the downgrade. Applied by `cc_instruction_status_touch_and_oi141_premise_repin.md` Task 1, whose §0a carries the verdict; the closing state is the queue's §22. Checked at the register data before the write — the rule carried NO entry — so this is a creation landing in the commit that records the ratification (rule (c)). ★ THE GROUND THE USER WAS GIVEN, AND DID NOT CONTRADICT, IS EVIDENCE RATHER THAN ARGUMENT: the two open rows this ruling closes each recorded the COMPOSITION as ambiguous in their own words — `OPEN_ITEMS.md` OI-322 saying the same filing question applies to every completed audit in the tree and declining to take it, and OI-320 saying what its corrected text should say is not a session's to choose — and two rows stopping independently at the composition is what shows the standing principles did not decide it. THE KIND HALF WAS JUDGED BEFORE THE WRITE: the receiving document is the ONE home this project's writing standards have (`CLAUDE.md` Conventions), every section of it states a standard with its ruling and its defense, and the section this one sits beside is D-659's home — the kind list the convention's own kind call reads. ★ THE HOME IS THE RULING'S OWN AND WAS NOT DERIVED: Ruling 62 states it in terms — "The convention's home: `cowork_design_doc_template.md`, beside the Ruling 28 kind list, written under this ruling's licence." The queue's §21 nonetheless proposed no home, against its own §1 rule, which is the same procedural gap §20 reported for §19; it is recorded again at the queue's §22 and at `cowork_away_returns.md` §1.20, and in this instance it decided nothing. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14) — the user ruled the classification, and the entry text was written afterwards. THE CONVENTION TEXT was written into its home on 2026-08-11 by `cc_instruction_return_continuation_14.md` Task 0 under the ruling's own licence, one batch before this entry; what rule (c) discharges here is the CLASSIFICATION. Cross-ref D-659 (the kind list the convention's kind call reads, and its neighbour at the home), D-249 (the whole decision surface before any choice question — the siting principle branch one applies), D-231 (the phase-1 doc-sync half and its criterion C5, which branch two serves), D-644 (the tried-and-closed shape a superseded REMOVAL takes inside a specification — the neighbouring act for a rule rather than for a document), `OPEN_ITEMS.md` OI-320 and OI-322 (the two rows the ruling closed), OI-332 (the third instance, its item 3).


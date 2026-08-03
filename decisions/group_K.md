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

**Home.** `ARCHITECTURE.md:353-354`

**Provenance.** ARCHITECTURE.md:308-316 'Doc governance (2026-06-29) - the hierarchy'

### D-092 — A cross-cutting contract is stated once and never redefined in a layer document

> a **cross-cutting contract is stated once, here (§2.15), and never redefined in a
> layer doc**

**In plain words.** Rules that apply to every stage are written down in one place. A stage's own document may use such a rule but may not restate it in its own words.

**Why.** Same passage, ARCHITECTURE.md:312-313: a cross-cutting contract restated in a layer document is a second copy that can drift (#6); a layer document may USE the span typology or the verifiability contract, not redefine them.

**Status.** LIVE · decided 2026-06-29 · ratifier not stated

**Home.** `ARCHITECTURE.md:350-351`

**Provenance.** ARCHITECTURE.md:308-316

### D-093 — STATUS.md wins on current state; ARCHITECTURE.md on design

> Where a
> heading's status and STATUS.md disagree, STATUS.md wins. This section describes the **designs**.

**In plain words.** For what is built right now, read STATUS.md. For what was decided, read this document. Where they disagree about built-or-not, STATUS.md is right.

**Why.** Stated constraint, ARCHITECTURE.md:303-306 and :3102-3103: the two documents move on different clocks - current state changes every session, design changes only when a decision changes - so each owns the question it can keep current.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3487-3488`

**Provenance.** ARCHITECTURE.md:3363-3365, consistent with :251-254

### D-094 — Each layer carries exactly one build state

> Each layer below is tagged with exactly one build state: **Built+Live** (wired into the
> production pipeline), **Built+Dormant** (built and tested but not wired — reachable only via diagnostics, byte-identical on
> production), or **Design-only** (specified, not yet built).

**In plain words.** Every stage is labelled as live, built-but-not-connected, or designed-only - one label each, no ambiguity.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1222-1224`

**Provenance.** ARCHITECTURE.md:1151-1154. Three layer tags and two prose statements are stale after the switch - see OPEN_ITEMS OI-232

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

### D-127 — An architectural decision that changes is documented in the same commit

> When an architectural decision changes — update this document in the same commit.
> Stale documentation is worse than no documentation because it actively misleads.
> Claude Code should update relevant sections of this document as its last act when
> a session changes an architectural decision.

**In plain words.** When a design decision changes, the change to this document goes in the same commit as the change to the code.

**Why.** Stated constraint, ARCHITECTURE.md:6757: stale documentation is worse than no documentation, because it actively misleads.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6931`

**Provenance.** ARCHITECTURE.md:6754-6759 (§18.4); the standing principle is CLAUDE.md #10 (D-174). No date or ratifier stated.

### D-192 — A scoring change and its documentation land in the same commit

> **Sync rule — mandatory:** Any commit that adds or modifies a template, bonus,
> guard, gate, or other scoring term in `chordanalyzer.cpp` **must** include a
> corresponding update to `docs/scoring_model.md` in the same commit. The two
> must never drift apart. Specifically:
>
> - Adding a template: update the Templates section (§2), increment the template
>   count in the array-size comment, add the guard description if applicable
> - Adding or changing a bonus/gate: update the relevant §4 or §6 entry
> - Adding a new constraint or dead end: add it to §8

**In plain words.** Any commit that adds or changes a template, bonus, guard, gate or other scoring term in the chord analyzer must carry the matching update to the scoring-model document. They may never drift apart.

**Why.** Stated constraint, CLAUDE.md:625-630: violating the scoring model's invariants without reading it first has caused several failed attempts, named in the record - the leading-tone ambiguity attempt, four attempts at one bonus, and a rotation-selector bypass. The staleness check is mechanical: the template count in the document must equal the array size in the code (CLAUDE.md:642-645).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `CLAUDE.md:759`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:621-660. The document itself is `docs/scoring_model.md`.

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

**Home.** `CLAUDE.md:951`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:821-821; predicate qualification user-directed 2026-06-24, defined terms user-directed 2026-07-02. The ONE home is `cowork_design_doc_template.md`, which also carries the fourteen-section document structure, the status-banner convention and the implementation/test locator rule. Conformance of the existing tree is open at OPEN_ITEMS OI-230.

### D-194 — No self-invented labels, abbreviations, numbering schemes or jargon

> - **No self-invented labels, abbreviations, numbering schemes, or jargon** — in documents,
>   register rows, commit messages, and conversation alike. Use the name a thing already has
>   in the repository; if it has none, describe it in plain words. (User-directed, repeatedly;
>   recorded 2026-07-11.)

**In plain words.** A thing is called by the name it already has in the repository. If it has none, it is described in plain words rather than given a coined label - in documents, rows of the open-items register, commit messages and conversation alike.

**Why.** derivation not recorded.

**Status.** LIVE · decided 2026-07-11 · ratified by user

**Home.** `CLAUDE.md:947`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `CLAUDE.md:1003`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:873-876, user-directed 2026-08-01 at the decisions-register ratification review. The register's rationale field is what serves it; the founding instances the entry names are D-004's segment-cap value, D-059's window and D-015's boundary-tick convention.

### D-230 — The decisions register is a mandatory session-start read, and a new ruling lands in the register in the commit that records it

> (c) **a new ratification, shelving or falsification
> gets its register entry (data + regenerated files) IN the commit that records it**

**In plain words.** Every session must read the decisions index at its start, and whenever a decision is made, shelved or overturned, its register entry is part of the very commit that records the event - so rulings bind mechanically instead of by memory.

**Why.** The diagnosed root cause of the Stage-3.1b contradiction: decision history lived in archives outside the session-start read, so a later build contradicted a recorded ruling unknowingly (open_items/OI-208.md). The register existed as a snapshot; this rule is what makes it the living surface (#10 applied to decisions; #6 one home).

**Status.** LIVE · decided 2026-08-02 · ratified by user

**Home.** `CLAUDE.md`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling 2026-08-02 (the living-surface half of OI-208, all recommendations adopted); the CLAUDE.md decisions-register section + the session-start read list, edited in the same commit.

### D-232 — The section numbers are authoritative; the "Rule N" labels are a legacy flat numbering

> *The "Rule N" labels in §2.11–§2.12 are a legacy flat numbering of the coding/process rules and do not align with the
> §-numbers (and appear out of order); the **§-numbers are authoritative**. Read each "Rule N" as a local name for the
> rule stated beside it, not a cross-reference to a numbered list.*

**In plain words.** Where a coding or process rule in sections 2.11-2.12 carries a "Rule N" label, that label is only a local name for the rule beside it. The section number is what identifies the rule.

**Why.** The constraint that forced it, stated in the quote: the flat numbering does not align with the section numbers and appears out of order, so reading a "Rule N" label as a cross-reference sends the reader to the wrong rule.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:639-641`

**Provenance.** ARCHITECTURE.md:601-603 (stated as a standing reading instruction in the document itself) ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

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

**Home.** `cowork_design_doc_template.md:75-78`  — a project-wide convention with no owning layer; this is its correct home.

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

**Home.** `cowork_design_doc_template.md:82-91`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** cowork_design_doc_template.md:82 ('The locator stays (user, 2026-06-24)') and :91 ('User mandate 2026-06-22, refined 2026-06-24'). Homed in the file CLAUDE.md's Conventions entry names as the ONE home for writing standards, which names the implementation/test locator rule among what it carries. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-307 — A specification cites code by function or section anchor, never by raw line number

> **The locator's FORM: cite by function or by section anchor, never by a raw line number** (ruled 2026-07-02;
> homed here 2026-08-02 from `STATUS_ARCHIVE.md`, `OPEN_ITEMS.md` OI-272 — this is the writing standards' one
> home, and the locator rule above stated no constraint on the locator's shape). A specification points at

**In plain words.** When a design document points at the code, it names the function or the section, not the line. Line numbers go stale as soon as the file above them changes.

**Why.** The defect it answers is measured in the record: the gap analysis found stale line-number citations across the layer specifications, and the rule was made a policy at the same ruling that fixed them (`STATUS_ARCHIVE.md:242`).

**Status.** LIVE · decided 2026-07-02 · ratified by Cowork

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_design_doc_template.md:93-95`  — a project-wide convention with no owning layer; this is its correct home.

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

**Home.** `cowork_notation_adoption_increment.md:18`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **the opening block (above the first section heading)** — `# The notation-layer adoption increment — decision surface (★ USER-RATIFIED 2026-07-26)` (heading at line 1). Not reached: the document's delegation is graded before any section question arises. Decided by **D-432, the delegation bar — the strongest delegation is a provenance-attribution, which the bar does not admit**.

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

**Home.** `CLAUDE.md:205`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-03 (the fifth ruling set of that date), applied at phase 1n; dispatch `cc_instruction_phase1n_criterion_premise_and_reading_regime.md` §2. **It SUPERSEDES, and does not falsify, the two tests that preceded it** — the delegation-specificity criterion ruled and measured earlier the same day (`OPEN_ITEMS.md` OI-281, first measurement note) and the document-kind test ruled and measured later the same day (same row, second note). Both were proxies for this test, and each produced the evidence that located its own error: the specificity criterion's residue turned out to be its third clause used as a judgment, and the kind test's residue turned out to be that kind is a property of the DOCUMENT while a delegation points at a SECTION. Recorded that way so a reader meets one derivation rather than three rival tests. **Applied STAGED, as the ruling directs:** only to the entries where section granularity decides something — the ambiguous population of the kind test plus the `cowork_score_census.md` entries, 46 entries across 5 documents — with everything else migrating as its document is next touched. The staging is stated in the register's own scope note (`header.scope.home_granularity`) so the mixed field cannot be misread. **The tooling cost was measured BEFORE any entry was changed, against a stop criterion declared in the dispatch before the diff existed (#22):** the change is confined to an additive per-entry field plus the generator and checker that read it; `home` itself is untouched, so the quote-verification path, the anchor check and the drift report are byte-unchanged and no existing anchor needed re-aiming. The section is DERIVED from the home document's own headings and the entry's own cited line by `tools/audit/decisions/gen_section_homes.py`, whose `--check` re-derives it, so no section is transcribed and none can go stale when a heading moves. Guard (g) is untouched: the delegation confers, and only the user writes a delegation into `ARCHITECTURE.md`. NOT RATIFIED as an ENTRY — it goes to the user in the phase-1n ratification queue. **THE STAGING ENDED 2026-08-03 (phase 1q):** the user ruled the criterion applied to the whole home population in one pass, so both halves — the delegation half and the states-rules half — now decide every entry the criteria reach, and the register's home field is no longer of mixed granularity. The applier is `tools/audit/decisions/gen_home_classification.py`, which replaces `gen_section_homes.py` (two appliers of one criterion is the duplication #6 forbids). How a WHOLE-DOCUMENT delegation is read — it reaches every section — was, at phase 1q, an interpretation of this ruling's *BY NAME* clause, taken on the record's own precedent at `OPEN_ITEMS.md` OI-290 and recorded, with the strict alternative it rejects, at `backbone_decisions.json` → `section_home_criterion.whole_document_reading`. **THE VERBATIM ABOVE WAS RE-TAKEN 2026-08-03 (phase 1r), because the user WROTE THAT INTERPRETATION INTO THE RULE.** The GRANULARITY clause — a delegation naming a document reaches all its sections, a delegation naming sections reaches only those, and the rule-stating half is judged per section in both cases — was ruled by the **user on 2026-08-03** at the phase-1q whole-document reading and written into `CLAUDE.md` rule (h) itself. It is recorded here as a **SCOPE CLARIFICATION of this decision, not as a separate decision**, and deliberately gets no sibling entry (#6): it fixes what this ruling's own *BY NAME* clause reaches when a delegation names no section, introduces no new criterion, changes nothing about which surfaces may delegate (that is D-432), and reaffirms rather than alters the states-rules half. What it does change is the record's option space — before it, the strict alternative was recorded as available to the user; after it, the strict reading is closed. **The verbatim this replaces, preserved (#12):** *"**(h) THE UNIT OF (g) IS A SECTION, NOT A DOCUMENT (user, 2026-08-03): a home is a SECTION of a document, admitted when a user-ratified surface delegates a stated concern to that section BY NAME and that section STATES RULES rather than recording findings.**"* — the same opening sentence, ending at *recording findings*, without the kind/banner sentence and without the granularity clause.

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

**Home.** `CLAUDE.md:232`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-03 (the seventh ruling set of that date, W2 — 'grade the forms and set the bar'), homed at phase 1p as rule (i) of the decisions-register section, beside (g) and (h) which it completes. **RECORDED AT PHASE 1p, APPLIED AT PHASE 1q.** The dispatch ordered a check before applying it — *does this bar change the verdict for any document the register currently classifies `contract-home`?* — and predicted no, on the ground that the admitted set was reached on explicit delegation clauses. The check was run in a generator (`tools/audit/decisions/gen_phase1p_delegation_bar.py` → `pre_apply_check`) and the prediction is **REFUTED**: the bar excludes documents the register currently admits. Under the dispatch's own instruction that is a #13 STOP, so no entry's home class was changed and the non-conformance is rowed at `OPEN_ITEMS.md` OI-291. The generator applies nothing — it only reads the backbone. NOT RATIFIED as an ENTRY — it goes to the user in the phase-1p ratification queue. **APPLIED 2026-08-03 (phase 1q, the user's ruling of that date, option A3):** the user ruled ONE re-classification pass over the whole home population rather than a forward-only migration or a revision of the bar, with a WRITE LIST for the homes the record means to keep. The pass is `tools/audit/decisions/gen_home_classification.py` → `phase1q_reclassification.json`; its `totals` carry the movement and its `write_list` the drafted delegations, which go to the user because only the user writes one. `OPEN_ITEMS.md` OI-291 flips with that provenance. **THE WRITE LIST CAME BACK WRITTEN, 2026-08-03 (phase 1r).** The user wrote a delegation for each of the six documents the pass emitted, and the pass was re-run against them: all six move, two only in part (`tools/audit/decisions/phase1q_reclassification.json` -> `the_phase_1r_re_run`; `OPEN_ITEMS.md` OI-293 closes). The bar itself is unchanged — what changed is the wordings it reads, which is the outcome the ruling was designed to produce. The pre-apply check still reports STOP over the same three documents: four delegation grades moved today, so the grades the check was run against are frozen at `gen_phase1p_delegation_bar.py` -> `GRADE_AT_PHASE_1P` while `FORMS` stays live for the classifier (#12, and one live grade with one home, #6). **This entry's own defense now cites two line numbers that have moved** — the same act shifted `ARCHITECTURE.md`, and no tool re-aims a line number quoted inside a rule's prose; carried at `OPEN_ITEMS.md` OI-294. **CORRECTED BY THE USER'S RULING, 2026-08-03 (phase 1s, Y2 — option 1B): the defense is CONVERTED FROM LINE NUMBERS TO A DESCRIPTION.** The rule's *Why:* clause now says that one line ends *"Full spec:"* and names its target on the next, and that the delegation clause immediately beneath names its target and its sections — the same evidence, stated so that nothing in it can drift. The reason is written into the rule text because it generalizes: a line number quoted inside a rule's PROSE is not a register anchor, so `reaim_home_anchors.py` cannot maintain it and it goes stale on the next insertion above it. **The FORMER wording is preserved here (#12):** "*Why:* the canonical document distinguishes the two acts in ADJACENT LINES — `ARCHITECTURE.md:1482` ends *\"Full spec:\"* and names its target on the next line, while `:1485` immediately beneath is a delegation clause that names its target AND its sections. The distinction is `ARCHITECTURE.md`'s own, not a preference." **This entry's VERBATIM did not need re-taking and was not re-taken**, which is stated rather than glossed: the quoted block ends at *"…a parenthetical recording where something was ratified."*, and the corrected *Why:* clause sits immediately BELOW it, outside the quote. The `rationale` field above already carried the description form (it cites `tools/audit/decisions/phase1p_delegation_bar.json` → `the_defense`, generated), so it needed no change either. `OPEN_ITEMS.md` OI-294 flips.

### D-433 — A shelved section can be a home — shelving is a status, not a kind

> **A SHELVED SECTION CAN BE A HOME — SHELVING IS A STATUS, NOT A KIND (user, 2026-08-03).** A
> section whose rules are shelved still STATES rules, and the register records shelvings with their
> evidence, so a shelved decision needs a home exactly as a live one does (#12).

**In plain words.** A section of a document does not stop being the proper home of a decision because the work it describes was shelved. The kind test asks what a section DOES — state rules, or report findings — and a shelved banner does not change that. Shelved decisions are kept with their evidence, so they need a home just as live ones do.

**Why.** Stated with the ruling: the kind half of the section-level criterion asks what a section DOES, and a status banner does not change that. It also closes a residue the record was still carrying — the phrase *"stable enough to be cited"*, a clause of the superseded delegation-specificity criterion which survived in the tracking prose after the section-level ruling replaced it, and which would otherwise have invited a fourth criterion (`OPEN_ITEMS.md` OI-281, first measurement note, §4).

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `CLAUDE.md:226`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `CLAUDE.md:255`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-03 (the eighth ruling set of that date, X2 — 'draft a proper delegation rather than an exception'), homed at phase 1q as rule (j) of the decisions-register section, beside (g), (h) and (i) whose interaction it fixes. It resolves the collision the phase-1p wave reported and did not settle: that wave's own §4 ordered `cowork_engage_arc_plan.md`'s three entries ADMITTED on the test *names it by name for a stated concern*, while **D-432** excludes that naming as a provenance attribution. **The bar governs and the phase-1p §4 admission is superseded on this point**, recorded rather than dropped; the remedy for the arc plan is a drafted delegation on the phase-1q write list (`tools/audit/decisions/phase1q_reclassification.json` → `write_list`), which goes to the user because only the user writes a delegation. NOT RATIFIED as an ENTRY — it goes to the user in the phase-1q ratification queue. **THIS ENTRY'S RATIONALE IS STALE AT HEAD, and is left standing rather than rewritten (2026-08-03, phase 1r).** It says the bar excludes `cowork_engage_arc_plan.md` as a delegation TARGET "because the only naming of it is inside a list of citations (`CLAUDE.md:129-130`)" — true when the ruling was made, and no longer true: on the user's direction the OI-293 write list wrote an explicit delegation clause into `CLAUDE.md` for exactly this document, so its three entries are now `contract-home`. **The RULING is untouched by that** — (j) says delegating and being a home are different tests, and the arc plan became a home by being delegated to, which is the rule working rather than an exception to it. What is stale is the verbatim's closing clause, *"and today none does"*, a factual statement inside user-ruled text that this session may not edit; it is rowed at `OPEN_ITEMS.md` OI-294 for the user. **CORRECTED BY THE USER'S RULING, 2026-08-03 (phase 1s, Y2 — option 1B).** The user ruled the stale clause struck and this rationale re-taken. The verbatim above is RE-TAKEN from the corrected rule text, which now says the arc plan is not a delegation target BY THE FACT of being a source and that the home question is answered by reading the delegations that exist — a statement of what the two tests ARE, carrying no present-tense claim about any document's current standing, so it cannot go stale the same way again. **The FORMER verbatim clause is preserved here (#12):** "— is not thereby a delegation TARGET: whether any section of it is a home turns on whether some user-ratified surface delegates a concern to it in a form (i) admits, and today none does." **The FORMER rationale is preserved here (#12):** "The question arose in exactly this form and had to be answered before the delegation bar could be applied: `cowork_engage_arc_plan.md` is one of the three user-ratified surfaces the contract-home criterion reads delegations FROM, and the bar excludes it as a delegation TARGET, because the only naming of it is inside a list of citations (`CLAUDE.md:129-130`). Stating the two roles apart is what keeps the bar a mechanical test: the alternative on the table was an exception for this one document, and a mechanical test with a case-by-case exception is not a mechanical test." The RULING is untouched by either correction.


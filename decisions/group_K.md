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

**Home.** `ARCHITECTURE.md:315-316`

**Provenance.** ARCHITECTURE.md:308-316 'Doc governance (2026-06-29) - the hierarchy'

### D-092 — A cross-cutting contract is stated once and never redefined in a layer document

> a **cross-cutting contract is stated once, here (§2.15), and never redefined in a
> layer doc**

**In plain words.** Rules that apply to every stage are written down in one place. A stage's own document may use such a rule but may not restate it in its own words.

**Why.** Same passage, ARCHITECTURE.md:312-313: a cross-cutting contract restated in a layer document is a second copy that can drift (#6); a layer document may USE the span typology or the verifiability contract, not redefine them.

**Status.** LIVE · decided 2026-06-29 · ratifier not stated

**Home.** `ARCHITECTURE.md:312-313`

**Provenance.** ARCHITECTURE.md:308-316

### D-093 — STATUS.md wins on current state; ARCHITECTURE.md on design

> Where a
> heading's status and STATUS.md disagree, STATUS.md wins. This section describes the **designs**.

**In plain words.** For what is built right now, read STATUS.md. For what was decided, read this document. Where they disagree about built-or-not, STATUS.md is right.

**Why.** Stated constraint, ARCHITECTURE.md:303-306 and :3102-3103: the two documents move on different clocks - current state changes every session, design changes only when a decision changes - so each owns the question it can keep current.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3364-3365`

**Provenance.** ARCHITECTURE.md:3363-3365, consistent with :251-254

### D-094 — Each layer carries exactly one build state

> Each layer below is tagged with exactly one build state: **Built+Live** (wired into the
> production pipeline), **Built+Dormant** (built and tested but not wired — reachable only via diagnostics, byte-identical on
> production), or **Design-only** (specified, not yet built).

**In plain words.** Every stage is labelled as live, built-but-not-connected, or designed-only - one label each, no ambiguity.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1151-1153`

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

**Home.** `ARCHITECTURE.md:6756`

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

**Home.** `CLAUDE.md:632`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Why.** Stated constraint, CLAUDE.md:818-819: inherited prose is audited as hard as new prose, so the standard is about the document a reader meets rather than about who wrote which sentence. The one-home rule is #6 applied to the standards themselves (CLAUDE.md:820-821).

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `CLAUDE.md:812`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:812-821; predicate qualification user-directed 2026-06-24, defined terms user-directed 2026-07-02. The ONE home is `cowork_design_doc_template.md`, which also carries the fourteen-section document structure, the status-banner convention and the implementation/test locator rule. Conformance of the existing tree is open at OPEN_ITEMS OI-230.

### D-194 — No self-invented labels, abbreviations, numbering schemes or jargon

> - **No self-invented labels, abbreviations, numbering schemes, or jargon** — in documents,
>   register rows, commit messages, and conversation alike. Use the name a thing already has
>   in the repository; if it has none, describe it in plain words. (User-directed, repeatedly;
>   recorded 2026-07-11.)

**In plain words.** A thing is called by the name it already has in the repository. If it has none, it is described in plain words rather than given a coined label - in documents, rows of the open-items register, commit messages and conversation alike.

**Why.** derivation not recorded.

**Status.** LIVE · decided 2026-07-11 · ratified by user

**Home.** `CLAUDE.md:808`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:808-811, user-directed repeatedly and recorded 2026-07-11.

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

**Home.** `CLAUDE.md:864`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:864-876, user-directed 2026-08-01 at the decisions-register ratification review. The register's rationale field is what serves it; the founding instances the entry names are D-004's segment-cap value, D-059's window and D-015's boundary-tick convention.

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

**Home.** `ARCHITECTURE.md:601-603`

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

**Home.** `cowork_design_doc_template.md:82-91`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** cowork_design_doc_template.md:82 ('The locator stays (user, 2026-06-24)') and :91 ('User mandate 2026-06-22, refined 2026-06-24'). Homed in the file CLAUDE.md's Conventions entry names as the ONE home for writing standards, which names the implementation/test locator rule among what it carries. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-307 — A specification cites code by function or section anchor, never by raw line number

> **(#9 stale line-number citations)** RULED with a POLICY: specs cite by **function/§ anchor, not raw line number** (numbers rot)

**In plain words.** When a design document points at the code, it names the function or the section, not the line. Line numbers go stale as soon as the file above them changes.

**Why.** The defect it answers is measured in the record: the gap analysis found stale line-number citations across the layer specifications, and the rule was made a policy at the same ruling that fixed them (`STATUS_ARCHIVE.md:242`).

**Status.** LIVE · decided 2026-07-02 · ratified by Cowork

**Home.** `STATUS_ARCHIVE.md:242`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `STATUS_ARCHIVE.md` (session 21e, the gap-analysis rulings). It is NOT in `cowork_design_doc_template.md`, which is the ratified home of the writing standards and states the implementation/test locator rule without this constraint on the locator's form — checked at the source. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue).


# The CURATED BOOT LIST — DRAFTED for the user's ruling (2026-08-19)

> **Preparation output (d), drafted by Cowork on 2026-08-19.** Nothing here is executed by anything
> in this file: no read regime changes, no document moves, no candidacy moves, and no session boots
> from this list until the user rules it. It lands in git at the next dispatch's Task 0, on the
> standing interim-carrier clause.
>
> **★ WHY IT EXISTS AT ALL, STATED BEFORE ANYTHING ELSE.** This output was commissioned on
> 2026-08-15 and has been excluded by name from **every one of the fourteen preparation dispatches**
> — each carries the line *"No curated boot list."* It is the PILOT phase's only stated hard
> prerequisite. It has never been drafted. That is why it is drafted first and alone here.

---

## 0. The referents, from scratch

**The six phases.** The project's governing structure is six phases, ruled 2026-08-15: preparation →
the pilot → the framework → the detail specifications → measurement design → the audit. Their one
home is `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §3, blob
`8de58f0ed968b345dc6806dcbfa7980deddd04f2` at branch tip `891bacc5d2`.

**An implementation-blind session** is a session that derives what the analysis SHOULD do without
reading what the current code or its specifications say it DOES. The pilot phase is built on such
sessions: its constraint reads *"NOT ALLOWED: reading implementation-derived material inside the
deriving session; treating the current text as authority rather than as an untrusted source."*

**The curated boot list** is the reading list such a session opens at boot. Its ruled definition, at
`cowork_rulings_2026_08_17_session_start_read_sitting.md` §4 (blob `881b468f63`), verbatim:

> *"The curated boot list remains the implementation-free read list an implementation-blind session
> boots from — for those sessions only … It is NOT widened to ordinary sessions. It remains a live,
> unblocked preparation output, DRAFTED and RULED before any derivation session boots from it, and
> it is not the route to a smaller ordinary session-start read."*

**The ordinary session-start read** is a different thing and is untouched by this list: `CLAUDE.md`,
`STATUS.md`, `DECISIONS.md`, and the derived gating answer narrowed to its identity list. Nothing
below shrinks, widens or amends it.

---

## 1. The membership test applied — AUTHORED, and stated so it can be challenged per member

A document is a member when all three hold:

1. **It is implementation-free.** It states rules, ruled intent, or fact independent of this
   project's code — and carries no statement derived from the current implementation's behaviour,
   measured values, or structure.
2. **A deriving session cannot do its work without it.** Not merely useful: absent it, the session
   either breaks a standing rule or invents something it was not licensed to invent.
3. **It is that content's home**, not a pointer to it (#6).

A document failing any limb is OUT. **A document this test cannot place is a STOP back to the user,
never defaulted either way.** None arose in this draft.

---

## 2. The members

### (1) The phase definitions — `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md`, §3 whole
Blob `8de58f0ed9`. Carries the six phase definitions, the standing constraints over every phase
(§3.8), and the retrospective that closes each (§3.9). **Implementation-free:** it is a ruling about
work structure and names no behaviour, value or code fact. **Necessary:** it is what tells a deriving
session what it may and may not do, and §3.2 is the pilot's own charter.

### (2) The guiding principles and the conventions — `CLAUDE.md`, TWO SPANS ONLY
Blob `450dff57cf`. The spans are named by their own heading anchors and never by line number (the
OI-330 lesson): the span opening at **`## Guiding principles`** and running to the end of the
`Delegation pointer` paragraph; and the span opening at **`## Conventions`** and running to the end
of **`## The self-check after every coding exercise`**.
**Implementation-free:** both spans state rules and their defenses. **Necessary:** #1–#24 are the
decision guide every act is checked against, and the conventions carry the reserved-word rule, the
never-work-from-memory rule, the working-tree-read rule and the decision-surface rule.
**★ THE REST OF `CLAUDE.md` IS EXCLUDED AND THE REASON IS THE WHOLE POINT OF A CURATED LIST** — see
§3(a).

### (3) The writing standards — `cowork_design_doc_template.md`, whole
Blob `518048459d`. The predicate-qualification rule, the defined-terms rule, the fourteen-section
document structure, the status-banner convention. **Implementation-free** and **necessary**: a
deriving session's output is a written specification, and this is the one home of how one is written.

### (4) The dispatch protocol — `cowork_audit_protocol.md`, its dispatch-protocol section, whole
Blob `8166688e2c`. The clauses carrying the membership marker govern how a dispatch, a session report
and a ruling record are written, sequenced and executed. **Implementation-free** — every clause is
about conduct. **Necessary:** a deriving session is dispatched, and these bind it.

### (5) The design-intent rulings — `tools/audit/rulings_sort_classification.json`, the `DESIGN-INTENT` class only
Blob `1659e79970`. 244 of the 411 deciding-act-named register entries, sorted into design intent
versus management of the implementation, ruled at its own sitting. **Necessary:** it is the seed
material the framework consumes and the ratified design intent the pilot reads.
**★ ITS IMPLEMENTATION-FREEDOM IS ASSERTED BY THE SORT'S OWN TEST AND IS NOT SEPARATELY MEASURED**,
and that is declared rather than hidden: the sort separates intent from management, which is not the
same cut as implementation-derived versus not. A member of this class that turns out to carry a
measured value or a code fact is a finding, not a contradiction. **This is the one member of the list
whose limb (1) rests on an imported test.**

### (6) The defect-type catalog — `DEFECT_TYPES.md`, whole
Blob `3450429290`. The named failure shapes a derivation must not walk into (DT-2 and its siblings).
**Implementation-free:** the catalog names shapes of reasoning error, not code. **Necessary:** the
standing self-check checks work against it by name.

---

## 3. What is EXCLUDED, each with its reason — the half that makes the list curated

**(a) The rest of `CLAUDE.md`.** The gate and threshold policy blocks publish measured corpus
agreement values, hard-stop durations and per-preset run sets; the local-patches section describes
edits to the built application; the build and test commands operate it; the two register sections
govern apparatus a deriving session does not touch. **Every one of them is implementation-derived by
construction**, and a blind session that reads them is no longer blind.

**(b) `DECISIONS.md` and its group files.** The register indexes decisions about the system as built,
and its rule (a) makes it an ordinary-session read. The part a deriving session needs — ruled design
intent — reaches it through member (5), which is that content's derived home. Admitting both would be
two homes for one concern (#6).

**(c) `STATUS.md`.** Current iteration and baseline state of the implementation.

**(d) `ARCHITECTURE.md`.** The implementation's own specification. Reading it is precisely what
"implementation-blind" excludes. It is read AFTER the derived statement is written, as an untrusted
source, exactly as §3.2 sequences it.

**(e) `docs/scoring_model.md`.** The pilot's own subject, derived blind; read only after the derived
statement exists, together with its history at the preserved pre-restructuring version `b006dc15b5`.

**(f) `OPEN_ITEMS.md`, its detail files, and the derived gating answer.** The open-items register
tracks discovered defects of the built system.

**(g) `cowork_handoff.md`, the dispatches (class 20) and the coding-side reports (class 21).**
Process records of the implementation arc. They are mining inputs to the preparation phase behind its
fact-gate, never boot reads.

**(h) `BUILD_AND_TEST.md`** — a conditional read for a session that builds, tests or runs a
measurement tool. A deriving session does none of those.

---

## 4. The one member that does not exist yet, named rather than silently omitted

**The EMPIRICAL FINDINGS LEDGER (preparation output (c)) is NOT BUILT** — no artifact of that kind
exists anywhere in the tree at `891bacc5d2`. Its ruled place is a member of this list: it is the
fact-gated home of the empirical findings that survive the implementation being thrown away, and a
deriving session is meant to read admitted facts from it and from nowhere else.

**So this list is drafted with a declared hole.** Two readings are available and the record does not
choose between them: the pilot opens on the list as it stands and the ledger joins it when built; or
the ledger is built first and the list is ruled once, whole. **That choice is the user's and no
recommendation is made on it (D-658).**

---

## 5. The mechanical check Ruling 4 demands, RUN and reported

Ruling 4 records that **a mandatory-read or boot listing HOLDS a retirement candidate**, so a boot
list changes what holds candidates and moves the archiving wave's inputs.

**Derived at `tools/audit/retirement_caller_check.json` (blob at tip): the nine candidacies are**
`ai-assistant-design-notes` (PASSES-THE-CHECK), and, HELD-BY-CALLERS,
`documentation-directory-prose`, `idiom-discovery-workspace`, `llm-triage-prompts`,
`measurement-and-analysis-tools`, `measurement-outputs-recorded-beside-the-tools`,
`reports-from-the-coding-side`, `stray-working-files-committed-to-the-repository-root`,
`writing-side-scratch-directories`.

**No member of this list belongs to any of the nine.** The six members fall in
`governing-documents`, `ratification-surfaces`, `writing-side-design-documents` and
`audit-apparatus-artifacts`, none of which is a candidacy. **So this list holds nothing new, and the
archiving wave's inputs do not move.** The check comes back clean.

---

## 6. What this list does NOT do

It does not shrink, widen or amend the ordinary session-start read (Ruling 4 in terms). It archives,
moves, renames and deletes nothing. It authorizes no derivation, no design, no specification edit and
no fix. It moves no candidacy and no verdict. It does not claim the membership is complete: the
membership is **AUTHORED**, each member carries the reason it is one, and a document the test would
admit that nobody thought of would not appear — which is stated so the authored half is checkable by
reading six reasons rather than trusted.

---

*Provenance: Cowork, 2026-08-19, drafted at branch tip `891bacc5d2`. Every document named above was
read at its git OBJECT by explicit hash or opened with the file tools from a snapshot staged through
the device bridge; `CLAUDE.md` was read in full by this session, lines 1 to 1844. Spans are named by
their own heading anchors and never by line number. No character total is published here, because a
published character value names the tool that produced it (F66) and no generator for this list's size
exists yet.*

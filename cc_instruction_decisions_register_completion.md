# CC instruction — the decisions-register correction and completion pass (OI-207/OI-208 follow-up from the user's ratification review)

> **Read first (every session):** `C:\s\MS\CLAUDE.md` IN FULL — note it now carries a NEW
> Conventions entry, user-directed 2026-08-01: **every design decision carries its defense at its
> home** (this entry is a riding Cowork edit — commit it with your first commit). Also
> `C:\s\MS\STATUS.md`, `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\OPEN_ITEMS.md` (INDEX) and the detail
> files **OI-207, OI-208, OI-237**; then `DECISIONS.md` itself (the register your work amends) and
> its generators under `tools/audit/decisions/`.
>
> **Context.** The OI-207 adjudication delivered the register (115 entries) and the user began the
> ratification review. That review, verified at the objects by Cowork, found (a) a cluster of
> defects in the register data, and (b) a bounded scope gap: the backbone read `ARCHITECTURE.md`'s
> per-layer sections in full, but ratified decisions also live in that document's NON-layer
> sections (§17 Coding Standards, §12.1 User Interface, §1.2–1.3 among them), in `CLAUDE.md`'s
> principles and policies, in open-item rows and handoff blocks, and on standing decision-bearing
> surfaces. The user directed the completion. **Ratification of the register happens AFTER this
> pass, over the corrected and completed register.**
>
> **Current state:** branch `master`; expected HEAD `e9ecd37314` — verify; mismatch = STOP. The
> riding Cowork edit to `CLAUDE.md` (the new Conventions entry) rides your first commit. The
> untracked files `cc_instruction_*.md` and `cowork_oi200_perspective_inventory.md` stay
> untracked — do not commit them.
>
> **Hard stops:** origin only; **no `src/` change of any kind**; no golden, `tools/corpus/` or
> `tools/robust_stop/` movement; **no `ARCHITECTURE.md` edit** (writing a specification entry
> remains a separate, ratified act — OI-208 ruling 2); no fix, no design, no inference change.
> A surprise is a STOP (#13). VS Code bash rules on every command. A feasibility stop with a
> measured partition proposal is an accepted outcome.
>
> **Writing rules bind your new prose:** predicates qualified; plain restatements written for the
> user (music theory and software architecture, not C++, not statistics); the bare word always
> carries the musical meaning (quoted repository text stays verbatim, collisions included; your
> own prose avoids them).

**Dispatch author:** Cowork, 2026-08-01.

---

## Task 1 — corrections to the existing register data

All corrections go into `tools/audit/decisions/backbone_decisions.json` (the source of record),
then `DECISIONS.md` is regenerated; `--check` must pass. The verbatim quotes are NEVER altered.

**(a) The mis-aimed open-items cross-references in provenance — sweep ALL of them, not only the
verified four.** Cowork verified at the objects: D-060's provenance cites OI-237 where the
non-conformance row is **OI-235**; D-100 and D-114 cite OI-239 where the documentation-gap row is
**OI-237**; D-019 cites OI-232 where the non-conformance row is **OI-231** (OI-232 remains correct
for the stale-status point); D-011 and D-030 cite OI-231 where the conflict rows are
**OI-210/OI-212** (and OI-213 if the per-command multiplier was meant). Re-aim every provenance
`OI-…` reference in the backbone by opening the referenced row and confirming its subject matches
the sentence citing it; state in the report how many were wrong and the underlying cause.

**(b) Stale line anchors in `open_items/OI-237.md`.** Its Kind-1 table cites D-098's home as
`OPEN_ITEMS.md:185`; the nine inserted rows moved it to `:194`. Re-verify every line anchor in
that file (D-096 `:26`, D-097 `:123` included) against the current tree and correct.

**(c) Plain-restatement rewordings** (the verbatim quotes stay; only the "In plain words" text
moves), each traced to the user's review:

- **D-033** — the current restatement says "answers one question from one kind of evidence",
  which the user read as an evidence restriction. The decision is about OWNERSHIP of
  contributions; restate so it says each stage owns one contribution and, within it, **uses all
  the information the note reader carries** (spelling, metric weight, voice).
- **D-050** — "The analysis never reaches into music it was not given" over-generalizes from the
  slicer to the whole analysis. Restate narrowly: the SLICER never reaches outside the span it
  was handed; extending the span is the orchestration's job (D-030's extensible-span rule), and
  the re-slice-equivalence guarantee is what makes extension lawful.
- **D-100** — the restatement states the pre-amendment rule too starkly. Include the 2026-07-12
  amendment: EVIDENCE-class facts are published broadly even WITHOUT a named consumer, each
  carrying its establishment status; disposition of an unconsumed fact is decided fact-by-fact
  (declared dormancy with a named future reader, or removal), and non-inference consumers count.

**(d) D-103 gains its successor pointer.** The ratified successor decision is recorded at
`open_items/OI-194.md` (and the OI-194 index row): the **voice-independent pedal-point class
supersedes the legacy bass-only fact**. Link D-103's provenance to it, and add the successor as
its own backbone entry (Task 3 class (c)) since it is a recorded ruling with no entry.

**(e) `STATUS.md` entry ordering.** The 2026-08-01 entry sits below three 2026-07-28 entries;
newest-first is the file's convention. Move it to the top, byte-verbatim.

**(f) "Derivation not recorded" flags (the new Conventions entry applied).** Where an entry's
value or convention has no recorded derivation — verified instances: D-004's segment-cap VALUE 4
(the cap's FORM is the established semi-Markov default, `cowork_joint_estimator_factorization.md`
§7 factor 7; the value's derivation appears nowhere), D-059's 16/8 window, D-015's
boundary-tick convention — the provenance states **"derivation not recorded"**. Never fill a
missing defense in from inference.

## Task 2 — the rationale field

Add a **rationale** field to the backbone entry shape and to the generated register entry
("**Why.**" beneath the plain restatement). Populate it ONLY from the record: the factorization
document's per-factor research citations (Temperley, Raphael & Stoddard, de Clercq, and the rest
of §7), a measurement the record names, or a constraint the record states. Where the record is
silent, the field reads **derivation not recorded** — that population count is a reportable
number, and the user's directive exists precisely to drive it down over time. Do not summarize a
source you have not opened; cite file:line.

## Task 3 — the backbone completion pass

Same discipline as the original Task 1: verbatim quote, home at file:line, plain restatement,
status from the record only ("not stated" permitted, inference forbidden), the anchor guard
extended over every new entry. Number new entries continuing from the current maximum. Four
classes:

**(a) `ARCHITECTURE.md`'s non-layer sections, read IN FULL.** The document has 19 sections plus
appendices. First state, from the existing backbone's citations, which sections the original pass
demonstrably covered; then read the remainder in full — at minimum §1, §6–§19 and the appendices
where not already covered. Known-present decisions that MUST appear (found by Cowork at the
objects): **§17.1–17.2** (MuseScore coding style, `.clang-format` before every commit, naming,
GPL v3 file headers, include ordering; the higher documentation standard — public classes and
methods documented in musical terms; every non-obvious scoring weight or threshold explains its
musical reasoning); **§12.1** (all user-visible strings through MuseScore's Qt localization,
`.ts`/Qt Linguist, English and Swedish for all new strings; KDDockWidgets/QML panel integration,
no parallel infrastructure; Qt accessibility patterns); **§1.2–1.3** (GPL v3, GPL-compatible
libraries only, the long-term official-contribution intent). Cross-link the §1.2 contribution
intent with the `CLAUDE.md` distribution constraint (fork-local only, NEVER upstream, the
`cfc7eb5e39` hard stop) — two recorded positions, a general intent and a one-patch exception;
record BOTH with the link, resolve nothing.

**(b) `CLAUDE.md`'s standing decisions.** The guiding principles **#1–#24** (each its own entry;
#12 already exists as D-099 — no duplicates), the ratified corollaries (constrained-optimum
ledger; scope-of-surprise and the desk-simulate → read-only probe → build funnel; the
**decision-neutrality corollary**, user-ratified 2026-07-26), the two-tier class-(a)/(b) gate
policy (user-ratified 2026-06-22), the scoring-model same-commit sync rule, the self-check rule
(2026-07-11), the writing standards (predicate qualification 2026-06-24; defined terms
2026-07-02; home `cowork_design_doc_template.md`), the **distribution constraint** (2026-06-15)
and the two do-not-revert local patches, and the new rationale-directive entry itself (user,
2026-08-01). Home is `CLAUDE.md` (the OI-237 Kind-2 pattern) unless a layer specification is the
proper home — in which case the entry is ALSO a documentation-gap row (Kind-1 pattern).

**(c) Ratified rulings living only in open-item rows or handoff blocks.** Each becomes an entry
whose home is the row or block that records it: *make it work first — compromise on performance
only if performance proves a problem* (user, 2026-07-28); the large-score requirement (OI-209);
the effort control as ONE setting with several dials, temporally bounding, too early to implement
(2026-07-28); *candidate admission is completion, not refinement* (2026-07-28); *a human acts as
ground truth where no formal ground truth exists* (OI-56, 2026-07-13); intonation kept held as a
declared future consumer (OI-62, 2026-07-13); the voice-independent pedal-point class (OI-194);
the fix-designed-once-over-an-enumerated-family rule (the 2026-07-28 arc); the OI-222 remedy
(withheld findings never enter a mandatory session-start read); the OI-84 A1 rule (retiring code
gets no audit, only the no-information-loss check at deletion); the measurement conventions —
parent-collection mode grading (OI-132), the dual home/local key-agreement column (OI-143), the
abstain-aware regression-stop convention (OI-33). Where you find further rulings of this class
during the reading, add them — this list is Cowork's floor, not a ceiling.

**(d) Standing decision-bearing surfaces, indexed.** One entry per surface pointing at it as a
whole, plus per-decision entries where the surface states discrete rulings: `DEFECT_TYPES.md`
(each defect type is a do-not-do-this ruling; one surface entry suffices unless a type is itself
a ratified standing constraint), `docs/scoring_model.md` §8 (constraints and dead ends — discrete
shelved-with-evidence decisions; enumerate them individually, they are few), the
writing-standards template, and `BUILD_AND_TEST.md`'s measurement policies
(regenerate-before-baseline; the enforced music21 pin).

## Task 4 — gaps found by this pass

Documentation-gap and conflict findings follow the established shape: one `OPEN_ITEMS.md` row
each (index + detail in the same commit), both sides quoted, no fixes. Two named candidates to
check rather than assume: (i) whether a GENERAL rule for our code's allowed dependencies on
existing MuseScore code exists anywhere beyond the two scoped forms already registered (D-072,
D-073) and §17/§18 — if it exists, register it; if it does not, record that as a decision surface
for the user (a missing ruling is the user's to make, not yours); (ii) anything in §6–§16/§18–§19
that contradicts a registered decision.

## Task 5 — regeneration, checks, and the disposition boundary

Regenerate `DECISIONS.md`; `gen_decisions_register.py --check` passes; the DT-12 line-anchor
guard runs over ALL entries, old and new. **The cluster dispositions are NOT redone.** The
Task-3 coverage guarantee (14,460/14,460) stands; new backbone entries may make some of the 6,374
unresolved clusters classifiable, and that refinement is NAMED as deferred (a dated remark in
`disposition_manifest.json`'s successor or the OI-208 note), not silently re-opened here.

## Task 6 — notes and close

Dated notes on OI-207, OI-208 and OI-237; the new rows from Task 4; the `STATUS.md` entry — a
pointer, at the TOP of the file (Task 1e restores the ordering; keep it). Commits per
change-class; the riding `CLAUDE.md` edit in the first commit. Push origin.

## Report

Hashes. Task 1: each correction listed, the cross-reference sweep's wrong-count and cause. Task
2: the rationale-population split (recorded vs "derivation not recorded"). Task 3: entries added
per class, sections read, the before/after entry count. Task 4: gaps and conflicts, counted and
listed. Task 5: the check results. Anomalies each diagnosed; a surprise is a STOP. If you must
stop for feasibility: stop, and propose a partition with measured counts — a successful outcome,
not a failed one.

Standing self-check before reporting: re-read the actual diff of every touched file against the
guiding principles, the conventions, the gate policies, and `DEFECT_TYPES.md`.

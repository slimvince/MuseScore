# Decisions group L — Licensing, contribution, and coding standards

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-116 — The system is a module inside MuseScore Studio, not a plugin

> This system is implemented as a new module (`composing`) within MuseScore Studio's
> existing C++ codebase. It is not a plugin. It integrates directly with MuseScore's
> score model, rendering pipeline, playback engine, and UI infrastructure.

**In plain words.** The harmonic analysis is built into MuseScore Studio's own program code as a new component of it, not added on afterwards as a plugin. It uses MuseScore's own score model, engraving, playback and interface directly.

**Why.** Stated constraint, ARCHITECTURE.md:422-426: the analysis library itself has NO engraving dependency and is pure music theory; the bridge layer is what touches the engraving model. Being a module rather than a plugin is what lets that bridge exist at all.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:626`

**Provenance.** ARCHITECTURE.md:374-378 (§1.2). No date or ratifier stated.

### D-117 — The long-term intent is an official contribution to MuseScore Studio

> The long-term intent is for this to become an official contribution to MuseScore Studio.
> All code follows MuseScore's coding standards, licensing requirements, and contribution
> guidelines.

**In plain words.** The aim is for this work eventually to become part of MuseScore Studio proper, so it is written to MuseScore's own coding, licensing and contribution rules from the start.

**Why.** Derivation not recorded for the intent itself. What the record does state is the consequence it carries (ARCHITECTURE.md:381-382): following MuseScore's standards from the start is what keeps the contribution possible.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:630`

**Provenance.** ARCHITECTURE.md:380-382 (§1.2); restated at ARCHITECTURE.md:6821-6823 (the composing module is 'intended as a future contribution'). ★ READ WITH the CLAUDE.md DISTRIBUTION CONSTRAINT (D-197): the MusicXML declared-mode import patch cfc7eb5e39 is FORK-LOCAL ONLY and must NEVER reach musescore/MuseScore. Two recorded positions - a general intent and a one-patch exception - and the record does not state how the general intent applies to the rest of the tree.

### D-118 — GPL v3, and every external library must be GPL v3 compatible

> All code is licensed under **GPL v3** — consistent with MuseScore Studio's open source
> license. All external libraries used must be GPL v3 compatible.

**In plain words.** All the code is released under the GPL v3 licence, the same licence MuseScore Studio uses, and no outside library may be used unless its licence is compatible with that.

**Why.** Stated constraint, ARCHITECTURE.md:386-387: consistency with MuseScore Studio's own open source licence. A GPL-incompatible library would make the code undistributable with MuseScore.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:636`

**Provenance.** ARCHITECTURE.md:384-387 (§1.3). No date or ratifier stated. The per-file consequence is ARCHITECTURE.md:6654 - a GPL v3 header on every file.

### D-119 — The MuseScore contributor licence agreement is signed before any pull request

> The Contributor License Agreement (CLA) with MuseScore must be signed before any
> pull requests are submitted.

**In plain words.** Before any of this work is offered back to MuseScore as a pull request, the contributor agreement with MuseScore must be signed.

**Why.** SEARCHED 2026-08-09 (CC, `cc_instruction_return_continuation_3.md` Task 2). The record holds no reason. The home states the requirement flatly, inside a licensing section whose neighbouring sentences DO carry a ground — all code under GPL v3, "consistent with MuseScore Studio's open source license", and every external library required to be GPL-v3-compatible. That is the defense of the LICENCE CHOICE, not of the contributor-agreement precondition, and it is deliberately not borrowed for it. No date and no ratifier are stated either, and no alternative is considered.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:639`

**Provenance.** ARCHITECTURE.md:389-390 (§1.3), restated at ARCHITECTURE.md:6750-6752 (§18.3). No date or ratifier stated.

### D-120 — MuseScore's coding style is followed, with clang-format run before every commit

> Follow MuseScore's existing coding style throughout:
> - Formatting defined in `.clang-format` — run clang-format before every commit
> - Naming conventions — consistent with existing MuseScore code
> - File headers — GPL v3 license header on every file (see existing files for template)
> - Include ordering — follow MuseScore's convention

**In plain words.** The code looks like MuseScore's own code: the formatter configuration in the repository is run before every commit, names follow MuseScore's conventions, every file carries the GPL v3 header, and includes are ordered MuseScore's way.

**Why.** Stated constraint, ARCHITECTURE.md:519-523 (§2.8): read how MuseScore already does a thing and follow the same pattern rather than inventing parallel infrastructure - the same reason that governs panels, score traversal, playback, settings and localization.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:7976`

**Provenance.** ARCHITECTURE.md:6649-6655 (§17.1). No date or ratifier stated.

### D-121 — Where MuseScore's documentation practice is minimal, the higher standard applies

> Where MuseScore's documentation practice is minimal, use good practice instead.

**In plain words.** Following MuseScore's conventions does not mean copying how little it documents. Where MuseScore documents sparsely, this project documents properly instead.

**Why.** Stated constraint, ARCHITECTURE.md:6709-6712 (§17.3): the analyzers are the most complex components in the codebase, and a musician with reasonable theoretical knowledge must be able to read them and understand why each decision was made.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:7982`

**Provenance.** ARCHITECTURE.md:6649-6657 (§17.1). No date or ratifier stated.

### D-122 — Every public class and method is documented in musical terms

> Every public class must have a documentation comment explaining:
> - What musical concept it implements
> - What it receives as input (in musical terms)
> - What it produces as output (in musical terms)
> - What it does not handle (important for setting expectations)

**In plain words.** A public class must say which musical idea it implements, what music it takes in, what it produces, and what it deliberately does not handle. A public method must say the same about the musical operation it performs, in musical terms rather than programming terms.

**Why.** Stated constraint, ARCHITECTURE.md:504-508 (§2.6) with :6322-6323: the documentation is written so a person with reasonable musical knowledge and basic programming familiarity can read it, including MuseScore contributors with no familiarity with this codebase at all.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:7986`

**Provenance.** ARCHITECTURE.md:6659-6671 (§17.2). No date or ratifier stated.

### D-123 — Every non-obvious scoring weight or threshold explains its musical reasoning

> Every non-obvious scoring weight or threshold must explain its musical reasoning.

**In plain words.** A number in the scoring code that is not self-evident must be accompanied by the musical reason it has the value it has.

**Why.** Stated constraint, ARCHITECTURE.md:6709-6712 (§17.3): the analyzers are the most complex components, and their weights and thresholds are where the musical judgment actually lives - an undocumented one is unreadable and unarguable.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:7998`

**Provenance.** ARCHITECTURE.md:6673 (§17.2). No date or ratifier stated. ★ This is the rule the 2026-08-01 CLAUDE.md Conventions entry generalizes from scoring values to design decisions as a class (D-195) - and the rule this register's rationale field serves.

### D-124 — The analyzer code must be readable by a musician

> Every scoring weight, threshold, and heuristic must be documented with its musical
> rationale. A musician with reasonable theoretical knowledge must be able to read the
> analyzer code and understand why each decision was made.

**In plain words.** Every weight, threshold and rule of thumb in the chord and key analyzers carries its musical reason, to the standard that a musician with ordinary theoretical training can read the code and see why each choice was made.

**Why.** Stated constraint, ARCHITECTURE.md:6709: these are the most complex components in the codebase, so they are where readability is worth the most.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:8035`

**Provenance.** ARCHITECTURE.md:6707-6719 (§17.3), which gives a worked example from existing code (the circle-of-fifths interval deltas). No date or ratifier stated.

### D-125 — Every test documents the musical situation, the expected result, and what a failure means

> Every test must document:
> - What musical situation is being tested
> - What the expected result is and why it is musically correct
> - What a failure would indicate about the system's behavior

**In plain words.** A test says which musical situation it exercises, what the right answer is and why it is musically right, and what it would mean about the system if the test failed.

**Why.** Stated constraint, ARCHITECTURE.md:6728-6729: the tests must be readable by MuseScore contributors with no deep familiarity with this codebase.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:8048`

**Provenance.** ARCHITECTURE.md:6721-6729 (§17.4). No date or ratifier stated.

### D-126 — One coherent piece of functionality per pull request

> Each pull request should implement one coherent piece of functionality. Large
> pull requests are hard to review. The phased plan in Section 15 defines natural
> PR boundaries.

**In plain words.** Each contribution offered back to MuseScore does one thing.

**Why.** Stated constraint, ARCHITECTURE.md:6744-6746: large pull requests are hard to review, and the phased plan defines where the natural boundaries fall.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:8069`

**Provenance.** ARCHITECTURE.md:6742-6746 (§18.2). No date or ratifier stated.

### D-292 — The fitting-pool licence constraint - values that ship are fitted only on freely-licensed music

> **(e) A value that SHIPS may be fitted only on freely-licensed music.** The pool a ship-intended weight or
> table is estimated on is restricted to public-domain, CC0 and CC-BY sources. Music carrying a
> non-commercial licence or no stated licence — the record names the DCML corpora, MCMA and Essen — may be

**In plain words.** Any number that is fitted and then shipped may be fitted only on public-domain or permissively-licensed music. Music under a non-commercial or unstated licence may be used to check and validate, never to fit a shipped value.

**Why.** A licensing constraint, not a measurement one: fitted values derived from a corpus inherit that corpus's licence terms, and this project ships under GPL v3 (D-118). The record requires the fitting design to state its objective-source versus validation-source split explicitly.

**Status.** LIVE · decided 2026-07-04 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:340-342`

**Provenance.** Recorded in `cowork_handoff_archive.md` (the queue block, marked BINDING on the fitter design), naming `cowork_score_census.md` §8c as the constraint's own block and `cowork_stage5_fitter_design.md` §2/§3a as where it binds. ★ Load-bearing at HEAD and NOT reconciled anywhere in the record this pass read: the joint estimator's tables and weights are fitted on the DCML ground truth, which this constraint names as non-commercial-class and therefore validation-only. Whether the constraint was amended, scoped, or simply not carried forward is not stated. Found by the phase-1e second-partition archive read, 2026-08-02; rowed. ★ RULED by the user 2026-08-02 (OI-271, reading 1): THE CONSTRAINT BINDS, reaffirmed as written. Consequence recorded with the census's own nuance (cowork_score_census.md:239-248): the constraint's class list places the WiR analyses (CC-BY-SA) in the SHIPPABLE pool and the DCML corpora in the NC class — and the record names the 326-chorale ground truth 'WiR/DCML' interchangeably — so the practical consequence turns on a VERIFICATION not yet made: establish at the objects which class the fitted tables' annotation source falls in. If NC-class, the current fitted values are development/validation only and ship-intended values are fitted on the licensed pool at the corpus-onboarding event (OI-38, where the licensing and precision motives converge); if CC-BY-SA, the fit conforms and that establishment is recorded. The verification is OI-271's remaining action. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue). ★ LICENCE-CLASS VERIFICATION AT THE OBJECTS (CC, 2026-08-02, the phase-1f wave, executing the remaining action of the [[OI-271]] ruling). What the fit actually reads: the generators stamp `ground_truth_substrate: dcml_parser.load_wir_regions` and point `WIR_DIR` at `tools/dcml/when_in_rome`, whose loader reads `Corpus/Early_Choral/Bach,_Johann_Sebastian/Chorales/<NNN>/analysis.txt`. ESTABLISHED: (1) that source is NOT a DCML-lab corpus — the DCML corpora sit in sibling directories each carrying its own CC BY-NC-SA 4.0 licence file, while `when_in_rome` is a clone of MarkGotham/When-in-Rome with no licence file at all; so the NC reading this row assumed is REFUTED. (2) NOTHING under `tools/dcml/` is committed to this repository — the whole tree is ignored (`.gitignore:24`) and `git ls-files tools/dcml/when_in_rome` returns zero, so no annotation file is distributed by this fork today. (3) The When-in-Rome README grants CC BY-SA 4.0 to “new content in this repository, including the new analyses, code, and the conversion (specifically) of existing analyses” and defers analyses that originated elsewhere to their original source — and it lists the Bach chorales under “Corpora originating elsewhere” as RomanText analyses by Dmitri Tymoczko and colleagues needing no conversion. (4) No chorale analysis file names a licence or a source: 0 of 371 carry a Source header, against the README’s own claim that links to the original sources appear “within every analysis.txt file”; each names only an analyst and a proofreader, and the per-folder `remote.json` records `analysis_source` as a relative path, not a licensed origin. The scores themselves are the music21 public-domain chorale edition and are not in doubt. VERDICT: the class is NOT NC, and NOT unambiguously CC-BY-SA either — the remaining question is narrower than the row’s and is a question for the WiR maintainers, not for this record. No guess is entered; [[OI-271]] stays open on that narrowed question. ★ HOMED 2026-08-02 (CC, phase 1j, executing the user's per-kind ruling on [[OI-272]]): the constraint is now stated as standing rule (e) of the joint estimator's own specification, with its defense and its ratifying event. Former home preserved (#12): `cowork_handoff_archive.md:2478`, the queue block, marked BINDING on the fitter design. The constraint's detailed per-licence-class block remains `cowork_score_census.md` §8c, which the homed rule cites; that document is NOT a contract home (Cowork-delivered banner, no user-ratified delegation — the phase-1j transitive-authority verification), which is why a homed restatement was owed rather than a pointer.

### D-315 — A one-line fix was made to MuseScore's own chord-symbol parser and is live in the fork

> One line removed: the redundant case-sensitive `tok1 = u"sus"` assignment beside the correct
> lowercase `tok1L = u"sus"` path. The redundant assignment was the underlying cause of the
> "sussus" double-rendering defect in chord-symbol display.

**In plain words.** One line was deleted from MuseScore's own chord-symbol parser because it made every suspended chord with an alteration render its suffix twice. The change is in this fork and has not been sent upstream.

**Why.** Diagnosed at the source: the lowercase parsing path was already correct, and the parallel assignment beside it was the cause of the doubled suffix — stated in the commit message of `b1ba746` and in the drafted upstream report `docs/chordlist_bug_report.md`.

**Status.** LIVE · decided 2026-04-15 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `CLAUDE.md:1350-1352`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Recorded in `STATUS_ARCHIVE.md`. VERIFIED AT THE OBJECTS 2026-08-02: commit `b1ba746` deletes exactly that one line from `src/engraving/dom/chordlist.cpp`, only an upstream header-update commit has touched the file since, and the line is absent at HEAD. This is a THIRD edit to MuseScore's own code beside **D-198** and **D-199**, and it is not in `CLAUDE.md`'s “Local patches — do not revert” section, which carries exactly two subsections; the non-conformance against the ruled **D-229** is rowed at [[OI-273]]. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue). ★ HOMED 2026-08-08 (CC, `cc_instruction_away_execution.md` Task 2) into `CLAUDE.md`'s local-patches section, beside **D-316**, which records the same patch's distribution disposition. **The entry's own text is what settled the owner and what dated it:** it recorded that the section carried exactly two subsections and not this one — true when written, and closed the same day by the subsection the [[OI-273]] ruling added, which is why the home now exists to move into. NO NEW TEXT STATES THE FIX: the subsection already states it, so the homing act is the NAMING that makes the entry findable from the section (#6 — the rule is published once, there), and the verbatim is re-taken from that existing text rather than a copy being written beside it. Its class moves to `process` for the same reason D-316 carries that class: the decision is a record of an edit to a dependency, which the local-patches section is the declared home for. FORMER HOME, PRESERVED (#12): `STATUS_ARCHIVE.md:2262`. FORMER CLASS, PRESERVED (#12): `unhomed`. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "One-line fix in MuseScore core `src/engraving/dom/chordlist.cpp:993` — removed `tok1 = u\"sus\"` from the susPending re-attachment block in `ParsedChord::parse()`. This was a genuine MuseScore core bug causing double-sus render for all sus+alteration chord suffixes. Should be reported upstream." Its closing sentence — that the fix should be reported upstream — is NOT lost by the move: it is the subject of D-316, which rules the disposition UPSTREAMABLE and sits in the same section.

### D-375 — Every real source of difficulty labels is research-only or proprietary — a difficulty-grading feature needs a licence path before it can be sold

> **T-32 caveat: all real label sources research-only/proprietary — commercial use needs a license path.**

**In plain words.** For rating how hard a piece is to play, every collection that carries real labels is either restricted to research or is commercial property; no machine-readable dump from the examination boards or the standard publisher grading exists. So the feature can be built and studied, but shipping it commercially needs a licence arranged first.

**Why.** Established by the union search of 2026-07-04, recorded in `cowork_union_search_record.md` §3, which enumerates the four candidate sources and the restriction on each. The caveat is the harder sibling of the shipped-parameter licence constraint (**D-292**): there the freely-licensed pool exists and merely has to be declared; here no commercially usable label source exists at all.

**Status.** LIVE · decided 2026-07-04 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:272`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8c** — `## 8c. The FULL-NEEDS AUDIT — the union-of-needs mechanism (user question, 2026-07-03)` (heading at line 224). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Its class before the phase-1n staged application was `gap`.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-489 — The snapshot sources are hash-pinned rather than copied in-tree, because their licences make an in-tree copy incompatible with this project's licence

> Because these live in unpinned, gitignored clones, the goldens are byte-meaningful
> only against the manifest's recorded commits. **License:** the four CC BY-NC-SA 4.0
> repos (mozart/chopin/corelli/schumann) plus the no-LICENSE repos
> (bach_chorales/bach_en_fr_suites) make an in-tree copy **GPL-incompatible** —
> hash-pinning (not copying) is the chosen mechanism (audit C1 license check).

**In plain words.** The scores the snapshot test uses are not committed. They are referenced by content hash and fetched from their own repositories, because four of them are licensed in a way that conflicts with this project's licence and two carry no licence at all — so keeping copies here would be a licensing violation, while recording their hashes is not.

**Why.** Stated with the decision and derived from the licences read per repository: four are CC BY-NC-SA 4.0 and two carry no LICENSE file, which together make an in-tree copy incompatible with the project's own licence — so the mechanism is chosen by the constraint, not by preference.

**Status.** LIVE · decided 2026-06-11 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/score_inventory.md:94-98`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** The licence finding of the score inventory's snapshot-suite section (audit C1). Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.)

### D-614 — Every real difficulty-grade label source is research-only or proprietary at origin — a commercial grading feature needs a licence path or its own labels

> **★ AND THE DIFFICULTY-GRADE CASE IS A DIFFERENT PROHIBITION FROM THE FOUR BULLETS ABOVE, STATED APART SO IT IS NOT
> READ AS THE SAME ONE.** Those restrict the pool a **shipped FITTED VALUE** may be estimated on. This restricts a
> shipped **FEATURE** whose labels are somebody else's property. **Every real difficulty-grade label source is
> research-only or proprietary AT ORIGIN:** no machine-readable exam-syllabus dump exists in any form, the open sets
> carry no licence file at all, the gated one is request-access and research-use-only, and the largest carries a
> free-licence badge over research-use-only text. **So a COMMERCIAL grading feature needs a licence path or labels of
> our own** — the held material is enough to validate the idea as research and is not enough to ship it. *Why it is
> stated here and not only where it was found:* this is the section a fitter or a feature design reads before declaring
> its pool, and a designer who meets the fitted-value rule must also meet the case where the constraint bites on the
> feature instead.

**In plain words.** Every collection that says how hard a piece is to play is either restricted to research use or belongs to somebody who sells it. So a difficulty feature in a shipped product would need either a licence agreement or labels of our own; the held material is enough to check the idea works and not enough to ship it.

**Why.** Established by the same search, per source: the two open datasets carry no licence file at all, the gated one is request-access and research-only, and the largest carries a free-licence badge over research-use-only text. The consequence is not inferred but named — the research/commercial split is what the caveat records, and it is the licence-posture instance of the shipped-value constraint **D-292** applied to a feature rather than to a fitted value.

**Status.** LIVE · decided 2026-07-04 · ratified by user

**Home.** `cowork_score_census.md:307-316`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8c** — `## 8c. The FULL-NEEDS AUDIT — the union-of-needs mechanism (user question, 2026-07-03)` (heading at line 224). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_union_search_record.md` §3, the union search round. Read in full by READ WAVE 6, 2026-08-04. The document's status block records the user's disposition of item 3 in terms — *"the T-32 commercial caveat recorded in the product-tool register"* — so the caveat carries the user's act while the search finding behind it names no ratifier. Distinct from **D-292**, which restricts the pool a SHIPPED FITTED VALUE may be estimated on; this restricts a shipped FEATURE whose labels are somebody else's property. ★ RE-HOMED 2026-08-09 into `cowork_score_census.md` §8c, beside the Stage-5 fitting-pool licence constraint, by `cc_instruction_return_continuation_8.md` Task 1, under the user's Ruling 40 of `cowork_rulings_2026_08_09_eighth_stop.md` — STEP 2. Step 1 was CLOSE and did not apply: that constraint's last bullet already says the difficulty case *"carries its own harder version of this caveat"*, which states the FACT and not the consequence, so the rule was written beside it in the section's own voice under the census-edit licence. THE KIND HALF WAS JUDGED BEFORE THE WRITE and this block passes it — it is rule (h)'s own founding case, named in the user's approved Ruling 39 delegation wording as `the §8c shipped-parameter licence-pool constraint`. FORMER HOME, PRESERVED (#12): `cowork_union_search_record.md:87-90`, which is untouched. FORMER VERBATIM, PRESERVED (#12): '**Negatives:** no machine-readable ABRSM/RCM/Trinity syllabus, no Henle dump, no violin/guitar grade dataset. **T-32 caveat recorded:** every real label source is research-only/proprietary at origin — a COMMERCIAL grading feature needs a license path or own labels; CIPI+Mikrokosmos suffice for research validation.' The home text names the label sources by their licence posture rather than by identity, so the rule survives a source list that moves (D-431).


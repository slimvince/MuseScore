# Decisions group I — Module boundaries and code structure

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-070 — Style behaviour is fully data-driven - no conditional logic on style identity

> The C++ implementation contains no conditional logic based on style identity. All
> behavioral differences between musical styles are expressed as parameter values in
> style JSON files.

**In plain words.** Nowhere does the code ask 'is this jazz?'. Differences between styles are numbers in a settings file.

**Why.** Stated constraint, ARCHITECTURE.md:440-442 with the worked wrong/correct pair at :392-402: if behaviour branched on a style's identity, adding or renaming a style would require C++ changes; driving it from parameters means it never does.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:471-473`

**Provenance.** ARCHITECTURE.md:433-436 states the §2 principles are 'hard constraints, not guidelines'; restated at §2.4 :435-438

### D-071 — The analysis layer never produces display strings

> Analysis components produce structured data — they never produce display strings.
> Formatting is handled by separate formatter classes.

**In plain words.** The analysis returns facts. Turning those facts into text on screen is somebody else's job.

**Why.** Stated constraint, ARCHITECTURE.md:483-485: the separation is already established by `ChordSymbolFormatter`, and keeping it means the same analysis can be rendered several ways without the analysis knowing about any of them.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:514-515`

**Provenance.** ARCHITECTURE.md:481-485; mechanically guarded for the joint module by D-017

### D-072 — The dependency rule - the analysis library knows nothing about the score format

> This dependency order is **enforced**. Any code that would invert it (e.g. a composing header forward-declaring `mu::engraving::Note`) must be moved to the notation bridge layer.

**In plain words.** The music-theory library must not know how MuseScore stores a score. Anything that needs both lives in a thin bridge layer in between.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1143`

**Provenance.** ARCHITECTURE.md:1079-1137, checklist at :1424-1431

### D-073 — Single implementation for shared logic; mirroring is a last resort

> Any algorithm that must produce identical results in both the notation bridge and
> `batch_analyze` belongs in the `composing` module (`src/composing/`), not in either
> consumer.

**In plain words.** If the program and the measurement tool must agree, the code that makes them agree lives in one shared place. Copying it into both is a last resort that must be flagged as debt.

**Why.** Stated constraint, ARCHITECTURE.md:536-554: the notation bridge and `batch_analyze` must produce identical results, so shared logic lives in the composing module both call; mirroring is permitted only when a shared implementation is blocked by a dependency constraint, and then only with a marked technical-debt note.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:567-569`

**Provenance.** ARCHITECTURE.md:534-567; the standing project-wide form is CLAUDE.md #6 (total unification)

### D-074 — Analyze and suggest - never modify the score without explicit user action

> The system presents analytical findings and suggestions. It never modifies the main score
> automatically. All score modifications require explicit user action.

**In plain words.** The program tells you what it thinks. It never changes your music unless you ask it to.

**Why.** Stated constraint, ARCHITECTURE.md:527-532: the chord staff, the status bar and the panels are informational - they show what was inferred - and every change to the music is the user's explicit act through standard MuseScore editing.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:558-560`

**Provenance.** ARCHITECTURE.md:525-532

### D-075 — Interface-based design for machine-learning substitutability

> Every component that may eventually be replaced or augmented by a machine learning
> model must be defined behind a pure abstract interface.

**In plain words.** Anything that might one day be replaced by a trained model is hidden behind an interface, so the replacement can be dropped in without touching everything else.

**Why.** Stated constraint, ARCHITECTURE.md:458-460: the rest of the system depends only on the interface, so a machine-learning implementation can replace a rule-based one without any consumer changing.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:489-490`

**Provenance.** ARCHITECTURE.md:456-479; the substitution points are listed at §14.1

### D-076 — Score inspection before diagnosis

> Claude Code does not have direct score access and must not substitute
> statistical inference for visual score inspection.

**In plain words.** When a corpus number looks odd, somebody opens the actual music and looks at it before anyone changes code or runs more statistics.

**Why.** Stated constraint, ARCHITECTURE.md:576-597: score inspection takes two minutes and answers what corpus statistics cannot - the actual texture, whether the chord staff is over-segmenting, whether the opening key is right - and Claude Code has no score access, so it must not substitute statistical inference for looking.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:627-628`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** ARCHITECTURE.md:569-597

### D-077 — The configuration interface is split into two narrow IoC interfaces

> The implode bridge has no business knowing about status-bar display preferences; the analysis bridge has no business knowing about chord-staff output settings.

**In plain words.** Settings are exposed through two small interfaces rather than one big one, so each component can only see the settings it actually needs.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1692`

**Provenance.** ARCHITECTURE.md:1595-1607, restated at :2967-2978

### D-078 — The cross-layer value types live in a dependency-free leaf header

> **The cross-layer value-types LEAF** — a dependency-free header (STL only; no `chord/`, `key/`, or engraving includes) holding the value types that cross the L1.5 / L3 / L4 boundaries

**In plain words.** The small data types that several stages share live in one header that depends on nothing, which removed two places where a lower stage had to include a higher one.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1526`

**Provenance.** ARCHITECTURE.md:1439-1447

### D-107 — American English throughout

> All identifiers, comments, and documentation use American English spelling.

**In plain words.** Analyzer, not analyser; color, not colour.

**Why.** Stated constraint, ARCHITECTURE.md:492-502: MuseScore's own codebase is American English, so one spelling convention throughout is what keeps identifiers matching across the boundary.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:525`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** ARCHITECTURE.md:492-502; restated in CLAUDE.md Conventions

### D-108 — Cross-platform by default

> All code must run on every platform officially supported by MuseScore Studio: Windows,
> macOS, and Linux.

**In plain words.** Everything must work on Windows, macOS and Linux; platform-specific code is allowed only where unavoidable and must be walled off.

**Why.** Stated constraint, ARCHITECTURE.md:676-682: the code must run on every platform MuseScore Studio officially supports, so platform-specific code is permitted only when unavoidable and must be abstracted so the rest of the module stays platform-agnostic.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:709-710`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** ARCHITECTURE.md:676-682

### D-227 — Read how MuseScore already does it, and never invent parallel infrastructure

> Before implementing anything that touches MuseScore's existing infrastructure —
> UI panels, score traversal, playback, settings, localization — read how MuseScore
> already does it and follow the same pattern. Do not invent parallel infrastructure.

**In plain words.** Before touching anything MuseScore already provides - panels, walking the score, playback, settings, translation - the existing MuseScore code for it is read and followed. A second, parallel mechanism of our own is never created.

**Why.** Derivation not recorded as a separate defense. Its consequences are recorded across the document and are what the rule buys: the panel infrastructure (§12.1), the localization path (§12.1), the accessibility patterns (§12.1), the coding style (§17.1), and the preview pathway (§10.5) all resolve by this rule rather than by separate argument.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:552`

**Provenance.** ARCHITECTURE.md:519-523 (§2.8). No date or ratifier stated. This is the GENERAL form of the relationship to existing MuseScore code; the two scoped forms are D-072 (the analysis library depends on no engraving type) and D-073 (shared logic has one implementation). What none of the three states is which MuseScore interfaces our bridge code may call - see OPEN_ITEMS OI-241.

### D-228 — The bridge pattern - engraving types enter and leave at named free functions in the notation namespace

> - Takes engraving types as input (Note*, Score*, Fraction, …)
> - Produces composing-domain results (ChordAnalysisResult, HarmonicRegion, …)
> - Lives in `mu::notation` namespace
> - Is declared in a `notation/internal/notation*bridge.h` header
> - Is defined in the corresponding `notation/internal/notation*bridge.cpp`
>
> **Callers** of bridge functions include only the notation-side bridge header, not composing headers, for the function itself. They may still include composing headers for the composing types in the function signature.

**In plain words.** The only code that may take MuseScore's own score objects and turn them into analysis results is a plain function living on the notation side, declared in a bridge header and defined in the matching bridge source file. Whoever calls it includes the bridge header, not the analysis headers, for the call itself.

**Why.** Stated constraint, ARCHITECTURE.md:1123-1127: the analysis library is pure music theory and can be unit-tested in complete isolation - no score, no staves, no interface - which is what makes its test suite fast and reliable. If analysis headers imported engraving types the tests would have to link the whole engraving library, and more fundamentally the music theory would carry knowledge of one particular score format, a coupling that makes the algorithms harder to reuse or replace.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1191`

**Provenance.** ARCHITECTURE.md:1129-1140 (§3.3, the bridge pattern), with the enforcement statement at :955 (D-072) - any code that would invert the dependency order must be moved to the bridge layer. The bridge file inventory at :977-985 is the as-built list. No date or ratifier stated.

### D-229 — The MuseScore-dependency rule - one general rule for what our code may depend on

> 1. **The analysis library (`composing`) depends on no MuseScore or engraving types** — the
>    Dependency Rule above, unchanged.
> 2. **The bridge layer reads the score model only through the established bridge pattern, and
>    never layout-derived state as analysis input.** The Layer-1 note model is the single
>    sanctioned reading surface for analysis facts; positions, spacing and other layout products
>    are presentation outputs, readable only for placing presentation artifacts, never as
>    inference evidence (a layout read entering analysis is the OI-98 class, judged against this
>    rule).
> 3. **Editing MuseScore's own code is admissible only for a defect blocking our feature.** Each
>    instance is recorded in `CLAUDE.md`'s local-patches section with a do-not-revert note and an
>    explicit per-instance distribution disposition (upstreamable or fork-local), ratified by the
>    user. The recorded contribution intent (§1.2) governs our module as a whole; distribution is
>    decided per patch — the fork-local constraint on the MusicXML mode-import patch is such an
>    instance, not a contradiction of the intent.

**In plain words.** Three parts. The music-theory library uses no MuseScore code at all. The bridge code that connects analysis to the score reads the score only through the established bridge functions, and never uses layout results (positions, spacing) as analysis input - the note reader is the one sanctioned reading surface. And changing MuseScore's own code is allowed only to fix a defect blocking our feature, each change recorded, with its distribution (upstreamable or fork-only) decided and ratified case by case.

**Why.** Stated at the rule's home (ARCHITECTURE.md:1115-1121): derived from the already-ratified scoped forms (the Dependency Rule, the bridge pattern, the local-patches constraints) rather than invented (#1); one rule where practice-by-example governed (#6/#7); the layout exclusion because layout is presentation downstream of the facts (a layout read entering analysis is a layer inversion and the self-feedback class); the per-instance patch ratification preserves #14 and reconciles the §1.2 contribution intent with the fork-local patch constraint.

**Status.** LIVE · decided 2026-08-02 · ratified by user

**Home.** `ARCHITECTURE.md:1150-1163`

**Provenance.** User ruling 2026-08-02 at the OI-241 adjudication (all recommendations adopted); written into ARCHITECTURE.md §3.3 in the same commit (the register's same-commit rule, D-230). open_items/OI-241.md records the gap this closes.

### D-233 — Build and test commands run synchronously; one run, one result

> **Rule 14 — Shell discipline for long-running commands**
>
> All build and test commands must run synchronously (foreground). Never use background jobs or split output.

**In plain words.** Every build and test command is run in the foreground and its output is read whole. A command is never backgrounded, never killed and re-run differently, and never silently re-run: unexpected output is reported and instructions asked for.

**Why.** Derivation not recorded. The record states the rule and its correct/incorrect patterns (ARCHITECTURE.md:627-649) but not the incident or measurement that produced it.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:654-656`

**Provenance.** ARCHITECTURE.md:623-625 (Rule 14) and :649 (the one-run-one-result statement) ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-296 — READING MuseScore's engraving code is allowed from anywhere we may edit; only EDITING the notation and engraving code is off limits

> 4. **READING and CALLING MuseScore's engraving code is allowed from anywhere we may edit; only EDITING
>    the notation and engraving source is off limits.** Clause 3's prohibition is on changing
>    `src/notation` and `src/engraving` code, not on consulting it: any code we are entitled to write may

**In plain words.** Our code may call into and read from MuseScore's own score and engraving code wherever we are allowed to write. What is out of bounds is changing MuseScore's notation and engraving source itself.

**Why.** A user correction of an over-statement that had conflated the two. Its worked consequence is recorded with it: a measurement that needed fermatas read them in the batch tool, which already loads the score, and passed them into our own analysis through our own input structure - zero edits outside our area.

**Status.** LIVE · decided 2026-06-14 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:1164-1166`

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-14 Stage-4c block) as a standing lesson. Bears directly on D-229, the general MuseScore-dependency rule the user adopted 2026-08-02: this is the EDIT-versus-READ half, stated a month and a half earlier and consistent with it. D-229 adds what the bridge may read (the score model through the bridge pattern, never layout-derived state) and when an edit to MuseScore's own code is admissible. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue). ★ HOMED 2026-08-02 (CC, phase 1j, executing the user's per-kind ruling on [[OI-272]]): written as clause 4 of the MuseScore-Dependency Rule in `ARCHITECTURE.md` §3.3, beside D-229 — the home this row's own text named. Former home preserved (#12): `cowork_handoff_archive.md:3732`, the 2026-06-14 Stage-4c block.

### D-311 — The chord-analyzer file split happens once — the SEQUENCING is spent (the split happened first, not last); the once-only LESSON is what carries forward

> **Stage 4 — R9: the `chordanalyzer.cpp` file split (OWED #1), LAST.** "Split once," after the E4 removals.

**In plain words.** Breaking the large chord-analysis source file into smaller ones was to wait until the code destined for deletion had been deleted, so that it happened once rather than twice. It did happen once — but in June 2026, BEFORE those deletions, not after. So the ordering instruction no longer governs anything: there is nothing left to sequence. What survives is the lesson it was an instance of — restructure once, after the boundaries have stabilized — which is what later work cites it for.

**Why.** The reason is stated with the rule — “split once”: performing the split before the removals would produce a structure the removals then invalidate. The record does not say why the split was nonetheless performed first; the delivering commit gives its own immediate purpose (“isolates the gate layer for refactor #2”), which is a reason for doing it, not a reason for doing it out of order, and no ruling reconciling the two exists. That gap is stated rather than filled.

**Status.** SUPERSEDED IN FACT · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_engage_arc_plan.md:126`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `STATUS_ARCHIVE.md` (session 22i, the Stage-5 planning checkpoint) as a ruling read off the ratified retirement map. It is load-bearing now beyond its original subject: [[OI-205]] half (b) cites it as “the ratified Stage-3.5 file-split lesson (restructure ONCE, after the boundaries stabilize)” to time the `ARCHITECTURE.md` restructure. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue). ★ HOME MOVED 2026-08-02 (CC, phase 1j, executing the user's per-kind ruling on [[OI-272]]) — NO specification text was written, because the rule already stands verbatim in a user-ratified document that owns the concern: `cowork_engage_arc_plan.md` (RATIFIED by the user, 2026-07-07) is 'the standing reference for the order of work', and its Stage 4 states the split is last and why. Former home preserved (#12): `STATUS_ARCHIVE.md:166`, session 22i. The arc plan is NOT a contract home (it is a plan, not a contract for a layer — the phase-1i criterion), so the classification stays 'gap'; what changes is that the decision is no longer recorded ONLY on a tracking surface. D-401 restates the same sequencing at the 2026-08-02 structural audit; the two are consistent and neither supersedes the other. ★ RESTATED 2026-08-03 (user ruling on `OPEN_ITEMS.md` OI-286, applied at phase 1m). **Former title, preserved (#12):** “The chord-analyzer file split happens once, after the retirements have settled — not before”. **Former status, preserved (#12): DEFERRED** — stale, because the act it defers was performed on 2026-06-17 as commit `41f7c65f63` (verified at the object; register entry **D-427**), before this ruling was even read off the retirement map at the 2026-07-03 Stage-5 checkpoint. The new status is **SUPERSEDED IN FACT** in the register's exact sense: a later BUILD performed what this decision governs, and no ruling names it — it is deliberately not upgraded to “superseded by”. **The verbatim and its home are unchanged**, because `cowork_engage_arc_plan.md` still says what it says and a ratified surface is annotated, never rewritten. **What does NOT lapse:** the once-only lesson, which `OPEN_ITEMS.md` OI-205 half (b) cites as “the ratified Stage-3.5 file-split lesson (restructure ONCE, after the boundaries stabilize)” to time the `ARCHITECTURE.md` restructure; that citation stands and is unaffected by this entry's status. **The LEGACY mark is REMOVED from this entry**, not by a sweep but on established evidence: its subject is `chordanalyzer.cpp`, which `STATUS_ARCHIVE.md`:114 records as surviving the engagement (“R9 *splits* `chordanalyzer.cpp`, does not delete it”), and one of the five translation units the split produced, `chordsymbolformatter.cpp`, is run by the record arm at `notationimplodebridge.cpp`:1170. This entry is one of the two demonstrated errors that caused the LEGACY marker's wording to be weakened on the same date; the other is D-329, and the re-verification of the whole marked set is `OPEN_ITEMS.md` OI-289. The renames half of OWED refactor #1, which this entry never covered, is **D-428**.

### D-401 — The refactor sequencing call — the portable unification wins run before Layer 5, the legacy-path tangles fold into the decoder engagement, and the file split is last

> **In one line:** *pre-L5 = FQ-1, FQ-3, FQ-5, FQ-6, FQ-7 (portable unification wins); part-of-L5/E4 = FQ-2,
> FQ-4, FQ-8 (the legacy-path tangles the decoder + §6-block dissolution retire); then R9 splits the file
> last.* This adds no new stage — it slots the audit's fixes into the plan the roadmap already has.

**In plain words.** The structural debt found across the built layers is ordered into one sequence rather than fixed as it was found. What is independent of which analysis path runs — the shared different-root scan, moving the neighbour-chord computation out of the derived-view layer, the duplicated fact-layer helpers, the two disagreeing alternative-list views, and sourcing the key decoder's constants from shared symbols — is done first, because none of it depends on the replacement decoder. The tangles that live in the legacy chord path fold into the engagement that retires that path, because fixing them separately would be work thrown away. Splitting the large chord-analysis source file comes last, after the deletions, so it is split once.

**Why.** The record gives the reason as a measured property of the code, not a preference: the anchor tangle sits in code the engagement retires, and its clean target is ALREADY BUILT in the dormant decoder (§1.4, cited to `chord/chordslicedecoder.cpp:746-789`), so a standalone refactor of the legacy carry substrate would be throwaway work on retiring code — while three slices are genuine early wins precisely because they are path-independent or serve both paths (§4).

**Status.** LIVE · decided 2026-07-07 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_structural_integrity_audit.md:326-328`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1i continuation wave, 2026-08-02, reading `cowork_structural_integrity_audit.md` IN FULL. The document's banner records `Status: read-only grounded catalogue (CC, 2026-07-07; Engage arc #6)` — an authored catalogue, not a ratified contract. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1i ratification queue. The document itself says the sequencing call is brought to the user (`:345-346`), and the record does not show that happening. What the record DOES show is a delegation: the user-RATIFIED `cowork_engage_arc_plan.md` (2026-07-07) states that it 'does not re-derive the fix details — those live in `cowork_structural_integrity_audit.md` (§3 fix-queue, §4 sequencing)'. Whether a ratified plan's delegation ratifies the delegated content is the [[OI-268]] question in another form; it is NOT decided here, and the entry carries the record's own status. ★ RATIFIED (user, 2026-08-02, the phase-1i queue).

### D-404 — Relocating the neighbour-chord temporal-context computation out of the derived-view layer is DEFERRED to the decoder engagement, which owns regional temporal context

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **FQ-3 — ⛔ STOP-and-deferred to E4 (UNCLEAR-7 resolved → fold into E4).** Byte-identically relocatable
>   and decoder-independent, BUT E4-entangled: the decoder (already seeded by `findTemporalContext` at
>   `regionanalyzer.cpp:899-902`, `decoder.commit()≡advanceTemporalContext`) is the E4-decided owner of
>   regional temporal context (ARCHITECTURE.md D-P4/D-BRIDGE/1068: the cold walk is superseded). Relocating
>   to an interim L4 home now is the "redone at E4" case; most-invasive item (new region unit + notation
>   wrapper + test relocation). Deferred, not forced (report §6).

**In plain words.** A view-only helper in the derived-view layer runs the whole chord-decision pipeline twice to work out the identity of the neighbouring chords — a decision-layer computation living in a layer that is supposed only to expose views of the notes. Moving it was verified to be possible without changing any output, but it was deferred: the replacement decoder is the decided owner of regional temporal context, so an interim home would be built and then undone.

**Why.** The record gives both halves. The reason it is a violation is grounded at the code (the derived-view primitive instantiates the chord analyzer and runs the full decision pipeline twice, on the live path). The reason it is deferred rather than fixed is that the decoder is already seeded by this same helper and its commit step is the temporal-context advance, so the ownership move belongs to the engagement — making an interim relocation the redone-later case, and it is also the most-invasive item in the queue (a new region unit, a notation wrapper, and a test relocation).

**Status.** DEFERRED · decided 2026-07-07 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_structural_integrity_audit.md:270-275`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1i continuation wave, 2026-08-02, reading `cowork_structural_integrity_audit.md` IN FULL. The document's banner records `Status: read-only grounded catalogue (CC, 2026-07-07; Engage arc #6)` — an authored catalogue, not a ratified contract. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1i ratification queue. Recorded as '⛔ STOP-and-deferred to E4'. The deferral's target — the engagement of the dormant decoder with the function layer — was itself overtaken by the joint estimator without any ruling that names it (`ARCHITECTURE.md`'s Layer-4 plan correction, 2026-08-02; `OPEN_ITEMS.md` OI-259 re-dispositions the engage-era agenda), so what becomes of this deferral is open. ★ RATIFIED (user, 2026-08-02, the phase-1i queue).

### D-416 — Two structural refactors are DEFERRED and OWED, and must be surfaced at every planning checkpoint until done

> **⛔ TWO DEFERRED STRUCTURAL REFACTORS — DO NOT FORGET (user mandate 2026-06-14):** (1) **Stage 3.5**
> the physical split of `chordanalyzer.cpp` along the layer seams + iteration-API renames — DEFERRED until
> the layer boundaries stabilize; (2) **Stage 5** the dissolution of the post-hoc gate-correction layer
> (Gates A–L) into fitted weights — the gates are still load-bearing (3.4 retired none). Neither blocks the
> current Stage-4 key work, but both are OWED and must be surfaced at every planning checkpoint until done.
> Mirrored in `cowork_handoff.md` (top standing block).

**In plain words.** Two pieces of restructuring were postponed rather than dropped: splitting the large chord-analysis source file along its layer seams (with the iteration-era function names renamed), and dissolving the layer of after-the-fact correction rules into fitted weights. Neither may be quietly forgotten — each planning checkpoint has to raise them until they are done.

**Why.** Each half carries its own stated reason. The file split waits because the layer boundaries have not stabilized — splitting before they do would mean splitting twice (the same reason register entry D-311 records as "split once"). The correction-rule dissolution waits because the rules are still load-bearing: the gate-retirement stage retired none of them, so removing them now would remove work nothing else does. The surfacing obligation is the remedy for the failure mode a deferral has — a postponed item with no carrier becomes a dropped one.

**Status.** LIVE · decided 2026-06-14 · ratified by user

**Entry ratified.** 2026-08-03 · by user

**Home.** `docs/implementation_roadmap.md:28`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `docs/implementation_roadmap.md`:20-25, recorded as a user mandate of 2026-06-14 and mirrored, the record says, in `cowork_handoff.md`'s top standing block. Beside register entry D-311, which records the FILE-SPLIT half alone as deferred until after the retirements, and D-401, which sequences it last; the half registered nowhere until now is the gate-dissolution, together with the surfacing obligation that covers both. Found by the phase-1k continuation wave, 2026-08-03, reading `docs/implementation_roadmap.md` IN FULL (the OI-207 reading list's next document, 18 clusters). The document's own banner records it as the SINGLE TRACKER ensuring every review conclusion is addressed (`:4-8`); it carries none of the four declared status banners (register entry D-256), so it is not a contract home. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1k ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1l queue — ratified AS DRAFTED, with the status exactly as the record states it; the ratification is of each RULE itself, and it supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.) ★ THE PHASE-1l DISPOSITION WAS NOT WRITTEN — the check that had to precede it did not confirm its premise, so it is a STOP (#13) rather than a ruling. What the check found, at the code and the record, 2026-08-03: HALF (1)'s file split is DELIVERED, not owed — committed `41f7c65f63` on 2026-06-17 ('split chordanalyzer.cpp into single-responsibility layer TUs (byte-identical)'), three days after this mandate deferred it, producing the five sibling translation units `chordsymbolformatter.cpp` / `chordvoicing.cpp` / `chorddiagnose.cpp` / `chordpostpasses.cpp` / `postscoringgates.cpp` beside the residual oracle, and recorded as the current layout at `docs/scoring_model.md`:26-37. It IS the same named act as D-311's R9 — `docs/implementation_roadmap.md` writes 'R9 `chordanalyzer.cpp` file-split (OWED refactor #1)' in so many words. HALF (1)'s iteration-API RENAMES are NOT done: `applyIter8691Pedal` is still the declared name in `chordanalyzer.h`, defined in `chordpostpasses.cpp` and called from `sectionanalyzer.cpp`:450 and `regionanalyzer.cpp`:1011. And the premise that both halves' subjects are legacy is FALSE: one of the five translation units the split produced, `chordsymbolformatter.cpp`, is LIVE production code on the record arm (`notationimplodebridge.cpp`:1159-1170 and :1189-1191 call `formatSymbol` / `formatNashvilleNumber` on the record arm explicitly; `sectionrecordadapter.h`:69-71 names them the record path's presentation derivations), and `STATUS_ARCHIVE.md`:114 records the residual `chordanalyzer.cpp` as one that 'SURVIVES the engagement; R9 *splits* `chordanalyzer.cpp`, does not delete it'. A disposition of 'superseded by D-418 — the subject is deleted rather than refactored' would therefore have been false of the subject. The contradiction of record this surfaced is rowed as `OPEN_ITEMS.md` OI-286; the disposition itself waits on the user. The surfacing obligation stands in the meantime, unchanged. ★ DISPOSITIONED 2026-08-03 (user ruling, applied at phase 1m): **split into its three real components, each dispositioned on its own evidence** — **D-427** the physical file split (DELIVERED, commit `41f7c65f63`, 2026-06-17), **D-428** the iteration-API renames (STILL OWED, subject partly LIVE, no LEGACY mark), **D-429** the gate-layer dissolution (STILL OWED, subject dormant on both production surfaces, principle TRANSFERRED to the phase-3 family design). The three-way split is Cowork's reading of this one mandate, user-ratified on that date — a reconstruction, labelled as one; the record held one mandate with two numbered halves. **THIS ENTRY IS NOT RETIRED AND ITS STATUS DOES NOT MOVE:** it is a correct record of what the user mandated on 2026-06-14, and the mandate said what it said. **The surfacing obligation stands** for D-428 and D-429 until they are done. The five later records that still called half (1) owed and parked — the retirement map (D-418), `STATUS_ARCHIVE.md`:166, `cowork_stage5_fitter_design.md`:103, `cowork_structural_integrity_audit.md`:313-314 and D-311 — were corrected in the same act, each with a dated annotation naming the ruling and none of them edited in its original wording (#12).

### D-427 — Component (1a) of the two-deferred-refactors mandate — the physical `chordanalyzer.cpp` file split: DELIVERED 2026-06-17

> Split `chordanalyzer.cpp` along the now-real layer seams

**In plain words.** The large chord-analysis source file was to be broken along its layer seams. It was: on 17 June 2026 the file lost 2,178 lines into five sibling files, one per responsibility. This component is done, and the register records it as done rather than as owed.

**Why.** The reason for splitting is stated with the item — the seams are "now-real", so a split along them is meaningful where an earlier one would not have been; the companion reason for splitting ONCE is register entry D-311's "split once". The delivering commit's own message adds the immediate purpose: it "isolates the gate layer for refactor #2" — the split was performed in service of the mandate's other half, which is why it happened three days after the mandate deferred it rather than years later.

**Status.** LIVE · decided 2026-06-14 · ratified by user

**Home.** `docs/implementation_roadmap.md:492`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** A component of the 2026-06-14 user mandate registered as **D-416**, whose parent entry carries the mandate's full text. The split of the one 2026-06-14 mandate into three components is **Cowork's reading of that mandate, user-ratified 2026-08-03** — a reconstruction, labelled as one. The record never held three items: it held one mandate with two numbered halves, the first of which has two halves of its own. **D-416 remains RATIFIED and is not retired** — it is a correct record of what the user mandated; what these entries carry is each component's own disposition on its own evidence. **DELIVERED, established at the object:** commit `41f7c65f63` (2026-06-17 08:23 +0200) — "split chordanalyzer.cpp into single-responsibility layer TUs (byte-identical; oracle residual + formatter/voicing/diagnose/post-passes/gates); isolates the gate layer for refactor #2" — removes 2,178 lines from `src/composing/analysis/chord/chordanalyzer.cpp` and adds `chordsymbolformatter.cpp` (1,054), `postscoringgates.cpp` (586), `chordpostpasses.cpp` (297), `chordvoicing.cpp` (233) and `chorddiagnose.cpp` (188), touching nothing else but `CMakeLists.txt` and `docs/scoring_model.md`. `docs/scoring_model.md`:26-37 records the resulting layout as current. It is the same named act as **D-311**'s R9 and as roadmap item 3.5's first clause — `docs/implementation_roadmap.md` writes "R9 `chordanalyzer.cpp` file-split (OWED refactor #1)" in so many words. **Two things this component is NOT.** It is not a retirement: `STATUS_ARCHIVE.md`:114 records the residual `chordanalyzer.cpp` as one that "SURVIVES the engagement; R9 *splits* `chordanalyzer.cpp`, does not delete it", and one of the five units it produced, `chordsymbolformatter.cpp`, is LIVE production code on the record arm (`notationimplodebridge.cpp`:1159-1170 and :1189-1191 call `ChordSymbolFormatter::formatSymbol` / `formatNashvilleNumber`, the second on BOTH arms; `sectionrecordadapter.h`:69-71 names them the record path's presentation derivations) — so this component's subject is NOT the dormant pipeline and it carries no LEGACY mark. And it did not follow the sequencing D-311 and the retirement map state: the split preceded the E4 removals rather than following them. "Split once" holds in the sense that exactly one split has happened, and no second split is licensed. **Found** 2026-08-03 by the phase-1l code check that had to precede D-416's disposition, rowed at `OPEN_ITEMS.md` OI-286; the five later records that still called it owed and parked are corrected at phase 1m, each with a dated annotation naming the user's ruling. Every code fact below was read with the file tools in the phase-1m session, 2026-08-03; commit `41f7c65f63` was verified at the object by explicit hash. NOT RATIFIED as an ENTRY — it goes to the user in the phase-1m ratification queue.

### D-428 — Component (1b) of the two-deferred-refactors mandate — the iteration-vocabulary API renames: STILL OWED, and the subject is the LEGACY arm

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> rename iteration-vocabulary APIs (`applyIter8691Pedal` → descriptive names)

**In plain words.** Functions still named after the numbered experiments that produced them — chiefly `applyIter8691Pedal` — were to be given names that say what they do. They have not been. Every place that name is used sits on the older stage-by-stage analysis path, on one of its orchestrators, in its diagnostic view or in its tests — so this is naming debt on code awaiting deletion, not on the code that runs, and deleting that path discharges it. The entry said the opposite until 2026-08-03; the correction and the check behind it are in the provenance.

**Why.** The reason is the one the mandate's parent gives for the whole item and the back-half verification method states in terms: "a layer can't be cleanly audited while physically tangled in `chordanalyzer.cpp` or smeared across the post-hoc gate layer" (`docs/implementation_roadmap.md`, the back-half verification method, user, 2026-06-14). A name that records which experiment produced a function tells a reader nothing about what it does, which is the same auditability cost one level down.

**Status.** DEFERRED · decided 2026-06-14 · ratified by user

**Home.** `docs/implementation_roadmap.md:492`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** A component of the 2026-06-14 user mandate registered as **D-416**. The split of the one 2026-06-14 mandate into three components is **Cowork's reading of that mandate, user-ratified 2026-08-03** — a reconstruction, labelled as one. The record never held three items: it held one mandate with two numbered halves, the first of which has two halves of its own. **D-416 remains RATIFIED and is not retired** — it is a correct record of what the user mandated; what these entries carry is each component's own disposition on its own evidence. **NOT DONE, established at the code:** `applyIter8691Pedal` is still the declared name at `src/composing/analysis/chord/chordanalyzer.h`:729, defined at `src/composing/analysis/chord/chordpostpasses.cpp`:119, and called at `chordanalyzer.h`:752 (an inline helper), `chordpostpasses.cpp`:249 (its own second pass), `sectionanalyzer.cpp`:450, `regionanalyzer.cpp`:1011, :1229 and :1419, `harmonicsegmenter.cpp`:394, :403, :546, :743, :820 and :912, `notationcomposingbridge.cpp`:663, `regiontoneprimitives.cpp`:511 and :569, `chorddiagnose.cpp`:172, and in the test suites at `tests/test_helpers.h`:122 and throughout `tests/postscoringgates_tests.cpp`. Roadmap item 3.5 names this half and carries no done mark. **★ CORRECTED 2026-08-03 (phase 1n, on the user's ruling that the premise be settled before this classification stands). This entry said until today: "Its subject is PARTLY LIVE, so it is NOT legacy work and carries no LEGACY mark", on the single ground that `regiontoneprimitives.cpp` hosts the Layer-1.5 primitive `OPEN_ITEMS.md` OI-165 records as "not currently scheduled to die". That ground does not hold, and the entry is now LEGACY-marked.** The check is written into OI-165 as an answer and is summarized here. (a) That phrase is accurate about SCHEDULING — no item of either retirement map names the primitive, and OI-165 says so itself — and was being read as a claim about SURVIVAL, which it does not support. (b) The primitive has exactly two production call sites, `regionanalyzer.cpp`:921 and `notationcomposingbridge.cpp`:651, and BOTH are on the legacy arm, established at the branch: `analyzeHarmonicContextAtTick` returns the record view at `notationcomposingbridge.cpp`:737 whenever `useJointNotationRecord()` is true (the default), above the fallback that holds the second site — which `ARCHITECTURE.md`:4098 already records as having "no production caller" — and `analyzeRegions`, which holds the first, is entered only from `analyzeHarmonicRhythm` ("legacy-arm only", `ARCHITECTURE.md`:4099) and from `batch_analyze.cpp`:601, which `--joint-inference` returns above at `batch_analyze.cpp`:5590-5601. (c) No consumer for the primitive is named anywhere in the record; what the record names instead is a REPLACEMENT — `ARCHITECTURE.md`:1607-1608, "The decoder's path state supersedes `findTemporalContext`'s cold walk", and **D-404**. **And the correction does not rest on that primitive alone:** the whole enumeration above was re-checked this session against the two production surfaces, and EVERY call site of `applyIter8691Pedal` is on the legacy chord analyzer and its post-passes (`chordanalyzer.h`, `chordpostpasses.cpp`, `postscoringgates.cpp` — the "legacy chord competition + Gates A-L" of retirement item R1), on one of that path's orchestrators (`sectionanalyzer.cpp`:450 inside the legacy `analyzeSection`; `regionanalyzer.cpp` inside `analyzeRegions`; `harmonicsegmenter.cpp` inside `greedyExpandSegmentation`, whose only production caller is `regionanalyzer.cpp`:872), on the dead P4 fallback (`notationcomposingbridge.cpp`:663), in the legacy analyzer's diagnostic view (`chorddiagnose.cpp`:172, `diagnoseChord`, called from tests only), or in the test suites. **No file under `src/composing/analysis/joint/` names the symbol at all.** So this component is LEGACY CLEANUP that the retirement discharges, not live debt: the A1 verdict of the audit plan (`OPEN_ITEMS.md` OI-84 — code that retires gets no audit, only the #12 no-information-loss check at deletion; the rule's home is `cowork_audit_protocol.md` P9, register entry **D-209**) applies to it. The surviving obligation is therefore the #12 check at the moment of deletion, not a rename pass. **What this correction does NOT establish**, stated because an insulation claim must enumerate its false-negative paths (#17e): dormant is not deleted and the record flag is a runtime setting with a declared reverse map; the diagnostic surface (`batch_analyze` without `--joint-inference`, which `CLAUDE.md` gate block (C) still presents as runnable) still reaches this code; the tests are a consumer; and the FILE `regiontoneprimitives.cpp` is a mixed unit whose other symbols have their own lifetimes — this entry's subject is the SYMBOL, not the file. The full enumeration is at OI-165 §5. **Renaming a symbol is a code change**, and the three-phase rule **D-231** forbids fix design before phases 1-2 complete, so this component is RECORDED and not performed. The surfacing obligation D-416 imposes stands for this component until it is done. Found with D-427 at the phase-1l code check, rowed `OPEN_ITEMS.md` OI-286. Every code fact in this entry was read with the file tools in the phase-1m session (the call-site enumeration) or the phase-1n session (the arm check and the correction), both 2026-08-03; commit `41f7c65f63` was verified at the object by explicit hash. NOT RATIFIED as an ENTRY — it goes to the user in the ratification queue, now carrying the phase-1n correction as well as the phase-1m entry.

### D-429 — Component (2) of the two-deferred-refactors mandate — dissolving the post-hoc gate-correction layer into fitted weights: STILL OWED, and its PRINCIPLE binds the live design

⚠ **LEGACY IN ITS LETTER — TRANSFERRED IN ITS PRINCIPLE.** The text of this decision belongs to the dormant pipeline awaiting deletion at the retirement map, and goes with it. Its principle does NOT: a ruling carried that across to the live design, and the plain restatement below names the ruling. Read it before concluding this decision lapsed (marking convention user-ratified 2026-08-02).

> **Stage 5** the dissolution of the post-hoc gate-correction layer
> (Gates A–L) into fitted weights — the gates are still load-bearing (3.4 retired none).

**In plain words.** The layer of after-the-fact correction rules laid over the old chord scorer was to be dissolved: each correction becomes a weight the model learns, rather than a rule applied afterwards to patch the answer. It has not been. The RULE ITSELF — a correction belongs in a factor's fitted value, never in a layer of corrections over the decode — was carried across to the current estimator by the user's ruling of 2026-08-03 and binds the coming family design; only the legacy text goes with the legacy code.

**Why.** The mandate states the reason for the deferral, not for the rule: the gates were still load-bearing, the gate-retirement stage having retired none of them, so removing them then would have removed work nothing else did. The reason for the RULE is the one the estimator's specification gives for its own standing rule (a) and `CLAUDE.md` #8 / `DEFECT_TYPES.md` DT-2 give generally: a correction applied after the decision is fitted to the cases that motivated it and measures nothing on the next one, whereas a correction expressed as a factor value is fitted once, graded held-out, and cannot be tuned per case.

**Status.** DEFERRED · decided 2026-06-14 · ratified by user

**Home.** `docs/implementation_roadmap.md:30`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** A component of the 2026-06-14 user mandate registered as **D-416**. The split of the one 2026-06-14 mandate into three components is **Cowork's reading of that mandate, user-ratified 2026-08-03** — a reconstruction, labelled as one. The record never held three items: it held one mandate with two numbered halves, the first of which has two halves of its own. **D-416 remains RATIFIED and is not retired** — it is a correct record of what the user mandated; what these entries carry is each component's own disposition on its own evidence. **NOT DONE:** the gate-correction layer is intact — `applyPostScoringGates` and `applyIter8691Pedal` are live symbols in `src/composing/analysis/chord/postscoringgates.cpp` and `chordpostpasses.cpp`, and the Stage-5 fitter design that owns the dissolution (`cowork_stage5_fitter_design.md`, SIGNED user 2026-07-04) carries it as scope-IN, unexecuted. **Its SUBJECT is reached only through the legacy chord path, established at the control flow rather than assumed:** the joint module calls none of it (`src/composing/analysis/joint/` contains no reference to `chordanalyzer.h`, `analyzeChord`, `applyIter8691Pedal`, `applyPostScoringGates`, `harmonicsegmenter`, `regionanalyzer`, `sectionanalyzer` or `chordpostpasses` beyond one comment), and neither does the record adapter (`sectionrecordadapter.cpp`). On the notation surface all four seams branch on `useJointNotationRecord()` and return the record path when it is true — `notationcomposingbridge.cpp`:729-738 (the note seam), :1491-1507 (the span emit), `notationimplodebridge.cpp`:1416-1432, `notationtuningbridge.cpp`:774-792 — and the flag defaults TRUE at `composingconfiguration.cpp`:178. **The false-negative paths, enumerated rather than waved past (#17e):** (i) the flag set explicitly to false, which selects the legacy arm entire; (ii) `batch_analyze` run without `--joint-inference`; (iii) the test suites; (iv) `analyzeHarmonicContextAtTickUncachedForTesting` (`notationcomposingbridge.cpp`:764, declared "NOT the production path"). **★ A CORRECTION OF THE PREMISE THIS ENTRY WAS DISPATCHED UNDER, and the reason the entry says 'dormant' rather than 'liveness unresolved':** the phase-1m dispatch held that the subject is reachable on the LIVE notation arm, citing `notationcomposingbridge.cpp`:750-753 (the P4 fallback, which does run `findTemporalContext`, `analyzeChord` and `applyIter8691Pedal` at :651, :656 and :663). Those three facts are correct; the reachability conclusion is not — :753 sits BELOW the record-arm early return at :737, so it is reached only when the flag is false. The "Fires 0/2231 on the perf corpus" figure the dispatch called the only figure we have measures how often P4 fires GIVEN the legacy arm ran, and is not a measurement about the live arm at all. **What remains genuinely open is therefore narrower than the dispatch supposed and is rowed at `OPEN_ITEMS.md` OI-288.** **THE TRANSFER (the reason for the LEGACY-IN-ITS-LETTER mark):** the user ruled 2026-08-03 that this component's principle — corrections belong in fitted factor values, never in a post-hoc correction layer laid over the decode — binds the phase-3 family design over the candidate-admission and emission family (`OPEN_ITEMS.md` OI-215, OI-226, OI-227, OI-228, OI-243, OI-244, OI-246, OI-277, each cross-referenced to this entry). It is pointed at, not restated, from the joint estimator's standing rules in `ARCHITECTURE.md` — a second copy would be a #6 violation, and the pointer is what a missing delegation owes. **A withdrawal recorded rather than quietly dropped (#12):** an earlier Cowork reading held that the estimator's standing rule (a) DISCHARGED this component; that reading is withdrawn — rule (a) governs how factor values are fitted and never mentions a post-hoc correction layer, and a specification that simply omits a layer does not thereby dissolve one that exists in code. The surfacing obligation D-416 imposes stands for this component until it is done. Every code fact below was read with the file tools in the phase-1m session, 2026-08-03; commit `41f7c65f63` was verified at the object by explicit hash. NOT RATIFIED as an ENTRY — it goes to the user in the phase-1m ratification queue.


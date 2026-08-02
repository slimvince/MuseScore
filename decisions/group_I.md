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

**Home.** `ARCHITECTURE.md:444-446`

**Provenance.** ARCHITECTURE.md:433-436 states the §2 principles are 'hard constraints, not guidelines'; restated at §2.4 :435-438

### D-071 — The analysis layer never produces display strings

> Analysis components produce structured data — they never produce display strings.
> Formatting is handled by separate formatter classes.

**In plain words.** The analysis returns facts. Turning those facts into text on screen is somebody else's job.

**Why.** Stated constraint, ARCHITECTURE.md:483-485: the separation is already established by `ChordSymbolFormatter`, and keeping it means the same analysis can be rendered several ways without the analysis knowing about any of them.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:487-488`

**Provenance.** ARCHITECTURE.md:481-485; mechanically guarded for the joint module by D-017

### D-072 — The dependency rule - the analysis library knows nothing about the score format

> This dependency order is **enforced**. Any code that would invert it (e.g. a composing header forward-declaring `mu::engraving::Note`) must be moved to the notation bridge layer.

**In plain words.** The music-theory library must not know how MuseScore stores a score. Anything that needs both lives in a thin bridge layer in between.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1097`

**Provenance.** ARCHITECTURE.md:1079-1137, checklist at :1424-1431

### D-073 — Single implementation for shared logic; mirroring is a last resort

> Any algorithm that must produce identical results in both the notation bridge and
> `batch_analyze` belongs in the `composing` module (`src/composing/`), not in either
> consumer.

**In plain words.** If the program and the measurement tool must agree, the code that makes them agree lives in one shared place. Copying it into both is a last resort that must be flagged as debt.

**Why.** Stated constraint, ARCHITECTURE.md:536-554: the notation bridge and `batch_analyze` must produce identical results, so shared logic lives in the composing module both call; mirroring is permitted only when a shared implementation is blocked by a dependency constraint, and then only with a marked technical-debt note.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:540-542`

**Provenance.** ARCHITECTURE.md:534-567; the standing project-wide form is CLAUDE.md #6 (total unification)

### D-074 — Analyze and suggest - never modify the score without explicit user action

> The system presents analytical findings and suggestions. It never modifies the main score
> automatically. All score modifications require explicit user action.

**In plain words.** The program tells you what it thinks. It never changes your music unless you ask it to.

**Why.** Stated constraint, ARCHITECTURE.md:527-532: the chord staff, the status bar and the panels are informational - they show what was inferred - and every change to the music is the user's explicit act through standard MuseScore editing.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:531-533`

**Provenance.** ARCHITECTURE.md:525-532

### D-075 — Interface-based design for machine-learning substitutability

> Every component that may eventually be replaced or augmented by a machine learning
> model must be defined behind a pure abstract interface.

**In plain words.** Anything that might one day be replaced by a trained model is hidden behind an interface, so the replacement can be dropped in without touching everything else.

**Why.** Stated constraint, ARCHITECTURE.md:458-460: the rest of the system depends only on the interface, so a machine-learning implementation can replace a rule-based one without any consumer changing.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:462-463`

**Provenance.** ARCHITECTURE.md:456-479; the substitution points are listed at §14.1

### D-076 — Score inspection before diagnosis

> Claude Code does not have direct score access and must not substitute
> statistical inference for visual score inspection.

**In plain words.** When a corpus number looks odd, somebody opens the actual music and looks at it before anyone changes code or runs more statistics.

**Why.** Stated constraint, ARCHITECTURE.md:576-597: score inspection takes two minutes and answers what corpus statistics cannot - the actual texture, whether the chord staff is over-segmenting, whether the opening key is right - and Claude Code has no score access, so it must not substitute statistical inference for looking.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:600-601`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** ARCHITECTURE.md:569-597

### D-077 — The configuration interface is split into two narrow IoC interfaces

> The implode bridge has no business knowing about status-bar display preferences; the analysis bridge has no business knowing about chord-staff output settings.

**In plain words.** Settings are exposed through two small interfaces rather than one big one, so each component can only see the settings it actually needs.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1617`

**Provenance.** ARCHITECTURE.md:1595-1607, restated at :2967-2978

### D-078 — The cross-layer value types live in a dependency-free leaf header

> **The cross-layer value-types LEAF** — a dependency-free header (STL only; no `chord/`, `key/`, or engraving includes) holding the value types that cross the L1.5 / L3 / L4 boundaries

**In plain words.** The small data types that several stages share live in one header that depends on nothing, which removed two places where a lower stage had to include a higher one.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1451`

**Provenance.** ARCHITECTURE.md:1439-1447

### D-107 — American English throughout

> All identifiers, comments, and documentation use American English spelling.

**In plain words.** Analyzer, not analyser; color, not colour.

**Why.** Stated constraint, ARCHITECTURE.md:492-502: MuseScore's own codebase is American English, so one spelling convention throughout is what keeps identifiers matching across the boundary.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:498`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** ARCHITECTURE.md:492-502; restated in CLAUDE.md Conventions

### D-108 — Cross-platform by default

> All code must run on every platform officially supported by MuseScore Studio: Windows,
> macOS, and Linux.

**In plain words.** Everything must work on Windows, macOS and Linux; platform-specific code is allowed only where unavoidable and must be walled off.

**Why.** Stated constraint, ARCHITECTURE.md:676-682: the code must run on every platform MuseScore Studio officially supports, so platform-specific code is permitted only when unavoidable and must be abstracted so the rest of the module stays platform-agnostic.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:682-683`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** ARCHITECTURE.md:676-682

### D-227 — Read how MuseScore already does it, and never invent parallel infrastructure

> Before implementing anything that touches MuseScore's existing infrastructure —
> UI panels, score traversal, playback, settings, localization — read how MuseScore
> already does it and follow the same pattern. Do not invent parallel infrastructure.

**In plain words.** Before touching anything MuseScore already provides - panels, walking the score, playback, settings, translation - the existing MuseScore code for it is read and followed. A second, parallel mechanism of our own is never created.

**Why.** Derivation not recorded as a separate defense. Its consequences are recorded across the document and are what the rule buys: the panel infrastructure (§12.1), the localization path (§12.1), the accessibility patterns (§12.1), the coding style (§17.1), and the preview pathway (§10.5) all resolve by this rule rather than by separate argument.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:525`

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

**Home.** `ARCHITECTURE.md:1135`

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

**Home.** `ARCHITECTURE.md:1104-1117`

**Provenance.** User ruling 2026-08-02 at the OI-241 adjudication (all recommendations adopted); written into ARCHITECTURE.md §3.3 in the same commit (the register's same-commit rule, D-230). open_items/OI-241.md records the gap this closes.

### D-233 — Build and test commands run synchronously; one run, one result

> **Rule 14 — Shell discipline for long-running commands**
>
> All build and test commands must run synchronously (foreground). Never use background jobs or split output.

**In plain words.** Every build and test command is run in the foreground and its output is read whole. A command is never backgrounded, never killed and re-run differently, and never silently re-run: unexpected output is reported and instructions asked for.

**Why.** Derivation not recorded. The record states the rule and its correct/incorrect patterns (ARCHITECTURE.md:627-649) but not the incident or measurement that produced it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:627-629`

**Provenance.** ARCHITECTURE.md:623-625 (Rule 14) and :649 (the one-run-one-result statement) ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-296 — READING MuseScore's engraving code is allowed from anywhere we may edit; only EDITING the notation and engraving code is off limits

> - **★ FERMATA/OFF-LIMITS CLARIFICATION (user, 2026-06-14) — corrects a Cowork over-statement:** *reading/calling*
>   engraving is ALLOWED from any code we may edit; only *editing* `src/notation`/`src/engraving` CODE is off-limits.

**In plain words.** Our code may call into and read from MuseScore's own score and engraving code wherever we are allowed to write. What is out of bounds is changing MuseScore's notation and engraving source itself.

**Why.** A user correction of an over-statement that had conflated the two. Its worked consequence is recorded with it: a measurement that needed fermatas read them in the batch tool, which already loads the score, and passed them into our own analysis through our own input structure - zero edits outside our area.

**Status.** LIVE · decided 2026-06-14 · ratified by the user

**Home.** `cowork_handoff_archive.md:3732`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-14 Stage-4c block) as a standing lesson. Bears directly on D-229, the general MuseScore-dependency rule the user adopted 2026-08-02: this is the EDIT-versus-READ half, stated a month and a half earlier and consistent with it. D-229 adds what the bridge may read (the score model through the bridge pattern, never layout-derived state) and when an edit to MuseScore's own code is admissible. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue).

### D-311 — The chord-analyzer file split happens once, after the retirements have settled — not before

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map; it has no effect on the live solution (marking convention user-ratified 2026-08-02).

> **the `chordanalyzer.cpp` file split (refactor #1) stays parked BY the ratified engage map** (R9 sequences it AFTER the E4 removals — "split once"; pulling it now would violate, not honor, the ratified order)

**In plain words.** Breaking the large chord-analysis source file into smaller ones waits until the code that is going to be deleted has been deleted. Splitting first would mean splitting twice.

**Why.** The reason is stated with the rule — “split once”: the retirement map already sequences the split after the removals, so performing it earlier would produce a structure the removals then invalidate.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `STATUS_ARCHIVE.md:166`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `STATUS_ARCHIVE.md` (session 22i, the Stage-5 planning checkpoint) as a ruling read off the ratified retirement map. It is load-bearing now beyond its original subject: [[OI-205]] half (b) cites it as “the ratified Stage-3.5 file-split lesson (restructure ONCE, after the boundaries stabilize)” to time the `ARCHITECTURE.md` restructure. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue).


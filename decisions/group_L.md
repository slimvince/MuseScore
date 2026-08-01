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

**Why.** Stated constraint, ARCHITECTURE.md:415-419: the analysis library itself has NO engraving dependency and is pure music theory; the bridge layer is what touches the engraving model. Being a module rather than a plugin is what lets that bridge exist at all.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:369`

**Provenance.** ARCHITECTURE.md:367-371 (§1.2). No date or ratifier stated.

### D-117 — The long-term intent is an official contribution to MuseScore Studio

> The long-term intent is for this to become an official contribution to MuseScore Studio.
> All code follows MuseScore's coding standards, licensing requirements, and contribution
> guidelines.

**In plain words.** The aim is for this work eventually to become part of MuseScore Studio proper, so it is written to MuseScore's own coding, licensing and contribution rules from the start.

**Why.** Derivation not recorded for the intent itself. What the record does state is the consequence it carries (ARCHITECTURE.md:374-375): following MuseScore's standards from the start is what keeps the contribution possible.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:373`

**Provenance.** ARCHITECTURE.md:373-375 (§1.2); restated at ARCHITECTURE.md:6599-6601 (the composing module is 'intended as a future contribution'). ★ READ WITH the CLAUDE.md DISTRIBUTION CONSTRAINT (D-197): the MusicXML declared-mode import patch cfc7eb5e39 is FORK-LOCAL ONLY and must NEVER reach musescore/MuseScore. Two recorded positions - a general intent and a one-patch exception - and the record does not state how the general intent applies to the rest of the tree.

### D-118 — GPL v3, and every external library must be GPL v3 compatible

> All code is licensed under **GPL v3** — consistent with MuseScore Studio's open source
> license. All external libraries used must be GPL v3 compatible.

**In plain words.** All the code is released under the GPL v3 licence, the same licence MuseScore Studio uses, and no outside library may be used unless its licence is compatible with that.

**Why.** Stated constraint, ARCHITECTURE.md:379-380: consistency with MuseScore Studio's own open source licence. A GPL-incompatible library would make the code undistributable with MuseScore.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:379`

**Provenance.** ARCHITECTURE.md:377-380 (§1.3). No date or ratifier stated. The per-file consequence is ARCHITECTURE.md:6432 - a GPL v3 header on every file.

### D-119 — The MuseScore contributor licence agreement is signed before any pull request

> The Contributor License Agreement (CLA) with MuseScore must be signed before any
> pull requests are submitted.

**In plain words.** Before any of this work is offered back to MuseScore as a pull request, the contributor agreement with MuseScore must be signed.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:382`

**Provenance.** ARCHITECTURE.md:382-383 (§1.3), restated at ARCHITECTURE.md:6528-6530 (§18.3). No date or ratifier stated.

### D-120 — MuseScore's coding style is followed, with clang-format run before every commit

> Follow MuseScore's existing coding style throughout:
> - Formatting defined in `.clang-format` — run clang-format before every commit
> - Naming conventions — consistent with existing MuseScore code
> - File headers — GPL v3 license header on every file (see existing files for template)
> - Include ordering — follow MuseScore's convention

**In plain words.** The code looks like MuseScore's own code: the formatter configuration in the repository is run before every commit, names follow MuseScore's conventions, every file carries the GPL v3 header, and includes are ordered MuseScore's way.

**Why.** Stated constraint, ARCHITECTURE.md:512-516 (§2.8): read how MuseScore already does a thing and follow the same pattern rather than inventing parallel infrastructure - the same reason that governs panels, score traversal, playback, settings and localization.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6429`

**Provenance.** ARCHITECTURE.md:6427-6433 (§17.1). No date or ratifier stated.

### D-121 — Where MuseScore's documentation practice is minimal, the higher standard applies

> Where MuseScore's documentation practice is minimal, use good practice instead.

**In plain words.** Following MuseScore's conventions does not mean copying how little it documents. Where MuseScore documents sparsely, this project documents properly instead.

**Why.** Stated constraint, ARCHITECTURE.md:6487-6490 (§17.3): the analyzers are the most complex components in the codebase, and a musician with reasonable theoretical knowledge must be able to read them and understand why each decision was made.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6435`

**Provenance.** ARCHITECTURE.md:6427-6435 (§17.1). No date or ratifier stated.

### D-122 — Every public class and method is documented in musical terms

> Every public class must have a documentation comment explaining:
> - What musical concept it implements
> - What it receives as input (in musical terms)
> - What it produces as output (in musical terms)
> - What it does not handle (important for setting expectations)

**In plain words.** A public class must say which musical idea it implements, what music it takes in, what it produces, and what it deliberately does not handle. A public method must say the same about the musical operation it performs, in musical terms rather than programming terms.

**Why.** Stated constraint, ARCHITECTURE.md:497-501 (§2.6) with :6322-6323: the documentation is written so a person with reasonable musical knowledge and basic programming familiarity can read it, including MuseScore contributors with no familiarity with this codebase at all.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6439`

**Provenance.** ARCHITECTURE.md:6437-6449 (§17.2). No date or ratifier stated.

### D-123 — Every non-obvious scoring weight or threshold explains its musical reasoning

> Every non-obvious scoring weight or threshold must explain its musical reasoning.

**In plain words.** A number in the scoring code that is not self-evident must be accompanied by the musical reason it has the value it has.

**Why.** Stated constraint, ARCHITECTURE.md:6487-6490 (§17.3): the analyzers are the most complex components, and their weights and thresholds are where the musical judgment actually lives - an undocumented one is unreadable and unarguable.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6451`

**Provenance.** ARCHITECTURE.md:6451 (§17.2). No date or ratifier stated. ★ This is the rule the 2026-08-01 CLAUDE.md Conventions entry generalizes from scoring values to design decisions as a class (D-195) - and the rule this register's rationale field serves.

### D-124 — The analyzer code must be readable by a musician

> Every scoring weight, threshold, and heuristic must be documented with its musical
> rationale. A musician with reasonable theoretical knowledge must be able to read the
> analyzer code and understand why each decision was made.

**In plain words.** Every weight, threshold and rule of thumb in the chord and key analyzers carries its musical reason, to the standard that a musician with ordinary theoretical training can read the code and see why each choice was made.

**Why.** Stated constraint, ARCHITECTURE.md:6487: these are the most complex components in the codebase, so they are where readability is worth the most.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6488`

**Provenance.** ARCHITECTURE.md:6485-6497 (§17.3), which gives a worked example from existing code (the circle-of-fifths interval deltas). No date or ratifier stated.

### D-125 — Every test documents the musical situation, the expected result, and what a failure means

> Every test must document:
> - What musical situation is being tested
> - What the expected result is and why it is musically correct
> - What a failure would indicate about the system's behavior

**In plain words.** A test says which musical situation it exercises, what the right answer is and why it is musically right, and what it would mean about the system if the test failed.

**Why.** Stated constraint, ARCHITECTURE.md:6506-6507: the tests must be readable by MuseScore contributors with no deep familiarity with this codebase.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6501`

**Provenance.** ARCHITECTURE.md:6499-6507 (§17.4). No date or ratifier stated.

### D-126 — One coherent piece of functionality per pull request

> Each pull request should implement one coherent piece of functionality. Large
> pull requests are hard to review. The phased plan in Section 15 defines natural
> PR boundaries.

**In plain words.** Each contribution offered back to MuseScore does one thing.

**Why.** Stated constraint, ARCHITECTURE.md:6522-6524: large pull requests are hard to review, and the phased plan defines where the natural boundaries fall.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6522`

**Provenance.** ARCHITECTURE.md:6520-6524 (§18.2). No date or ratifier stated.


# Decisions group P — The user interface, persistence, and machine-learning readiness

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-154 — New panels use MuseScore's own panel and interface infrastructure

> New panels follow MuseScore's existing panel architecture — KDDockWidgets for
> panel management, QML for UI components. Do not create parallel infrastructure.
> Read how existing MuseScore panels are implemented before creating new ones.

**In plain words.** Any new panel is built with the same window-docking and interface technology MuseScore already uses, after reading how MuseScore's existing panels are built. No parallel machinery is created.

**Why.** Stated constraint, ARCHITECTURE.md:519-523 (§2.8): read how MuseScore already does it and follow the same pattern - the same rule that governs score traversal, playback, settings and localization.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:7485`

**Provenance.** ARCHITECTURE.md:6158-6162 (§12.1); the panels themselves are planned (§12.2-§12.5). No date or ratifier stated.

### D-158 — Our data lives in separate files inside the score archive; the score file is never touched

> MuseScore's MSCZ format is a ZIP archive. Our metadata lives as additional files
> within the archive alongside `score.mscx`:

**In plain words.** Constraints, branches, cached analysis and preferences travel with the score as extra files inside its archive, beside the standard MuseScore score file, which our code never modifies.

**Why.** Stated trade-off, ARCHITECTURE.md:6290-6294: the score stays a valid standard MuseScore file with zero interference in MuseScore's own reading and writing, and our data travels with it. The accepted cost is stated too - exporting to MusicXML, PDF or MIDI loses it, which is acceptable because the workflow is MuseScore-native.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:7603`

**Provenance.** ARCHITECTURE.md:6276-6294 (§13.1), a planned component. No date or ratifier stated.

### D-159 — Every custom file carries a format version, and the score file is never rewritten by our persistence

> All our custom files include a format version field. When the format changes,
> migration code handles existing files. The score.mscx is never modified by our
> persistence layer.

**In plain words.** Each of our own files records which version of its format it is, so older files can be migrated when the format changes; the standard MuseScore score file inside the archive is never rewritten by us.

**Why.** SEARCHED 2026-08-09 (CC, `cc_instruction_return_continuation_3.md` Task 2). IT DIFFERS BY PART. The VERSION FIELD carries its purpose in the very next sentence, and a purpose of that shape is a reason: "When the format changes, migration code handles existing files" — the field exists so an older file can be migrated rather than broken. The SECOND HALF — that our persistence never rewrites the score file — is stated flatly with no ground given at all. NOTHING IS BORROWED from the neighbouring paragraph, whose reason belongs to a different point: that export to MusicXML, PDF or MIDI loses our metadata is called acceptable "— the arranging workflow is MuseScore-native". Status DEFERRED: the component is planned rather than built, so the absence is a fact about the record and not about live code.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:7623`

**Provenance.** ARCHITECTURE.md:6296-6300 (§13.2), a planned component. No date or ratifier stated.

### D-160 — Arranger interactions are logged from the start, with consent, as future training data

> The system logs arranger interactions from the start — with user consent — as
> future ML training data. Every suggestion accepted, modified, or rejected is a
> labeled training example specific to vocal jazz arranging, filling the corpus gap
> identified in the design phase.

**In plain words.** Every suggestion a user accepts, changes or rejects is recorded - with their consent - as a labelled example for future machine learning.

**Why.** Stated constraint, ARCHITECTURE.md:6343-6344: the recording exists to fill the corpus gap identified in the design phase, there being no existing labelled corpus of vocal jazz arranging decisions.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:7666`

**Provenance.** ARCHITECTURE.md:6339-6356 (§14.2), a planned component. No date or ratifier stated.

### D-161 — Chord symbols already in a score are a second analyst's opinion, not ground truth

> Mode 2 — Pre-existing symbols present: treated as a second analyst's opinion,
> not ground truth. Judge comments on agreements and disagreements without
> scoring disagreements as errors. Framing: "two analysts may reach different
> but equally valid conclusions."

**In plain words.** When the automated review meets a score that already carries chord symbols, it treats them as another analyst's reading. Disagreements are discussed, not scored as our errors.

**Why.** Stated constraint, ARCHITECTURE.md:6375-6376, in the record's own words: two analysts may reach different but equally valid conclusions. Errors are scored only in Mode 3, against a known ground-truth corpus (:5989-5990) - the same distinction the project's standing rule draws between corroboration and ground truth.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:7698`

**Provenance.** ARCHITECTURE.md:6358-6383 (§14, the automated annotation review), marked planned. No date or ratifier stated.


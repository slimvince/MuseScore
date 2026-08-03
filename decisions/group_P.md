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

**Home.** `ARCHITECTURE.md:6320`

**Provenance.** ARCHITECTURE.md:6158-6162 (§12.1); the panels themselves are planned (§12.2-§12.5). No date or ratifier stated.

### D-155 — Every user-visible string goes through MuseScore's localization, in English and Swedish

> All user-visible strings use MuseScore's existing Qt localization infrastructure
> (`.ts` files, Qt Linguist). English and Swedish translations provided for all new strings.

**In plain words.** Text a user can read is translatable through MuseScore's own translation system, and every new string is supplied in English and Swedish.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6324`

**Provenance.** ARCHITECTURE.md:6164-6165 (§12.1); listed in the Core scope at ARCHITECTURE.md:6617-6618. No date or ratifier stated.

### D-156 — Accessibility follows MuseScore's existing patterns

> Accessibility follows MuseScore's existing Qt accessibility patterns — focus
> management, keyboard navigation, screen reader hooks.

**In plain words.** Keyboard navigation, focus handling and screen-reader support are done the way MuseScore already does them.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6327`

**Provenance.** ARCHITECTURE.md:6167-6168 (§12.1); listed in the Core scope at ARCHITECTURE.md:6618. No date or ratifier stated.

### D-157 — The harmonic-display preference exists for clarity, not for cost

> A user preference controls whether harmonic analysis is shown in the status bar. This
> preference exists for UI clarity — some users find the chord and key information
> distracting, particularly when doing work unrelated to harmony.

**In plain words.** The setting that hides the harmonic information from the status bar is there because some users find it distracting, not because the analysis is expensive. Switching it off does not skip the analysis.

**Why.** Measurement named in the record, ARCHITECTURE.md:6174-6174: the analysis cost at this seam is 'well under 1ms'. ★ That number is the LEGACY bounded-window path's; open_items/OI-203 and OI-206 record the record arm running a whole-score decode per selection, measured in seconds on large scores - so the reason this preference is not a performance control no longer holds as stated.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6332-6334`

**Provenance.** ARCHITECTURE.md:6170-6199 (§12.1a). No date or ratifier stated. ★ Verbatim RE-TAKEN 2026-08-02 (the phase-1 truth-sync): the paragraph's second half — 'It is not a performance control: analysis cost is negligible (well under 1ms) and suppressing the display does not require skipping the analysis' — is FALSE at HEAD on both clauses and is corrected in place (OPEN_ITEMS OI-242 discharged). The surviving quote is the decision proper: the preference exists for clarity. Whether it should also become a performance control is left OPEN at the home, not decided.

### D-158 — Our data lives in separate files inside the score archive; the score file is never touched

> MuseScore's MSCZ format is a ZIP archive. Our metadata lives as additional files
> within the archive alongside `score.mscx`:

**In plain words.** Constraints, branches, cached analysis and preferences travel with the score as extra files inside its archive, beside the standard MuseScore score file, which our code never modifies.

**Why.** Stated trade-off, ARCHITECTURE.md:6290-6294: the score stays a valid standard MuseScore file with zero interference in MuseScore's own reading and writing, and our data travels with it. The accepted cost is stated too - exporting to MusicXML, PDF or MIDI loses it, which is acceptable because the workflow is MuseScore-native.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6438`

**Provenance.** ARCHITECTURE.md:6276-6294 (§13.1), a planned component. No date or ratifier stated.

### D-159 — Every custom file carries a format version, and the score file is never rewritten by our persistence

> All our custom files include a format version field. When the format changes,
> migration code handles existing files. The score.mscx is never modified by our
> persistence layer.

**In plain words.** Each of our own files records which version of its format it is, so older files can be migrated when the format changes; the standard MuseScore score file inside the archive is never rewritten by us.

**Why.** derivation not recorded.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6458`

**Provenance.** ARCHITECTURE.md:6296-6300 (§13.2), a planned component. No date or ratifier stated.

### D-160 — Arranger interactions are logged from the start, with consent, as future training data

> The system logs arranger interactions from the start — with user consent — as
> future ML training data. Every suggestion accepted, modified, or rejected is a
> labeled training example specific to vocal jazz arranging, filling the corpus gap
> identified in the design phase.

**In plain words.** Every suggestion a user accepts, changes or rejects is recorded - with their consent - as a labelled example for future machine learning.

**Why.** Stated constraint, ARCHITECTURE.md:6343-6344: the recording exists to fill the corpus gap identified in the design phase, there being no existing labelled corpus of vocal jazz arranging decisions.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6501`

**Provenance.** ARCHITECTURE.md:6339-6356 (§14.2), a planned component. No date or ratifier stated.

### D-161 — Chord symbols already in a score are a second analyst's opinion, not ground truth

> Mode 2 — Pre-existing symbols present: treated as a second analyst's opinion,
> not ground truth. Judge comments on agreements and disagreements without
> scoring disagreements as errors. Framing: "two analysts may reach different
> but equally valid conclusions."

**In plain words.** When the automated review meets a score that already carries chord symbols, it treats them as another analyst's reading. Disagreements are discussed, not scored as our errors.

**Why.** Stated constraint, ARCHITECTURE.md:6375-6376, in the record's own words: two analysts may reach different but equally valid conclusions. Errors are scored only in Mode 3, against a known ground-truth corpus (:5989-5990) - the same distinction the project's standing rule draws between corroboration and ground truth.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6533`

**Provenance.** ARCHITECTURE.md:6358-6383 (§14, the automated annotation review), marked planned. No date or ratifier stated.


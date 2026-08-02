# Decisions group J — Presentation and output conventions

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-086 — Roman numerals and Nashville numbers are presentation choices, not separate analyses

> Roman numerals and Nashville numbers are **presentation choices**, not
>   separate analyses — they are alternative formatters on the same `ChordAnalysisResult`.

**In plain words.** Showing the harmony as Roman numerals or as Nashville numbers is a choice of how to display one and the same analysis.

**Why.** Stated constraint, ARCHITECTURE.md:5843-5845: Roman numerals and Nashville numbers encode identical information, so showing both on one staff would be redundant and would destroy legibility - which makes the choice a display preference, not two analyses.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3245-3246`

**Provenance.** ARCHITECTURE.md:3242-3246; consistent with D-016

### D-087 — Display options live with the formatter, not with the analyzer preferences

> Display options (`Options`) live in `ChordSymbolFormatter`, not in
> `ChordAnalyzerPreferences`, enforcing the analysis/display separation (principle 2.3).

**In plain words.** Which spelling convention to use on screen is a formatter setting, kept away from the settings that affect the analysis itself.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2946-2947`

**Provenance.** ARCHITECTURE.md:2907-2947

### D-088 — No automatic key signature injection

> No automatic key signature
> injection is planned.

**In plain words.** The program will never add a key signature to your score by itself. It shows what it inferred in the chord staff and leaves the decision to you.

**Why.** Stated constraint, ARCHITECTURE.md:527-532 (§2.9): writing a key signature into the score would be the system modifying the music without the user asking.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3846-3847`

**Provenance.** ARCHITECTURE.md:3839-3847; an instance of D-074

### D-089 — The legacy confidence exposure gates - 0.5 tentative, 0.8 assertive

> - Above 0.8 — display without qualifier
> - 0.5–0.8 — append "?" to key/mode label
> - Below 0.5 — suppress key-dependent chord-track annotations rather than exposing a low-confidence key

**In plain words.** On the old path, a key the program is unsure of is shown with a question mark, and one it is very unsure of is not shown at all rather than shown wrongly.

**Why.** derivation not recorded.

**Status.** SUPERSEDED BY D-018 · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3531-3533`

**Provenance.** The record arm replaces the 0.5/0.8 literals with the fitted nats constants (ARCHITECTURE.md:175-177); the literals are legacy-arm-only (sectionanalyzer.cpp::legacyKeyExposureBucket)

### D-090 — Abstention is a valid outcome - high precision before coverage

> - high precision on exposed results
> - calibrated abstention when evidence is weak

**In plain words.** The aim is not to put a label on everything. It is to be right about what we do label, and to say nothing when the evidence is thin.

**Why.** Stated constraint, ARCHITECTURE.md:3545-3553 and its consumer rules at :5604-5612: the stated product target is not 'always emit a label' but high precision on exposed results, calibrated abstention when evidence is weak, and coverage gains only after precision is acceptable - so below the confidence bar the key-dependent annotations are suppressed rather than printed tentatively.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3551-3552`

**Provenance.** ARCHITECTURE.md:3538-3590

### D-106 — The augmented-sixth labels are gated to the Standard and Baroque presets

> **Preset gating is NOT implemented — corrected 2026-08-02 (`OPEN_ITEMS.md` OI-112(c); this section
> asserted "Gated to Standard and Baroque presets only", and the code defers exactly that).**

**In plain words.** The specific Italian, French and German augmented-sixth labels are shown only under the classical presets.

**Why.** derivation not recorded.

**Status.** SUPERSEDED IN FACT · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3862-3863`

**Provenance.** open_items/OI-112 already records this preset-gating as stale; open_items/OI-201 records that the record arm collapses the family to a plain major triad symbol ★ Verbatim RE-TAKEN 2026-08-02 (the phase-1 truth-sync): §5.11's assertion 'Gated to Standard and Baroque presets only' was corrected, since the formatter explicitly defers that gate for want of preset context (`chordsymbolformatter.cpp:882-883`) and emits the labels under every preset (OPEN_ITEMS OI-112(c) discharged). The decision's own words survive at the home, quoted inside the correction.

### D-234 — A chord symbol string must be valid under chords_std.xml; chords.xml is not relied on

> **Rule 16 — Do not rely on chords.xml**
>
> MuseScore has two chord description files:
> - `share/chords/chords_std.xml` — the active standard chord list used by default in all scores
> - `share/chords/chords.xml` — legacy file, likely deprecated, contains known bugs and inconsistencies with the parser
>
> When our formatter produces a chord symbol string, it must be valid according to `chords_std.xml` only. Do not add chord symbol strings that exist only in `chords.xml` — they will fail to parse correctly under the Standard chord style and may produce corrupted output.

**In plain words.** MuseScore ships two chord description files. Everything our formatter emits must parse under the active one, chords_std.xml. A string that exists only in the legacy chords.xml is not used.

**Why.** The measurement that decided it is cited in the record: `9sus` exists in chords.xml (id=134) and not in chords_std.xml, and under the Standard chord style it triggers `generateDescription()`, producing the corrupted `Fsussus9` render (ARCHITECTURE.md:672). The remedy named there is `sus(add9)`.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:664-670`

**Provenance.** ARCHITECTURE.md:664-674 (Rule 16), restated in the retired-session record at STATUS_ARCHIVE.md:2247


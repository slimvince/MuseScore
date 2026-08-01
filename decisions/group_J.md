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

**Why.** Stated constraint, ARCHITECTURE.md:5678-5680: Roman numerals and Nashville numbers encode identical information, so showing both on one staff would be redundant and would destroy legibility - which makes the choice a display preference, not two analyses.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3138-3139`

**Provenance.** ARCHITECTURE.md:3135-3139; consistent with D-016

### D-087 — Display options live with the formatter, not with the analyzer preferences

> Display options (`Options`) live in `ChordSymbolFormatter`, not in
> `ChordAnalyzerPreferences`, enforcing the analysis/display separation (principle 2.3).

**In plain words.** Which spelling convention to use on screen is a formatter setting, kept away from the settings that affect the analysis itself.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2850-2851`

**Provenance.** ARCHITECTURE.md:2816-2851

### D-088 — No automatic key signature injection

> No automatic key signature
> injection is planned.

**In plain words.** The program will never add a key signature to your score by itself. It shows what it inferred in the chord staff and leaves the decision to you.

**Why.** Stated constraint, ARCHITECTURE.md:520-525 (§2.9): writing a key signature into the score would be the system modifying the music without the user asking.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3739-3740`

**Provenance.** ARCHITECTURE.md:3732-3740; an instance of D-074

### D-089 — The legacy confidence exposure gates - 0.5 tentative, 0.8 assertive

> - Above 0.8 — display without qualifier
> - 0.5–0.8 — append "?" to key/mode label
> - Below 0.5 — suppress key-dependent chord-track annotations rather than exposing a low-confidence key

**In plain words.** On the old path, a key the program is unsure of is shown with a question mark, and one it is very unsure of is not shown at all rather than shown wrongly.

**Why.** derivation not recorded.

**Status.** SUPERSEDED BY D-018 · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3424-3426`

**Provenance.** The record arm replaces the 0.5/0.8 literals with the fitted nats constants (ARCHITECTURE.md:168-170); the literals are legacy-arm-only (sectionanalyzer.cpp::legacyKeyExposureBucket)

### D-090 — Abstention is a valid outcome - high precision before coverage

> - high precision on exposed results
> - calibrated abstention when evidence is weak

**In plain words.** The aim is not to put a label on everything. It is to be right about what we do label, and to say nothing when the evidence is thin.

**Why.** Stated constraint, ARCHITECTURE.md:3438-3446 and its consumer rules at :5604-5612: the stated product target is not 'always emit a label' but high precision on exposed results, calibrated abstention when evidence is weak, and coverage gains only after precision is acceptable - so below the confidence bar the key-dependent annotations are suppressed rather than printed tentatively.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3444-3445`

**Provenance.** ARCHITECTURE.md:3431-3483

### D-106 — The augmented-sixth labels are gated to the Standard and Baroque presets

> Gated to
> Standard and Baroque presets only. Jazz and Nashville presets continue to
> emit chromatic Roman numerals or chord symbols respectively.

**In plain words.** The specific Italian, French and German augmented-sixth labels are shown only under the classical presets.

**Why.** derivation not recorded.

**Status.** SUPERSEDED IN FACT · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3753-3755`

**Provenance.** open_items/OI-112 already records this preset-gating as stale; open_items/OI-201 records that the record arm collapses the family to a plain major triad symbol


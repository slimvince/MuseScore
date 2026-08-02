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

**Why.** Stated constraint, ARCHITECTURE.md:5854-5856: Roman numerals and Nashville numbers encode identical information, so showing both on one staff would be redundant and would destroy legibility - which makes the choice a display preference, not two analyses.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3268-3269`

**Provenance.** ARCHITECTURE.md:3253-3257; consistent with D-016

### D-087 — Display options live with the formatter, not with the analyzer preferences

> Display options (`Options`) live in `ChordSymbolFormatter`, not in
> `ChordAnalyzerPreferences`, enforcing the analysis/display separation (principle 2.3).

**In plain words.** Which spelling convention to use on screen is a formatter setting, kept away from the settings that affect the analysis itself.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2969-2970`

**Provenance.** ARCHITECTURE.md:2918-2958

### D-088 — No automatic key signature injection

> No automatic key signature
> injection is planned.

**In plain words.** The program will never add a key signature to your score by itself. It shows what it inferred in the chord staff and leaves the decision to you.

**Why.** Stated constraint, ARCHITECTURE.md:527-532 (§2.9): writing a key signature into the score would be the system modifying the music without the user asking.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3869-3870`

**Provenance.** ARCHITECTURE.md:3850-3858; an instance of D-074

### D-089 — The legacy confidence exposure gates - 0.5 tentative, 0.8 assertive

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map; it has no effect on the live solution (marking convention user-ratified 2026-08-02).

> - Above 0.8 — display without qualifier
> - 0.5–0.8 — append "?" to key/mode label
> - Below 0.5 — suppress key-dependent chord-track annotations rather than exposing a low-confidence key

**In plain words.** On the old path, a key the program is unsure of is shown with a question mark, and one it is very unsure of is not shown at all rather than shown wrongly.

**Why.** derivation not recorded.

**Status.** SUPERSEDED BY D-018 · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3554-3556`

**Provenance.** The record arm replaces the 0.5/0.8 literals with the fitted nats constants (ARCHITECTURE.md:175-177); the literals are legacy-arm-only (sectionanalyzer.cpp::legacyKeyExposureBucket)

### D-090 — Abstention is a valid outcome - high precision before coverage

> - high precision on exposed results
> - calibrated abstention when evidence is weak

**In plain words.** The aim is not to put a label on everything. It is to be right about what we do label, and to say nothing when the evidence is thin.

**Why.** Stated constraint, ARCHITECTURE.md:3556-3564 and its consumer rules at :5604-5612: the stated product target is not 'always emit a label' but high precision on exposed results, calibrated abstention when evidence is weak, and coverage gains only after precision is acceptable - so below the confidence bar the key-dependent annotations are suppressed rather than printed tentatively.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3574-3575`

**Provenance.** ARCHITECTURE.md:3549-3601

### D-106 — The augmented-sixth labels are gated to the Standard and Baroque presets

> **Preset gating is NOT implemented — corrected 2026-08-02 (`OPEN_ITEMS.md` OI-112(c); this section
> asserted "Gated to Standard and Baroque presets only", and the code defers exactly that).**

**In plain words.** The specific Italian, French and German augmented-sixth labels are shown only under the classical presets.

**Why.** derivation not recorded.

**Status.** SUPERSEDED IN FACT · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3885-3886`

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

**Home.** `ARCHITECTURE.md:668-674`

**Provenance.** ARCHITECTURE.md:664-674 (Rule 16), restated in the retired-session record at STATUS_ARCHIVE.md:2247 ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-295 — Zero information loss to the end user - every inferred object must be displayable

>   R-map at its next edit) and **E-14** (user-stated principle: ZERO INFORMATION LOSS TO THE END USER — every
>   inferred object displayable; progressive disclosure yes, structural hiding no; ARCH pointer rides ARCH's next
>   edit). Market probe recorded: no comparable engine anywhere in the MuseScore GitHub space; plugins hand-annotate
>   what our layers infer.

**In plain words.** Anything the analysis works out must be capable of being shown to the user. Showing it gradually, so the display is not overwhelming, is fine; leaving something permanently unreachable because the interface has no place for it is not.

**Why.** A user-stated principle. It is the display-side counterpart of the no-information-loss principle (D-099, principle #12), which governs what the analysis may discard internally; this governs what the interface may withhold.

**Status.** LIVE · date not stated · ratified by the user

**Home.** `cowork_handoff_archive.md:2507`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the standing-records block) as item E-14 of `cowork_product_tool_register.md`, with a note that a pointer into the architecture document was owed at its next edit. This pass found no such pointer in the register's own home census, so the owed act appears undischarged. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue).

### D-304 — The analyzer always emits its fullest reading; simplifying it happens only when comparing against a corpus, never in the product

> Extension-stripping policy implemented as test-only utility (`stripSymbol`, `classifyComparison`); never in production. Per principle in memory `project_no_stripping_in_production.md` — analyzers always emit maximal output, stripping happens only at corpus-comparison boundaries. Design memo: `docs/extension_stripping_policy.md`.

**In plain words.** When our analysis names a chord it states everything it found, including the added notes above the basic triad. Cutting that back to a plainer name is something only the comparison machinery may do, so that a difference of notation is not counted as a difference of analysis.

**Why.** The stated principle is that the analyzer reports what it found; the record shows the measured consequence — applying the comparison-side simplification reduced the pinned baseline from 135 differences to 10 (`STATUS_ARCHIVE.md:944`), which is the size of the notation-convention difference the rule keeps out of the analysis.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `STATUS_ARCHIVE.md:943`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `STATUS_ARCHIVE.md`; the design memo it names, `docs/extension_stripping_policy.md`, exists on disk. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue).


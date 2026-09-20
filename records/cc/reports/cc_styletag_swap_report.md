# CC report — the StyleTag swap (re-tag the Harmonic Vocabulary with the five ratified idioms)

**Dispatch:** ratified forward-sequence step 1 (mechanical). **State: COMPLETE, HELD for the single fork-only commit
(not committed — see §7).** Dormant-module only; grep-proof no production consumer; suites green with NO golden refresh;
corpus gate **53/24/53** reproduced exact. **No θ, no inference-problem coding.** Source of every tag:
`cowork_idiom_entry_mapping.md` (verbatim) + the two instruction directives it references (plain ii–V–I → Diatonic-
functional; tritone-sub Ger-6 dual-tag).

---

## 1. The representation choice (declared)

- **Idiom tag — a bitmask set, `IdiomSet = uint8_t`.** `enum class Idiom : uint8_t` with five power-of-two bits
  (`DiatonicFunctional=1<<0 … ChromaticColoristic=1<<4`). **Multi-valued** per entry (the mapping is explicitly
  multi-tag). A **set/bitmask** (not `vector<Idiom>`) because the query semantics are *set intersection* — "an entry is
  admissible under ANY of the requested idioms" — which is one `&`. Compose with a C++17 fold helper
  `idiomSet(Idiom...)`; the default query subset is `constexpr IdiomSet kAllIdioms`; the filter is
  `idiomsIntersect(a,b) == (a & b) != 0`. This replaces the placeholder `enum class StyleTag {Baroque, Jazz, Default}`
  and the four `…Styles()` vector helpers (all removed).
- **Two cross-attributes — separate per-entry enums** (`enum class Mode {Major, Minor, Both}`,
  `enum class Chromaticism {Diatonic, Chromatic, Both}`), tagged **independently** of the idiom (proposal §4 decision 2).
  The mapping gives **no explicit per-entry cross-attribute table**, so each value is read **mechanically off the entry's
  own encoded skeleton** (the mode it commits to; whether any element is non-diatonic / applied / borrowed) — a structural
  read, not an idiom judgment — governed by a mapping row-note where one states a value (lament "chromatic", Andalusian
  "chromatic-flavoured"). Declared derivation rule; see §5.
- **One extra structural flag — `bool voiceLeadingDefined`** — added to honor the mapping "Notes" bullet 2 ("flag them so
  the future [voice-leading] layer claims them"). Set on the galant schemata (Prinner, Romanesca, Do-Re-Mi, Monte, Fonte)
  and the line cliché. It carries no weighting; it is a structural marker only. *(Beyond the two named cross-attributes;
  flagged here as a declared addition — trivially removed if Cowork considers it out of scope.)*
- **Query semantics:** `browse/recognise/suggest` signatures changed from `const std::vector<StyleTag>&` to
  `IdiomSet idiomSubset = kAllIdioms`; the filter `inActiveStyles → inActiveIdioms` uses intersection. **No weighting,
  no ranking change** — the idiom-mixture weighting is the recognition consumer's job (next step), not this one.
- **`GenerativeSlot` (expand) is left untagged** — it is the generative spine (§5.1 R1–R5), not an enumerated `Entry`;
  it carries no idiom field in v1. See §6.

---

## 2. The re-tag table (37 entries, verbatim from the entry-mapping)

Idioms: **D**=Diatonic-functional(1) · **C**=Chromatic-functional(2) · **S**=Seventh-functional(3) · **T**=Triadic-modal(4)
· **X**=Chromatic-coloristic(5). VL = voiceLeadingDefined.

| # | Entry | Idiom(s) | Mode | Chrom. | VL | Mapping row |
|---|---|---|---|---|---|---|
| 1 | Authentic cadence (V–I) | D | Major | Diatonic | | R6 |
| 2 | Authentic cadence, minor (V–i) | D | Minor | Diatonic | | R6 |
| 3 | Deceptive cadence (V–vi) | D,C | Major | Diatonic | | R7 |
| 4 | Deceptive cadence, minor (V–♭VI) | D,C | Minor | Diatonic | | R7 |
| 5 | Plagal cadence (IV–I) | D | Major | Diatonic | | R6 |
| 6 | Phrygian half cadence, minor (iv6–V) | D,C | Minor | Diatonic | | R7 |
| 7 | ii–V–I (common-practice, triads) | D | Major | Diatonic | | header (plain ii–V–I → 1) |
| 8 | IIm7–V7–Imaj7 (major ii–V–I) | S | Major | Diatonic | | R8 |
| 9 | iiø7–V7–i (minor ii–V–i) | S | Minor | Diatonic | | R8 |
| 10 | Incomplete ii–V (no resolution) | S | Major | Diatonic | | R8 |
| 11 | Turnaround I–vi–ii–V | S | Major | Diatonic | | R9 |
| 12 | Turnaround I–VI7–ii–V | S,C | Major | Chromatic | | R9 (+VI7 → 2) |
| 13 | Turnaround iii–vi–ii–V | S | Major | Diatonic | | R9 (family-inherit — §4-a) |
| 14 | Rhythm-changes A (I–VI7–IIm7–V7) | S,C | Major | Chromatic | | R9 (+VI7 → 2) |
| 15 | Circle-of-fifths (full) | D | Major | Diatonic | | R10 (triadic → 1) |
| 16 | Circle-of-fifths (iii–vi–ii–V–I) | D | Major | Diatonic | | R10 (triadic → 1) |
| 17 | Descending-thirds (I–vi–IV–ii) | D | Major | Diatonic | | R11 |
| 18 | Lament bass (descending tetrachord, minor) | C,X | Minor | Chromatic | | R16 (§4-b) |
| 19 | Andalusian cadence (i–♭VII–♭VI–V) | T,X | Minor | Chromatic | | R15 |
| 20 | Doo-wop (I–vi–IV–V) | T | Major | Diatonic | | R13 |
| 21 | Axis (I–V–vi–IV) | T | Major | Diatonic | | R13 |
| 22 | Pachelbel | T,D | Major | Diatonic | | R14 |
| 23 | Prinner (bass 4̂–3̂–2̂–1̂) | C | Both | Diatonic | ✓ | R17 |
| 24 | Romanesca (I–V–vi–iii) | C | Major | Diatonic | ✓ | R17 |
| 25 | Do-Re-Mi (melody 1̂–2̂–3̂) | C | Major | Diatonic | ✓ | R17 |
| 26 | Monte (V7/IV–IV–V7/V–V) | C | Major | Chromatic | ✓ | R12 |
| 27 | Fonte (V7/ii–ii–V7/I–I) | C | Major | Chromatic | ✓ | R12 |
| 28 | Backdoor (♭VII7–I) | X | Major | Chromatic | | R18 |
| 29 | Coltrane changes | X | Major | Chromatic | | R18 |
| 30 | Secondary dominant / tonicization | C | Both | Chromatic | | R19 |
| 31 | Related ii–V | S | Both | Chromatic | | R20 |
| 32 | Tritone substitution (subV) | X,C | Both | Chromatic | | R21 + R4 Ger-6 dual-tag (task #3) |
| 33 | Diatonic (functional) substitution | D | Both | Diatonic | | R22 |
| 34 | Modal interchange | C,T | Both | Chromatic | | R23 (+4 triadic borrowings) |
| 35 | Diminished approach | C | Both | Chromatic | | R24 |
| 36 | Deceptive resolution | C | Both | Both | | R25 |
| 37 | Line cliché | X | Both | Chromatic | ✓ | R26 |

**Counts:** 37 entries re-tagged (= all §5 catalog entries). **11 multi-tag** (#3,4,6,12,14,18,19,22,32,34) — 10 dual +
#32 dual. **6 voice-leading-flagged** (#23–27, #37). Idiom coverage: D×9, C×13, S×7, T×5, X×7 (multi-tag overlaps).

---

## 3. Consumer / query updates

- `browse`, `recognise`, `suggest` now take `IdiomSet idiomSubset = kAllIdioms`; internal `inActiveIdioms` replaces
  `inActiveStyles` (intersection filter). No other call-site exists (dormant — §4).
- **Semantics = "admissible under ANY requested idiom"** (union/intersection filter), exactly as the instruction
  specifies. No weighting, no ranking change — ranking is unchanged (matchScore → specificity → length).

---

## 4. STOP list & declared decisions

**Hard-STOP list (entries untaggable without a guess): EMPTY.** Every §5 catalog entry maps to a mapping row. The four
items below are **declared resolutions / observations**, surfaced for Cowork — none is a silent guess.

- **(a) `Turnaround iii–vi–ii–V` (#13)** — not itemised in R9's example list (`I–vi–ii–V, I–VI7–ii–V, rhythm-changes A`).
  Tagged **{S}** by inheritance from the R9 *Turnarounds family row*: its structurally-identical all-triadic sibling
  `I–vi–ii–V` is R9-tagged {S} (note: even the all-triadic turnaround is {S} in R9, *not* {D} — so the "plain-triadic → 1"
  header principle does not override the turnaround family tag). Declared; Cowork may re-rule.
- **(b) `Lament bass` (#18)** — mapping R16 gives **"2 / 5"** and describes the *chromatic* descending tetrachord, but the
  catalog entry holds the **diatonic 4-note** minor tetrachord (1̂–♭7̂–♭6̂–5̂; the chromatic 5-note variant is a declared
  non-distinct v1 skeleton). Encoded as **{C, X}** (both idioms the row names — multi-tag is the point) with
  **chromaticism = Chromatic** per R16's explicit "chromatic" note. The skeleton-descriptor discrepancy is surfaced here,
  not papered over.
- **(c) §5.1 function-map rows R1–R5 (Diatonic functions / Secondary V7/x·viio7/x / Applied ii–V / Substitute subV7/x /
  Modal interchange)** describe the **generative spine** (the `expand()` slots), which are **not enumerated `Entry`
  records** and carry no idiom field in v1 (`GenerativeSlot` is untagged). Their §5.3 substitution-operation counterparts
  **are** tagged entries (R19–R25). So R1–R5 having "no matching Entry" is **by construction** (the spine is generative
  per spec §5.1), not a defect. Declared — not STOP-listed.
- **(d) Cross-attributes** — the mapping gives no explicit per-entry mode/chromaticism table; values are derived
  mechanically from each entry's own encoded skeleton (§5), governed by a row-note where present. Declared derivation
  rule; Cowork may pin an explicit table later (the values would then be a mechanical re-read, not a re-decision).

---

## 5. Cross-attribute derivation rule (mechanical, declared)

- **mode** = the key mode the entry's skeleton is built on: **Major** (major-key skeleton), **Minor** (minor-key
  skeleton — the "minor" / `i` / Andalusian entries), **Both** (mode-agnostic substitution *operations*; the mode-neutral
  bass-line schema Prinner).
- **chromaticism** = **Chromatic** if the entry involves a non-diatonic degree / an applied-secondary dominant /
  a borrowed chord / a chromatic line (turnarounds with VI7, Monte/Fonte, Andalusian, backdoor, Coltrane, subV, secondary
  dom, modal interchange, dim approach, line cliché, lament); **Diatonic** if every element is diatonic to the entry's mode
  (plain cadences, triadic ii–V–I, triadic circle-of-fifths, doo-wop, Axis, Pachelbel, Prinner, Romanesca, Do-Re-Mi);
  **Both** for an operation with both realisations (deceptive resolution: V→vi diatonic, V→♭VI chromatic). The raised
  leading-tone of the minor-key dominant is treated as diatonic-standard (harmonic minor), consistent with R6/R7 tagging
  the minor authentic/deceptive cadences as functional (1).

---

## 6. Gate & dormancy proof

- **Dormancy (grep-proof).** Post-change, the vocabulary symbols (`HarmonicVocabulary`, `harmonicvocabulary`, `IdiomSet`,
  `Idiom::`, `enum class Idiom`) appear in **exactly three files** — `harmonicvocabulary.{h,cpp}` + its unit test — across
  all `**/*.{cpp,h,py}`. **Zero `tools/` hits, zero other production `src/` consumers.** So the change is byte-identical on
  production **by construction** (no caller executes the retagged code). The `src/engraving/rw/*` "StyleTag" hits are an
  unrelated `readStyleTag()` method (engraving XML), not this symbol.
- **Suites (green, NO golden refresh):** composing **1035** (was 1033; **+2** new vocabulary tests — see §8), notation
  **53** (4 skipped baseline), pipeline_snapshot **11/11** (no `--update-goldens`).
- **Corpus gate — reproduced EXACT (one end-of-run reproduction):** `characterise_bir_false.py` per preset —
  **Baroque 53 / Jazz 24 / Default 53**, manifests validated, 352 scores each. Byte-identical to the CLAUDE.md sets by
  construction (dormant; `batch_analyze` has no vocabulary caller, so its output is unchanged).
- **Unity-build hygiene:** the first build surfaced C4459 (single-letter idiom aliases `S`/`T` shadowing
  `keymodesequence.cpp` in the shared Unity TU). Fixed by renaming the aliases to two-letter forms (`Df/Cf/Sf/Tm/Cc`);
  the final build has **zero warnings referencing the vocabulary file**.

---

## 7. Files & commit (HELD — not committed)

**Commit set (this swap, ONE fork-only commit — staged-ready, NOT committed per "commit only when explicitly asked"):**
1. `src/composing/analysis/vocabulary/harmonicvocabulary.h`
2. `src/composing/analysis/vocabulary/harmonicvocabulary.cpp`
3. `src/composing/tests/harmonicvocabulary_tests.cpp`
4. `cowork_progression_schema_dictionary.md` (doc-sync: §5/§6/§12.1 + glossary flip to the ratified taxonomy)
5. `cowork_style_taxonomy_proposal.md` (doc-sync: status line → "EXECUTED (StyleTag swap, this commit)")
6. `docs/implementation_roadmap.md` (doc-sync: forward-sequence step 1 → ✅ EXECUTED)

**★ Working-tree surprise, surfaced not bundled:** `STATUS.md` (already `M` at session start) and
`cowork_layer6_grouping_design.md` (pre-existing Cowork L6 edit — verified **no** StyleTag/Idiom content) are modified but
are **NOT mine** — excluded from the commit set above (the don't-bundle-others'-hunks precedent). `scratch_artifacts/`
(untracked build logs) and this report (gitignored) are also excluded. **No STATUS.md session entry was added** (it is
Cowork-dirty; adding to it would collide with an in-progress Cowork edit — surfaced for the user/Cowork to fold).

---

## 8. Tests

- Updated `BrowseReturnsEntriesInActiveStylesOnly` → `BrowseReturnsEntriesInActiveIdiomsOnly` — oracle-asserted vs the
  mapping (Seventh-functional surfaces IIm7–V7–Imaj7 and excludes triadic-modal/chromatic-functional-only entries;
  Chromatic-coloristic surfaces tritone-sub + Coltrane; Triadic-modal surfaces the pop loops).
- **New — the multi-tag test** `MultiTagEntryRetrievableUnderEachOfItsIdioms`: Pachelbel {T,D} is retrievable under
  Triadic-modal AND Diatonic-functional, and NOT under Seventh-functional, and under both-requested-together.
- **New — the cross-attribute test** `CrossAttributesTagModeAndChromaticismIndependently`: minor ii–V–i = Minor+Diatonic;
  authentic cadence = Major+Diatonic; secondary-dom substitution = Both+Chromatic (the two axes vary independently); the
  Prinner carries voiceLeadingDefined.
- Suite: **18** HarmonicVocabulary tests (16 prior + 2 new), all pass.

---

*Report length: 188 lines.*

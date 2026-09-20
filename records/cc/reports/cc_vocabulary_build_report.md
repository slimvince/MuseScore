# CC build report — Harmonic Vocabulary component v1 (dormant, byte-identical)

**Task:** `cc_instruction_vocabulary_build.md` — build the Harmonic Vocabulary component (step 1 of the
ratified order: encyclopedia → L6 → wire the consumer). Spec (contract):
`cowork_progression_schema_dictionary.md`. Consumer design (context, NOT built):
`cowork_progression_schema_design.md`.

**Outcome:** built, dormant, byte-identical on production by construction. Gate green
(composing 974→990, notation 53, snapshot 11/11 no-refresh). Corpus 53/24/53 unchanged BY CONSTRUCTION
(no production consumer — grep-proven below; not re-measured per instruction §4).

---

## §0 working-tree sweep
Clean start (`git status -s` showed only the gitignored `scratch_artifacts/`). During the session two
untracked Cowork docs appeared (`cowork_idiom_discovery_design.md`, `cowork_upstream_merge_risk.md`) —
parallel Cowork work, **excluded from my commit** (the L5-step precedent that excluded
`contrapunctus_findings.md`).

## §1 read-only confirm (GREEN — nothing false, no STOP)
All four confirms held at source:
- **Degree + quality + RN types reusable, no duplicate formatter forced:**
  - degree — `region::diatonicDegreeForRootPc(rootPc, keyFifths, KeySigMode)` → 0..6 / −1
    (`region/sparsechordrefinement.h`);
  - quality — `analysis::ChordQuality` enum (`types/analysistypes.h`) + `analysis::Extension` bitmask
    on `ChordIdentity.extensions` (`chord/chordanalyzer.h`);
  - RN — `ChordSymbolFormatter::formatRomanNumeral` / the L5 wrap `deriveBaseRomanNumeral`.
- **`functionprogression` licensed-progression predicate reusable** — `isLicensedProgression` + the four
  sub-predicates (`isDescendingFifth/Third`, `isAscendingSecond`, `isAppliedResolution`) over
  `ProgressionChord{rootPc, quality}` — exactly the descending-fifth / descending-third / ascending-second /
  applied-resolution content for the pairwise motion.
- **Span input representable** — `FunctionLayerOutput{units[], region}` (`function/functionoutput.h`): each
  unit carries `committedIdentity` (root/bass/quality/extensions) + ticks; `region` carries
  `localTonicPc`/`localMinorMode`. The query span (`SpanChord`/`VocabularySpan`) maps from that and is
  hand-constructible in tests.
- **No production-path change** — the component is additive and unreferenced by production.

## §2 what I reused vs. built

**Reused (no parallel encoding — the firewall discipline):**
- `analysis::ChordQuality` (the triad quality) + `analysis::Extension`/`hasExtension` (the seventh bits) —
  composed by `SeventhRequirement`, NOT a second quality enum.
- The licensed-progression CONTENT (descending-fifth / -third / ascending-second / applied resolution) is
  `functionprogression`'s predicate domain; the catalog's named progressions are its multi-chord extension
  (the §5.2 entries encode those motions as concrete skeletons).
- The DEGREE notion — the skeleton's scale-degree is the chromatic semitone offset `(rootPc − tonicPc) mod 12`,
  the same root-relative-to-tonic notion `diatonicDegreeForRootPc` computes (kept chromatic, see declared
  decision below).

**Built (new, dormant):**
- `src/composing/analysis/vocabulary/harmonicvocabulary.{h,cpp}` (namespace `mu::composing::analysis`):
  the data model (`StyleTag`, `SeventhRequirement`, `ChordDegreeStep`/`LineDegreeStep`, `FunctionalSkeleton`
  tagged union, `SubstitutionMapping`, `Entry`, `SpanChord`/`VocabularySpan`, `VocabularyCandidate`,
  `SubstitutedMember`, `GenerativeSlot`); the `HarmonicVocabulary` class with the four §4 queries
  (`browse`/`recognise`/`suggest`/`expand`); the in-code seed catalog; the generative spine via `expand`.
- `src/composing/tests/harmonicvocabulary_tests.cpp` — 16 oracle-asserted tests.

## §3 seed catalog inventory (the §5 first-pass content, in-code)
**Generative spine (`expand`, §5.1):** per target degree x → `V7/x`, `viio7/x`, `IIm7/x`, `subV7/x`, and the
sub's related ii (`IIm7/subV7/x`) — a function, not enumerated rows.

**Progression entries (§5.2):**
- Cadential (overlap L5 §5.2): Authentic V–I (major + minor), Deceptive V–vi (major + minor ♭VI), Plagal
  IV–I, Phrygian half iv6–V.
- ii–V family: ii–V–I (common-practice triads), IIm7–V7–Imaj7 (major), iiø7–V7–i (minor), incomplete ii–V.
- Turnarounds: I–vi–ii–V, I–VI7–ii–V, iii–vi–ii–V, rhythm-changes A-section.
- Sequences: circle-of-fifths (full I–IV–viio–iii–vi–ii–V–I; partial iii–vi–ii–V–I), descending-thirds.
- Bass-line / pop loops: lament bass (BASS line), Andalusian, Doo-wop, Axis, Pachelbel.
- Galant (harmonic/bass pattern only): Prinner (BASS line 4̂–3̂–2̂–1̂), Romanesca (chords), Do-Re-Mi (MELODY
  line), Monte/Fonte (harmonic-pattern approximations).
- Advanced jazz: Backdoor ♭VII7–I, Coltrane changes (major-thirds tonic cycle).

**Substitution entries (§5.3):** Secondary dominant, Related ii–V, Tritone sub, Diatonic functional, Modal
interchange, Diminished approach, Deceptive resolution, Line cliché. (Upper-structure/voicing is explicitly
OUT per §5.3 — intentionally not an entry.)

## §4 the four queries (signatures fixed here; semantic contract = the spec's)
- `browse(styleSubset=all)` → every enumerated entry in the active styles, ranked.
- `recognise(span, styleSubset=all)` → progression entries the span exactly realises (key-relative,
  substitution-aware), each with the substitution mapping for any substituted member; ranked; may be empty.
- `suggest(span, direction, styleSubset=all)` → Follow (span = a prefix) / Precede (span = a suffix) /
  Replace (applicable substitution entries + the diatonic-functional alternative); ranked; may be empty.
- `expand(targetDegreeOffset)` → the five generative slots.

Every returned candidate carries `matchScore`; v1 = **1.0 for an exact realisation** (structural
completeness), non-exact excluded. Ranked by matchScore → specificity (more-constrained/longer) → length.
Never a binary match, never a decision (the firewall).

## §5 dormancy grep proof (byte-identical-on-production)
`grep` over `src/` + `tools/` for the new identifiers
(`HarmonicVocabulary|harmonicvocabulary|VocabularyCandidate|VocabularySpan|SuggestDirection|FunctionalSkeleton|GenerativeSlot|SubstitutionMapping|SubstitutionType`):
- `src/`: 5 files — `vocabulary/harmonicvocabulary.{h,cpp}`, `tests/harmonicvocabulary_tests.cpp`, and the two
  CMakeLists. **No production consumer.**
- `tools/`: **0 files.**
⇒ unreachable from production ⇒ byte-identical by construction; corpus 53/24/53 not re-measured (instruction §4).

## §6 gate
- composing_tests **990** (was 974; +16 new vocabulary tests) — PASS.
- notation_tests **53** (4 skipped baseline) — PASS.
- pipeline_snapshot_tests **11/11** — **NO golden refresh** (nothing in the production path changed).
- corpus **53/24/53 — unchanged BY CONSTRUCTION** (dormant; not re-measured).
- default constants only; no scoring/gate/template/`kTemplateCount` change; `upstream` untouched.

## §7 DECLARED build-decisions (to Cowork — declared, not acted-on beyond this build)
1. **Placement** — new module `src/composing/analysis/vocabulary/harmonicvocabulary.{h,cpp}`, namespace
   `mu::composing::analysis` (the suggested placement; no better home found).
2. **Degree representation** — the skeleton scale-degree is the CHROMATIC semitone offset
   `(rootPc − tonicPc) mod 12 ∈ [0,11]`, the pitch-class realization of the Roman-numeral degree. This is the
   same root-relative-to-tonic notion `diatonicDegreeForRootPc` computes, kept chromatic rather than folded to
   a diatonic 0..6 — because the catalog needs chromatic degrees (♭II Neapolitan, ♭VI/♭VII modal interchange,
   subV) that the diatonic fold returns −1 for and cannot express. It is plain pitch-class arithmetic (the same
   primitive `functionprogression::rootMotion` uses), NOT a second degree enum.
3. **Quality representation** — `ChordQuality` (triad) + `SeventhRequirement` (composing the `Extension`
   seventh bits). `ChordQuality` alone conflates triad vs. seventh (V vs V7, I vs Imaj7), so the catalog needs
   the seventh aspect; `SeventhRequirement` composes the existing enums, NOT a parallel quality vocabulary. An
   Unspecified-seventh step matches regardless of seventh (still EXACT — the step simply does not constrain it).
4. **Span-type concretisation** — `SpanChord{rootPc, bassPc, quality, extensions, localTonicPc, localMinorMode}`
   carries each chord's own local key, so a modulating span is representable; v1 matches each chord key-relative
   to its own local tonic.
5. **v1 substitution-awareness** — recognise drives substitution-aware matching for the **tritone substitution**
   only (an exact, key-relative degree transform: a Major-triad dominant step may surface as a dominant-seventh
   a tritone away). It is the one §3-required case; the other substitution operations are catalog entries
   returned by browse/suggest-replace but do not (in v1) drive recognise substitution-awareness. The literal
   skeleton is unchanged; the substitution is recorded only as the underlying-function read-out (design §4.2).
6. **`matchScore` on `expand`** — `GenerativeSlot` carries `matchScore = 1.0` (a fully-specified generated
   slot) so every query return uniformly carries a structural score (instruction §2).
7. **MelodyLine skeletons (ambiguity DECLARED, not guessed)** — galant schemata defined by a MELODY (Do-Re-Mi
   1̂–2̂–3̂) are encoded as `MelodyLine` skeletons, carried in the catalog (browsable) but **not matchable** in v1:
   a committed-chord span carries no melody pc. Bass-line schemata (Prinner) ARE matched against the span's bass.
8. **Lament-bass chromatic variant** — only the BASS form `1̂–♭7̂–♭6̂–5̂` is encoded; the 5-note chromatic variant
   is a voice-leading elaboration, not a distinct v1 skeleton (declared, not encoded).
9. **Monte/Fonte** encoded as harmonic-pattern approximations of voice-leading schemata; **Ponte/Quiescenza**
   (pedal/voice-leading-defined) are NOT encoded as offset skeletons in v1 (declared); **Coltrane changes**
   encoded as the defining major-thirds tonic cycle (the full ii–V realisation spans modulations — declared as
   a representative, modulation-spanning entry).
10. **Style taxonomy (Cowork correction, applied mid-build)** — `StyleTag` is the small, replaceable
    preset-aligned set `{Baroque, Jazz, Default}` (Default = the user-run/general config); the §5 bracket labels
    map coarsely via the family helpers (common-practice → {Baroque, Default}; jazz → {Jazz}; vernacular →
    {Default}). The formal §12.1 hierarchical taxonomy is a separate joint decision with the preset system.
11. **Build trap fixed** — the `expand` local `slots` collided with Qt's force-included `#define slots` keyword
    macro (via the PCH); renamed to `genSlots`.

## §8 commit
Local-unpushed: the vocabulary module + its test + the two CMakeLists + this STATUS entry, one commit.
`upstream` untouched. STATUS.md "next" pointer set to **L6 (grouping) sign-off → build**.

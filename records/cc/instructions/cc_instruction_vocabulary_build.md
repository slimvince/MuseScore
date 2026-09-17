# CC Instruction: Build the Harmonic Vocabulary component (v1, dormant, byte-identical)

## Pre-reading (mandatory)

- `C:\s\MS\CLAUDE.md`
- `C:\s\MS\STATUS.md` — current state (read the top entry; BIR gate 53/24/53)
- `C:\s\MS\cowork_progression_schema_dictionary.md` — **the component spec you are building** (the contract)
- `C:\s\MS\cowork_progression_schema_design.md` — the consumer design (context; the consumer is NOT built here)

Use the file tools to read local files — **do not `bash cat`** local files (standing rule).

---

## Where this sits

Ratified build order: **encyclopedia → L6 → wire the consumer.** This task is step 1 — the **encyclopedia
component itself**, standalone. It is **not** L5, **not** L6, and the recognition consumer (the L5 prior + the
L6 annotation) is a **later** step. Build it **dormant**: no production consumer, byte-identical on production
by construction (the established L5-step pattern).

This is **architectural completion**, not inference problem-fixing — in scope under the standing constraint.
No accuracy tuning, no scoring/gate/template changes.

---

## Ratified build decisions (do these as specified — already settled with the user)

1. **Plain in-code catalog.** The catalog is C++ initializer data in the module (like the chord templates) —
   **no external data file, no data-file-migration scaffolding.** It is extended only by source contributors,
   so runtime extensibility is a non-goal. Design for contributor **readability**, not for serialisation.
2. **Type reuse — no parallel encoding (the firewall discipline L5 followed reusing `formatRomanNumeral`).**
   The functional skeleton and the recognise matcher **reuse the existing degree + chord-quality + Roman-numeral
   machinery** — confirm at source which to reuse (candidates: `analysis/function/functionromannumeral`,
   `region::diatonicDegreeForRootPc`, the `ChordSymbolFormatter` RN path, `ChordIdentity`/the quality enum) and
   **reuse `analysis/function/functionprogression`'s licensed-progression predicate** for the pairwise-motion
   content (descending-fifth / descending-third / ascending-second / applied resolution). Do **not** define a
   second degree/quality vocabulary.
3. **Skeleton = a tagged union.** A progression entry's skeleton is **either** a chord-degree sequence
   (key-relative `(scale-degree, quality)` pairs) **or** a bass/melody-degree sequence (for the bass-line and
   galant entries — e.g. Prinner's bass `4̂–3̂–2̂–1̂`). One representation holds both.
4. **v1 matcher = exact, key-relative, structural.** `recognise`/`suggest` match by **exact key-relative
   skeleton realisation**, substitution-aware (via the substitution entries). Rank by **specificity** (longer /
   more-constrained skeleton first) then **length**. The `matchScore` field exists on every returned entry but
   v1 sets it to a structural-completeness value (1.0 for an exact realisation; non-exact entries are excluded).
   The **fuzzy / partial / metric-sensitive** scoring is **precision-phase, deferred** (the consumer design's
   "conservative recogniser, near-exact only"). Do not build the fuzzy matcher.
5. **Dormant / byte-identical.** No `src/` production consumer. The component is reachable only from its own
   module + its unit tests. Corpus gate stays **53/24/53 by construction** (not re-measured — the L5-step
   precedent + CLAUDE.md scoping).
6. **★ CORRECTED (user, 2026-06-30) — style tags = the existing scoring presets `{Baroque, Jazz, Default}`,
   provisional.** Do **NOT** build the §12.1 16-value taxonomy as a committed enum (that pre-empts the unratified
   joint taxonomy decision, spec §12.1). Tag entries with the **three presets the analyzer already has**,
   multi-valued, mapping the §5 bracket labels coarsely: `[common-practice]`/`[galant]` → `Baroque`;
   `[jazz]`/`[chiefly jazz]` → `Jazz`; `[all styles]` and `[pop]`/`[folk]`/`[blues]` (no preset exists) →
   `Default` (general). Keep the `StyleTag` type **small and trivially replaceable**: the richer idiom set is
   about to be put on **empirical footing** by the style-clustering work (`cowork_style_clustering_plan.md`),
   which may redefine the idioms entirely (possibly not even genre-based) — so do not entrench any taxonomy here.
   The component only carries labels; style *behavior* is the consumer's.
   *(If `harmonicvocabulary.h` already has the 16-value enum, replace it with the 3-value set + the coarse mapping.)*

---

## §0 — working-tree sweep

`git status -s; echo "exit:$?"` — confirm a clean start (only the gitignored `scratch_artifacts/` expected
untracked). If `cc_instruction_vocabulary_build.md` shows untracked, that is this file — ignore it. Report any
unexpected dirty file before building.

---

## §1 — read-only confirm (the L5-step pattern — GREEN before you build)

Confirm at source, and **STOP + report** if any is false:
- the degree + quality + RN types of decision (2) are reachable/reusable (no duplicate formatter forced);
- `functionprogression`'s licensed-progression predicate is reusable for the pairwise content;
- the **span input** the queries consume — a contiguous run of committed chords, each with decided
  function + key — is representable from the existing `functionoutput` / `ChordIdentity` / region key types
  (this is the consumer's eventual input; here, build the query to accept that shape, hand-constructible in tests);
- nothing requires a production-path change (the component is additive and unreferenced by production).

Record what you reuse vs. what is new.

---

## §2 — build the component (dormant)

Create a new module under `src/composing/analysis/` (suggested `analysis/vocabulary/harmonicvocabulary.{h,cpp}`,
namespace `mu::composing::analysis` — adjust placement with a one-line declaration if a better home exists).

**Data model (spec §3):**
- `Entry` — `name`, `styleTags[]` (decision 6), `kind ∈ {Progression, Substitution}`, `provenance`; for a
  progression entry the **skeleton** (decision 3); for a substitution entry the **substitution mapping** (the
  surface→underlying-function rule, spec §3/§5.3).
- The **generative spine** (spec §5.1) as a function, not enumerated rows: `expand(degree x)` → the per-degree
  slots `V7/x, viio7/x, IIm7/x, subV7/x`, and the sub's related ii (spec §4 Expand).

**The four queries (spec §4 — fix the concrete signatures here; the semantic contract is the spec's):**
- `browse(styleSubset)` → every enumerated entry in the active styles.
- `recognise(span, styleSubset)` → progression entries the span exactly realises (key-relative), each with the
  substitution mapping for any substituted member; ranked (decision 4). May be empty.
- `suggest(span, direction, styleSubset)` → `follow` (entries with the span as a prefix) / `precede` (as a
  suffix) / `replace` (substitution entries applicable + same-function diatonic alternatives); ranked. May be empty.
- `expand(x)` → the generative slots for `x`.

Every return is a **ranked list of candidates carrying `matchScore`**; **never** a binary match, **never** a
decision (spec §2, §6 firewall). Every query takes the active **style subset** (default = all).

**Seed catalog content** — encode the spec's first-pass lists, converting the Roman-numeral skeletons to the
reused `(degree, quality)` representation:
- §5.1 function map (diatonic / secondary / substitute-dominant / modal-interchange) — the generative spine
  via `expand` + the modal-interchange set;
- §5.2 named progressions & schemas (cadential — note these overlap L5 §5.2, reuse where they do; ii–V family;
  turnarounds; sequences; bass-line & pop loops; galant schemata **by harmonic pattern only**, decision 3's
  bass/melody skeleton; advanced jazz cycles);
- §5.3 substitution operations (secondary-dominant, related ii–V, tritone sub, diatonic sub, modal interchange,
  diminished approach, deceptive resolution, line cliché — **upper-structure/voicing is explicitly OUT**, spec §5.3).

The list is "a first pass, not exhaustive" (spec §5) — encode it faithfully; do not invent entries beyond the
spec's content (provenance discipline, spec §8). If an entry's skeleton is ambiguous to encode, **declare it**
rather than guess.

---

## §3 — tests (oracle-asserted vs the spec)

A `harmonicvocabulary_tests.cpp` (new), oracle-asserted against theory/the spec:
- `expand(x)` emits the four slots + related ii for a sample degree;
- `recognise` matches a hand-built ii–V–I span (and a minor iiø7–V7–i), in several keys (key-relative
  invariance), and returns **empty** on an unrecognised span;
- `recognise` surfaces a substituted member (a tritone-subbed V in a ii–subV–I reads the underlying dominant
  via the substitution mapping), the **literal skeleton unchanged** (spec §4.2 is the consumer's; here just the
  mapping is carried);
- `suggest follow/precede` return prefix/suffix continuations; `suggest replace` returns applicable substitutions
  + same-function diatonic alternatives; each can be **empty**;
- ranking is specificity-then-length; `matchScore` present on every candidate;
- a galant/bass-line entry matches by its **bass/melody** skeleton (decision 3).

---

## §4 — gate (byte-identical-on-production)

- `composing_tests.exe` — all pass (was 974; +N for the new tests).
- `notation_tests.exe` — **53** (4 skipped baseline), unchanged.
- `pipeline_snapshot_tests.exe` — **11/11, NO golden refresh** (nothing in the production path changed).
- **Corpus 53/24/53 — unchanged BY CONSTRUCTION, do NOT re-measure** (no production consumer; grep `src/`+`tools/`
  to PROVE the new identifiers appear only in the module + its test + the two CMakeLists, and report that grep).
- Default constants only; no scoring/gate/template/`kTemplateCount` change; `upstream` untouched.

Follow the VS Code bash rules (CLAUDE.md): append `; echo "exit:$?"`, redirect large test output to a file and
`head` it.

---

## §5 — declare, commit, report

- **Declare to Cowork** (do not act on) any build-decision you made beyond this instruction (placement,
  signature shape, any entry whose skeleton was ambiguous, the span-type concretisation) — the L5-step pattern.
- **Commit locally (do NOT push — code commits stay local-unpushed until the user calls it).** Sync rule: if any
  doc needs the new component noted, include it in the same commit. Message e.g.
  `feat(vocabulary): Harmonic Vocabulary component v1 — catalog + browse/recognise/suggest/expand (dormant, byte-identical)`.
- Write `cc_vocabulary_build_report.md` (gitignored): the §1 confirm result, what you reused vs. built, the seed
  catalog inventory, the dormancy grep proof, the gate numbers, and your declared decisions.
- Update STATUS.md as the last act: a new top entry for this build session; correct the "next" pointer to
  **L6 (grouping) sign-off → build** (the encyclopedia step now done; L6 is next in the ratified order).

**STOP and ask Cowork if:** a production-path change would be required to build it dormant; the spec content is
ambiguous to encode faithfully; or the gate is not byte-identical (any corpus/snapshot move).

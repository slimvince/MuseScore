# Spec language-precision audit (pass B) — offender inventory

> **✅ DISPOSITIONED (the merged Cowork doc pass, 2026-07-03).** All 87 rows executed against the four documents
> (every HIGH source-verified before rewriting; §0 tables added to L4 + the dictionary; L5's §5.0/§12 rows extended;
> L6's residue fixed in place). Retained as the audit record; row texts describe the PRE-pass state.

**Auditor:** Cowork subagent, 2026-07-03.
**Razor:** the two "Writing standard" sections of `cowork_design_doc_template.md` — (1) *qualified predicates* (every
two-place word names its argument/test at the point of use or via a terms row; deferring a numeric to tuning is allowed,
leaving the argument or decision structure unnamed is not); (2) *defined terms, plain vocabulary, no shorthand* (a §0
TERMS table, nothing used before its row; no invented synonyms; no "iff"/insider compression; inherited prose audited as
hard as new).
**Intended reader:** knows music theory; does NOT know this project's private vocabulary.
**Scope:** inventory only — no rewrites. Severity: **HIGH** = a rule could be misimplemented from the ambiguity;
**MED** = a reader is likely to misread but the rule survives; **LOW** = style.
**Violation classes:** UNDEFINED-TERM · INVENTED-SYNONYM · UNQUALIFIED-PREDICATE · SHORTHAND · MISSING-§0-ROW ·
TYPOLOGY-TERM-LAG.

Reference points given as § plus approximate line in the current file text.

---

## 1. `cowork_layer4_chordsymbol_design.md` (27 findings)

| §/line-vicinity | Offending text (short quote) | Violation class | Proposed fix (one line) | Severity |
|---|---|---|---|---|
| doc-wide (glossary at §12) | terms "prevailing chord", "inherit", "uncertain", "carried readings" used from the banner/§1 onward; defined only at the end | MISSING-§0-ROW | Add a §0 TERMS table per the L6 discipline; nothing used before its row (move/duplicate the §12 rows forward) | MED |
| doc-wide (known lag) | the emitted per-slice span is never named "**harmonic region [chord-rhythm]**"; "slice" never tied to the span typology | TYPOLOGY-TERM-LAG | Add the typology row: slice = the harmonic region [chord-rhythm] of the target-architecture §2.15 span family, with citation | MED |
| §10 ~l.449 / §13 ~l.471 | "the replaced **per-region** path" / "the **per-region** chord path" | TYPOLOGY-TERM-LAG | "region" unqualified is banned by the span-typology contract; qualify ("the replaced coarse-region path, pre-typology") | LOW |
| banner ~l.13 | "It is **built but DORMANT**" | UNDEFINED-TERM | Define "dormant" at first use (compiled and tested, no production call site) or cite the build plan's definition | LOW |
| banner ~l.14–16 | "the **engage-with-L5** strategy defers the production switch… deferred to the **engage step**" | UNDEFINED-TERM | State once: engage/engagement = the production switch that retires the legacy path; then use that one term | LOW |
| banner ~l.9–16 | "implements **G1** … **G2/G3** … **G6** … **G4/C1** … **§15-O2** (bounded-window joint) + **C2**" | SHORTHAND | Name each mechanism by its role with the plan ID in parentheses, or cite the build plan as the ID-defining document | LOW |
| banner ~l.14 / §7 ~l.325 | "→ L5" / "the **L4→L5** carry-fix" | SHORTHAND | Replace arrow compression with words ("handed to Architectural Layer 5"; "the Layer-4-to-Layer-5 carry correction") | LOW |
| §1 ~l.100 | "reported as the **closest** recognized tertian chord" | UNQUALIFIED-PREDICATE | Closest *by the §5 fit score* — name the measure at the point of use | LOW |
| §2 ~l.151 | "a weak preference on the likely chord vocabulary … **overridden by clear note evidence**" | UNQUALIFIED-PREDICATE | Name the test for "clear" (e.g. the notes decide when the §5 fit-plus-membership score wins by more than the preset preference's weight); as written the preset-vs-notes hand-off has no rule | HIGH |
| §2 ~l.148 | "the **pinned** analysis snapshots are refreshed" | UNDEFINED-TERM | Define "pinned snapshot" (a stored golden output a test compares exactly) or cite the testing doc | LOW |
| §2 ~l.140 | "read from the **Layer-1.5** phrase-boundary primitive (its **texture strength profile**…)" | UNDEFINED-TERM | Layer 1.5 (the shared derived-view stratum) is never introduced in this document; define or cite at first use, and gloss "texture strength profile" | MED |
| §2 ~l.141 | "never Layer 6's assembled **punctuation-span**" | UNDEFINED-TERM | Cite the defining document (L6 §0) at first use of "punctuation-span" | LOW |
| §5 ~l.272–277 | "pins the root … where the spelling is **present and internally consistent** … only where the spelling is **absent or contradicts the other evidence** does it defer" | UNQUALIFIED-PREDICATE | State the consistency test (e.g. every sounding tone spells the stacked-thirds pattern on the candidate root, no member enharmonically re-spelled) and enumerate which "other evidence" can contradict and by what comparison — the pin-vs-defer branch is this layer's signature rule and currently has no stated test | HIGH |
| §5 step 4 ~l.260 | "enough **independent** chord tones … (three distinct chord tones)" | UNQUALIFIED-PREDICATE | Two words for one test ("independent" vs "distinct"); state it once: distinct pitch classes, doublings not counted | LOW |
| §7 ~l.319 | "the bass-versus-root distinction … is what **the home metric** scores" | UNDEFINED-TERM | "The home metric" is never defined here; name it (the held-out chord-root+bass agreement of §10) | MED |
| §7 ~l.324 | "the V7/x applied gate, and the **Ger+6-vs-It+6 nationality**" | SHORTHAND | "the German versus Italian augmented sixth"; abbreviated chord names are insider compression | MED |
| §7 ~l.323 | "the **aug6** spelling markers (♯13/♯11)" | SHORTHAND | "augmented-sixth spelling markers" | LOW |
| §7 ~l.324 | "the **V7/x applied gate**" | UNDEFINED-TERM | "Gate" is unexplained here; write "the applied-dominant trigger (Layer 5 §5.6)" | LOW |
| §7 ~l.333 | "(`isPedalPoint`/`pedalBassPc` are **not** carried…)" | SHORTHAND | Code identifiers doing explanatory work in the body; say "the pedal-point flags" in prose, identifier as a marked locator | LOW |
| §8 ~l.351 | "resolves the carried readings at its **gated entry**" | UNDEFINED-TERM | Name the gate (Layer 5's §5.5 entry conditions) or drop "gated" | MED |
| §10 ~l.411 | "the **BIR=false** cases" | SHORTHAND | Expand at first use ("bass-is-root = false") and cite the gate-policy document | MED |
| §10 ~l.415 | "plain segmentation **over-grab**" | INVENTED-SYNONYM | Standard phrasing exists: over-segmentation / a slice spanning two ground-truth chords; define if the coinage is kept | LOW |
| §10 ~l.415 | "the **change-point slicing** removes by construction" | UNDEFINED-TERM | Cite the Layer-2 spec that defines change-point slicing at the point of use | LOW |
| §15-O1b ~l.529 | "the fine-grain chord override — the **class-(b) transients**" | UNDEFINED-TERM | class-(b) is never defined in this document (only in the L5 glossary / gate policy); define (a root/key error at a pitch-class-decidable sonority) or cite at the point of use — the override *duty* hangs on it | HIGH |
| §15-O1b ~l.532/536 | "its ranked `alternatives` (**∪** the prevailing chord) … capped (**`topK`**)" | SHORTHAND | Replace the set-union symbol with "together with"; "capped at a fixed number of highest-ranked readings (a tunable)" | LOW |
| §15-O1b ~l.538/545 | "A **lock-in test** pins the carry" | UNDEFINED-TERM | Define "lock-in test" (a unit test asserting the carried fields exist and are populated) once | LOW |
| §15-O3 ~l.559 / §14 ~l.495 | "at the **precision phase** … (**style-only-in-calibration** contract)" / "Erlangen **FMP**" | UNDEFINED-TERM (+SHORTHAND) | Define "precision phase" (the later numeric-calibration phase; L5 calls it "the firewall") and cite the style contract's document; expand FMP (Fundamentals of Music Processing) | LOW |

**L4 counts:** UNDEFINED-TERM 12 · UNQUALIFIED-PREDICATE 4 · SHORTHAND 7 · INVENTED-SYNONYM 1 · MISSING-§0-ROW 1 ·
TYPOLOGY-TERM-LAG 2. (HIGH: 3.)

---

## 2. `cowork_layer5_function_design.md` (27 findings)

| §/line-vicinity | Offending text (short quote) | Violation class | Proposed fix (one line) | Severity |
|---|---|---|---|---|
| §12 "Ambiguity kind" ~l.652 vs §5.5 ~l.333 | glossary row lists **five** kinds "(transition, share-tone, relative pair, close, insufficient)"; §5.5 says "exactly the **six** ambiguity kinds" incl. **symmetric-rotation** | MISSING-§0-ROW | Add symmetric-rotation to the glossary row so the two enumerations match — a resolver enumerating kinds from the glossary drops one §5.5 rule | HIGH |
| §5.0 ~l.163 | "a cadence confirms it **iff** the cadence's arrival falls inside it" | SHORTHAND | "if and only if" (explicit razor rule) | LOW |
| §8 case 4 ~l.527 | "override **iff** the contradiction is decisive" | SHORTHAND | "if and only if" | LOW |
| §5.0 ~l.163 | "the as-built **`LocalKeySpan`**" | SHORTHAND | Code identifier in the §1–§12 body (the doc's own code-free rule); body says "the key-span record", identifier to §13 | LOW |
| §5.0 ~l.168 | "a punctuation boundary (**the L1.5 picked tick**)" | UNDEFINED-TERM | Expand: the boundary tick the Layer-1.5 phrase-boundary primitive selects by peak-picking; "L1.5" and "picked tick" are both insider handles | MED |
| §5.0 ~l.166 / §12 "Region" ~l.655 | "bounded by a look-ahead window (**≈ the phrase**)" / "cross-cuts **phrases**" | TYPOLOGY-TERM-LAG | "phrase" is reserved for the melodic [MT] unit after the L6 rename; write "≈ one punctuation-span's extent" (the L6 §15-7 propagation pass, still pending here) | MED |
| §2 ~l.62 / §8 ~l.543 | "through the **one shared spelling interpreter**" | UNDEFINED-TERM | Name it — the Layer-1.5 spelling view already cited in §3 — at first use of "interpreter" | MED |
| §5.2 ★ ~l.239 | "a weak soft tonic-vote the key layer's aggregation absorbs against the **home-signature pull**" | INVENTED-SYNONYM | Spell out: the key layer's prior toward the notated key signature, with a pointer to where that prior is defined | MED |
| §5.2 ★ ~l.241 | "a **key-layer** judgement (the **cadence-anchored-key model**)" | UNDEFINED-TERM | The named model has no definition or citation; name the mechanism (the §5.2 vote consumed by the key layer's aggregation) or cite its doc | LOW |
| §5.3 ~l.305 | "notated accidentals are **sustained** and consistent with the candidate key's diatonic set" | UNQUALIFIED-PREDICATE | "Sustained" needs its argument (persisting across how many successive slices — structure named, constant tunable); "consistent" has its test, "sustained" does not | MED |
| §5.3 note ~l.309–317 | "reusing the dormant **`localmodulationdetector`** … Step-3's **`forwardoverride`** … the detector's **`kEstablishmentMinChords`**" | SHORTHAND | Code identifiers in the §5 body; describe by role (the modulation-span substrate; the forward-recompute unit; the minimum-chords establishment floor), identifiers to §13 | MED |
| §5.3/§5.5/§5.6 (multiple) | "**Step-M** check / **Step-M** measurement / **Step-2/3/4/5 build**" | UNDEFINED-TERM | Define once (the build plan's numbered steps; Step M = the measurement step) or cite the build plan at first use | MED |
| §5.5 ~l.377 | "measured as **61 Commit / 25 Inherit**" | SHORTHAND | Expand: 61 cases where Layer 4 committed, 25 where it inherited (capitalized enum-style words are code compression) | LOW |
| §5.5 carry-fix ~l.382–390 | "the emitted **STRUCT** … emits the slice's own **`chosen`** verbatim … (**readingA/readingB/alternative**)" | SHORTHAND | Body prose: "the emitted reading record / the selected carried reading"; field names to §13 | MED |
| §5.6 ~l.428 | "emits `V/iv` … in **62/29/56 units**" | SHORTHAND | Label the triple at the point of use (Baroque / Jazz / Default preset counts) — unreadable otherwise | MED |
| §5.6 ~l.438 / §11 ~l.633 | "a **Phase-5d** / Step-M reconciliation" / "engagement (**Phase 5d**)" | UNDEFINED-TERM | Define Phase 5d (the deferred production-engagement phase) at first use or cite the roadmap | MED |
| §8 case 2 ~l.522 | "(the **menu resolution**, §5.5)" | INVENTED-SYNONYM | "the selection among the carried readings" — drop the menu metaphor or give it a terms row | LOW |
| §7 D-L5a ~l.501 | "observed to ~25 on the **E0 spine**" | UNDEFINED-TERM | "E0 spine" has no definition or citation in this document; name the evaluation run/corpus it denotes | MED |
| §7 D-L5a ~l.505 | "publishes **`combinedBoundary = combined / (combined + k)`**" | SHORTHAND | A code formula in the §1–§12 body; state in words (a fixed monotone squash into [0,1)) and put the formula in §13 or the contract doc | LOW |
| §10 ~l.602 | "**The corpus gate** (the two-tier root-error gate) governs as for the lower layers" | UNDEFINED-TERM | Cite the gate-policy document by name at the point of use (the §12 class-(b) row says only "see the gate policy", no locator) | MED |
| §10 ~l.593 | "**coverage-matched** accuracy and correct residual-marking" | UNDEFINED-TERM | Define: accuracy compared at equal answered-fraction (abstentions held equal) | LOW |
| §5.6 ~l.441 / §15-0 ~l.714 | "this is **byte-identical** now" / "**byte-identical** on production" | UNDEFINED-TERM | Define once: produces byte-for-byte identical production output (no observable change) | LOW |
| §5.5 ~l.363 | "(the gate-policy **class-(a)**: pitch-class-undecidable…)" | UNDEFINED-TERM | class-(a) has no glossary row (class-(b) does); add the paired row or cite the gate policy | MED |
| §3 ~l.81 | "(the **override-readiness forward-carry**)" | INVENTED-SYNONYM | Restate the mechanism at first use (the ranked-alternatives-plus-uncertainty carry that makes the §8 override possible) and keep one named term with a row | LOW |
| §5.6 ~l.429–434 | "(**L5-close review** D1, 2026-06-29)" / D2 / D3 | UNDEFINED-TERM | The review has no document locator anywhere in the spec; cite its file at first reference | LOW |
| §3 ~l.96 | "the **DCML** harmony-annotation standard" | SHORTHAND | Expand the initialism once (the Digital and Cognitive Musicology Lab standard) with its citation | LOW |
| §5.2 ★ ~l.237 | "a position-independent dominant signature (**admits robustly**)" | UNQUALIFIED-PREDICATE | Robust against what — name it (admits the cadence regardless of inversion/position) | LOW |

**L5 counts:** UNDEFINED-TERM 11 · UNQUALIFIED-PREDICATE 2 · SHORTHAND 9 · INVENTED-SYNONYM 3 · MISSING-§0-ROW 1 ·
TYPOLOGY-TERM-LAG 1. (HIGH: 1.)

---

## 3. `cowork_layer6_grouping_design.md` (17 findings)

*The §0 terms discipline holds well in the body; nearly all residue is in the status banner and the §10/§15
status prose — insider compression that predates or bypasses §0.*

| §/line-vicinity | Offending text (short quote) | Violation class | Proposed fix (one line) | Severity |
|---|---|---|---|---|
| banner ~l.5 | "over **hand-injectable POD views**" | SHORTHAND | "plain-data input structures a test can construct by hand" — POD is programmer slang | LOW |
| banner ~l.7 / §15-1 ~l.415 | "the 16 **dev beds**" / "the richest cadence **beds**" | UNDEFINED-TERM | Define "bed" (a development-split sub-corpus used as a test bed) or cite the registry split it comes from | MED |
| banner ~l.7 | "**exact-interior 718/718**" | SHORTHAND | Name the metric: interior span boundaries exactly matched, n of n | LOW |
| banner ~l.12 | "Dormancy **grep-proven**; **gate 53/24/53** exact" | SHORTHAND | "no production call site (verified by source search); the corpus gate unchanged on all three presets (Baroque 53 / Jazz 24 / Default 53)" — the unlabeled triple recurs at §10 | MED |
| banner ~l.5 | "18 oracle-asserted tests (**composing 1033**)" | SHORTHAND | Label the number ("the composing suite's 1033 tests total") | LOW |
| §0 punctuation-span row ~l.65 | "a harmonic / annotation grouping construct — **spelling-blind** to melody and voice" | INVENTED-SYNONYM | "Blind to melody and voice"; "spelling-blind" already means enharmonic-spelling-blind elsewhere in the project — a mis-transferred term | MED |
| §5.1 ~l.209 | "acting on it … is the **orchestrator's** decision" | UNDEFINED-TERM | The orchestrator has no §0 row or citation; name it (the pipeline driver defined in the target-architecture / bounded-context contract) | MED |
| §5.2 ~l.235 | "once the **D-L3a close-out** lands, the one declared L3/L5 number, not the **diagnostic sigmoid**" | UNDEFINED-TERM | Cite the document defining D-L3a; name the "diagnostic sigmoid" (the L3 diagnostic confidence squash) — neither resolvable from this doc | MED |
| §5.2 ~l.235 | "[0,1], **Class-M-declared**" | UNDEFINED-TERM | The citation to the confidence contract exists; add the one-phrase gloss ("declared in the contract's measurable class M") so the row reads without the other doc | LOW |
| §11 ~l.362 | "`bwv112.5` has no fermata — a **1-stem edge**" | UNDEFINED-TERM | "Stem" = a corpus file's base name in project usage; a musician reads note-stem — write "a single-score edge case" or define the project sense | MED |
| §15-1 ~l.408 | "the full **DLC container (40/40)**" | SHORTHAND | Expand DLC at first use (the DCML corpus container) and say what 40/40 counts | MED |
| §15-1 ~l.416 | "per the **engage-criteria E2** discipline" | UNDEFINED-TERM | Cite the engage-criteria document and gloss E2 (held-out data untouched until engagement) | MED |
| §5.4 ~l.269 | "composed entirely of **confidently-read** units is reported as fully resolved" | UNQUALIFIED-PREDICATE | Name the test — if it is simply "no open mark", say so; "confidently" invites a confidence threshold that does not exist | MED |
| §3 ~l.150 | "(… cues, **max-normalised, peak-picked**)" | SHORTHAND | Gloss the two signal-processing terms (strengths scaled to the strongest cue; local maxima selected as boundaries) | LOW |
| §10 ~l.349 | "later, at the **pre-inference boundary**" | UNDEFINED-TERM | Name the phase in plain terms (before the inference phase opens) with a roadmap citation | LOW |
| banner ~l.11 | "**default-inert**" | SHORTHAND | "inert under default settings (changes no output unless explicitly enabled)" | LOW |
| §0 Slice row ~l.71 | "the **§2.15 span typology**" (first use names no document) | SHORTHAND | "the target-architecture §2.15 span typology" at the first mention (later mentions do name it) | LOW |

**L6 counts:** UNDEFINED-TERM 7 · UNQUALIFIED-PREDICATE 1 · SHORTHAND 8 · INVENTED-SYNONYM 1 · MISSING-§0-ROW 0 ·
TYPOLOGY-TERM-LAG 0. (HIGH: 0.)

---

## 4. `cowork_progression_schema_dictionary.md` (16 findings)

| §/line-vicinity | Offending text (short quote) | Violation class | Proposed fix (one line) | Severity |
|---|---|---|---|---|
| doc-wide (glossary at §10) | "entry", "functional skeleton", "generative slot", "span" all used (§1–§4) before their §10 rows; no §0 | MISSING-§0-ROW | Add a §0 terms table (or move the glossary forward); nothing used before its row | MED |
| §4 ~l.79 | "a **match score** — the component's structural measure of **how well** the input realises … the entry" | UNQUALIFIED-PREDICATE | Name the measure's structure (what is credited: matched members, order, length, substituted-member penalty) even with constants deferred — every consumer thresholds this number and its decision structure is unnamed | HIGH |
| §4 ~l.69 | "the progression entries whose functional skeleton that span **realises**" | UNQUALIFIED-PREDICATE | Define "realises": the degree-quality match rule, whether partial spans match, and how a substituted member matches (via a substitution entry?) — the core *recognise* semantics | HIGH |
| §4 ~l.79 | "ranked by it (secondarily by **specificity**, then length)" | UNQUALIFIED-PREDICATE | Define the specificity ordering (more constrained skeleton? fewer free parameters?) — a tie-break rule with no test | MED |
| §4 ~l.75 | "and **the sub's related ii**" | SHORTHAND | "the tritone substitute's related supertonic (§5.1)" — "sub" is jazz-insider clipping, and "related ii" is used here before its §5.1 definition | MED |
| §5.1 ~l.106 | "The functional flow is **T → (T) → SD → D → T**" | SHORTHAND | Expand T/SD/D and state what the parenthesized (T) permits (an optional tonic-family interpolation?) — currently a private diagram | MED |
| §5.1 ~l.105–106 | family named "**pre-dominant** family" in one clause, abbreviated "**SD**" (subdominant) in the next | INVENTED-SYNONYM | Two names for one function class; pick "pre-dominant" (the term §5.2 and the L5 spec use) | LOW |
| §5.2 ~l.124 | "the **rhythm-changes A-section**" | UNDEFINED-TERM | Define or cite (the "I Got Rhythm" A-section turnaround, `I–vi–ii–V` family) — a classical-side reader does not know it | MED |
| §5.2 ~l.132 | "**Monte** (ascending sequence)" | UNDEFINED-TERM | The gloss cannot be encoded as a functional skeleton (contrast Fonte's); give the pattern (an ascending-by-step chain of applied-dominant resolutions) or cite its catalog entry precisely | MED |
| §5.2 ~l.125/130 | "circle-of-fifths (`**…**iii–vi–ii–V–I`)" / "Romanesca (descending bass, `I–V–vi–iii**…**`)" | SHORTHAND | Ellipses inside skeletons are unencodable; complete the pattern or state the continuation/entry-point rule | MED |
| §5.2 ~l.125 | "the **secondary-dominant'd** `I–VI7–ii–V`" | SHORTHAND | "with VI7 as a secondary dominant of ii" — invented verbing | LOW |
| §5.2 ~l.128 | "Axis `I–V–vi–IV` (**and rotations**)" | UNQUALIFIED-PREDICATE | State the rule: all four rotations as one entry, or each a distinct entry — affects matching | LOW |
| §6 ~l.167 | "Diatonic-functional · Chromatic-functional · Seventh-functional · Triadic-modal · Chromatic-coloristic" | UNDEFINED-TERM | Cited to the taxonomy proposal but used as load-bearing tags; add a one-line gloss per idiom at first use | LOW |
| §5.2 ~l.121 | "(Already detected by **L5 §5.2**; listed for completeness.)" | SHORTHAND | Bare "L5" assumes the project's layer numbering; name the document (the function-layer design §5.2) | LOW |
| §3 ~l.41 | "the harmonic pattern of a **Prinner**" (first use; defined only at §5.2) | UNDEFINED-TERM | Forward-point at first use ("a Prinner, §5.2") so the named schema is never used before its row | LOW |
| §5.1 ~l.106 | "the **licensed** pairwise root motions are the descending fifth, the descending third, and the ascending second" | TYPOLOGY-TERM-LAG | "Licensed" is the L5 §5.0 defined test and its enumeration there is wider (adds applied-resolution and cadential motion); either cite L5 §5.0 or use a different word ("the primary functional root motions") to avoid a conflicting definition of a project term | MED |

**Schema-dictionary counts:** UNDEFINED-TERM 4 · UNQUALIFIED-PREDICATE 4 · SHORTHAND 5 · INVENTED-SYNONYM 1 ·
MISSING-§0-ROW 1 · TYPOLOGY-TERM-LAG 1. (HIGH: 2.)

---

## 5. Cross-document summary

| Document | UNDEFINED-TERM | INVENTED-SYNONYM | UNQUALIFIED-PREDICATE | SHORTHAND | MISSING-§0-ROW | TYPOLOGY-TERM-LAG | Total | HIGH |
|---|---|---|---|---|---|---|---|---|
| L4 chord-symbol | 12 | 1 | 4 | 7 | 1 | 2 | 27 | 3 |
| L5 function | 11 | 3 | 2 | 9 | 1 | 1 | 27 | 1 |
| L6 grouping | 7 | 1 | 1 | 8 | 0 | 0 | 17 | 0 |
| Schema dictionary | 4 | 1 | 4 | 5 | 1 | 1 | 16 | 2 |
| **Total** | **34** | **6** | **11** | **29** | **3** | **4** | **87** | **6** |

### The three worst (HIGH) offenders across all four documents
1. **L4 §5 (~l.272–277) — the symmetric-root spelling-pin rule:** "pins the root … where the spelling is *present and
   internally consistent*; only where the spelling is *absent or contradicts the other evidence* does it defer."
   Neither "internally consistent" nor "contradicts" names its test, and this is the layer's signature pin-vs-defer
   branch — an implementer cannot decide from the spec when to pin a diminished-seventh's root and when to abstain.
2. **Schema dictionary §4 (~l.69/79) — the recognition semantics:** "entries whose functional skeleton that span
   *realises* … a *match score* — the component's structural measure of *how well* …" The entire query contract
   (recognise, suggest, ranking, and every consumer's threshold) rests on a match relation and a score whose decision
   structure is never stated — not even which features are credited.
3. **L5 §12 vs §5.5 — the ambiguity-kind enumeration lag:** the glossary row lists **five** kinds; §5.5 states "exactly
   the **six** ambiguity kinds" including **symmetric-rotation**. A resolver implemented from the glossary's enumeration
   silently drops the §5.5 symmetric-rotation rule (and the L4 spec never defines the kinds at all — its "class-(b)
   transients" §15-O1b is the sibling HIGH).

*(Remaining HIGH rows, for completeness: L4 §2 "overridden by clear note evidence" — the preset-vs-notes hand-off has
no rule; L4 §15-O1b "class-(b) transients" — the override duty rests on a term this document never defines.)*

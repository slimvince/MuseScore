# Spec language-precision audit — offender inventory (pass A)

> **✅ DISPOSITIONED (the merged Cowork doc pass, 2026-07-03).** All 67 rows executed against the four documents
> (every HIGH source-verified before rewriting; §0 TERMS tables added to all four). This file is retained as the
> audit record; the row texts below describe the PRE-pass state.

**Audited 2026-07-03 against the two "Writing standard" sections of `cowork_design_doc_template.md`:**
(1) qualified predicates (2026-06-24) — every two-place word names its argument/test; deferring a numeric value is
allowed, leaving the argument unnamed is not; (2) defined terms / plain vocabulary / no shorthand (2026-07-02) —
§0 TERMS discipline, no invented synonyms, no insider compression, inherited prose audited as hard as new.
Reader model: knows music theory; does NOT know this project's private vocabulary.
Span-typology reference: ARCHITECTURE.md §2.15 (constant-sonority slice · harmonic region · key-span ·
punctuation-span · decision-context span · cadential scope; **unqualified "region" is banned**).

Violation classes: UNDEFINED-TERM · INVENTED-SYNONYM · UNQUALIFIED-PREDICATE · SHORTHAND · MISSING-§0-ROW ·
TYPOLOGY-TERM-LAG. Severity: HIGH = a rule could be misimplemented from the ambiguity; LOW = style.
Inventory only — no rewrites performed.

---

## Doc 1 — `cowork_layer1_note_model_design.md` (Layer 1, note model)

**§0/terms discipline:** No §0 TERMS table. Has a tail glossary (§12, "only terms we coined"), which does not
enforce "nothing used before its row" — e.g. "imported cue notes" (§7) is explained only in §13; "staff-eligible"
is coined in §12 but the body never uses it.
**§2.15 typology terms it should adopt:** the known lag — L1 never equates its covered span to the
bounded-context/§2.15 vocabulary (**loaded span / selection / context span**; the substrate every span family is
cut from). "The analysed span" / "widen the span" are private synonyms for contract terms that exist.

| §/line-vicinity | Offending text (short quote) | Class | Severity | Proposed fix (one line) |
|---|---|---|---|---|
| §1 ("keeps but marks"), §7, §12 | "the chord-symbol track" | UNDEFINED-TERM | HIGH | The staff-eligibility rule excludes it, but which staff/track this is (the project's dedicated chord staff) is never defined or cited — define it or cite the chord-staff configuration that marks it. |
| §10 | "the project-wide per-event accuracy metric and both automated test suites stay green" | UNDEFINED-TERM | HIGH | Which metric and which two suites? Name/cite them (the reader cannot run the system check from this doc). |
| §2 "stay fast", §8 "Fast at any selection size", §10 "confirming it stays fast" | "fast" | UNQUALIFIED-PREDICATE | HIGH | Fast by what bound? The §10 acceptance test has no criterion and can be written vacuously — name the complexity/time budget the measurement checks. |
| Status banner, §3, §11 | "Phase-1a" / "Phase-1b" | UNDEFINED-TERM | LOW | Delivery-phase labels used as load-bearing status without citing the delivery plan that defines them. |
| §3 status note | "append-only, exactly one step, no convergence loop" | SHORTHAND | LOW | Contract vocabulary compressed; restate ("one widening per request; the caller, not this layer, iterates") — the cited bounded-context doc softens but does not remove the compression. |
| §1 | "a clean, complete list" | UNQUALIFIED-PREDICATE | LOW | "Clean" by what test? Replace with the defined properties (tie-resolved, lossless) or drop the word. |
| §2, §6 | "so the prevailing key before the selection can be seen" | UNQUALIFIED-PREDICATE | LOW | "Prevailing"/"can be seen" by what test? Point at L3's operational stop condition (the leading-edge key stops changing). |
| §7 | "imported cue notes" | MISSING-§0-ROW | LOW | Used inside the "does it sound" data rule before its only explanation (§13) — add a terms row or forward citation. |
| §3, §5, §12, §14 | "weightedPcView" | SHORTHAND | LOW | "Pc" compression in a name doing prose work; gloss "(the weighted pitch-class view)" at first use. |
| §11, §13 | "moved the project's accuracy metric by a small amount" | UNQUALIFIED-PREDICATE | LOW | "Small" by what threshold? State the number or cite the measurement record. |
| §3, §11 | "byte-identical" | UNDEFINED-TERM | LOW | Project discipline term; define once ("output identical byte-for-byte to the previous behaviour on the pinned outputs"). |
| §11 | "the batch-testing path" | UNDEFINED-TERM | LOW | Which path? Name the offline corpus-testing harness. |
| §1–§12 throughout | "the analysed span", "widen the span" | TYPOLOGY-TERM-LAG | LOW | Never equated to the contract's **loaded span / selection / context span**; adopt the §2.15/bounded-context names (the doc cites the contract but keeps private synonyms). |
| §12 vs consumers | "**Staff-eligible** — the note's staff takes part in tonal analysis" | TYPOLOGY-TERM-LAG | LOW | Coined only in the glossary, never used in the body; downstream (phrase-boundary doc) cites Layer 1 for "eligible **voice**", which L1 never defines — align the term and its granularity (staff vs voice) here. |

**Out-of-class note:** the §3 as-built insertion narrates API names (`extend(Direction, int)`, `boundaryReached()`)
in prose — borderline against the template's locator-vs-mechanics line, flagged for the template owner.

**Doc 1 counts:** UNDEFINED-TERM 5 · UNQUALIFIED-PREDICATE 4 · SHORTHAND 2 · MISSING-§0-ROW 1 ·
TYPOLOGY-TERM-LAG 2 · INVENTED-SYNONYM 0 — **14 rows, 3 HIGH.**

---

## Doc 2 — `cowork_phrase_boundary_design.md` (Layer 1.5, phrase boundary)

**§0/terms discipline:** No §0 TERMS table. Has a good mid-tail glossary (§9), the best of the four, but terms are
used before their rows ("tick" is never in it at all; "eligible" from §2–§3, glossed only in §9 via a dangling
citation) and one glossary row contradicts the body (see the "running mean" row).
**§2.15 typology terms it should adopt:** **punctuation-span** — after the 2026-07-01 rename ("phrase [MT]" reserved
for the melodic voice-leading object), this primitive's output is the *cue that delimits the punctuation-span*
(§2.15 says so explicitly); the doc states its typology role only in §11-5, while §1/§9 still define the output
against an untyped "musical phrase".

| §/line-vicinity | Offending text (short quote) | Class | Severity | Proposed fix (one line) |
|---|---|---|---|---|
| §1 and throughout | "a phrase boundary is a **tick** where a musical phrase ends" | UNDEFINED-TERM | HIGH | "Tick" (the time unit) is never defined and is absent from §9; the sibling L1/L2/L3 docs say "time-position" — define tick = absolute time-position and reconcile the two names (one thing, two project words). |
| §3 consumes, §9 glossary | "the **eligible** voices ... (**Eligible voice** — a voice on a staff that takes part in tonal analysis (defined in Layer 1))" | UNDEFINED-TERM | HIGH | Dangling citation: Layer 1 defines *staff*-eligibility plus separate sounds/visible flags, never voice eligibility — every cue's input set is ambiguous (are muted/invisible notes in the per-voice profiles?); state the exact flag combination and the staff→voice mapping. |
| §9 "Peak-picking" row | "exceed the adaptive threshold (**running mean** + k·SD)" | UNDEFINED-TERM | HIGH | Contradicts §4.4's pinned rule ("whole profile, **not a sliding window**"): "running mean" names the rejected sliding mechanism — an implementer working from the glossary builds the wrong threshold; fix the row to "whole-profile mean + k·SD". |
| §2, §7 | "measured against the corpus **two-tier gate** on **both presets**" | UNDEFINED-TERM | HIGH | The acceptance gate and the presets are never named or cited (the two-tier BIR gate, Baroque/Jazz, CLAUDE.md) — the builder cannot run the check from this doc. |
| §7 | "checked against the **known phrase structure** of the corpus" | UNDEFINED-TERM | HIGH | Known from what ground-truth source? If the chorale phrase GT is itself fermata-derived, the validation is circular — name the independent source. |
| §4.1, §9 | "the standard **local-change rule** (the established surface boundary-strength formula)" | INVENTED-SYNONYM | LOW | The literature name exists (Cambouropoulos's Local Boundary Detection Model family); name and cite it — the inline formula keeps the mechanism safe, so style only. |
| §4.4 | "the standard 'Simple Picker'" | UNDEFINED-TERM | LOW | A quoted proper name with no citation; cite its entry in the methods catalog. |
| Status banner | "audited against **the three design-doc standards + the language-mechanical tests**" | UNDEFINED-TERM | LOW | Name/cite the three standards and the test documents. |
| Status banner, §11-2b | "the whole-profile peak threshold **pinned**" / "**pin** them with non-chorale test cases" | UNDEFINED-TERM | LOW | "Pinned" is project jargon (fixed by ratified decision/regression test); define once. |
| §2 | "deferred constants (**the firewall**)" | UNDEFINED-TERM | LOW | Presumes the project's "inference firewall" vocabulary; the mechanism/constant split is stated, so define or drop the label. |
| §2, §4 passim | "**precision-phase** constants" | UNDEFINED-TERM | LOW | "The precision phase" (a schedule entity) is never defined or cited to the plan that defines it. |
| §1, §4.3, §5 | "the **cadence gate**" | MISSING-§0-ROW | LOW | Handle coined mid-prose (explained at §1 first use, good) but absent from the §9 glossary — add the row. |
| §3 | "see **the L5 spec**" | SHORTHAND | LOW | Bare layer letter; the doc elsewhere writes "function layer" — expand and cite the file name. |
| §4.2 | "the theoretical max is **#voices · Σ(cue weights)**" | SHORTHAND | LOW | Symbol compression inside a normative magnitude rule (the spike floor); write it out in words. |
| §4.1 | "the gap/rest is **by far the most precise** surface cue" | UNQUALIFIED-PREDICATE | LOW | Most precise by what measurement? Cite the methods-catalog result the ranking comes from. |
| §8 | "The **SOTA**-competitive reference engine" | SHORTHAND | LOW | Expand "state-of-the-art"; the intended reader is a musician, not an MIR researcher. |
| §10 | "the dormant **key-agnostic cadence anchor** and the default-off **joint-key re-key pass**" | UNDEFINED-TERM | LOW | Insider component names, uncited (background section, but the standard binds the full text). |
| Status banner | "**Class-M** boundary confidence under the cross-layer confidence contract" | UNDEFINED-TERM | LOW | The class label's defining document is not named (`cowork_confidence_contract.md`); the inline gloss covers the mechanism, so style only. |
| Status banner | "closing **gap-analysis-v2 A-2** — ruled by Cowork" / "v2 gap **A-3**" | SHORTHAND | LOW | Insider issue labels; cite the gap-analysis document or restate the gap. |
| §1, §9 (vs §11-5) | "a musical phrase ends" / "ends a phrase" | TYPOLOGY-TERM-LAG | LOW | Post-rename, state in §1/§9 that the output is the **punctuation-span** delimiter cue and that "phrase [MT]" is reserved for the melodic object (currently said only in §11-5). |

**Doc 2 counts:** UNDEFINED-TERM 12 · SHORTHAND 4 · INVENTED-SYNONYM 1 · UNQUALIFIED-PREDICATE 1 ·
MISSING-§0-ROW 1 · TYPOLOGY-TERM-LAG 1 — **20 rows, 5 HIGH.**

---

## Doc 3 — `cowork_layer2_slicing_design.md` (Layer 2, change-point slicing)

**§0/terms discipline:** No §0 TERMS table. Tail glossary (§12) is small and clean; the body mostly defines-at-use
well (best predicate discipline of the four). Main failures are insider handles in the as-built/status prose.
**§2.15 typology terms it should adopt:** the known lag — L2 never equates its **slice** to the typology's
**constant-sonority slice** (the atomic analysis unit, §2.15's founding principle), and never states the nesting
relation to the **harmonic region**; it also uses banned unqualified "region" for a plain span.

| §/line-vicinity | Offending text (short quote) | Class | Severity | Proposed fix (one line) |
|---|---|---|---|---|
| §2 ("Connected into the live analysis pipeline") | "(**the clip** is inert there)" | UNDEFINED-TERM | HIGH | "The clip" names a mechanism (presumably clipping slices to the selection/loaded span) that is defined nowhere in the document — state what is clipped, by what rule, and why it is inert on the whole-score path. |
| §7, §14 | "the collection of **pitch-letters** present" | INVENTED-SYNONYM | LOW | The standard term is *pitch class* (§14 itself says "pitch-class-mask"); "letters" wrongly suggests letter-name equivalence (C ≡ C♯) — use one standard term. |
| §2 | "feeds the result to the **key-mode sequence decoder**" | UNDEFINED-TERM | LOW | Named component without citation; cite `cowork_layer3_keymode_design.md`. |
| §2, §10 | "**byte-identical** slices on the **whole-score live path**" | UNDEFINED-TERM | LOW | Two project handles in one clause; gloss each once (identical output byte-for-byte; the production path where selection = score). |
| §8 metric-weight contract | "a **prefs-free**, key-/chord-agnostic notation-derived value" | SHORTHAND | LOW | Expand: "preference-free (independent of user settings)". |
| §8 | "the function layer's **prerequisite (i)**" | SHORTHAND | LOW | A list-item pointer into an unnamed document; cite the function-layer spec section that enumerates the prerequisites. |
| §8 | "owned there (a **Layer-1.5** notation view, beside the bass/spelling/phrase-boundary views)" | UNDEFINED-TERM | LOW | The Layer-1.5 half-tier is used without definition or citation in this doc; cite ARCHITECTURE.md/the phrase-boundary doc. |
| §10 | "leave **both automated test suites** and the **pinned analysis outputs** unchanged" | UNDEFINED-TERM | LOW | Name the two suites; define "pinned" (the golden snapshots refreshed only on verified change). |
| §11, §13 | "the old segment-first machinery (**Pass-2/2b**)" | UNDEFINED-TERM | LOW | Insider pass numbering, never defined — name the passes or cite the doc that does. |
| §13 | "about **45% of the measured error**" | UNQUALIFIED-PREDICATE | LOW | Error on which metric, measured how? Name the metric or cite the measurement record. |
| §8 bounded-context bullet | "the change-point slices for the **newly loaded region**" | TYPOLOGY-TERM-LAG | LOW | §2.15 bans unqualified "region", and here it collides with the typology's *harmonic region* while meaning a plain span — say "newly loaded span". |
| §1, §7, §12 | "**slice**" (never tied to the typology) | TYPOLOGY-TERM-LAG | LOW | Equate once: the slice IS §2.15's **constant-sonority slice**, the atomic analysis unit; state that *harmonic regions* (chord-rhythm spans) are later groupings of slices. |

**Out-of-class note (consistency, flagged for the owner):** §9's last decision still reads "Chosen: keep it
separate [not connected into the live pipeline]" while §2/§10/§11 state Layer 3 now consumes the slices — the
decision row needs an as-built/superseded annotation (rule 4: inherited prose binds).

**Doc 3 counts:** UNDEFINED-TERM 6 · INVENTED-SYNONYM 1 · UNQUALIFIED-PREDICATE 1 · SHORTHAND 2 ·
MISSING-§0-ROW 0 · TYPOLOGY-TERM-LAG 2 — **12 rows, 1 HIGH.**

---

## Doc 4 — `cowork_layer3_keymode_design.md` (Layer 3, key/mode)

**§0/terms discipline:** No §0 TERMS table. Tail glossary (§12) covers the core coinages, but the status banner and
§11 carry the densest insider compression of all four docs, and several load-bearing predicates in §1/§5/§10 are
unqualified.
**§2.15 typology terms it should adopt:** the known lag — L3 never coins **key-span** (§2.15's name for the very
object this layer produces: a maximal run of equal key/mode), and it uses banned unqualified "region" in at least
three senses (the legacy coarse analysis region, "stable/modulation regions" as measurement categories, plain spans).

| §/line-vicinity | Offending text (short quote) | Class | Severity | Proposed fix (one line) |
|---|---|---|---|---|
| §5 step 1 | "keep ... the best-scoring candidates **plus the key/mode the sequence is currently in**" | UNQUALIFIED-PREDICATE | HIGH | "Currently" has no referent at local-fit time — no sequence exists yet; is it the previous slice's Viterbi-leading candidate, every surviving predecessor, or a seed key? The anti-excursion mechanism hinges on this candidate-list rule; state the construction. |
| §2 as-built, §5, §6 | "trigger = the selection's leading-edge slice is **unsettled**" / "the opening ... has **no settled key**" | UNQUALIFIED-PREDICATE | HIGH | Settled by what test — marked "uncertain"? confidence below which level? key changing under re-decode? The reach-back trigger cannot be implemented as written. |
| §1 | "reported as the **closest** of the 21 recognized modes" | UNQUALIFIED-PREDICATE | HIGH | Closest by what measure? Presumably "highest local-fit score", but "closest" implies an unnamed scale-distance metric — name the measure. |
| §11 (sweep item) | "found none that moves **the clean set** net-positive" | UNDEFINED-TERM | HIGH | "The clean set" (a grading subset) is never defined or cited — the sweep's acceptance criterion is unreproducible; define the set or cite the sweep record. |
| §10 | "full agreement on the cases where the human analyses are **unambiguous** ... is among the **defensible** readings" | UNQUALIFIED-PREDICATE | HIGH | Unambiguous/defensible by what rule or whose adjudication? The layer's acceptance bar is untestable as stated — name the partition procedure. |
| §3 consumers; banner "per coarse region"; §11 "stable regions", "modulation regions" | unqualified "**region**" (three senses) | TYPOLOGY-TERM-LAG | HIGH | §2.15 bans bare "region"; disambiguate each use, and coin the typology's **key-span** for this layer's own output (a maximal run of equal key/mode) — the one §2.15 term Layer 3 owns and never names. |
| Status banner | "**S2** segmentation-stable seed; ... **C1** emission-confidence fidelity fixes", "the **P4 tick-local path** ... **re-split (c)** ... **S1** full seed-retire" | UNDEFINED-TERM | LOW | Increment codenames without citation to the delivery plan that defines them; cite it once. |
| Banner, §11, §15 | "the two-tier **BIR** gate", "chord/**BIR-flat**" | SHORTHAND | LOW | The acronym is never expanded in the doc (bass-is-root); the CLAUDE.md citation covers the gate but not the letters — expand once. |
| Status banner | "**duration-majority** per coarse region" | UNDEFINED-TERM | LOW | The slice→region reduction rule is named, not stated — add one clause ("the region takes the key/mode holding the majority of its duration"). |
| §1, §11 | "selecting among ... the **carried** alternatives" / "**carried** among the alternatives" | MISSING-§0-ROW | LOW | The forward-carry mechanism is stated at first use (good), but "carried" is project vocabulary with no §12 glossary row — add it. |
| §1 | "no production consumer yet → byte-identical, **with a lock-in test**" | UNDEFINED-TERM | LOW | QA jargon; say "a regression test pinning the carried data so it cannot be silently dropped". |
| §1 | "performed at its **gated** entry" / "the **gated step**" | UNQUALIFIED-PREDICATE | LOW | Gated on what condition? Cite the function-layer spec's entry condition. |
| §5 | "bring back the **O(N²)** cost" | SHORTHAND | LOW | Complexity notation for a music-theory reader; the doc's own idiom exists ("work growing with the square of the number of notes"). |
| §8 | "whether to run the optional **keyscape** refinement" | MISSING-§0-ROW | LOW | "Keyscape" first used in §8, defined/cited only in §14 (Sapp) — gloss or cite at first use. |
| §11 (leading-tone item) | "scheduled for **Phase B (B2)** of **the stabilization plan**" | UNDEFINED-TERM | LOW | Which document is the stabilization plan? Cite it. |
| §11 (same item) | "behind **the inference firewall**" | UNDEFINED-TERM | LOW | Project jargon (the mechanism/constant vs inference-quality split), undefined in this doc — define or cite. |
| §11 (shared-scorer lever) | "(measured decode-only, **+57…+73 Baroque / +38…+68 Jazz**)" | UNQUALIFIED-PREDICATE | LOW | +57 of what unit on which metric? Name it (the held-out key metric's cases?) so the wiring-time re-measurement is comparable. |
| §4, §12 | "the standard, fast **best-sequence algorithm**" | INVENTED-SYNONYM | LOW | The standard name (Viterbi dynamic programming) appears only in §14; the §12 glossary row should equate the plain-language coinage to it (the template's own glossary example lists "Viterbi"). |
| §13 | "roughly **87%** on the Baroque test set and roughly **61%** on the Jazz test set" | UNQUALIFIED-PREDICATE | LOW | Percent of what metric? Name the held-out key/mode agreement measure being baselined. |
| §11 vs §15 | "the Phase-4 **tpc**-capability foundation" (before §15 expands "tonal pitch class (tpc)") | SHORTHAND | LOW | Abbreviation used before its expansion; expand at first use (§11) or move the expansion forward. |
| §10 | "**the project-wide accuracy metric** ... on either of **the two tuning presets**" | UNDEFINED-TERM | LOW | Name/cite the metric and the presets (Bach + Jazz are named only in §14). |

**Doc 4 counts:** UNDEFINED-TERM 7 · UNQUALIFIED-PREDICATE 7 · SHORTHAND 3 · INVENTED-SYNONYM 1 ·
MISSING-§0-ROW 2 · TYPOLOGY-TERM-LAG 1 — **21 rows, 6 HIGH.**

---

## Cross-document summary

| Doc | UNDEF | INV-SYN | UNQUAL | SHORT | §0-ROW | TYPO-LAG | Total | HIGH |
|---|---|---|---|---|---|---|---|---|
| L1 note model | 5 | 0 | 4 | 2 | 1 | 2 | 14 | 3 |
| Phrase boundary | 12 | 1 | 1 | 4 | 1 | 1 | 20 | 5 |
| L2 slicing | 6 | 1 | 1 | 2 | 0 | 2 | 12 | 1 |
| L3 key/mode | 7 | 1 | 7 | 3 | 2 | 1 | 21 | 6 |
| **All** | **30** | **3** | **13** | **11** | **4** | **6** | **67** | **15** |

**§0 discipline:** none of the four documents has a §0 TERMS table (all predate the 2026-07-02 standard; rule 4
makes inherited prose auditable regardless). All four have tail glossaries (§12 / §9) that do not enforce
"nothing used before its row", and each glossary has at least one gap found above (phrase doc's is the best and
still carries the one glossary row that *contradicts* its body).

**The known typology lag, confirmed:** L1 and L2 never equate their units to the §2.15 span typology
(L1: loaded span / selection / context span; L2: **constant-sonority slice** + the harmonic-region nesting);
L3 never coins **key-span** for its own output and uses banned unqualified "region" in three senses; the
phrase-boundary doc states its **punctuation-span** delimiter role only in §11-5, not in §1/§9 where the output
is defined.

## The three worst HIGH offenders (all four docs)

1. **L3 §5 step 1 — "plus the key/mode the sequence is currently in."** The candidate-list rule that implements
   excursion suppression references a "current" sequence that does not exist at local-fit time; three inequivalent
   constructions fit the sentence, and the layer's central behaviour (brief tonicization vs modulation) differs
   under each.
2. **Phrase §9 glossary "running mean + k·SD" vs §4.4 "whole profile, not a sliding window."** A direct internal
   contradiction on the peak threshold: an implementer working from the glossary builds the sliding-window
   mechanism §4.4 explicitly pins away.
3. **Phrase §3/§9 — "eligible voice ... (defined in Layer 1)."** A dangling citation: Layer 1 defines
   staff-eligibility (plus separate sounds/visible flags), never voice eligibility — whether muted/invisible notes
   feed the per-voice cue profiles is undecidable from the two documents, and every cue's input set depends on it.

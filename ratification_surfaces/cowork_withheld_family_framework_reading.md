# The WITHHELD-FAMILY CANDIDATES for the `framework` subject — put to the user for a ruling

> **STATUS: NOT RULED. NOTHING IS WITHHELD. NO PACK IS RENDERED. NO SESSION IS BOOTED.**
>
> Prepared by Claude Code, 2026-08-28, under `cc_instruction_framework_pack_preparation.md` Task 1,
> at the tree carrying the landing commit that dispatch's Task 0 made.
>
> **This file is an ENUMERATION and nothing else.** It carries the two candidate lists the dispatch
> ordered — the ratified-design-intent entries a candidate criterion returns, and the passages of
> `CLAUDE.md` that would leak the answer through boot-pack member (2) — and it **asks the user for
> one verdict per candidate. It recommends none**, because the record does not settle the question
> and a surface that returns such a question gathers facts and makes no recommendation
> (register entry **D-658**).
>
> **★ NO PACK DIRECTORY EXISTS FOR THIS SUBJECT, AND THAT IS DELIBERATE.** A rendered pack is a
> bootable pack. The withheld set for this subject is not ruled, and a pack rendered with an empty
> family would hand a deriving session the very thing it is being asked to derive. The render is a
> later batch, after this file is ruled.
>
> **★ AND THE BATCH THAT WROTE THIS FILE MET A TOOL SHAPE IT COULD NOT REACH. §8 STATES IT.** The
> generator has no state for *enumerate the candidates and withhold nothing*: a candidate must carry
> an authored verdict or the tool STOPs, and the only verdict that withholds is `IN`. So the
> enumeration below exists, and the generator's own manifest carries **no block for this subject**.
> That is reported rather than worked around, and nothing was authored to make the tool complete.

---

## 1. The words used here, explained before anything rests on them

- **The framework document** — the product of the framework phase: the layer decomposition, each
  layer's charter, and the boundary contracts between layers.
- **A deriving session** — one that writes what the analysis SHOULD do, from music theory, from
  published research it fetches and reads, and from ruled design intent, WITHOUT reading what this
  project's code or this project's specifications say it DOES. Such a session is
  *implementation-blind*, or *blind* for short.
- **The boot pack** — the one rendered directory such a session reads at boot: six members plus a
  read-me, generated from the ruled boot list.
- **The withheld family** — the per-subject authored cuts: withheld register identities, withheld
  documents, and withheld passages inside member (2). **For this subject the family is EMPTY as
  authored, and the lists below are what the user rules into it or out of it.**
- **The leak check** — the standing per-entry test that keeps an entry whose rendered fields carry a
  `docs/` or `src/` path, the string `ARCHITECTURE.md`, a withheld identity or a withheld document's
  name OUT of the generated member, listing it instead. **Its scope is members (5) and (6) only** —
  the two the generator writes rather than quotes.
- **The candidate criterion** — the per-subject authored pattern that PROPOSES candidates for
  withholding. **It proposes; the user rules.**

## 2. The subject the blind session will derive, stated from scratch

> **How the analysis should be divided into layers — what question each layer answers, on what
> evidence, what it publishes, and what may cross between them.**

A harmonic analysis of a notated score has to answer several different questions — which notes are
sounding, where one stretch of unchanging sound ends, what tonality is in force, which chord is
sounding, what role that chord plays, and how the answers are assembled for a reader. Dividing the
work is a design act: which of those questions belong together because they cannot be answered
apart, what evidence each of them actually needs, and what one part of the analysis is allowed to
assume about what reaches it from another. That division is what the blind session is being asked to
write.

## 3. What this family protects — and the one thing it is NOT

**There is NO ORACLE for this subject, and the field on the artifact says so rather than naming a
span.** The pilot's first subject was held out against a ruled answer, and its family existed so
that the answer could not reach the session by a side route. **This subject is not held out against
anything.** No ruling states the decomposition the framework document is to arrive at; there is no
answer to protect.

What the family exists to keep out is the ruled constraint, quoted verbatim from
`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §3.3:

> **NOT ALLOWED:** implementation-derived material as design input; evidence treated as the decision.

**That makes this subject harder than the first, not easier, and the reason is worth stating.** The
first subject's leak surface was narrow — a handful of entries about where a boundary falls. Here
the thing that must not reach the session is *the shape of the analysis itself*, and much of what
this project has written down is about exactly that shape. The two lists below are the measure of
it.

**One standing exclusion is ruled and is not a preference.** An entry whose home is
`cowork_joint_estimator_factorization.md` — the user-ratified ten-factor model — is **NEVER** a
candidate for withholding, because Ruling 2 of `cowork_rulings_2026_08_21_successor_plan_sitting.md`
admits that document to a blind session **by name**, as design intent rather than a description of
built software.

## 4. How LIST ONE was derived, and the bound the derivation carries

The list was not hand-picked. `tools/audit/gen_derivation_boot_pack.py` walks the `DESIGN-INTENT`
class of the ratified rulings sort and returns as a **candidate** every entry meeting **any** of:

- its `group` is **A** (the estimator architecture), **C** (cross-cutting analysis contracts), **D**,
  **E**, **F**, **G**, **H** (the layers) or **I** (module boundaries and code structure);
- any of `title`, `verbatim`, `plain` or `patterns` contains one of the keywords: *layer, layers,
  decomposition, charter, boundary contract, publishes, consumes, one path per concern, span
  typology, the record, seam, adapter, pipeline, stage, upstream, downstream, note model, slicer,
  slice, key and mode, chord identity, function layer, grouping layer, derived view, emission,
  decode, joint estimator, state space, factor, forward-only, backward edge, re-derive, recompute*.

The criterion is the writing side's, given in full by the dispatch and imported into the generator's
authored table rather than re-decided here. **It names no oracle span and no home document**, this
subject having no oracle.

**★ THE BOUND ON THE CRITERION, STATED BECAUSE A PATTERN THAT DOES NOT SAY WHAT IT MISSES READS AS
COMPLETE.** *The criterion is a pattern match over the design-intent register's own text.* **ITS
REACH IS UNMEASURED** *(#19): an entry that bears on this subject in words none of the criterion's
terms carry would not appear, and an empty match would be evidence of nothing. The bound is stated
rather than a detection measurement being owed, under* **D-673**, *and that clause's test is met:*
**NO ANALYSIS DECISION CONSUMES THIS ENUMERATION** *— the user rules it at this file.*

**The match also fires inside longer words.** The generator publishes each keyword hit with its own
surrounding text so that a reader can see why the pattern fired; that per-candidate context is not
reproduced in the table below, because the table would become unreadable. It is obtained by re-running
the derivation — see the provenance at the foot, which names the producing command.

**The standing exclusion was applied AFTER the criterion, outside the tool, and it removed ONE
entry.** The criterion's own machinery carries no exclusion term, and adding one would be a change
to that machinery, which this batch is barred from making. So the tool's candidate list was taken as
it fell and the exclusion applied to it by hand, visibly: **D-565** — *Exact score ties in the decode
are real and are broken by a declared TOTAL ORDER on paths* — is the only entry of the whole
design-intent class homed in `cowork_joint_estimator_factorization.md`, it did reach the candidate
list, and it is **removed**. It is named here rather than silently dropped, so the step is checkable.

## 5. The verdict the user is asked to give, one per candidate

The generator's closed vocabulary, and its own definitions:

- **IN** — a deriving session that read this entry would know, in whole or in part, how this project
  has decided to divide the analysis. **An `IN` verdict is what withholds the entry from the pack.**
- **OUT** — the entry bears on something else, and reading it tells the session nothing about that
  division.
- **UNPLACED** — the entry's own text does not settle it.

**NO VERDICT IS PROPOSED HERE, FOR ANY CANDIDATE.** The pilot's first subject was graded by the
executing side and the grades were then ruled; this batch was ordered not to do that, and it has not.
Every row below carries the entry's identifier, its title, and the criterion limb that returned it —
and nothing more.

---

## LIST ONE — the RATIFIED-DESIGN-INTENT candidates

*Every entry the criterion returned, less the one the standing exclusion removes. In identifier
order. **The `group` column of the criterion and the keywords matched are given so that a reader can
see why each row is here**; a row reached by a keyword alone is not thereby weaker than one reached
by its group, and neither is a verdict.*

| ID | Title | Returned by |
|---|---|---|
| D-001 | Key, mode and chord are inferred by ONE joint decode | group **A**; keyword `decode`, `factor`, `joint estimator` |
| D-002 | The fitted tables and weights are compiled into the binary verbatim | group **A** |
| D-003 | Inference is preset-independent; presets are presentation concerns | group **A** |
| D-005 | The joint estimator is the production inference layer on the batch and corpus surface | group **A**; keyword `layer`, `joint estimator`, `pipeline` |
| D-010 | The switch - the record path is the production in-app notation analysis | keyword `the record`, `joint estimator` |
| D-022 | The founding principle - analyse at the finest grain, coarser views are derived | group **C**; keyword `derived view`, `slice` |
| D-023 | The atomic analysis unit is the constant-sonority slice, never the metric beat | group **C**; keyword `slice` |
| D-024 | The fact layers are style-agnostic; style lives only in calibration | group **C**; keyword `layer`, `layers` |
| D-025 | Forward-only, with two scoped escapes | group **C**; keyword `forward-only`, `stage`, `recompute` |
| D-026 | The global joint-lattice decode was measured inert (2026-06-29) | group **C**; keyword `decode`, `layer` |
| D-027 | Every layer emits ranked candidates plus a confidence, never a forced point estimate | group **C**; keyword `layer`, `stage` |
| D-028 | The span typology - every layer names the span it operates on; bare 'region' is banned | group **C**; keyword `layer`, `span typology` |
| D-029 | The verifiability contract | group **C** |
| D-030 | Bounded context - cost scales with the working span, not the whole score | group **C**; keyword `layer` |
| D-031 | Whole-score analysis is the degenerate case, not the design | group **C** |
| D-032 | Every confidence crossing a layer boundary is in 0..1, class-declared, with its decision named | group **C**; keyword `layer`, `stage` |
| D-033 | Each layer owns one evidence-source-times-question contribution and uses all of L1's information | group **C**; keyword `layer`, `stage` |
| D-034 | A new layer or axis is admitted only through three co-equal gates | group **C**; keyword `layer`, `stage` |
| D-035 | The effort setting - every cost-driving choice is a setting, never a hardcoded constant | group **C**; keyword `stage` |
| D-057 | The priority of evidence - actual sounding notes are the strongest evidence | group **F** |
| D-072 | The dependency rule - the analysis library knows nothing about the score format | group **I**; keyword `layer` |
| D-095 | The dual path during the joint-estimator build is a declared, bounded, pre-ratified migration state | group **A**; keyword `stage` |
| D-096 | Fitted values are fit once against ground truth, never per-case tuned | group **A**; keyword `factor` |
| D-099 | Negative evidence is information - a ruled-out possibility is carried, not dropped | group **C**; keyword `layer`, `publishes` |
| D-100 | Every derived fact is published exactly once, on the producing layer's output surface | group **C**; keyword `layer`, `re-derive`, `publishes`, `stage` |
| D-114 | The decoder commits its best path; there is no abstention on the key axis | group **A**; keyword `decode`, `joint estimator` |
| D-170 | #6 - total unification: one path per concern | keyword `one path per concern` |
| D-171 | #7 - a layer is enhanced only with what belongs to it | keyword `layer`, `layers`, `stage` |
| D-172 | #8 - no inference-problem-driven coding until the refactoring, the architectural design and the algorithmic completion are done | keyword `factor`, `layer` |
| D-190 | The decision-neutrality corollary - what exists carries no weight in choosing a design | keyword `one path per concern`, `downstream` |
| D-207 | The pedal-point class is defined voice-independently, superseding the bass-only fact | group **G** |
| D-229 | The MuseScore-dependency rule - one general rule for what our code may depend on | group **I**; keyword `layer`, `the record`, `upstream`, `note model` |
| D-260 | Analysis output covers exactly the selection; everything loaded beyond it is evidence, never a result | group **C** |
| D-261 | A layer never guesses how much context it needs - the amount is discovered by convergence | group **C**; keyword `layer` |
| D-262 | The extension increment is chosen by the requesting layer, not by the layer that supplies the notes | group **C**; keyword `layer`, `slice` |
| D-264 | Extension is an optimisation of load-more-then-rerun: any sequence of extensions equals one fresh run | group **C**; keyword `slice` |
| D-265 | Asking a lower layer for more notes is a data-supply call, not a backward inference edge | group **C**; keyword `layer`, `forward-only`, `layers` |
| D-267 | There are exactly two admissible confidence classes, and no layer may claim a calibrated probability until one is fitted | group **C**; keyword `layer`, `stage` |
| D-268 | A confidence attaches to a named decision, is compared only within its class and a declared frame, and keeps its identity downstream | group **C**; keyword `downstream`, `layer`, `slice` |
| D-270 | The held-out evaluation protocol - five-fold cross-validation grouped by ground-truth analysis file | group **A** |
| D-271 | The capacity budget - a cell keeps its own estimate only above a stated count, and free parameters are bounded against the training tokens | group **A**; keyword `stage`, `factor` |
| D-275 | Every published record carries its own instrument provenance; a provenance-less analysis cannot exist | keyword `the record`, `decode` |
| D-276 | Modal colour is published as un-rounded per-degree counts; no mode label is inferred or published anywhere | keyword `layer`, `publishes`, `the record` |
| D-278 | The joint key-and-chord step is SHELVED - measured not to pay | group **C**; keyword `stage`, `decode`, `factor`, `joint estimator` |
| D-279 | The Stage-3 entry gate - seven conditions before any engagement wiring reaches production | keyword `stage`, `layer` |
| D-280 | Gates read structured fields only - never a chord symbol string and never a Roman numeral | group **G**; keyword `layer` |
| D-282 | Meta-finding: the oracle/tier metric, never a bare proxy - superseded by the robust-unit stop and the two-tier policy | group **C** |
| D-283 | Meta-finding: never learn keys, the lever is keychain structure - superseded by the joint estimator and the forms-from-theory rule | group **A**; keyword `joint estimator`, `factor` |
| D-284 | Meta-finding: selection/competition is saturated, stop adding re-ranking gates - superseded by the gates doctrine and the adoption | group **G**; keyword `joint estimator` |
| D-285 | Meta-finding: embellishment is chord-first, never a richer vocabulary - absorbed by the emission design and the ornament-label increment | group **A**; keyword `emission`, `re-derive`, `factor` |
| D-286 | Whole-score interactive analysis was SHELVED WITH EVIDENCE; the bounded window is the ratified reading | group **C**; keyword `stage` |
| D-288 | Beam widening is SHELVED - a wider search cannot fix the failure class it was proposed for | group **C** |
| D-289 | Meta-principle: precision lives in the evidence and the functional labelling, not in the search | group **C**; keyword `stage`, `emission`, `decode` |
| D-291 | The tonicization labeller is NOT wired - wiring it would raise the reported agreement while hiding a real key error | group **H**; keyword `layer`, `the record` |
| D-292 | The fitting-pool licence constraint - values that ship are fitted only on freely-licensed music | keyword `the record` |
| D-293 | Fitted values are fitted per IDIOM, never for a user preset; presets are regression surfaces and delivery carriers | group **C** |
| D-296 | READING MuseScore's engraving code is allowed from anywhere we may edit; only EDITING the notation and engraving code is off limits | group **I** |
| D-306 | The key layer's backward re-reading stays switched off in the shipped configuration | group **F**; keyword `layer` |
| D-313 | A confidence map is monotone or it is not fitted — a non-monotone curve is an upstream finding, not a mapping target | group **C**; keyword `upstream`, `layer` |
| D-317 | The backward-walk boundary change is a dead end — do not retry it | group **G** |
| D-318 | A short-region external merger is a dead end — do not retry it | group **G** |
| D-319 | Re-analysing the merged aggregate is a dead end — no tone-aggregation approach fixes the arpeggio root failure | group **G** |
| D-320 | The absent-root guard is REVERTED and must not be retried — 'absent root means wrong reading' is false corpus-wide | group **G**; keyword `the record` |
| D-321 | Winner selection compares candidate scores exactly, with no epsilon anywhere in the ranking | group **G**; keyword `layer` |
| D-322 | Any change to optimization flags or to the order of the scoring arithmetic requires a full corpus A/B on both presets | group **G**; keyword `factor` |
| D-323 | Asking whether a pitch belongs to the key is a question about the collection, never about the tonic — the tonic-anchored form must not return | group **F** |
| D-324 | Retirement of a post-scoring rule is global — a rule still doing work on any one preset is retained for all | group **G** |
| D-325 | A correction rule that changes a committed chord's identity is retired or folded in BEFORE the search is widened past it | group **G**; keyword `decode` |
| D-326 | The chord-path search emits the whole path with every stretch's alternatives and margins, not the committed reading alone | group **G**; keyword `layer`, `consumes`, `function layer`, `decode` |
| D-327 | The root-continuity guard reads the reconstructed inversion credit, superseding the designed sounding-third test | group **G**; keyword `layer`, `the record`, `pipeline` |
| D-329 | Completeness of the candidate list is the priority — a chord never listed can never be chosen | group **G**; keyword `slice`, `layer`, `downstream`, `decode`, `joint estimator` |
| D-330 | Never a pooled recompute — the chord is never re-derived from several stretches' notes thrown together | group **G**; keyword `re-derive`, `recompute`, `layer`, `note model`, `slice` |
| D-331 | Every chord decision carries its ranked alternatives and its confidence — committed, inherited, and abstained alike, never pruned | group **G**; keyword `layer` |
| D-335 | The function layer outputs the Roman numeral; the tonic/subdominant/dominant summary is a derived read-out, never a stored output | group **H**; keyword `layer`, `function layer` |
| D-336 | Cadence detection is key-agnostic and votes for the key rather than reading one | group **H** |
| D-337 | A lean toward another degree is a tonicization by default; a key change needs a confirming cadence AND persistence, expressed as a change-cost | group **H**; keyword `layer` |
| D-338 | The function layer selects among the chord layer's carried readings and never re-derives a chord from the notes | group **H**; keyword `layer`, `function layer`, `re-derive`, `slice` |
| D-339 | A confident earlier decision can be overturned by decisive later evidence, through ONE confidence-weighted forward-recompute mechanism — architecture-wide | group **C**; keyword `recompute`, `layer`, `layers`, `forward-only`, `stage` |
| D-341 | The licensed root-motion set is completed by theory — the ascending fifth, the descending second and the diatonic diminished fifth are added | group **H**; keyword `slice` |
| D-343 | The key/mode layer owns the candidate space and the note-evidence model outright; the residual is SELECTED from its carried alternatives, never re-scored | group **F**; keyword `layer`, `seam`, `stage` |
| D-344 | A scale outside the twenty-one recognized modes is reported as the best-fitting recognized mode, never as the unrecognized scale | group **F**; keyword `layer` |
| D-345 | The style preset first enters the analysis at the key/mode layer, as a deliberately weak prior over the modes that the note evidence overrides | group **F**; keyword `layer`, `layers` |
| D-347 | The cost of changing tonality is cheap-to-stay plus a term growing with tonal distance plus a large extra penalty on the relative major/minor switch | group **F** |
| D-348 | Tonal distance in the change cost is circle-of-fifths distance — not semitone distance, not differing scale tones — and brief-versus-sustained has no duration threshold at all | group **F**; keyword `slice` |
| D-349 | The key/mode confidence compares whole readings — the winning run against the best run forced to a different tonality there — not the top two candidates at that stretch | group **F**; keyword `slice` |
| D-351 | The key/mode search is its own decoder; the chord decoder is not reused for it | group **F**; keyword `decode` |
| D-352 | The key/mode grading bar splits the cases first: agreement where the published analyses are unanimous, any recorded reading (or an uncertain mark) where they are not | group **F**; keyword `layer`, `the record` |
| D-353 | The key/mode layer is graded on two goals kept apart — agreement where the notes decide, and whether its own uncertainty lands on the genuinely ambiguous cases | group **F**; keyword `layer`, `slice` |
| D-376 | The joint key-and-chord step was designed as a BOUNDED COUPLING over the two existing decoders, and the unified single-state alternative was REJECTED — the option later adopted as the production architecture | group **A**; keyword `decode`, `layer`, `layers`, `pipeline`, `slice`, `factor`, `forward-only`, `recompute`, `stage` |
| D-380 | The carry's meaningful axis is DISTINCT ROOTS, and every above-threshold root is carried at graded confidence — a carry of winner-plus-one discards the third root on about a quarter of slices | group **G**; keyword `slice` |
| D-381 | The carry must cap on DISTINCT ROOTS, not on voicings — the existing voicing-keyed cap gives no structural guarantee that a third root survives | group **G**; keyword `layer`, `decode` |
| D-382 | The function layer selects by JOINT CONSISTENCY across tonality, root, inversion and bass — not by maximizing any one score — and every ambiguity kind reasons over the full carried distribution | group **H**; keyword `layer`, `function layer`, `slice` |
| D-383 | Bass, spelling and tonality-consistency DECIDE; a licensed progression is only a tie-break among already-consistent readings and may never override a committed root | group **H**; keyword `slice` |
| D-384 | Re-ranking the tonality under chord evidence is a SEPARATE step, never part of the function layer's selection — the function layer reasons inside a tonality already fixed | group **H**; keyword `layer`, `function layer`, `downstream`, `stage`, `upstream` |
| D-385 | Pedal-point detection's home is DECIDED: a reader over the chord layer's carry that annotates a carried reading — never a second analysis that overwrites the winner | group **G**; keyword `layer`, `chord identity`, `decode` |
| D-386 | No fourth hand-rolled scan for the best different-root alternative — the pedal reader consumes the carry's own ranking, or the one unified primitive | group **G**; keyword `consumes`, `stage`, `slice`, `decode`, `layer` |
| D-387 | A contradiction between the function context and a committed chord is surfaced on the ONE open mark, enriched with a reason — not on a second parallel flag, and not by overloading the plain undecided mark | group **H**; keyword `slice`, `stage` |
| D-388 | Texture is read primarily from HOW VOICES MOVE TOGETHER, not from how far each line leaps — the interval-led alternative was measured weaker and partly an encoding artifact | group **H** |
| D-389 | A notated voice is a FACT and an inferred perceptual line is a JUDGMENT — the two are separate types and are never conflated | group **H** |
| D-390 | The first version classifies the WHOLE selection as one texture — classifying within a piece is deferred behind a measurement, because the evidence is per-piece | group **H** |
| D-391 | Reads between the two analysis dimensions are admissible only where the combined dependency graph stays acyclic — harmonic layers may take voice-leading FACTS freely; a voice-leading component may take a committed harmonic result only if nothing that result depends on consumes it back | group **H**; keyword `layer`, `layers`, `consumes`, `stage` |
| D-392 | The later voice-leading components are CLAIMS WITH OWNERS, not builds — each clears its own design document and its own evidence before any instruction exists | group **H**; keyword `stage` |
| D-393 | Every voice-leading inference publishes the committed answer AND the FULL ranked list of all alternatives with their weights — nothing below the top is discarded | group **H**; keyword `publishes`, `stage`, `downstream` |
| D-394 | Reducing a chord-bearing voice to one line is a DECLARED parameter of the request, uniform across sources — never silent, never chosen per source; the first version offers exactly one rule | group **H** |
| D-395 | Three named floors govern abstention, and the FIT floor is the one that lets a passage resembling NO known texture decline rather than be forced to its nearest | group **H**; keyword `stage` |
| D-396 | The voice-leading dimension covers NOTATED music only, and its style coordinate is UNDEFINED — not zero — for sources that carry no voices | group **H** |
| D-397 | The homeless analysis objects are ASSIGNED to named owners on the voice-leading dimension — the stock patterns, the melodic phrase, chord voicing, and part-writing advice — as claims, discharged only at each owner's own ratified design | group **H** |
| D-398 | Parallel motion is judged SEMITONE-EXACT, not by generic diatonic size — a same-direction move whose semitone interval changes counts as similar motion | group **H** |
| D-400 | A PER-VOICE span kind is admitted to the span typology — melodic phrases overlap across voices by construction and tile only within one voice | group **H**; keyword `span typology` |
| D-406 | The catalog owns the NAMED progressions and substitutions; the pairwise licensing grammar is owned by the function layer — the two are never derived from each other | keyword `layer`, `function layer` |
| D-419 | Until the recognition consumer is built, the function layer does not touch the harmonic vocabulary | group **H**; keyword `layer`, `function layer`, `grouping layer` |
| D-421 | Idiom re-discovery rides every corpus wave, on research material only, and a changed cluster set is its own ratification event | keyword `the record`, `pipeline` |
| D-423 | The gate-retirement stage is the only sanctioned way the post-scoring gates change, and three do-not rules hold through every stage | group **G**; keyword `stage`, `layer` |
| D-425 | The uncertainty surface's contract IS the full posterior; the local slice is the first delivered step, and the completion is a named step, never an indefinite upgrade | keyword `slice`, `publishes` |
| D-440 | The language-model integration is purpose-built and does not wait for the plugin-API reform | keyword `layer`, `layers` |
| D-444 | The core access layer is a facade over interfaces that already exist, not a redesign | keyword `layer` |
| D-449 | Factor granularity is fixed: the bass factor is evaluated per event, the missing-tone penalty per event of segment length, the emission per tone, and the boundary-family factors per boundary | group **A**; keyword `emission`, `factor` |
| D-450 | The key-signature and declared-mode prior conditions the INITIAL key state only, re-entering only at a notated signature change | group **A** |
| D-451 | A desk simulation's table values are provisional, enter no fit, and a verdict that would flip inside a provisional value's plausible range is reported as a near-tie, never as a win | group **A** |
| D-452 | Every desk-simulation trace runs at identity weights — the ratified ablation baseline — so the trace tests the structure and the tables, not the weighting | group **A** |
| D-453 | The desk simulation's verdict: the ratified factorization passes nine of ten traces and no finding reopens the structure | group **A**; keyword `factor`, `decode` |
| D-454 | The grouping layer detects nothing — it assembles what earlier layers decided, and pressure to add detection means the work belongs elsewhere | group **H**; keyword `layer`, `layers`, `grouping layer`, `stage` |
| D-455 | A cadence away from a grouping boundary is surfaced as internal, never snapped to the nearest boundary and never discarded | group **H**; keyword `upstream` |
| D-456 | Sections, periods and sentences are out of the grouping layer's core for PROPORTIONALITY — not disqualified for lacking an oracle | group **H**; keyword `layer`, `grouping layer`, `stage` |
| D-457 | A group truncated by the selection edge is marked as truncated, and a group that runs off the edge unclosed carries an extension cue the grouping layer only surfaces | group **H**; keyword `layer`, `grouping layer`, `layers`, `pipeline`, `forward-only`, `stage` |
| D-459 | The key-area confidence is a declared margin-class boundary confidence, and its input is the declared key confidence — never the grading diagnostics' sigmoid | group **H**; keyword `layer`, `publishes`, `emission`, `stage` |
| D-460 | A group counts as fully resolved exactly when no unit in it carries an unresolved mark — no confidence threshold enters the test | group **H**; keyword `layer`, `stage` |
| D-461 | The grouping layer is an explainability layer, not an accuracy requirement, and is deliberately kept thin | group **H**; keyword `layer`, `grouping layer`, `stage` |
| D-462 | Cadence validation is scoped to LOCATION; cadence TYPE is only partially attributable and is never a clean gate | group **H** |
| D-463 | The temporal signals sitting in the vertical scorer are left where they are, and the gate that depends on them must move with them | group **G**; keyword `layer` |
| D-464 | No further progression-level signal may be added to the single-step look-around structure; it goes in the progression context instead | group **G** |
| D-465 | The policy for judging a proposed post-scoring gate: another bias correction gets the bias fixed first, a structural condition is sound, and a cascade means the missing thing is functional context | group **G** |
| D-466 | Forward-only is a strong DEFAULT, not dogma — a backward edge is admissible only as a deliberate, surfaced, measured, documented exception | group **C**; keyword `forward-only`, `backward edge`, `stage` |
| D-467 | A rebuilt or re-tuned chord scoring must not rely on the held-note repetition bonus the faithful note model removed | group **G**; keyword `note model`, `layer`, `upstream` |
| D-469 | The tick-local path is left OUTSIDE the unified pipeline by design — its point-in-time semantics would be distorted by one shared interface | group **I**; keyword `pipeline` |
| D-470 | The temporal-context extension fields are recorded during the pipeline's own analysis pass; no consumer re-runs the chord analysis to rebuild them | group **I**; keyword `pipeline`, `the record`, `re-derive` |
| D-472 | Key areas are grouped by a smoothing pass over regions whose key sequence has already been smoothed, and a region that disagrees without clearing the confidence test keeps its own key while being grouped into the enclosing area | group **H**; keyword `layer`, `layers` |
| D-474 | No published study reports per-axis inter-annotator agreement for Roman-numeral analysis of Baroque/classical symbolic music — the ground-truth ceiling principle #21 demands is unmeasured by the entire field | group **C** |
| D-475 | The BCMH chorale annotations are NOT established as an instrument: one named annotator with no independent second annotation, the annotations sit on a reduction, and they reached the repository through a machine translation | group **C** |
| D-476 | The phrase-boundary primitive is owned by the notation-derived view layer — not by the note model, and not by the function layer that consumes it | group **H**; keyword `layer`, `consumes`, `note model`, `function layer`, `derived view`, `stage` |
| D-477 | Phrase boundaries are read from the written surface alone — never from a resolved key, chord or cadence — and the boundaries this misses are accepted, not recovered here | group **H**; keyword `layer`, `consumes`, `downstream`, `function layer`, `stage` |
| D-478 | A phrase boundary is a peak in a continuous boundary-strength profile, not the OR of a few binary signals | group **H** |
| D-479 | The boundary cues run per eligible voice and aggregate to the texture, and BOTH the per-voice and the texture boundaries are published | group **H** |
| D-480 | The phrase-boundary primitive is NOT an accuracy requirement — a competitive reference engine does no phrase segmentation at all — so it is built right but kept proportionate | group **H**; keyword `pipeline` |
| D-481 | The notated markers are emitted as boundaries unconditionally; only the surface-cue strength is peak-picked | group **H** |
| D-482 | The two hand-synchronised copies of the fermata scan retire into one owned primitive, and that retirement changes no output | group **H** |
| D-484 | The phrase-boundary primitive is a derived view: it inherits the loaded span, requests no extension of its own, and publishes a per-profile max-normalised boundary confidence | group **H**; keyword `publishes`, `derived view`, `layer`, `recompute` |
| D-485 | Each picked boundary should carry which cue fired and at what scope; the picked set is scope-blind today and the refinement waits for the inference phase | group **H**; keyword `downstream` |
| D-490 | FALSIFIED: no threshold can make the fine-grain function override net-positive — the harm rate is flat against both quantities the threshold is built from | group **H** |
| D-491 | REFUTED: making the override's comparison vertically fair does not repair it — even where the alternative fits the notes at least as well, it is still about 71 % harmful | group **H**; keyword `layer` |
| D-492 | The recommended redesign is to demote the override to an annotation — carrying the earlier reading unchanged and surfacing the contradiction — floored by simply disabling it | group **H**; keyword `stage` |
| D-493 | Restricting the override to the genuinely-coupled key-and-chord minority is UN-COMPUTABLE, not merely unmeasured: its trigger is not computed anywhere and building it is the still-owed joint step | group **H**; keyword `the record`, `stage`, `decode` |
| D-494 | RATIFIED AMENDMENT A-4: the function layer must gain key-confirmation channels that do not require a cadence, plus an enharmonic-identity rule for key spans | group **F**; keyword `layer`, `function layer` |
| D-495 | RATIFIED AMENDMENT A-5: when the phrase-boundary profile is flat, cadence admission relaxes with vote-weight scaling instead of starving | group **H**; keyword `layer` |
| D-496 | RATIFIED AMENDMENT A-6: whether the pairwise progression grammar lives inside the harmonic vocabulary or stays a separate store is decided at the recognition-consumer build, explicitly | keyword `layer`, `function layer` |
| D-497 | RATIFIED AMENDMENT A-7: the empirically-unvalidated mark must be APPLIED to the Jazz preset constants and the unvalidated idioms, with the validation path named | group **C**; keyword `the record` |
| D-499 | RATIFIED AMENDMENT A-10: four documentation riders — a consolidated ownership page for the notation-derived views, the membership tie-breaker recorded as idiom-calibrated, and the producer-agnostic seam pinned as a design property | keyword `seam`, `derived view`, `layer` |
| D-500 | The user ratified CORPUS EXPANSION at the architecture review: gate-grade jazz ground truth, chromatic material of the Wagner class, and more non-Bach, non-Baroque annotation generally | group **C** |
| D-501 | A tool may read a written chord symbol ONLY as a comparison or ground-truth label — never as input that influences what the analyzer computes | group **G** |
| D-503 | The idiom mixture is DISCOVERED from the score and merely SEEDED by the user's preset, in three forward-only phases | keyword `forward-only` |
| D-504 | A recognised harmonic sequence is ALWAYS emitted as key evidence — the earlier gate that emitted it only where no cadence existed threw corroboration away | keyword `layer`, `stage` |
| D-505 | A harmonic sequence requires at least two transposed statements of the SAME recognised entry; a single internally-sequential entry emits none | keyword `stage`, `publishes` |
| D-507 | A catalog entry defined by its melodic or bass lines is recognised by its chord skeleton alone and carries a 'chords-only' mark, with its prior strength reduced | keyword `layer` |
| D-509 | Where the analysis already committed a chord, a recognised progression corrects it through the EXISTING override frame and may only SELECT an already-carried reading — no new comparison frame, and never a reading built from the notes | keyword `layer` |
| D-510 | The correct carry is the one that keeps the distinct alternative reading, not the one that appends a near-duplicate of the winner — chosen on the carry's purpose, not on which code is at HEAD | group **G**; keyword `layer` |
| D-511 | One promotion primitive with a present-first dedup guard replaces the two ad-hoc promotion idioms; the append branch fires only when the target is genuinely absent | group **G** |
| D-512 | Gate A becomes removable only once the unified promotion reproduces its carry byte-for-byte — that reproduction IS the retirement condition, not the winner-inertness that preceded it | group **G** |
| D-514 | A newly acquired annotation set whose works OVERLAP the regression corpus is RECORD-ONLY: it may not be wired to, compared against, or bulk-diffed with the gate corpus without a user ruling | keyword `the record` |
| D-521 | The general law of the circularity map: an abstract circle becomes acyclic in the concrete by one of four named conditions — and every alleged circle in this system fell to one of them | group **C**; keyword `recompute` |
| D-522 | Explaining an inference to the end user is a late-bound DISPLAY consumer of facts that already exist — not a new analysis | group **C** |
| D-524 | The joint state's mode axis is TWO modes — major and composite minor; modal and chromatic colour lives in the pitch emission, and the un-rounded reading is published | group **A**; keyword `emission`, `layer`, `decode`, `state space`, `factor` |
| D-525 | The fit is STAGED: the factor tables are counted from ground truth and frozen, and only a small vector of combination weights is fit discriminatively — with an all-weights-equal ablation arm that must be beaten | group **A**; keyword `stage`, `factor`, `layer`, `emission` |
| D-526 | The joint state's chord axis is SCALE-DEGREE-VALUED — a Roman numeral relative to the state's own tonic and mode — and the chord symbol is a DERIVED fact published once | group **A**; keyword `layer` |
| D-527 | There is NO live non-chord-tone cleaning stage: each tone is emitted by category inside the one decode, conditioned on chord-independent melodic and metric covariates, and ornament labels are derived AFTER it | group **A**; keyword `stage`, `decode`, `layer`, `upstream`, `chord identity`, `emission`, `factor` |
| D-528 | The key signature and declared mode enter as a WEAK FITTED SOFT PRIOR with no conditional gate anywhere — the probability calculus delivers 'consult it only when unsure', and the hard declared-mode wall is formally retired | group **A**; keyword `factor` |
| D-531 | The hand-built emission is CONFIRMED and the learned replacement is NOT triggered — retained as an explicit fallback with a concrete trigger, and scoped to one repertoire with a named re-check gate | group **C**; keyword `emission`, `layer`, `decomposition`, `slice` |
| D-532 | The chord-transition table gains one pooling level that groups a secondary dominant's continuations by their RELATION to its target — restoring from counts the one behaviour that defines the chord class | group **A**; keyword `layer` |
| D-533 | A continuation too rare to have its own stored probability is scored by dividing the row's leftover in PROPORTION to each chord's overall frequency — never evenly, and never as impossible | group **A**; keyword `decode` |
| D-534 | The penalty for a chord tone that never sounds is COUNTED per chord factor — root, third, fifth, seventh — replacing one invented blanket number; the per-factor asymmetry then comes free | group **A**; keyword `factor` |
| D-535 | The checking stage's verdict: the real counted tables overturn no desk-simulation verdict, but margins moved in both directions and one margin expectation was plainly wrong | group **A**; keyword `stage`, `recompute` |
| D-536 | The bass note and the chord are chosen TOGETHER — the winner is the (bass, root, template) triple — replacing the sequential commit-the-bass-then-score pipeline | group **G**; keyword `pipeline` |
| D-537 | The completeness bonus fires ONLY for a root-position reading whose three triad tones are all present — the guard that stops it from demoting genuine slash chords | group **G** |
| D-538 | A multi-signal scoring change lands one signal at a time, with the corpus check re-run after each step and any increase in errors a hard stop before the next | group **G** |
| D-545 | The uniform mechanical extractor for idiom discovery is the external library, stopping at the note-and-slice front — OUR OWN key/chord/function inference must NEVER touch the extraction | keyword `slice`, `slicer` |
| D-569 | Collecting, filtering and weighting are THREE separate responsibilities; the collection layer collects and annotates, and does nothing else | group **D**; keyword `layer`, `downstream` |
| D-571 | The declared-mode influence becomes a small additive hint, and SMALLNESS IS THE GATE — no separate confidence test is added | group **F** |
| D-572 | The hard post-hoc declared-mode promotion is REMOVED OUTRIGHT rather than kept in a gated form | group **F** |
| D-575 | The Baroque partial-signature convention is handled by DETECTING it and reinterpreting the signature one step, not by widening the candidate family for every score | group **F**; keyword `joint estimator` |
| D-576 | The corpus root-agreement measurement UNDERSTATES the real-world quality impact of a wrong key, because root and bass are largely key-independent | group **C** |
| D-580 | Two of the twelve post-scoring gates are purely-local vertical refinements and MUST survive the dissolution; the other ten dissolve into the competition | group **G**; keyword `pipeline` |
| D-584 | The perfect/imperfect cadence call is made on the BASS-DERIVED inversion; the soprano arrival degree is demoted to a soft optional nudge and the tool never attempts melody identification | keyword `layer` |
| D-587 | A user-facing preset presents as a familiar genre-era label plus exemplars the user knows — never as an idiom name or an obscure exemplar; genre names are LABELS over mixtures, never axes | group **F** |
| D-588 | Preset coverage beyond the analysed corpora is three tiers with NO bare guessing — measured, editorially declared with a stated theory rationale, or self-correcting by detection | group **F** |
| D-589 | Every idiom mixture is selectable and the discovered cloud is the EVIDENCE MAP, not the boundary — each chosen point carries its evidence status | group **F** |
| D-590 | The score's own metadata is the PRIMARY home of that score's idiom mixture, and a user-set mixture is never silently overwritten by re-detection | group **F** |
| D-591 | The licence split for the style system: the ANCHORS are the shipped licence-constrained fitted parameters, and the mixture weights are free user configuration | group **F** |
| D-598 | The style taxonomy and the per-style weights are ONE data-derived object; VALIDATION is a separate third thing that needs annotated scores and is not delivered by the clustering | group **F** |
| D-600 | The quality-overwrite information-loss violation is TOLERATED until the gate-dissolution step and stays VISIBLE in the open-items register — tolerated is not forgotten | group **C**; keyword `layer`, `stage` |
| D-601 | Before any constant that would make two differently-scaled confidences comparable is fitted, the premise that a fitted constant CAN do so must itself pass a premise ledger and a desk simulation | group **C**; keyword `factor` |
| D-605 | The local-key hypothesis derives from key-agnostic signals ONLY and never from the key-area grouping, which is a post-grouping of the resolved key — a hard design rule, not a preference | group **E**; keyword `downstream` |
| D-613 | Ground truth for IMPLIED polyphony is confirmed ABSENT — do not re-search it | keyword `the record` |
| D-616 | A global tonic anchor enters key scoring at RESOLVER/SECTION scope — never as one more local term inside the window scorer, which is what re-enters the coupling that defeated the local levers | group **F**; keyword `layer`, `decode` |
| D-622 | The reach-back convergence PROXY was measured FALSE and dropped — the as-built tracks the leading-edge key itself and stops when it stops changing | group **F** |
| D-623 | A selection-aware capability is a PARAMETER on the one orchestrator, never a sibling — the capability must not duplicate the orchestration | group **I**; keyword `seam`, `slice`, `decode`, `note model` |
| D-625 | Spelling presence is tested with the validity predicate, never with a non-negative test — the flat side of the line of fifths is negative and a non-negative guard silently drops it | group **D**; keyword `layer` |
| D-629 | The resolver of carried uncertain readings IS the function layer itself — there is no distinct gated box between the note layers and it | group **H**; keyword `layer`, `layers`, `function layer`, `stage` |
| D-656 | The crediting rule is NOT amended to count a tonicization label as agreeing with the annotator's modulated numeral; only a diagnostic partial-sub-split is defensible | group **C**; keyword `layer`, `function layer` |
| D-665 | What a voice/stream label set actually MEASURES is said at intake — the labels obtainable today come from engraved notation, not from a listener's judgment | keyword `the record` |

**One entry the criterion returned is NOT in the table above, and it is named rather than dropped:**
**D-565** — *Exact score ties in the decode are real and are broken by a declared TOTAL ORDER on
paths* — removed by the standing exclusion of §3, its home being
`cowork_joint_estimator_factorization.md`. It is the only entry of the design-intent class homed
there.

---

## LIST TWO — the MEMBER-(2) PASSAGE candidates

*Member (2) of the boot pack is `CLAUDE.md`. The record carries two occasions on which that member
leaked the held-out answer for the first pilot subject, and **both lay outside the leak check's
scope, which is members (5) and (6)** — so no string test would ever have caught them. For THIS
subject the answer is the decomposition itself, and `CLAUDE.md` is a document about exactly that.
This list is the enumeration the dispatch ordered. **Nothing here is cut.***

**★ FIRST, A CORRECTION OF A PREMISE THE DISPATCH AND THE CURRENT HANDOVER BLOCK BOTH STATE, BECAUSE
IT DECIDES HOW MUCH OF `CLAUDE.md` THIS LIST HAS TO COVER.** Both say member (2) is *`CLAUDE.md`
rendered whole*. **It is not.** The generator's own authored member table takes **TWO SPANS ONLY**:
from the `## Guiding principles` heading down to the end of the paragraph opening `**Delegation
pointer`, and from the `## Conventions` heading to the end of the file. Its own docstring says so in
terms. **Everything between those two spans — the open-items register section, the decisions
register section, the project context, the build and test commands, the whole gate-threshold and
preset policy, the scoring-model section, the score corpora, the local patches and the VS Code rules
— is NOT in the pack at all.** That matters here more than it did for the first subject, because the
gate-policy section is where `CLAUDE.md` names the numbered layers, the record arm and the legacy
arm, and the segmentation layer, by name and repeatedly. **None of it reaches a deriving session.**

*Why the correction is stated rather than quietly worked around:* a reader of this list who believed
the wider premise would take its shortness for thoroughness, and a later ruling to widen member (2)
would silently bring a great deal of implementation description into the pack.

### The candidates INSIDE member (2)

*Each row gives the anchor text by which the passage is located — never a line number — the limb of
the dispatch's signature that it matches, and what it discloses. **No verdict is proposed.***

| # | Where, by its own anchor text | Limb matched | What a deriving session would learn from it |
|---|---|---|---|
| **P1** | Span 1 — `7. **Adhere to layers.**` | what a layer is responsible for | That the analysis IS divided into layers, that each layer owns particular algorithms and methods, and that the remedy for a misfit is a layer redesign rather than a cross-layer patch. It states the layered shape as settled without saying what the layers are. |
| **P2** | Span 1 — `8. **No inference-problem-driven coding until the refactoring` | what a layer is responsible for | *"every method and algorithm implemented in its correct layer, the architecture designed"* — the same disclosure as P1, that a correct-layer assignment exists for every method. |
| **P3** | Span 1 — `12. **No information loss.**` | a named layer's output | That a ruled-out possibility is **carried at low confidence rather than dropped**, and that a collapse is admissible only where the collapsed value is recomputable — a statement about what one part of the analysis hands on to the next. |
| **P4** | Span 1 — `15. **Verify at objects/data on the full output surface` | a named layer's output | *"(winner **and** carry, not the winner alone)"* — that the output surface of a decision carries a committed answer **and** a carry of alternatives beside it. |
| **P5** | Span 1 — the corollary opening `*Fact-publication corollary to #6/#7/#12` | a named layer's output; what may cross between layers | **The densest boundary-contract statement in span 1.** *"every derived analytical fact is published exactly once, on the producing layer's output surface; consumers read, never re-derive"*; a fact nobody consumes is declared dormancy or waste; EVIDENCE-class facts are published broadly even with no named consumer; each published fact carries its establishment status on the surface and an unvalidated fact may not be put under load; publication is the in-memory surface while serialization stays selective. It answers, in advance, three of the questions the framework document exists to answer. |
| **P6** | Span 1 — `23. **End-state principles need lawful transitions.**` | the arrangement of the record and the two arms | That a parallel build with a declared retirement map is a first-class state here. It discloses the *pattern* without naming the two arms. |
| **P7** | Span 2 — inside `**NEVER WORK FROM MEMORY INSTEAD OF DOCUMENTED FACTS`, the clause opening `**Where the primary source is:**` | what the layers are | *"how a layer should work → that layer's section in `ARCHITECTURE.md`"* — that the analysis is decomposed into layers and that each has its own section in the one document this session must not open. |
| **P8** | Span 2 — inside the same bullet, the clause opening `**Founding instance:** on 2026-07-28 Cowork reasoned` and closing `which is the general case, not the exception.` | a ranking of evidence; where a boundary falls; a named layer's input; what the layers are | **The densest passage in member (2), and it matches four limbs.** It names a *Layer-2 specification*; it states that *slice identity IS the eligible sounding-note set with releases as boundaries*; and it states that *actual sounding notes* are ranked the **STRONGEST** evidence. **★ THIS IS THE PASSAGE ALREADY WITHHELD FOR THE `harmony-boundary` SUBJECT (passage one of that family, widened 2026-08-22). Its withholding is scoped to that subject: it is neither carried across to this one nor removed from that one.** |
| **P9** | Span 2 — inside `**EVERY DESIGN DECISION CARRIES ITS DEFENSE AT ITS HOME`, the sentence opening `Founding instances of the gap:` and closing `each recorded with no derivation.` | where a boundary or a segment falls; a named layer's input | It names, from its own words, *the decode segment cap's value (4)*, *the legacy 16-beats-back/8-forward window*, and *the boundary-tick-belongs-to-the-segment-it-starts convention*. **★ THIS IS THE SECOND PASSAGE ALREADY WITHHELD FOR `harmony-boundary` (ruled 2026-08-23), re-tested here on the same terms as P8 and likewise neither carried across nor removed.** |
| **P10** | Span 2 — the bullet opening `**CANDIDATE ADMISSION IS COMPLETION, NOT REFINEMENT` | a named layer's input | That there is a *joint decoder*, that a rule decides *which chord classes it will even consider*, and that the rule lives in *the joint estimator's standing rules* of the specification this session must not open. |
| **P11** | Span 2 — the bullet opening `**ONE FIX IS DESIGNED ONCE OVER THE WHOLE ENUMERATED FAMILY` | what the layers are | Its worked instance names an *empty-decode cliff*, a sibling *at the opposite end of the density spectrum*, and an *emission-side twin* — disclosing that a decode and an emission are distinct components of the built arrangement. |
| **P12** | Span 2 — the bullet opening `**ISSUE-EXHAUSTION AND SPECIFICATION COMPLETION BEFORE ANY FIX DESIGN` | what a layer is responsible for | Its phase-3 clause — *"where each fix lives (its proper layer)"* — and the detail-specification phase's *"every decision in its owning specification"* both presuppose a per-layer decomposition with owned specifications. The weakest of the twelve, and listed rather than judged. |

### Considered against the signature and NOT listed, with the reason

Recorded so that the list's shortness is a result rather than an omission (**#12**).

- **Principle #6** (*one path per concern*) and the **decision-neutrality corollary**'s
  downstream-impact clause — both are about how a design is CHOSEN, not about what any layer is,
  consumes or publishes. Neither matches a limb.
- **Principle #17's desk-simulation clauses**, including the identity-weights rider — they describe
  how a mechanism is TRACED before it is built. The rider does disclose that the model is a
  weighted product of factors; the ten-factor model is admitted to a blind session by name (§3), so
  that disclosure is ruled admissible rather than a leak.
- **The MUSIC-THEORY WORDS bullet and its disambiguation convention** — a vocabulary rule. Its
  collision inventory names no layer, no boundary and no evidence rank.
- **The delegation pointer paragraph** — it delegates the ORDER OF WORK, not the decomposition.
- **The MAKE IT WORK FIRST bullet**, the **WORKING-TREE FILES** bullet, the **INVESTIGATE BY
  DEFAULT** bullet and the **self-check section** — process rules with no analysis content.

### What `CLAUDE.md` carries OUTSIDE member (2) — already out of the pack, listed so nobody re-derives it

*Stated at SECTION granularity with the passages named, and declared as such: this is not a
passage-level enumeration, because none of it can be withheld from a pack it is not in. It is here
so that a later proposal to widen member (2) meets the cost first.*

- **The gate-threshold and preset policy section** — by far the largest concentration, and it
  matches **all five** limbs: the numbered layers by name (*the change-point slicer (Layer 2)*, *the
  Layer-4 notated-spelling root pin*, *Architectural Layer 5*, *the Layer-3 decoder wiring*, *the
  key layer*, *the segmentation layer*); **the record arm and the legacy arm** named as the two paths
  that can produce the result, with the switch and its default; the two-tier class policy's root
  cause located at the chord layer; and the whole cross-layer-budget caveat, which apportions a
  measured residual across Layers 1–5.
- **The scoring-model section** — the conditional read of *the joint estimator's section of
  `ARCHITECTURE.md`*, and a second statement of the same founding instance P8 carries.
- **The open-items register and decisions register sections** — repeated reference to *the OWNING
  LAYER'S SPECIFICATION*, to per-layer and per-component design documents, and to *signed layer
  specifications*. Limb: what a layer is responsible for, weakly.
- **The build and test commands, score corpora, local patches and VS Code sections** — no limb match
  found; they name source files and procedures rather than the analysis's shape.

**★ THE BOUND ON THIS ENUMERATION, IN THE SAME TERMS AS §4's.** *This list is AUTHORED in its
signature — the five limbs are the dispatch's, and what counts as a span matching one of them is
this session's reading of them.* **ITS REACH IS UNMEASURED** *(#19): a passage that discloses the
decomposition in words none of the five limbs anticipate would not appear, and its absence from this
list is evidence of nothing. The bound is stated rather than a detection measurement being owed,
under* **D-673**, *and that clause's test is met:* **NO ANALYSIS DECISION CONSUMES THIS ENUMERATION**
*— the user rules it here.* The first subject's own record already makes the same concession in its
own words: the span was searched for the oracle's phrases and not for every paraphrase.

---

## LIST THREE — the LEAKS, and why this batch does not publish one for this subject

*The leak check is the standing per-entry test over members (5) and (6), and it is the whole of the
cutting for a subject whose withheld family is empty.*

**This batch did not measure a leak list for the `framework` subject, and the reason is the STOP of
§8: the generator raises before it reaches the leak check.** No number is asserted here, and none is
predicted.

**What IS on the record, and it is not the same thing.** The second pilot subject, `scoring-model`,
is rendered with an empty withheld family, and its leak entries are published whole at
`tools/audit/derivation_boot_pack.json` → `subjects.scoring-model.LEAKS.entries`. The leak check's
inputs for an empty family are the same for any subject — the string `ARCHITECTURE.md` and the
`docs/`- and `src/`-path test, and nothing subject-specific — so that list is the closest thing the
record holds to what this subject's would be. **That is an argument from the code's shape, not a
measurement of this subject, and it is not offered as one.** The measurement is owed at the render.

---

## 6. What this batch did, and what it deliberately did not

**Did:** authored the `framework` subject into the generator's authored tables with an **EMPTY**
withheld family and the criterion the dispatch fixes; ran the enumeration; applied the standing
exclusion after it; enumerated the member-(2) passage candidates; and wrote this file.

**Deliberately did not:**

- **Withhold anything.** No identity, no document, no passage. The family is empty and stays empty
  until the user rules.
- **Render a pack.** `tools/audit/derivation_boot_pack/` holds `harmony-boundary/` and
  `scoring-model/` and no third directory. Both were proven byte-unchanged, file by file.
- **Boot a session.** Nothing was derived, nothing compared, no placement test run.
- **Touch either existing subject.** Their manifest blocks, pack files, families and reading files
  are byte-unchanged.
- **Propose a verdict.** Not for any candidate, in either list.

## 7. What this file does NOT do

- **It rules nothing.** Every list above is a proposal to the user and nothing is applied.
- **It claims no completeness.** Both enumerations carry their bound, and each says what it would
  miss.
- **It moves no register entry and no status.** Proposing an entry as a withholding candidate says
  nothing whatever about that entry's standing.
- **It closes no open item.** [[OI-179]] stays OPEN and GATES.
- **It edits no governing document.** `CLAUDE.md`, `ARCHITECTURE.md`, `DECISIONS.md`,
  `DEFECT_TYPES.md`, `cowork_design_doc_template.md`, `cowork_audit_protocol.md` and the
  phase-definition surface are untouched by the act that produced it.
- **It does not finalise the brief.** `cowork_blind_session_brief_framework.md` stays a DRAFT; its
  §7 (P2) is answered only when the user rules the lists above and a later batch renders the pack.

## 8. ★ THE STOP — the tool shape this batch met, reported rather than worked around

The dispatch orders an enumeration with an empty withheld family and no render, and requires the
generator's manifest to gain a `framework` block whose candidate and leak counts are measured.
**Those two orders cannot both be met by the tool as it stands, and no wider change to it was
made.**

1. **The generator has no ENUMERATE-ONLY state.** Its fourth STOP fires when a derived candidate
   carries no authored verdict — *"a candidate cannot be graded by silence"* — so a non-empty
   criterion obliges an authored verdict for every candidate it returns. **The only verdict that
   withholds is `IN`.** So *enumerate the candidates, withhold nothing, and let the user grade them*
   is a state the tool cannot represent: it can withhold what a session has already graded, or it
   can search for nothing at all (the `scoring-model` shape, where the criterion is empty by
   ruling), and there is no third thing.
2. **The consequence, measured:** the run STOPs, **the manifest is not written**, and it therefore
   gains **no `framework` block**. The dispatch's assumption A3 fails. Nothing was authored to make
   the tool complete, because authoring a verdict for every candidate is exactly the grading this
   dispatch reserves to the user.
3. **The enumeration itself survives the STOP, which is why this file exists.** The STOP's own
   message lists every ungraded candidate with its identifier, title, verbatim, plain restatement
   and matching criterion — so the derivation ran in full and its result is above. What is missing
   is a durable artifact, not the answer.
4. **A SECOND SHAPE, WHICH WOULD HAVE PUT A FALSE STATEMENT INTO A GENERATED ARTIFACT HAD THE RUN
   COMPLETED.** Two places in the generator hardcode the FIRST subject's criterion while claiming to
   describe the running one: a `group` match is recorded with the fixed gloss *"Layer 2 — the
   slicer"*, which is false of a group-A, C, D, F, G, H or I match; and the manifest's
   candidate-criterion block renders five fixed bullets that describe the harmony-boundary
   criterion — *"its `group` is E — Layer 2, the slicer"*, *"its `home` is `ARCHITECTURE.md` at a
   line inside one of the oracle spans below"*, *"it is an identity the ruling names"* — none of
   which is this subject's criterion. **Correcting either is a change to the criterion machinery,
   which this batch is barred from making.** It is reported here so that a later render is not taken
   over it.
5. **The exclusion could not be expressed in the tool either.** The criterion has no exclusion term,
   so the standing exclusion of §3 was applied after the criterion and by hand, as the dispatch
   directs, and the one entry it removed is named in §LIST ONE rather than silently absent.

**The consequence for the guard set, stated plainly: `tools/audit/gen_derivation_boot_pack.py
--check` STOPS from the commit that carries this file, and it will go on STOPPING until the user
rules the lists above and a later batch writes the reviewed verdicts into the authored table.** That
is the shape the record already sanctions for an authored establishment — the standing check fails
deliberately across the authoring interval and clears only when the reviewed set is applied
(**D-655**). **The cost is stated because an accepted cost is not a discharged one: while it STOPS,
the check cannot report drift in the two EXISTING packs either**, so a change to them during the
interval would not be caught by it. Both were proven byte-identical to their committed blobs at the
tree this file was written on.

---

*Provenance: Claude Code, 2026-08-28, under `cc_instruction_framework_pack_preparation.md` Task 1.*
*LIST ONE is DERIVED — produced by `tools/audit/gen_derivation_boot_pack.py` from the `DESIGN-INTENT`
class of `tools/audit/rulings_sort_classification.json` and the entry text of
`tools/audit/decisions/backbone_decisions.json`, and reproducible by running that tool with the
`framework` subject authored, whose STOP enumerates the population with each candidate's own
verbatim, plain restatement and matched context. The standing exclusion was applied to that output
afterwards and the one entry it removed is named. LIST TWO is AUTHORED from `CLAUDE.md` read through
the file tools at the tree, its signature and its bound declared on its own face. **No verdict is
proposed in either list, and nothing is withheld.** TOWARDS the ultimate objective and TOWARDS the
guiding principles.*

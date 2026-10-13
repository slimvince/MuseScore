# L2 tail — the style and idiom family: decision surface, 2026-10-10

> **STATUS: DECISION SURFACE.** Cowork, 2026-10-10 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_thirty.md`. Delivered as text, nothing asked. The check
> runs in the next turn; the questions come after it, one per turn, each ruling recorded before the next. Nothing here is
> applied: the reading file's rows are re-marked by the application dispatch the L2 route ruling names as its step 2.

## 0. What this surface covers

**The rows.** The L2 comparison (`ratification_surfaces/cowork_comparison_l2_reading.md`) set the old project text
beside the derived L2 specification, sentence by sentence, and gave each old sentence a proposed filing label. 432
sentence-parts got no label (UNPLACED). After the family rulings of 2026-10-04 to 2026-10-10, 85 of them were cut into
this family, all about the style system: the five idioms, how they were discovered, the user-facing presets, and the
old fitter's model of how fitted numbers would vary with style. One more, Row 23.222 claim (ii), travels in because it
raises the same question, whether a preference reaches the analysis. The 86, by the document they come from:

- `ARCHITECTURE.md` §6, the style system (member 25): 33.
- `cowork_idiom_entry_mapping.md`, the table tagging each progression-catalog entry with its idioms (member 55): 19.
- `cowork_stage5_fitter_design.md`, the old fitter's design (member 9): 17.
- `cowork_progression_schema_dictionary.md`, the progression catalog (member 50): 8.
- Single rows: 1.27, 13.12(ii), 23.39, 23.222(ii), 43.39(ii), 46.57, 48.46(ii), 53.11, 57.13(ii).

33 + 19 + 17 + 8 + 9 = 86.

**What L2 is.** L2 is the part of the analysis that decides, together, the tonality at each moment, where each chord
begins and ends, which sounding notes belong to the chord, and what the chord is.

**The filing labels**, as the comparison defines them (its §5):

- **ADOPTED — carried:** a derived L2 statement already says it.
- **ADOPTED — proposed:** a proposal to add it to L2's text.
- **RELOCATED:** it belongs to another part of the framework (a "charter": L0, L1, L3, the second axis — voice
  leading, the uncertainty surface, the measurement of the analysis).
- **QUARANTINED:** it describes how the code works, and is kept with a question for the later audit.
- **HISTORICAL:** an event, a build state, a superseded plan or a status — not a rule.

**Two kinds of "weight" appear below, and they are different things.** An *idiom-mixture weight* says how much each of
the five idioms counts in a preset or in a piece (for example "70 % Chromatic-functional, 30 % Diatonic-functional").
An *L2 weight* is one of the fitted numbers in L2's candidate score. The old text sometimes calls both "weights".

## 1. What the record already says — read before anything is proposed

**The style system's own home is outside the framework.** `ARCHITECTURE.md` §6 is the style system. Its §6.7 is the
canonical style taxonomy, and by the user's maintained-object rule of 2026-08-07 it owns the discovery method too:
*"§6.7 owns both the canonical style taxonomy and the protocols and method that produce and re-produce it"*
(`cowork_owner_rulings_2026_08_07.md`, read this sitting). Its §6.8 is the user-facing preset layer, and its status line
reads: *"Status: RECORDED and DEFERRED product work … Nothing here is built at HEAD"* (read at the file this sitting).
The decisions homed there are LIVE in the register: D-131 (one shared taxonomy), D-421 and D-542 to D-545 (the
discovery protocol), D-598 (taxonomy and idiom-mixture weights are one object; validation is separate), and D-587 to
D-591 (preset naming, coverage, selectable mixtures, where a piece's mixture is stored, the licence split). None of the
framework's charters names the style system.

**What may reach L2, as the ratified framework fixes it.** Ruling 2 of the 2026-08-29 ratification sitting ratified
*"the layer decomposition, the charters and the boundary contracts"*. Within those:

- L2's charter: *"Consumes: everything L0 and L1 publish. Nothing else."*
- L0 gives the notated record: *"spelled pitch, duration, voice membership, metric position and bar, time signature,
  key signature, bar lines, repeats, fermatas, ties, pedal marks, and whether each note sounds and is visible."*
- L1 publishes slices, metric strength, notated boundary evidence and cadence cues.
- The contract table: *"L3 → L2: Nothing."* The derived statement L2-S49 says the same: *"L2 consumes nothing L3
  publishes."*

No preset, style label or idiom mixture is among what L0 and L1 publish.

**What the framework says about style, outside the charters.** `FRAMEWORK.md` §3.3: *"It does not depend on any style
identity, on any preset a user may have chosen, or on any presentation concern. Style-specificity reaches the analysis
only through the calibration of the layers that judge — their priors and weights — and never through the structure."*
§8.3 says the same. *My reading:* Ruling 2's words name the decomposition, the charters and the contracts, and do not
name §3 or §8, so whether those two sections are ratified is not stated by the ruling. Nothing below rests on them
alone; the charter and the contract table carry the same consequence for L2.

**The register says the same for presets.** D-003 (LIVE): *"Inference is preset-independent (presets are
presentation concerns)."* D-293 (LIVE): *"Values are fitted per IDIOM, never for a user preset. … A preset is a
regression surface and a carrier for delivering a fitted set."*

**What has already been ruled about L2's weights.**

- L2-S38 (the derived statement on fitting): every L2 weight is fitted from annotated music, not set by hand, and *"It
  is fitted only on freely licensed music."*
- Fit Ruling 1 of 2026-10-05: *"The tables are counted from annotated music, once, and frozen; the short list of
  combination weights is fitted discriminatively, to the graded measure."*
- Assignment-evidence Ruling 1 of 2026-10-05 carried one half of D-333 into L2: *"the weighting set per idiom, never a
  structural branch — is carried"*. So L2's weights may differ by idiom.
- Fit Ruling 2 (ii): an old fitter rule *"does not carry: it governed the legacy scorer's hand-set constants, and L2
  has none."*

**Where an idiom mixture is actually computed in the old design.** D-503 (LIVE): *"The consumer holds a weight vector
`w` with one weight per idiom. `w` is DISCOVERED from the score, seeded by the user's preference … in three phases —
forward-only, no loop."* The consumer is the progression recognizer; its register entry says the prior strength of a
recognised progression is the match score times the largest idiom-mixture weight over the entry's idioms. The
comparison proposes that recognising named progressions belongs to L3 (Row 5.91, proposed RELOCATED to *L3 — The
read-off facts*). So in the old design the per-piece mixture lives with the recognizer, after L2.

**How much music we hold per idiom.** The old fitter design says only the chorale idiom (Chromatic-functional) has
licensed annotated music, and the other four have no fit target (Row 9.237, proposed HISTORICAL — relayed from that
2026-07 design, not re-checked against the corpus record). D-422 (DEFERRED): the jazz fit waits on jazz ground truth.

**The derivation itself names no style, idiom or preset.** Searched this sitting: "idiom", "preset" and "genre" do not
occur; "style" occurs once, as "the style header" of a score file the deriving session opened; "repertoire" occurs only
for the music being graded.

**Two proposals no family has reached, which bear on this family.** Row 17.11 (ADOPTED — proposed): *"that no
user-facing style preset enter L2's reading."* Row 1.25 (ADOPTED — proposed): *"that L2's weights be fitted per idiom …
and never adjusted for a named preset."* They are not in the 86 and this surface does not take them in. The charter
already enforces Row 17.11's content; the per-idiom half of Row 1.25 is already carried through D-333. They stay
proposals unless you want them put.

### The method as it now stands, for style

L2 reads only what L0 and L1 publish: the notes with their spelling, durations, voices and bar positions, the key
signature as a weak hint, the notated marks, and L1's slices, metric strengths, boundary evidence and cadence cues. No
preset, style label or idiom mixture reaches it, and nothing comes back from L3. Every L2 weight is fitted from
annotated, freely licensed music: the term tables counted once and frozen, the short list of combination weights fitted
to the graded measure. The weights may be set per idiom. **Nothing in L2's text says how a piece's idiom would be
chosen at run time**, and with annotated music held for one idiom only (relayed), there is in practice one fitted set.

## 2. Follows from the record — recorded as this side's derivation, not asked

You may challenge each at its row. Each files documentation only; L2's algorithm is unchanged.

- **Row 23.222 claim (ii)** (`ARCHITECTURE.md`, the retirement rationale of the old jazz path): *"Analyzer output is a
  pure function of notes + key signature + preferences."* For L2, the ratified charter fixes the inputs as what L0 and
  L1 publish, which contain the notes and the key signature and no preference. The sentence is the rationale of a
  completed retirement, and its input list is replaced by the charter. **HISTORICAL.**
- **Row 57.13 claim (ii)** (`cowork_architecture_review_2026_07.md`, amendment A-10, D-499): *"pin B-swap readiness as a
  design property"*. D-499's own plain words: *"the property that a learned component could be dropped in where the
  hand-built one sits is currently true but written down nowhere"*. It is a documentation rider still to be carried out
  — a plan — and it is about replacing the old estimator's hand-built part, not about style; it came into this family
  through its row's title (my reading; the cut's reason was not recorded). The comparison's own reading files a plan
  as HISTORICAL. **HISTORICAL — a plan.** *(Corrected at the check; former wording, kept: "it came into this family
  through its row's title" — stated as a fact where it is a reading.)*
- **Recorded as open, not decided: how a piece's idiom would choose L2's weights.** Once a second idiom has licensed
  annotated music, L2 could have more than one fitted set, and the record does not say how one would be chosen for a
  given piece. Under the ratified charter no preset or mixture can reach L2, so any answer would change a charter
  (for example: L2 estimates the mixture itself as part of its reading; or one pooled set serves all idioms). Your
  rule of 2026-10-07 applies (as you gave it; not read at a record this sitting): the charter's rule holds until there
  is reason to believe breaking it would improve inference, and then it is tested by measurement. No difference
  between idioms can be measured until a second idiom's annotated music exists (D-422; corpus expansion D-500);
  within the chorale idiom, differences by mode and chromaticism can be (Row 9.238, relayed). So nothing is put now.
  *(Corrected at the check; former wording, kept: "Nothing can be measured until a second idiom's annotated music
  exists" — wider than the record, which names a measurement possible now within one idiom; and the 2026-10-07 rule
  was cited without saying it was not read at a record.)* **Trigger:** the arrival of that music. Rows 13.12(ii)
  and the style-coordinate rows may travel with it (Question 4).
- **A tension recorded for L3, not decided here.** D-503 seeds the recognizer's mixture from the user's preset; §3.3
  says the analysis depends on no preset. That falls to whoever derives L3, and is noted beside Row 5.91 on the
  transfer list.

## 3. Question 1 — which label for the style system's own live rules (45 rows)

**Meta level: the filing vocabulary of the comparison — the project's own apparatus, not the analysis.** It is worth
its cost because one answer places 45 rows, and without one they stay UNPLACED against the route ruling.

**The rows.** Sentences whose content is a live rule of the style system and whose home is `ARCHITECTURE.md` §6.7 or
§6.8, not L2:

- **The taxonomy (§6.7), 12:** Rows 25.14, 25.15, 25.16, 25.17 (one shared taxonomy of five idioms with mode and
  chromaticism beside them; tags multi-valued; the same set the progression catalog uses; discovered, not
  theory-derived); 9.30, 9.31 (the old fitter's glossary entry for the idioms; genre and era are not an axis); 50.52,
  50.53, 50.73 (the catalog's statement of the same taxonomy); 55.3 (the mapping's list of the five); 46.57 (the style
  structure is at least two-dimensional: harmonic idiom and voice-leading idiom); 43.39(ii) (genre labels live in the
  knowledge component, genre-aware behaviour at whatever reads it).
- **The discovery method (§6.7), 14:** Rows 25.20 to 25.33 — discover first, name afterwards; the encoding; the
  confound gate and the source-leakage test; the external extractor that our own analysis never touches; re-discovery
  with every corpus wave on research material only; a changed cluster set is its own ratification event.
- **Presets and mixtures, and where a mixture is stored (§6.8), 19:** Rows 25.34(i) and (ii), 25.35 (preset names: a
  familiar genre-era label with known musicians; genre labels a mixture, never an axis); 25.36, 25.37, 25.38, 25.39
  (coverage in three tiers, no bare guessing; the analysis moves away from the starting mixture as it reads the music);
  25.40, 25.41, 25.42 (every mixture selectable, each point carrying its evidence status); 25.43, 25.44, 25.45 (the
  piece's own file stores its mixture, with its provenance; a user-set mixture never silently overwritten); 25.47(ii),
  25.48(ii) (the licence split: idiom-mixture weights are free user configuration; shipped preset mixtures come from
  licensed music or are declared); 1.27 (a preset is a regression surface and a carrier; which presets a user sees is
  decided later); 9.33, 50.55, 50.76(i) (presets are named idiom-mixtures).

12 + 14 + 19 = 45.

**Why they are UNPLACED.** Each is a live rule, so HISTORICAL ("not a rule") misdescribes it. RELOCATED is defined as
"belongs to another charter", and no charter is the home of the style system. The comparison also left several of them
open because they seemed to decide whether L2 reads a style prior; §1 shows the charter already answers that (it does
not), so that obstacle is gone.

**What it changes.** Documentation only, under every alternative. L2's algorithm is unchanged: no preset or mixture
reaches L2 either way. The style system's rules stay LIVE at their own homes.

**Alternatives:**

- **A — RELOCATED, stretched to name a home outside the framework**: "RELOCATED — outside the framework, to
  `ARCHITECTURE.md` §6.7, the style taxonomy and its discovery method" (26 rows) or "… to §6.8, the user-facing preset
  layer, recorded and deferred product work" (19 rows). The stretch is recorded beside the rows, as Ruling 1 of
  2026-10-10 recorded its stretch of QUARANTINED. The transfer list gains one entry, "outside the framework — the style
  system".
  - Towards the objective (#4): keeps every rule findable at the place that maintains it, and keeps L2's text free of
    rules about a product part L2 never reads.
  - Towards the principles: #6 (each rule keeps its one home); #12 (nothing set aside unheard); #10 (the label says
    where the content went). Cost: RELOCATED's definition is stretched; the stretch is written down.
- **B — a new label**, for example "OUTSIDE THE ANALYSIS — homed at §x".
  - Towards the objective: the same as A.
  - Towards the principles: exact, but it adds a word to a vocabulary the comparison declares closed, and the
    application dispatch must re-mark with a word nothing else uses. More apparatus than A for the same effect.
- **C — HISTORICAL, with the home recorded beside each row** (the form Ruling 2 of 2026-10-10 used for the product
  scope).
  - The comparison's own reading files "a plan" as HISTORICAL, which fits the 19 deferred preset-layer rows. It does not
  fit §6.7: the taxonomy is ratified and encoded, and the discovery protocol is a standing rule.
  - Towards the principles: against #10 for the 26 §6.7 rows — the file would call live rules history.
- **D — leave them UNPLACED.** Against the route ruling, which asks you to place UNPLACED rows.

**Recommended: A.** It follows the stretch you accepted in Ruling 1, names the true home, and adds nothing to the
vocabulary.

## 4. Question 2 — the idiom tags on the catalog's entries (22 rows)

**The rows.** The mapping that tags each entry of the progression catalog with its idioms and with mode and
chromaticism: Rows 55.1, 55.2, 55.4, 55.5 to 55.17, 55.19, 55.22 (18 from the mapping), and the catalog's own
statements of the same tagging: 50.54, 50.67, 50.75, 53.11 (4). 18 + 4 = 22. For example Row 55.6: *"Secondary dominant
`V7/x`, secondary leading-tone `viio7/x` | 2 | applied chromaticism"*.

**What the record says.** The set of tags is §6.7's (D-131: the same set, not two). The tagging of each entry is part of
the catalog. The catalog's recognizer reads the tags (D-503: a recognition's prior strength uses the largest
idiom-mixture weight over the entry's idioms). The comparison proposes the recognizer and the catalog's named
progressions for L3 (Row 5.91), and sends other catalog content there with it (Rows 50.69, 50.70, 50.76(ii)). The
comparison itself grouped these tag rows with the taxonomy (Row 9.30).

**What it changes.** Documentation only. L2's algorithm is unchanged: L2 reads nothing from the catalog's recognizer
(L2-S49).

**Alternatives:**

- **A — RELOCATED to *L3 — The read-off facts*, travelling with Row 5.91.** A standard relocation, no stretch.
  - Towards the objective: the tags go where they are used, beside the mixture they feed.
  - Towards the principles: #6 (per-entry data lives with its entries; the set itself stays at §6.7).
- **B — with the taxonomy, under Question 1's answer (§6.7).**
  - Towards the principles: keeps the comparison's own grouping, but files per-entry catalog data at the section that
    defines the set, so the catalog's content would sit in two places (against #6, mildly).

**Recommended: A.**

## 5. Question 3 — per-preset values in the old scorer (4 rows)

**The rows.**

- Row 9.61 claims (i) and (iii) (the old fitter design, quoting the preset policy of `CLAUDE.md`): *"presets are fitted
  separately … a cross-style problem is solved by a structural entry condition or a preset-specific override."*
- Row 23.39 (`ARCHITECTURE.md`): when a gate causes regressions in a non-Baroque preset, the fix is *"a tighter
  structural entry condition … or (b) a preset-specific threshold value"*.
- Row 48.46 claim (ii) (`cowork_joint_estimator_architecture.md`, D-527, ruled L2's own): *"the changed
  ornamental/metric conventions … are covariate TABLE VALUES refit per preset."*

**What the record says.** These presuppose a preset reaching the scorer. L2's charter admits none, and D-003 and D-293
(*"never for a user preset"*) agree. The first three govern the old scorer's per-preset constants and gate thresholds;
L2 has no gates and no hand-set constants (fit Ruling 2 (ii)). The fourth is one clause of D-527 that D-293
contradicts, and fit Ruling 1 counts L2's tables once and freezes them. *Added at the check:* `CLAUDE.md`'s "Gate
threshold and preset policy", read at its opening, concerns the Baroque-calibrated gate thresholds of the old scorer,
and its block (A) records the regression reference as identical on every preset "because inference is
preset-independent". Your fit Ruling 2 handled the same shape for
D-383: a part that does not carry into L2, with the register status settled at the ratification act.

**What it changes.** Documentation only. L2's algorithm is unchanged: L2 already has no preset input, no per-preset
values and no gates.

**Alternatives:**

- **A — HISTORICAL: they do not carry into L2.** D-527's register status is settled at the ratification act, not here.
  - Towards the objective: no value in L2 can be tuned to make one preset come out right.
  - Towards the principles: D-293, D-003, the charter; #6 (per idiom, not per preset, is already the rule).
- **B — ADOPTED — proposed, reworded "per idiom".** It would repeat what D-293, Row 1.25's proposal and the carried
  half of D-333 already say (against #6), and refitting tables contradicts fit Ruling 1.
- **C — leave UNPLACED.** Against the route ruling.

The alternatives have nearly collapsed to A; this is put as a confirmation because one clause of a decision ruled L2's
own (D-527) is set aside by it. **Recommended: A.**

## 6. Question 4 — the style coordinates: the old fitter's model of how a fitted number varies with style (13 rows)

**The rows.** From the old fitter design's terms and its decision D-11 (that document's own numbering, not a register
entry): Rows 9.38 (a piece's style position: its idiom mixture, mode, chromaticism, and for some numbers a texture
class); 9.39 (which of those a number responds to is chosen per number); 9.41 (three shapes: no response, a table per
idiom, or a smooth function of the mixture); 9.226 (a style-varying number is a function over the style position);
9.227 (i) to (iii) (how many dimensions is measured, never assumed; values fitted at each idiom and mixed between them,
never a dense table; borders measured); 9.228 (iv) to (vii) (the coordinates chosen per number; partial pooling between
idioms; mixing valid only for some kinds of number; the mixture varies within a piece); 9.239 (an unstable verdict
defaults to the simpler structure). And Row 13.12 claim (ii) (`docs/nct_detection_design.md`): *"structural cues
(instrumentation, tempo, key signature density) might be defensible signals"* of the idiom. 1 + 1 + 1 + 1 + 3 + 4 + 1
+ 1 = 13.

**What the record says.** The old fitter design was written for the old scorer's hand-chosen constants (the
comparison's manifest for that document, reading its banner; the banner itself was not opened). *(Corrected at the
check; former wording, kept: "(its own banner)" — a relay presented as read.)* Its style model assumes a piece's mixture is known when the numbers are used. L2's charter admits no mixture;
fit Ruling 1 fixes how L2's numbers are fitted; and with one idiom's annotated music held (relayed), no cross-idiom
response can be measured (Row 9.238, proposed HISTORICAL). These rows are, in substance, possible answers to the open
question in §2: how a piece's idiom would choose L2's weights.

**The method as it now stands:** as in §1 — one fitted set in practice, weights allowed to differ by idiom, no style
input to L2.

**Alternatives:**

- **1 — HISTORICAL:** the old fitter's model for constants L2 does not have.
  - Documentation only; the algorithm unchanged.
  - Towards the objective: loses the worked-out ideas (measured dimensionality, partial pooling, the simpler-structure
    default) at the moment they could matter.
  - Towards the principles: weak on #12.
- **2 — held UNPLACED, travelling with the open question in §2** (the way your Ruling 4 of the L2-S31 record held
  four rows with the open question of chord patterns longer than pairs, DP-O — relayed from entry 330).
  - Documentation only; the algorithm unchanged.
  - Towards the objective (#4) and your 2026-10-07 rule: when a second idiom's music arrives, the question and its
    candidate answers are found together, ready to be measured.
  - Towards the principles: #12; D-254 (investigate by default); D-630 (no new component without a measured need).
- **3 — RELOCATED to *the measurement of the analysis*:** the §4.4a style-response measurement and its guards.
  - Documentation only. Fits 9.227(i) and 9.239, which are measurement rules; does not fit 9.226, 9.227(ii) or
    9.228(vi) and (vii), which describe how the numbers themselves would be built.
- **4 — ADOPTED — proposed:** a style-response model added to L2.
  - **This changes the algorithm as the specification defines it, and would also change L2's charter**, because it
    needs a mixture as input.
  - Against the charter, D-003, D-630 and #17(b): no measured basis, and no response across idioms can be measured
    with one idiom. *(Corrected at the check; former wording, kept: "nothing can be measured with one idiom".)*

**Recommended: 2.** Meta level: the analysis's own specification (what stays attached to an open question about L2).

## 7. The arithmetic

- Recorded as derivation (§2): 2 (Rows 23.222(ii), 57.13(ii)).
- Question 1: 45. Question 2: 22. Question 3: 4. Question 4: 13.
- 2 + 45 + 22 + 4 + 13 = 86.

Under the recommendations, every one of the 86 is placed, 13 of them as held with the open question. After this family,
the UNPLACED population is those 13 (if Question 4 is ruled 2) and the six already held (five by your rulings, Row
7.104(i) by the tractability record).

## 8. What this surface does not do

- It places nothing until you rule.
- It writes no dispatch.
- It does not put the open question of §2.
- It does not take in Rows 17.11 or 1.25.
- It does not touch the six held rows.

## 9. What was read for it

- The reading file: §5, member 25 whole, member 55 whole, Rows 1.25 to 1.27, 9.30 to 9.42, 9.61 to 9.63, 9.226 to
  9.240, 13.11 to 13.12, 17.11, 23.33 to 23.39, 23.222, 43.39, 46.57 to 46.58, 48.46, 50.52 to 50.56, 50.67 to 50.76,
  53.11, 57.13, 5.91, and member 9's manifest.
- `FRAMEWORK.md`: §0, §1, §2, §3.1 to §3.3, §5 (L0, L1, L2, L3, the second axis, NOT A LAYER, the contract table),
  §8.
- The derivation: L2-S38 and L2-S49 whole; a search for style, idiom, preset and genre.
- `ARCHITECTURE.md`: the §6 headings, §6.1, §6.7's opening, the lines 5578 to 5627 (the end of §6.7 and the opening of
  §6.8).
- `cowork_idiom_entry_mapping.md` whole.
- Register entries whole at their group files: D-003, D-131, D-132, D-293, D-421, D-499, D-503, D-542 to D-545, D-587
  to D-591, D-598. The register index whole.
- Ruling records: the 2026-10-05 fit sitting whole; the 2026-10-05 assignment-evidence sitting at Ruling 1; the
  2026-10-04 route sitting whole; the 2026-08-29 ratification sitting at Ruling 2; the 2026-08-07 owner rulings at the
  maintained-object rule; a search of all 2026-10-04 to 2026-10-09 records and of the 2026-08-31 record for the rows
  and decisions named here.

Not opened: `cowork_progression_schema_design.md`, `cowork_stage5_fitter_design.md`, `cowork_style_taxonomy_proposal.md`,
the corpus record behind "one idiom held".

## §B. The check, run at the sources in the turn after the surface was delivered

Every quotation was compared with its source, and every claim tested for completeness, coherence, correctness and words
wider than what was read. Four corrections and one addition, made at their sites above with the former wordings kept:

1. **§2, the open question:** "Nothing can be measured until a second idiom's annotated music exists" was wider than
   the record; Row 9.238 names differences by mode and chromaticism as measurable now within the chorale idiom. Narrowed
   to differences between idioms. The 2026-10-07 rule is now marked as not read at a record.
2. **§6, alternative 4:** the same over-wide "nothing can be measured", narrowed the same way.
3. **§6, the old fitter design's banner:** cited as read; it was the comparison's reading of it. Now labelled a relay.
4. **§2, Row 57.13(ii):** why the cut put it in this family was stated as a fact; it is a reading.
5. **Added to §5:** `CLAUDE.md`'s gate-threshold and preset policy, read at its opening, which supports Question 3.

**Confirmed at the objects, unchanged:** the quotations of `FRAMEWORK.md` §3.3, the L2 charter, L0's list and the
contract table; Ruling 2 of 2026-08-29; D-003, D-293, D-503 and their provenance; L2-S38 and L2-S49; fit Rulings 1 and
2 (ii); assignment-evidence Ruling 1; the maintained-object rule; §6.8's status line; the rows' texts and their
proposed placements as the comparison writes them; the arithmetic 12 + 14 + 19 = 45, 18 + 4 = 22, 2 + 45 + 22 + 4 +
13 = 86.

Nothing in the check moved a recommendation.

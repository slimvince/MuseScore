# THE SEALED PLACEMENT SAMPLE — 2026-08-27

> # ⛔ DO NOT READ IF YOU ARE AUTHORING THE FRAME.
>
> **This file is withheld from the frame's author, alongside the code.** Ruling 3 of
> `cowork_rulings_2026_08_27_placement_sample_sitting.md`. If you are the fresh Cowork session that
> authors the framework phase's frame, stop reading here and close this file. Reading it defeats the
> sealing property that Ruling 3 of `cowork_rulings_2026_08_26_framework_opening_sitting.md` exists
> to create.
>
> ---
>
> **THIS IS THE SEALED PLACEMENT SAMPLE, AND IT IS CLOSED.** Drawn at branch tip
> `0e7186a961f50b32e0552483b289b11069f1319a`, read by this side at `.git/refs/heads/master` with the
> file tool. Enumerated and drawn by Claude Code under `cc_instruction_placement_sample.md`, which
> carries the selection rule authored by the writing side **before any count was known**. The
> drawing side chose nothing: given the enumeration, exactly one sample follows from the rule.
> Committing this file is the seal.
>
> ---
>
> **`T = 25` IS DECLARED, NOT DERIVED.** No measurement in this project supports it. It is the
> threshold and take-rate the dispatch declares at its Task 2.2, with the stated ground that the
> predecessors' whole placement test placed sixty statements across all sources, so twenty-five per
> stratum gives each stratum on its own more than a third of what the entire test formerly had, and
> caps this one at two hundred items across eight strata. **A successor citing 25 as a measured
> value has misread it.**
>
> ---
>
> # ⛔ FOUR STRATA ARE **STOPPED**, AND THE FRAME IS NOT AUTHORED UNTIL THE USER HAS RULED ON EVERY
> # ONE OF THEM.
>
> A sample missing a stratum nobody ruled on is not sealed, it is incomplete — Ruling 3 of
> 2026-08-26 read plainly. The four, each with what was found and what is missing, are at §§1, 2, 3
> and 6 below:
>
> | Stratum | Why it is STOPPED |
> |---|---|
> | **1 — ruling records** | Two named objects disagree about the membership: 74 files against 78. |
> | **2 — decision surfaces** | No object enumerates the class, and the one named directory demonstrably does not hold all of them. |
> | **3 — dossiers** | The repository's only tree-wide, user-ruled classification deliberately does not separate dossiers; and the declared unit has no determinable form. |
> | **6 — declared dormancies** | No defining artifact exists; three candidate readings of the phrase disagree. |
>
> **Four strata ARE drawn and are sealed here: 4, 5, 7 and 8.** Their being drawn does not make the
> sample complete.
>
> ---
>
> **What this file does NOT carry**, by the dispatch's own instruction: any judgement about whether
> an item is placeable, any grouping by topic, any commentary on the frame, any ranking. **It is a
> list.**

---

## 0. The selection rule, quoted from the dispatch that authored it

**The ordering — deterministic, and no other ordering is permitted.** Within each stratum, items are
ordered by this tuple, ascending: (1) the repository-relative path of the file the item is found in,
by byte order; (2) then the line number at which the item begins; (3) then, **for stratum 8 only**,
the hash of the commit that deleted the heading, lexicographically. Not by importance, recency,
topic, length or interest.

**The threshold and the take.** Let `N` be a stratum's enumerated count and `T = 25`.

- If `N ≤ T`: the stratum goes in **WHOLE** — census, no sampling, no uncertainty range needed.
- If `N > T`: the stratum contributes exactly `T = 25` items, taken systematically from the ordering
  above: `k = floor(N / T)`; the items at 1-indexed ordered positions `1, 1+k, 1+2k, …, 1+24k`.

**TWO ITEMS IDENTICAL ON ALL THREE ORDERING KEYS ARE A STOP.** It was checked for every drawn
stratum and **no such pair occurs in any of them**; the check is recorded at each stratum below.
*(The dispatch words this condition with the verb "tie"; the word is avoided in this record's own
prose under the reserved-word convention, and nothing about the condition is changed by that.)*

**★ A PROPERTY OF THE DECLARED RULE, REPORTED BECAUSE IT IS NOT OBVIOUS FROM ITS WORDING AND IT
DECIDES WHAT TWO OF THE FOUR DRAWN STRATA CONTAIN.** For any stratum with `T < N < 2T` — that is,
`26 ≤ N ≤ 49` — `k = floor(N/T) = 1`, and the take `1, 1+k, …, 1+24k` degenerates to positions
`1 … 25`: **the first twenty-five items of the ordering, contiguously, and nothing after them.** It
is not a spread. This is what happened to **stratum 5** (`N = 33`, so items 26–33 — the whole of the
inventory's Layer-5 section and most of its Layer-4 section — cannot be drawn) and, less severely,
to **stratum 8** (`N = 59`, `k = 2`, so the ordering's positions 51–59 cannot be drawn). The rule was
applied exactly as written; the consequence is reported and nothing was adjusted to soften it.

---

## 1. Stratum 1 — ruling records — **STOPPED**

**Unit declared by the dispatch:** one numbered ruling in a ruling record.

**Two named objects define this class, and they disagree. Neither was chosen.**

**Object A — `tools/audit/gen_evidence_pin_membership.py`**, whose output
`tools/audit/evidence_pin_membership.json` this batch regenerated at Task 0(c). It publishes the
definition among the things it DERIVES, at `tools/audit/gen_evidence_pin_membership.py:29`:

> `RULING RECORDS       Every root-level `cowork_rulings_*.md`.`

and implements it at `tools/audit/gen_evidence_pin_membership.py:112`:

> `RULING_RECORD = re.compile(r'^cowork_rulings_.*\.md$')`

Its run at Task 0(c) reported **`ruling records read 74`**, and the artifact carries the same
definition in its own field `the_derivation.ruling_records`: *"every root-level
`cowork_rulings_*.md`"*.

**Object B — `tools/audit/gen_artifact_inventory.py`**, the derived walk of the whole tree, whose
class **`writing-side-ruling-records`** is defined at
`tools/audit/gen_artifact_inventory.py:245-249`:

> `("writing-side-ruling-records",`
> ` "repository-root files whose name begins `cowork_rulings_`, `cowork_ruling_`, "`
> ` "`cowork_owner_rulings_`, `cowork_pending_rulings_` or `cowork_document_route_rulings_`",`

That class and its signature were **put to the user and ruled** — the reading surface is
`ratification_surfaces/cowork_artifact_inventory_ruling_surface.md` §16, which carries the same
signature verbatim beside its example members.

**The disagreement, measured at the objects.** Object B's signature admits **four root-level files
that Object A's excludes**, all four present on disk at the seal:

| File | Admitted by B's prefix | In A? |
|---|---|---|
| `cowork_ruling_guard_family_2026_08_08.md` | `cowork_ruling_` | no |
| `cowork_owner_rulings_2026_08_07.md` | `cowork_owner_rulings_` | no |
| `cowork_pending_rulings_2026_08_02.md` | `cowork_pending_rulings_` | no |
| `cowork_document_route_rulings_2026_08_08.md` | `cowork_document_route_rulings_` | no |

So the file population is **74 under A and 78 under B**. Because the declared unit is a numbered
ruling *inside* a record rather than the record itself, the item count differs by more than four, and
`k = floor(N/25)` differs, so **the two readings produce entirely different draws** — not merely a
sample four items longer.

**What is missing:** a ruling saying which of the two objects defines the stratum. Nothing else is
missing — both objects exist, both are generated, both are current, and both are unambiguous on their
own terms.

**One thing that is NOT a second disagreement, checked so the writing side does not have to.** The
tracked/untracked axis is inert here: at the start state exactly **two** root-level ruling records
stood untracked, and both were landed by this batch's Task 0(c). Working-tree membership and tracked
membership therefore coincide at the seal.

---

## 2. Stratum 2 — decision surfaces — **STOPPED**

**Unit declared by the dispatch:** one numbered decision in a decision surface.

**No object in this repository enumerates the decision surfaces.** What exists:

**Candidate A — the directory `ratification_surfaces/`,** named as a class by
`tools/audit/gen_artifact_inventory.py:240-242`:

> `("ratification-surfaces",`
> ` "anywhere below `ratification_surfaces/` — the reading surfaces a ruling was taken on",`

and its authored reason on the ruling surface
(`ratification_surfaces/cowork_artifact_inventory_ruling_surface.md` §15) is the only place in the
record that says what a decision surface *is*:

> **Reason — AUTHORED:** The reading surfaces rulings were taken on. Each states the alternatives,
> their costs and the recommendation — so it carries not only what was decided but what was declined
> and why, which is the constrained-optimum shape the ledger corollary to #17 asks for. Directly
> admissible: a decision surface argues from principles toward a choice, which is design intent by
> construction.

It holds **31 files** at the seal.

**Candidate A is refuted as complete, at the objects.** Decision surfaces stand at the repository
**root**, outside that directory — `cowork_extent_decision_surface.md`,
`cowork_phase1_commissioning_surface_2026_08_11.md`,
`cowork_framework_phase_opening_surface_2026_08_26.md` and
`cowork_placement_sample_surface_2026_08_27.md`. Two of those four are named as decision surfaces by
the writing side's own text: `cowork_placement_sample_surface_2026_08_27.md:239-241` lists what the
frame's author must read — *"this handoff, yesterday's ruling record, the opening surface, the plan,
the phase-definition surface"* — and then says of them:

> Those are *ruling records* and *decision surfaces*: two of the eight strata the sample is drawn
> from.

The *opening surface* in that list is `cowork_framework_phase_opening_surface_2026_08_26.md`, a
root-level file. So the directory is not the class.

**Candidate B — `tools/audit/gen_ratification_surface_set.py`** and its output
`tools/audit/ratification_surface_set.json`. Its CLASS reading is defined at
`tools/audit/gen_ratification_surface_set.py:15-18`:

> `CLASS   -- every root-level document whose own opening declares it a ratification queue or`
> `           a ratification review aid. This is the candidate population, and it is the only`
> `           reading that is a property of the DOCUMENTS rather than of who happens to cite`
> `           them.`

This is a **different subject** — ratification queues and review aids, not surfaces that argue
alternatives toward a choice — and it is root-scoped, so it excludes the directory that Candidate A
is. The two do not merely disagree at the edges; they enumerate different kinds.

**What is missing:** an object, or a ruling, that says which documents are the decision surfaces.
Both candidate readings are named objects, both are current, and they disagree in both directions.

---

## 3. Stratum 3 — dossiers — **STOPPED**

**Unit declared by the dispatch:** one claim or finding entry in a dossier.

**The membership is not determinable from any named object, and the reason is a deliberate property
of the one object that could have supplied it.** `tools/audit/gen_artifact_inventory.py` is this
project's only derived, whole-tree, user-ruled classification of every file — all 44 of its classes
were put to the user and ruled at
`ratification_surfaces/cowork_artifact_inventory_ruling_surface.md`. **It has no dossier class.** It
lumps dossiers into two classes by path prefix alone, naming them in the class descriptions:

`tools/audit/gen_artifact_inventory.py:256-259`:

> `("writing-side-design-documents",`
> ` "every other repository-root file beginning `cowork_` — designs, audits, dossiers, plans, "`
> ` "inventories and findings authored by the writing side",`

`tools/audit/gen_artifact_inventory.py:269-272`:

> `("reports-from-the-coding-side",`
> ` "every other repository-root file beginning `cc_` — the reports, dossiers and measurement "`
> ` "outputs CC returned",`

and it states in terms, at `tools/audit/gen_artifact_inventory.py:25-29`, why it will never separate
them:

> `THE SIGNATURE IS PATH AND EXTENSION ONLY. ... every tracked file at the commit this ran against`
> `is classed by where it sits and what it is called.  That is a stronger position than the dispatch`
> `requires and it is recorded here so a later reader does not add a content read casually — a`
> `signature that opens a file is one that can be argued about, and this table cannot.`

**The only remaining candidate is a filename convention, `*_dossier.md`, which the record nowhere
establishes.** It matches **26** root-level files at the seal. It also collides with the ruled
classification for at least one of them: `cc_instruction_stage3_4i_gate_retirement_dossier.md` is a
**dispatch** under the ruled class `dispatches-to-the-coding-side`
(`tools/audit/gen_artifact_inventory.py:266-268`, *"repository-root files beginning
`cc_instruction_` — one dispatch per CC session"*) and a **dossier** under the convention. Nothing
in the record decides which it is for this purpose.

**A second, independent reason this stratum cannot be enumerated: the declared unit has no
determinable form.** No dossier declares a "claim" or a "finding entry" as its unit of record, and
the two opened to check use unrelated structures — `cowork_adjudication_dossier.md` is two Parts
(`## Part A — the seven audit adjudications, in plain language` at line 14; `## Part B — the 17
siloed facts: complete disposition …` at line 90), while `cc_functional_residual_dossier.md` is
numbered task sections with sub-sections (`## §0 — Task 0: the headroom decomposition …` at line 22,
`### §0.1 — The three headline counts (NEW vs OLD)` at line 33, and so on). Even with the membership
ruled, the items could not be enumerated without the writing side fixing the unit.

**What is missing:** a ruling naming the object that defines the dossier population, **and** a
determinable unit inside a dossier. Both are owed; neither is invented here.

---

## 4. Stratum 4 — the DEFERRED entries of the decisions register — **CENSUS, N = 21**

**Defining object: the decisions register itself — the INDEX `DECISIONS.md` — read at its STATUS
field.** The status vocabulary is stated in the register's own table at `DECISIONS.md:175`:

> `| **DEFERRED** | Decided to be built later. The decision itself stands. |`

and the register declares itself generated, never hand-edited, from one source
(`DECISIONS.md:90-93`):

> **GENERATED FILE — do not hand-edit.** Source of record:
> `tools/audit/decisions/backbone_decisions.json`; generator
> `tools/audit/decisions/gen_decisions_register.py`. Every number below is computed, never
> transcribed.

**The membership is the register's own rows whose status cell opens `DEFERRED`** — which under the
register's rule (f) is what carries a row's state, the `⚠LEGACY` marking being a separate flag and
not a second status. **`N = 21`.**

**One thing established rather than assumed, because it would otherwise silently change `N`.** The
source `backbone_decisions.json` carries **51** records with `"status": "deferred"`. The difference
is not a discrepancy: thirty of them sit in the file's **retired / soft-discarded** array, not in its
`decisions` array, and the register does not render them — they were retired from it on 2026-08-17
under Rulings 1 and 3 of `cowork_rulings_2026_08_17_residue_sitting.md`. **The register's DEFERRED
entries are the 21 the register carries.** Both numbers are reported so a successor meeting 51
somewhere else does not read this census as short.

**Ordering:** all 21 items are found in one file, so the ordering is by line number in
`DECISIONS.md`. **No two items are identical on the ordering keys.** `N ≤ T`, so this is a census: `k` does not apply and
no uncertainty range is needed.

### The 21 items, verbatim, with `path:line`

**1 — `DECISIONS.md:290`**
```
| D-008 | The true probabilities are deferred to a later step | DEFERRED | — | `ARCHITECTURE.md` |
```

**2 — `DECISIONS.md:331`**
```
| D-021 | The pedal-point fields are suspended on the record arm | DEFERRED | — | `ARCHITECTURE.md` |
```

**3 — `DECISIONS.md:382`**
```
| D-422 | The jazz fit is deferred to the jazz ground-truth conversion; only the classical common-practice idiom is fitted now | DEFERRED | 2026-08-03 · user | `cowork_score_census.md` §5 |
```

**4 — `DECISIONS.md:469`**
```
| D-207 | The pedal-point class is defined voice-independently, superseding the bass-only fact | DEFERRED | — | `ARCHITECTURE.md` |
```

**5 — `DECISIONS.md:473`**
```
| D-300 | Gate M (minor read as diminished) is DEFERRED and must not be retried without a new runtime signal | DEFERRED ⚠LEGACY | 2026-08-02 · user | `docs/scoring_model.md` |
```

**6 — `DECISIONS.md:474`**
```
| D-301 | Gate N (major read as an inverted minor) is DEFERRED and must not be retried without a multi-region model | DEFERRED ⚠LEGACY | 2026-08-02 · user | `docs/scoring_model.md` |
```

**7 — `DECISIONS.md:494`**
```
| D-381 | The carry must cap on DISTINCT ROOTS, not on voicings — the existing voicing-keyed cap gives no structural guarantee that a third root survives | DEFERRED ⚠LEGACY | 2026-08-02 · user | `cowork_layer5_engagement_design.md` “§2.3 Does the decoder's governed carry provide this? The distinct-root guarantee is OWED [code]” |
```

**8 — `DECISIONS.md:510`**
```
| D-580 | Two of the twelve post-scoring gates are purely-local vertical refinements and MUST survive the dissolution; the other ten dissolve into the competition | DEFERRED ⚠LEGACY | 2026-08-04 · user | `docs/scoring_model.md` |
```

**9 — `DECISIONS.md:520`**
```
| D-084 | The progression-schema recognizer is a consumer of the function layer, not a new layer | DEFERRED | — | `ARCHITECTURE.md` |
```

**10 — `DECISIONS.md:522`**
```
| D-248 | Tonicization labels are not implemented and are deferred | DEFERRED ⚠LEGACY | 2026-08-02 · user | `ARCHITECTURE.md` |
```

**11 — `DECISIONS.md:584`**
```
| D-404 | Relocating the neighbour-chord temporal-context computation out of the derived-view layer is DEFERRED to the decoder engagement, which owns regional temporal context | DEFERRED ⚠LEGACY | 2026-08-02 · user | `cowork_structural_integrity_audit.md` §3.1 ⚠gap |
```

**12 — `DECISIONS.md:587`**
```
| D-428 | Component (1b) of the two-deferred-refactors mandate — the iteration-vocabulary API renames: STILL OWED, and the subject is the LEGACY arm | DEFERRED ⚠LEGACY | — | `docs/implementation_roadmap.md` |
```

**13 — `DECISIONS.md:588`**
```
| D-429 | Component (2) of the two-deferred-refactors mandate — dissolving the post-hoc gate-correction layer into fitted weights: STILL OWED, and its PRINCIPLE binds the live design | DEFERRED ⚠LEGACY | — | `docs/implementation_roadmap.md` |
```

**14 — `DECISIONS.md:658`**
```
| D-132 | The remaining empirical grounding is the per-preset WEIGHTS alone; the clusters half is delivered by the ratified five-idiom set | DEFERRED | — | `ARCHITECTURE.md` |
```

**15 — `DECISIONS.md:661`**
```
| D-410 | The first version matches EXACTLY AND WHOLE; the partial matcher is deferred with its decision structure already fixed and only its constants left open | DEFERRED | 2026-08-03 · user | `cowork_progression_schema_dictionary.md` §4 |
```

**16 — `DECISIONS.md:662`**
```
| D-411 | The Axis loop is ONE entry in one canonical rotation — its other rotations become rotation-tolerant matching on that entry, never three more entries | DEFERRED | 2026-08-03 · user | `cowork_progression_schema_dictionary.md` §5.2 |
```

**17 — `DECISIONS.md:683`**
```
| D-440 | The language-model integration is purpose-built and does not wait for the plugin-API reform | DEFERRED | 2026-08-04 · user | `ARCHITECTURE.md` |
```

**18 — `DECISIONS.md:684`**
```
| D-441 | Analysis and modification are phases of ONE conversation; a follow-up instruction re-uses the reasoning rather than re-analysing | DEFERRED | 2026-08-04 · user | `ARCHITECTURE.md` |
```

**19 — `DECISIONS.md:748`**
```
| D-202 | The effort control is one setting with several dials, and it must bound the time taken | DEFERRED | — | `ARCHITECTURE.md` |
```

**20 — `DECISIONS.md:752`**
```
| D-206 | Intonation is held as a future feature, and is a declared future consumer of the analysis | DEFERRED | — | `ARCHITECTURE.md` |
```

**21 — `DECISIONS.md:774`**
```
| D-258 | A prune and tidy pass runs before any publish of the fork, and nothing on its list is acted on before it | DEFERRED | 2026-08-02 · user | `cowork_prune_pass_checklist.md` |
```

---

## 5. Stratum 5 — the evidence inventory — **TAKE, N = 33, k = 1**

**Defining object: `cowork_evidence_inventory.md`**, one file, and it is a member of the
specification document set by an ADMITTED delegation `ARCHITECTURE.md` writes to it — the grade and
its governing naming are published at `tools/audit/specification_document_set.json` and the grade's
ground is stated at `tools/audit/gen_specification_document_set.py:280-287`:

> `"cowork_evidence_inventory.md": g(`
> `    CLAUSE,`
> `    "A subject-is-X naming with a delegating predicate — 'The catalog of what each layer "`
> `    "discovers is X' — the same shape as the bar's first admitted form, and it binds an "`
> `    "obligation to the document (kept in step with the layer specifications as facts are "`
> `    "adopted). Same grade and same ground as the seed's.",`

**★ THE UNIT IS A DECLARED READING AND THE WRITING SIDE MUST SEE IT, BECAUSE THE ALTERNATIVE
READING CHANGES BOTH `N` AND THE DRAW.** The dispatch's unit is *"one inventory row"*. **The document
contains no table and therefore no rows**: a search for a table row (`^\s*\|`) returns **zero
matches**. Its records are markdown list items. The reading taken here is **every markdown list
item, at any nesting depth** — `N = 33` — because it is the only reading that adds no judgement of
mine: 24 items sit at the top level and 9 are nested one level deep, and excluding the nested ones,
or excluding the two top-level items that are bare labels introducing nested ones
(`cowork_evidence_inventory.md:100` and `:123`), would each be a decision about which items count.
**Under the alternative reading — top-level items only — `N = 24`, which is `≤ T`, so the stratum
would be a CENSUS of 24 and the drawn set would be different.** The reading is declared, not
concealed; it is the writing side's to fix.

**Ordering:** all items are in one file, ordered by line number. **No two items are identical on the
ordering keys.**
`N = 33 > T`, so `k = floor(33/25) = 1` and the take is positions `1 … 25` — the contiguous first
twenty-five, per the property recorded at §0. The document's §7 (Layer 5) contributes nothing.

### The 25 drawn items, verbatim, with `path:line`

**1 — `cowork_evidence_inventory.md:17`**
```
- Notated pitches with SPELLING (tonal pitch classes — F♯ vs G♭ as the composer wrote
  them). INPUT, carried at the note layer, consumed today by one pin only (OI-15).
  **This is the fact that dissolves the spelling circularity — see §8.**
```

**2 — `cowork_evidence_inventory.md:20`**
```
- Notated key signature(s), INCLUDING mid-piece changes. INPUT; read once at start,
  changes never re-anchored (OI-94).
```

**3 — `cowork_evidence_inventory.md:22`**
```
- Declared mode from the file format. INPUT; siloed to the key path (OI-78).
```

**4 — `cowork_evidence_inventory.md:23`**
```
- Time signatures; barlines including double/section barlines; repeats.
  INPUT; time signatures consumed by metric weights; the rest UNDISCUSSED —
  a double barline is a section boundary hint, directly useful for phrase-aligned
  key spans.
```

**5 — `cowork_evidence_inventory.md:27`**
```
- **Fermatas.** In Bach chorales the fermata IS the phrase-end marker — the single
  most reliable phrase-boundary fact in exactly our corpus, and the comparable
  product's biggest key-detection win came from a phrase-end ("pseudo-fermata")
  alignment fix. UNDISCUSSED as key evidence; not in the note model's 11 documented
  facts. Cheap to read; enormous leverage for transition costs and cadence location.
```

**6 — `cowork_evidence_inventory.md:32`**
```
- **Rests/silences as phrase ends** (user-raised 2026-07-12, pairing with the
  fermata fact above): a sufficiently long rest signals a phrase end just as a
  fermata does. Status: HALF-EMBODIED — the dormant phrase-boundary view is already
  a silence-based phrase-end detector, gated off, with "sufficiently long" a
  hand-set 240-tick threshold (one of the OI-87 unfit constants). The composite
  publication the key layer wants: phrase-end facts from fermatas AND long rests
  together (fermatas are a chorale convention; rests generalize to other
  repertoire), the silence threshold fit rather than guessed. Grace notes
  (embellishment hints); slurs/articulation (phrase shaping, weak); lyrics/verse
  structure (chorale phrase structure — UNDISCUSSED, probably redundant with
  fermatas); tempo/character markings (style/preset hints, weak); pedal lines
  (sustain — affects which pitches actually sound together; the known piano-pedal
  gap in the backlog); instrument/part names (voice identification).
```

**7 — `cowork_evidence_inventory.md:45`**
```
- Existing chord-symbol / Roman-numeral / Nashville annotations IN the score —
  recognized as flags, never read (OI-80). A user-provided ground-truth hint the
  analysis ignores entirely.
```

**8 — `cowork_evidence_inventory.md:51`**
```
- Per note: pitch class, octave/register, onset, duration, tie state, voice and
  staff identity, spelled pitch. PUBLISHED at the model — **but voice/staff identity
  is DROPPED at the shared tone surface** (OI-74), which is why everything above the
  note layer is voice-blind (the structural root of several silos).
```

**9 — `cowork_evidence_inventory.md:55`**
```
- UNDISCUSSED from this layer: **register/bass-register identity as evidence**
  (the bass voice's motion is the strongest functional signal there is — see layer
  1.5); octave doubling counts (which pc the texture emphasizes); courtesy
  accidentals versus functional accidentals (a NOTATED accidental outside the
  signature is a tonicization/mode event in the composer's own hand — a raised
  seventh in minor is literally written on the page).
```

**10 — `cowork_evidence_inventory.md:64`**
```
- Metric weights: region-level weights PUBLISHED; **per-note beat weight
  decoder-private** (OI-82). Beat strength is evidence for cadence arrival and for
  which tones are structural.
```

**11 — `cowork_evidence_inventory.md:67`**
```
- Weighted pitch-class collections per span (with repetition and cross-voice
  boosts — constants unfit, OI-87). PUBLISHED to the key path (its emission input).
```

**12 — `cowork_evidence_inventory.md:69`**
```
- Bass onset/sub-boundary facts. Computed; consumption narrow.
```

**13 — `cowork_evidence_inventory.md:70`**
```
- **Phrase-boundary view: ends-a-phrase facts. DORMANT, gated off** — the exact
  fact the transition-cost design wants (and fermatas §1 would make it sharper).
```

**14 — `cowork_evidence_inventory.md:72`**
```
- Per-note melodic signals (step/leap/suspension — `StepwiseSignals`): **TRAPPED
  inside the decoder's membership internals** (OI-72).
```

**15 — `cowork_evidence_inventory.md:74`**
```
- Texture classification (homophonic/polyphonic; the voice-leading axis): DORMANT.
  The comparable product routes its key detectors BY texture — never discussed here.
```

**16 — `cowork_evidence_inventory.md:76`**
```
- UNDISCUSSED from this layer: **bass MOTION intervals** (a bass falling a fifth
  into a strong beat is the dominant→tonic skeleton — computable voice-aware from
  the model without any chord knowledge); **soprano scale-degree at phrase ends**
  (cadence formulas constrain the melody note — a PAC wants the tonic on top);
  melodic contour per voice; parallel-motion facts (voice-leading legality —
  built in the dormant axis).
```

**17 — `cowork_evidence_inventory.md:85`**
```
- Slices (change-point boundaries), slice durations, explicit empty slices.
  PUBLISHED.
```

**18 — `cowork_evidence_inventory.md:87`**
```
- UNDISCUSSED from this layer: **boundary STRENGTH** (how decisive the change-point
  evidence was — a graded boundary confidence instead of a binary cut; useful for
  tonicization-boundary arbitration and for the segmentation-edge artifact class);
  **harmonic rhythm** (the pattern of slice durations — accelerating harmonic
  rhythm approaching a phrase end is a classic cadence-approach signal, textbook
  theory, computable purely from slice durations); anacrusis/pickup detection.
```

**19 — `cowork_evidence_inventory.md:96`**
```
- Produced today: per-region key+mode; the alternatives list (top-4, margins
  DISCARDED — OI-75/OI-81); a sequence-margin confidence (diagnostics only); the
  full 252-state per-slice emission scores (dump-only); the declared-mode
  pass-through.
```

**20 — `cowork_evidence_inventory.md:100`**
```
- UNDISCUSSED facts this layer KNOWS and could publish:
```

**21 — `cowork_evidence_inventory.md:101`**
```
  - **The collection/tonic split.** The decode is often CONFIDENT about the pitch
    collection (one flat) while ambiguous only about the tonic within it (F major
    vs D minor). Publishing "collection: confident; tonic: open between these two"
    instead of one flat key guess is the single most consequential unpublished fact
    in the system — because our own measurements show the chord layer's decisions
    are almost entirely collection-driven (roots are key-invariant under collection
    siblings). The chord layer could consume the confident half while the tonic
    stays honestly open for cadence/grammar evidence to settle. See §8.
```

**22 — `cowork_evidence_inventory.md:109`**
```
  - Per-slice key AMBIGUITY (the emission near-tie structure — where the music is
    locally keyless/transitional; useful to the chord layer's symmetric-rotation
    handling and the function layer's open marks).
```

**23 — `cowork_evidence_inventory.md:112`**
```
  - Boundary-margin facts (how close the decode was to placing a key change one
    slice earlier/later — tonicization-boundary evidence).
```

**24 — `cowork_evidence_inventory.md:114`**
```
  - Which pitch classes DROVE the key choice (evidence decomposition — useful for
    explaining and for spotting emission pathologies).
```

**25 — `cowork_evidence_inventory.md:119`**
```
- Produced today: the committed identity (root/quality/inversion/bass/extensions);
  capped alternatives (voicing-biased, OI-9); the raw candidate grid + threshold
  (in-memory); membership verdicts (chord tones vs non-chord tones) — **dying at
  the layer-4→5 boundary** (OI-73); abstention margins; a diatonic-to-key flag.
```

---

## 6. Stratum 6 — the declared dormancies — **STOPPED**

**Unit declared by the dispatch:** one declared dormancy.

**The concept is defined; the population is not.** The definition is `CLAUDE.md:251-255`, the
fact-publication corollary ratified by the user 2026-07-10:

> *Fact-publication corollary to #6/#7/#12 (ratified by the user, 2026-07-10):* every derived
> analytical fact is **published exactly once, on the producing layer's output surface;
> consumers read, never re-derive.** A fact consumed by no one is either **declared dormancy**
> (its future consumer named) or **waste** (removed).

**No defining artifact exists.** A search of the whole generated-artifact population for the stem
`dormanc` returns 36 `.json` files; every one of them is a register data file, a per-layer audit
disposition set, a guard classification or a screen — **none is an enumeration of the declared
dormancies**, and no generator writes one.

**Three candidate readings, and they disagree about the subject as well as the extent.**

1. **The evidence inventory's dormancy labels.** `cowork_evidence_inventory.md`'s own banner (lines
   10–13) declares a status vocabulary per fact including *"DORMANT (built, gated off)"*, and its
   §8b is headed `## 8b. Declared future consumers, named by the user (2026-07-13)` — which is the
   corollary's own *future consumer named* half. Under this reading the population is a set of rows
   in one document.
2. **The free-text declarations across the record.** `ARCHITECTURE.md` carries the phrase twice, at
   `:31` (*"…as declared dormancy — consumer: the notation record build…"*) and at `:87` (*"their
   declared dormancy is discharged"*), and it recurs across dispatches, CC reports and per-layer
   audit dispositions. Under this reading the population is scattered across dozens of files with no
   marker convention to find it by.
3. **The specification document set's per-member `live_or_dormant` property**, published at
   `tools/audit/specification_document_set.json` and DORMANT for several members. This is a
   **different subject** — a document's dormancy, not a published fact's — and is named here only so
   the writing side can rule it out explicitly rather than have a successor find it and use it.

**What is missing:** an object, or a ruling, that says what the declared dormancies are and where
they are enumerated. Note the second reading's shape: if it governs, the stratum cannot be
enumerated at all without a marker convention being built first, which is work rather than a ruling.

---

## 7. Stratum 7 — every current document heading — **TAKE, N = 730, k = 29**

**Defining object: `tools/audit/specification_document_set.json`, the derived membership of THE
DOCUMENT SET**, written by `tools/audit/gen_specification_document_set.py`. The stratum's own wording
comes from the successor plan §6.2 (`cowork_specification_reconstruction_plan_successor_2026_08_21.md:323-327`):

> **What the current headings and the deleted headings become:** NOT the frame's source. They are
> demoted to a TEST POPULATION for the placement test below — every current heading and every
> heading ever deleted from the document set is a statement to be placed — which keeps the one
> real value of the history walk (a removed section is a dropped perspective) without inheriting
> the structure or paying the history walk's unmeasured cost up front.

and *the document set* is the plan's §5, derived in three limbs, which
`tools/audit/gen_specification_document_set.py:7-12` restates as what it exists to produce:

> `WHAT IT IS FOR.  The successor plan`
> `(`cowork_specification_reconstruction_plan_successor_2026_08_21.md` §5) needs to know WHICH`
> `documents specify the analysis.  The ruling fixes the answer in three limbs: `ARCHITECTURE.md``
> `itself (the analysis layers' sections, the joint estimator's standing-rules section, document`
> `governance); every document `ARCHITECTURE.md` delegates to in a form the delegation-form rule`
> `admits; and `docs/scoring_model.md`.  This tool derives that set and publishes it whole.`

**The artifact is current at the seal.** `--check` was run and re-derived without drift:
`the specification document set re-derives / targets named 68; namings 199; admitted 25 / members
26; with no file 0 / seed misses 5 of 25`. `STATUS.md` is graded ADMITTED and then **excluded from
the member list** by the authored exclusion the user ruled on 2026-08-22 (Ruling 1(a) of
`cowork_rulings_2026_08_22_step_zero_return_sitting.md`), so it is not in this stratum.

**The 26 members, in the byte order that keys the sample:** `ARCHITECTURE.md`,
`cowork_bounded_context_design.md`, `cowork_confidence_contract.md`, `cowork_evidence_inventory.md`,
`cowork_idiom_entry_mapping.md`, `cowork_joint_estimator_architecture.md`,
`cowork_joint_estimator_factorization.md`, `cowork_layer1_note_model_design.md`,
`cowork_layer2_slicing_design.md`, `cowork_layer3_keymode_design.md`,
`cowork_layer4_chordsymbol_design.md`, `cowork_layer5_engagement_design.md`,
`cowork_layer5_function_design.md`, `cowork_layer6_grouping_design.md`,
`cowork_notation_adoption_increment.md`, `cowork_notation_output_contract.md`,
`cowork_phrase_boundary_design.md`, `cowork_prefit_gates.md`,
`cowork_progression_schema_design.md`, `cowork_progression_schema_dictionary.md`,
`cowork_score_census.md`, `cowork_stage5_fitter_design.md`, `cowork_target_architecture.md`,
`cowork_voiceleading_axis_design.md`, `docs/llm_integration.md`, `docs/scoring_model.md`.

**Two readings declared, because each moves `N`.**

- **Whole file, not the delegated sections.** Several members carry a `delegation_scope` of
  `sections` rather than `document` — `ARCHITECTURE.md` itself is scoped to three named regions. The
  reading taken is **every heading in the member FILE**, because the dispatch's unit is *"one
  markdown heading in a current member of the document set"* and the artifact's member field is the
  file path; the scope field governs how far a delegation REACHES, which is a different question.
  Under the narrow reading `ARCHITECTURE.md` would contribute only its three regions' headings and
  `N` would fall sharply.
- **Fenced code blocks are excluded.** A bare `^#{1,6} ` match also catches `#` comments inside
  fenced code blocks, which are shell comments and not markdown headings. **Fence-aware `N = 730`;
  naive `N = 737`.** The seven excluded lines are all in `ARCHITECTURE.md` and are all shell
  comments — `# Build`, `# Tests — run once, capture tail`, `# Python scripts`, `# Long corpus runs
  — use tee`, `# Then after completion:` (lines 896–907) and `# Full Bach corpus`, `# Single chorale
  for spot-checking` (lines 7794–7797). **The naive reading would have put two of those shell
  comments into the drawn sample** (at ordered positions 30 and 262), which is why the exclusion is
  taken and declared rather than left.

**How the count was established, on both sides.** The heading population was extracted from the
content-addressed git objects at the tip, and independently counted in the WORKING TREE with the
file tools: the two agree **per file and in total at 737 naive**, so the working tree and the tip
carry the same headings for all 26 members (no member is among the changed paths). Every one of the
25 drawn items below was then re-read from the working tree with the file tool at its own line and
matched verbatim.

**Ordering:** by path byte order, then line. **No two items are identical on the ordering keys** (two
headings cannot share a line). `N = 730 > T`, so `k = floor(730/25) = 29`; positions `1, 30, 59, 88, 117, 146, 175,
204, 233, 262, 291, 320, 349, 378, 407, 436, 465, 494, 523, 552, 581, 610, 639, 668, 697`.

### The 25 drawn items, verbatim, with `path:line`

| # | Position | `path:line` | The heading, verbatim |
|---|---|---|---|
| 1 | 1 | `ARCHITECTURE.md:1` | ``# MuseScore Arranger — Architecture Document`` |
| 2 | 30 | `ARCHITECTURE.md:1333` | ``## 3. Directory Structure`` |
| 3 | 59 | `ARCHITECTURE.md:2516` | ``#### Output — `ChordAnalysisResult` `` |
| 4 | 88 | `ARCHITECTURE.md:3580` | ``### Phase 1a — Validate Existing Chord-Symbol-Driven Path`` |
| 5 | 117 | `ARCHITECTURE.md:4601` | ``### 5.8 Known Analyzer Limitations`` |
| 6 | 146 | `ARCHITECTURE.md:5200` | ``#### §5.16.1 Declared Key-Signature Mode Override`` |
| 7 | 175 | `ARCHITECTURE.md:5988` | ``### 9.2 ConstraintStore`` |
| 8 | 204 | `ARCHITECTURE.md:6905` | ``#### Relationship to the Generalized Tuning Algorithm`` |
| 9 | 233 | `ARCHITECTURE.md:7483` | ``### 12.1 MuseScore Panel Integration`` |
| 10 | 262 | `ARCHITECTURE.md:7932` | ``### Core — Must Be Implemented`` |
| 11 | 291 | `cowork_bounded_context_design.md:201` | ``## 7. Architecture decisions (with alternatives)`` |
| 12 | 320 | `cowork_idiom_entry_mapping.md:50` | ``## Notes for the re-tag`` |
| 13 | 349 | `cowork_layer1_note_model_design.md:208` | ``## 10. Quality & testing`` |
| 14 | 378 | `cowork_layer3_keymode_design.md:286` | ``## 7. Data design`` |
| 15 | 407 | `cowork_layer5_engagement_design.md:54` | ``### §1.2 The selection machinery already built — `resolveCarriedReadings` [code]`` |
| 16 | 436 | `cowork_layer5_engagement_design.md:519` | ``### §7.4 The trigger: an annotation trigger, never an override lever `[contract §4]` `` |
| 17 | 465 | `cowork_layer5_function_design.md:709` | ``## 12. Glossary`` |
| 18 | 494 | `cowork_layer6_grouping_design.md:430` | ``## 15. Open items & deferred refinements`` |
| 19 | 523 | `cowork_phrase_boundary_design.md:33` | ``## 0. Terms (read first — nothing below uses a term before its row)`` |
| 20 | 552 | `cowork_progression_schema_design.md:112` | ``### 4.2 Substitutions`` |
| 21 | 581 | `cowork_score_census.md:13` | ``## 1. Why corpora kept being "discovered" — and the method that closes it`` |
| 22 | 610 | `cowork_stage5_fitter_design.md:807` | ``## 11. Risks & technical debt`` |
| 23 | 639 | `cowork_voiceleading_axis_design.md:412` | ``### 5.4 The staged components (named, scoped, design-gated — each gets its own design doc before build)`` |
| 24 | 668 | `docs/llm_integration.md:272` | ``### 4.1 Score Reader`` |
| 25 | 697 | `docs/llm_integration.md:773` | ``### The two plugin API tiers, for reference`` |

The same twenty-five, one per line and outside a table, so that no character of any of them depends
on table escaping:

```
ARCHITECTURE.md:1                             # MuseScore Arranger — Architecture Document
ARCHITECTURE.md:1333                          ## 3. Directory Structure
ARCHITECTURE.md:2516                          #### Output — `ChordAnalysisResult`
ARCHITECTURE.md:3580                          ### Phase 1a — Validate Existing Chord-Symbol-Driven Path
ARCHITECTURE.md:4601                          ### 5.8 Known Analyzer Limitations
ARCHITECTURE.md:5200                          #### §5.16.1 Declared Key-Signature Mode Override
ARCHITECTURE.md:5988                          ### 9.2 ConstraintStore
ARCHITECTURE.md:6905                          #### Relationship to the Generalized Tuning Algorithm
ARCHITECTURE.md:7483                          ### 12.1 MuseScore Panel Integration
ARCHITECTURE.md:7932                          ### Core — Must Be Implemented
cowork_bounded_context_design.md:201          ## 7. Architecture decisions (with alternatives)
cowork_idiom_entry_mapping.md:50              ## Notes for the re-tag
cowork_layer1_note_model_design.md:208        ## 10. Quality & testing
cowork_layer3_keymode_design.md:286           ## 7. Data design
cowork_layer5_engagement_design.md:54         ### §1.2 The selection machinery already built — `resolveCarriedReadings` [code]
cowork_layer5_engagement_design.md:519        ### §7.4 The trigger: an annotation trigger, never an override lever `[contract §4]`
cowork_layer5_function_design.md:709          ## 12. Glossary
cowork_layer6_grouping_design.md:430          ## 15. Open items & deferred refinements
cowork_phrase_boundary_design.md:33           ## 0. Terms (read first — nothing below uses a term before its row)
cowork_progression_schema_design.md:112       ### 4.2 Substitutions
cowork_score_census.md:13                     ## 1. Why corpora kept being "discovered" — and the method that closes it
cowork_stage5_fitter_design.md:807            ## 11. Risks & technical debt
cowork_voiceleading_axis_design.md:412        ### 5.4 The staged components (named, scoped, design-gated — each gets its own design doc before build)
docs/llm_integration.md:272                   ### 4.1 Score Reader
docs/llm_integration.md:773                   ### The two plugin API tiers, for reference
```

---

## 8. Stratum 8 — every heading ever deleted from the document set — **TAKE, N = 59, k = 2**

**Defining object: the same 26-member document set as §7, plus the repository's history walked from
the explicit tip** `0e7186a961f50b32e0552483b289b11069f1319a`. The stratum's wording is the same
successor-plan sentence quoted at §7; Ruling 1 of `cowork_rulings_2026_08_26_framework_opening_sitting.md`
is why this side enumerates it, in that ruling's own words:

> The population is large, scattered and history-dependent — every current heading, every heading
> ever deleted from the document set, the ruling records, the decision surfaces, the dossiers, the
> deferred entries of the decisions register, the evidence inventory and the declared dormancies —
> and enumerating the deleted half requires the repository's history.

**How it was enumerated.** For each member, every commit that changed it was listed from the
explicit tip hash (**279 commits across the 26 members**), and every one of those versions was read
from its content-addressed git object. Walking newest to oldest, a heading present in a version and
absent from its successor **and absent at the tip** is a deleted heading; its recorded line is its
line in the last version that carried it, and its deleting commit is the version in which it first
does not appear. **`N = 59`**, fence-aware on the same rule as §7 (the naive count is 60; the one
extra is `# Full corpus` at `ARCHITECTURE.md:2523` in a historical version, a shell comment inside a
fenced block).

**Two readings declared.**

- **"Absent at the tip" is read per member**, not across the document set: a heading that moved from
  one member to another counts as deleted from the first. The unit's own wording — *"present in an
  earlier commit of a document-set member and absent at the tip"* — is what this follows.
- **A heading deleted, reintroduced and deleted again is carried once**, at its latest presence.

**Ordering:** by path byte order, then the line in its last version, then the deleting commit hash
lexicographically. **The third ordering key is load-bearing here and was needed:** three items share
`ARCHITECTURE.md` line 635 and are separated only by their deleting commits. **No two items are
identical on all three ordering keys.** `N = 59 > T`, so `k = floor(59/25) = 2`; positions `1, 3, 5, … 49`. Positions 51–59 of
the ordering cannot be drawn.

### The 25 drawn items, verbatim, with their provenance

Each row: the ordered position; the member; the line it stood at in the last version that carried
it; the commit that deleted it; then the heading verbatim on its own line.

```
pos  1 | ARCHITECTURE.md | line 68   | deleted at a3ac7b00cfe2524652b07297a19be8ff00ba7e6e
### 1.4 Current Status

pos  3 | ARCHITECTURE.md | line 240  | deleted at 6152ad83fa503c38e2cab8326f4524499f8c2534
### 2.11 Cross-Platform by Default

pos  5 | ARCHITECTURE.md | line 466  | deleted at 70e679e819e986ca93df0fd347f7a95dc827a626
#### Modal Infrastructure

pos  7 | ARCHITECTURE.md | line 597  | deleted at 632c195294d019639f646c15a179c18a8e8988b5
#### Layer 1 — the lossless note model (note-model rebuild, 2026-06-21, as-built)

pos  9 | ARCHITECTURE.md | line 635  | deleted at 70e679e819e986ca93df0fd347f7a95dc827a626
#### Current Gaps in the Calling Code

pos 11 | ARCHITECTURE.md | line 667  | deleted at 9b643a454af07f688ed54673b90eec08b8791526
#### Region Analysis — Canonical Modules (Iter 97, complete; note-reading half superseded by Layer 1)

pos 13 | ARCHITECTURE.md | line 688  | deleted at 70e679e819e986ca93df0fd347f7a95dc827a626
### 5.2 Connecting KeyModeAnalyzer to ChordAnalyzer

pos 15 | ARCHITECTURE.md | line 746  | deleted at 632c195294d019639f646c15a179c18a8e8988b5
#### Layer 4 — the per-slice chord-symbol decoder (2026-06-28, as-built, **DORMANT** — engages with L5; final commit `1e74f21ea4`)

pos 17 | ARCHITECTURE.md | line 792  | deleted at a3ac7b00cfe2524652b07297a19be8ff00ba7e6e
#### Remaining Gap in the Calling Code

pos 19 | ARCHITECTURE.md | line 811  | deleted at a1017528616f16d9e2b8f8e2e08881d42b18fc38
#### Technical debt — duplicate note collection paths

pos 21 | ARCHITECTURE.md | line 825  | deleted at 70e679e819e986ca93df0fd347f7a95dc827a626
### 5.7 Normalized Confidence Scores

pos 23 | ARCHITECTURE.md | line 928  | deleted at 7f84dca71d03659d02052667b06cfcfc38a988ee
##### Accumulated-note analysis (optional)

pos 25 | ARCHITECTURE.md | line 1118 | deleted at 7a534ac45f55d6725d792d17f06431b850e6a00a
#### Relationship to current jazz mode

pos 27 | ARCHITECTURE.md | line 1150 | deleted at 7a534ac45f55d6725d792d17f06431b850e6a00a
##### Problem

pos 29 | ARCHITECTURE.md | line 1190 | deleted at 7a534ac45f55d6725d792d17f06431b850e6a00a
##### Jazz boundary extraction

pos 31 | ARCHITECTURE.md | line 1236 | deleted at ab336f43b5e5610077488117a8a3a1ea32cec440
#### Layer 3 — key/mode is the sequence decoder (Built+Live)

pos 33 | ARCHITECTURE.md | line 1268 | deleted at 7a534ac45f55d6725d792d17f06431b850e6a00a
##### Files to touch

pos 35 | ARCHITECTURE.md | line 1290 | deleted at ab336f43b5e5610077488117a8a3a1ea32cec440
#### Layer 4 — the per-slice chord-symbol decoder (Built+Dormant — not wired; engages with L5)

pos 37 | ARCHITECTURE.md | line 1466 | deleted at 70e679e819e986ca93df0fd347f7a95dc827a626
#### Two note-collection modes

pos 39 | ARCHITECTURE.md | line 1971 | deleted at 70e679e819e986ca93df0fd347f7a95dc827a626
## Platform Support Requirement

pos 41 | ARCHITECTURE.md | line 2594 | deleted at 7a534ac45f55d6725d792d17f06431b850e6a00a
#### Order-of-annotation safety guarantee

pos 43 | ARCHITECTURE.md | line 3043 | deleted at 632c195294d019639f646c15a179c18a8e8988b5
#### Active follow-up plan (2026-04-10)

pos 45 | ARCHITECTURE.md | line 8153 | deleted at bf48b1f834afe7b0b71da7473b373e37549e99ea
### 19.4 Implementation phases

pos 47 | cowork_evidence_inventory.md | line 206 | deleted at 0922e2bfdcd72563b05f8754e7c1e67eb0136718
## 8b. A declared future consumer, named by the user (2026-07-13)

pos 49 | cowork_layer6_grouping_design.md | line 81 | deleted at d39da15d9558b5ff770630c0ed6e2e4108f3f264
### 5.1 Phrase segmentation
```

---

## 9. What is sealed, and what is not

**Sealed here:** the drawn items of strata 4, 5, 7 and 8 — 21 + 25 + 25 + 25 = **96 items**.

**Not sealed:** strata 1, 2, 3 and 6, each STOPPED at §§1, 2, 3 and 6 above. **The frame is not
authored until the user has ruled on every one of them.**

**Every item above is rendered verbatim.** No item could not be rendered verbatim, so the dispatch's
provision for recording such a case is unused.

*Drawn and sealed by Claude Code under `cc_instruction_placement_sample.md`, 2026-08-27, at branch
tip `0e7186a961f50b32e0552483b289b11069f1319a`. The selection rule is the writing side's, authored
before any count was known. The drawing side chose no item, added none, removed none and reordered
none.*

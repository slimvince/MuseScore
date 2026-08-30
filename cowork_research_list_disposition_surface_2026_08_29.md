# Disposition surface — the external research list against the framework decomposition (first reading)

> **Reading surface (Cowork writing side, 2026-08-29).** Preparation for the ratification sitting
> that `cowork_framework_document_draft_2026_08_28.md` §1.4 requires: the framework decomposition is
> ratified only after the user's external list of published research has arrived and been
> **dispositioned against it**. The list arrived 2026-08-28 at
> `external resarch summary/external research.xlsx` (the folder name's spelling as it stands) and was
> read whole by this side. **This surface presents the dispositions for the user to rule on. It rules
> nothing, changes no document, and creates no register entry.** The choice questions are put
> separately, one decision per turn, after this surface is read.
>
> **Provenance discipline.** The workbook grades its own rows — RECOVERED (from a lost prior
> conversation), SOURCE-ENRICHED, PRIMARY-DEEP-READ, DISCOVERY-SWEEP — and its own standing rule is
> that partially-verified items are not established facts. This surface honours that and adds our
> own: a workbook claim is cited here as *the list reports*, never as established; **anything a
> ruling would put load on needs the primary source read on our side first** (guiding principle #1:
> a citation to a paper nobody read is not a fact basis). Where this surface says a design point is
> *supported*, the meaning is: the list's reported evidence points the same way as the framework's
> recorded ground — it is corroboration of direction, not new establishment.
>
> **Identifier convention, fixed here for every later citation.** The workbook's own identifiers
> (D001…, R001…, E001…, AF001…) collide with this project's register namespaces. A workbook row is
> cited as **[list: <sheet>, <row-ID>]** — for example [list: Research, R120] — and its identifiers
> are never imported bare.

---

## 1. The overlap with what the derivation already weighed, established at the source register

The framework was derived from, among other sources, **all fifty-eight PDFs at
`docs/research_papers/`** (its Appendix A.2). That folder's `BIBLIOGRAPHY.md` was read whole by this
side on 2026-08-29 and compared against the list. The result:

**A large share of the list's core is already inside the derivation's sweep** — among others:
Temperley and the preference-rule line, Pardo & Birmingham, Raphael & Stoddard's joint
harmony-and-tonality models, Masada & Bunescu's segmental model and the semi-Markov formalism
behind it, the Rohrmeier grammar line (the 2011 paper and the generalized parsing framework), the
Chen & Su papers, AugmentedNet, Micchi 2020, ChordGNN, RNBERT, AnalysisGNN, the cadence work (Bigo
2018; Karystinaios & Widmer 2022), the pitch-spelling line, Ju 2017 on non-chord-tone
identification, and the whole ground-truth family — TAVERN, ABC, the Mozart sonatas, When-in-Rome,
Dilemmadata, the annotator-subjectivity literature, BCMH. **For all of these, the list corroborates
the derivation's inputs rather than adding to them**, and its per-row primary-source checks (many
with "full paper checked" status and URLs) are useful independent confirmation that those inputs
say what the framework reports them saying.

**What the register does NOT contain, and the list does — the genuinely new classes:**

1. **The McLeod & Rohrmeier family.** The 2021 modular six-component harmonic analyzer (1,540
   spelled chords, 70 tonality states, beam-search joint decoding) with its **public implementation
   that takes MusicXML in and writes annotations onto MuseScore3 files** [list: Research, R120–R128];
   the 2024 chord-alteration/suspension work [list: Research, R132]; the 2021 unified chord model
   [list: Research, R133]; and the 2022 graded chord-evaluation metrics with the open `chord-eval`
   toolkit [list: Research, R134–R135]. *(The framework's §14 names an unnamed "reference joint
   model" over tonic, mode and chord; whether that is this system or another cannot be established
   from the framework's text, which names no papers — the register's candidates are Raphael &
   Stoddard and Temperley 2009. Established either way: McLeod & Rohrmeier appears nowhere in
   `BIBLIOGRAPHY.md`.)*
2. **The executable grammar and ontology branch.** HarmTrace (error-correcting parsing of chord
   sequences into functional trees, style grammars, the measured lesson that unrestricted
   modulation rules explode the parse space) [list: Research, R200–R204]; the Functional Harmony
   Ontology [list: Research, R180–R183]; the Modal Harmony Ontology with all seven modes formalized
   and multiple modal interpretations returned per progression [list: Research, R170–R173]; the
   representation ontologies (Polifonia, ChoCo, Music/Chord Ontology). This is the class the
   framework's own R-7 declares unreachable by construction — *work not using this vocabulary*.
3. **The mode branch.** Four-mode symbolic detection on Irish traditional music at roughly 80%
   reported accuracy, with Phrygian, Lydian and Locrian explicitly named under-researched [list:
   Research, R110–R111]; relative mode as a continuum [list: Research, R113]; and the list's two
   synthesized gap findings — **no mature general seven-mode symbolic inference, and mode-specific
   functional harmony a larger gap still** [list: Research, R116–R117]. Plus two concrete
   representation facts: the DCML standard's modal collapse as the list reports it, and the Distant
   Listening Corpus's own documentation of `e.phrygian` breaking the standard's grammar [list:
   Research consolidation, EB310].
4. **Recent and multilingual items** — BACHI (boundary-aware symbolic chord recognition, ICASSP
   2026, public code); the Nápoles López 2020 local-keys/modulations/tonicizations evaluation
   methodology; Hu & Arthur 2021; the German and French research branches (the Saarland project,
   the Lille thesis) — the *non-English* and *not yet indexed* classes R-7 names.
5. **Historical lineage detail** (Winograd's need for manual segmentation and non-chord-tone
   removal, Maxwell's rule system, Cochonut/Funchal, Kostka-Payne) — low load, useful colour.

**Consequence stated plainly: the list partially discharges R-7** — the framework's declared risk
that its literature is not coverage — in exactly the classes R-7 names, and what it found there
**overturns no chosen design point** (§3 below). R-7's specifically named unread alternatives
(multi-resolution tonality, time-span reduction trees, tonality in a transform space) are **not**
in the list either; R-7 is narrowed, not closed.

---

## 2. Dispositions per design point of the framework's §9

Verdict vocabulary: **SUPPORTS** — the list's reported evidence points the same way as the recorded
ground; **ENRICHES** — new material that bears on the point without changing its evidence balance;
**RIVAL-SHAPED** — reported evidence a ruling should look at before ratifying; **NO BEARING**.
Nothing below reaches CONTRADICTS: **no chosen design point of the framework meets a falsifier in
the list.**

- **DP-A (do not divide the deciding by published field) — SUPPORTS.** New, independent: the modular
  system's own authors report that their key inference inherits errors from other modules and that
  an end-to-end baseline avoids this [list: Research, R122; McLeod-Rohrmeier deep read, MR015]; the
  1968 system's functional grammar was strong while segmentation and non-chord-tone removal had to
  be done by hand [list: Research consolidation, EB209]. Same direction as the multi-task
  pathologies the framework already carries.
- **DP-B (no tonality-first pipeline) — SUPPORTS.** Raphael & Stoddard's joint model is already in
  the register; the list adds the task-ordering question as its own research object (the
  When-implies-What line) and the modular system's conditional, error-inheriting key stage.
- **DP-C (segmentation decided with chord identity) — SUPPORTS, plus one new comparable.** The
  semi-Markov evidence is already weighed. New: **BACHI** as a 2026 boundary-aware decoder — a
  benchmarking comparable for the measurement phase, not framework input.
- **DP-D (chord-tone assignment part of the one decision) — the one RIVAL-SHAPED item, and on a
  careful read it resolves to ENRICHES.** The 2024 McLeod & Rohrmeier work classifies each note as
  chord or non-chord tone and derives suspensions and added notes **after** chord segmentation,
  root and quality are fixed, works under noisy upstream labels, and outperforms a strong heuristic
  baseline [list: Alterations & suspensions deep read, AS001–AS010]. That looks like a measured
  counter-design to deciding assignment jointly. **Its own stated scope is what defuses it:** the
  method assumes the segmentation and the basic chord already known [AS010], so it does not answer
  the framework's ground for the entanglement — that the discriminating information for an
  elaboration lives in the boundary placement (ledger C27) and that the chord label is a function
  of the elaboration reading (the analyst's own note). What it IS strong evidence for: deriving the
  **type** of an elaboration after the decision (which is where the framework and the incumbent's
  ruled emission design already put it — R-4 assigns the type to L2, published beside the
  assignment), a compact base vocabulary with alterations derived rather than a flat thousand-label
  space [AS002, AS009], and a two-stage training route for rare chords — all **L2
  detail-specification material**. *Put to the user because it is the closest thing to a rival in
  the whole list; the recommendation is that it changes the cut not at all and enriches the detail
  phase considerably.*
- **DP-E (tonality decided with the chords; changes at harmonic boundaries) — SUPPORTS.** The
  modular system represents applied chords as brief, recursively embedded tonality changes [list:
  McLeod-Rohrmeier deep read, MR003] — an existence proof that secondary function can be carried by
  tonality transitions rather than a separate label, which also bears on Δ4.
- **DP-F/G/H (spelling, meter, voice separation not layers for notated input) — SUPPORTS.** The
  list's spelling and meter research is about *inferring* what our input *gives* (its own rows say
  so), the modular system reads spelled input as we do, and the corpus-quality warning about MIDI's
  ambiguous spelling [list: Discovery sweep 3, DS310] supports C-1's notation-input constraint.
- **DP-I (cadence cues at L1, type at L3) — ENRICHES.** The graph-network cadence line is already
  in the register; the list adds no evidence against the measured authentic/half asymmetry the
  split rests on.
- **DP-J (phrase boundaries are not harmonic boundaries) — SUPPORTS.** The list's phrase material
  adds the boundary-versus-formal-function distinction [list: Phrase-form deep read, PF007], which
  the framework's L3 charter also draws.
- **DP-K (publish rivals with mass, including segmentation-differing) — SUPPORTS strongly.** The
  beam decoder retains multiple chord/tonality hypotheses with configurable pruning [list: McLeod
  code deep read, MC008]; the ontology returns several modal interpretations of one progression
  rather than forcing one [list: Lazzari deep read, LM006–LM007]; the meta-corpus explicitly
  rejects a universal ground truth [list: Research consolidation, EB303]; TAVERN preserves
  annotator disagreement with adjudication [EB305]. All the same direction as the ground truth's
  published variants.
- **DP-L (the chord symbol is a derivation, published as a view) — SUPPORTS, with a representation
  candidate.** The unified chord model [list: Chord model deep read, CM001–CM010] — spelled,
  generic and enharmonic pitch classes as distinct types with equivalences as explicit
  transformations, never destructive normalization; mode as a first-class interval collection
  including Phrygian and Hypodorian — is a **new candidate reference for §7's data design at the
  detail phase**, congruent with C-5 and the establishment-status rule.
- **DP-M / §8.4 (narrow revision) — NO BEARING** beyond HarmTrace's error-tolerant parsing, which
  is candidate-admission robustness (L2 detail), not revision.
- **DP-N (cadential six-four — underived, open) — no decisive input.** The list carries no evidence
  choosing among the three theoretical readings. One mitigation for later: graded chord-distance
  evaluation [list: Evaluation deep read, EV001–EV005] reduces the measurement cost of whichever
  label vocabulary is ruled. **Stays open.**
- **DP-O (hierarchy — underived, open) — ENRICHES substantially; stays open.** The list supplies
  what the grammar branch looks like when executed: parse trees built automatically over chord
  sequences, error-correcting parsing, style-specific grammars, and the measured tractability
  lesson that unrestricted modulation rules explode ambiguity [list: HarmTrace deep read,
  HT006–HT009; Rohrmeier grammar deep read, RG012]. It also exhibits a placement option the
  framework's text already admits: hierarchy as a downstream analysis over the settled reading. The
  falsifier DP-O states — a tree model beating a matched-capacity sequence model on this
  repertoire's ground truth — **is not supplied by the list**, so the point stays open, now with
  named systems to test if the falsifier is ever run.
- **DP-P (how L2's candidate score is formed and fitted — deferred to detail specification) —
  ENRICHES that later phase** (two-stage training for rare chords; graded evaluation; the
  vocabulary-explosion argument).
- **DP-Q (may the analysis decline to read — underived, open) — mild SUPPORT for representable
  abstention** (the list's own principles P3/P10 put insufficient evidence and unforced answers
  first-class), no decisive input. **Stays open.**
- **§9.0 (a unit is a decision) — already ruled 2026-08-28; the list is consistent with the
  ruling** — its inventories and information model are organized around interpretive objects and
  decisions, and its factor-like content appears as methods for computing them.

---

## 3. Dispositions for the held and open differences of Appendix A.4

- **Δ2 — decomposition by question versus by evidence-source-times-question (gradable since the
  §9.0 ruling, not decided): the list SUPPORTS the derived side.** The strongest items are the
  modular system's own authors on module error inheritance [MR015], the joint-modelling framing of
  the thesis line, the root/non-chord-tone circular dependency stated as such in the literature
  [list: Discovery sweep 2, DS206], and the 1968 lesson [EB209]. Nothing in the list supports
  assembling one question's answer across stages.
- **Δ3 (rivals differing in segmentation) and Δ5 (merge-equal retired) — held under §1.4; this
  sitting is where the holds resolve. The list ENRICHES the ambiguity case and adds one honest
  caution:** no system the list surveys *publishes* rivals that differ in segmentation — the beam
  decoder holds them during search and commits one. Adopting Δ3 therefore goes beyond surveyed
  published practice; **the decisive evidence remains the ground truth's own published variant with
  a different number of chords**, which no list item weakens. The §10 fill-in's finding stands
  beside it: the capability is absent from the incumbent by construction.
- **Δ4 (the Roman numeral is not a separate decision) — SUPPORTS, with a nuance recorded fairly.**
  The applied-chords-as-tonality-changes representation [MR003] shows function carried without a
  separate functional field. The downstream functional systems (HarmTrace, the Functional Harmony
  Ontology) *do* decide function separately — but over bare chord-symbol sequences with the
  tonality assumed known, without note evidence; given a settled tonality and chord, their input is
  what the framework's settlement already IS, so they are not counter-evidence to Δ4.
- **Δ6 (the elaboration type belongs to L2, derived beside the assignment) — SUPPORTS.** The 2024
  alteration work is a measured route for exactly that derivation.
- **Δ7 (what earns a layer) and Δ8 (where the forward-override is permitted) — NO BEARING.** The
  list's sixty-odd "candidate areas" are research problems, not runtime units, and it carries
  nothing on confidence-scale commensurability.

---

## 4. The one genuinely NEW QUESTION the list raises, and where it routes

**Mode.** The list's sharpest original content: general seven-mode symbolic inference has no mature
system; mode-specific functional harmony is a larger gap; the annotation standard this project
grades against collapses modes into major and minor, and its own corpus documentation shows a
Phrygian tonality breaking the standard's grammar; mode may also be treatable as a continuum. The
list's design principle P8 — tonal centre and mode representable independently, not collapsed for
convenience — presses on this project at three ruled places: the framework's definition of tonality
as tonic plus mode (which leaves the mode *vocabulary* open), the incumbent's ruled two-mode joint
state with modal colour in the emission and the un-rounded reading published, and the ruled grading
convention that reduces an exotic-mode emission to its parent collection's minor tonality.

**Disposition proposed: this is not a framework-cut question.** The decomposition is
mode-vocabulary-agnostic — nothing in the layer cut, the charters or the contracts changes if the
mode set changes. It routes to three later homes: **L2's detail specification** (what the tonality
axis's mode vocabulary is, where the ruled two-mode state and the published modal colour meet this
evidence), **measurement design** (what mode ground truth even exists — the list's own finding is
that corpus labels are the bottleneck), and **the style system** (modal repertoires as idioms).
Recorded now so the question has a place and is not re-derived; decided in those phases.

---

## 5. Routed forward — bearing on later phases, not on this sitting

- **Measurement design:** the graded chord-distance metrics and open toolkit; the
  local-keys/modulations/tonicizations evaluation methodology; the reported finding that
  non-chord-tone ground truth is itself sometimes ambiguous; TAVERN's preserved disagreements and
  adjudication — the last also bearing on the standing ground-truth-ceiling obligation (OI-179),
  whose design surface already holds TAVERN's duplicates open as a computable route.
- **Corpus intake:** the list's dataset sheet enters under the ruled intake discipline — research
  material on entry, never the gate; overlap with the gate corpus record-only without a ruling.
- **Comparables for later benchmarking:** the McLeod & Rohrmeier implementation (GPL-3.0 —
  licence-compatible on its face; verified before any use), AugmentedNet v1.9.1 (the thesis
  version, which its repository recommends over the 2021 paper's), BACHI, HarmTrace. Prior art for
  comparison at the audit and measurement phases; none is input to the framework.
- **Intake mechanics, when the dispositioning is executed into the record:** the citation
  convention of §0; and, only if anchored citations prove necessary, a mechanically generated text
  extraction beside the workbook — the workbook itself never edited.

---

## 6. The recommended order for the sitting, one decision per turn

1. **Ratify the decomposition, or amend it** — the §1.4 hold's own question, now that the list is
   dispositioned: no chosen design point meets a falsifier; the one rival-shaped item (DP-D)
   resolves on its own stated scope; the underived points stay open as the output form allows.
   Ratification releases the holds on Δ3 and Δ5 (both already agreed in principle) and is the
   natural moment to rule Δ2, whose evidence is one-sided in the list.
2. **Rule the DP-D question explicitly** — that the 2024 alteration evidence changes the cut not at
   all and is admitted as detail-specification input. Put separately because it is the list's only
   rival-shaped item and should not ride silently inside ratification.
3. **Route the mode question** as §4 proposes — a placement ruling, not a design ruling.
4. **Note for the record** that R-7 is narrowed as §1 states, and that the list's remaining
   verification debt (its RECOVERED tier) binds any later load-bearing use.

The choice questions for these will be delivered as user-visible text, one per turn, when the user
takes the sitting.

---

## Provenance

Cowork writing side, 2026-08-29. Read at the objects this session through the file tools on
bridge-staged snapshots: the workbook whole (all twenty-one sheets, dumped to text and read in
full); `cowork_framework_document_draft_2026_08_28.md` §0–§14 and Appendix A.1–A.5 (the sealed
files and Appendix B not opened); `docs/research_papers/BIBLIOGRAPHY.md` whole;
`cowork_rulings_2026_08_28_framework_delta_sitting.md` whole (earlier this session);
`EMPIRICAL_FINDINGS_LEDGER.md` at the entries cited. The framework document's modification time was
re-established unchanged before this surface was written. **No shell command of any kind was run on
the repository and no git object was resolved.** Workbook claims are relayed at the workbook's own
verification grades and are marked so; nothing here establishes a published result at the primary
source. This side is barred from authoring the framework document and this surface authors none of
it.

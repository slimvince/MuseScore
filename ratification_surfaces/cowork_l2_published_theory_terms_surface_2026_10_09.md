# The L2-S39 family — terms taken from published theory — ratification surface, 2026-10-09

> **STATUS: RATIFICATION SURFACE, §A AND ITS CHECK §B.** *(Former wording, preserved (#12): "§A ONLY". §B added on
> the user's "continue".)* Cowork, 2026-10-09 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_twenty_six.md`. Written as text, nothing asked in the
> turn that delivers it. The check (§B) comes in a later turn, and the questions after that, one per turn. Nothing here
> is applied, and no tracked document is edited. Marks: *checked* = read at the object by this sitting; *relayed* =
> taken from another record and not re-read here; *my reading* = this side's interpretation.

---

## §A.1 What this family is

The derived statement, whole (*checked*, `cowork_blind_derivation_l2_2026_09_27.md`, its lines 967–984):

> **L2-S39. A distance or profile taken from published theory (Lerdahl's tonal pitch space, Weber's
> table, a scale-degree profile) enters the candidate score as a feature whose single weight is fitted.
> Its internal constants are the published ones, unchanged, and are not tuned on evaluation music.**
> - *Defense.* Fitting a published theory's internal constants would make the theory a fitted table, and
>   its establishment would then rest on the fit, not on the theory [RULED — principle #19]. Keeping them
>   fixed and fitting one weight keeps the capacity small and the provenance of each part separate. The
>   published systems that use these distances hand-set their exponents "after experiment" (1.1 and 1.01)
>   [FACT (relayed, 08) — Rocher et al. 2010, §2.3] or set normalisers from stated presumptions [FACT
>   (relayed, 08) — Catteau, Martens & Leman, p. 14]. Both are uses of evaluation-adjacent data or
>   presumption that the rule above excludes.
> - *Source class.* Derived.
> - *Status.* Settled.
> - *Premise.* The published constants are good enough in shape that a single weight suffices.
>   **False-negative path:** a distance whose shape is wrong for this repertoire. The fitted weight tends
>   toward zero, and the fix is a different published space, ruled, not a tuned one.
> - *Falsifier.* CODE. **Observable:** the fit's parameter list. **Decision rule:** falsified if any
>   internal constant of a published distance is a fitted parameter. **Not falsified by:** choosing
>   between two published spaces by held-out comparison.

No open question names L2-S39 (a search of the derivation for "L2-S39" finds only its own line, 967). It is tied to
OQ-L2-3 (the measured shapes and values), whose last item is "the choice between Lerdahl's and Weber's tonal spaces"
(*checked*, derivation lines 1210–1213).

**In plain words.** Some of what L2 weighs comes ready-made from music theory: a measure of how far apart two
tonalities are (Lerdahl's tonal pitch space; Weber's 1817 table of key relationships), or a profile of how much each
scale degree belongs to a tonality. L2-S39 says how such a thing enters L2's scoring: the theory's own numbers are
used exactly as published, and L2 learns only one number for it — how much weight it gets beside everything else.
Nobody adjusts the theory's numbers to make L2 score better. If the theory's shape is wrong for the music, its weight
goes towards zero and a different published theory is tried; the theory is not reshaped by hand.

**What the family holds — 10 row-parts in all:**
- **§7's list for L2-S39** (*checked*, the comparison file `ratification_surfaces/cowork_comparison_l2_reading.md`,
  its lines 71239–71242): 8 AGREES (Rows 1.1(i), 1.2(i), 9.160(i), 10.16(i), 17.1(iii), 21.1(i), 43.39(i), 48.4(i)) and
  1 DIFFERS (Row 10.28).
- **Taken in on subject (1)** — this side's cut, which the user may change: **Row 48.6** (THE DERIVATION IS SILENT,
  proposed ADOPTED — proposed; comparison lines 63338–63347). Its axis note names L2-S39 in terms: "L2-S39 fixes how a
  published theory's term enters; neither it nor L2-S38 speaks to a term with no theoretical form." It is the other
  half of the rule Row 1.1(i) states.

Where the rows come from (*checked*, the comparison file's member headings): Row 1.x is `ARCHITECTURE.md`'s section
*"The joint estimator — the standing rules of the production inference layer"* (line 367); 9.x
`cowork_stage5_fitter_design.md` (17025); 10.x `cowork_joint_estimator_factorization.md` (22233); 17.x
`ARCHITECTURE.md`'s opening block (27168); 21.x `ARCHITECTURE.md` §2 *Architectural Principles* (29088); 43.x
`cowork_target_architecture.md` (55754); 48.x `cowork_joint_estimator_architecture.md` (63219). Three of the rows lie
inside the homes of decisions ruled L2's own and carry the comparison's mark WITHHELD: Row 1.1 (D-096), Row 17.1
claims (i)–(iii) (D-001), Row 21.1 (D-531). *(§B item 1. Former wording, preserved (#12): "Four of the rows".)*

---

## §A.2 The research, searched before writing (entry 319 §2)

- **`docs/research_papers/BIBLIOGRAPHY.md`** (*checked*, its header lines 1–18 and a search for Lerdahl, Weber,
  Krumhansl, Temperley, Octave, profile and the systems below): **neither Lerdahl's *Tonal Pitch Space* nor Weber's
  1817 table has a row.** Krumhansl's *Cognitive Foundations of Musical Pitch* (1990) has a row with no local copy
  (line 23, PAYWALL). Temperley's "A Bayesian Approach to Key-Finding" (2002) is held (line 19). The systems that use
  the two named spaces are held: Rocher et al. 2010 (line 41), Catteau, Martens & Leman 2006 (line 42, PAYWALL, a
  copy marked held), Feisthauer et al. 2020 (line 44), Noland & Sandler 2006 (line 40).
- **So the two spaces L2-S39 names reach the record only at second hand**, through the extracts of the papers that use
  them (`reading_pass/extracts/`, located at a listing): the Rocher extract states Lerdahl's distance as the paper uses
  it, "`δ(x → y) = i + j + k`", with two exponents set "After experiment" to 1.1 and 1.01 (its lines 70–79, *seen in
  search results*); the Catteau extract records the transition distances as "Lerdahl's, taken from published theory and
  not fitted", a printed table of distances between tonalities (Table 2, p. 8), and normalisers resting on the stated
  presumption "that a modulation is as hard as moving three times from one chord to another" (its lines 85–111, *seen
  in search results*); the Feisthauer extract records Weber's table chosen over the circle of fifths "because Mozart
  often switched between Major and minor modes of the same key", with the authors' caveat that it "seems to be relevant
  mostly for the classical period" (its lines 116–127, *seen in search results*). The Rocher and Catteau passages
  agree with the two quotations L2-S39's defense relays; the Feisthauer passage is relayed in L2-S34's defense, not
  L2-S39's. *(§B item 2. Former wording, preserved (#12): "These three agree with L2-S39's relayed defense quotations
  at the points quoted.")*
- **Under the theory-grounding corollary to #1/#2 (D-473), no equation is carried out of a text not fetched.** L2-S39's
  phrase "the published ones, unchanged" therefore cannot be met from what is held: a published space or profile that
  enters under L2-S39 needs its primary fetched and read first. This is the same bound the structural-bass record carried
  for the Rule of the Octave (*checked*, its lines 121–123: "a published form entering under L2-S39 needs one fetched
  and read first"). It is a bound for the research iteration ruled on 2026-10-07 and for measurement design, not a
  question (§A.6).
- **A measured comparison bearing on Row 10.28, read whole at its extract** (*checked*,
  `reading_pass/extracts/noland-sandler-2006-key-estimation-using-a-hidden-markov-model.md`, a first-pass extract read
  at the paper's page images by an earlier sitting; this sitting did not open the paper). Noland & Sandler build a
  key-change table from a published key-distance measure — Krumhansl's key-profile correlations, offset and normalised
  — and then, in some runs, re-fit it. Their Table 1 (as the extract reproduces it): 87% of 110 songs' keys correct with
  nothing trained; 91% with the key-change table re-fitted. **What this does and does not show** (*my reading*): it is a
  published instance of the two forms Row 10.28 sets against each other — a table taken from a published measure, and
  the same table fitted to music, though fitted by unsupervised estimation rather than counted from annotated changes
  as Row 10.28's is — and the fitted one scored higher; but the re-fit was made **per song, unsupervised, on the
  song being decoded**; the corpus is popular music and the task is the overall key only; and the extract reports no
  uncertainty for the 4-point difference, so under #24 it is not a finding. *(§B items 3 and 4. Former wordings,
  preserved (#12): "a published instance of exactly the two forms … a table from published theory, and a table fitted
  to music"; "the paper gives no uncertainty".)* It shows the question is live; it does not
  settle it.
- **The published spaces disagree about which tonality change is nearest** (*relayed*, from two extracts' own
  findings): in Krumhansl's correlations as Noland & Sandler print them, C major's nearest key is A minor, its relative
  (Noland extract, finding (2), lines 254–262, *checked*); in Lerdahl's space as Catteau et al. apply it, the relative
  major/minor is at distance one, "the cheapest tonality change there is", tied with the moves to the dominant and
  subdominant ("distance 1, the same as C major → F major or → G major"; Catteau extract, finding (5), lines 308–312,
  *checked*). *(§B item 5. Former wording, preserved (#12): "the relative major/minor is at distance one, the nearest
  possible change (Catteau extract, line 308–310, *seen in search results*)".)*
  The legacy D-347 put a large extra penalty on exactly that pair. *My reading:* this is one reason to let the music
  set the cells of a key-change table, which is what Row 10.28's table does.
- **The derivation** (*checked*, a search for learn, neural, network, black box, data-driven): it names no learned term
  of the candidate score. Its three hits (lines 660, 811, 901) are quotations of published systems in defenses, seen in
  the search results only.

---

## §A.3 What the record has already settled, and what it carried here

- **The fit (L2-S38's family, *checked*, `records/cowork/rulings/cowork_rulings_2026_10_05_l2_fit_sitting.md` read
  whole).** Ruling 1: "The term tables of L2's candidate score are counted from annotated music, once, and frozen; the
  short list of combination weights over them is fitted discriminatively, **to the graded measure**." L2-S38's second
  sentence is to be amended to say so. Ruling 2(ii) made Row 9.160(iii) HISTORICAL (the old fitter's exemption for
  values with a "ratified structural rationale": "L2 has none"). Ruling 1 made Row 10.16(ii) HISTORICAL (fitting by
  likelihood). Ruling 4 placed Rows 1.1(ii), 1.2(iii) and 48.4(ii) ADOPTED — carried under L2-S38 — the "values fitted
  once" halves of three of this family's rows. **So the values half of the old rule is placed; this family holds the
  forms half.**
- **The tonality-change cost (L2-S34's family, *checked*,
  `records/cowork/rulings/cowork_rulings_2026_10_06_l2_tonality_and_progression_terms_sitting.md` read whole).**
  Ruling 3 placed six rows of D-347 and D-348 ADOPTED — proposed, with the proposal: "OQ-L2-3's held-out comparison of
  tonal spaces names one more candidate beside Lerdahl's and Weber's — circle-of-fifths distance together with a
  relative major/minor term — each entering with fitted weights only (L2-S38, L2-S39). Nothing is chosen now." Its
  "Recorded as put" (lines 99–103): "Row 10.28 (agrees with L2-S34, UNPLACED against L2-S39 — the joint estimator's
  ratified table over fifths distance and major/minor pair, a third way to handle the relative pair) is not placed
  here; it belongs to L2-S39's family, which reads this ruling first." Ruling 1 declined D-341's licensed-motion list
  "entering L2 as a published-theory feature with one fitted weight (L2-S39's form)", keeping it as "the named remedy
  if the measurement-design stage finds such a shortfall".
- **The bass-scale-degree prior (L2-S28's family, *checked*,
  `records/cowork/rulings/cowork_rulings_2026_10_08_l2_structural_bass_sitting.md` read whole).** Ruling 3 put D-585
  into OQ-L2-3 "as a counted table or as the published rule entering under L2-S39 with one fitted weight" — the same
  two forms Row 10.28 raises, put side by side in one held-out comparison.
- **How far the objective reaches (L2-S10's family, *checked*,
  `records/cowork/rulings/cowork_rulings_2026_10_07_l2_chord_tone_membership_sitting.md`, Ruling 6, lines 196–223).**
  "The ultimate objective (maximum-precision inference, #4) is the prime objective and outranks every design rule in
  the long run. **It acts through evidence:** a design rule holds while there is no reason to suspect that breaking it
  would improve the inference; when there is such reason, the departure is opened up for investigation and is
  investigated, tested and measured under #18, #19 and #20 before it carries load. An asserted benefit by itself
  overrides nothing." L2-S39 is a design rule of this kind, and so are the two rules Question 3 is about. *(§B item 6.
  Former wording, preserved (#12): "of exactly this kind".)*
- **Theory-built tables for the church modes (*checked*,
  `records/cowork/rulings/cowork_rulings_2026_10_04_l2_tonality_vocabulary_sitting.md`, Ruling 1, lines 81–98, and the
  exchange it was given upon, lines 410–479).** *Added at the check, §B item 7.* The user's word on that ruling: "I
  agree with you recommendations." Each church mode, before it is admitted as a tonality, needs "a theory-built pitch
  profile and chord-expectation table whose source is read on our side (#1; D-531 is the precedent for a confirmed
  hand-built table; Levine's *Jazz Theory Book*, reached through the Modal Harmony Ontology, is a candidate source, not
  yet read)". The exchange behind it adds that such tables "cannot be counted from the ground truth held and can be
  built from theory (D-531 …), labelled THEORY, their precision a declared bound (#24)". **Two things follow for this
  family** (*my reading*): a ruling already requires a theory's source to be read on this side before its table is used
  — the bound of §A.6 rests on it as well as on D-473; and that ruling reads D-531 in the direction that supports
  theory-built tables, which bears on Question 3 (see there).
- **The research iteration (*checked*, `records/cowork/rulings/cowork_rulings_2026_10_07_context_research_sitting.md`
  read whole).** One targeted iteration, after the last detail specification is ratified and before measurement design,
  asking per load-bearing statement "is there a published method, algorithm or public software that would infer
  better than what is specified?"; a finding that a rule may cost precision sends the rule to a measurement.
- **The route (*checked*, `records/cowork/rulings/cowork_rulings_2026_10_04_l2_route_sitting.md` read whole).** "Rows
  no family reaches stay proposals."
- **The L0/L1 side** (*checked*): the L0/L1 reading file has no hit for D-096, "Factor FORMS", "forms come from",
  "theory-grounded factor", "Learned factors", D-531, learned replacement, Lerdahl, Weber or L2-S39; the 2026-08-31
  record's one hit for D-096 (line 32) is a remark that a weight "is fitted at L2 under DP-P and #20/**D-096**", not a
  ruling on this subject. The L2 file's member 62 (the rows the L0/L1 side sent over, lines 70314–70956) was read at its
  row headings: none is on this subject. `FRAMEWORK.md` (*checked*, searches for Lerdahl, Weber, published constants,
  single weight, forms from theory, learned, neural, black box): no charter text on this subject; its uses of
  "learned" (lines 679, 1607) and "neural" (lines 673, 1596) are DP-A's account of the neural multi-task lineage and
  that account's provenance (lines 671–683 read; 1596–1607 seen in the search results only), which concern dividing the
  deciding, not term forms.

---

## §A.4 The rows (*checked*, each at its row)

**Row 1.1 — "factor forms from theory; values fit once, never tuned per case."** *WITHHELD — D-096.* (lines 386–402)
Outgoing: "**(a) Factor FORMS come from theory; factor VALUES are fit ONCE against ground truth and are never tuned per
case.**" Claim (i), the forms half: L2-S39 **AGREES** "on the forms it names". **Proposed: ADOPTED — proposed** —
"that every term's form be derived from established music theory or published research before any value is attached to
it — L2-S39 carries this for published distances and profiles only." (Claim (ii) placed by the fit record.)

**Row 1.2 — "the shape before the number …"** (lines 406–426) Claim (i): "Every factor's shape is derived from
established music theory before any number is attached to it". L2-S39 **AGREES**. **Proposed: ADOPTED — proposed**,
travelling with Row 1.1(i).

**Row 9.160 — "what is not fitted …"** (lines 18975–18985) Claim (i): "Structural predicates (template interval
definitions, the class-(a) structural test, §6-block entry *conditions* as opposed to their numeric thresholds, the
outer-guard structure)" are not fitted. L2-S39 **AGREES** — a published form enters "as a feature whose single weight
is fitted", its constants "not tuned". **Proposed: ADOPTED — proposed**, travelling with Row 1.1(i). (Claim (ii) placed
HISTORICAL by the L2-S34 record; claim (iii) HISTORICAL by the fit record.)

**Row 10.16 — "one weight per factor …"** (lines 22452–22462) Claim (i): "The weight vector is small (one weight per
factor, roughly ten)". L2-S39 **AGREES** — a feature "whose single weight is fitted". **Proposed: ADOPTED — carried
(L2-S39).** (Claims (ii) and (iii) placed by the fit record.)

**Row 17.1 — "key, mode and chord in one decode; … every clue a factor from theory …"** *WITHHELD — D-001, claims
(i)–(iii).* (lines 27234–27255) Claim (iii): "every enumerated clue enters as a factor grounded in theory". L2-S39
**AGREES** "as at Row 1.1(i)". **Proposed: ADOPTED — proposed**, travelling with Row 1.1(i). *(The comparison notes
that this is an AGREES on a WITHHELD statement: the derivation reached a ruled answer it was not shown.)*

**Row 21.1 — "the hand-built analysis confirmed; the learned replacement retained behind the interface as a
fallback."** *WITHHELD — D-531.* (lines 29154–29170) Claim (i): "the hand-built analysis is confirmed". L2-S39
**AGREES** "as at Row 1.1(i)". **Proposed: ADOPTED — proposed**, travelling with Row 1.1(i). (Claim (ii), the learned
replacement as fallback, is proposed ADOPTED — proposed travelling with Row 1.55; it is not in this family, §A.7.)

**Row 43.39 — "curated knowledge a component the layers query …"** (lines 56328–56336) Claim (i): "durable curated
knowledge (this vocabulary; the chord templates; the key profiles) is a **component queried by the layers**, distinct
from the layers' per-piece inference". L2-S39 **AGREES** — a published profile "enters the candidate score as a feature
whose single weight is fitted. Its internal constants are the published ones, unchanged". **Proposed: ADOPTED — carried
(L2-S39).** *My reading:* L2-S39 carries the half that matters to the analysis — the curated numbers stay fixed and
apart from what is fitted to the music; it says nothing about holding them in a separate software component, which is a
matter of how the code is organised and needs no L2 statement. (Claim (ii), on genre labels, is UNPLACED and names no
derived statement; not this family's.)

**Row 48.4 — "forms from theory; values fit once against ground truth and frozen."** (lines 63314–63322) Claim (i):
"each factor's **form** comes from established theory (#1/#2)". L2-S39 **AGREES** "as at Row 1.1(i)". **Proposed:
ADOPTED — proposed**, travelling with Row 1.1(i), the proposal written there "that every term's form be derived from
established theory" (§12, line 73678).

**Row 48.6 — "a learned term admitted only where theory supplies no form, as one inspectable term."** (lines
63338–63346; taken in on subject) Outgoing: "**Learned factors** are admitted *only* where established theory supplies
no form, kept as a single inspectable term inside the model (the C-kernel, hybridized — not a black box replacing the
model)." THE DERIVATION IS SILENT. **Proposed: ADOPTED — proposed** — "that a learned term enter L2's candidate score
only where established theory supplies no form, and then as one inspectable term inside the model."

**Row 10.28 — "the key transition: a fitted, transposition-invariant table over fifths distance and mode pair."**
(lines 22600–22610) Outgoing: "**Key transition** `P_key(k_j | k_{j-1})` — transposition-invariant small table over
(circle-of- fifths distance between tonics, mode pair), with the relative and parallel relations as their own cells
(the Noland/Rocher family; asymmetries permitted — the table is fit, not a symmetric curve)." L2-S34 **AGREES** ("a
cost for a tonality change, graded by the distance between the two tonalities"); L2-S39 **DIFFERS**: "The outgoing
table *"is fit, not a symmetric curve"* …; L2-S39 says of a published distance, *"Its internal constants are the
published ones, unchanged"*, its *"single weight"* fitted." **Proposed: UNPLACED** — "a ratified fitted table over tonal
distance, against L2-S39's published distance with one fitted weight; placing it would choose between them."

---

## §A.5 The two forms behind Row 10.28, in plain words

L2-S34 (i) gives L2 a cost for changing tonality, "graded by the distance between the two tonalities in a published
tonal space" (*checked*, derivation lines 844–846). There are two ways to build that cost:

- **Form 1 — a published distance, one weight (L2-S39 as written).** Take a theory's distance between any two
  tonalities exactly as published (Lerdahl's, Weber's, or — added by the L2-S34 record's Ruling 3 — the circle of
  fifths with a term for the relative major/minor). L2 learns one number: how heavily that distance counts.
- **Form 2 — a counted table (Row 10.28).** Group all pairs of tonalities by two things only — how far apart their
  tonics are on the circle of fifths, and which modes they are (major to major, major to minor, and so on), with the
  relative and parallel relations as their own entries — and count from annotated music how often each kind of change
  actually happens. The table's entries come from the music, not from a theory, and need not be symmetric (a move to
  the dominant and a move back need not cost the same). The theory supplies only the grouping.

Form 2 is the shape the fit record's Ruling 1 already uses for L2's other tables — counted once from annotated music
and frozen, one combination weight fitted. It is not a published distance with its constants tuned, which is what
L2-S39 forbids; it is a counted table, which L2-S38 as amended allows (*my reading*). What it is not is "graded by the
distance … in a published tonal space" in the sense L2-S34 (i)'s words most naturally carry: its grading comes from
counts. So it is a third candidate for the same cost — the L2-S34 record's words for it are "a third way to handle the
relative pair" — and what decides between the candidates is a held-out measurement (OQ-L2-3; L2-S39's own falsifier
admits "choosing between two published spaces by held-out comparison"). *(§B item 8. Former wording, preserved (#12):
"a third candidate for the same cost, as the L2-S34 record called it")*

---

## §A.6 What stands, and what the three questions would decide

**The method that stands now** (L2-S34, L2-S38 and L2-S39 *checked* at the derivation; the fit record's Ruling 1 and
the L2-S34 record's Ruling 3 *checked*): the candidate score carries a cost for a change of tonality, graded by the
distance between the two tonalities in a published tonal space (L2-S34 (i)); which space is used is a held-out
measurement among Lerdahl's, Weber's and the circle of fifths with a relative major/minor term (OQ-L2-3, the last
candidate added by the L2-S34 record's Ruling 3 and written in at the application act; §B item 9); a published distance or profile enters with its published constants unchanged and one fitted
weight (L2-S39); L2's other tables are counted once from annotated music and frozen, and the short list of combination
weights is fitted to the graded measure on held-out folds (L2-S38 as the fit record amends it). The derivation names
no learned term (§A.2). **No statement of L2 read here says, for terms other than published distances and profiles,
where a term's form must come from.** The statements read whole here (L2-S34, L2-S38, L2-S39) each carry a defense
with its sources *(§B item 10. Former wording, preserved (#12): "The statements read here (L2-S34, L2-S37, L2-S38,
L2-S39)" — only the tail of L2-S37 was read at the derivation)*; the others were not read for this, and whether every term's form traces to published theory or
research was **not checked term by term** by this sitting.

**A bound that is not a question.** A published space or profile entering under L2-S39 must have its primary fetched
and read before its constants carry load (D-473). Neither of the two named primaries (Lerdahl's, Weber's) is held; for a
scale-degree profile, Krumhansl's book has no local copy and Temperley's 2002 paper is held, its extract not read here
(§A.2). This follows from the record and is carried for the research iteration and measurement design, as the
structural-bass record carried the same bound for the Rule of the Octave.

### Question 1 — a confirmation (documentation only)

**What would be ruled:** Rows 10.16 claim (i) and 43.39 claim (i) **ADOPTED — carried (L2-S39)**, as proposed. 2
row-parts. **Algorithm:** unchanged; L2-S39's wording unchanged.
*Ground, as it would be put:* towards the objective (#4), nothing the analysis does changes — one weight per term, and
curated theory values kept fixed and apart from the fit, are what L2-S39 already says. Towards the principles: D-599
(the record settles the placement); #12 (each row keeps its proposal, the ruled label added beside it). Meta level:
filing labels on rows. The "component the layers query" wording of Row 43.39(i) is a matter of code organisation and
is not carried as a rule (*my reading*, §A.4).

### Question 2 — a confirmation, the alternatives having collapsed (documentation now; the algorithm only as a measurement decides)

**What would be ruled:** Row 10.28 **ADOPTED — proposed**, placed from UNPLACED, with the proposal, for the application
act to write beside OQ-L2-3: *"the held-out comparison of tonal spaces for L2-S34 (i)'s cost gains one more candidate —
a counted, transposition-invariant table over the circle-of-fifths distance between the tonics and the pair of modes,
with the relative and the parallel relations as their own entries and asymmetries allowed, counted once from annotated
music and frozen, with one fitted weight (L2-S38 as amended by the fit record's Ruling 1); graded like the other
candidates; nothing chosen now."*
**Algorithm:** unchanged now. L2-S34 (i) and L2-S39 keep their wording. If the counted table ever beats the published
distances beyond the comparison's uncertainty (#24), L2-S34 (i)'s words "in a published tonal space" would need
amending, by its own ruling then — an asserted benefit overriding nothing (L2-S10 record, Ruling 6).
*Ground, as it would be put:* towards the objective (#4), a ratified design and the derived one are tested on the music
rather than one set aside on argument; the published spaces disagree about which change is nearest (§A.2), and a
counted table lets the music decide; the published comparison found (§A.2) favoured the fitted table but cannot
settle it. *(§B item 11. Former wording, preserved (#12): "the one published comparison of the two forms" — no search
for others was run.)* Towards the principles: D-254 (measure rather than ask); #12 (neither form dropped unheard); #19
(whichever wins is established by measurement); #20 and D-271 (the table's size within the declared capacity budget);
the precedents of the L2-S34 record's Ruling 3 (one more candidate inside this same comparison) and the structural-bass
record's Ruling 3 ("a counted table or … the published rule entering under L2-S39", in one comparison). Meta level: the
analysis's own measurement list. *Cost accepted:* one more arm in a measurement already owed; changes of tonality are
rarer than chord-to-chord changes, so the table's entries are thinly counted — D-533's proportional share and D-271's
budget are what bound that (*my reading*).
**Why it is a confirmation and not a decision** (*my reading*, stated so it can be challenged): the two other placements
each decide what D-254 and the user's 2026-10-07 rule say a measurement decides. *HISTORICAL* would drop a design the
comparison calls ratified, untested (against #12, D-254, L2-S10 Ruling 6). *Adopting the counted table now in place of
the published distance* would change L2's algorithm with no measured basis on this repertoire (against D-630's burden
on the change, applied by analogy since D-630 speaks of adding a component, #17(b), D-254). *(§B item 12. "applied by
analogy …" added.)* That leaves one placement, the one the two precedent rulings took.

### Question 3 — a decision (whether L2's specification gains a rule on where a term's form comes from, and on learned terms)

The seven row-parts: the six travelling with Row 1.1(i) (Rows 1.1(i), 1.2(i), 9.160(i), 17.1(iii), 21.1(i), 48.4(i))
and Row 48.6.

**What is at stake, in plain words.** The old design had a two-part rule: the *shape* of every piece of evidence comes
from music theory, and only its *numbers* are learned from annotated music (D-096); and a learned piece of evidence —
one whose shape is itself learned, such as a trained network — is allowed only where theory has nothing to offer, and
then as one piece among the others that can be inspected (Row 48.6). The derived L2 keeps the numbers half (L2-S38,
placed) and the shape half only for published distances and profiles (L2-S39). It says nothing about the shape of its
other terms, and nothing about learned terms. **No term L2 now specifies is learned** (the derivation searched, §A.2),
so the learned-term rule would change none of them. Whether every term L2 now specifies has a form traced to published
theory or research was **not checked term by term** (§A.6), so the forms rule's effect on the present terms is
unchecked; *my reading* is that the derivation's discipline (sources in every defense read here) makes a conflict
unlikely, and the research iteration is where it would be checked. What the question decides is whether L2's
specification carries rules that every term, present and future, must meet.

**A fact that bears on the learned-term half** (*checked*, D-531 at `decisions/group_C.md` lines 1025–1046): the old
decision that kept the hand-built scorer and did not trigger the learned replacement says "Two limits ride with the
verdict and are part of it": first, "the decomposition covers one repertoire only, and the fallback's advantage is
concentrated on the harder chromatic material that was not decomposed"; second, "the corrected metric must be
**committed before any fitting**". And the learned option "re-opens for **any slice later established as a genuine
ceiling**". *My reading:* the first limit is a recorded reason to suspect, on chromatic music, that a learned form might
infer better — the condition under which the user's 2026-10-07 rule opens a design rule up for measurement.
*(§B item 13. Former wording, preserved (#12): "states two limits "as part of it": "the decomposition covers one
repertoire only, and the fallback's advantage is concentrated on the harder chromatic material that was not
decomposed"" — one limit quoted as if it were both.)*

**A ruling that reads D-531 the other way** (§A.3, *checked*; §B item 14): the tonality-vocabulary record of 2026-10-04
cites D-531 as "the precedent for a confirmed hand-built table" when it requires theory-built profiles for the church
modes. *My reading:* that use supports the forms half (a theory-built table, its source read on our side); it says
nothing for or against a learned form, so it does not reach the learned-term half. It is a further ground for writing
the forms rule (Positions 1 and 2) and against leaving it unwritten (Position 3).

**Position 1 — write both rules into L2 (the comparison's proposals as written).** The seven row-parts ADOPTED —
proposed; the application act writes, beside L2-S39: *"Every term's form is taken from established music theory or
published research and fixed before any value is attached to it (L2-S39 being the case of a published distance or
profile). A learned term enters only where established theory supplies no form, and then as one inspectable term inside
the candidate score."* **Documentation:** the rows' labels and the two sentences. **Algorithm, as the specification
defines it:** L2 gains a rule on which terms its score may contain; no present term is learned, and the forms rule's
effect on the present terms is unchecked (above). Under the L2-S10
record's Ruling 6 the second sentence, like any design rule, gives way to a held-out measurement once there is reason to
suspect a learned form would infer better — and D-531's chromatic limit is such a reason, so the research iteration
would carry it as a question.
*Towards the objective:* every term keeps a musical meaning, so a wrong result can be traced to a named term (#3, #13);
small capacity (#20). Against it: it writes as a rule a preference the record itself already doubts on part of the
repertoire. *Towards the principles:* #1 applied to L2's terms; D-096 and D-001 (ruled L2's own; the derivation reached their
forms-from-theory clause only for distances and profiles); D-531's fallback shape; #19 (a term established by its theory, not by its fit). Meta
level: the analysis's own specification.

**Position 2 — write the forms rule only; send the learned-term rule to the research iteration (this side's
recommendation).** Rows 1.1(i), 1.2(i), 9.160(i), 17.1(iii), 21.1(i), 48.4(i) ADOPTED — proposed, the application act
writing beside L2-S39 the first sentence of Position 1. Row 48.6 ADOPTED — proposed, its proposal standing, with a
ruled line beside it: *"carried to the research iteration of 2026-10-07 as its question for L2's terms: where a term's
form comes from theory, would a published learned form infer better? D-531's limits (one repertoire; the learned
fallback's advantage concentrated on undecomposed chromatic music) are the recorded reason to ask."* **Documentation:**
the labels, the one sentence, the ruled line. **Algorithm, as the specification defines it:** L2 gains the forms rule
(its effect on the present terms unchecked, as above); L2 states no rule on learned terms until the research iteration and, if it finds
reason, a held-out measurement decide one.
*Towards the objective:* the traceability of Position 1 for every term, without writing a preference against learned
forms that the record already has reason to doubt (#4, through the L2-S10 record's Ruling 6). Against it: L2's
specification is silent on learned terms for now, so a learned term proposed before the research iteration would be
judged on #1 alone. *Towards the principles:* #1; D-096 and D-001 as in Position 1; the L2-S10 record's Ruling 6 and the
research-iteration ruling (the question goes where it was ruled to go); D-254 (investigate rather than decide on
argument); #12 (Row 48.6 keeps its proposal). Meta level: the analysis's own specification and its research list.

**Position 3 — write neither.** The seven row-parts stay ADOPTED — proposed, unplaced, as the route ruling allows for
rows no family reaches. **Algorithm:** unchanged; L2's specification stays silent on term forms outside L2-S39.
*Towards the objective:* nothing gained or lost now. *Towards the principles:* #1 binds every design project-wide, and
D-473 every design justified from published research, so nothing is unprotected (#6, no second statement of a
principle). *(§B item 15. Former wording, preserved (#12): "#1 and D-473 already bind every design project-wide".)* Against it: D-096's and D-001's forms
half, ruled for L2, would live in L2's specification only for distances and profiles; this family reaches the rows, so
leaving them unplaced is a decision by default rather than by ruling (#12 keeps the rows, but not a placement).

**The recommendation, Position 2, and the strongest argument against it.** Position 2 keeps the part of the old rule
that the record does not doubt and that L2's derivation appears to follow in its own discipline (each statement read
here carries a defense with sources), and sends the part the record does doubt — the preference against learned forms — to the place
the user ruled such questions go. The strongest argument against it is Position 1's: D-531 was a measured decision, not
an opinion, and its re-check gate already says when the learned option re-opens; writing Row 48.6 as a rule, with
D-531's gate as its exception, would give L2 a complete answer now instead of a deferred one. *My reading:* the two are
close; Position 2 is preferred because the user's 2026-10-07 rule asks that a rule be opened up for investigation once a
reason to suspect is on the record, and D-531's own limit is that reason.

**The family's arithmetic, if all three are confirmed as recommended:** 2 ADOPTED — carried (Question 1) + 1 ADOPTED —
proposed (Question 2) + 7 ADOPTED — proposed (Question 3, six with the forms sentence, one carried to the research
iteration) = 10 = §7's 9 + 1 taken in.

---

## §A.7 Searches made so the questions do not repeat an earlier ruling, or miss a row

All 38 ruling records dated 2026-10 and the 37 `cowork_l2_*` files in `ratification_surfaces` were staged before
searching (entry 324 §2), with the 2026-08-31 record.
- The 2026-10 ruling records searched for "L2-S39": hits only in the L2-S34 record (lines 43, 88, 92, 99, 101, 143,
  164) and the structural-bass record (lines 105, 122), both read whole.
- The same records searched, as whole numbers, for 1.1, 1.2, 17.1, 21.1, 9.160, 10.16, 43.39, 48.4, 48.6, 10.28, 1.55
  and 21.2: **no placement of any of this family's row-parts.** The hits are the fit record's placements of other
  claims of Rows 1.1, 1.2, 9.160, 10.16 and 48.4 (read in that record); the L2-S34 record's placement of Row 9.160(ii)
  and its lines on Row 10.28 (read); and the score-decomposition record's placement of Row 17.1 claim (ii) (its line
  96, seen in the search results only).
- The `cowork_l2_*` files searched for "L2-S39": the tonality-and-progression-terms surface (read at lines 180–214; its
  hits at lines 34, 116, 283, 294, 326 and 394 seen in the search results only) and the structural-bass surface (hits
  at lines 338, 346, 381, seen in the search results only). *(§B item 16. Former wording, preserved (#12): "the
  tonality-and-progression-terms surface (read at lines 180–214)".)*
- **Added at the check (§B item 7):** the 2026-10 records searched for D-096, D-001, D-531 and "learned term / form /
  replacement / factor": the tonality-vocabulary record (read at lines 60–119 and 410–479, §A.3); the one-decision
  record (line 72) and the tonality-evidence record (lines 39, 64), which cite D-001 for the one decode, seen in the
  search results only. **The first writing searched by row number and statement number only, and so missed the
  tonality-vocabulary ruling.**
- The comparison file searched for "L2-S39", "travelling with Row 1.1(i)" and "travelling with Row 10.28": the eight
  §7 rows, Row 48.6's axis note, and the §12 proposal list (lines 73590–73684) and §12's one-sentence DIFFERS list
  (lines 74060–74089), read at those lines. Also searched for published theory, published distance, tonal space, pitch
  space, Weber, Lerdahl, scale-degree profile, key profile, fifths distance and "form … theory": Rows 7.164 and
  48.23 read at their rows (7.164 proposed carried under L2-S20; 48.23 proposed HISTORICAL, a plan); Row 7.76 seen at
  its heading and difference line (in L2-S34's family, its claims (ii) and (iii) ruled by that record's Ruling 3); the
  other hits seen in the search results only.
- **Not taken in, on this side's cut:** Rows 1.55, 21.1(ii) and 21.2 — the learned replacement kept as a drop-in, and
  "that the search over readings be independent of how the values of the candidate score's terms are produced" (Row
  1.55's proposal, lines 1308–1320) — whose subject is the search's independence from how term values are produced, not
  where a term's form comes from; and Row 1.56 (read to its derived-statements line: none). They stay proposals unless the user widens
  the cut.

---

## §A.8 What was not read

The derivation outside the lines cited; `FRAMEWORK.md` outside lines 660–699 and its search hits; the register group
files beyond D-096 (lines 130–143) and D-531 (lines 1025–1052); D-001's entry; the Rocher, Catteau and Feisthauer
extracts beyond their search-result lines; the Temperley 2002 extract; every paper itself; the second-pass Noland &
Sandler extract; the L2-S10 record beyond lines 190–249; the tonality-vocabulary record beyond lines 60–119 and
410–479; the comparison file beyond the rows, §5, §7, §8 (OQ-L2-3), §12
and member 62's headings cited; the L0/L1 reading beyond its search.

---

## §B The check, at the sources (2026-10-09, on the user's "continue")

The landed §A (37,145 bytes) was read whole and checked for completeness, coherence, correctness and absolutes; the
claims below were re-read at their objects. Sixteen corrections, each made at its site with the former wording kept in
place (#12). **None moves a placement, a count, a proposal or the recommendation**; item 7 adds an earlier ruling the
first writing missed, and items 7 and 14 add a ground to Question 3 without changing its positions.

1. §A.1 — "Four of the rows" carry WITHHELD; three do (Rows 1.1, 17.1, 21.1, at their row headings).
2. §A.2 — "These three agree with L2-S39's relayed defense quotations": L2-S39's defense relays Rocher and Catteau
   only; the Feisthauer passage is L2-S34's.
3. §A.2 — "exactly the two forms": Noland & Sandler re-fit a theory-built table by unsupervised estimation; Row 10.28's
   table is counted from annotations. "exactly" struck, the difference stated.
4. §A.2 — "the paper gives no uncertainty": the paper was not opened by this sitting; the extract reports none.
5. §A.2 — the Catteau finding read at its lines (308–312): distance one for the relative pair is tied with the
   dominant and subdominant, not "the nearest possible change"; re-marked *checked*.
6. §A.3 — "of exactly this kind" softened.
7. §A.3 and §A.7 — **a missed ruling**: the tonality-vocabulary record's Ruling 1 (2026-10-04) requires a
   theory-built profile's "source read on our side" and cites D-531 as precedent for a theory-built table. Found by a
   search for the decisions the rows rest on (D-096, D-001, D-531), which the first writing did not run. Read at
   lines 60–119 and 410–479.
8. §A.5 — "as the L2-S34 record called it": the record's words are "a third way to handle the relative pair".
9. §A.6 — the circle-of-fifths candidate is a ruled addition to OQ-L2-3, written in at the application act; said so.
10. §A.6 — L2-S37 listed among statements "read here": only its tail was read at the derivation; removed.
11. Question 2 — "the one published comparison": no search for others was run; "the published comparison found".
12. Question 2 — D-630 speaks of adding a component; its use against a replacement marked "by analogy".
13. Question 3 — D-531 quoted in part: "Two limits ride with the verdict and are part of it"; the first writing quoted
    the first limit as if it were both. The second (the corrected metric committed before any fitting) now quoted.
14. Question 3 — the tonality-vocabulary record's use of D-531 added as a further ground for writing the forms rule
    (Positions 1 and 2) and against Position 3; it does not reach the learned-term half (*my reading*).
15. Position 3 — "#1 and D-473 already bind every design": D-473 binds designs justified from published research.
16. §A.7 — the tonality-and-progression-terms surface's other hits were seen in the search results only; listed.

**Confirmed at the objects in the same act:** L2-S39's text (derivation 967–984); §7's nine row-parts (71239–71242);
each row's proposed disposition at its row; the three ruling-record quotations (L2-S34 Ruling 3 and its "Recorded as
put", structural-bass Ruling 3, L2-S10 Ruling 6); the fit record's placements of the rows' other claims; D-096's and
D-531's register text; the bibliography's rows; the Noland Table 1 figures at the extract; the family's arithmetic
(2 + 1 + 7 = 10).

**Degradation tells, reported under the user's standing rule of 2026-08-15.** Two of the named shapes occurred in the
first writing: **a ruling quoted in part** (item 13) and **an overstatement of what was read** (item 10), with a search
described narrower than its subject needed (item 7). **And one shell command was run in the container during this
check** (`true`; it read and wrote nothing and no claim rests on it), against the opening instruction; declared here.
*Recommendation:* put the three questions one per turn, record each, and hand over at the placed family.

# The WITHHELD FAMILY for the harmony-boundary subject — put to the user for a ruling

> **STATUS: RULED 2026-08-22 — applied by this commit; the lists below are the ruled family.** The
> ruling record is `cowork_rulings_2026_08_22_withheld_family_sitting.md` — five rulings, one per
> list. **No session has been booted from the pack.** This is the reading surface for one decision:
> which recorded decisions are withheld from the boot pack an implementation-blind session will
> read, so that what that session derives can be compared against a ruled answer it has not seen.
>
> Prepared by Claude Code, 2026-08-22, under `cc_instruction_pilot_preparation_withheld_family.md`
> Task 1(d), executing amendment (a1) of Ruling 1 of
> `cowork_rulings_2026_08_22_boot_list_sitting.md` and Ruling 1 of
> `cowork_rulings_2026_08_22_pilot_order_sitting.md` — *"the dispatch derives the candidates at the
> objects and the authored family is the user's to rule."* **Corrected to the ruled lists by
> `cc_instruction_withheld_family_correction.md` Task 1(d), in the commit that corrects the
> generator's authored table and re-renders the pack.**
>
> **The verdicts below were AUTHORED and they CLEARED NOTHING when they were written.** Under the
> standing clause a session may perform an owed establishment and author its verdicts, and those
> verdicts clear no guard when they are written: they were delivered as this reading file, and they
> take effect now, because the user has ruled them and the reviewed set has been applied to the
> generator's authored table. **The pack a deriving session boots from is the one this commit
> renders.**

---

## 1. The words used here, explained first

- **The pilot** — the phase that proves the derivation method before the method is trusted.
- **An implementation-blind deriving session** — a session that writes what the analysis *should*
  do for one unit, without reading what the current code or the current specifications say it
  *does*.
- **The curated boot list** — the implementation-free read list such a session opens at boot. You
  ruled its membership on 2026-08-22: six members, eight exclusions, three amendments.
- **The boot pack** — the rendered, self-contained directory generated from that list. A deriving
  session opens that directory and nothing else. It now exists on disk at
  `tools/audit/derivation_boot_pack/harmony-boundary/`.
- **The held-out test** — one decision derived blind with your own ratified ruling on it WITHHELD.
  The withheld ruling is the *oracle*: the answer the blind derivation is later compared against.
- **The withheld family** — the recorded decisions, documents and passages cut out of the pack for
  this one subject, so that the oracle does not reach the session by a side route.

## 2. The subject the blind session will derive, stated from scratch

> **How the analysis should decide where one chord ends and the next begins, and what evidence
> decides it.**

Music does not announce its own harmonic boundaries. Something has to decide that one chord is
sounding from here to there and a different one from there onward — and something has to decide
which evidence is allowed to settle that, and in what order when two kinds of evidence disagree.
That decision is what the blind session is being asked to write, from the domain and from your
ratified design intent, without reading what this project's own specifications currently say.

## 3. The oracle, as Ruling 4(c) of 2026-08-21 states it

Quoted from the ruling record, in full:

> *"(c) the held-out test — one decision derived blind with its user-ratified design-intent ruling
> withheld, the evidence-ranking ruling of 2026-08-11 (`ARCHITECTURE.md:394-402`) as the oracle, and
> Claude Code's five recorded corpus traces of the ratified factorization
> (`cowork_joint_estimator_factorization.md:196-203`) as the oracle's second arm where the pilot
> unit is a factor of the factorization."*

That ruling has two halves, and both are what the family has to protect: **where a boundary falls**,
and **which evidence ranks first in deciding it**. The oracle's own text is not quoted here, and
this file deliberately does not restate it.

## 4. How the candidate list was derived, and the bound on the derivation

The family was not hand-picked. A generator —
`tools/audit/gen_derivation_boot_pack.py` — walks the `DESIGN-INTENT` class of the rulings sort you
ratified and returns as a **candidate** every entry meeting any one of these, all of them derived at
the objects on every run:

- its group is **E** — Layer 2, the slicer;
- its recorded home is `cowork_joint_estimator_factorization.md` or
  `cowork_factorization_desk_simulation.md`;
- its recorded home is `ARCHITECTURE.md` at a line **inside one of the two oracle spans**, each
  located by its own text rather than by line number;
- any of its title, its verbatim, its plain restatement or its search patterns contains one of a
  fixed list of words — *slice, slicing, segment, segmentation, boundary, boundaries, change-point,
  onset, release, harmonic rhythm, where one chord ends, finest grain, grain, atomic, sounding,
  struck, priority of evidence, evidence ranking*;
- it is an identity the ruling names — **D-057**.

**★ THE BOUND, STATED BECAUSE A PATTERN THAT DOES NOT SAY WHAT IT MISSES READS AS COMPLETE.** The
last of those is a plain substring match over the register's own text, and **its reach has never
been measured**. An entry that bears on this subject in words none of those terms carry would not
appear below at all. The bound is stated on the artifact rather than a detection measurement being
owed, under the standing clause for an enumerating pattern, and that clause's test is met: **no
analysis decision consumes this enumeration — you do.**

The match also fires **inside longer words**, and that is now visible rather than hidden: every
keyword match is published with the matched text **in its own context**, so a candidate that reached
the list only because `slice` sits inside `isLicensedProgression`, or `release` inside *released*,
can be seen for what it is — and so can one that reached it only because the keyword sits inside a
code identifier, as `onset` does inside `onsetAtRegionStart` and `boundary` inside
`combinedBoundary`. Six of the entries below are annotated as exactly that, and each says so.

*Every figure about this derivation — the size of the class, of the candidate list, of each verdict
class — is at `tools/audit/derivation_boot_pack.json` → `subjects.harmony-boundary.counted`, and
none is restated here.*

## 5. The test each verdict was made against

- **IN** — a deriving session that read this entry would know, in whole or in part, what the ruled
  answer to *where one chord ends and the next begins, and what evidence decides it* is. Applied
  concretely: does the entry disclose **(a)** where a boundary falls, or **(b)** which evidence
  outranks which in deciding one?
- **OUT** — the entry bears on another unit, and reading it tells the session neither (a) nor (b).
  The reason says what it bears on instead.
- **UNPLACED** — the entry's own text does not settle it. The reason says what was read.

**Default nothing:** a verdict that could not be defended in one sentence at the entry's own
verbatim was recorded UNPLACED rather than guessed into IN or OUT.

---

## LIST ONE — IN: withheld from the pack

*These are the entries a deriving session will not see. Each is withheld because it discloses part
of the ruled answer.*

| ID | Title | Why it is withheld |
|---|---|---|
| D-001 | Key, mode and chord are inferred by ONE joint decode | Its verbatim names segmentation a MODELED (semi-Markov) VARIABLE of the one decode, and its plain restatement says that single pass "also decides where one chord ends and the next begins" — how a boundary is decided, in terms. |
| D-022 | The founding principle — analyse at the finest grain, coarser views are derived | Its plain names the grain "the smallest stretch over which the sounding harmony does not change", which is where a boundary falls. |
| D-023 | The atomic analysis unit is the constant-sonority slice, never the metric beat | Its plain defines the unit as "a stretch during which exactly the same notes are sounding" — the boundary rule itself. |
| D-024 | The fact layers are style-agnostic; style lives only in calibration | It names L2 as *slicing* and rules it a lossless, style-agnostic FACT layer, so where a stretch ends is a fact read from the notes and never a style-calibrated judgment. |
| D-057 | The priority of evidence — actual sounding notes are the strongest evidence | The identity amendment (a1) names. Its verbatim IS the legacy statement of the withheld ranking. |
| D-317 | The backward-walk boundary change is a dead end | It rules on how a note's RELEASE relates to a boundary — counting notes that stop exactly where a stretch begins as belonging to it — which is the ruled answer's own subject. |
| D-318 | A short-region external merger is a dead end | It discloses a live merge rule that decides where one stretch ends: "the same-root merge already inside the first pass has combined those stretches". |
| D-383 | Bass, spelling and tonality-consistency DECIDE; a licensed progression is only a tie-break | It ranks the evidence channels with the vertical ones primary and the progression channel a tie-break — the same subordination of temporal-context evidence the oracle's ranking makes. *(Reached the list only through an in-word match.)* |
| D-449 | Factor granularity is fixed per factor | It states the machinery that decides where a segment's edges fall — the boundary-family factors per boundary, and the length bias whose bookkeeping "alone decided merge against split, against the ground truth". |
| D-450 | The key-signature and declared-mode prior conditions the INITIAL key state only | It states the notated signature's subordination to the sounding evidence: the prior is paid once and "the music governs thereafter". |
| D-453 | The desk simulation's verdict on the ratified factorization | It is the factorization's own trace verdict and points at the granularity finding that decides merge against split. |
| D-491 | REFUTED: making the override's comparison vertically fair does not repair it | It states, measured, that the vertical commit predicts the annotated root better than the progression re-pick — the oracle's ranking, as a measurement. |
| D-545 | The uniform mechanical extractor stops at the note-and-slice front | It describes the extraction as "reading notes and cutting them into simultaneities" and calls our own equivalent a slicer — telling a session that a slice IS a simultaneity. |
| D-565 | Exact score ties are broken by a declared TOTAL ORDER on paths | It decides which of two segmentations is committed — "fewer segments first; then the earliest boundary-tick sequence" — and is homed in the oracle's second-arm document. |
| D-569 | Collecting, filtering and weighting are THREE separate responsibilities | Its verbatim supplies the vocabulary of the withheld passage — "every sounding note in a region", "eligible for harmonic analysis", onset and offset as the note's own edges — without stating the rule. A deriving session that read it would have the oracle's own terms, and the comparison could not distinguish recovery from recall. *(Ruled IN 2026-08-22, from UNPLACED — Ruling 3.)* |
| D-575 | The Baroque partial-signature convention is handled by DETECTING it | It has the sounding weight overrule the written key signature, which is the oracle's ranking between those two evidence classes. |

**Beside the identities, two further withholdings, both already ruled and both applied:**

- **The document `cowork_joint_estimator_factorization.md`** — recorded by amendment (a1) as ORACLE
  material for the pilot and not a boot member. It was never a member of the pack; it is named here
  so the family is readable whole.
- **A derived set of CROSS-REFERENCE ADDITIONS** — every entry of the class whose own text quotes or
  cross-references one of the identities above, or names that document, including in fields the pack
  never renders. These are **derived, not authored**, and they are not a list you are asked to rule;
  they are published whole at `tools/audit/derivation_boot_pack.json` →
  `subjects.harmony-boundary.THE_WITHHELD_FAMILY.derived_cross_reference_additions`, each with the
  field and identity that matched. **Their bound is stated with them: one pass, from the authored
  identities only, and NOT transitive.** Several of them are entries graded OUT below — an entry can
  be irrelevant on its own subject and still be a route to a withheld one, and both facts are kept.

---

## LIST TWO — OUT: admitted to the pack

*These reached the candidate list, were read, and bear on another unit. Each says what it bears on
instead.*

| ID | Title | What it bears on instead |
|---|---|---|
| D-032 | Every confidence crossing a layer boundary is bounded and class-declared | The confidence contract between stages; its "boundary" is a LAYER boundary. |
| D-114 | The decoder commits its best path; no abstention on the key axis | The key axis's commitment and the abstain counter. |
| D-207 | The pedal-point class is defined voice-independently | The ornament vocabulary's pedal-point class and which voices it reaches. |
| D-224 | Joint bass-and-chord scoring requires accumulated regional evidence | When the dormant vertical scorer's joint path switches on. *(Reached the list only through an in-word match of `onset` inside `onsetAtRegionStart`.)* |
| D-262 | The extension increment is chosen by the requesting layer | The bounded-context extension protocol. |
| D-264 | Extension is an optimisation of load-more-then-rerun | The bounded-context extension's correctness guard. |
| D-268 | A confidence attaches to a named decision and keeps its identity | The cross-layer confidence contract; "chord-of-slice" appears only as a decision's name. |
| D-276 | Modal colour is published as un-rounded per-degree counts | What the record publishes about modal colour. |
| D-280 | Gates read structured fields only | The inference/presentation boundary, which is the boundary its text names. |
| D-285 | Embellishment is chord-first, never a richer vocabulary | How ornamental tones are handled; it names a segmentation step without saying where its boundaries fall. |
| D-313 | A confidence map is monotone or it is not fitted | Confidence calibration. *(Reached the list only through an in-word match of `boundary` inside `combinedBoundary`.)* |
| D-320 | The absent-root guard is REVERTED and must not be retried | Chord identity — whether a candidate whose root does not sound may win. |
| D-327 | The root-continuity guard reads the reconstructed inversion credit | One gate of the dormant vertical scorer and what its test reads. |
| D-329 | Completeness of the candidate list is the priority | Candidate admission for a stretch already cut, not where the cut falls. |
| D-330 | Never a pooled recompute | Note membership per stretch; it presupposes slices without stating where their edges fall. |
| D-337 | A lean toward another degree is a tonicization by default | Where one KEY gives way to the next — a different unit. |
| D-338 | The function layer selects among the chord layer's carried readings | The function layer's selection discipline. |
| D-339 | A confident earlier decision can be overturned by decisive later evidence | The architecture-wide override mechanism. |
| D-341 | The licensed root-motion set is completed by theory | Which root motions count as functional progressions. *(Reached the list only through an in-word match of `slice` inside `isLicensedProgression`.)* |
| D-343 | The key/mode layer owns the candidate space and the note-evidence model | Which layer owns key/mode inference; its "evidence boundary" is a line between layers. |
| D-348 | Tonal distance in the change cost is circle-of-fifths distance | The key-change cost. |
| D-349 | The key/mode confidence compares whole readings | How the key confidence is computed. |
| D-353 | The key/mode layer is graded on two goals kept apart | How the key/mode layer is graded. |
| D-376 | The joint key-and-chord step was designed as a BOUNDED COUPLING | The shape of the key-and-chord coupling, since shelved. |
| D-380 | The carry's meaningful axis is DISTINCT ROOTS | What the chord layer hands forward. |
| D-382 | The function layer selects by JOINT CONSISTENCY | The function layer's selection objective. |
| D-386 | No fourth hand-rolled scan for the best different-root alternative | Where the pedal reader takes its confirmation margin from. |
| D-387 | A contradiction with the function context is surfaced on the ONE open mark | How that contradiction is surfaced. |
| D-392 | The later voice-leading components are CLAIMS WITH OWNERS | The voice-leading dimension's build sequencing. |
| D-394 | Reducing a chord-bearing voice to one line is a DECLARED parameter | The voice-leading dimension's reduction rule. |
| D-400 | A PER-VOICE span kind is admitted to the span typology | The span typology and the phrase span's tiling law. |
| D-425 | The uncertainty surface's contract IS the full posterior | What the analysis publishes about its own uncertainty. |
| D-454 | The grouping layer detects nothing | The grouping layer's scope. |
| D-455 | A cadence away from a grouping boundary is surfaced as internal | Cadence alignment to punctuation spans — a different span kind. |
| D-457 | A group truncated by the selection edge is marked as truncated | The grouping layer's marking of a group or key area truncated by the selection edge; it discloses that the slicer distinguishes an artificial clip boundary from a musical one — the existence of a distinction, not its rule (Ruling 3 of the withheld-family sitting). *(Ruled OUT 2026-08-22, from UNPLACED.)* |
| D-459 | The key-area confidence is a declared margin-class boundary confidence | The grouping layer's published key-area confidence. |
| D-463 | The temporal signals in the vertical scorer stay where they are | A known structural debt in the dormant vertical scorer; it ranks no evidence class against another. |
| D-464 | No further progression-level signal in the single-step look-around | Which structure carries progression-level signals. |
| D-474 | No published study reports per-axis inter-annotator agreement | The ground-truth ceiling. *(Reached the list only through an in-word match of `release` inside "released".)* |
| D-476 | The phrase-boundary primitive is owned by the notation-derived view layer | The PHRASE boundary — a different span kind — and its owner. |
| D-477 | Phrase boundaries are read from the written surface alone | The phrase-boundary primitive's inputs; its exclusion of harmonic evidence is the opposite question. |
| D-478 | A phrase boundary is a peak in a continuous strength profile | The phrase-boundary model. |
| D-479 | The boundary cues run per eligible voice and aggregate to the texture | The phrase-boundary primitive's scope. |
| D-480 | The phrase-boundary primitive is NOT an accuracy requirement | The phrase-boundary primitive's proportionality. |
| D-481 | The notated markers are emitted as boundaries unconditionally | The phrase-boundary picking rule. |
| D-484 | The phrase-boundary primitive is a derived view | The phrase-boundary primitive's context obligation and confidence class. |
| D-485 | Each picked boundary should carry which cue fired and at what scope | The phrase-boundary primitive's owed provenance. |
| D-490 | FALSIFIED: no threshold can make the fine-grain override net-positive | That override's viability; "grain" appears only inside "fine-grain". |
| D-495 | Cadence admission relaxes when the phrase-boundary profile is flat | Cadence admission against the phrase-boundary profile. |
| D-526 | The joint state's chord axis is SCALE-DEGREE-VALUED | The chord axis's representation as a scale degree; it names a segmenter prior at the head of a gap in order to say it dissolves — the existence of a prior, not a rule (Ruling 3 of the withheld-family sitting). *(Ruled OUT 2026-08-22, from UNPLACED.)* |
| D-527 | There is NO live non-chord-tone cleaning stage | The emission factor and ornament labelling; it ranks no evidence class and locates no boundary. |
| D-531 | The hand-built emission is CONFIRMED and the learned replacement is NOT triggered | Whether the scorer is replaced by a trained model. |
| D-534 | The penalty for a chord tone that never sounds is COUNTED per chord factor | The missing-tone penalty's values. |
| D-536 | The bass note and the chord are chosen TOGETHER | The dormant vertical scorer's internal ordering. |
| D-584 | The perfect/imperfect cadence call is made on the BASS-DERIVED inversion | Cadence typing, and why the structural melody is unavailable to that layer. |
| D-589 | Every idiom mixture is selectable and the discovered cloud is the EVIDENCE MAP | The style system; its "boundary" is the edge of the measured idiom cloud. |
| D-605 | The local-key hypothesis derives from key-agnostic signals ONLY | What evidence a MODULATION decision may read — the key axis's circularity guard. It is the sole group-E entry and its content is not the chord boundary. |
| D-613 | Ground truth for IMPLIED polyphony is confirmed ABSENT | Corpus availability for voice and stream separation. *(Reached the list only through an in-word match of `release` inside "released".)* |
| D-623 | A selection-aware capability is a PARAMETER on the one orchestrator | Orchestration — that one path builds, slices and decodes. |

---

## LIST THREE — UNPLACED: the entry's own text does not settle it

**RULED 2026-08-22 (Ruling 3, the user's word: "B"). THE LIST IS NOW EMPTY.** The three entries it
carried could not be defended either way in one sentence at the entry's own verbatim, so they were
not guessed and no recommendation was made on any of them. The user ruled each:

- **D-569 → IN**, and it is now the sixteenth row of LIST ONE. Its leak is the oracle's own
  vocabulary, and the comparison could not distinguish recovery from recall.
- **D-457 → OUT**, and it is now a row of LIST TWO. It discloses that the slicer distinguishes an
  artificial clip boundary from a musical one — the existence of a distinction, not its rule.
- **D-526 → OUT**, and it is now a row of LIST TWO. It names a segmenter prior at the head of a gap
  in order to say it dissolves — the existence of a prior, not a rule.

*The heading stays because the value stays in the generator's closed three-value vocabulary: DEFAULT
NOTHING still governs every later candidate, so a future subject's derivation can put an entry here
again. What was read at each of the three is preserved as that entry's finding in the generator's
authored table and at `tools/audit/derivation_boot_pack.json` →
`subjects.harmony-boundary.THE_CANDIDATES_AND_THEIR_VERDICTS` (#12); nothing was deleted.*

---

## LIST FOUR — LEAKS: entries the pack could not render for a different reason

*The pack's two GENERATED members — the design-intent file and the defect-type catalog — are string-
checked before rendering. An entry whose rendered text carries a withheld identity, the withheld
document's name, a `docs/` or `src/` path, or the string `ARCHITECTURE.md` is not rendered; it is
listed instead. **The scope is those two members only**: the four members quoted whole are ruled
whole and are not string-checked, because member (2) names `ARCHITECTURE.md` in the
never-work-from-memory rule by design.*

| ID | Title | Field | What matched |
|---|---|---|---|
| D-270 | The held-out evaluation protocol — five-fold cross-validation grouped by ground-truth analysis file | verbatim | a `docs/` path |
| D-296 | READING MuseScore's engraving code is allowed; only EDITING it is off limits | verbatim | two `src/` paths |
| D-440 | The language-model integration is purpose-built | verbatim | a `src/` path |

*Each match is published with its exact matched string at
`tools/audit/derivation_boot_pack.json` → `subjects.harmony-boundary.LEAKS.entries`.* **None of the
three bears on this subject** — the leak check is about pointing INTO the implementation's own
documents, not about the oracle.

**RULED 2026-08-22 (Ruling 4, the user's word: "A"): THE CHECK STANDS AS IT IS**, and the three stay
listed rather than rendered. The two alternatives were declined at the ruling — rendering with the
matched path redacted, which would be a hand edit to a ratified entry's verbatim inside a generated
member and a second copy differing from the decisions register (#6); and dropping the `docs/`/`src/`
path test, which is the test that catches routes into code and is what the phase definition's
constraint is about.

---

## LIST FIVE — the withheld PASSAGE

*Ruled by you on 2026-08-22 (Ruling 1 of `cowork_rulings_2026_08_22_member_two_leak_sitting.md`) and
**WIDENED by you the same day** (Ruling 5 of the withheld-family sitting, the user's word: "B"). It
is listed as a fifth list because it is the one withholding that cuts into a member rendered whole.*

- **Where:** `CLAUDE.md`, the Conventions span — boot-pack member (2) — inside the bullet opening
  `**NEVER WORK FROM MEMORY INSTEAD OF DOCUMENTED FACTS`.
- **What, as WIDENED:** the whole founding-instance clause, located by its own text and never by
  line number: the span opening *"**Founding instance:** on 2026-07-28 Cowork reasoned"* and closing
  *"which is the general case, not the exception."* **The widened span CONTAINS the span ruled at
  the member-two-leak sitting** — which opened at *"the specification states it explicitly and
  twice"* and closed at *"ranked the STRONGEST evidence)"* — so this is ONE authored passage with
  wider anchors replacing the narrower ones, not a second passage (#6). **The statement of the
  never-work-from-memory rule itself, above the clause, stays whole in the pack.**
- **Why the narrower cut was widened:** the application was confirmed as meant, and the residue it
  left told a deriving session that a documented decision on this subject exists, is more specific
  than a summary of it, and is contradicted by the implementation — the existence of the ruled
  answer, disclosed without its content. The wider anchors remove the clause whole.
- **Why the passage is withheld at all:** it states both halves of the withheld answer for this
  subject — where a chord boundary falls and which evidence ranks first — and it carries no withheld
  identity and no withheld document name, so no string check would have caught it.
- **How it is applied:** the span is cut from the rendered member and the omission is marked in
  place with one line saying that a passage is withheld for this subject, carrying no content and no
  reason. `CLAUDE.md` itself is untouched.
- **The exact text matched, and its length, are published** at
  `tools/audit/derivation_boot_pack.json` →
  `subjects.harmony-boundary.THE_WITHHELD_FAMILY.passages`, so the cut is checkable without
  reopening the file.

**The bound the ruling itself states, repeated here because it is easy to lose:** the span was
searched for the oracle's own phrases and **not** for every paraphrase. This surface does not claim
member (2) carries no other leak.

---

## What was ruled

**2026-08-22, one list per turn, in the order below. The record is
`cowork_rulings_2026_08_22_withheld_family_sitting.md`.**

1. **LIST ONE — "A".** It stands as authored: all sixteen IN entries are withheld. *(Recorded beside
   the ruling: D-450 and D-575 are withheld on a reading of the test wider than its words. If the
   blind session's specification later cites the notated key signature as evidence for a chord
   boundary, that is read against the pack's silence on these two and is not scored as a method
   failure.)*
2. **LIST TWO — "A".** It stands as authored: all OUT entries are admitted, D-339 among them as a
   principle the derivation is meant to apply across every axis rather than an answer it is meant to
   find.
3. **LIST THREE — "B".** D-569 IN; D-457 and D-526 OUT. The list is now empty.
4. **LIST FOUR — "A".** The leak check stands unchanged; the three stay listed and not rendered.
5. **LIST FIVE — "B".** The application is confirmed as meant, **and** the withheld passage is
   widened to the whole founding-instance clause.

**The two rulings that moved the artifact are 3 and 5, and this commit applies them:** the
generator's authored table carries D-569 IN, D-457 and D-526 OUT, and one withheld passage at the
widened anchors; the pack is re-rendered from it and its check is green.

## What the ruling does NOT do

- **It boots no session.** The blind derivation is a separate, later act, opened only after this
  ruling.
- **It does not settle who derives.** Ruling 1 of
  `cowork_rulings_2026_08_22_deriving_side_sitting.md` names a fresh Cowork session; that ruling
  stands and is not re-opened here.
- **It edits no governing document.** `CLAUDE.md`, `ARCHITECTURE.md`, `DEFECT_TYPES.md`,
  `cowork_design_doc_template.md`, `cowork_audit_protocol.md`, the phase-definition surface,
  `DECISIONS.md` and the register's own data are byte-unchanged by the act that produced this file.
- **It moves no register entry and no status.** Withholding an entry from one pack says nothing
  about that entry's standing.
- **It closes no open item.** [[OI-179]] stays OPEN and GATES; [[OI-372]] and [[OI-374]] stand as
  found.
- **It does not claim the candidate list is complete.** The criterion's reach is unmeasured and
  said so above.

---

*Provenance: Claude Code, 2026-08-22, at the tree carrying commit `a12cc0350322dd286708dcbf19d95548b01f7d55`
(`cc_instruction_pilot_preparation_withheld_family.md` Task 1). Every list above is authored from the
entry's own verbatim and plain restatement, read at
`tools/audit/decisions/backbone_decisions.json` through the file tools; the candidate population, the
matching criterion per candidate, the derived cross-reference additions, the leaks and the withheld
passage are DERIVED and published whole at `tools/audit/derivation_boot_pack.json`, from which every
figure is to be read. TOWARDS the ultimate objective and TOWARDS the guiding principles.*

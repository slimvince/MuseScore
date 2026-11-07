# Decision surface — L3-S17, the cadence type (third cadence surface), 2026-11-03

> **STATUS: DECISION SURFACE, NOT RULED.** Cowork, 2026-11-03 (Stockholm), the sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_five.md`. Delivered to the user in conversation
> first, then checked in the next turn (§B), then written here with the check's corrections applied in place and the
> former wordings kept in §B (#12). **The user has ruled nothing on it.** It lands in git at the next dispatch's Task 0.
> A new Cowork session re-presents it from this file, then puts Decision 1 alone, then Decision 2 alone (§C).

## A. The surface, as corrected

### A.1 What is being decided

L3 is the layer that reads things off a settled tonal reading — cadences, phrases and sections, chord symbols, figured
bass. Two rulings already fix the cadence: it is published only at a phrase end L3 has decided
(`cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md`, Ruling 1), and it is made of six defining features, each
read off a lower layer (`cowork_rulings_2026_11_03_l3_cadence_features_sitting.md`): (1) where the arrival falls and its
metric strength; (2) the last two or three chords, in the arrival's key; (3) whether the key at the arrival differs
from the key before the phrase; (4) any suspension or appoggiatura at the arrival; (5) whether the phrase end is
elided; (6) the scale degree of the highest sounding pitch at the arrival — now computable, since L1 is to publish the
highest sounding pitch per slice (Ruling 2 of that record).

**L3-S17** (`cowork_blind_derivation_l3_2026_10_17.md`, lines 578–608): *"The cadence type is a view of the defining
features under a declared vocabulary. Which vocabulary is principal is not decided here (OQ-L3-2 ★). Every type of the
declared vocabularies is a deterministic function of L3-S16's features, and a type that cannot be computed carries a
named reason. The cases where the traditions disagree are named, not settled."* Its sources on the traditions are
relayed through the derivation, not read: Caplin (an authentic cadence needs a root-position dominant; an evaded
type); the American textbook convention (an inverted V–I is an imperfect authentic cadence); de Clercq's chorale study
(adds a subdominant stop and *no cadence*).

**D-584** (`decisions/group_J.md`, LIVE, ratified by the user; home `ARCHITECTURE.md:2111-2118`): the
perfect/imperfect call is made on the bass-derived inversion; the soprano arrival degree is a soft optional nudge; the
layer never attempts melody identification. Ground: the highest sounding voice is often a doubling, and in some
textures the lead sits below the top.

The reading file (`ratification_surfaces/cowork_comparison_l3_reading.md` §7) lists 29 DIFFERS rows against L3-S17:
2.7 (i), 2.9, 7.1 (i), 7.8, 7.31 (ii), 7.35, 7.44 (i), 7.96, 7.99, 7.100, 7.101 (i), 7.102, 7.103, 7.104, 7.106,
7.107 (ii), 7.115 (i), 7.189 (i), 7.269, 7.301 (i), 7.329 (i), 8.11 (i), 8.40 (i), 8.59 (i), 8.88 (i), 28.47,
38.26 (i), 46.14, 57.60 (i). All 29 were read at §6, whole, by this sitting, and Rows 7.97, 7.109, 7.110 to 7.114, 8.37,
8.38 beside them. Each row is placed once below.

### A.2 What follows from the standing principles (for ratification as derivations — Decision 1)

- **a. The type is L3's, read off L2's decided chords** — Rows 8.88 (i) (type made by the old function layer and
  carried verbatim), 7.99 (the authentic-versus-passing call a key-layer judgment: RELOCATED to *L2 — The tonal
  reading*, as Row 7.98 was by Ruling 1a of 2026-11-03), 38.26 (i) (*"A cadence is a V→I"*). Follows from the charter
  (`FRAMEWORK.md` L3 block: *"A cadence type is a claim about what the decided chords do at a decided phrase end"*) and
  item a of the cadence-placement Ruling 2. Row 28.47 (a statement about `detectCadences()`'s current behaviour)
  QUARANTINED as the reading file proposes, on the ground of item c of that Ruling 2. **Documentation only.**
- **b. Row 7.104 (the perfect/imperfect branch is total).** With feature (6) computable, the split is computable
  wherever the last chords and the highest pitch carry values and the vocabulary's definition is written; *type not
  computable* remains only where a feature is missing (L3-S17, L3-S18). L3-S17's status sentence *"Feature (6) blocks
  the PAC/IAC split in every vocabulary until OQ-L3-4 is ruled"* is overtaken; its correction is the application act's.
  **Documentation only.**
- **c. Row 7.115 (i), the evaded cadence.** Defined by what the next phrase does instead of arriving; no feature holds
  it; published as *type not computable* with that reason until OQ-L3-5 (thematic parallelism). **Documentation only.**
- **d. Rows 8.37 (i) and 8.38 (i)** — L3 never identifies a melody or structural line: follow from Ruling 1c of
  2026-11-03. **Documentation only.**
- **e. Row 7.109 (the half cadence) ADOPTED — proposed, with Rows 7.110 (i), 7.111, 7.113, 7.114 (i) travelling with
  it, and Row 7.97 (i) (an authentic cadence does not need the seventh)** — adopted as types or rules of the declared
  vocabularies; each vocabulary's exact wording is written from its source when that vocabulary is declared (§A.5).
  **Documentation now.**

### A.3 Decision 1 — the perfect/imperfect split (a genuine choice, after the check)

Rows 2.7 (i), 2.9, 7.1 (i), 7.31 (ii), 7.100, 7.101 (i), 7.102, 7.103, 7.106, 7.107 (ii), 7.189 (i), 7.269,
7.301 (i), 8.40 (i) — fourteen rows — restate D-584. Row 46.14's *"perfect/imperfect by inversion"* clause bears here
too; the row is counted once, in §A.4.

- **Alternative A — publish the split both ways.** Each declared vocabulary publishes its perfect/imperfect split as
  two separately named views: on the bass-derived inversion alone, and on the inversion plus the highest sounding
  pitch's degree. The second carries the status *not yet validated*, so no consumer may put it under load until a
  measurement establishes it (#19; the fact-publication corollary's amendment of 2026-07-12). Towards the objective:
  nothing is lost (#12), and the measurement that would show which criterion is more precise becomes possible. Towards
  the principles: under the user's ruling of 2026-10-07 (Ruling 6 of
  `cowork_rulings_2026_10_07_l2_chord_tone_membership_sitting.md`) a design rule holds while there is no reason to
  suspect that breaking it would improve the inference; the reason here is that some tradition, as relayed by the
  derivation, reads the soprano's degree at the arrival (theory, no source fetched; de Clercq's model relayed). *This
  side's readings, unchecked:* that the ground-truth annotators decide perfect versus imperfect by the melody, and that
  in chorales the highest pitch is nearly always the soprano (voice crossing exists). **Algorithmic:** D-584's "the bass
  alone decides" superseded at L3 in that respect.
- **Alternative B — keep D-584 at L3.** The split rests on the bass-derived inversion alone; feature (6) is published
  and no type reads it. Towards the objective: the bass is the robust fact, and D-584's ground (doubling, a lead below
  the top) stands. Towards the principles: D-584 is a user-ratified rule; one label per cadence per vocabulary.
  Against: if the relayed theory and the unchecked readings above hold, it builds in a known disagreement with how the
  ground truth is made, and leaves it unmeasurable.
- **Meta level of both:** the analysis itself.
- **Recommendation: A**, as the course that loses nothing and lets the question be settled by measurement — with its
  ground stated at the strength §B leaves it, not stronger.
- **Row 2.9's confidence half** (*"the top voice may nudge the confidence"*) goes with L3-S19, where a cadence's mass is
  set; not on this surface.

### A.4 Decision 2 — OQ-L3-2 ★, the principal cadence vocabulary

Rows 7.8, 7.35, 7.44 (i), 7.329 (i), 8.11 (i), 8.59 (i), 46.14, 57.60 (i) fix one list of types. Row 46.14's reading-file
proposal is UNPLACED because no charter names the catalog it comes from. The derivation's question (lines 1204–1210):
which theory names the principal type, or is none principal, with every declared vocabulary's view published side by
side?

- **None principal at L3.** For: decides no question of theory on no evidence; loses nothing. *This side's readings:*
  no layer consumer needs a single label — the section grouping takes cadential evidence as fitted terms (L3-S23) and
  could read the features; the mapping to the annotators' labels is *proposed* (Row 57.60 (ii), not ruled) for the
  measurement-design stage. Against: the charter says *"the cadence at each phrase end, with its type"*, singular —
  read here as one type per vocabulary, a reading, not a ruling.
- **The old project list principal** (perfect authentic, imperfect authentic, half including Phrygian, deceptive,
  plagal, evaded). For: the old documents used it, and they state it is a superset of the DCML standard's six labels
  (Row 57.60 — the old text's claim, not checked at the standard). Against: chooses a theory without stated reason;
  its definitions are the project's own.
- **Caplin principal.** For: an inverted V–I is not an authentic cadence; the evaded type exists; the one staged case
  (exemplar 1 bar 4, `V6 V65 I` at a phrase end with no cadence label, read at the file by the derivation) fits it.
  Against: not read at its source; one case.
- **The American textbook set principal.** For: widely taught (relayed). Against: not read at its source; the staged
  case above leaves the inverted close unlabelled, which this set would call an imperfect authentic cadence.
- **Meta level of all:** the analysis itself.
- **Recommendation: none principal at L3**, the display's first-shown type a presentation setting.
- **Algorithmic:** none principal changes nothing beyond L3-S17's form; any one principal adds a principal-type field.

### A.5 Carried open, not decided

- **Row 7.96** — the old authentic-cadence rule requires the leading tone to resolve to the tonic as an event; none of
  the six features holds motion within a voice. If a declared vocabulary needs it, a seventh feature is needed, possibly
  from the voice-leading axis, which L3 does not read (L3-S42). UNSETTLED.
- **Each vocabulary's definitions are written from sources actually read** (theory-grounding corollary; D-254): Caplin,
  the American textbook tradition and de Clercq are relayed, not read. Focused research precedes the writing.
- **The charter's "with its type"** in the singular (§A.4).
- **The DP-N analogy:** DP-N stands *"NONE CHOSEN — underived: open, needs a ruling or new research"*
  (`FRAMEWORK.md`); it is not a precedent for publishing every reading side by side.

### A.6 The currently decided method

A cadence is published only at an L3-decided phrase end, carrying six features read off lower layers; feature (6)
becomes computable once L1 publishes the highest sounding pitch per slice; L3 never identifies a melody. The
perfect/imperfect call stands as D-584 at its home (bass-derived inversion) until Decision 1 is ruled.

## B. The check, run in the turn after delivery — ten corrections

1. "Every tradition it cites defines the perfect authentic cadence by the melody arriving on the tonic" — overstated;
   narrowed to the derivation's relayed theory. *(Former wording kept.)*
2. "The annotations we grade against are made that way"; "in the chorale corpus the highest sounding pitch is the
   soprano melody" — unchecked; labelled as this side's readings.
3. "The American textbook set … matches the chorale annotators' habits as the derivation reports them" — **wrong**:
   the derivation's staged case (exemplar 1 bar 4, inverted V–I unlabelled) points the other way.
4. "Keeping D-584 by rule would do exactly that" (decide a theory question silently) — **wrong**: D-584 was ratified
   openly. In consequence Decision 1 is a genuine choice, no longer a derivation (the delivered surface had it as item
   d of the derivations).
5. "Already placed with the measurement-design stage" — only proposed (Row 57.60 (ii)); "the section grouping can read
   features" — this side's reading.
6. "The split is now always computable" — narrowed (§A.2 b).
7. "Fifteen rows" in the D-584 group — fourteen; Row 46.14 counted once, in the vocabulary group; its UNPLACED proposal
   stated.
8. Rows 8.37 (i), 8.38 (i) omitted — added (§A.2 d); Rows 7.110 (i), 7.111, 7.113, 7.114 (i) travel with 7.109 —
   added.
9. "A superset of the DCML standard's six labels" — the old text's claim, not checked at the standard.
10. The DP-N analogy leaned on harder than its text allows — stated at §A.5.

**The sitting's own state.** Corrections 1, 3 and 4 are the degradation signs the user's standing rule of 2026-08-15
names (a claim wider than its source; hedged assertion about unexamined things). The sitting recommended handover at
this verified stop and put no question.

## C. What the next session does with this file

Re-present §A in its own turn, self-contained, plain English (it may re-check any row at §6). Then Decision 1 alone, in
a later turn, no widget. Then Decision 2 alone. Then the ratification of §A.2's derivations a to e as one question,
alone. Write the ruling record in the turn each ruling is given.

*Provenance: Cowork, 2026-11-03 (Stockholm). The user's words: the opening instruction; "continue"; "continue";
"continue".*

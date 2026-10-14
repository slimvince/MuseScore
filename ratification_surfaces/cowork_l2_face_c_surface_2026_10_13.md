# Ratification surface — face (c) of the L2 specification: the tonality at each moment

> **STATUS: DECISION SURFACE, delivered for reading. Nothing is asked in the turn that delivers it.** Cowork,
> 2026-10-13 (Stockholm), the sitting booted on `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_eighty_one.md`.
> The check of this surface is the next turn's; the question comes after that, alone. Nothing here is applied:
> every change named below is made later by a dispatch, and nothing is ratified by this file.

## 0. What is being decided, from the beginning

**The file under ratification** is `cowork_derived_specification_l2_2026_10_10.md`, the "successor". It is the
specification of L2, the layer that decides for each stretch of music the tonality, the chord, where one chord
gives way to the next, and which sounding notes belong to the chord. A deriving session wrote it blind, and it was
then amended by the forty-three L2 family rulings of 2026-10-04 to 2026-10-10. Its banner says NOT RATIFIED.

**How it is ratified.** On 2026-10-13 you ruled "option 3, one aspect at a time", so the file is ratified one face
at a time, nine surfaces in all (`records/cowork/rulings/cowork_rulings_2026_10_13_l2_ratification_granularity_sitting.md`).
Face (a), statements L2-S1 to L2-S10, was ratified the same day ("ratified"), and face (b), L2-S11 to L2-S15, also
the same day ("yes"). Their ruling records are `cowork_rulings_2026_10_13_l2_face_a_ratification_sitting.md` and
`cowork_rulings_2026_10_13_l2_face_b_ratification_sitting.md` in the same folder.

**Face (c)** is the third face: the seven statements L2-S16 to L2-S22 (successor lines 607 to 910). Together they
say: each harmonic stretch has exactly one tonality (L2-S16); the written key signature is only a weak lean
(L2-S17); a chord that can be heard as an applied chord in the current key can also be heard as a plain chord in a
new key, and both readings are kept (L2-S18); a pivot chord is published in one key, with the other key's reading as
a rival (L2-S19); what the tonality evidence reads, and what it does not read (L2-S20); the minor mode with its
variable sixth and seventh degrees and the Picardy third (L2-S21); and how L2 reads music beyond the selection and
when it stops asking for more (L2-S22).

A "statement" in this file has six fields: the statement itself (in bold), its defense, its source class, its
status, its premise with the way the premise could fail unnoticed (the "false-negative path"), and its falsifier
(how to test the code against it). Rulings are written beneath a statement as short sub-items.

## 1. What was read for this surface (each at the object, this sitting)

**The successor:** §0 and §2 (lines 1–101); §3c whole (lines 607–910); OQ-L2-3's opening and its first four added
items (lines 1995–2016); OQ-L2-5 and OQ-L2-6 (lines 2088–2100); the carried item beside L2-S44 that names L2-S16
(lines 1752–1754).

**The ruling records, whole:** pivot chord (2026-10-05), key-signature prior (2026-10-05), tonality evidence
(2026-10-06), tonality and progression terms (2026-10-06), applied chord or new tonality (2026-10-07), four agreeing
statements (2026-10-07), one tonality per span (2026-10-07), context at the edge (2026-10-07). The silence-and-no-chord
record (2026-10-05) at lines 105–129 only. The tonality-vocabulary record (2026-10-04) searched only.

**The application dispatch** `records/cc/instructions/cc_instruction_l2_application_2026_10_10.md`: its
construction-state table (lines 1–69, including the stale-field row at line 68); §L.5 (lines 739–777); §L.10
(lines 982–1098); §L.18 at lines 1905–1959; §L.19 at lines 1995–2064 and 2100–2113; §L.21 at lines 2314–2322; §L.23
(lines 2520–2628); §L.25 at lines 2756–2839; §L.29 (lines 3174–3282); §L.31 (lines 3399–3587); §L.41 at lines
4886–4904; Task 1 at lines 5446–5449. For every other line of the dispatch that names one of the seven statements
(lines 1298, 2661, 2688, 3090, 3131, 3149, 3636, 3690, 3824, 3855, 3870, 4390, 4401, 4709, 5904), a fragment of up to
about 160 characters either side, returned by a search.

**How the rulings were found.** By the method entry 379 §2 set: the dispatch's §L entries were searched for the
seven statement identifiers. That found seven of the eight records above as the families of these statements (the
tonality-and-progression record is L2-S34's family, read here for its bearing on L2-S18 and D-337) and no other
record ruling on these statements' wording; the other mentions are rows' filing lines. **The search finds a ruling only where the dispatch
names the statement by its identifier**, so a ruling that bears on one of the seven without naming it is not found.
One such case is known from this sitting's reading: tonality-vocabulary Ruling 1 of 2026-10-04 (L2's modes are major
and *composite minor*) bears on L2-S21 without naming it; the four-agreeing record pairs them ("L2-S21 with
tonality-vocabulary Ruling 1"). They agree.

## 2. The seven statements, checked against the rulings' words

- **L2-S16 — one tonality per stretch, changing only at a boundary between stretches.** *Rulings:* pivot chord
  Ruling 1 ("one"), whose ruling paragraph ends "**L2-S16 stands as derived**, untouched by this ruling" — shown in
  the successor as a sub-item pointing at the quotation beside L2-S19. One tonality per span Ruling 1
  ("confirmed"): "L2's algorithm as its statements define it is unchanged; L2-S16's wording does not change." —
  **not shown.** **Matches.**
- **L2-S17 — the written key signature is a weak lean on the tonality, at the start and at each notated signature
  change, and nowhere else; it never forbids a reading; the file's hidden major/minor tag is not read.** *Rulings:*
  key-signature prior Ruling 1 ("confirmed": the last sentence, on the hidden tag, stands as derived), Ruling 2
  ("confirmed": the first sentence amended to act only at the start and at each notated signature change, the
  every-stretch pull excluded by name) and Ruling 3 ("confirmed": the spread stands as derived; the sizes are held
  out under OQ-L2-3). All three are shown, with the former first sentence kept. The new first-sentence words were
  written by the dispatch from Ruling 2's words (see §3, point 1). The Premise's false-negative path and the
  Falsifier were brought into line on your word "B" of 2026-10-13. **Matches.**
- **L2-S18 — an applied chord in the current key and a plain chord in a new key are both admitted and both kept as
  rivals; the candidate score over the whole passage picks the principal one, not a rule.** *Rulings:* applied chord
  or new tonality Rulings 1, 2 and 3 ("confirmed" each), each stating "L2-S18's wording does not change" — **not
  shown.** Ruling 1's carried bullet on D-291's measured cadence figure is shown beside L2-S18, with a pointer to the
  accepted cost quoted beside L2-S34. **Matches.**
- **L2-S19 — a pivot chord is published as one stretch in one key, the other key's reading as a rival with its
  weight.** *Ruling:* pivot chord Ruling 1 ("one"): "L2-S19 stands as derived; its status 'Open (OQ-L2-5 ★)' closes.
  OQ-L2-5 is answered". Shown, with the Status set to Settled and the Falsifier turned into a code test, marked as
  "the surface's reading, not ruled separately". **Matches** — but the bold statement's last sentence still says the
  question is yours to answer (§4, correction 2(a)).
- **L2-S20 — the tonality evidence reads the chords the reading proposes and a recency-weighted account of which
  spelled scale degrees have sounded, never a whole-stretch pitch-class profile.** *Ruling:* none on its wording.
  The tonality-evidence record says, in its §1g and under no ruling heading, "L2-S20 stands as derived; Ruling 4
  adds one candidate to OQ-L2-3 and Ruling 3 one reporting requirement to the same measurement, neither changing
  L2-S20's wording." Shown as a recorded sub-item, with the two additions under OQ-L2-3, pointers beside L2-S20, and
  the five rulings' accepted costs and named remedy. **Matches.**
- **L2-S21 — the minor mode is one mode whose sixth and seventh degrees may each be raised or not; the Picardy
  third is a chord of the minor key.** *Ruling:* four agreeing statements Ruling 1 ("yes"): "no wording of L2-S3,
  L2-S9, L2-S15 or L2-S21 is changed by this ruling". **Not shown**; nothing stands beside L2-S21. **Matches.**
- **L2-S22 — at the edge of the selection L2 asks for more music and stops when its publication stops changing.**
  *Rulings:* context at the edge Ruling 1 ("Confirmed"): "L2-S22's wording does not change by this ruling"; Ruling 2
  ("2"): the last sentence replaced — at the top effort setting nothing published may still be moving; below it, a
  tolerance on the weights set by the effort setting; the principal reading unchanged at every setting; the safety
  cap ends a loop that does not settle, and the result is marked as truncated. **Ruling 2 says in terms that it
  changes L2's algorithm** (the stopping rule). Shown: the amendment with the former sentence, the declined positions,
  the recorded readings, the Status and Falsifier brought into line, and a pointer at the Defense's overtaken last
  sentence. **Matches** — the Premise is out of step (§4, correction 2(b)).

## 3. The points the dispatch noted for you, each tested against the record (D-599)

Each point below is answered by the record or by a rule already ratified, so none is put to you as an option.

1. **L2-S17's new first sentence** reads "The written key signature enters as one term of the candidate score, a
   weak prior over the spans' tonalities that acts at the start and at each notated signature change, and nowhere
   else." Ruling 2's own words are "a weak lean on the tonality at the start and at each notated signature change,
   and nowhere else"; the dispatch kept "the spans' tonalities" so that "them" in the next sentence ("It never
   constrains them") still has something to refer to. **It stands.** The words are authored, so you may change them.
2. **L2-S17's Premise and Falsifier** — settled by your word "B" of 2026-10-13 (rewritten in place, former wording
   kept). Nothing remains.
3. **The D-291 bullet stays beside L2-S18.** It comes from L2-S18's own family record, in the same ruling that says
   L2-S18's wording does not change, and it bears on the choice L2-S18 describes (a cadence tends to confirm a real
   key change; L2 carries that tendency as a fitted term, not a rule).
4. **Ruling 2's sentence on the D-minor and F-major readings stays in Row 5.177's filing line.** L2-S18's bold text
   already says both readings are admitted and kept, and its Defense already cites exemplar 3's `V7/III` in D minor.
   Writing it beside L2-S18 too would say it twice (#6).
5. **L2-S20's "Stands as derived" sub-item stays in its recorded form** (marked as the record's derivation, not a
   ruling), because the sentence sits in the record's §1g under no ruling heading. Face (b) gave the same answer for
   L2-S11.
6. **L2-S20's two OQ-L2-3 additions stay under OQ-L2-3, with pointers beside L2-S20.** The record names OQ-L2-3 as
   what each is added to. Faces (a) and (b) gave the same answer.
7. **The context-at-the-edge record's recorded paragraph stays split**: its first two readings beside L2-S22, its
   third (about a sentence in an older design document) in Row 45.58's line, the row that quotes that sentence.
8. **OQ-L2-6 is marked ANSWERED** although the record says "closed". It was closed by a ruled answer (position 2),
   so the mark says what happened. **It stands.**
9. **L2-S22's Status and Defense** — settled on 2026-10-13: the stale-field surface stated them as settled by your
   2026-09-22 rule, you did not object (relayed from the dispatch's §L.31 item 6), and both are now written (the Status amended; a pointer beside the Defense's
   last sentence, the derived wording standing).
10. **Row 45.55 has no filing line** because the ruling says "not placed now"; it keeps its proposal and travels
    with the effort setting's design. It is a row, not a statement, and changes nothing here.
11. **The "wording does not change" lines for L2-S16, L2-S18 and L2-S21** are correction 1 below. The ground on which
    you ratified face (a)'s correction C5 and face (b)'s correction 1 applies to them equally: the specification
    shows every ruling that touched a statement, by one line and a citation.
12. **The ruled sub-item beside L2-S16 from the pivot-chord record** — settled at the dispatch's check turn and
    written. Nothing remains.

## 4. What needs writing — documentation only, none of it a choice

None of these corrections changes the algorithm. The applying dispatch would write each one, keeping every former
wording in place (#12).

- **Correction 1 — one recorded line per "wording unchanged" ruling not shown**, quoting it and citing the record
  (face (a)'s C5 rule):
  - beside L2-S16, one tonality per span Ruling 1;
  - beside L2-S18, applied chord or new tonality Rulings 1, 2 and 3 (one line; the sentence is the same in each);
  - beside L2-S21, four agreeing statements Ruling 1.

  **Not for L2-S22.** Ruling 1's "does not change by this ruling" is already cited there (the recorded-readings
  sub-item names Ruling 1), and Ruling 2 of the same record then amends the statement. A line saying the wording does
  not change, written beside a statement whose last sentence the next ruling replaced, would read as a contradiction.
  This is this side's reading of how the C5 ground applies; you may want the line written anyway.
- **Correction 2 — two passages a ruling has overtaken, fixed without asking under your 2026-09-22 rule:**
  - **(a) L2-S19's bold last sentence** still reads "Whether L2 should instead be able to publish a span as a pivot,
    carrying both tonalities in the principal reading, is a question for the user (OQ-L2-5 ★)." Pivot Ruling 1
    answered it. The ruling says L2-S19 "stands as derived", so the bold text is not edited; **proposed:** a pointer
    beside it, in the shape you accepted for L2-S22's Defense and ruled for L2-S28's bold text (the L2-S28 ruling relayed
    from the dispatch's §L.31 item 8; the structural-bass record was not read) — "The statement's
    last sentence states the question as the derivation left it. Ruling 1 has since answered it (OQ-L2-5 ANSWERED).
    The derived wording stands."
  - **(b) L2-S22's Premise**, false-negative path: "a reading that never converges, such as an oscillating pivot. The
    record edge (IC Ruling 46 (vi)) ends the loop, and the record-edge mark says so." Since Ruling 2, the safety cap
    (D-624) can also end such a loop, and the result is then marked as truncated (D-263); the sentence names only the
    record edge. The stale-field list put to you on 2026-10-13 named L2-S22's Status, Defense and Falsifier, not its
    Premise.
    **Proposed**, in the "B" form you chose for the out-of-date Premise and Falsifier fields that list named
    (rewritten in place, former wording kept; applying that form to a field the list did not name is this side's
    reading):
    "a reading that never converges, such as an oscillating pivot. The record edge (IC Ruling 46 (vi)) or the safety
    cap (D-624) ends the loop, and the publication says so (the record-edge mark, or marked as truncated, D-263)."
  - *Why it is not a choice:* a sentence in the specification that is no longer true is fixed (your 2026-09-22 rule;
    #10), and both shapes are ones you have already accepted. **The wordings are this side's and you may change
    them.**
- **Considered and not proposed:** a pointer from L2-S17's Status ("Settled in shape. **Open** in value.") to
  OQ-L2-3, as face (b) added for L2-S12. Here the ruled sub-item beside L2-S17 already says "The sizes are a
  measurement, held out (OQ-L2-3)", so the pointer is already beside the statement (#6).
- **Routed elsewhere, not written now — to the ninth surface (§0 terms with §4 open questions):** whether the
  UNSETTLED items carried beside statements should also stand in §4 as open questions. Those from this face's
  records: the two beside L2-S17 (§5 below); which tonality a silent stretch carries (beside L2-S44, naming L2-S16);
  the "this chord is in both keys" label (beside L2-S19, carried to L3).

## 5. Left open by this face's rulings — carried, not decided by ratifying

- **Where exactly the key-signature lean acts (beside L2-S17, UNSETTLED).** The key-signature record left two points
  "for the application, not ruled": "at the start" of what — the piece, or the stretch the user selected and the
  analysis loaded; and whether a signature change that falls between two note change points becomes a point where
  the lean applies again. The application dispatch wrote both as UNSETTLED and decided neither; the bold text keeps
  the framework's bare words "at the start". **So the algorithm is not fully fixed at these two points**, and
  ratifying face (c) as written leaves them open; it does not decide them.
- **Which tonality a silent stretch carries** (beside L2-S44) and **whether and where the "both keys" label for a
  pivot is published** (carried to L3's own specification).
- **The effort setting's numbers for L2-S22** — the tolerance values and each setting's default are decided when the
  effort setting is built (D-202 stays deferred); whether the top setting's "nothing still moving" test settles
  before the safety cap in ordinary music is a measurement at that build. Ruling 2 of the context-at-the-edge record
  also recorded a targeted reading of the public research on this question as a next act; the research record of the
  same date filed a plan for it (relayed from the dispatch's §L.32 row; that record was not read).
- **A figure in L2-S20's Defense, for the check turn.** The Defense cites "4.6 points on tonality and 1.8 on chord"
  as the cost of separating tonality from chord (Rocher et al. 2010, Table 5, relayed). Entry 169 §4 (2026-09-13)
  records an item left with you from the second extraction of that paper: one of the compared figures is
  post-smoothed and the other has no stated smoothing status, "so the like-for-like chord figure may be 0.6".
  *Checked at the check turn:* the second extract
  (`reading_pass/extracts_second_pass/rocher-robine-hanna-oudre-2010-concurrent-estimation-of-chords-and-keys.md`,
  unchanged since 2026-09-13 at its folder listing) states at its §8(2) that the 74.9 is the post-smoothed figure and
  that whether the 73.1 was post-smoothed "is stated nowhere in the six pages as read", so the chord margin may be
  0.6 rather than 1.8; the tonality margin (62.4 against 57.8, 4.6) "carries no such ambiguity". No later ruling
  settling it was searched for beyond that file. **So the Defense's chord figure is uncertain and its tonality
  figure stands.** It is a measured value, which your 2026-09-22 rule does not let this side correct unasked; it is
  carried as stated, not written in, and it bears on the Defense, not on the statement, which also rests on the
  ratified charter (DP-B).

## 6. What the rulings of this face leave owed at the ratification act, outside the successor

- **D-605's register status** (tonality evidence Ruling 2: "settled at the ratification act").
- **A-3's register standing** (tonality evidence Ruling 5: "settled at the ratification act"), with the record's
  observation that A-3 is named as D-358 in D-494's provenance and that no D-358 row appears in `DECISIONS.md`'s index
  — "noticed, not judged". This sitting's whole read of the index, and a search of it for "D-358", also found no
  D-358 row.
- **D-337's register standing** (applied chord or new tonality Ruling 1: "settled at the ratification act"; the
  tonality-and-progression record's Ruling 2, L2-S34's family, says the same, so face (f) will meet it again).
- **The declared-mode halves of D-528, D-450, D-057 and D-056** (key-signature Ruling 1: "The register status of
  those entries is not changed here", the rule (c) suspension file being the route).

The register cannot take an entry while `cowork_register_rule_c_suspension_2026_08_28.md` is the standing route, as
the granularity and face (a) ruling records state; that file was not opened this sitting. **So these wait on that
route**, recorded and not lost, as face (a)'s D-271 item and face (b)'s list do.

## 7. The decision, and what it does

**One decision: do you ratify face (c) — L2-S16 to L2-S22 as written in the successor, with corrections 1 and 2
written by the applying dispatch, the routed item carried to the ninth surface, the open points of §5 carried as
open, and the register items of §6 carried to that dispatch?**

- **Documentation:** it marks the seven statements ratified, writes corrections 1 and 2 with every former wording
  kept, and lists the register items for the applying dispatch.
- **Algorithm:** **nothing changes by this act.** Two of the seven statements already carry rulings that changed
  the algorithm — L2-S17 (the signature's lean only at the start and at each signature change; key-signature Ruling
  2) and L2-S22 (the stopping rule; context-at-the-edge Ruling 2). Ratifying confirms them as written; it does not
  change them. Correction 1 adds lines quoting rulings already given. Correction 2 adds a pointer and brings one
  premise sentence into line with a ruling already given. The two key-signature points of §5 stay open.

**The currently decided method for face (c), in plain words.** Every harmonic stretch carries exactly one key (a
tonic, spelled, and major or minor), and the key can change only where one stretch gives way to the next. The key is
decided together with the chords and boundaries, in one decision over whole readings. The written key signature is a
weak lean towards its own major and minor keys and the keys one accidental either side; it acts at the start and at
each notated change of signature, nowhere else, and never rules a reading out; the file's hidden major/minor tag is
not read at all. Where a chord can be heard as an applied chord (V/V in C) or as a plain chord in a new key (V in G),
both readings are scored and kept as rivals with their weights, and the score over the whole passage decides which is
principal; there is no rule such as "no key change without a cadence" — a cadence helps through a fitted term. A pivot
chord is published in one key, with the other key's reading as a rival. The key evidence reads the chords each reading
proposes, with their function and cadential progressions, and a recency-weighted record of which spelled scale degrees
have sounded — never a pitch-class count over a whole stretch. In minor, the sixth and seventh degrees may each be
raised or not without a change of key, and a final major tonic in a minor piece (the Picardy third) is a chord of the
minor key, with the change to major as a rival. At the edge of the selection L2 asks for more music, the step and the
stop being its own; at the top effort setting it stops only when nothing it publishes (readings, rivals, weights) still
changes; below the top, within a tolerance the effort setting sets; the principal reading must be settled at every
setting; and a safety cap ends a loop that never settles, the result marked as truncated. **Still open:** the fitted
sizes of the signature lean and the form of the recency evidence (OQ-L2-3, with the candidates added there); where
exactly the lean acts at the start and at a mid-slice signature change (§5); the effort setting's tolerances and
defaults.

## 8. Recommendation: ratify, with the corrections

- **Towards the ultimate objective (maximum-precision inference, #4):** the audit will measure the code against this
  text. A statement that hides a ruling that touched it, or a sentence that still calls a decided question open, is
  the kind of gap that misled entry 378. The corrections remove that risk and change nothing L2 computes. The two
  open key-signature points stay visible rather than being settled in passing.
- **Towards the guiding principles:** #10 (the specification true and complete about itself); #6 (pointers and
  one-line citations, never second copies); #12 (every former wording kept); D-599 (nothing here is put as a choice
  the record settles); face (a)'s ratified C5 rule and face (b)'s corrections applied the same way; your 2026-09-22
  rule on out-of-date wording, and your "B" form for out-of-date Premise fields.
- **Meta level:** documentation of the analysis's own specification; no measurement tool, no governance rule.

## 9. Bounds of this surface

Not read this sitting: `FRAMEWORK.md` (C-2, DP-B and DP-E, which L2-S16, L2-S17 and L2-S20 cite), the L0/L1
specification (IC S-6, Ruling 46, Ruling 57), the decisions-register group files, the comparison reading file and its
rows, the eight family records' surfaces, the context-research record, the rival-publication record, the
second extraction of the Rocher et al. paper beyond a search of it (read at its matching lines in the check turn),
and the register's rule (c) suspension file. Every claim about them above is
relayed from the records, the successor or the dispatch. The exemplars L2-S17 to L2-S21 cite were not opened. The
dispatch's row-by-row placements were checked by the writing side at the time and were not re-checked here; this
surface is about the statements.

## 10. The check of this surface — run in its own turn, after delivery, at the sources

Checked for completeness, coherence, correctness and absolutes, each claim against the object it rests on. **Seven
corrections, made at their sites above; none moves a finding, a correction's content or the recommendation. One
completes an item this surface left for the check (item 5). Former wordings, preserved (#12):**

1. §1: a count that did not match its own list. Former: *"That found the seven family records above and no other
   record ruling on these statements' wording;"* — eight records are listed; the tonality-and-progression record is
   L2-S34's family.
2. §3 point 9: "you did not object" was unmarked as relayed. Former: *"2026-09-22 rule, you did not object, and both
   are now written"*.
3. §4 correction 2(a): the L2-S28 ruling was unmarked as relayed. Former: *"in the shape you accepted for L2-S22's
   Defense and ruled for L2-S28's bold text — "The statement's"*.
4. §4 correction 2(b): applying the "B" form to a field the list did not name was stated as your choice. Former:
   *"**Proposed**, in the "B" form you chose for out-of-date Premise fields (rewritten in place, former wording
   kept):"*.
5. §5, the L2-S20 Defense figure: the check was run. Former: *"This sitting has not checked whether that was settled
   after 2026-09-13; the check turn will. It bears on a figure in the Defense, not on the statement, which also rests
   on the ratified charter (DP-B)."*
6. §6, D-337: completed — the same register item is named by L2-S34's family record. Former: *"(applied chord or new
   tonality Ruling 1: "settled at the ratification act")."*
7. §9: the bound updated for the read in item 5. Former: *"the second extraction of the Rocher et al. paper, and"*.

**Checked and standing:** every quotation in §2 against its record (one tonality per span Ruling 1; pivot Ruling 1;
key-signature Rulings 1 to 3; applied-or-new Rulings 1 to 3, the same sentence in each; tonality evidence §1g; four
agreeing Ruling 1; context at the edge Rulings 1 and 2); §2's account of what the successor shows, at lines 607–910;
§3 point 1's quotation of L2-S17's bold text (lines 623–627); §4 correction 2's quotations of L2-S19's bold last
sentence (lines 734–735) and L2-S22's Premise (lines 868–870); §5's key-signature points against the record's §1b
and the dispatch's §L.10 item 3; §6's register list against the four records and `DECISIONS.md` (D-605, D-337, D-528,
D-450, D-057, D-056 present; D-358 absent); §7's method against the seven statements. **Absolutes swept** ("all",
"every", "never", "nothing", "only", "exactly"): each hit is the statements' own wording, a quotation, or a claim
about this sitting's own reading as §1 and §9 bound it.

**What the check did not do:** it searched for no later ruling on the Rocher figure beyond the second extract, and
re-opened nothing else §9 lists as unread.

*Provenance: Cowork, 2026-10-13 (Stockholm), the sitting booted on entry 381. The user's words this sitting: the
opening instruction; "continue" (the check).*

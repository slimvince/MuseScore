# Ratification surface — face (e) of the L2 specification: the chord read over each span

> **STATUS: DECISION SURFACE, delivered for reading. Nothing is asked in the turn that delivers it.** Cowork,
> 2026-10-13 (Stockholm), the sitting booted on `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_eighty_four.md`.
> The check of this surface is the next turn's; the question comes after that, alone. Nothing here is applied:
> every change named below is made later by a dispatch, and nothing is ratified by this file.

## 0. What is being decided, from the beginning

**The file under ratification** is `cowork_derived_specification_l2_2026_10_10.md`, the "successor". It is the
specification of L2, the layer that decides for each stretch of music the tonality, the chord, where one chord
gives way to the next, and which sounding notes belong to the chord. A deriving session wrote it blind, and it was
then amended by the forty-three L2 family rulings of 2026-10-04 to 2026-10-10. Its banner says NOT RATIFIED.

**How it is ratified.** On 2026-10-13 you ruled "option 3, one aspect at a time", so the file is ratified one face
at a time, nine surfaces in all (`records/cowork/rulings/cowork_rulings_2026_10_13_l2_ratification_granularity_sitting.md`).
Faces (a) to (d) — statements L2-S1 to L2-S26 — were ratified the same day ("ratified", "yes", "yes", "yes"). Their
ruling records are the four `cowork_rulings_2026_10_13_l2_face_*_ratification_sitting.md` files in the same folder.

**Face (e)** is the fifth face: the four statements L2-S27 to L2-S30 (successor lines 1049 to 1171). Together they
say what L2 decides about the chord of a stretch, and from what:
- **L2-S27:** L2 decides the chord as four fields — the degree (the Roman numeral's step, read against the
  stretch's own tonality), the quality (major, minor, dominant seventh and so on), the figure (which chord member
  is taken as the bass) and the applied target (as in "V of V"). L2 does not publish a chord symbol (root pitch
  class, quality, bass note); L3 computes that from L2's answer.
- **L2-S28:** the figure is part of the reading. It is the chord member the reading takes as the stretch's
  structural bass, which need not be the lowest note sounding at the stretch's first moment (an Alberti bass is
  the standard case). A term of the candidate score relates the figure to the lowest sounding pitch of every slice
  of the stretch, weighted by duration and metric strength.
- **L2-S29:** the cadential six-four is admitted under two readings — a tonic chord in second inversion (`I6/4`)
  and a dominant with the sixth and fourth above its bass as elaborations (`V(64)`) — and both are carried as rivals.
  Which theory is principal is not decided; the charter records that question as its own open point DP-N.
- **L2-S30:** no chord term decides a chord from the pitch-class content of the stretch alone. The chord terms
  also read the neighbouring chords (the progression), which notes count as chord tones, and the voice-leading
  evidence of L2-S24.

A "statement" in this file has six fields: the statement itself (in bold), its defense, its source class, its
status, its premise with the way the premise could fail unnoticed (the "false-negative path"), and its falsifier
(how to test the code against it). Rulings are written beneath a statement as short sub-items.

## 1. What was read for this surface (each at the object, this sitting)

**The successor:** §3e whole (lines 1049–1171); in §4, OQ-L2-3's structural-bass item (lines 2032–2043), OQ-L2-11
(lines 2139–2146) and the closing count (lines 2202–2204); a search of the whole file for the four identifiers,
"OQ-L2-11" and "bass-scale-degree".

**The ruling records, whole:** chord as degree (2026-10-08), structural bass (2026-10-08), cadential six-four
(2026-10-05), context in chord terms (2026-10-09), and chord vocabulary (2026-10-05).

**The application dispatch** `records/cc/instructions/cc_instruction_l2_application_2026_10_10.md`: its
construction-state table at lines 20–64; its section headings by search; §L.8 whole (lines 875–925); §L.33 at lines
3617–3675 and 3725–3730; §L.34 at lines 3800–3829 and 3910–3917; §L.35 at lines 3945–3975 and 4020–4025. For every
other line that names one of the four statements (lines 51, 52, 844, 855, 863, 1516, 1711, 1784, 1816, 1841,
1942, 2078, 2080, 2181, 2321, 2687, 2786, 2794, 2795, 2799, 2805, 2881, 2913, 2928, 2986, 2987, 2992, 3005–3007,
3192, 3233, 3246, 3254, 3331, 3333, 3335, 3351, 3367, 3395, 3500, 3516, 3976–4014, 4055, 4201, 4280, 4345, 4643, 4709,
4712, 4722, 5009, 5015, 5690, 5698, 5904), a fragment of up to about 170 to 250 characters either side, returned by a
search. Lines 45, 53 and 68 (rows of the construction-state table) were returned by the search as too long to show
and were not read at those hits; lines 45 and 53 were read whole in the table read at lines 20–64.

**Also read:** the face (a) surface at lines 118–147 (its corrections C3 to C6); the face (b) surface at lines 95–134
(its correction 1); the face (c) surface at lines 120–189 (its correction 1 and what it left out); the face (d)
surface whole, as the form this surface follows; `STATUS.md` whole.

**How the rulings were found.** By the method entry 382 §2 set: the dispatch was searched for the four statement
identifiers. That found one family record for each statement — chord as degree (L2-S27), structural bass
(L2-S28), cadential six-four (L2-S29), context in chord terms (L2-S30) — and the chord-vocabulary record, which
names L2-S27 for two rows it carries and L2-S29 for a row that travelled to that family; it rules on L2-S2, L2-S4
and L2-S5, not on any face (e) statement's wording. The other hits read are rows' filing lines, other records' "what
stands" lists (the dispatch says those order nothing) and notes that nothing is written beside a face (e) statement,
quotations of rulings in Task 5, a quoted open-question bullet, and other statements' text; none read orders a change
to a face (e) statement. **The search finds a ruling only
where the dispatch names the statement by its identifier**, so a ruling that bears on one of the four without
naming it is not found. One such bearing is known: the chord vocabulary L2-S27 decides over is set by
chord-vocabulary Rulings 1 and 2 (every listed chord kind its own state; a sounding ninth, eleventh or thirteenth an
elaboration). The chord-as-degree record's method paragraph names Ruling 1 ("the vocabulary is chord-vocabulary
Ruling 1's"); Ruling 2 bears on the same vocabulary without being named there. Both rule on L2-S2, L2-S4 and L2-S5,
in face (a), which you ratified with every ruling quotation beside its statements confirmed (relayed from face (a)'s
ruling record; this sitting did not re-read those sub-items).

## 2. The four statements, checked against the rulings' words

- **L2-S27 — the chord as degree, quality, figure and applied target; no chord symbol published.** *Rulings:*
  chord as degree Ruling 1 ("Confirmed."): 45 rows placed, documentation only; "**L2's algorithm as its statements
  define it is unchanged; L2-S27's wording does not change.**" Ruling 2 ("confirmed"): three rows placed at L3,
  documentation only, "L2's algorithm as its statements define it is unchanged." **Neither ruling is shown beside
  L2-S27**; the statement has no sub-item at all. The dispatch noted this for you (§L.33 item 1). **Matches** — §4,
  correction 1.
- **L2-S28 — the figure decided in the reading, with a term on the lowest sounding pitch of every slice.**
  *Rulings:* structural bass Ruling 1 ("confirmation"): 16 rows placed, documentation only; "**L2's algorithm as its
  statements define it is unchanged; L2-S28's wording does not change.**" — **not shown beside L2-S28**. Ruling 2
  ("A"): L1 publishes the lowest sounding pitch of every slice; OQ-L2-11 answered; "L2-S28's term already wants
  exactly this" — shown: two sub-items beside L2-S28 (one quoting the ruling beside the last sentence, one beside the
  Defense's "not for every slice", the derived wording standing), the Status amended on your word of 2026-10-13 with
  its former value kept, OQ-L2-11 marked ANSWERED. Ruling 3 ("A"): the bass-scale-degree prior of D-585 becomes a
  held-out measurement under OQ-L2-3 — shown: the item quoted under OQ-L2-3 (lines 2032–2043) and a pointer beside
  L2-S28. **Matches** — §4, correction 1 for Ruling 1.
- **L2-S29 — the cadential six-four under two readings carried as rivals; DP-N not decided here.** *Ruling:*
  cadential six-four Ruling 1 ("One"): "**L2-S29 stands as derived.**"; no theory is principal; DP-N stays open; the
  six-four as its own category (`Cad64`) is not a state in the first specification, named as an exclusion under
  L2-S2. Shown: the ruled sub-item, the two carried paragraphs ("The costs, carried."; "What it does not decide."),
  and a pointer to the exclusion beside L2-S2 (which you ratified with face (a)). The Status, "**Open** (DP-N, the
  charter's)", is left as derived, as the dispatch ordered (§L.8 item 1), since the record orders no change and DP-N
  is open. **Matches.**
- **L2-S30 — no chord decided from pitch-class content alone; context terms read.** *Ruling:* context in chord
  terms Ruling 1 ("confirmed"): 27 rows placed, documentation only; "**Algorithm: unchanged.** L2-S30's wording does
  not change; nothing is added to or taken from the candidate score." **Not shown beside L2-S30**; the statement has
  no sub-item. The dispatch noted this for you (§L.35 item 1). **Matches** — §4, correction 1.

**The Premise and Falsifier fields.** No ruling of this face amended a statement's bold text, so no Premise or
Falsifier has fallen behind its statement. The two fields a ruling overtook — L2-S28's Status and its Defense's "not
for every slice" — have been brought into line (the Status amended, the Defense given a sub-item). L2-S28's Premise ("The structural bass is a reading decision, not a notated fact") and Falsifier (falsified if
the figure is set by a fixed rule from one slice's lowest pitch) are untouched by Ruling 2, which changes what L1
publishes, not what L2 decides.

## 3. The points the dispatch noted for you, each tested against the record (D-599)

Each point below is answered by the record or by a rule already ratified, so none is put to you as an option.

1. **No "wording unchanged" line beside L2-S27, L2-S28 and L2-S30** (§L.33 item 1, §L.34 item 6, §L.35 item 1). The
   ground on which you ratified face (a)'s correction C5, and faces (b) and (c)'s correction 1, applies equally: the
   specification shows every ruling that touched a statement, by one line and a citation. It is correction 1 below.
   The dispatch also offered each record's arithmetic paragraph with the line; the earlier faces' lines quote the
   ruling's sentence and cite the record, and this surface follows them.
2. **L2-S30's first "Carried, not decided" bullet** (§L.35 item 3: "he may have the first bullet written beside
   L2-S30 as a carried item"). The bullet says that no source held measures how much the context terms gain over
   pitch-class content alone, on the same music with its uncertainty, and that the size of that gain is what the
   fitted weights will show (L2-S38). It bears on L2-S30's defense, which rests on cases rather than on a measured
   gain. **Proposed as part of correction 1, on the shape you accepted for L2-S14's "no reason to suspect" sentence
   in face (b).** Including it is this side's proposal, and you may drop it. The second bullet (the ledger entries
   C2, C6, C7, C8, C35 and C41 were not opened by that sitting) is about that sitting's reading, not about the
   statement, and is not proposed.
3. **The voicing-and-doubling item is not written into the successor** (§L.33 item 2). The chord-as-degree record
   files your direction ("Both doubling and voicing in the sense where drop two is one example should be explored
   when it fits plan") as a standing item of the plan, and says of it: "It changes no specification and no algorithm
   now." The successor states what L2 decides, and the record is the item's home (the dispatch's words, §L.33 item
2). **It stands.** It is carried in §5
   so that ratifying this face cannot be read as setting it aside.
4. **A pointer to the bass-scale-degree item under OQ-L2-3 stands beside L2-S28 alone** (§L.34 item 5: "he may have a
   pointer beside L2-S39 as well, or instead"). The ground of face (a)'s ratified correction C6 settles it, as that
   surface states it: "where an open measurement says something survives under, or may change, a statement, the
   statement points at it." On that ground face (a) already ordered the pointer beside L2-S3, where the "never a gate" half survives. The item says a published form
   of the rule would enter "under L2-S39", so L2-S39 points at it too. **L2-S39 is in face (f)**: the pointer is
   routed there (§4).
5. **L2-S28's Status, bold last sentence and Defense** (§L.34 item 7, carried to you as stale-field point 6). Settled
   before Task 0: the Status was amended on your word of 2026-10-13, its former value kept; the last sentence and the
   Defense each have a sub-item, the derived wording standing. Nothing remains.
6. **Nothing beside L2-S27 for the "summary mode" reading** (§L.30, lines 3331–3335). Settled by point 4 of the face
   (b) surface, which you ratified: the reading stays in Row 23.72's line and "decides nothing about L2-S14 or L2-S27". Nothing remains.

## 4. What needs writing — documentation only, none of it a choice

None of these changes the algorithm. The applying dispatch would write it, keeping every former wording in place
(#12).

- **Correction 1 — one recorded line per "wording unchanged" ruling not shown**, quoting it and citing the record
  (face (a)'s C5 rule):
  - beside L2-S27, chord as degree Ruling 1: "L2's algorithm as its statements define it is unchanged; L2-S27's
    wording does not change." (Ruling 2 says the same of the algorithm and places rows only; one line for the
    record.)
  - beside L2-S28, structural bass Ruling 1: "L2's algorithm as its statements define it is unchanged; L2-S28's
    wording does not change." Unlike L2-S22 in face (c), no later ruling of the same record replaced any of L2-S28's
    bold text — Ruling 2 says "the derived wording standing" — so the line contradicts nothing beside it.
  - beside L2-S30, context in chord terms Ruling 1: "Algorithm: unchanged. L2-S30's wording does not change;
    nothing is added to or taken from the candidate score." **Proposed with it** (§3 point 2, droppable): the record's
    carried bullet, "No source held measures the gain from context over content alone on the same data with its
    uncertainty (surface §A.2); the size of that gain is what the fitted weights show (L2-S38)."
  - **Not for L2-S29**: its ruled "Stands as derived" sub-item already shows its ruling.
- **Considered and not proposed:**
  - L2-S29's Defense ends "The charter's third candidate, the six-four "as its own category", cannot be represented
    until DP-N is ruled." Cadential six-four Ruling 1 has since excluded that category by name in the first
    specification, without making the exclusion depend on DP-N. The sentence is still true (it cannot be represented now), and the ruled
    sub-item beside L2-S29 already points to the exclusion beside L2-S2. Nothing is false, so nothing is written.
  - L2-S29's Status ("**Open** (DP-N, the charter's)"). DP-N is open, as the ruling says ("The charter's DP-N stays
    open exactly as ratified"), so the Status is true. Nothing is written.
- **Routed to face (f), not written now:** a pointer beside L2-S39 to the bass-scale-degree item under OQ-L2-3 (§3
  point 4). Face (f) also carries, from earlier faces, the pointer beside L2-S33 to the notated-flag item under
  OQ-L2-3 and the register standing of D-527 and the notation increment's Decision 4.
- **Nothing routed to the ninth surface from this face.** The UNSETTLED items that face (c) and face (d) sent there
  are about UNSETTLED items carried beside statements; none of this face's open points (§5) is marked UNSETTLED — a
  search of the four family records finds the word in none of them.

## 5. Left open by this face's rulings — carried, not decided by ratifying

- **DP-N, the charter's open point** — which theory of the cadential six-four is principal. Not L2's; the ruling
  keeps it open, and its settling route is measurement design (the framework's §S9, as the record relays it).
- **The cadential six-four's measurement-design questions** (the record's "What it does not decide"): how a `Cad64`
  annotation converts into L2's four fields; whether any grading corpus writes `Cad64`; whether the grading accepts
  either rival; which reading each grading corpus uses. And the record's carried costs: the committed label can
  differ from a corpus's convention; L3's cadence reading must handle a committed `I6/4`; the ceiling cost of
  excluding `Cad64` is uncounted. Both paragraphs stand quoted beside L2-S29.
- **The bass-scale-degree prior (D-585)** — a held-out measurement under OQ-L2-3. No source for the Rule of the
  Octave is held; a published form needs one fetched and read first (the structural-bass record, Ruling 3).
- **Voicing and doubling** — your standing direction of 2026-10-08, recorded in the chord-as-degree record §2: to be
  explored, as evidence for the analysis and as objects of their own, when the plan reaches a fitting point. That
  record places it in the context-research ruling's research iteration as "This side's reading of where it fits,
  not ruled"; whether that iteration's list now carries it was not checked this sitting. Beside it, the
  structural-bass record's reading (not ruled): no L2 statement reads the register of the lowest sounding pitch, and
  register is routed to the same item, "which does not name it".
- **How much context gains over content** — no source held measures it (context in chord terms record §2); the
  fitted weights will show it (L2-S38). Correction 1 proposes writing this beside L2-S30.
- **Two bounds the chord-as-degree record carries with Ruling 2**: whether the 2026-07-26 user ratification in
  `cowork_notation_adoption_increment.md`'s banner reaches its §3 (not checked); and whether L3 offers a view of a
  region's Roman numerals relative to an enclosing key area (L3's derivation's question; L2's degree stands either
  way).

## 6. What the rulings of this face leave owed at the ratification act, outside the successor

- **D-335 and D-526** — rows on these WITHHELD statements were placed by chord as degree Ruling 1; "those entries'
  register status is settled at the ratification act, not here".
- **D-472** — chord as degree Ruling 2: "D-472's register status is settled at the ratification act, not here."
- **D-449 and D-536** — rows on these WITHHELD statements were placed by structural bass Ruling 1; the same words.
- **D-585** — structural bass Ruling 3: "D-585's register standing is settled at the ratification act."
- **D-629** — context in chord terms Ruling 1: "Row 4.7 is on a WITHHELD statement (D-629); that entry's register
  status is settled at the ratification act, not here."
- **Nothing for the cadential six-four record**: it amends no register entry and names none as owed (its §2; the
  dispatch's §L.8 says the same).
- **Structural bass Ruling 2's edits outside L2** — S-50, the §0 entry *The lowest sounding pitch* and S-44 of the
  L0/L1 specification, and `FRAMEWORK.md`'s L1 list — were written by the application dispatch's Task 5 (relayed
  from `STATUS.md`'s 2026-10-13 Task 5 entry; neither file was read this sitting). Nothing more is owed for them here.

The register cannot take an entry while `cowork_register_rule_c_suspension_2026_08_28.md` is the standing route, as
the earlier face records state; that file was not opened this sitting. **So these wait on that route**, recorded and
not lost, as the earlier faces' register items do.

## 7. The decision, and what it does

**One decision: do you ratify face (e) — L2-S27 to L2-S30 as written in the successor, with correction 1 written by
the applying dispatch (with or without the L2-S30 bullet), the pointer beside L2-S39 routed to face (f), the open
points of §5 carried as open, and the register items of §6 carried to that dispatch?**

- **Documentation:** it marks the four statements ratified, writes three recorded lines (and, if you keep it, the
  L2-S30 bullet) with every former wording kept, and lists the register items for the applying dispatch.
- **Algorithm:** **nothing changes by this act.** No ruling of this face changed what the successor says L2
  computes: the chord-as-degree, structural-bass and context-in-chord-terms records say so in terms, and the
  cadential six-four ruling says "L2-S29 stands as derived". One
  ruling of this face did change an algorithm, but L1's, not L2's, and it was decided on 2026-10-08 and is already
  written: structural bass Ruling 2 made L1 publish the lowest sounding pitch of every slice, which L2-S28's term
  already wanted. Ratifying face (e) confirms it as written; it adds nothing to it.

**The currently decided method for face (e), in plain words.** For each stretch, L2 decides the chord as four
fields: the degree, read against the stretch's own tonality; the quality; the figure; and, for an applied chord, its
target. The chord kinds to choose from are the ruled vocabulary — every listed kind its own state however rare, and a
sounding ninth, eleventh or thirteenth treated as an elaboration of a simpler chord until the named jazz increment
lands. This is decided inside the one decision that also settles the boundaries, the tonality and which notes are
chord tones. The figure is the chord member the reading takes as its bass; it is not read off the first bass note by
a rule. A term of the candidate score compares the figure with the lowest sounding pitch of every slice in the
stretch (which L1 publishes for every slice), weighted by how long the slice lasts and how strong its metric
position is, with a fitted weight. A change of figure alone is a change of chord, and rival figures are carried with
their weight. At a cadential six-four, both `I6/4` and `V(64)` are carried as rivals and the evidence decides which
is published as the reading; `Cad64` is not a state. No chord is decided from the notes of the stretch alone: the
progression to and from the neighbouring chords, which notes count as chord tones, and the voice-leading evidence
all enter the score, so two chords with the same notes are told apart by their context, or kept near-equal where
nothing separates them. L2 publishes no chord symbol, root or bass note; L3 computes the chord symbol, the bass note
and the figured bass from L2's answer. **Still open:** DP-N (the charter's); the bass-scale-degree prior (a
measurement under OQ-L2-3); the weights' values (L2-S38); the vocabulary's completeness and the applied chain's depth
(OQ-L2-1, the open measurement face (a)'s statements name); whether the joint search can afford all of this (OQ-L2-8, the tractability route).

## 8. Recommendation: ratify, with correction 1 and the L2-S30 bullet

- **Towards the ultimate objective (maximum-precision inference, #4):** the audit will measure the code against this
  text. Three of the four statements carry a ruling the text does not show — the same kind of gap that once led a sitting
  to report ruled statements as unruled (entry 378). The lines close it and change nothing L2 computes. The L2-S30
  bullet tells a later reader that L2-S30's benefit is argued from cases and not measured; leaving it out loses
  nothing L2 computes.
- **Towards the guiding principles:** #10 (the specification true and complete about itself); #6 (one line and a
  citation, never a second copy); #12 (every former wording kept); D-599 (nothing here is put as a choice the record
  settles); face (a)'s ratified C5 and C6 rules and the earlier faces' correction 1 applied the same way; #24 for the
  L2-S30 bullet (a condition that cannot be established is declared as a bound).
- **Meta level:** documentation of the analysis's own specification; no measurement tool, no governance rule.

## 9. Bounds of this surface

Not read this sitting: `FRAMEWORK.md` (the charter's L2 and L3 lists, DP-A, DP-C, DP-L, DP-N, §S9), the L0/L1
specification (S-44, S-49, S-50), the four family records' surfaces, the ledger entries the Defenses cite (C2, C6,
C7, C8, C32, C35, C38, C41), the exemplars, the papers the Defenses relay (McLeod & Rohrmeier 2021, Masada & Bunescu,
Pardo & Birmingham 2002), the decisions-register group files, the comparison reading file and its rows, the
context-research ruling record, `cowork_notation_adoption_increment.md`, and the register's rule (c) suspension file.
Every claim about them above is relayed from the records, the successor, the dispatch or `STATUS.md`. The dispatch's
row-by-row placements were checked by the writing side at the time and were not re-checked here; this surface is
about the statements.

## 10. The check of this surface — run in its own turn, after delivery, at the sources

Checked for completeness, coherence, correctness and absolutes, each claim against the object it rests on. **Twelve
corrections, made at their sites above. None moves a finding, a proposed correction, the algorithm statement or the
recommendation. Former wordings, preserved (#12):**

1. §1 and §2: the OQ-L2-3 structural-bass item runs to line 2043 (its recorded sentence, bound and cost), read at
   the check. Former: *"(lines 2030–2039)"* (§1); *"(lines 2032–2039)"* (§2).
2. §1: **a correction of fact.** The chord-as-degree record's method paragraph names chord-vocabulary Ruling 1 only.
   Former: *"the chord vocabulary L2-S27 decides over is chord-vocabulary Rulings 1 and 2 (every listed chord kind
   its own state; a sounding ninth, eleventh or thirteenth an elaboration), which the chord-as-degree record's own
   method paragraph names; those rulings stand beside L2-S2 and L2-S4, in face (a), which you ratified."*
3. §1: the account of the other search hits was wider than what was read. Former: *"Every other hit is a row's
   filing line, another record's "what stands" list (the dispatch says those order nothing), or another statement's
   text."*
4. §2: two fields were overtaken, not one. Former: *"The one field a ruling overtook — L2-S28's Status — has been
   brought into line."*
5. §3 point 3: "the record is the item's home" is the dispatch's wording; now attributed. Former: *"and the record
   is the item's home. **It stands.**"*
6. §3 point 4: what face (a) ratified was correction C6 (two pointers); the general rule is that surface's ground.
   Former: *"Face (a)'s ratified C6 rule settles it: "where … points at it." Under that rule face (a) already
   ordered"*.
7. §3 point 6: point 4 is a point of the face (b) surface, ratified with it. Former: *"Settled by face (b)'s point
   4, ratified:"*.
8. §4: "whatever DP-N becomes" said more than the ruling. Former: *"excluded that category by name in the first
   specification, whatever DP-N becomes."*
9. §4: an absolute and an imprecise reason in the ninth-surface item. Former: *"are about items carried beside
   statements; this face's carried items (§5) are all the records' "carried" or "what it does not decide"
   paragraphs or their recorded bounds; a search of the four family records finds no "UNSETTLED" in any of them."*
   (the voicing item and the structural-bass reading in §5 are neither).
10. §5: the structural-bass record's words "which does not name it" were omitted. Former: *"and register goes to the
    same item."*
11. §7: **an absolute.** The cadential six-four record has no "algorithm unchanged" sentence. Former: *"Every ruling
    of this face says L2's algorithm is unchanged."* — and in the method paragraph, OQ-L2-1 is open, not ratified.
    Former: *"(OQ-L2-1, ratified with face (a))"*.
12. §8: the L2-S30 bullet was tied to the 2026-10-07 rule and to #24 more widely than either reaches; "exactly the
    gap" overstated the likeness to entry 378's case. Former: *"bullet tells a later reader that L2-S30's gain is
    unmeasured, which bears on your 2026-10-07 rule that a design rule is tested by measurement as soon as there is
    reason to suspect it; leaving it out loses nothing L2 computes."*; *"#24 for the L2-S30 bullet (a result carries
    its uncertainty, and a missing measurement of a gain is part of that)."*; *"exactly the gap"*.

**Checked and standing:** every quotation in §2, §3, §4 and §6 against its record (chord as degree Rulings 1 and 2;
structural bass Rulings 1 to 3; cadential six-four Ruling 1; context in chord terms Ruling 1 and §2); §2's account of
what the successor shows, at lines 1049–1171, 2032–2043 and 2139–2146, and the named exclusion beside L2-S2 (lines
171–174, found by search); §3's dispatch citations against §L.8, §L.33 items 1 and 2, §L.34 items 5 to 7, §L.35
items 1 and 3 and §L.30 lines 3331–3335; the C5, C6 and correction-1 precedents against the face (a), (b) and (c)
surfaces at the lines §1 names and the face (b) ruling record (the L2-S14 sentence "taken in by the word"); §6's
Task 5 relay against `STATUS.md`. **Absolutes swept** ("all", "every", "never", "nothing", "none", "only",
"exactly", "always", "whole"): each remaining hit is a statement's or ruling's own wording, a quotation, a claim
about this sitting's reading as §1 and §9 bound it, or a claim checked at its object above.

**What the check did not do:** it re-opened nothing §9 lists as unread, and did not re-read the sub-items beside
L2-S2, L2-S4 and L2-S5 (§1 marks that as relayed).

*Provenance: Cowork, 2026-10-13 (Stockholm), the sitting booted on entry 384. The user's words this sitting: the
opening instruction; "continue" (the check).*

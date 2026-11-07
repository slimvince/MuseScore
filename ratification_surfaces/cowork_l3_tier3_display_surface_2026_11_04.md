# Surface — L3, tier 3, item 13, first cut: what the analysis publishes and what a display makes, 2026-11-04

> **STATUS: SURFACE, NOT A RULING RECORD.** Cowork, 2026-11-04 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_five_hundred_and_eighteen.md`. Written to disk on landing; checked in the
> next turn. **Applying D-599 first, no choice remains in this cut: the 25 row-parts below are settled by the record,
> and what is put to the user, after the check, is whether to ratify them as derivations.** Nothing is ruled.
> **[checked]** means read at the object by this sitting; **[relayed]** means not.

---

## 1. What this is about

Entry 481 §2 lists the work of the L3 route in tiers. Item 13 opens the third tier: the outgoing statements that the L3
comparison (`ratification_surfaces/cowork_comparison_l3_reading.md`, "the reading file") proposes to **add** to the
derived L3 specification — the disposition **ADOPTED — proposed**, defined at the reading file's §5 (lines 383–385
**[checked]**; *corrected by the check, §10 item 1; former wording: "line 383"*) as *"a PROPOSAL to the user that the outgoing content be added to the derived specification"* — and that
no earlier family has reached. The route record (`records/cowork/rulings/cowork_rulings_2026_11_02_l3_route_sitting.md`
§2 step 1 **[checked]**) has the writing side cut these *"by member and subject"*; rows no family reaches stay proposals.

Which rows remain was found by listing every ADOPTED — proposed line in the reading file's §12 (lines 82118–83160
**[checked]**) and searching the L3 ruling records of 2026-11-02 to 2026-11-04 for each row number **[checked by search,
not by a whole read of each record]**. The phrase-units, cadence-features, cadence-type and key-areas records name the
other lead rows as placed. The list reconciles with the reading file's own per-member tables, whose ADOPTED — proposed
counts sum to 99, the route record's total **[checked: lines 1688 to 78416]**. Seventeen row-parts that travel with lead
rows already placed are not named in the records that placed those leads: 8.17, 8.29, 8.46, 8.63 (ii), 8.74, 8.79 (i)
(with 8.12); 8.48 (i), 8.89, 8.91 (with 8.31 (i)); 8.53, 8.76, 8.82, 8.117, 8.145 (with 8.52 (ii)); 7.69, 7.70 (ii)
(with 7.63); 7.303 (with 7.108). On the reading file's travelling convention each follows its lead row at the
application act, as the S38 ratification record took Row 3.15 with Row 3.5 (ii) "by travel" **[checked at that
record, line 39]**; they are not this cut's. *[Corrected by the check, §10 item 2. Former wording: "The phrase-units,
cadence-features, cadence-type and key-areas records placed the rest."]* What remains falls under four subjects; **this cut takes the first: display**. The other three (kinds of span
named by what bounds them; general architecture rules applied to L3; facts from the published literature) are later
cuts. The UNPLACED display statements of member 48 (the reading file at 65770–65777 **[checked]**) are tier item 14's,
not this cut's.

Every row below was read at its own entry in the reading file's §6 **[checked]**, at the line given.

## 2. Part A — every display string is made outside the analysis, from published facts (10 row-parts)

**The rows, in the old documents' own words:**
- **Row 4.2** (line 2100) and **Row 4.3** (2116), `ARCHITECTURE.md` §4.3: the formatter is *"Kept separate from
  `ChordAnalyzer` so the analysis layer remains display-agnostic"*; *"analysis produces data, formatters produce
  strings."* Graded AGREES with L3-S5.
- **Row 19.1** (23848) and **Row 19.3 (ii)** (23874), `ARCHITECTURE.md` §2.3: *"Analysis components produce structured
  data — they never produce display strings"*; the separation *"must be maintained throughout."* AGREES with L3-S5.
- **Row 15.42 (iii)** (21811): *"display renderings are presentation, facts are published"*. AGREES with L3-S5.
- **Row 7.329 (ii)** (8245) and **Row 7.330** (8263), the old function-layer design: translating cadence labels is
  *"a display/formatting task on the structured cadence-type identifiers"*. The derivation is silent.
- **Row 21.191** (30195), **Row 21.205** (30399) and **Row 57.119** (73487): Roman numerals and Nashville numbers are
  *"presentation choices, not separate analyses"*, and *"encode the same information"*. The derivation is silent.

**The proposal** (Row 4.2): *"that every display string be produced outside the analysis, from published facts, and
that the analysis carry no display convention — L3-S5 carries this for the chord symbol's root only."*

**Why the record already settles it:**
- **L3-S5** (derivation `cowork_blind_derivation_l3_2026_10_17.md` lines 258–260 **[checked]**): a display that needs a
  root for every chord *"reads the quality and the bass and chooses its own convention, as a display act, and never
  publishes it back into the analysis."* L3-S27 (lines 848–850 and its status line 863 **[checked]**) says the same of
  the figured bass: the full figure *"is the published fact"*, an abbreviated figure *"a view of it under a declared
  convention"*, and *"Which convention a display defaults to is the display's own choice."* Where else the derivation
  names a display (L3-S29, lines 892–893 and 909–910 **[checked]**: a comparison with the composer's figures is *"the
  measurement layer's act or a display's"*) it agrees. The proposal states the rule once for all of L3. *[Corrected by
  the check, §10 items 3 and 4. Former wording: "L3-S25's status line (863 [checked]) says the same of the figured bass:
  … The derivation already applies the rule in the two places it speaks of display; …"]*
- **The chord-symbol Ruling 1 of 2026-11-03** (the user's word "confirmed" **[checked]**) has L3 publish the chord
  symbol as fields — the spelled root with its pitch class, the quality, the bass. **The pivot-label Ruling 1** of the
  same day (the user's word "yes" **[checked]**) publishes the pivot as a re-expressed degree with a flag. That neither
  ruling publishes a text string is this side's reading; neither says so in terms. *[Corrected by the check, §10 item 5.
  Former wording: "as structured fields — … the bass — not as a string. … with a flag, not as a label string."]*
- **D-100** (`DECISIONS.md` line 267, LIVE **[checked]**): *"Every derived fact is published exactly once, on the
  producing layer's output surface"*. A Roman numeral and a Nashville number made from the same decided chord are two
  ways of writing one fact, so they are renderings, not two facts.

**Weak points:**
1. *"The analysis carry no display convention"* must not be read against the chord-symbol ruling. A spelled root is
   information the reading decided (F♯ is not G♭), not a way of writing it; the ruling published it on that ground. The
   proposal concerns how facts are turned into text.
2. L3 publishes some facts in the form the ground-truth annotations use (the figure *"written in the figured-bass manner
   the ground truth uses"*, `FRAMEWORK.md` glossary line 97, as the chord-symbol record quotes it **[relayed]**). That
   is the form of a published fact, fixed so it can be graded, not a display string. A display may still abbreviate it.
3. Row 4.2's own sentence names a component of the old code (`ChordAnalyzer`). What is adopted is the rule, not the
   component; the code's present state stays with the QUARANTINED audit questions of Rows 15.42 (i)–(ii) and 19.3 (i).

## 3. Part B — the tonic / subdominant / dominant summary is no published fact (10 row-parts)

**The rows:**
- **Row 7.5 (i) and (ii)** (line 3235), the old function-layer design: *"The three-role summary (tonic / subdominant /
  dominant) is a lossy, deterministically-derivable read-out, not a stored output; it is built only if and when an
  accessibility/teaching display needs it, and never drives analysis."*
- Travelling with it: **Row 7.6** (3252), a first-class three-role analysis *"rejected (it would invent judgments no
  data can verify)"*; **Row 7.24** (3534); **Row 7.59** (4090), *"Optionally derive the three-role read-out … by a fixed
  lookup; not part of the analysis"*; **Row 7.226 (ii)** (6732); **Row 7.227** (6748), rejected because it *"would have
  to resolve the few context-dependent role cases, which no reference data can verify"*; **Row 7.228** (6763), *"The
  read-out, if built for accessibility, defaults those cases to their tonic-side bucket"*; **Row 7.274** (7429), the
  glossary entry; **Row 7.294 (i)** (7712), no three-role prediction target, *"the literature outputs Roman numerals and
  treats the three roles as a derived view"*. The derivation is silent on all of them. Rows 7.226–7.228 carry the SEEN
  mark: the deriving session saw D-335's heading line only.

**The proposal** (Row 7.5): *"that the tonic / subdominant / dominant summary be no published fact of the analysis — at
most a read-out a display computes from the published chord — and that no decision read it"*, Row 7.228's tonic-side
default carried for any such read-out.

**Why the record already settles it:**
- **D-335** (`DECISIONS.md` line 435, LIVE, 2026-08-02 · user **[checked]**): *"The function layer outputs the Roman
  numeral; the tonic/subdominant/dominant summary is a derived read-out, never a stored output"*. Rows 7.226 to 7.228
  lie in D-335's home (the old function-layer design §9, lines 621–626); the other rows say the same at other places of
  that document. D-335 speaks of the old function layer; that its subject is now L3's is this side's reading, on the
  charter's placing of the cadence and the chord symbol at L3. Adopting the proposal carries a live ruling of the
  user's into L3's specification. *[Corrected by the check, §10 item 6. Former wording: "The rows above are D-335's home
  text and its glosses."]*
- **The ruled standard for departing from a design rule** (`CLAUDE.md`, *HOW A DECISION SURFACE IS WRITTEN*, step 4,
  citing the 2026-10-07 ruling **[checked]**): a rule holds while there is no reason to suspect that breaking it would
  improve the inference. The summary *"never drives analysis"* (Row 7.5 (ii)), and the literature *"outputs Roman
  numerals and treats the three roles as a derived view"* (Row 7.294 (i)); so, on this side's reading, publishing it
  would not change what is inferred. *[Corrected by the check, §10 item 7. Former wording: "No decision reads the
  summary and the grading is against Roman numerals (Row 7.294 (i)), so publishing it would not change what is
  inferred."]*
- **D-295** (line 509, LIVE **[checked]**), *"every inferred object must be displayable"*, is met: the summary can be
  displayed, computed by the display from the published chord.

**Weak point — the tension with the pivot label, stated.** The pivot-label ruling put a re-expression of L2's decided
facts at L3 rather than at a display, after the lesson *"What harm is there in exposing such names?"* (entry 499, as
that record quotes it **[relayed]**). By that lesson, L3 could publish the summary too. **The difference is the harm D-335
names:** the pivot label re-expresses the decided chord and settles nothing (that record: *"No chord is named 'the
pivot'"*), whereas the summary must put the few context-dependent chords on one side or the other, a judgment Row 7.227
says *"no reference data can verify"*. Publishing it at L3 would publish that judgment as a fact of the analysis. One
variant was considered and is not recommended: L3 publishes the summary with a flag on the context-dependent chords in
place of the tonic-side default. It meets the harm, but it would overturn a live ruling without any reason to expect a
gain in inference, which the step 4 standard requires. **If the user sees a gain this side does not, the variant is
the alternative to raise.**

## 4. Part C — the grouping has one producer, L3, and it is what a display reads (1 row-part)

- **Row 8.54** (line 9601), the old grouping design: *"The contract to the display layer above is this structure; L6 is
  its only producer."* The derivation is silent. **Proposal:** *"that the grouping have L3 as its only producer, and be
  the surface a display reads."*
- **Settled by:** the charter's L3 *Publishes* list, which includes the phrase and section grouping (as the route
  record §2 restates it **[checked there]**; `FRAMEWORK.md` itself not read **[relayed]**); the key-areas Ruling 2 of
  2026-11-03, which adds key areas to L3's grouping (Rows 3.1 (iii), 8.12 and the others ADOPTED, that record's lines
  89–90 **[checked]**; *corrected by the check, §10 item 8; former wording: "[checked at that record's line 127 by
  search]"*); and D-100 (one
  fact, one home, on the producing layer's surface).
- **Weak point:** "L6" is an old layer name. What is adopted is "L3 is the grouping's only producer"; no layer number
  from the old documents enters the specification.

## 5. Part D — nothing L3 publishes is written into the score except by the user's own act (4 row-parts)

- **Row 19.5** (line 23902), `ARCHITECTURE.md` §2.9: *"It never modifies the main score automatically."* Travelling with
  it: **Row 19.4** (23889), *"The system presents analytical findings and suggestions"*; **Row 19.6** (23916), *"All
  score modifications require explicit user action"*; **Row 19.8** (23944), the user acts on a suggestion *"explicitly
  through standard MuseScore editing"*. The derivation is silent. **Proposal:** *"that nothing L3 publishes be written
  into the score except by the user's explicit act."*
- **Settled by — this side's reading, the weakest of the four parts:** no register entry on this subject was found
  (`DECISIONS.md` searched for *explicit user*, *modif… the score*, *display-agnostic*, *formatter*, *Nashville*: one
  hit, line 90, a passage naming the formatter's source file under D-311, whose subject is a file split, not this
  **[checked]**; the `decisions/` group files not searched). The ground is the charter's shape: L3's outputs are things
  it *publishes*, and the score is L0's notated record, which the layers beneath L3 read and L3 reads through them. A
  layer that wrote into the score would change what it and they read. *[Corrected by the check, §10 item 9. Former
  wording: "… *Nashville*: no matching entry [checked by search]). … which every layer reads. A layer that wrote into
  the score would change its own input."]* So the sentence, read as a statement about L3, restates what L3 already is; it adds no step and removes none.
- **Weak points:** (1) the rule in `ARCHITECTURE.md` is about the whole application, not one layer; adopting it into
  L3's specification states only L3's part of it. (2) Row 19.4 says nothing about L3 in particular; it travels because
  it opens the same paragraph. (3) The disposition vocabulary has no charter for the user interface, so the alternative
  to adopting is to leave the rows as proposals, which the route record allows. This side sees no gain in that, and
  found no harm in adopting. *[Corrected by the check, §10 item 10. Former wording: "Nothing is gained by that; no harm
  in adopting was found."]*

## 6. Documentation and the algorithm, separately

- **Algorithm: no change.** Each part restates something the currently decided method already does or does not do.
  **The currently decided method on this subject:** L2 publishes the decided chord as a degree in its tonality, with
  the tonality. L3 publishes structured facts read off it: the chord symbol (spelled root with its pitch class, quality,
  bass, or a named reason in place of the root), the figured bass, the harmonic rhythm, the cadence at each phrase end
  with its type, the phrase and section grouping, key areas, and the pivot re-expression with its flag (the route record
  §2, the chord-symbol, pivot-label and key-areas rulings **[checked at those records]**). L3 publishes no tonic /
  subdominant / dominant summary. A display turns published facts into text.
- **Documentation only:** if ratified, the 25 row-parts are recorded ADOPTED, which adds four statements to the amended
  L3 specification (parts A to D). The re-marking of the rows and the writing of the statements are the application
  dispatch's act (route record §2 step 2), not this sitting's.

## 7. Recommendation

**Ratify parts A to D as derivations.** Towards the ultimate objective (#4): neutral — on this side's reading none of
the four changes what is inferred *(the qualifier added by the check, §10 item 11)*; part B keeps an unverifiable judgment out of the analysis's facts. Towards the guiding principles: one fact,
one home (D-100, #6 **[relayed]**); every inferred object displayable (D-295); a live user ruling carried rather than
overturned without a reason to expect a gain (D-335, and the step 4 standard). Meta level: the analysis's own
specification text, documentation only.

## 8. What follows

1. The check of this surface at its sources, in its own turn.
2. Then, unless the check finds a real choice, the question whether to ratify parts A to D as derivations, alone, plain
   text, documentation and algorithm stated separately.
3. Then the next cut of item 13: kinds of span named by what bounds them.

## 9. Read by this sitting

Entry 518 whole; the start-up chain at the sections entry 291 §4 step 3's amendment names (entry 118, the first
paragraph of "THE BRIDGE FAULT"; entry 152, item (vi); entry 169, its "Boot" block and "The cadence for your session";
entry 291 whole); `STATUS.md` whole; the gating answer at its counts; D-599 at its row (`decisions/group_T.md` line 900);
entry 481 whole; the L3 route record whole; the third-cut surface of the fit and the rest whole (for the form);
`CLAUDE.md` lines 1850–1923; the reading file at §5 (366–432), §12's ADOPTED — proposed lines (82118–83160, by search
and in part), its per-member ADOPTED — proposed table lines (1688 to 78416, by search), 65770–65779, and the 25
row-parts' entries; the derivation at lines 236–265, 848–866 and 888–911, and its statement headings L3-S25 to L3-S29
by search; `DECISIONS.md` lines 86–91 and the D-311 and D-329 index rows;
`DECISIONS.md` at D-100, D-254, D-295, D-297 and D-335's index rows, and searched; the chord-symbol record lines 20–119;
the pivot-label record lines 10–79; the phrase-units record lines 10–119; the cadence-features record lines 55–79; the
mass-and-status record lines 34–43 and 150–164. **Searched, not read whole:** the other L3 ruling records of 2026-11-02 to
2026-11-04, for row numbers. **Not read:** `FRAMEWORK.md`; D-335's home text in `cowork_layer5_function_design.md`
(its sentences read as the reading file quotes them); the guiding principles' own text; `CLAUDE.md`'s six ruled spans
and `DECISIONS.md` whole (the start-up read narrowed on the user's word).

## 10. The check, run in the turn after the surface landed — eleven corrections

Each quotation re-read at its line; each row's entry line, grading and proposal re-read; the list of remaining rows
reconciled against the reading file's per-member tables (sum 99); the cited ruling records re-read at the lines cited;
the derivation's statement headings located; the sweep for absolutes read each "every", "all", "no", "none", "never",
"nothing", "only" and "already" at its line, the proposals' own wording left as quoted. **No part's filing changed, the
recommendation stands, and no real choice arose.**

1. §1: the §5 definition spans lines 383–385, not line 383.
2. §1: "placed the rest" was wider than the records: they name the lead rows; seventeen travelling row-parts are not
   named there. Now listed, with their route (they follow their leads at the application act). The list's
   completeness is now reconciled against the 99, which the first writing had not done.
3. §2: the figured-bass status line 863 belongs to **L3-S27**, not L3-S25 (L3-S25 opens at line 780, L3-S27 at 848).
4. §2: "the two places it speaks of display" was unestablished; the derivation also names a display at L3-S29. It
   agrees; now stated.
5. §2: "not as a string" was this side's gloss on the two rulings, not their words. Now marked as a reading.
6. §3: "D-335's home text and its glosses" — only Rows 7.226–7.228 lie in the home; the rest restate it elsewhere in the
   same document. Also added: carrying D-335's subject from the old function layer to L3 is this side's reading.
7. §3: "the grading is against Roman numerals" misread Row 7.294 (i), which speaks of what the literature outputs. Now
   quoted, with Row 7.5 (ii) for "never drives analysis".
8. §4: the key-areas citation pointed at line 127 (the surface's alternatives); the adoption is at lines 89–90.
9. §5: the search was reported as "no matching entry" — it had one hit, not on this subject; and only the index file
   was searched. "Every layer reads" the score narrowed.
10. §5: "Nothing is gained by that" restated as this side's view.
11. §7: "none of the four changes what is inferred" marked as this side's reading.

*Found and not acted on (outside this cut, judged against the plan):* the seventeen travelling row-parts of item 2 are
for the application dispatch to re-mark with their leads; nothing in a ruling record is changed by this sitting.

*Provenance: Cowork, 2026-11-04 (Stockholm), the sitting booted on entry 518. The user's words: the opening instruction;
"narrow"; "continue"; "continue" (the check).*

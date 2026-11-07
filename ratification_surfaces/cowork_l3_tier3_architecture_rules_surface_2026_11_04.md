# Surface — L3, tier 3, item 13, third cut: general architecture rules applied to L3, 2026-11-04

> **STATUS: SURFACE, NOT A RULING RECORD.** Cowork, 2026-11-04 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty.md`. Written to disk on landing; checked in the
> next turn (§12, eight corrections). *[Former wording: "to be checked in the next turn".]* **Applying D-599 first, no choice remains in this cut: the 14 row-parts below are settled by the record,
> two of them in a narrower wording than the reading file proposes (part E), and what is put to the user, after the
> check, is whether to ratify them as derivations.** Nothing is ruled.
> **[checked]** means read at the object by this sitting; **[relayed]** means not.

---

## 1. What this is about

Item 13 of entry 481 §2 is the set of outgoing statements that the L3 comparison
(`ratification_surfaces/cowork_comparison_l3_reading.md`, "the reading file") proposes to **add** to the derived L3
specification (the disposition **ADOPTED — proposed**, the reading file's §5, lines 383–386 **[checked]**: *"a PROPOSAL
to the user that the outgoing content be added to the derived specification"*) and that no earlier family has reached.
The first cut (display) and the second (kinds of span) were ratified as derivations earlier on 2026-11-04
(`records/cowork/rulings/cowork_rulings_2026_11_04_l3_display_sitting.md` and
`…_l3_span_kinds_sitting.md`, each Ruling 1 **[checked]**). **This is the third cut: general architecture rules applied
to L3** — Rows 8.105 (i), 19.29 (i)–(ii), 19.33, 19.53 (ii), 19.56 (iii), 19.76 (ii), 19.77, 19.78, 19.82, 20.7,
36.111 (i), 38.47, 38.48: fourteen row-parts. The list is the display ruling record's §2 **[checked there]**; it is not
re-derived here.

Every row below was read at its own entry in the reading file's §6 **[checked]**, at the line given. "The derivation is
silent" below is the reading file's current-text axis at each row; the derivation itself was not opened by this sitting.
*[Sentence added by the check, §12 item 6.]* Member 8 is the old grouping-layer design (`cowork_layer6_grouping_design.md`:
D-461's home at the index, line 464, is that file's §7, and the reading file places D-461's home inside member 8 at
lines 324–326, *"§7, Proportionality"*, lines 8642–8643 **[checked]**; that member 8 is that file is this side's reading
of the two). *[Corrected by the check, §12 item 1. Former wording: "(`cowork_layer6_grouping_design.md`, D-461's home,
at the reading file's line 8642 **[checked]**)".]*
member 19 is `ARCHITECTURE.md`; member 20 is the same file's §3 *Directory Structure*; member 36 is
`cowork_phrase_boundary_design.md`; member 38 is `cowork_target_architecture.md`, its §2 *The layer model*.

**Each rule was checked against the register before writing**, at `DECISIONS.md`'s index rows **[checked]**, and its
home located by the reading file's marks at each member (lines 25426–25434, 27105–27106, 42120–42124, 46445–46448,
48732–48735 **[checked]**). The six parts below group the rows by subject.

## 2. Part A — cost: every cost-driving choice a setting, optional refinements separable, re-analysis local (3 row-parts)

**The rows, in the old documents' own words:**
- **Row 19.29 (i) and (ii)** (line 24281): *"**(a)** every cost-driving choice is an explicit *setting*, never a
  hardcoded constant; **(b)** every optional expensive refinement is a cleanly separable on/off stage."* Proposals:
  (i) *"that every choice of L3 that drives its cost be an explicit setting and never a constant written into the
  code"*; (ii) *"that every optional expensive refinement of L3 be a separable stage that can be turned on and off."*
- **Row 19.53 (ii)** (24715): *"**(R2)** re-analysis is incremental over the dirty span plus a bounded margin"*.
  Proposal: *"that L3's re-analysis after an edit cover only the edited span and a bounded margin around it."* Claims
  (i) and (iii) of the same row are ADOPTED — carried by L3-S40, whose defense holds L3 to *"the bounded-context rule
  that cost scales with the working span"* (as the row quotes it).

The derivation is silent on all three.

**Why the record already settles it:**
- **D-035** (`DECISIONS.md` line 265, LIVE **[checked]**): *"The effort setting - every cost-driving choice is a
  setting, never a hardcoded constant"*, home `ARCHITECTURE.md`; Row 19.29 lies in its home (reading file line 25429
  **[checked]**).
- **D-030** (line 260, LIVE **[checked]**): *"Bounded context - cost scales with the working span, not the whole
  score"*; Row 19.53 lies in its home (line 25431 **[checked]**). Claim (ii) is the re-analysis half of the same
  sentence whose other two halves L3-S40 already carries.
- **The tractability record of 2026-10-05** (`records/cowork/rulings/cowork_rulings_2026_10_05_l2_tractability_sitting.md`
  **[checked]**) already reads these settings for L2 without deciding any dial: Ruling 1 (iv), *"An effort setting may
  not quietly reduce how many readings the search keeps"*; §1b item 3, *"A dial the user rules and the end user turns is
  not the "quiet" reduction Ruling 1 (iv) bars"*; and **D-202** (line 659, **DEFERRED** **[checked]**), the effort
  control as one setting with several dials, deferred until a measurement shows which pieces must be switchable (as
  that record quotes it).

**Weak points:**
1. **No dial is decided, and none is proposed.** Adopting the rule says only that a cost-driving choice of L3, where one
   exists, is a setting rather than a constant. Which settings L3 has, and their defaults, are D-202's deferred question.
2. **The tractability ruling is L2's.** That a setting may not quietly reduce the readings L3 keeps is not ruled for
   L3; on this side's reading it follows for L3 from Row 19.77 below (D-297): a reading L3 has computed and then drops
   is a loss.
3. **"Bounded margin" and context growth.** For L2, context grows by convergence under a safety cap (tractability
   Ruling 1 (ii)), and what "the answer stops changing" means is open (OQ-L2-6). Row 19.53 (ii) says the margin is
   bounded; it does not say how the bound is set, and adopting it decides nothing about OQ-L2-6.
4. **D-035's index row names only claim (a).** Claim (b), the separable stage, stands in the same sentence of its home
   (the row's locator, lines 1070–1072); that it is covered by D-035 is this side's reading of the home's extent.

## 3. Part B — style lives only in the fitted values, never in the structure (1 row-part)

- **Row 19.33** (line 24357): *"Style-specificity lives **only** in the *calibration* of the judgment layers (their
  priors/weights), **never in structure**."* Proposal: *"that any style-specific behavior of L3 live only in the fitted
  values of its model, never in its structure."* The derivation is silent.
- **Settled by: D-024** (line 254, LIVE **[checked]**): *"The fact layers are style-agnostic; style lives only in
  calibration"*, home `ARCHITECTURE.md`; Rows 19.32 and 19.33 lie in its home (line 25430 **[checked]**). L3 is a
  judgment layer; the half of D-024 that speaks to it is *"style lives only in calibration"*.
- **Weak points:**
  1. **The naming-scheme question stays open, and this rule bears on how it is answered, not on what the answer is.**
     Sections Ruling 3 of 2026-11-03 *[corrected by the check, §12 item 2; former wording: "Ruling 6"]* left open *"which naming scheme (sonata-form labels, Caplin's theme types, or both)"*
     (`cowork_rulings_2026_11_03_l3_sections_sitting.md`, line 161 **[checked]**). Under this rule, whichever scheme is
     chosen, a dependence on style sits in fitted values (for example the mass a name receives), not in a separate
     structure per style. That is the content of D-024 carried into L3; it chooses no scheme.
  2. Under the user's rule of 2026-10-07 (no design rule may block the ultimate objective in the long run; a rule is
     tested by measurement as soon as there is reason to suspect breaking it would improve inference), this rule holds
     until such a reason appears. This sitting met none, and did not search for one. *[Corrected by the check, §12
     item 7. Former wording: "None is on the record this sitting read."]*

## 4. Part C — what L3 reads, and what counts as losing information (5 row-parts)

**The rows:**
- **Row 19.56 (iii)** (line 24761): *"within its scope uses *all* the information L1 carries losslessly (notated
  spelling, metric weight, voice)"*. Proposal: *"that L3 read, within its scope, all of the information the layers
  beneath it publish without loss — the notated spelling, the metric weight and the voice — and discard none of it."*
- **Row 19.76 (ii)** (25094): *"…the ruled-out reading is carried on the output surface at low confidence, unless the
  elimination is recomputable from what that surface does keep."* Proposal: *"that a reading L3 rules out need not be
  published where its exclusion can be recomputed from what L3 does publish."* Claim (i) is ADOPTED — carried by L3-S13.
- **Row 19.77** (25111): *"NEVER COMPUTING a possibility is not information loss; only DISCARDING a computed one is."*
  Proposal: *"that an alternative L3 decides on measured evidence never to compute is no loss of information, and that
  only a reading L3 computed and then left out of its publication is."*
- **Row 19.78** (25126): *"A layer that decides, on measured evidence, not to work out a particular alternative at all
  has lost nothing"*. ADOPTED — proposed, travelling with Row 19.77.
- **Row 19.82** (25182): *"A published fact that no one reads is either **declared dormant**, with its future consumer
  named, or removed."* Proposal: *"that an L3 fact no consumer reads be either declared dormant, with its future consumer
  named, or removed — evidence-class facts being published broadly as Row 19.81 states."*

The derivation is silent on all five.

**Why the record already settles it:**
- **Row 19.56 (iii): D-033** (line 263, LIVE **[checked]**): *"Each layer owns one evidence-source-times-question
  contribution and uses all of L1's information"*; Row 19.56 lies in its home (line 25432 **[checked]**). With it,
  L3-S37 as ratified: L3 reads everything L2 publishes plus L0's and L1's published facts, and nothing else (as the
  L3-S38 ratification record of 2026-11-03 states the decided method **[checked there]**; L3-S37's own text
  **[relayed]**).
- **Row 19.76 (ii): D-099** (line 266, LIVE **[checked]**): *"Negative evidence is information - a ruled-out possibility
  is carried, not dropped"*; Rows 19.75 and 19.76 lie in its home (line 25433 **[checked]**). The exception in claim (ii)
  is part of the same sentence of the home; a ruled-out reading that can be recomputed from what is published is not
  dropped information.
- **Rows 19.77 and 19.78: D-297** (line 290, LIVE, 2026-08-02 · user **[checked]**): *"Correction of record: never
  computing a possibility is not information loss; only discarding a computed one is"*; both rows lie in its home (line
  25433 **[checked]**). The tractability record read D-297 for L2 (Ruling 1 (iii)).
- **Row 19.82:** **no register entry was found homed at it** (the marks name D-100's home as falling in Rows 19.80 and
  19.81, line 25433 **[checked]**). It is consistent with: **D-100** (line 267, LIVE): every derived fact published once,
  on its producer's surface, evidence-class facts broadly even where no consumer is named (read for L2 by the
  publication-to-next-layer Ruling 1 of 2026-10-06, line 37 **[checked]**) — which the proposal keeps; **D-581** (line
  308, LIVE, 2026-08-04 · user **[checked]**): *"Information not yet consumed is NOT automatically a defect"*, classified
  preserved-awaiting-consumer, lost, should-already, or unclear — the row's "declared dormant, with its future consumer
  named" is that first class; and **D-297**: removing a fact means no longer computing it, which is no loss.

**Weak points:**
1. **"Voice" in Row 19.56 (iii).** The proposal names notated spelling, metric weight and voice as examples. Which of
   them L0 and L1 publish is their input contracts' matter, not read by this sitting. Adopted, the statement reads "all
   that the layers beneath publish", the three named as the old text names them.
2. **Row 19.82 rests on consistency, not on a register entry.** And D-295 (line 509, LIVE, 2026-08-02 · user
   **[checked]**: *"every inferred object must be displayable"*) together with D-522 (line 302, LIVE **[checked]**:
   *"Explaining an inference to the end user is a late-bound DISPLAY consumer of facts that already exist"*) means
   *[corrected by the check, §12 item 8; former wording: "(line 302, LIVE: explaining to the end user is a display
   *consumer*)"]*, on this side's reading, that a fact the display reads is a fact someone
   reads. So "no one reads" reaches only a fact no display and no later layer reads.
3. **Row 19.76 (ii) narrows what L3 must publish** (a redundant ruled-out reading may be left out). It changes nothing
   that is inferred, and nothing is lost, since the reading can be recomputed from what is published.

## 5. Part D — the analysis code depends on no type of the score editor (1 row-part)

- **Row 20.7** (line 25741): *"**The analysis library (`composing`) depends on no MuseScore or engraving types**"*.
  Proposal: *"that the code computing L3's facts depend on no type of the score editor."* The derivation is silent.
- **Settled by: D-229** (line 491, LIVE **[checked]**): *"The MuseScore-dependency rule - one general rule for what our
  code may depend on"*; Rows 20.7 to 20.9 lie in its home (line 27106 **[checked]**). With it **D-072** (line 488, LIVE
  **[checked]**): *"The dependency rule - the analysis library knows nothing about the score format"*.
- **Weak point:** this is a rule on the code. The specification states it as a requirement on any implementation of
  L3; nothing about the present code is examined or claimed here.

## 6. Part E — a reading missing from L3's own candidates is remedied inside L3 (2 row-parts; narrower wording)

**The rows:**
- **Row 38.47** (line 47404): *"**Coverage failures stay in their layer.**"* Proposal: *"that a reading missing from
  L3's own candidate readings be remedied inside L3, by widening its candidate set, and never by a backward edge."*
- **Row 38.48** (47418): *"If the true reading was never even among the carried alternatives (a coverage miss, not a
  selection miss), the fix is to **widen that layer's candidate set inside that layer** — not to add a backward edge."*
  ADOPTED — proposed, travelling with Row 38.47.

The derivation is silent on both.

**Why the record settles it — in a narrower wording than the proposal's "never":**
- **D-466** (line 294, LIVE, 2026-08-04 · user **[checked]**): *"Forward-only is a strong DEFAULT, not dogma — a
  backward edge is admissible only as a deliberate, surfaced, measured, documented exception"*. The reading file reads
  its clause as the quotation block of this same document's §2 (line 46445 **[checked]**).
- **L3-S38 as ratified** on 2026-11-03 (`cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md`, Ruling 1
  **[checked]**) ends: *"It is a question for a measured backward edge."*; that record's decided method: *"a backward
  edge is tested by measurement as soon as there is reason to suspect it helps"* (nothing-from-L3 Ruling 3, as that
  record cites it **[relayed]**).
- **The user's rule of 2026-10-07:** no design rule may block the ultimate objective in the long run.

So the remedy for a coverage miss is, by default, to widen L3's own candidate set; the proposal's **"never by a
backward edge"** is wider than D-466 and than ratified L3-S38, and is not what the record supports. **The wording this
side derives:** *"that a reading missing from L3's own candidate readings be remedied inside L3, by widening its
candidate set; a backward edge is not the remedy, except as the deliberate, surfaced, measured and documented exception
D-466 admits."* No alternative remains: the unqualified "never" would contradict a live user-ratified entry and a
ratified statement.

**Weak points:**
1. The narrowing is this side's; it rewrites a proposal sentence of the reading file. The rows themselves (the old
   document's *"not to add a backward edge"*) are carried as written.
2. Member 38 is homed in no register entry (line 48732 **[checked]**); D-466 is used as the live rule on the subject,
   not as the rows' home.

## 7. Part F — the grouping is an explanatory output, not an accuracy requirement (2 row-parts)

- **Row 8.105 (i)** (line 10437, WITHHELD — D-461): *"L6 is a deliberate **explainability** layer, not an accuracy
  requirement"*. Proposal: *"that the phrase and section grouping be held as an explanatory output of the analysis, not
  as an accuracy requirement on it."* Claim (ii), *"does not grow detection of its own"*, is UNPLACED (L3-S8 DIFFERS)
  and is tier item 14's, not this cut's.
- **Row 36.111 (i)** (42101, WITHHELD — D-480): *"So this primitive is **not** an accuracy requirement"*. ADOPTED —
  proposed, travelling with Row 8.105 (i). Claim (ii) is UNPLACED (L3-S38 DIFFERS) and is item 14's.

The derivation is silent on both claims (i).

**Settled by:**
- **D-461** (line 464, LIVE, 2026-08-04 · user **[checked]**): *"The grouping layer is an explainability layer, not an
  accuracy requirement, and is deliberately kept thin"*, home `cowork_layer6_grouping_design.md` §7; Row 8.105 lies in
  it (line 11245 **[checked]**).
- **D-480** (line 471, LIVE, 2026-08-04 · user **[checked]**): *"The phrase-boundary primitive is NOT an accuracy
  requirement — a competitive reference engine does no phrase segmentation at all — so it is built right but kept
  proportionate"*; Row 36.111 lies in its home (lines 42120–42124 **[checked]**).
- **L3-S38 as ratified:** *"L2 reads nothing L3 publishes"* — so nothing L3 publishes can carry the accuracy of L2's
  reading (this side's reading of the two together).

**Weak points:**
1. **"Not an accuracy requirement" does not exempt L3's own facts from measurement.** Each still carries its
   establishment status (for example sections Ruling 3 *[corrected by the check, §12 item 3; former wording: "Ruling
   6"]*: form-function names UNESTABLISHED until measured). On this
   side's reading, the rule says the analysis's accuracy is not made to depend on the grouping; it does not say the
   grouping is never measured.
2. **Both rows carry the WITHHELD mark:** the deriving session was not shown D-461 or D-480. That the derivation is
   silent here is consistent with that.
3. **"Kept thin" and "kept proportionate"** are not in claims (i); they stand with claims (ii), item 14.

## 8. Documentation and the algorithm, separately

- **Algorithm: no change.** Each part carries into L3's specification a live register entry or a ratified statement on
  a subject the derivation is silent on, and none changes what L3 infers. **The currently decided method on these
  subjects:** L3 reads everything L2 publishes (its reading, its rivals with mass) plus L0's and L1's published facts,
  and nothing else (L3-S37); it never revises L2, and L2 reads nothing L3 publishes; a backward edge is tested by
  measurement as soon as there is reason to suspect it helps (L3-S38); L3's cost scales with the working span, and its
  publication covers exactly the working span (L3-S40, as the reading file quotes it at Rows 19.53 and 19.54); a
  ruled-out reading is published, not dropped (L3-S13, from the reading file's AGREES verdicts at Rows 19.76 (i) and
  19.79, not from a quotation of L3-S13 *[marked by the check, §12 item 4]*); evidence-class facts are published broadly, each with its
  establishment status (L3-S15, as the reading file quotes it at Row 19.81). Which effort dials exist, and their
  defaults, is deferred (D-202). (L3-S37 and L3-S38 as the S38 ratification record states them **[checked there]**;
  L3-S13, L3-S15 and L3-S40 as the reading file quotes them **[checked at the reading file]**, the derivation itself not
  opened by this sitting.)
- **Documentation only:** if ratified, the 14 row-parts are recorded ADOPTED (Rows 38.47 and 38.48 in part E's narrower
  wording), which adds six statements to the amended L3 specification: (A) every cost-driving choice of L3 is a setting,
  every optional expensive refinement a separable stage, and re-analysis after an edit covers the edited span and a
  bounded margin; (B) style lives only in fitted values, never in structure; (C) L3 uses all the information the layers
  beneath publish, a recomputable ruled-out reading need not be published, never computing an alternative is no loss
  while dropping a computed one is, and a fact no one reads is declared dormant with its consumer named or removed;
  (D) the code computing L3 depends on no type of the score editor; (E) a coverage miss is remedied inside L3, a
  backward edge only as D-466's exception; (F) the grouping is an explanatory output, not an accuracy requirement. The
  re-marking of the rows and the writing of the statements are the application dispatch's act (route record §2 step 2),
  not this sitting's.

## 9. Recommendation

**Ratify parts A to F as derivations, part E in the narrower wording.** Towards the ultimate objective (#4): neutral on
this side's reading — each part carries a rule the register already holds and changes no inference; part E's narrowing
keeps the route to a measured backward edge open, which is what the objective's rule of 2026-10-07 asks. Towards the
guiding principles: the live register entries D-024, D-030, D-033, D-035, D-072, D-099, D-229, D-297, D-461 and D-480
carried into L3 rather than left behind *[corrected by the check, §12 item 5; former wording: "seven live register
entries (D-024, D-030, D-033, D-035, D-099, D-229, D-297) and two more (D-461, D-480)"]*; D-466 respected rather than overridden. Meta level: the
analysis's own specification text, documentation only. The alternative the route record allows is to leave the rows as
proposals; this side sees no gain in that.

## 10. What follows

1. The check of this surface at its sources, in its own turn.
2. Then, unless the check finds a real choice, the question whether to ratify parts A to F as derivations, alone, plain
   text, documentation and algorithm stated separately.
3. Then the last cut of item 13: facts from the published literature (20.31 (i), 36.106 (i), 56.2 (i)–(ii)); then item 14.

## 11. Read by this sitting

Entry 520 whole; entry 291 whole (short; §3 and §4 are the named sections); the start-up chain at the other sections
the 2026-11-02 amendment names (entry 118, the first paragraph of "THE BRIDGE FAULT"; entry 152, item (vi); entry 169,
its "Boot" block and "The cadence for your session"); `STATUS.md` whole; the gating answer at its counts (222 gating of
247 open); `DECISIONS.md` at the index rows of D-022, D-024, D-030, D-033, D-035, D-072, D-099, D-100, D-202, D-229,
D-254, D-295, D-297, D-461, D-466, D-480, D-522, D-581, D-599, and searched for the subjects of the rows; the display
and span-kinds ruling records whole; the span-kinds surface whole (for the form); the L3-S38 ratification record whole;
the tractability record of 2026-10-05 at lines 47–111 and searched; the sections ruling record at lines 130–165 and
searched for *style*; the publication-to-next-layer record of 2026-10-06 searched; the reading file at §5 (366–432), the
fourteen rows' entries (10437–10453, 24281–24296, 24357–24368, 24715–24731, 24761–24782, 25094–25136, 25182–25193,
25741–25753, 42101–42124, 47404–47430), the marks at lines 25422–25437, 27104–27109, 46440–46451, 47158–47166 and
48728–48743, and searched for D-072, D-229, D-461, D-466. **Not read:** the derivation itself; the register entries'
home texts and the `decisions/` group files; the input contracts; nothing-from-L3 Ruling 3's own record; `CLAUDE.md`
and `DECISIONS.md` whole (the start-up read narrowed on the user's word). *Added by the check:* the reading file at
lines 8634–8645; the sections ruling record searched for its headings and ruling numbers.

## 12. The check, run in the turn after the surface landed — eight corrections

Each quotation re-read at its line; each row's entry line, grading and proposal re-read; each register row re-read at
its index line and each "lies in its home" at the marks line cited; the cited ruling records re-read at the lines used;
the sweep for absolutes read each "every", "all", "never", "none", "nothing", "only", "already", "no" and "each" at its
line, the rows' and proposals' own wording left as quoted. **No part's filing changed, part E's narrowing stands, the
recommendation stands, and no real choice arose.**

1. §1: member 8's identity cited line 8642 alone, which names D-461 without its file. Now lines 8642–8643 and the index
   row, and marked as this side's reading of the two.
2. §3, part B weak point 1: the open naming-scheme question is sections **Ruling 3**, not Ruling 6 (the record's §3b;
   "Ruling 6" in that record is the 2026-10-07 record's).
3. §7, part F weak point 1: the same error. Corrected.
4. §8: L3-S13's content was stated as if quoted; it rests on the reading file's AGREES verdicts. Marked.
5. §9: "seven … and two more" left out D-072, which part D cites. Now the entries are listed without a count.
6. §1: "The derivation is silent" at every part is the reading file's axis; the derivation was not opened. Stated once.
7. §3, part B weak point 2: "None is on the record this sitting read" was wider than the act, which did not search for
   a reason to break D-024. Narrowed.
8. §4, part C weak point 2: D-522 was paraphrased; now quoted at its line.

*Found and not acted on (outside this cut, judged against the plan):* nothing.

*Provenance: Cowork, 2026-11-04 (Stockholm), the sitting booted on entry 520. The user's words: the opening instruction;
"narrowed"; "continue" (the check).*

# L2 tail — the scope rows and the single rows: decision surface, 2026-10-10

> **STATUS: DECISION SURFACE.** Cowork, 2026-10-10 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_twenty_nine.md`. Delivered as text, nothing asked.
> The check runs in the next turn; the questions come after it, one per turn. Nothing here is applied: the reading
> file's rows are re-marked by the application dispatch the L2 route ruling names as its step 2.

## 0. What this surface covers

The L2 comparison (`ratification_surfaces/cowork_comparison_l2_reading.md`) left 432 row-parts UNPLACED, meaning
the comparer could not name one filing label for them. The family rulings of 2026-10-04 to 2026-10-09 placed 335
of them. Six are held on purpose. Five of those six are held by your rulings, waiting on two open questions: whether
L2 should read chord patterns longer than pairs, and which dials the effort setting gets. The sixth, Row 7.104(i), is
held by the tractability record's §1c, which is this side's record and not a ruling. 91 rows were reached by no
family. The route ruling of 2026-10-04 says how they are taken: in families cut by member and subject, the cut and
the order chosen by this side, and you may change either.

This surface takes the small group: five row-parts that are not about the style and idiom system.

**One change to the cut I proposed last turn.** Row 23.222 claim (ii) moves to the style family. The row says the
analysis is "a pure function of notes + key signature + preferences". Whether a preference may reach the analysis
is the question the style rows raise: one of them is D-503, at its register index line: "The idiom mixture is
DISCOVERED from the score and merely SEEDED by the user's preset, in three forward-only phases". *(Corrected at the
check; former wording, kept: "D-503's "the idiom mixture is discovered from the score and merely seeded by the
user's preset"" — a quotation with its capitals changed and its last clause dropped.)* Placing the row here would answer that question in advance. So this surface
covers five row-parts, not six.

The filing labels, as the comparison defines them (its §5):

- **ADOPTED — carried:** a derived statement already says it.
- **ADOPTED — proposed:** a proposal to add it to L2's text.
- **RELOCATED:** it belongs to another part of the framework.
- **QUARANTINED:** it describes how the code works, and is kept with a question for the audit.
- **HISTORICAL:** an event, a build state, a superseded plan or a status.

L2 is the part of the analysis that decides the key, the chords, where each chord begins and ends, and which notes
are chord tones.

## 1. Follows from a ruling already given — recorded as this side's derivation, not asked

**Row 5.253 claim (i)**, `cowork_layer5_function_design.md` §9: *"Rejected: (a) treating each override as a
bespoke one-off (it hides that they are the same mechanism and makes generalizing a rewrite)"*. The comparison
left it UNPLACED "with Row 5.218(ii) — a rule about how the overrides of the general mechanism are organized".
Weight-meaning Ruling 3 of 2026-10-05 found that this mechanism has no site in L2. The mechanism is the old
function layer's forward override, which overturns an earlier decision when later evidence is decisive (D-339).
That ruling placed the mechanism's rules HISTORICAL, Row 5.218(ii) among them. A rule about how that mechanism's
overrides are organized falls with it.

**Placed HISTORICAL**, as this side's derivation (D-599). You may challenge it at the row. Documentation only.
L2's algorithm is unchanged.

## 2. Confirmation 1 — Row 2.20, "a selection-aware capability is a parameter on the one orchestrator"

**The row** (`ARCHITECTURE.md`, the Layer-3 section): *"A selection-aware capability is a PARAMETER on the one
orchestrator, never a sibling (D-623 …)."*

**What it is about.** D-623 is LIVE in the decisions register. In plain words: when the program was taught to
analyse only part of a score, this was built as an option on the existing driver, not as a second driver. So one
path still builds the notes, cuts them into slices and runs the analysis. It is a rule about how the program's
code is organised, not about what the analysis decides.

**What already stands.**

- The next row, Row 2.21 ("the capability was built as an option on the existing driver"), is proposed
  QUARANTINED with the audit question *"is there one driver that builds, slices and decodes, with
  selection-awareness as an option on it?"*. That question checks exactly what D-623 requires.
- For the analysis itself, L2-S48 states: *"The result after any sequence of enlargements equals a single fresh
  run over the final loaded span."* The framework's C-8 states: *"Whole-score analysis is the degenerate case."*
  A selection and a whole score are therefore one analysis in L2's text already.
- The phase rule (`CLAUDE.md` Conventions) reserves comparing specification against code for the audit.

**Why it is UNPLACED.** None of the labels fits a rule about code structure. RELOCATED needs a part of the
framework to send it to, and none of the framework's parts is the home of code structure.

**Alternatives:**

- **A — QUARANTINED, travelling with Row 2.21 and its audit question.** D-623 stays LIVE at its own home.
  - Towards the objective (#4): the audit checks that there is one path, which is what protects the result.
  - Towards the principles: #6, because the rule keeps one home and L2's text does not copy it. The phase rule
    puts code checks at the audit.
  - Cost: QUARANTINED is defined for a statement of how the code works. Here it is stretched to a rule for the
    code, and the stretch is recorded beside the row.
- **B — ADOPTED — proposed**, the sentence: "A selection and a whole score are analysed by one procedure, the
  working span its only difference."
  - Towards the objective: nothing gained. L2-S48 and C-8 already state it.
  - Towards the principles: against #6, a second statement of a rule L2's text already carries.
- **C — leave it UNPLACED.**
  - Towards the principles: against the route ruling, which asks you to place UNPLACED rows.

**Recommended: A.** Meta level: a filing label on one row. **Documentation only. L2's algorithm is unchanged.**

## 3. Confirmation 2 — Rows 34.1 and 34.4, the product's scope lists

**The rows** (`ARCHITECTURE.md` §16, *Scope Reference*).

- **Row 34.1** is the core scope. It begins *"Harmonic analysis (functional, modal, extended tonal, jazz)"* and
  goes on through twenty-four further items. Among them are tuning, file persistence, undo, localization,
  "extensible style system, initial five styles" and "musical language detector and graceful degradation".
  Several of them are about the analysis and not the product, and §3's Alternative A now names each one's home.
  *(Corrected at the check; former wording, kept: "goes on through about twenty product features" — the items
  were counted at the row: twenty-four, and not all of them are product features.)*
- **Row 34.4** is what is out of scope. It lists *"Live and real-time operation, film synchronization, adaptive
  game music, non-Western traditions (graceful degradation at boundary), post-tonal and serial music (graceful
  degradation at boundary), audio transcription from recording, spatial music, extended techniques as primary
  language."*

**Why they are UNPLACED.** Each is one sentence that mixes product features with a few clauses about the
analysis, so no single label covers it.

**What the record already answers in them.**

- **34.1, "modal":** tonality-vocabulary Ruling 1 of 2026-10-04 writes the church modes into L2 as a named
  increment, and the record says the sentence "goes to the tail with the UNPLACED rows by subject, its
  'modal' clause recorded here as answered".
- **34.1, "jazz":** chord-vocabulary Ruling 2 of 2026-10-05 names an increment for added notes. Until it lands,
  a jazz `Cmaj9` reads as `Cmaj7` with the ninth as an elaboration.
- **34.4, "graceful degradation at boundary", and 34.1, "musical language detector and graceful
  degradation":** D-498 is LIVE in the register: *"a product stance is owed for
  output that is mostly uncertain, and for music outside the tonal vocabulary altogether."* The silence family
  of 2026-10-05 RELOCATED Row 1.19 to *the uncertainty surface* "beside D-498's owed display decision". In L2, doubt
  is shown by the weights of the rival readings alone. Silence Ruling 1, read at the record at the check: "Over
  every stretch where notes sound, the chord-and-key layer infers and publishes its best reading of the harmony
  with the rival readings and their weights … Doubt is shown by the weights alone". So on post-tonal music L2
  still publishes readings, with their weights.
- **34.1's other clauses that concern the analysis, each already with a home** (this side's reading of where
  each belongs, from the framework's §3.1 and §5):
  - "voice leading analysis and optimization": *the second axis — voice leading*.
  - "ornamentation (analysis …)": L2's elaboration relations (passing, neighbour, suspension, anticipation).
  - "enharmonic spelling" and "pickup bars and anacrusis": *L0 — The notated record*.
  - "chord symbol input": not input to the analysis; written chord symbols are comparison material only
    (`FRAMEWORK.md` §3.1).
  - "incremental analysis cache": C-8 ("Re-analysis after an edit is incremental over the changed stretch plus a
    bounded margin") and working-span Ruling 3 of 2026-10-09.
  - "extensible style system, initial five styles": the style family.
- **UNSETTLED — 34.1, "monophonic chord inference":** chords inferred from a single melodic line. No home was
  found for it at the record this sitting read. Filing the sentence decides nothing about it, and it is recorded
  beside the row as open.

**Alternatives:**

- **A — split each sentence by clause.**
  - Row 34.1: its "modal" and "jazz" clauses recorded as answered by the two increments; its "musical language
    detector and graceful degradation" clause RELOCATED to *the uncertainty surface*, with Row 1.19 and D-498;
    the homes of its other analysis clauses recorded beside it (above), with "monophonic chord inference"
    recorded as UNSETTLED; the rest of the sentence HISTORICAL, as the product's scope status.
  - Row 34.4: its "graceful degradation at boundary" clause RELOCATED to *the uncertainty surface*, travelling
    with Row 1.19 and D-498; the rest HISTORICAL.
  - Towards the objective (#4): the two clauses that bear on what a user sees for music L2 cannot read well are
    kept, at the place where that display decision is owed.
  - *(Corrected at the check; former wording of Row 34.1's part, kept: "its "modal" and "jazz" clauses recorded
    as answered by the two increments; the rest of the sentence HISTORICAL, as the product's scope status". It
    filed as a product status a graceful-degradation clause and several analysis clauses that have homes. The
    former objective line read "the one clause".)*
  - Towards the principles: #12, nothing set aside unheard; #6, each clause filed once.
- **B — both rows HISTORICAL whole.**
  - Towards the principles: simpler, but it files the graceful-degradation clause as a status when D-498 still
    owes a decision on it (against #12).
- **C — ADOPTED — proposed:** a scope statement added to L2 ("L2 reads tonal music; outside it, it publishes
  low-weight readings rather than refusing").
  - It adds a sentence to the algorithm's specification. In this side's reading it says nothing silence Ruling
    1 does not already make L2 do. *(Corrected at the check; former wording, kept: "that says nothing L2's
    weights do not already do", stated as a fact where it is a reading.)*
  - Against #6 and D-630, which says do not add a component without a measured shortfall it resolves.

**Recommended: A.** Meta level: filing labels on two rows. **Documentation only. L2's algorithm is unchanged.**
The product scope itself stays where it is, at `ARCHITECTURE.md` §16.

## 4. Decision — Row 13.26 claim (i), "the same music in different voicings should give the same chord"

**The row** (`docs/nct_detection_design.md`, its *Quality impact estimate*): *"Same music in slightly different
voicings should produce same chord ID; NCT detection stabilizes this if voice-leading context is consistent."*
Claim (ii), the second half, is proposed HISTORICAL by the comparison and is not part of this question.

**The question in plain words.** If a passage is re-voiced, the inner voices respaced or a note doubled, should
L2 read the same chord?

**The method that stands** (the derivation, read at the file this sitting):

- **L2-S28:** the figure (the inversion) is decided in the reading. It is *"the chord member the reading takes
  as the span's structural bass"*, and a term relates it to the lowest sounding pitch of each slice.
- **L2-S24:** whether a note is a passing note, neighbour, suspension or anticipation is read from each voice's
  own melodic motion, as L1 publishes it.
- **L2-S30:** *"No chord term decides a chord from the pitch-class content of the span alone"*. The chord terms
  also read the neighbouring chords, which notes count, and the voice-leading evidence.
- **L2-S32:** the content term counts the span's notes that do and do not fit the chord, in duration-weighted
  and metric-weighted forms.

So under L2 as derived, a re-voicing that moves the bass, or changes how a voice moves, may rightly change the
reading. The outgoing text's own second half makes the same condition ("if voice-leading context is
consistent"). A re-voicing that changes only spacing or doubling leaves the bass and the voices' motion alone.
*This side's reading, not checked:* a doubled note is one more note event, so it adds duration weight to the
content term, and that could shift the weights between rival readings. Whether it can move the principal reading
is not known.

**The positions:**

- **1 — HISTORICAL:** a hope stated in an old design's quality estimate. L2's own statements decide what may move a
  reading.
  - Documentation only; the algorithm unchanged.
  - Towards the objective: no check that L2 is not over-sensitive to doubling.
  - Towards the principles: #12 is weak here; a sound musical intuition is filed away untested.
- **2 — RELOCATED to *the measurement of the analysis*, narrowed:** a robustness check for the measurement-design
  stage. On passages re-voiced so that only spacing and doubling change, with the bass, the spelled pitch content
  and each voice's motion unchanged, the principal reading is compared before and after, and a change is reported
  as a finding.
  - Documentation only now; the algorithm unchanged. If the check later finds L2 over-sensitive, the remedy would
    be a separate ruling.
  - Towards the objective (#4): over-sensitivity to doubling is found on the music, not assumed away.
  - Towards the principles: D-254 (investigate by default); #12; D-630 (no new rule without a measured need).
    The precedent is Row 7.48, proposed RELOCATED to the measurement of the analysis.
- **3 — ADOPTED — proposed:** an invariance statement added to L2, with a falsifier: "a change of spacing or
  doubling alone does not change the principal reading".
  - This **changes the algorithm as the specification defines it**: it adds a constraint, which might force the
    content term to discount doubled notes.
  - Towards the objective: it might help, but nothing has measured a problem.
  - Towards the principles: against D-630 and #17(b), a rule with no measured basis. It also risks contradicting
    L2-S32's duration-weighted forms (#6).

**Recommended: 2.** Meta level: the analysis's measurement list.

## 5. What this surface does not do

- It places nothing until you rule.
- It writes no dispatch.
- It does not touch the six held rows.
- It does not take up the style family (85 rows, with Row 23.222(ii)).

## 6. What was read for it

- At the reading file: the five rows whole, Row 2.21, Row 2.22 and Row 17.11.
- In the derivation: L2-S24, L2-S27 to L2-S30, L2-S32, and L2-S44 to L2-S49.
- In `FRAMEWORK.md`: §1.3, §2 (C-1 to C-9), §3.1 to §3.3, and the L2, L3, voice-leading and NOT A LAYER blocks
  of §5.
- In `decisions/group_I.md`: D-623 whole.
- D-498 at its index line only.
- The ruling records cited, at the passages named.

At the check, also read: silence Ruling 1 at its record; chord-vocabulary Ruling 2 at its record.

Not opened: `ARCHITECTURE.md` itself, `docs/nct_detection_design.md`, `cowork_layer5_function_design.md`, and
D-498's own entry.

## §B. The check, run at the sources in the turn after the surface was delivered

Every quotation was compared with its source. Every claim was tested for completeness, coherence, correctness
and words wider than what was read. The four corrections are made at their sites above, each with its former
wording kept:

1. **D-503's quotation** had its capitals changed and its last clause dropped. It is now quoted as its register
   index line reads.
2. **Row 34.1's length** was given as "about twenty product features". It is twenty-four further items, counted
   at the row, and several are about the analysis, not the product.
3. **Incompleteness in §3, the one correction that changes an alternative.** Alternative A filed the whole
   remainder of Row 34.1 as a product status. That remainder holds a second graceful-degradation clause
   ("musical language detector and graceful degradation"), now RELOCATED with the 34.4 clause. It also holds
   analysis clauses that already have homes, now recorded beside the row, and one clause with no home found,
   "monophonic chord inference", now marked UNSETTLED. The recommendation is unchanged: A, as amended.
4. **Alternative C's cost in §3** stated as a fact what is this side's reading. It is now labelled as a reading,
   with the ruling it rests on, silence Ruling 1, read at its record.

**Confirmed at the objects, unchanged:**

- §1 (Row 5.253(i) and weight-meaning Ruling 3).
- §2: D-623's register entry, Row 2.21's audit question, L2-S48 and C-8 quoted exactly; the framework's §5 has no
  home for code structure.
- §4: L2-S24, L2-S28, L2-S30 and L2-S32 quoted or summarised from the derivation; the Row 7.48 precedent at the
  tonality-vocabulary record.
- The arithmetic: 335 + 6 + 91 = 432; 5 here + 1 travelling + 85 in the style family = 91.

Nothing in the check moved a recommendation.

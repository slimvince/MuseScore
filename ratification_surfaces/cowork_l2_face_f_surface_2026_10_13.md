# Ratification surface — face (f) of the L2 specification: the candidate score, and how its parts combine

> **STATUS: DECISION SURFACE, delivered for reading. Nothing is asked in the turn that delivers it.** Cowork,
> 2026-10-13 (Stockholm), the sitting booted on `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_eighty_five.md`.
> The check of this surface is the next turn's; the question comes after that, alone. Nothing here is applied:
> every change named below is made later by a dispatch, and nothing is ratified by this file.

## 0. What is being decided, from the beginning

**The file under ratification** is `cowork_derived_specification_l2_2026_10_10.md`, the "successor". It is the
specification of L2, the layer that decides for each stretch of music the tonality, the chord, where one chord
gives way to the next, and which sounding notes belong to the chord. A deriving session wrote it blind, and it was
then amended by the forty-three L2 family rulings of 2026-10-04 to 2026-10-10. Its banner says NOT RATIFIED.

**How it is ratified.** On 2026-10-13 you ruled "option 3, one aspect at a time", so the file is ratified one face
at a time, nine surfaces in all (`records/cowork/rulings/cowork_rulings_2026_10_13_l2_ratification_granularity_sitting.md`).
Faces (a) to (e) — statements L2-S1 to L2-S30 — were ratified the same day. Their ruling records are the five
`cowork_rulings_2026_10_13_l2_face_*_ratification_sitting.md` files in the same folder.

**Face (f)** is the sixth face: the nine statements L2-S31 to L2-S39 (successor lines 1172 to 1525).
Together they say how L2 puts a number on a candidate reading of the music (the "candidate score"), how that number
is built from parts, how the search over readings may and may not cut corners, and how the parts' weights are
learned. One complete answer for the loaded music — every stretch's tonality, chord, boundaries and note roles — is
a **reading**. In plain words:

- **L2-S31:** a reading's candidate score is a sum of terms over each stretch ("span terms") plus terms over each
  pair of neighbouring stretches ("pair terms"). How long a stretch lasts is decided as part of the reading, not
  fixed in advance.
- **L2-S32:** the content term rates how well a stretch's notes, each with its role (chord tone or a named
  elaboration), fit the spelled chord. It counts notes that sound but do not belong, and chord members that do not
  sound. A missing chord member is a cost, never a disqualification.
- **L2-S33:** where an elaboration's preparing or resolving note lies in the neighbouring stretch (a suspension
  prepared in the previous chord, say), the term reads that neighbour's candidate chord. So the pair term also
  carries elaborations that cross a boundary. The published "weak" form, in which a stretch's term sees only its own
  chord, is not used.
- **L2-S34:** three families of terms link the stretches: (i) a cost for changing tonality, graded by the distance
  between the two tonalities in a published tonal space; (ii) the tonality–chord cost of L2-S3; (iii) a progression
  term on each pair of neighbouring chords read as degrees in their own tonalities, which is also how a cadence
  confirms a tonality. Every weight is fitted, and no term rewards a chord root simply continuing.
- **L2-S35:** the weights of all readings of the loaded music together sum to one. One stretch's rivals are never
  normalised against each other alone.
- **L2-S36:** the search is exact, or it drops a reading only on proof that it could not finish above one kept.
  No search that keeps a fixed number of the best partial readings (a "beam") is admitted. If exactness cannot be
  afforded, the rule gives way only by a ruling (open question OQ-L2-8).
- **L2-S37:** L1's three cadence cues are read only as their standing allows. The leading-tone cue may carry load.
  The falling-fifth and fourth-and-seventh cues rest on a stand-in window and may not be read by any fitted term
  until the window is measured (OQ-L2-12).
- **L2-S38:** every weight is learned from annotated music, never set by hand: the tables counted once and frozen,
  the short list of combination weights fitted to the graded measure, only on freely licensed music, every recorded
  analyst variant accepted as an answer. No value is given.
- **L2-S39:** a distance or profile from published theory (Lerdahl's tonal pitch space, Weber's table, a scale-degree
  profile) enters as one feature with one fitted weight; its own constants stay as published.

A "statement" in this file has six fields: the statement itself (in bold), its defense, its source class, its
status, its premise with the way the premise could fail unnoticed (the "false-negative path"), and its falsifier
(how to test the code against it). Rulings are written beneath a statement as short sub-items.

## 1. What was read for this surface (each at the object, this sitting)

**The successor:** §3f whole (lines 1172–1525); in §4, OQ-L2-3 (lines 1995–2081), OQ-L2-8 (2106–2120), OQ-L2-12
(2147–2150), OQ-L2-13 (2151–2164) and the closing count (2202–2204); searches of the whole file for "OQ-L2-8",
"sizing" and "effort setting".

**The ruling records, whole:** score decomposition (2026-10-07; L2-S31), nothing from L3 (2026-10-07; its note on
DP-O beside L2-S31), span content term (2026-10-09; L2-S32), crossing elaborations (2026-10-09; L2-S33), tonality
and progression terms (2026-10-06; L2-S34), weight meaning (2026-10-05; L2-S35 with L2-S40), tractability
(2026-10-05; L2-S36), cadence cues (2026-10-09; L2-S37), fit (2026-10-05; L2-S38), published theory terms
(2026-10-09; L2-S39).

**The paper sizing** `ratification_surfaces/cowork_l2_search_sizing_2026_10_05.md`, whole (the act the tractability
record's route named; its §C records your word on its result).

**The application dispatch** `records/cc/instructions/cc_instruction_l2_application_2026_10_10.md`: its
construction-state table (lines 18–67); its section headings by search; §L.11 whole (1100–1190); §L.12 whole
(1191–1238); §L.15 at 1422–1499; §L.18 at 1880–1919 and 1984–1993; §L.20 at 2115–2164 and 2210–2219; §L.21 at
2276–2307 and 2370–2379; §L.36 at 4060–4099 and 4150–4159; §L.37 at 4214–4258 and 4300–4316; §L.38 at 4355–4389;
§L.39 at 4495–4544 and 4594–4603; and the lines 1243–1250, 1312–1319, 1336–1347 and 3562–3569, found by search for
"L2-S35", "sizing" and the held rows. **The dispatch names one of the nine statements at 359 places**; this sitting
did not read every one. It read the entries of the ten families above at their "points noted for the user", found
by a search for "Noted for the user", "may overrule" and "may have".

**Also read:** the face (e) surface whole, as the form this surface follows; the face (a) surface at lines 135–146
(its C6 and the ground stated with it); the face (b) surface at lines 56–62 and 142–149 (its routing to L2-S33);
the five earlier face ruling records whole; `STATUS.md` whole.

**How the rulings were found.** By the method the handoff entries set: the family each statement belongs to is named
in the dispatch's construction-state table and in the sub-items beside the statement, and each family record was
read whole. **That finds a ruling only where it is filed against one of the nine statements, or names one by its
identifier.** A ruling that bears on one of them without either is not found. Three that bear on this face were
found another way, by reading OQ-L2-3 whole in the successor, and are named where they bear: the any-boundary-set
record of 2026-10-07, whose OQ-L2-3 sub-line says "L2-S7's and L2-S31's wordings are unchanged"; the
notated-boundary-evidence record of the same date, whose sub-line says "L2-S13's, L2-S31's and L2-S33's wordings are
unchanged"; and the structural-bass record of 2026-10-08, whose OQ-L2-3 item names L2-S39.

## 2. The nine statements, checked against the rulings' words

- **L2-S31 — span terms plus pair terms; stretch length decided.** *Rulings:* score decomposition Rulings 1 to 4
  ("confirmed" ×3, "Confirmed"): rows placed; Rulings 1 and 3 each say "**L2-S31's wording does
  not change**", and the record's arithmetic says it again. *Shown beside L2-S31:* Ruling 1's carried remedy (a
  piece-level tonality term, if the measurement-design stage finds L2 losing the choice between a key and its relative
  over whole passages), Ruling 3's recorded observation, and the nothing-from-L3 record's note for whoever takes up
  DP-O (pairs against longer chord-to-chord terms against a hierarchy, to be measured). **The "wording does not
  change" sentence is not shown.** **Matches** — §4, correction 1.
- **L2-S32 — the content term.** *Rulings:* span content term Ruling 1 ("confirmed"): rows placed; "**Algorithm:
  unchanged.** L2-S32's wording does not change." — **not shown**. Ruling 2 ("confirmed"): one more arm for OQ-L2-3's
  held-out comparisons (the content term with an elaboration split by whether its spelled pitch lies in the tonality's
  collection, against the term without the split) — shown, by a pointer beside L2-S32 to its sub-line under OQ-L2-3.
  **Matches** — §4, correction 1.
- **L2-S33 — crossing elaborations read the neighbour's candidate chord.** *Rulings:* crossing elaborations Ruling 1
  ("yes"): rows placed; "**Algorithm: unchanged.** L2-S33's wording does not change." — **not shown**. Ruling 2
  ("3"): one item for OQ-L2-3 (whether an elaboration's name is decided inside the score or derived afterwards) —
  shown by a pointer. The record's "Recorded beside it, not ruled" sentence (L2-S33's premise condition — that
  "pedal point" is an admitted relation — is met) — shown, the Premise field unedited. **Matches** — §4, corrections
  1 and 2.
- **L2-S34 — tonality change, tonality–chord cost, progression on degrees.** *Rulings:* tonality and progression
  terms Rulings 1 to 5 ("confirmed" ×5): rows placed; Rulings 3 and 4 add two held-out comparisons to OQ-L2-3; the
  record's §1f: "L2-S34 stands as derived; the two held-out comparisons added to OQ-L2-3 (Rulings 3 and 4) are
  additions to its open question, not changes to its wording." *Shown:* the §1f sentence as a recorded sub-item,
  pointers to both OQ-L2-3 sub-lines, Ruling 1's carried named remedy and the four rulings' "cost accepted"
  sentences. Published theory Ruling 2 also adds a candidate to the same comparison and is shown by a pointer beside
  L2-S34. **Matches**, with one field overtaken — §4, correction 3.
- **L2-S35 — whole-reading normalisation.** *No ruling names its wording.* The weight-meaning record places its rows
  and rules (Ruling 3) that D-339's forward override has no site in L2 — shown beside L2-S35. It says nothing of the
  statement itself, and the dispatch records that the surface's "stands" is not the record's (§L.15 item 7). So
  L2-S35 is **put on its derived defense**: per-stretch normalisation causes the label-bias problem — the transitions
  leaving a state "compete only against each other" (Lafferty, McCallum & Pereira, relayed), so, in the derivation's
  own words, later evidence could "change which branch wins but not how much mass flows into the branch"; the charter's own reason for forbidding early discarding has the same
  shape. **Checked against weight-meaning Ruling 1**, which says a stretch's published rival weights sum to "at most
  one": no conflict — L2-S35 is about the model's distribution over whole readings, and a published subset of one
  stretch's rivals can sum to less. **Matches.**
- **L2-S36 — exact search or a provably safe bound; no beam.** *Ruling:* tractability Ruling 1 ("yes"): "L2-S36 stands
  as derived"; "the end" is the end of the loaded music, not the whole score; a reading the admission rule never
  generates is not discarded (D-297), and what L2-S36 bars is dropping a reading the search has begun to score; an
  effort setting may not quietly reduce how many readings are kept. *Shown:* the ruled sub-item and, beside the
  statement, the proposed sentence of (iii). The route for OQ-L2-8 is shown under OQ-L2-8 in §4. **Not shown:** what
  the paper sizing found and your word on it (its §8 and §C). **Matches** — §4, correction 4.
- **L2-S37 — cadence cues as their standing allows.** *Rulings:* cadence cues Ruling 1 ("yes"): rows placed;
  "**Algorithm: unchanged.** L2-S37's wording does not change." — **not shown**. Ruling 2 ("3"): one item for OQ-L2-3
  (the score with a cue term against the score without it; the two window-dependent cues only once OQ-L2-12 has
  measured the window) — shown by a pointer. **Matches** — §4, correction 1.
- **L2-S38 — every weight fitted.** *Rulings:* fit Ruling 1 ("2"): the second sentence amended — "The tables are
  counted from annotated music, once, and frozen; the short list of combination weights is fitted discriminatively,
  to the graded measure." — written into the bold text, the former sentence kept beside it; Ruling 1's three
  UNSETTLED items shown; Ruling 2 ("confirmed": D-383's fixed ranking and the old fitter's exemption do not carry)
  shown; Ruling 3 ("yes": OQ-L2-13's interim) shown under OQ-L2-13 with a pointer. **Matches.** *The amended bold
  text against its other fields:* the Premise (the annotated corpora carry what the fit needs) and the Falsifier
  (falsified if a weight is hand-set, if evaluation data overlap fit data, or if the fit pool holds music under a
  non-commercial or unstated licence) still test what the statement says. The one thing the amendment dropped from
  the bold text is taken up at §3 point 9.
- **L2-S39 — a published distance enters with one fitted weight.** *Rulings:* published theory Ruling 1 ("yes"):
  rows placed; "**Algorithm: unchanged.** L2-S39's wording does not change." — **not shown**. Ruling 2 ("yes"): a
  counted key-change table added as a candidate to the tonal-space comparison — shown by a pointer. Ruling 3 ("2"):
  the forms rule — "Every term's form is taken from established music theory or published research and fixed before
  any value is attached to it" — shown beside L2-S39, with its algorithm paragraph and accepted cost; the §1d bound
  (no primary of Lerdahl or Weber is held) shown. **Matches** — §4, corrections 1 and 2.

**The Premise and Falsifier fields.** One ruling of this face amended bold text: fit Ruling 1, L2-S38's second
sentence. Its Premise and Falsifier were checked above and still match. No other statement's bold text was amended,
so no other Premise or Falsifier has fallen behind its statement on that ground. One other field was overtaken by
later rulings without its bold text changing: L2-S34's Source class (§4, correction 3).

## 3. The points the dispatch noted for you, each tested against the record (D-599)

Each point below is answered by the record or by a rule already ratified. None is put to you as an option, except
the three parts of §4 marked droppable (the pointer beside L2-S32, and parts (c) and (d) of correction 4).

1. **No "wording does not change" line beside L2-S31, L2-S32, L2-S33, L2-S37 and L2-S39** (§L.20 item 3, §L.36 item 1,
   §L.37 item 1, §L.38 item 1, §L.39 item 7). The ground on which you ratified face (a)'s C5, and the correction 1
   of faces (b), (c) and (e), applies the same way: the specification shows every ruling that touched a statement, by
   one line and a citation. It is correction 1 below. The dispatch offered each record's arithmetic paragraph with
   the line; the earlier faces' lines quote the ruling's sentence and cite the record, and this surface follows them.
2. **Score-decomposition Ruling 3's recorded observation stands beside L2-S31, though it speaks of L2-S32's terms**
   (§L.20 item 2: "he may have it written beside L2-S32 instead, or beside both with one quotation and one pointer").
   The observation is that if an over-reading of the old kind returned, it would show as a heavy weight on
   assignment-blind forms of L2-S32's terms. It stays where the record put it (under L2-S31's family). **Proposed, as
   part of correction 2: a pointer beside L2-S32 to it**, so a reader of L2-S32 meets it, with nothing quoted twice
   (#6). This pointer is this side's proposal, and you may drop it.
3. **The DP-O note beside L2-S31** (§L.21 item 4: he may have it beside L2-S49 instead, or left out). It names
   L2-S31's premise and falsifier by name and says the measurement it asks for could change them. By the ground
   stated with face (a)'s C6 — "where an open measurement says something survives under, or may change, a
   statement, the statement points at it" — L2-S31 is where it belongs, with the pointer beside L2-S49 that face (h)
   will meet (the pointer relayed from the dispatch's item 4; not read in the successor this sitting). **It stands.**
4. **L2-S32's pointer to the content-split arm, and the Row 10.23 reading written in the two rows' lines** (§L.36
   items 3 and 4). The pointer follows the same ground. Row 10.23 names no derived statement and stays a proposal under
   the route ruling ("Rows no family reaches stay proposals"); the sentence about it concerns how the arm would test
   collection membership, which is the arm's own business under OQ-L2-3. **Both stand.**
5. **L2-S33's premise-condition sentence, written as a recorded sub-item and not as an edit of the Premise** (§L.37
   item 2), **and whether L2-S23 should also point to the crossing-elaborations item** (§L.37 item 4). The record says
   "the application act may say so beside the premise", and the Premise as written stays true (the path it describes
   still holds; its condition is now met). **It stands.** The pointer beside L2-S23 was ordered by face (d)'s
   correction 1, which you ratified. **Nothing remains.**
6. **L2-S34: the recorded "stands as derived" sub-item, and the two OQ-L2-3 proposals placed under OQ-L2-3 with
   pointers beside L2-S34** (§L.18 items 1 and 2). The record calls them "additions to its open question, not changes
   to its wording". **Both stand.** Two further pointer questions: **beside L2-S34 for the cue item** (§L.38 item 3) —
   not owed, because the record says that if the cue term pays, "L2-S37 gains the term", so the item may change L2-S37
   and not L2-S34; **beside L2-S34 as well as L2-S39 for the counted key-change table** (§L.39 item 3) — owed and
   already written, because published theory Ruling 2 says that if the table wins, "L2-S34 (i)'s words "in a
   published tonal space" are amended by their own ruling then". **Nothing remains.**
7. **L2-S36: the sentence of tractability Ruling 1 (iii) written beside the statement, not into its bold text**
   (§L.12 item 2). The record calls it a "Proposed addition to L2-S36" and, unlike the fit ruling, does not say the
   statement "is to be amended". Beside the statement or inside it, it says the same thing and changes nothing L2
   computes. **It stands as written.**
8. **No sub-line under OQ-L2-12 pointing at the cue item** (§L.38 item 4). The cue item conditions two of the three
   cues on OQ-L2-12's measurement. OQ-L2-12 is an open question in §4, not a statement of this face. **Routed to the
   ninth surface** (§0 terms with §4).
9. **L2-S38's amended bold text no longer says "on held-out folds, with its capacity budget declared in advance"**
   (§L.11 item 1, noted with a ★). The replacement is the ruling's own wording, and the ruling says "Every other
   sentence of L2-S38 stands." What the dropped words required still binds: principle #20 (held-out data and a
   capacity budget declared before any fit) governs every fit whatever a statement's bold text says, fit Ruling 1
   names D-271's budget, and L2-S38's own Defense cites #20 and its Falsifier tests that evaluation data do not overlap
   fit data. **No requirement is lost, and nothing is written.**
10. **L2-S39: the §1d bound beside L2-S39, and Row 48.6's research question left in its row's line** (§L.39 items 4
    and 6). The bound is on what enters under L2-S39, so it sits there. Row 48.6's question — whether a published
    learned form would infer better where a term's form now comes from theory — is a plan item of the research
    iteration of 2026-10-07, and the record says it is "not written into L2 now". The shape you ratified for the
    voicing-and-doubling item in face (e) applies: the record is its home. **Both stand**; Row 48.6 is carried in §5.

**Found by this side, not noted by the dispatch:**

11. **The paper sizing's result and your word on it are not in the successor.** The tractability record's route (shown
    under OQ-L2-8) says that after the sizing, if exact search is not clearly affordable, "which dials D-202's ambition
    setting gets, and their defaults, come to the user with the sizes, before this layer's specification is
    ratified". The sizing, dated 2026-10-05, found that it "cannot tell whether exact search is affordable
    at D-201's sizes" (its §8). Your word on it, recorded verbatim at its §C, ends: "So, as long as we build the
    software so that there are clear and easy "entry points" where we could apply/adhere to an "effort"-setting, I an
    not worried that we actually have not measured the response times. Continue." The sizing records what that
    settles: "no code trial and no timing measurement is owed before L2's specification is ratified. What is owed
    instead is that **the specification names clear entry points where an effort setting applies**", the dials and
    their defaults being decided "when the effort setting is built and measured (D-202 stays DEFERRED), not before
    ratification" — recorded there "as following from the record and his word, not as a new ruling". **So the
    dials question does not stand in the way of ratifying this face; your recorded word answers it.**
    What is owed — the entry points named in the specification — is not yet written. It is correction 4.
12. **L2-S34's Source class still speaks of "the two" tonal spaces.** It reads: "The distances are *given* by
    published theory (THEORY: Lerdahl's tonal pitch space; Weber's table). **Which of the two is used, and the weights,
    are *measured*, UNESTABLISHED.**" The comparison now holds four candidates: tonality and progression terms Ruling 3
    added circle-of-fifths distance with a relative major/minor term, and published theory Ruling 2 added a counted
    table, both quoted under OQ-L2-3. Out-of-date wording is brought into line without asking you (your rule of
    2026-09-22), in the pointer form you accepted in face (c). It is correction 3.

## 4. What needs writing — documentation only; the droppable parts are marked

None of these changes the algorithm. The applying dispatch would write them, keeping every former wording in place
(#12).

- **Correction 1 — one recorded line per "wording does not change" ruling not shown**, quoting it and citing the
  record (the ground of face (a)'s C5, as the later faces applied it):
  - beside L2-S31, score decomposition Rulings 1 and 3: "L2-S31's wording does not change." (one line for both
    rulings; Rulings 2 and 4 place rows only);
  - beside L2-S32, span content term Ruling 1: "Algorithm: unchanged. L2-S32's wording does not change.";
  - beside L2-S33, crossing elaborations Ruling 1: "Algorithm: unchanged. L2-S33's wording does not change.";
  - beside L2-S37, cadence cues Ruling 1: "Algorithm: unchanged. L2-S37's wording does not change.";
  - beside L2-S39, published theory terms Ruling 1: "Algorithm: unchanged. L2-S39's wording does not change."
  - **Not for L2-S34** (its recorded "stands as derived" sub-item already shows the record), **L2-S36** (its ruled
    sub-item already shows Ruling 1), **L2-S38** (amended, the amendment shown), **L2-S35** (no ruling on its wording).
- **Correction 2 — pointers, nothing quoted twice (#6):**
  - beside L2-S33, a pointer to the notated-boundary-flag item under OQ-L2-3 (successor lines 2026–2031: "whether a
    notated boundary flag, with its scope, at a boundary is a term on the elaborations that cross that boundary (in the
    pair term of L2-S33)"). Routed here by face (b), whose surface gave the reason: "If that measurement pays, the
    change lands in L2-S33's pair term". (Face (b)'s surface and ruling record sent it to face (d) by a slip; face (d)'s
    record corrected the routing to this face.)
  - beside L2-S39, a pointer to the bass-scale-degree item under OQ-L2-3 (lines 2032–2043), which says a published form
    of the Rule of the Octave would enter "under L2-S39". Routed here by face (e).
  - **Proposed with them, droppable (§3 point 2):** beside L2-S32, a pointer to score-decomposition Ruling 3's recorded
    observation beside L2-S31.
- **Correction 3 — L2-S34's Source class**, the field not edited, one line beside it: "The comparison of tonal spaces
  now holds four candidates: two added by the tonality-and-progression record's Ruling 3 (2026-10-06) and the
  published-theory record's Ruling 2 (2026-10-09), both quoted beneath OQ-L2-3 in §4. The derived wording stands."
- **Correction 4 — beside L2-S36, the sizing's result and your word on it**, as one recorded sub-item headed
  *"Recorded (ratification_surfaces/cowork_l2_search_sizing_2026_10_05.md, §8 and §C) — recorded as following from the
  record and the user's word, not as a ruling"*, quoting:
  - (a) §8's first sentence: "The sizing cannot tell whether exact search is affordable at D-201's sizes."
  - (b) §C's paragraph *"What it settles."* whole (from "§8's outcome" through "his word moves it to the build.").
  - (c) §C's paragraph *"The entry points this sizing locates"* whole, under its own words "*my reading*, a proposal
    for the application act, not ruled": (a) the admitted chord vocabulary — which chords may be applied and how deep,
    and later the allowed modes under the modal increment, following a style setting as you described; (b) which terms
    and algorithms run — for instance the crossing-elaboration link, or a table-only chord reading at the lowest
    setting, as your example; (c) the context extension's limit (D-261, under D-624's cap); (d) a stretch-length cap;
    (e) any reduction of the readings kept. "Each is a setting the user turns, so none is the "quiet" reduction Ruling 1
    (iv) of the tractability record bars. **The top setting is exact, as L2-S36 states.**" **Writing (c) is how the
    specification comes to name its entry points, as §C says is owed; the list is the sizing's proposal, and ratifying
    with correction 4 takes it in as written.** You may keep (a) and (b) and drop (c); then what §C says is owed stays
    owed.
  - **Proposed with it, droppable:** (d) from the sizing's §5 *"Limit 1 — masses"* paragraph, marked as it marks
    itself (*my reading*, UNSETTLED), the sentences from "A safe bound" to its end, the paragraph cited so that its
    "second speed-up above" (a provably safe bound) is read at its source: "A safe bound protects the principal reading, not the masses: a reading dropped
    because it cannot win still carried some mass. The derivation's falsifier for L2-S36 excuses only readings of zero
    mass. So the second speed-up above may be available for the principal reading and not for the rivals' masses. This
    bears on OQ-L2-8 and L2-S35; it is recorded, not decided." It names a tension between L2-S36's safe bound and
    L2-S35's whole-reading weights that whoever designs the search should meet at the statement. Including it is this
    side's proposal.
- **Considered and not proposed:**
  - L2-S36's Premise ends "neither is true for large scores. The user then rules between a narrower admission rule
    (L2-S2's ceiling cost) and a relaxation of the no-discarding rule." After your word at the sizing's §C, you rule
    those dials when the effort setting is built; the sentence still says you rule, and is true. Nothing is written.
  - The any-boundary-set item under OQ-L2-3 (an explicit stretch-length term, measured) says "L2-S7's and L2-S31's
    wordings are unchanged". If it ever pays, the term reads one stretch, which L2-S31's form already allows, so it does
    not change L2-S31; L2-S7 already points at it. No pointer beside L2-S31.
- **Routed to the ninth surface (§0 terms with §4), not written now:**
  - OQ-L2-8's sub-line still says the dials come to you "before this layer's specification is ratified". The ninth
    surface brings OQ-L2-8 up to date, pointing at correction 4.
  - A sub-line under OQ-L2-12 pointing at the cue item under OQ-L2-3 (§3 point 8).
  - OQ-L2-3's heading (which lists L2-S7, S12, S17, S20 and S34) does not list L2-S32, S33, S37 or S39, whose items now
    stand under it — the same question face (b) sent there.

## 5. Left open by this face's rulings — carried, not decided by ratifying

- **DP-O, the charter's** — whether L2 needs terms longer than neighbouring pairs, or a hierarchy. The note beside
  L2-S31 asks that, when DP-O is taken up, the measurement compare pairs, longer flat terms and a hierarchy on the same
  ground truth; named candidates are a longer chord memory, a cadential-formula term, the sequence term (carried under
  L2-S49) and harmonic rhythm. Beside it, score decomposition Ruling 1's named remedy: a piece-level tonality term, with
  D-616's proof obligation, if L2 is found losing a key against its relative over whole passages.
- **OQ-L2-3's held-out measurements that bear on this face:** the content-split arm (L2-S32); the elaboration-naming
  item (L2-S33); the notated-flag item on crossing elaborations (L2-S33); the tonal-space comparison with four
  candidates and the separate entry term (L2-S34, L2-S39); the cue term (L2-S37); the bass-scale-degree prior (L2-S39,
  with L2-S3 and L2-S28); the stretch-length form (L2-S7, read with L2-S31). Each keeps its "measurement precedes any
  build" wording.
- **OQ-L2-8, the tractability of the search.** The sizing could not tell; three unknowns decide it (how many applied
  chords the vocabulary carries, OQ-L2-1; two speed-ups that cannot be sized without the fitted form; a time budget,
  not found). The dials and their defaults are decided at the effort setting's build (D-202 stays DEFERRED). The
  sizing's Limit 1 (masses under a safe bound) is unsettled (correction 4 (d) proposes writing it beside L2-S36).
- **OQ-L2-12** — the cue window; until it is measured two of the three cues carry no load.
- **OQ-L2-13** — no annotated collection marks chord tones and elaborations note by note independently of the chord
  labels; until one is found, they are learned and graded through the chord labels (fit Ruling 3).
- **Fit Ruling 1's three UNSETTLED items**, shown beside L2-S38: which licence class the chorale analyses fall in;
  what exactly the graded measure is; whether the all-weights-one counted model stays a mandatory comparison arm.
- **The primaries of Lerdahl and Weber are not held**, nor a source for the Rule of the Octave; a published space or
  profile needs its primary fetched and read before its constants carry load (the §1d bound).
- **The forms rule beside L2-S39 was not checked term by term** against the present terms; the record names the
  research iteration as where that would be. **Row 48.6's question** (would a published learned form infer better) is
  carried to the same iteration; "L2 states no rule on learned terms" until then.
- **Rows held for the effort setting's own design** — Rows 43.12 and 7.104(i), held by the tractability record for
  the dials question, which the sizing's §C reads (not ruled) as travelling with D-202's design; and Row 45.55, which
  the context-at-the-edge record ruled "not placed now, travelling with the effort setting's design (D-202)" (both
  relayed from the dispatch, lines 1230–1232 and 3565–3567).

## 6. What the rulings of this face leave owed at the ratification act, outside the successor

- **D-616 and D-330** — score decomposition Rulings 1 and 3: each "settled at the ratification act, not here".
- **D-449, D-534 and D-329** — rows on these WITHHELD statements placed by span content term Ruling 1; **D-527** — Ruling
  2. Each "settled at the ratification act, not here".
- **D-527 and the notation increment's Decision 4** — crossing elaborations Ruling 2, which face (d) also carried.
- **D-341, D-337, D-347 and D-348** — tonality and progression terms Rulings 1 to 3. D-337 is also among face (c)'s
  carried items.
- **D-339 and D-509** — weight meaning Ruling 3. The same record's other register items (D-267, D-425, D-380, D-381,
  D-349) belong with L2-S40 and L2-S42, face (g); which statement Ruling 4's rows sit under was not checked here.
- **D-336, D-521 and D-605** — cadence cues Ruling 1; D-336 and D-605 again under Ruling 2. D-605 is also among face
  (c)'s carried items.
- **D-383** — fit Ruling 2, "settled at the ratification act". **D-525** — fit Ruling 1: "D-525's register status is
  not changed here", the suspension file being the route.
- **D-001, D-096 and D-531** — published theory terms Ruling 3.
- **Nothing for the tractability record**: it "amends no framework text and no register entry".
- **The charter's DP-P** — fit Ruling 1 says "DP-P is answered for L2's detail specification by this ruling"; no
  framework text is ordered amended (the dispatch: "no framework text is amended"). Nothing more is owed here.

The register cannot take an entry while `cowork_register_rule_c_suspension_2026_08_28.md` is the standing route, as
the earlier face records state; that file was not opened this sitting. **So these wait on that route**, recorded and
not lost.

## 7. The decision, and what it does

**One decision: do you ratify face (f) — L2-S31 to L2-S39 as written in the successor, with corrections 1 to 4
written by the applying dispatch (with or without the pointer beside L2-S32, the entry-point list (c) and the Limit-1
paragraph (d)), the items of §4 routed to the ninth surface, the open points of §5 carried as open, and the register
items of §6 carried to that dispatch?**

- **Documentation:** it marks the nine statements ratified; writes five recorded lines, two or three pointers, one line
  beside L2-S34's Source class and one recorded sub-item beside L2-S36, every former wording kept; and lists the
  register items for the applying dispatch.
- **Algorithm:** **nothing changes by this act.** Two rulings of this face changed what the specification says about
  L2's method, both decided earlier and both already written: fit Ruling 1 (L2-S38's second sentence — tables counted
  once and frozen, the combination weights fitted to the graded measure, a likelihood fit at most its starting point) and
  published theory Ruling 3 (the forms rule beside L2-S39). Ratifying confirms them as written. The other rulings of the
  face confirm their statements, place rows, add held-out measurements, or record what has no site in L2. Correction 4 names where an effort setting
  would act; at the top setting the search stays exact, and nothing below the top is decided (D-202 stays DEFERRED).

**The currently decided method for face (f), in plain words.** L2 gives each candidate reading of the loaded music one
number, the sum of terms over each stretch and over each pair of neighbouring stretches; how long a stretch lasts is
part of the reading. The stretch terms rate how the stretch's notes, each with its role, fit the spelled chord —
counting notes that sound but do not belong and chord members that do not sound, a missing member being a cost and
never a bar. Where a suspension, anticipation or other elaboration reaches across a boundary, the term reads the
neighbouring stretch's candidate chord, not a guess at it. Across stretches, a change of tonality costs according to
the distance between the two tonalities in a tonal space (which measure of distance is a held-out
measurement among four candidates); each chord is costed against its tonality; and each pair of neighbouring chords is rated as degrees in
their own tonalities, which is how a cadence confirms a key — no term rewards a root merely continuing. The weights of
all readings together sum to one, so later music can change how much weight flows to an earlier choice. The search
weighs every reading it has begun to the end of the loaded music, or drops one only on proof that it could not win;
no beam. Of L1's cadence cues, only the leading-tone cue may be read by a fitted term, and on the cadence record's reading of the derivation no
term reads a cue now; whether one should is measured. Every weight is learned: tables counted once from freely licensed annotated music and
frozen, a short list of combination weights fitted on held-out music to the graded measure, every analyst variant
accepted. A published distance or profile keeps its published numbers and gets one learned weight, and every term's
form comes from established theory or published research before any number is attached. **Still open:** DP-O; the
held-out measurements of §5; whether exact search is affordable at the largest sizes (OQ-L2-8), with the dials decided
at the effort setting's build; the cue window (OQ-L2-12); note-level ground truth (OQ-L2-13); the weights' values.

## 8. Recommendation: ratify, with corrections 1 to 4, including the pointer beside L2-S32 and parts (c) and (d) of correction 4

- **Towards the ultimate objective (maximum-precision inference, #4):** the audit will measure the code against this
  text. Five statements carry a ruling the text does not show, and two open measurements that bear on L2-S33 and
  L2-S39 are not pointed at from them; the lines and pointers close that gap and change nothing L2 computes. Correction
  4 puts the sizing's result, the place where the dials were moved, and the named entry points beside the statement a
  search designer reads; part (d) warns that a safe bound may protect the winner and not the rivals' weights, a
  difference that, on this side's reading, bears on what L3 and the display receive.
- **Towards the guiding principles:** #10 (the specification true and complete about itself); #6 (one line and a
  citation, never a second copy); #12 (every former wording kept); D-599 (nothing here is put as a choice the record
  settles); D-035 and D-202 (cost-driving choices are settings, the dials decided at the build); your 2026-09-22 rule on
  out-of-date wording (correction 3); the ground of face (a)'s C5 and C6 and the earlier faces' corrections applied the
  same way; #24 for part (d) (a condition that cannot be established is declared as a bound).
- **Meta level:** documentation of the analysis's own specification; no measurement tool, no governance rule.

## 9. Bounds of this surface

Not read this sitting: `FRAMEWORK.md` (the charter's L2 list, DP-C, DP-O, DP-P), the input contract (S-45 to S-48,
S-52), the ten family records' surfaces, the ledger entries the Defenses cite (C2, C16, C29, C41, C45), the papers the
Defenses relay (Masada & Bunescu; Yang, Cwitkowitz & Duan 2023; Lafferty, McCallum & Pereira; Rocher et al. 2010;
Catteau, Martens & Leman; Feisthauer et al. 2020; Och; Raphael & Stoddard 2003; McLeod & Rohrmeier 2021; Ju et al.
2017), the decisions-register group files, the comparison reading file and its rows, `cowork_confidence_contract.md`,
and the register's rule (c) suspension file. Every claim about them above is relayed from the records, the successor,
the dispatch or the sizing. The dispatch's row-by-row placements were checked by the writing side at the time and were
not re-checked here; this surface is about the statements. Of the dispatch's 359 places naming one of the nine
statements, those named in §1 were read.

## 10. The check of this surface — run in its own turn, after delivery, at the sources

Checked for completeness, coherence, correctness and absolutes, each claim against the object it rests on (the staged
copies of the records, the successor, the dispatch, the sizing and the earlier surfaces). **Seventeen corrections, made
at their sites above. None moves a finding, a proposed correction, the algorithm statement or the recommendation.
Former wordings, preserved (#12):**

1. §0: **a correction of fact.** Face (f) is not the largest face by statement count: face (a) has ten statements, face
   (f) nine. The claim was relayed from entry 385 §1 and not checked; it is corrected here, not at entry 385's site.
   Former: *"is the sixth face and the largest:"*.
2. §1: the three rulings were not found by the method the paragraph describes but by reading OQ-L2-3 whole, and the
   two records' sentences were quoted shorter than they stand. Former: *"Three that bear on this face were found that
   way and are named where they bear: the any-boundary-set and notated-boundary-evidence records of 2026-10-07, whose
   OQ-L2-3 items say "L2-S31's wording" and "L2-S33's wording" are unchanged;"*.
3. §2, L2-S31: the score-decomposition record does not call its rulings "documentation only". Former: *"rows placed,
   documentation only;"*.
4. §2, L2-S35: the sentence on how much weight flows into a branch is the derivation's own, not Lafferty, McCallum &
   Pereira's. Former: *"a stretch's rivals "compete only against each other", and later evidence cannot change how
   much weight flows into a branch (Lafferty, McCallum & Pereira, relayed);"*.
5. §3 opening: three droppable parts, not two. Former: *"except the two parts of §4 marked as this side's proposals,
   which you may drop."*
6. §3 point 3: the pointer beside L2-S49 was not read in the successor; marked as relayed. Former: *"that face (h) will
   meet. **It stands.**"*
7. §3 point 6: a ruling quoted short. Former: *"are amended". **Nothing remains.**"*
8. §3 point 9: **an absolute.** Former: *"**Nothing is lost, and nothing is written.**"*
9. §3 point 11: the sizing's date is its title's; when it was written was not checked. Former: *"The sizing was written
   on 2026-10-05 and found"*.
10. §3 point 11: §C's own standing ("not as a new ruling") was left out, and "the record answers it" claimed more than
    a recorded word. Former: *"ratification". **So the dials question does not stand in the way of ratifying this
    face; the record answers it.**"*
11. §4 heading: it contradicted the droppable parts below it. Former: *"documentation only, none of it a choice"*.
12. §4, correction 4 (d): it said "paragraph whole" and quoted part of it; the quoted "second speed-up above" needs its
    source. Former: *"(d) the sizing's §5 *"Limit 1 — masses"* paragraph whole, marked as it marks itself (*my
    reading*, UNSETTLED):"*.
13. §5, held rows: Row 45.55 is held by a ruling of the context-at-the-edge record, not by the sizing's reading. Former:
    *"Rows 43.12 and 7.104(i) (the tractability record) and Row 45.55 (the context-at-the-edge record), which the
    sizing's §C reads as travelling with D-202"*.
14. §7: fit Ruling 1 keeps a likelihood fit as a possible starting point, so "rather than by likelihood" overstated it;
    and the other rulings' kinds were listed short. Former: *"to the graded measure rather than by likelihood)"*; *"The
    other rulings of the face say the algorithm is unchanged, or that the statement stands, or place rows."*
15. §7 method: one of the four candidates (the counted table) is not a published space. Former: *"(which space is a
    held-out measurement among four candidates)"*.
16. §7 method: "no term reads a cue now" is the cadence record's reading of the derivation, marked so there. Former:
    *"and no term reads a cue now;"*.
17. §8: "may change" said more than the bass-scale-degree item says of L2-S39, and the closing clause was this side's
    reading unmarked. Former: *"two open measurements that may change L2-S33 and L2-S39"*; *"a difference that bears on
    what L3 and the display receive."*

**Checked and standing:** every quotation in §2 to §6 against its record — score decomposition Rulings 1 to 4 and its
arithmetic; nothing from L3, Rulings 1, 4 and the DP-O note; span content term Rulings 1 and 2; crossing elaborations
Rulings 1 and 2 and §0; tonality and progression terms Rulings 1 to 5 and §1f; weight meaning Rulings 1 and 3 and §1e;
tractability Ruling 1, §1b and §2; cadence cues Rulings 1 and 2; fit Rulings 1 to 3 and §2; published theory terms
Rulings 1 to 3 and §1d; the sizing's §8, §5 and §C; the face (a) surface's C6 ground (its line 146); the face (b) surface
at lines 145–146; the face (c), (d) and (e) records' carried items. §2's account of what the successor shows, at lines
1172–1525, 1995–2081, 2106–2120 and 2147–2164. §3's dispatch citations at the lines §1 names. §6's register items, each
against the words of its record. **Absolutes swept** ("all", "every", "never", "nothing", "none", "only", "exactly",
"always", "whole", "largest"): each remaining hit is a statement's or ruling's own wording, a quotation, a claim about
this sitting's reading as §1 and §9 bound it, or a claim checked at its object above.

**What the check did not do:** it re-opened nothing §9 lists as unread, did not read the successor beside L2-S49 (the
DP-O pointer, now marked relayed), and did not read the dispatch's other places naming the nine statements.

*Provenance: Cowork, 2026-10-13 (Stockholm), the sitting booted on entry 385. The user's words this sitting: the
opening instruction; "continue" (the check).*

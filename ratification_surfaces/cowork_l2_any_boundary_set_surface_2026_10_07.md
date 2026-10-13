# Where one chord may end — L2-S7 — ratification surface, 2026-10-07

> **STATUS: RATIFICATION SURFACE, §A AND ITS CHECK §B.** *(Former wording, preserved (#12): "§A ONLY".)* Cowork, 2026-10-07 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_fourteen.md`. Written as text, nothing asked in
> the turn that delivers it. The check (§B) comes in a later turn, and the questions after that, one per turn.
> Nothing here is applied, and no tracked document is edited. Marks: *checked* = read at the object by this
> sitting; *relayed* = taken from another record and not re-read here; *my reading* = this side's
> interpretation.

---

## §A.1 The statement, whole, and what it means

From `cowork_blind_derivation_l2_2026_09_27.md`, its lines 245–266 (*checked*):

> **L2-S7. Any subset of L1's change points may be the boundary set of a reading. No regularity of
> harmonic rhythm or segment length is an admission rule. Each such regularity is a term of the
> candidate score. If a maximum span length is imposed for tractability, it is an admission rule, it
> carries L2-S2's ceiling statement, and it is set no shorter than the longest span any annotation of
> the grading repertoire writes.**
> - *Defense.* The charter makes boundaries a subset of change points and nothing more [RULED — charter].
>   It also says why a stylistic regularity must not be a rule: a hard constraint "lets one wrong answer
>   delete the other question's right one" [RULED — charter, L2]. The published enumerate-then-filter
>   system took "harmonic rhythm cannot be syncopated" as a hard rule and records its own exceptions in
>   one of its two corpora, describing its rules as "'over fit' to chorale music" [FACT (relayed, 08) —
>   Condit-Schultz, Ju & Fujinaga, §3]. The published semi-Markov systems bound segment length for cost.
>   One states its bound only as a symbol L, and the other states none and reports quadratic cost [FACT
>   (relayed, 08) — Masada & Bunescu, p. 3; Yang, Cwitkowitz & Duan 2023, §6]. A bound shorter than a real
>   prolongation would make that prolongation unreachable.
> - *Source class.* Derived.
> - *Status.* Settled. The bound's value, if any, is *measured* (OQ-L2-3).
> - *Premise.* The joint search stays tractable without a tight length bound (see L2-S36).
>   **False-negative path:** a tractability failure that forces a bound shorter than a real span. It is
>   visible as a closure-test failure and must be ruled, not silently set.
> - *Falsifier.* CODE. **Observable:** the boundary sets reachable for a given slice list. **Decision
>   rule:** falsified if some subset of change points is unreachable other than through a declared
>   maximum span length. **Not falsified by:** a subset reachable and scored low.

**In plain words.** A *change point* is a moment where some note starts or stops (L1 publishes them). A
*reading* is one complete answer for the music loaded: where each chord begins and ends, the tonality and
the chord over each stretch, and which notes are chord notes. L2-S7 says:

1. A chord may begin at **any** change point and last to **any** later one. No pattern of how often chords
   change (the *harmonic rhythm* — for example "chords change on strong beats", "a chord lasts at least a
   beat", "harmonic rhythm is never syncopated") is allowed to forbid a reading.
2. Such patterns are still used — but as **costs and rewards in the candidate score** (the number that ranks
   readings), never as walls.
3. The **one** exception allowed: if the search turns out too expensive, a **maximum length of one chord's
   stretch** may be imposed. Then it is openly a wall, it must be ruled, its cost to the ceiling must be
   stated the way L2-S2 states every exclusion, and it may be no shorter than the longest chord stretch any
   published analysis of the graded music writes.

L2-S2, which the third point leans on, says (its lines 130–134, *checked*): "Every reading a published analysis
writes for a passage of the grading repertoire must be admissible … A reading type that some analyst writes and
the rule does not admit is excluded only by a named ruling that carries the ceiling cost it imposes."

## §A.2 What the record has already said about L2-S7

- **Used as a ground, not ruled.** Applied-or-new-tonality Ruling 1 of 2026-10-07 named L2-S7 among its grounds
  towards the principles (that record's line 48, *checked*; its surface quotes "Each such regularity is a term
  of the candidate score", line 185, *checked*). No record of 2026-10-04 to 2026-10-07 rules L2-S7 itself
  (searched, §A.4).
- **The sizing.** The paper sizing of 2026-10-05 says no value of the maximum stretch length is on the record,
  that L2-S7 "permits a bound only by ruling", and (*my reading* there, *relayed* here) that the length bound is
  not what drives cost unless the longest stretch exceeds about 1,400 change points (its lines 80–93,
  *checked*). It lists "a cap on stretch length" among possible dials, recommends none (its line 262,
  *checked*). **One mark there is wrong** — see §A.6.
- **The tractability record of 2026-10-05**, §1b, names L2-S7's stretch length as the second of the six cost
  drivers, and routes the question of dials to the user after the sizing (lines 84–109, *checked*). Nothing
  there decides whether a cap is imposed.
- **The DP-O note** (nothing-from-L3 record of 2026-10-07, Ruling 4, lines 103–104 and 163–166, *checked*) added
  "harmonic rhythm — whether a reading's chord changes speed up towards a likely cadence, rated per competing
  reading inside L2" as a candidate longer-span term to measure. That is a different regularity from a chord's
  own length (§A.5).

## §A.3 The rows — five named by §7, two taken in on their subject

§7 of `ratification_surfaces/cowork_comparison_l2_reading.md` lists for L2-S7 (its lines 71079–71082,
*checked*): **AGREES (3):** Rows 10.32(i), 22.76(ii), 48.12. **DIFFERS (2):** Rows 5.137, 30.16(ii). Each row was
read whole at the comparison file (*checked*). The outgoing texts, as the comparison quotes them:

**Row 5.137** (member 5, `cowork_layer5_function_design.md`, the Step-4 build remark, the comparison's lines
5899–5916). "Two realisations on record: the **persistence hysteresis is layered on the detector's committed
spans**, keeping the detector's **minimum-chords establishment floor** as a **candidate pre-filter** … with the
fixed floor a conservative pre-filter only; **Step-M check:** measure whether that floor ever rejects a real short
modulation the hysteresis would have admitted." DIFFERS: L2-S7 says "No regularity of harmonic rhythm or segment
length is an admission rule." **Proposed: QUARANTINED**, audit question: "does the dormant detector's
minimum-chords floor exist as a pre-filter, and does it ever reject a real short modulation?"
In plain words: the old key-change detector would not consider a new key at all unless it lasted some minimum
number of chords. That is a length rule used as a wall, which L2-S7 forbids; and the text describes what was
built, so it goes to the audit.

**Row 10.32** (member 10, `cowork_joint_estimator_factorization.md`, §3 item 7, the comparison's lines
22650–22658). "Segment duration is otherwise implicit-geometric with a hard length cap (the established
semi-Markov default; an explicit harmonic-rhythm duration model is recorded as CONJECTURE-gated future work)."
Two claims: **(i)** segment duration carries no term of its own beyond a hard length cap — AGREES with L2-S7's
"If a maximum span length is imposed for tractability, it is an admission rule"; **proposed: ADOPTED — carried
(L2-S7).** **(ii)** an explicit duration model is recorded future work — the derivation is silent; **proposed:
HISTORICAL.**
In plain words: in the old design, how long a chord lasts was not scored by itself; the only length-related
costs came from the cost of each change of chord (so many short chords cost more than one long one — that is
what "implicit-geometric" means, *my reading* *(§B item 1)*), plus a hard cap. An explicit model of typical chord lengths was written down
as a guess to try later.

**Row 22.76** (member 22, `ARCHITECTURE.md` §3, Layer 2, the comparison's lines 31899–31916). "Boundaries are
**necessary but not sufficient** for a chord change (the exhaustive candidate grid): a real chord change can never
be missed (over-grab is structurally impossible), and the slicer never asserts a change — layer 3 decides which
boundaries are real, layer N groups equal analyses." Claim **(ii)**, "the slicer asserts no change, and the reading
decides which change points are real boundaries", AGREES with L2-S7's first sentence. **Proposed: ADOPTED —
carried (L2-S7).** (Claims (i) and (iii) belong to L2-S11 and L2-S14.)

**Row 30.16** (member 30, `ARCHITECTURE.md` §11.5, *Intonation*, the comparison's lines 42962–42977). "In the
default smoothed mode, consecutive boundaries that produce the **same root and quality** are collapsed into a
single harmonic region, and sub-quarter-note fragments are absorbed so tuning and other range operations do not
overreact to ornaments." Claim **(ii)**, fragments shorter than a quarter note are absorbed, DIFFERS: L2-S7 says
"No regularity of harmonic rhythm or segment length is an admission rule." **Proposed: QUARANTINED, travelling
with Row 23.315** (the harmonic-rhythm component's smoothed default, itself QUARANTINED travelling with Row 20.4,
whose audit question is "does the harmonic-rhythm component run on any production path at the current commit,
and does it decide where one harmony gives way to the next apart from the chord?", the comparison's lines
37746–37756 and 28984–28994, *checked*).
In plain words: an old component that feeds the tuning feature throws away chord stretches shorter than a
quarter note. That describes a component's behaviour, so it goes to the audit. (*My reading:* it is a view made
for the intonation feature, not L2's decision; whether it ever decides anything L2 decides is exactly Row 20.4's
audit question.)

**Row 48.12** (member 48, `cowork_joint_estimator_architecture.md`, §2 *The factor roster*, the comparison's
lines 63418–63426). "**harmonic rhythm + boundary strength** → the segmentation (semi-Markov segment-duration)
model;" AGREES: a regularity of harmonic rhythm or segment length is "a term of the candidate score". **Proposed:
ADOPTED — carried (L2-S7).**

**Taken in on its subject — Row 17.10 claim (iv)** (member 17, `ARCHITECTURE.md`'s opening block, the as-built
paragraph, the comparison's lines 27417–27437, *checked*): "seg_cap 4". The comparison names no statement ("None —
L2-S7 states the condition any cap must meet and gives no value"), verdict THE DERIVATION IS SILENT. **Proposed:
QUARANTINED**, audit question: "what does the shipped segment cap count, and is it no shorter than the longest
span any annotation of the grading repertoire writes?" The audit question is L2-S7's own last clause, and no
other family reaches the row: the tonality-vocabulary record of 2026-10-04 says it decides nothing about "the
segment cap (17.10(iv))" (its line 231, *checked*). This side takes it into this family; the user may send it
elsewhere. Its other claims: (i) QUARANTINED by tonality-vocabulary Ruling 2 (that record's line 190); (iii)
carried under L2-S31 by score-decomposition Ruling 4 of 2026-10-07 (that record's lines 95–96); (ii), proposed
carried under L2-S27, is placed by no record searched (*checked*) *(§B item 2)*. *(Former wording, preserved
(#12): "Its other claims are placed elsewhere ((i) by tonality-vocabulary Ruling 2; (ii) and (iii) not
re-checked here).")*

## §A.4 The search for rows already placed

The 26 ruling records of 2026-10-04 to 2026-10-07 *(§B item 3; former wording, preserved (#12): "The 25 ruling
records")* and the 24 `cowork_l2_*` surfaces plus the sizing were searched
for "L2-S7", "OQ-L2-3", the six row numbers above, 23.315, "Row 20.4", "span length", "segment length", "length
bound", "length cap" and "seg_cap" (*checked*). **No hit places any of the seven row-parts of §A.3** *(§B item 4;
former wording, preserved (#12): "any of the six row-parts")*. The hits were: L2-S7 as
a ground (§A.2); the sizing and tractability lines in §A.2; OQ-L2-3 additions by other families (tonality
evidence, tonality-and-progression terms, key-signature prior, score decomposition) — none about span length;
17.10's other claims (§A.3); and Row 22.76 claim (i) in the one-decision surface's list (L2-S11's half, not this
family's). L2-S7 itself is ruled in none of them.

## §A.5 What this side found when reading the rows against each other

**Rows 48.12 and 10.32 are the same plan at two stages, and they disagree on one point.** Row 48.12 (the
architecture document) sends harmonic rhythm to "the semi-Markov **segment-duration** model". Row 10.32 (the
factorization, which details that design) says segment duration is "implicit-geometric" — no length term of its
own — and records an explicit duration model only as a conjecture for later. Both are proposed "carried" under
L2-S7.

**And L2-S7 on this point.** Its sentence "Each such regularity is a term of the candidate score" says such a
regularity is scored, not walled. It does not say which regularities L2 scores. Read against the other
statements (*checked*): L2-S12 scores the **metric strength** of the change point where a boundary falls ("The
metric strength class of a change point enters the candidate score as a term on reading a boundary there", its
lines 348–350) — that is the "chords change on strong beats" regularity. L2-S31 lets a span term read "the span's
position" and makes "span length … a variable of the reading" (its lines 776–780), so a term on a chord's length
is **allowed** by the form. **But no statement names a term on how long a chord lasts** (a search of the
derivation for "duration", "span length", "harmonic rhythm" and "semi-Markov", every hit read at its line: the
hits are duration-weighted evidence inside a span — the tonality falsifier at L2-S20, L2-S28's bass term,
L2-S32's content term — L2-S25's "no duration cut" for assignments, L2-S36's cost statement, and L2-S7 and L2-S31
themselves; a term worded otherwise would not be found by it) *(§B item 8)*, and OQ-L2-3's list of
measured shapes (its lines 1210–1213) names "the maximum span length if any" and no length term.** So as derived,
L2 has no explicit chord-length term; the length of a stretch is priced only through the terms at its two
boundaries — exactly the "implicit-geometric" form of Row 10.32 (i) (*my reading*).

So the question this family carries is not "is a length rule a wall?" — L2-S7 settles that it is not — but
**whether an explicit term on how long a chord lasts (a duration term) stands among L2's open measurements, or is
filed as an old conjecture.** That is §A.7's question. Nothing else in the family needs a decision.

## §A.6 One error found in another document — to be corrected as an error, not asked

The paper sizing (`ratification_surfaces/cowork_l2_search_sizing_2026_10_05.md`, its lines 82–84, *checked*)
writes that L2-S7 permits a bound only by ruling "… and that length is the measurement OQ-L2-3 (*ruled*)". Its own
tag definition (line 7) is "*ruled* = fixed by a ruling or a ratified text". **L2-S7 is a derived statement, not
ruled and not ratified**; the derivation's own tag on it is "Source class. Derived" (*checked*). The right tag is
*relayed* (taken from the derivation). Under the user's rule of 2026-09-22 (apparent errors are fixed without
asking; not a verdict, a value or a finding), this side corrects it at its site in the check turn, the former
wording kept in place (#12), and reports it. It moves nothing in the sizing's arithmetic.

## §A.7 What is proposed — two parts, kept apart

### Part 1 — Documentation only (filing the rows). One confirmation.

Six row-parts, as the comparison proposes, with nothing changed:

- **ADOPTED — carried under L2-S7 (3):** Rows 10.32 claim (i), 22.76 claim (ii), 48.12.
- **QUARANTINED (3), with their audit questions:** Row 5.137 (its own question, §A.3); Row 30.16 claim (ii)
  (travelling with Row 23.315 and through it Row 20.4, whose question is quoted in §A.3); Row 17.10 claim (iv)
  (taken in on subject; its own question, §A.3).
- **Row 10.32 claim (ii)** — its filing depends on Part 2: **HISTORICAL** as proposed if Part 2 is answered "no";
  **ADOPTED — proposed** (the proposal being Part 2's sentence) if "yes".

**Why this is a confirmation and not a choice.** Each placement follows from the vocabulary's definitions (§5 of
the comparison file, *checked*: "carried" where a derived statement already carries the content; "QUARANTINED"
where the text "states how the implementation currently works") and from L2-S7, which no row contests except two
descriptions of old components; and the route ruling sends descriptions of what was built to the audit (D-599).
**Algorithm:** nothing changes. **Arithmetic:** 3 carried + 3 quarantined + 1 depending on Part 2 = 7 row-parts:
§7's five (10.32 (i), 22.76 (ii), 48.12, 5.137, 30.16 (ii)), plus two taken in on subject — Row 10.32 claim (ii),
the other half of a row §7 lists (its verdict THE DERIVATION IS SILENT, so §7 does not count it), and Row 17.10
claim (iv).

### Part 2 — The specification's list of open measurements. One question, with its positions.

**What is being decided, in plain words.** Whether L2's specification records, as an open measurement, *whether a
term on how long a chord lasts improves the reading* — or files that idea as an old conjecture and leaves L2 as
derived (chord length priced only through the boundary terms).

**This does not change what the search computes now.** L2's algorithm as its statements define it stays as it
is (§A.8). What changes under "yes" is one line added to OQ-L2-3's list of held-out measurements; if that
measurement ever repays a duration term, adding the term to L2's candidate score would be its own ruling then.
Under "no", nothing in the specification changes, and Row 10.32 (ii) is filed HISTORICAL.

**Position A — add it to OQ-L2-3.** Proposed sentence for OQ-L2-3's list: *"the form of a chord's own length in
the candidate score: none beyond the boundary terms (the implicit form), or an explicit span-length term, and
over what unit (change points, beats, or time), compared by held-out measurement."*
- *Towards the ultimate objective (#4).* L2-S7 already says a harmonic-rhythm regularity is "a term of the
  candidate score". A chord's typical length is such a regularity; without a listed measurement, whether it
  helps is never tested, and if it does help, L2 reads worse than it could. The outgoing design itself recorded
  the explicit model as a conjecture to try (Row 10.32 (ii)), and the charter's ground for the semi-Markov form
  is "letting segment length be a decoded variable" (L2-S31's defense, quoting DP-C, *checked* at the
  derivation; `FRAMEWORK.md` not opened) *(§B item 5; former wording, preserved (#12): "and the published
  semi-Markov systems the derivation cites make segment length a decoded variable (L2-S31's defense,
  *relayed*)")*. That a length variable is decoded does not show that a length term helps; that is what the
  measurement would find.
- *Towards the guiding principles.* #5 and D-254 (investigate where facts are scarce; the fact here is
  unknown); #12 (a candidate the old design named is kept as an open question rather than filed away); #17
  (a conjecture enters only as a measured candidate, nothing built on it); #20 (any length term is fitted on
  held-out data with a capacity budget — the measurement carries that cost); Ruling 6 of the L2-S10 record of
  2026-10-07 (a change is investigated and measured, never asserted). Precedent: three rulings already added
  candidates to OQ-L2-3 on the same footing (L2-S34's Rulings 3 and 4 of 2026-10-06; tonality-evidence Ruling 4
  of 2026-10-06), and DP-O's note gained harmonic rhythm on 2026-10-07 (nothing-from-L3 Ruling 4).
- *Meta level.* The analysis's own specification (its measurement list). No governance act.
- *Cost.* One more held-out comparison in the measurement phase, and one more fitted weight if it is ever
  adopted (#20's capacity budget).

**Position B — file Row 10.32 (ii) HISTORICAL; L2 stays as derived.**
- *Towards the ultimate objective (#4).* Nothing is lost now: the form L2-S31 allows still permits a length term
  later. But no listed measurement would test it, so the question is open in fact and absent on paper.
- *Towards the guiding principles.* #6 and D-630 (do not add a component without a resolved residual — here
  nothing is added, only a measurement listed); D-200 (keep the measurement load small). Against it: #12 in
  substance (the conjecture survives only as a filed row, not as a question anyone will take up), and the
  standing bar of 2026-10-07 that no design rule may block the objective in the long run.
- *Meta level.* The analysis's own specification.
- *Cost.* None now; the risk is that a real gain is never measured.

**Recommendation: Position A.** Towards the objective, it is the position under which the regularity
L2-S7 says "is a term" is listed to be tested *(§B item 6; former wording, preserved (#12): "it is the only
position under which the regularity L2-S7 says "is a term" is ever tested")*; towards the principles, it follows #5, D-254, #12 and the precedent of
three OQ-L2-3 additions, at the cost of one held-out comparison; at the meta level it touches only the
analysis's measurement list. *My reading:* the record nearly settles this — the precedent points to A — but
whether one more measurement is worth its cost is the user's to weigh, so it is put as a question with its
alternative, not as a confirmation.

**Order of the questions** (one per turn, each recorded before the next): **first Part 1** (the six filings, with
Row 10.32 (ii) left to Part 2), **then Part 2.**

## §A.8 The method that stands — the algorithm as currently derived, unchanged by Part 1 and by either answer to Part 2

Quoted from the derivation and the records, *checked* this sitting:
- **L2-S7:** any subset of L1's change points may be the boundary set of a reading; no regularity of harmonic
  rhythm or segment length forbids a reading; each such regularity enters as a term of the candidate score; a
  maximum stretch length may be imposed only by ruling, as a declared exclusion carrying L2-S2's ceiling cost,
  no shorter than the longest stretch any analysis of the graded music writes. **No cap is imposed by L2's
  derived specification**; the sizing does not use the current program's cap of four, which has "NO recorded
  derivation anywhere in the record" (D-004, as the sizing quotes it) *(§B item 7; former wording, preserved
  (#12): "**No cap is imposed** (sizing, §A.2; the current program's cap of four is not used).")*.
- **L2-S12:** the metric strength class of the change point where a boundary falls is a term on the boundary,
  its weights fitted per class; no metric level forbids a boundary.
- **L2-S31:** the candidate score is a sum of span terms and terms on adjacent span pairs; span length is a
  variable of the reading, never a fixed grid. As derived, no term reads a chord's length by itself (§A.5).
- **L2-S36** (tractability Ruling 1): every reading begun is weighed to the end of the loaded music, or dropped
  only by a bound that provably cannot discard a possible winner; no beam.
- **L2-S2:** every reading a published analysis of the graded music writes is admissible, or excluded only by a
  named ruling that states its ceiling cost.

## §B The check at the sources (the next turn of the same sitting, before any question)

Every quotation and cited line in §A was re-read at its object in the staged copies: the derivation at L2-S2,
L2-S7, L2-S12, L2-S31, L2-S36 and OQ-L2-3; the comparison file at §7's entry and all seven row-parts with the rows
they travel with; the ruling records and surfaces cited. Row 17.10's other claims were searched for at the records
and read at their lines. The writing was swept for absolutes (no, none, nothing, every, any, only, never, all,
whole), each hit read at its line against the act that established it. The arithmetic was re-added: 3 carried +
3 quarantined + 1 depending on Part 2 = 7; §7's 3 AGREES + 2 DIFFERS = 5, plus 2 taken in = 7. **Eight findings,
all corrected at their sites; none moves a placement, the recommendation, or the claim that L2's algorithm as
derived does not change.**

1. **§A.3, an inference unmarked.** That "implicit-geometric" means chord length is priced only through the
   change-of-chord costs is this side's reading, not the source's words; now marked.
2. **§A.3 and §A.9, a check not run.** Row 17.10's claims (ii) and (iii) were left "not re-checked"; the search
   finds (iii) carried under L2-S31 by score-decomposition Ruling 4 and (ii) placed nowhere. Former wordings kept
   at their sites.
3. **§A.4, a wrong count.** The ruling records of 2026-10-04 to 2026-10-07 are 26, not 25.
4. **§A.4, a wrong count.** §A.3 has seven row-parts, not six.
5. **§A.7, a misattribution.** "Segment length a decoded variable" is the charter's DP-C ground quoted in
   L2-S31's defense, not a statement about the published systems; corrected, and the reach of the quotation
   stated (a decoded length is not evidence that a length term helps).
6. **§A.7, an absolute wider than its ground.** "The only position under which … is ever tested" — under
   Position B the idea could still be raised later; narrowed to "listed to be tested".
7. **§A.8, an ambiguous sentence.** "The current program's cap of four is not used" read as a claim about the
   program; it is the sizing that does not use it. Corrected.
8. **§A.5, a negative stated without its basis.** "No statement names a term on how long a chord lasts" now
   states the search it rests on and what that search cannot see.

**And §A.6's correction was made**: the sizing's tag at its lines 82–84 now reads *relayed*, with the date, this
surface named, and the former "(*ruled*)" kept in place. Nothing else in the sizing was changed.

**What the check did not do.** It did not open `FRAMEWORK.md`, the outgoing member documents, the register group
files, or the derivation beyond the statements named. Nothing in it was read through a shell.

## §A.9 Carried, not decided here

- **Whether any cap on a chord's stretch is ever imposed**, and its value: OQ-L2-3 (the measurement of the
  longest annotated stretch) and the dials question the tractability record routes to the user after the sizing
  (§A.2). *My reading, recorded for that question:* L2-S7's floor is "the longest span any annotation of the
  grading repertoire writes"; the scores D-201 says must be handled are larger than that repertoire, so a cap set
  at that floor could still be shorter than a real prolongation in a large score — the case L2-S7's own defense
  names. The ceiling statement L2-S7 demands is what would make that cost visible.
- Rows 23.315 and 20.4 (the harmonic-rhythm component): not placed here; Row 30.16 (ii) travels with them.
- Row 17.10's claim (ii) (L2-S27's): placed by no record searched; L2-S27's family takes it *(§B item 2;
  former wording, preserved (#12): "Row 17.10's claims (ii) and (iii): not re-checked by this sitting.")*.

## §A.10 What this sitting read

At the objects: the derivation at L2-S2, L2-S7, L2-S12, L2-S31, L2-S36 and OQ-L2-3; the comparison file at §5
(the vocabulary), §7's entry for L2-S7, Rows 5.137, 10.32, 17.10, 20.4, 22.76, 23.315, 30.16, 48.12 whole, their
neighbours 5.136, 5.138, 10.31, 10.33, 30.15, 48.11, and Rows 5.131 and OQ-L2-3's tabulation note; the ruling
records of 2026-10-04 (route, whole; tonality vocabulary, lines 222–237), 2026-10-05 (tractability, whole),
2026-10-07 (applied-or-new tonality, lines 25–54; nothing from L3, lines 98–176; the four agreeing statements,
whole); the sizing at lines 1–40, 70–109, 250–279; the applied-or-new-tonality surface at lines 178–191; the
four-agreeing-statements surface, whole. Searched, not read whole: the other records and surfaces of 2026-10-04 to
2026-10-07. **Not opened:** `FRAMEWORK.md`, the outgoing member documents behind the rows, the register group
files. Nothing was read through a shell.

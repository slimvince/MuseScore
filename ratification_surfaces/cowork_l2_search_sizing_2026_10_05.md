# How big is the search? — the paper sizing of the chord-and-key layer's search — 2026-10-05

> STATUS: SIZING ON PAPER, NOT RULED, NOT A MEASUREMENT. Written by the Cowork sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_ninety_one.md`, as the act §1b of
> `records/cowork/rulings/cowork_rulings_2026_10_05_l2_tractability_sitting.md` names. No code was written,
> no measurement was run, and nothing of the shipped program was read (phase-definition surface §3.4).
> It recommends no dial and asks nothing. Tags: *ruled* = fixed by a ruling or a ratified text, read at its
> source this sitting; *relayed* = a number taken from a record, not re-derived; *provisional* = a value
> this side declares so that the arithmetic can run, labelled as such and fit for nothing else (principle
> #17's rule for desk-simulation values, applied by analogy); *my reading* = this side's inference. Every
> result carries its uncertainty as a range (#24).

## 1. What is sized, in plain words

The layer looks at the music loaded for a selection and decides, all at once, the tonality of each
stretch, where one harmony gives way to the next, the chord over each stretch, and which notes are chord
notes and which are elaborations. One complete answer is a **reading**. The ratified rule (L2-S36,
confirmed by Ruling 1 of the tractability record) is that every reading the search has begun to weigh is
weighed to the end of the loaded music, or dropped only on proof that it could not have won.

The search the derivation describes is a *segmental* one (L2-S31): it walks through the music change point
by change point, and at each point it asks, for every possible label of a stretch ending there, which
stretch length and which preceding label give the best total. A **label** here is one tonality together
with one chord. **The unit of cost used below is one evaluation of the term linking two adjacent stretches'
labels** (a *pair evaluation*). It is a count, not a time; §6 converts it to time under a declared
assumption.

The six cost drivers are those §1b of the tractability record names. Each is sized in §3, then put
together in §4.

## 2. What the record already answers, checked before sizing (D-599)

- **No sizing of L2's search exists on the record I read.** The tractability surface says "No count of the
  search's size appears anywhere I read"; the framework's sizing record (`FRAMEWORK.md` A.7) sizes the
  writing of the framework, not the search (*checked*).
- **Real orchestral sizes do exist on the record**, beyond what entry 291 names (it names none for a Wagner act
  or a symphony, and none is found here either; see the next point). The open-item detail files
  for the empty-decode fault give event counts for committed large scores (*relayed*, `open_items/OI-215.md`
  and `OI-227.md`): Butterworth, *Banks of Green Willow*, **1,100 events**; Holst, *Mercury*, **1,743
  events**; and the 23 committed large scores together, **172,611 events**, which is about **7,500 per
  score** on average (the 23 include two pairs of duplicate uploads, Beethoven 9 and the Jupiter, as OI-215
  lists them, so the average is per committed file, not per distinct work). The unit is the current
  program's event lattice. *My reading:* that unit is closer to the derivation's change points than to
  individual notes, because the chorale figure the same documents use, "roughly 60–150 events" (Row 10.52),
  is the size a chorale's count of onset moments would have, and well below its count of notes; **neither
  count was made for any chorale this sitting.** This reading was not checked against the code and must not
  be leaned on beyond order of magnitude.
- **No event count for a Wagner act or a symphony as a whole was found** (the architecture review's
  Tristan stress case, `cowork_architecture_review_2026_07.md` §7, carries no count; *checked* by a search of
  that one file for "Tristan", "events", "slices", "bars" and "measures"; no wider search was run).
  The size of a Wagner act is therefore a **named input, N_W**, never a number invented here. Because the
  cost grows in direct proportion to the music loaded (§3.1), the result is also stated per 1,000 change
  points, so it can be multiplied by any N_W once one is established.
- **Not used:** two recorded measurements of the current program — the "10–14 s" full decode on the two
  orchestral scores (OI-215) and the window study's stopping point (OI-210's note). They describe the
  shipped engine, which has 24 tonalities, a counted chord list and a stretch cap of four, so they size a
  different search; and leaning on them would bring implementation material into this phase (§3.4). They are
  named so that their absence is not mistaken for ignorance of them.

## 3. The six drivers, one at a time

### 3.1 The music loaded

**N** = the number of change points in the loaded music — the selection plus its context (Ruling 1 (ii)).
The context is found by convergence (D-261) under a safety cap (D-624), so N is not known before the run;
its upper end, when the selection is a whole movement or act, is the whole of it.

Sizes used: a chorale, **60–150** (*relayed*, Row 10.52, an expectation); Butterworth **1,100**, Holst
*Mercury* **1,743**, the committed large-score average **≈ 7,500** (*relayed*, §2); a Wagner act, **N_W**,
unknown.

**How cost grows with N** (*my reading*, a standard rearrangement of the segmental search; no source was read
for it this sitting). The link between two stretches depends only on the two labels and on the music at
their shared boundary, not on how long either stretch is. So for each change point the best predecessor of
every label is found once, and the stretch-length choice is made afterwards. Cost then has two components:
**N × (pair evaluations per boundary)** and **N × L × S** for the stretch terms (L and S below). **Both
grow in direct proportion to N.** So the search obeys C-8 (cost grows with the working span) as long as
the stretch length has a bound; without one, see §3.2.

### 3.2 The maximum length of one chord's stretch

**L** = the longest stretch, in change points, the search considers. **No value is on the record for L2**:
L2-S7 permits a bound only by ruling, set no shorter than the longest stretch any annotation of the
grading repertoire writes, and that length is the measurement OQ-L2-3 (*relayed* from the derivation; L2-S7
is a derived statement, not ruled or ratified — corrected 2026-10-07 by the L2-S7 family's check,
`ratification_surfaces/cowork_l2_any_boundary_set_surface_2026_10_07.md` §A.6; former wording, preserved (#12):
"(*ruled*)"). The current program's cap
of four has "NO recorded derivation anywhere in the record" (D-004, *checked*) and is not used.

What can be said without a value (*my reading*, from the two components in §3.1): per change point, the
stretch component costs about L × 42 × C, and the pair component about 42 × C² (C, the number of chords per
tonality, is §3.3's). **So L is not the binding driver unless the longest stretch exceeds the number of
chords per tonality, C (§3.3) — at least about 1,400 change points.** With **no** bound at all, L becomes N and
the stretch component grows as N²/2; it then overtakes the pair component once N is larger than about 2C.
At the low end of §3.3 that is N above about 2,900: the average committed large score (≈ 7,500) is above
it, and a chorale is far below it.

### 3.3 The alternatives per stretch, under the ruled vocabulary

**Tonalities, K = 42** — seven letters, each natural, sharp or flat, in major and composite minor (*ruled*,
tonality record, Rulings 1 and 2). **No chord is excluded under any tonality** (L2-S3, *ruled*), so every
tonality carries the whole chord list.

**Chords per tonality, C.** Counted from L2-S4 and L2-S5 and the chord-vocabulary record's Ruling 1 (every
listed kind its own state):

| Component | Count | Basis |
|---|---|---|
| Degrees | 21 | *provisional, my reading* of "every diatonic and chromatically altered degree": seven steps, each with ♭, ♮ or ♯. Range 12–21. |
| Triads | 4 qualities × 3 figures = 12 per degree | L2-S4 (i), (v), *ruled* |
| Seventh chords | 5 qualities × 4 figures = 20 per degree | L2-S4 (ii), (v), *ruled* |
| Neapolitan | 0 extra | ♭II major is already a triad on an altered degree |
| Augmented sixths | 3 | L2-S4 (iv); counted in one bass position, *provisional* (up to 12 if every figure is admitted) |
| **Unapplied chords, C₀** | **21 × 32 + 3 = 675** | |
| Cadential six-four | 0 extra | the record's two readings are the tonic triad in second inversion, already a chord, and the dominant with the sixth and fourth as elaborations — a difference in the note assignments (§3.6), not a new chord |
| Added-note chords | 0, open | a sounding ninth, eleventh or thirteenth is an elaboration in the first specification (chord-vocabulary Ruling 2, *ruled*); **whether an added-sixth class is needed is left to the closure measurement (OQ-L2-1), and the same ruling adds three kinds to what that measurement checks** (the minor-major seventh, the dominant seventh with lowered fifth, the augmented dominant seventh). Each admitted would add about 21 × its figures to C₀ — small beside the applied chords |
| Tonalities, again | 42, open | tonics needing a double accidental are open (OQ-L2-1); if admitted, K grows |

**Applied chords** are the large unknown. L2-S5 admits a chain of depth two (V7/IV/III); its maximum depth is
OQ-L2-1, a measurement; nothing read restricts **which** chords may be applied or **to which** degrees. Two
bounds are therefore carried, both *provisional*:

- **Low:** only the dominant family is applied — V, V7, vii°, vii°7 and viiø7, with their figures, which is
  18 chords — to **6** target degrees, to depth two: 18 × 6 + 18 × 6² = 756. **C ≈ 1,431.**
- **High:** any of the 675 chords may be applied to any of **20** target degrees, to depth two:
  675 × 20 + 675 × 20² = 283,500. **C ≈ 284,175.**

**Labels per stretch, S = 42 × C: about 60,000 (low) to about 12 million (high).** For comparison, the one
published model the derivation cites as affording exact search had 168 labels (*relayed*, L2-S36's
defence). **The whole difference between the two bounds comes from the applied chords**, because the
unapplied count is held at 675 in both: **C differs by a factor of about 200 between the bounds**, and in
the pair component C enters squared. *Not carried into the bounds:* the degree count's own range (12–21);
at 12 degrees C₀ would be about 387 rather than 675, which lowers the low bound by about a fifth.

### 3.4 The cost at each change of chord

**Naive:** every label is linked to every possible preceding label: **S² = K² × C² pair evaluations per
boundary** — about **3.6 × 10⁹** (low) to **1.4 × 10¹⁴** (high).

**With the tonality-change block split** (Row 10.51(iii), *proposed for adoption*, read at the comparison
file, whose outgoing text reads "same-key: chord-transition table; key-change: key-transition × entry
tables"): a link that keeps the tonality reads a chord-to-chord table; a link that changes it reads a
tonality-to-tonality table and an entry table for the new chord — **and, on my reading of "entry tables",
not the previous chord**, which is what makes the split save anything. The best
predecessor across a tonality change is then found once per previous tonality rather than once per previous
chord. Cost per boundary ≈ **K × C²** (same-tonality block) **+ K² + 2 K C**.

**But L2's progression term does not allow that form as it stands** (*my reading*). L2-S34 (iii) puts a
progression term on "the pair of adjacent chords *read as degrees in their tonalities*", including the
cadences that confirm a new tonality, so a link that changes tonality still depends on the previous chord.
If that term depends on the two chords as degrees, and the tonalities enter only through the
tonality-change cost, an exact split still exists: cost per boundary ≈ **K² × C + K × C²**. This is
about **8.9 × 10⁷** (low) to **3.4 × 10¹²** (high) — roughly **42 times less than naive** at both ends,
the saving of one factor of K.

### 3.5 Elaborations crossing a change of chord

L2-S33 makes the link between two stretches read both chords whenever a note's preparing or resolving note
lies across the boundary (a suspension prepared in one harmony and sounding against the next). That breaks
the split of §3.4, because the link now depends on the previous chord's actual notes.

**An exact way round it** (*my reading*): what the link needs to know about the previous chord is only
whether each note involved at that boundary belongs to it. Previous labels can be grouped by that pattern
of memberships, and the split of §3.4 run once per group. **Cost per boundary ≈ G × (K² C + K C²)**, where
**G** is the number of distinct membership patterns at that boundary: at most 2 to the power of the
number of notes involved, and at most the number of distinct spelled chord sonorities (about 21 spelled
roots × 12 qualities ≈ 250, *provisional*). In a four-voice chorale few notes cross a boundary, so G is
small; in an orchestral texture, with many held notes, G can approach its upper limit. **G is
*provisional* in the range 1 to about 250**, and it multiplies everything in §3.4.

### 3.6 The chord-tone assignment

Each sounding note in a stretch is a chord tone or one of eight elaborations (passing, neighbour,
suspension, anticipation, appoggiatura, escape tone, pedal point, unclassified; *ruled*, elaboration
Ruling 1) — **nine choices per note per stretch** (L2-S9). Which of the two cases below holds is L2-S33's
family's question; both are sized.

- **(a) Chosen per note inside the stretch, nothing carried between stretches.** Given the stretch's chord,
  each note's best choice depends only on whether it belongs to the chord and on its own approach,
  departure, duration and metric position. That is a precomputed table per note over two cases (member or
  not) and nine choices. The coverage component of L2-S32 (which chord members sound) couples the notes of
  one stretch through at most four chord members, sixteen patterns. Notes crossing a boundary are scored
  inside the link of §3.5, which already sees both chords. **Cost: negligible next to §3.4** (*my reading*;
  it grows with N × notes sounding × a small constant).
- **(b) Carried in the search state.** If a note held across a boundary must keep a consistent assignment
  in both stretches — L2-S9's falsifier forbids an elaboration that "became" a chord tone in a later
  stretch — and that consistency is kept by carrying the earlier stretch's choice forward, every label is
  multiplied by **2^m to 9^m**, where m is the number of notes held across the boundary. For a chorale (m up
  to about 4) that is 16 to about 6,600; for an orchestral texture with ten held notes, about a thousand
  (2¹⁰) to about 3.5 billion (9¹⁰), and more with more held notes. **At the upper end of that range, case
  (b) alone multiplies the §4 totals past anything §6 converts to hours.** Whether the constraint
  can instead be enforced inside the link, as in (a), depends on the coverage coupling and is not settled
  here.

## 4. Putting it together

**Pair evaluations for one whole run**, with the split of §3.4 and G = 1 (no crossing elaborations), before
the stretch component and before the second pass that masses need (§5):

| Music loaded (change points) | Low vocabulary (C ≈ 1,400) | High vocabulary (C ≈ 284,000) |
|---|---|---|
| Chorale, 60 | 5.3 × 10⁹ | 2.0 × 10¹⁴ |
| Chorale, 150 | 1.3 × 10¹⁰ | 5.1 × 10¹⁴ |
| Butterworth, 1,100 | 9.7 × 10¹⁰ | 3.7 × 10¹⁵ |
| Holst *Mercury*, 1,743 | 1.5 × 10¹¹ | 5.9 × 10¹⁵ |
| Average committed large score, ≈ 7,500 | 6.6 × 10¹¹ | 2.5 × 10¹⁶ |
| **Per 1,000 change points** (multiply by N_W / 1,000 for a Wagner act) | **8.9 × 10¹⁰** | **3.4 × 10¹⁵** |

Naive (no split) is about 42 times each entry. **Then multiply by G (1 to about 250, §3.5), by about 2 for
masses (§5), and add the stretch component (§3.2), which matters only without a stretch bound at large N.**
Case (b) of §3.6 multiplies further.

**What the table shows** (*my reading*, every input declared above):

1. **Within the bounds declared in §3, the decisive driver is the number of chords per tonality, and within
   it the applied chords.** It
   enters squared; its two bounds are 200 apart, so the cost bounds are about 40,000 apart at every size.
2. **The music loaded enters in direct proportion** (C-8 holds for the search, given a stretch bound). A
   selection of a few bars costs a few-bars share of the totals above.
3. **The stretch length binds only without a bound at large N**, or if the longest annotated stretch turns
   out to be longer than the chord list is long.
4. **Crossing elaborations (G) and a carried assignment (case (b)) are the two multipliers that can make
   orchestral sizes unaffordable even at the low vocabulary.**

## 5. Speed-ups that leave the result unchanged (D-200 order), and two limits

Already counted: the change-point rearrangement (§3.1), the tonality-change split (§3.4), grouping by
membership pattern (§3.5), per-note assignment tables (§3.6 (a)). **Not sized on paper, and where the answer
turns:**

- **A sparse progression term.** If L2-S34 (iii)'s fitted table has the shape D-533 gives the current one —
  a stored value for continuations seen often enough, and one proportional remainder for the rest — the best
  predecessor can be found over the stored continuations plus one shared remainder, and the C² term falls
  towards C plus the number of stored continuations. Whether that step is exact needs proof at the design;
  the number of stored continuations is a property of the fit. *My reading*; unsized.
- **A provably safe bound** (L2-S36's own allowance, as in A* search with an admissible estimate). How much
  it saves depends on the fitted weights; it cannot be sized without them.

**Limit 1 — masses** (*my reading*, UNSETTLED). L2-S35 normalises over whole readings, so the published
masses need a sum over all readings, which on my reading is done as a forward and a backward pass — **about
twice** the cost above (the factor is this side's estimate, not a sourced figure). **A safe bound protects the principal reading, not the masses**: a reading dropped because it cannot
win still carried some mass. The derivation's falsifier for L2-S36 excuses only readings of zero mass. So the
second speed-up above may be available for the principal reading and not for the rivals' masses. This
bears on OQ-L2-8 and L2-S35; it is recorded, not decided.

**Limit 2 — no time budget was found.** D-202 reads "among the quantities it must bound is the TIME the
analysis takes" (*ruled*); no figure for that time was found in what I read. **So "affordable" in this
document means nothing more than the times §6 states**; no verdict of affordable or unaffordable is made
against a budget.

## 6. Into time, under one declared assumption

**R = 10⁸ to 10⁹ pair evaluations per second on one processor core** — *provisional*, a hand-declared
stand-in for the hardware, uncertain by a factor of ten. At G = 1, before the factor of two for masses:

- **Chorale, low vocabulary:** about 5 to 130 seconds. **High vocabulary:** about 2 days to 2 months.
- **Holst *Mercury*, low:** about 2.5 to 25 minutes. **High:** about 2 months to 2 years.
- **Average committed large score, low:** about 11 minutes to 2 hours. **High:** about 10 months to 8 years.

## 7. What each possible dial would save — stated, none recommended

| Possible dial | Saving | What it touches |
|---|---|---|
| Smaller selection or context | in direct proportion to N | C-8, D-261 (the context is found, not chosen); D-624's cap is a safety cap, not an answer |
| A cap on stretch length | only where L would exceed about C, or at large N with no bound (§3.2) | L2-S7: a cap is an admission rule and carries L2-S2's ceiling cost |
| Fewer applied chords or a shallower chain at a lower setting | up to (C_high / C_low)² ≈ 40,000 on the pair component | L2-S2's ceiling cost; OQ-L2-8's option (a) |
| Ignore crossing elaborations (the "weak" form) | up to G | L2-S33, which rejects the weak form |
| Keep only the best W labels per change point (a beam) | about S / W | L2-S36 and Ruling 1 (iv): a reduction of the readings kept, allowed only by ruling |

## 8. The result, and which of §1b's outcomes follows

**The sizing cannot tell whether exact search is affordable at D-201's sizes.** At chorale size and the
low vocabulary it takes seconds to about two minutes; at the high vocabulary it takes days to months even at
chorale size, and about nine hours at 10⁹ evaluations a second for a selection of only ten change points. At
orchestral sizes even the low vocabulary costs minutes to hours per large score before G, and the
multipliers of §3.5 and §3.6 (b) can push it out of reach. **Three unknowns decide it:**

1. **How many applied chords the vocabulary carries** — which chords may be applied, to which degrees, to
   what depth. That is OQ-L2-1, the closure measurement on annotated music; between this document's two
   provisional bounds for it, the cost moves by a factor of about 40,000.
2. **The two unsized speed-ups of §5** — a sparse progression term and a safe bound. Both need the fitted
   form or code, and the safe bound may not reach the masses.
3. **A time budget**, which was not found in what this sitting read.

Under §1b item 2 of the tractability record, "if the sizing cannot tell, whether a code trial may run inside
this phase comes to the user on its own surface". **This document asks nothing.** Whether that question, or
another, actually goes to the user is decided after the check of this document at its sources, and only
if the record does not already answer it.

## 9. Read, not read, and bounds

- **Read this sitting:** the derivation at §0–§2, L2-S1 to L2-S10, L2-S23, L2-S31 to L2-S36, L2-S43 and §4;
  `FRAMEWORK.md` at C-1 to C-9, the L2 charter and A.7; D-004, D-030, D-200, D-201, D-202, D-261, D-624 at
  their group files; the ruling records of the tonality, chord-vocabulary, elaboration-relations,
  assignment-evidence, cadential-six-four and tractability families whole, and the tractability surface
  whole; the comparison file at Rows 10.51 and 10.52 and its list entry for 10.51(iii); `open_items/OI-209.md`,
  `OI-210.md`, `OI-215.md`, `OI-227.md`; `cowork_architecture_review_2026_07.md` by search.
- **Not read:** the code; `cowork_joint_estimator_factorization.md`; `cowork_bounded_context_design.md` (so
  D-624's cap value is not known here); any paper; the derivation's statements other than those named.
- **Every number marked *provisional* is a stand-in** (21 degrees, 3 augmented-sixth positions, the two
  applied bounds, about 250 sonorities, R) and enters no fit. A verdict that would flip inside a provisional
  value's range is reported as unsettled, which is what §8 does.
- **Declared departures:** this sitting ran **two shell commands in error**, both in the container, neither
  reading nor writing anything, and no number here rests on either: `echo skip` during the boot, and `true`
  during the check (§B). Both break entry 291's "no shell at any point". No memory tool, git, widget, task
  list, subagent or web access.

This document writes no instruction for Claude Code, edits no other tracked document, amends neither the
framework nor the decisions register, and allocates no register number.

---

## §C. The user's word on the result, and what it settles

**His words, verbatim, in the turn after the check:** "On the sizing / response time; as long as we are
prepared for user settings for effort we will know where in the code we can apply them. One simple example
could be that a very lazy effort only uses lookup tables for chords and no procedural algorithms. Next step
would be to switch some algorithms on/off, maybe also restrict any temporal expansions beyond some limits.
Other restrictions we already know of are "allowed" modes (that would follow another user setting that maybe
would be "style"-ish. So, as long as we build the software so that there are clear and easy "entry points"
where we could apply/adhere to an "effort"-setting, I an not worried that we actually have not measured the
response times. Continue."

**What it settles.** §8's outcome ("whether a code trial may run inside this phase comes to the user") is
**not put**: no code trial and no timing measurement is owed before L2's specification is ratified. What is
owed instead is that **the specification names clear entry points where an effort setting applies**. This is
D-035 ("every cost-driving choice is a setting, never a hardcoded constant") and D-202 (one setting, several
dials, bounding time) applied to L2, so it is recorded as following from the record and his word, not as a
new ruling. Which dials exist, and their defaults, are decided when the effort setting is built and
measured (D-202 stays DEFERRED), not before ratification. The tractability record's §1b item 2 sent the
dials question to him "before this layer's specification is ratified"; his word moves it to the build.

**The entry points this sizing locates** (*my reading*, a proposal for the application act, not ruled):
(a) the admitted chord vocabulary — which chords may be applied and how deep (§3.3), and later the allowed
modes under the modal increment, following a style setting as he describes; (b) which terms and algorithms
run — for instance the crossing-elaboration link (§3.5), or a table-only chord reading at the lowest
setting, as his example; (c) the context extension's limit (D-261, under D-624's cap); (d) a stretch-length
cap (§3.2); (e) any reduction of the readings kept. Each is a setting the user turns, so none is the "quiet"
reduction Ruling 1 (iv) of the tractability record bars. **The top setting is exact, as L2-S36 states.**

**The two held rows** (Row 43.12, the old plan's effort dial on candidate counts; Row 7.104(i), the old key
decoder's candidate count an effort preset may lower) were held for the dials question. *My reading:* they now
travel with the effort setting's own design (D-202), not with L2's ratification. Recorded here as a
proposal; he may place them otherwise.

## §B. The check, run in the turn after the user's "continue"

Over completeness, coherence, correctness and absolutes, at the staged copies of the sources. **Thirteen
corrections, each made at its site; former wordings kept here (#12).** None moves a number in §3.4, §4 or
§6, the result of §8, or which of §1b's outcomes follows.

1. §2, *former:* "which entry 291 had not found". Entry 291 says it found no count for "a Wagner act or a
   symphony"; it says nothing of other orchestral scores. Narrowed.
2. §2, *former:* "matches the number of distinct onset moments in a chorale and not its number of notes".
   No chorale's onset moments or notes were counted this sitting. Restated as a reading of order of size.
3. §2, completeness: the 23 large scores include two pairs of duplicate uploads (OI-215's own list), so the
   average is per file. Added.
4. §2, *former:* "carries no count; *checked* by search". The search was of one file, for five words. Its
   reach now stated.
5. §3.2, *former:* "the stretch component costs about L × (number of chords per tonality) per change point,
   and the pair component about (number of chords per tonality)² × 42". The factor 42 belongs to both
   components; the conclusion (L binds only above about C) is unchanged.
6. §3.3, completeness: an added-sixth class and three more seventh kinds are left by the chord-vocabulary
   record's Ruling 2 to the closure measurement, and double-accidental tonics are open; each may enlarge C₀ or
   K. Added to the table, *former* row: "Added-note chords | 0 | …".
7. §3.3, *former:* "The applied chords are where nearly all of the range lives". The unapplied count is the
   same in both bounds, so the whole difference between them is the applied chords; "nearly" understated it
   and "range" left the degree count's own range unmentioned. Both now stated.
8. §3.4, *former:* "an entry table for the new chord, **not the previous chord**". The outgoing text reads
   "key-change: key-transition × entry tables"; that the entry table does not read the previous chord is my
   reading. Quoted and marked.
9. §3.6 (b), *former:* "a thousand to astronomically many. **Case (b) is unaffordable at orchestral sizes on
   its own.**" A hyperbole, and a verdict of "unaffordable" with no time budget (§5, Limit 2). Replaced by
   the numbers for ten held notes and a statement against §6's conversion.
10. §5, *former:* "done as a forward and a backward pass — **about twice** the cost above". The method and the
    factor are my reading. Marked.
11. §5, *former:* "**Limit 2 — no time budget is on the record.** D-202 says the ambition setting "must bound
    the TIME the analysis takes"". Not D-202's words, which are "among the quantities it must bound is the
    TIME the analysis takes"; and "on the record" claimed more than what was read. Both corrected, and the
    consequence for the word "affordable" stated.
12. §8, *former:* "At chorale size and the low vocabulary it is affordable in seconds; at the high vocabulary
    it is not affordable at any size." Two verdicts against a budget the document says it does not have, and
    "any size" wider than the sizes computed. Replaced by times.
13. §8, *former:* "it alone moves the cost by a factor of about 40,000" and "which the record does not
    hold". The factor is between this document's two provisional bounds, not a property of OQ-L2-1; the
    second is a claim about the whole record from a partial read. Both narrowed; §4 point 1 scoped to the
    bounds in the same way (*former:* "**The decisive driver is the number of chords per tonality, and within
    it the applied chords.**").

**Checked and standing:** the quotations of L2-S3, L2-S4, L2-S5, L2-S7, L2-S9's falsifier, L2-S33,
L2-S34 (iii), L2-S36 and its falsifier, C-8, D-004's "NO recorded derivation", D-533's form, Row 10.51 and
Row 10.52, §1b item 2's third clause, the tonality record's 42 and two modes, the elaboration record's eight
relations, the cadential six-four record's two readings, OI-215's and OI-227's counts (1,100; 1,743; 172,611;
23); and the arithmetic of §3.3 (675; 1,431; 284,175; S), §3.4 (both per-boundary costs, the factor of
about 42), §4 (every entry, re-multiplied) and §6 (every conversion, the chorale-high upper end at about two
months).

**What this check did not do:** re-read any source not staged at the first turn; search the record wider
for an event count of a Wagner act or for a time budget; test the exactness of the rearrangements marked
*my reading* (§3.1, §3.4, §3.5, §3.6 (a)), which is owed at the design, not here.

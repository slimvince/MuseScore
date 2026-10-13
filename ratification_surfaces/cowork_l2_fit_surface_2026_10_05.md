# How the analysis learns its numbers — the tenth family surface for the chord-and-key layer — 2026-10-05

> STATUS: DECISION SURFACE, NOT RULED. No question on it has been put. Written by the Cowork sitting that
> booted on `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_eighty_nine.md`. Tags: *checked*
> = read at the source this sitting; *relayed* = taken from a record and not re-read at its source; *my
> reading* = my inference.

## 1. Where we are

You are ruling, family by family, on how the new specification of the analysis's central layer should
read. That layer decides together, in one pass: the key at each moment, where each harmony gives way to
the next, which sounding notes are chord notes and which are passing notes, suspensions and the like,
and which chord sounds over each stretch. Beside its winning reading it publishes the rival readings,
each with a weight.

To choose between readings, the layer gives every candidate reading a number — call it the reading's
**score** — built by adding up many pieces of evidence: how well the notes fit the chord, whether the
bass is the root, how likely one chord is to follow another in this key, how costly a change of key is,
and so on. Each piece of evidence needs numbers: how much a missing fifth costs, how likely V is to go to
I, how strongly a stepwise bass counts. **This family is about where those numbers come from.**

Nine families are ruled. The derivation's statement for this one is **L2-S38**; the comparison file sets
138 sentence-parts of the existing documents beside it (73 agree, 65 differ).

## 2. The facts, before any question

**What the derivation says (L2-S38, *checked*, derivation lines 938–965).** "Every weight of the
candidate score is fitted from annotated music, not set by hand. The fit is discriminative, on held-out
folds, with its capacity budget declared in advance. Its objective is the graded measure, not likelihood
alone. It is fitted only on freely licensed music. It treats every recorded analyst variant as an
acceptable answer. No value is given here." In plain words: no number is chosen by a person; numbers are
learned from analysed music; they are learned so as to make the analysis *agree with the analysts* as
often as possible (rather than to make the music "most probable" under the model); the music used to
grade the result is never the music used to learn it; only freely licensed music may shape a number that
ships; and where analysts disagree, any of their readings counts as right. Its status is **open**: the
learning itself belongs to the measurement-design stage and a later act.

**What the framework you ratified says (*checked*, `FRAMEWORK.md` lines 406–408 and 845–849).** The L2
charter leaves "how any weight is fitted" to this layer's detail specification. Its design point DP-P,
"How are the terms of L2's score combined and fitted?", is marked **not decided** — left to the detail
specification and measurement design — and records one fact as the reason it is a real design point:
learning the combination weights by likelihood scored 12.2 on the measure actually wanted, against 19.6
when the weights were learned against that measure directly. (The framework labels this a fact; DP-P
names no source, and its twin in the framework's first-stage draft, DP16, names Och. It is a published
study's result, not a measurement on this project's music. I did not read the paper.)

**What the existing design says — D-525, user-ratified 2026-07-19 (*checked*, `decisions/group_A.md`, its
entry).** The learning is **staged**:

- **The tables are counted, once, and frozen.** Each table of probabilities — how likely each chord is to
  follow another in a key, which bass note goes with which chord and inversion, how notes of each kind
  (chord tone, passing note…) behave, how likely a key change is — is counted from the analysed chorales
  and then never touched again. Every entry stays a musically meaningful probability.
- **Only a short list of weights is learned on top** — one per kind of evidence, saying how much each
  table counts against the others. That list is capped at fourteen (D-271, *checked*).
- **Those few weights are learned by likelihood** (technically, "convex conditional likelihood").
- **A mandatory comparison:** setting every weight to one *is* the plain counted model, so the learned
  weights are adopted only if they beat that on held-back music.
- **Its own record of the road not taken:** learning everything together, freely, "possibly a higher
  ceiling", excluded because it loses the ability to see which table is at fault when the analysis goes
  wrong; "re-test if that constraint stops binding".
- **Its own fallback:** a direct search over the few weights against the reported measure "if the
  likelihood-fit weights measurably disagree with the reported metric".

Two neighbours of D-525 belong to the same design: **D-534** (*checked*) — the cost of a chord tone that
never sounds is *counted* per chord factor, so a silent seventh costs a great deal and a silent fifth
little, "the musical point" being yours; and **D-271** (*checked*) — the budget of how many numbers may be
learned at all.

**The one place the existing documents say what was actually built** (*relayed*, comparison Row 17.4,
quoting `ARCHITECTURE.md`'s opening block): the shipped weight list is "the direct-metric SELECTED
vector" — that is, the fallback route. The comparison sets that aside as a question for the audit; it is
not checked at the code.

**Where the two texts genuinely differ.** On the other rules — learned from analysed music, never set by
hand, never graded on the music it learned from, freely licensed music only, any analyst's reading
accepted — the derivation and the existing design say the same thing in substance (that is where most of
the 73 agreements are). They differ on two points only:

1. **Are the tables counted and frozen?** D-525: yes; only a few weights move. L2-S38 read literally:
   "every weight … the fit is discriminative" — everything is learned together.
2. **What are the learned weights aimed at?** D-525: likelihood first, the analysts' agreement only as a
   fallback. L2-S38: the analysts' agreement ("the graded measure, not likelihood alone").

**And one gap underneath both** (L2-S38's own weak point, its open question OQ-L2-13, *checked*): no
analysed collection known to the derivation marks, note by note, which notes are chord tones and which
are passing notes, independently of the chord labels. So anything about chord tones and passing notes can
only be learned and graded *through* the chord labels.

**What the rest of the existing text is.** Most of the 65 differences are not about the new design at
all: they are the old chord scorer's hand-set constants — "bassNoteRootBonus = 0.70", "the root weighted
1.8×, the third 1.2×", the twenty-one mode priors, and so on — which simply contradict "not set by hand".
The comparison proposes setting each aside for the audit (does the shipped code still use it?).

## 3. The decision that remains — how the numbers are learned

The record does not settle this: the framework you ratified explicitly leaves it open, and the derivation
and D-525 answer it differently. Three positions.

### Position 1 — D-525 as ratified

Tables counted from the analysed chorales and frozen; a short list of weights learned by likelihood; a
direct search against the analysts' agreement only if the likelihood weights are measured to disagree
with it. L2-S38 would be amended at "discriminative" and "the graded measure" to say this.

- *Towards the objective (the most precise analysis):* the safe, well-understood route, but it aims the
  weights at something other than what we grade. The one measured comparison on record (DP-P), a published
  study and not a measurement on our music, found that costing a great deal (12.2 against 19.6). The fallback catches it only after a separate measurement
  shows the disagreement.
- *Towards the principles:* each table is established on its own (#19); a small, declared number of
  learned values (#20); a fault can be traced to one table (#3, #13). Keeps a ratified decision unchanged.
- *Meta level:* the analysis's own specification only.

### Position 2 — keep the staging; aim the few weights at the analysts' agreement (recommended)

Tables counted once and frozen, exactly as D-525; the short list of weights learned directly against the
graded measure (D-525's own fallback becomes the main route; a likelihood fit may still serve as the
starting point). L2-S38 would be amended at its second sentence: "The tables are counted from annotated
music, once, and frozen; the short list of combination weights is fitted discriminatively, to the graded
measure." Everything else in L2-S38 stands.

- *Towards the objective:* it aims the learned numbers at exactly what we want — agreement with the
  analysts — which is the point DP-P's measured fact makes, while every table keeps its musical meaning
  (a silent seventh still costs what the chorales say it costs, D-534). It does not reach the possibly
  higher ceiling of Position 3.
- *Towards the principles:* #19 (each table established on its own), #20 (the weight list stays within
  the declared budget of fourteen), #3 and #13 (a wrong result can still be traced to one table), #1
  (L2-S38 names minimum error-rate training as the published method, and D-525's fallback is that same
  protocol applied to "the direct-metric few-weight search").
  It changes D-525 only by promoting a route D-525 already recorded as "the established fallback".
- *Meta level:* the analysis's own specification only.

### Position 3 — L2-S38 read literally: learn everything together, against the analysts' agreement

No frozen tables; every number of the score learned jointly and discriminatively.

- *Towards the objective:* possibly the highest ceiling — D-525 itself concedes that. But it learns many
  more numbers from 326 chorales, and *my reading* is that the published search against the wanted
  measure is a method for a short list of weights; whether it works for hundreds is not established on
  the record.
- *Towards the principles:* a fault can no longer be traced to one table (the reason D-525 excluded it,
  #3, #19); *my reading* is that the budget of fourteen learned weights (D-271) would have to be
  rewritten, a protocol change in its own right (#22); the counted, musically meaningful tables — your point about the silent seventh —
  would become free numbers. It reverses a ratified decision's recorded exclusion.
- *Meta level:* the analysis's own specification, plus an amendment to a ratified fitting protocol.

### The recommendation

**Position 2**, because it is the only one that both aims the learned numbers at the thing we grade —
the one fact the framework records on this point says that matters — and keeps every table counted and
traceable, which is what makes a wrong analysis diagnosable and what your own musical reasoning
about chord factors relies on. It asks the least of the ratified record: one route D-525 already
sanctioned becomes the main one.

**What each position does to the nine sentence-parts the comparison could not place** (Rows 1.45,
10.13(ii), 10.21(i), 12.24(i), 12.25, 48.35(i), 48.37(i) — "the tables counted once and frozen"; Rows
10.16(ii), 48.35(ii) — "the weights learned by likelihood"):

- Position 1: all nine **proposed for addition** to L2-S38.
- Position 2: the seven "counted and frozen" parts **proposed for addition**; the two "by likelihood"
  parts **historical** (a replaced choice of aim).
- Position 3: all nine **historical**.

## 4. What the record already settles — confirmations, not choices

### 4.1 The old fixed ranking of evidence does not carry into the new layer

The older function-layer design (D-383, decided 2026-07-07, its register entry ratified by you 2026-08-02,
*checked* at `decisions/group_H.md`) ruled
that the bass, the spelling and key-consistency "decide", and that a "licensed progression" (whether one
chord may follow another) "only breaks ties" and "may never override a committed root". Its ground was a
real measurement: the progression-driven correction moved a correct root to a wrong one on about 78 % of
its uses.

Why the record already answers it: that rule ranks evidence in a design where one layer first commits a
chord and a later layer chooses among its alternatives. The framework you ratified replaced that with one
decision in which key, chord and the rest are chosen together, and leaves how evidence is combined to this
layer's detail specification (DP-P), where L2-S38 derives that every weight is learned. D-383 itself fixed only "the ordering/direction" and left "the channel weights and
the deciding margin" to be learned. Learned against the analysts' agreement, a progression term that does
not help get the root right simply ends up with a small weight — the measurement then decides what D-383
fixed by hand. The third family's Ruling 1 already set aside a fixed rule of the same kind (D-333's
three-tier rule for chord tones) in favour of weighed evidence (*checked*, its ruling record). And the
measured 78 % finding is not lost: Row 8.74(i) already sets it aside as an audit question.

*Why the alternative is closed* — writing the ranking into L2 as a constraint on the learned weights:
it would be a number set by hand in a layer whose rule is that none is (L2-S38); it would sit uneasily
with the charter's line that "a reading-shaped evidence producer is a score and never a constraint" (that
it reaches a ranking of evidence is *my reading*); and its object — a committed root — does not exist
there. Meta level: the analysis's own specification.

Placements: Rows 8.74(ii), 8.77, 8.78(ii), 8.81, 8.82, 9.332(i) → **historical** (8.81 names only L2-S31,
is not one of this family's 138 parts, and travels with 8.77). D-383's register status waits for the ratification act, as earlier families did
for D-333 and D-385.

### 4.2 The old fitter's exemption for "values with a ratified structural reason" does not carry

Row 9.160(iii): the old weight-fitting plan for the legacy chord scorer left unfitted "any value whose
Phase-0 row names a ratified structural rationale". That plan was for the old scorer's hand-set constants;
the new layer has no such constants, and L2-S38 says no number is set by hand. Placement: **historical**.

### 4.3 Chord tones and passing notes are learned and graded through the chord, until a better collection is found

OQ-L2-13 — no analysed collection marks chord tones and passing notes note by note, independently of the
chord labels. Two earlier families already carried the consequence as a cost you accepted: the third
family's ruling (*checked*) says that "until one is found or the user rules otherwise they are fitted and
graded only through the chord", and the second family's ruling (*checked*) records the same gap for the
elaboration names. Confirmation: that interim stands for this family; finding or commissioning such a
collection is the measurement-design stage's search. OQ-L2-13 stays open as a search, not as a choice.

### 4.4 The other placements, as the comparison proposed them

- **Agreements (73):** 43 carried by L2-S38 as it stands; 28 moved to *the measurement of the analysis*
  (the held-out split, the capacity budget's details, which music validates, the graded measure itself,
  the headline number — the comparison's ground being L2-S38's own status, "the fit is the
  measurement-design stage's and a later act's"); 1 historical (Row 15.29); 1 set
  aside for the audit (Row 17.4(v), which weight list ships and how it was chosen).
- **Differences (65), apart from the fifteen placed above:** 44 set aside for the audit — Row 1.2(ii)
  ("which corpus's labels were the shipped values counted on, and does its licence admit them?"), Rows
  3.33–3.34 (the dormant decoder's hand-set abstention constant), Row 17.4(iv) (are the shipped tables the
  committed ones, counted on which labels?), and the old scorer's and old key-finder's hand-set constants
  (Rows 9.3, 9.49, 23.4, 23.20–23.22, 23.24, 23.47–23.48, 23.89–23.93, 23.184, 23.188, 24.20(ii), 39.24,
  39.134–39.153, 39.219, 39.310(i)); 2 moved to *the measurement of the analysis* (Row 6.153, measuring
  chord-tone calls; Row 9.108, the held-out exception at adoption); 4 historical (Rows 9.209, 9.300(ii),
  15.39, 56.3(i)).

Counted: 73 agree + 65 differ = 138, every part placed once the question in §3 is ruled.

## 5. What was read, what was not, and what is unsettled

- **Read:** the derivation at L2-S20, L2-S31 to L2-S40 and its open questions §4; `FRAMEWORK.md` at the L2
  charter, §9.0's closing ruling, DP-P, DP-Q, §10 and the first-stage draft's DP16; the comparison file at
  its vocabulary (§5), §7's entries for L2-S1 to L2-S9 and L2-S37 to L2-S40, and every one of the 138 row
  parts named above at its place in §6 — for Rows 6.202, 6.205, 9.83, 9.221, 12.40, 21.3, 39.310 and 62.4
  at their heading, axis and disposition only, the outgoing-quotation line not displayed by the search;
  for the others the row whole; register entries D-096, D-097, D-098, D-114, D-270, D-271, D-272, D-525, D-534 and D-383 at
  their group files; the nine earlier family ruling records by search for this family's identifiers, and
  the elaboration-relations, assignment-evidence and working-order records at the passages found.
- **Not read:** `cowork_joint_estimator_architecture.md`, `ARCHITECTURE.md` and `cowork_prefit_gates.md`
  beyond what the comparison rows and register entries quote; Och's paper; D-292 and D-352 beyond their
  register titles; the code.
- **Unsettled, not this family's choice** (*my reading*): **which licence class the chorale analyses fall
  in is not settled** (Row 1.24, the open-items row OI-271, *relayed*) — every position above counts or
  learns from them, so a shipped number depends on that answer; what "the graded measure" is exactly
  (measurement design); whether Position 2 or 3 leaves room for the plain counted model as a mandatory
  comparison arm (D-525's arm, Row 48.36, already moved to measurement).

This surface writes no instruction for Claude Code, edits no tracked document, amends neither the
framework nor the register, and allocates no register number.

**The questions, to be put later, one per turn:** first the decision in §3; then §4.1 and §4.2 together
as one confirmation; then §4.3; then §4.4.

---

## §B. The check, run in the turn after the user's "continue"

Run over completeness, coherence, correctness and absolutes, at the sources staged this sitting.
**Corrections, each made at its site, the former wording kept here (#12):**

1. §2: *former* "(The framework labels this a fact and cites Och; I did not read the paper.)" DP-P names no
   source (`FRAMEWORK.md` lines 845–849); only the first-stage draft's DP16 names Och (line 1918). The
   sentence now says so, and that the figure is a published study's, not a measurement on our music.
2. §3, Position 1: *former* "The one measured comparison on record (DP-P) found that costing a great deal"
   — now qualified as a published study, not our music, for the same reason.
3. §3, Position 2: *former* "#1 (a search over a few weights against the wanted measure is the published
   method L2-S38 itself names)". L2-S38 names minimum error-rate training and says nothing of "a few
   weights"; the "few-weight" wording is D-525's ledger (d). Now attributed to each text.
4. §3, Position 3: *former* "the budget of fourteen learned weights (D-271) would have to be amended". The
   cap governs a combination-weight list that Position 3 would not have in that form; what happens to it
   is my reading, now marked so.
5. §4.1: *former* "and leaves how evidence is combined to the learned weights (DP-P)". DP-P leaves it to
   the detail specification; that every weight is learned is L2-S38's derivation. Corrected.
6. §4.1: *former* "it would rank evidence inside one decision where the charter makes every piece of
   evidence a cost and never a veto". The charter's words are about the tonality–chord coupling and about
   "a reading-shaped evidence producer"; it now quotes them and marks their reach to a ranking as my
   reading.
7. §4.1: Row 8.81 is now said to lie outside this family's 138 parts.
8. §4.4: *former* "L2-S38 says these belong to measurement design" — now the comparison's ground, quoting
   L2-S38's status sentence.
9. §5: *former* "every one of the 138 row parts named above at its place in §6 (for Rows 39.135–39.152 the
   whole run; for the others the row itself)". Eight rows were read at heading, axis and disposition with
   their outgoing-quotation line not displayed; now named.

**Checked and standing:** the 138 parts re-counted from §7's two lists — agreements 43 carried, 28 moved,
1 historical, 1 audit; differences 44 audit, 2 moved, 4 historical, 15 unplaced (nine placed by §3, five
by §4.1, one by §4.2); D-525's, D-271's, D-534's and D-383's quoted phrases at their group files; L2-S38's
quoted sentences; the two earlier rulings quoted at §4.3; the DP-P figures. **None of the corrections moves
the recommendation, a confirmation or a placement.**

**Declared:** one shell command was run in error during the landing — `echo placeholder`, in the
container; nothing read or written, no claim rests on it (the same slip entries 287 and 288 record). No
other shell command was run, in the container or on the device; no memory tool was used. *(Former
wording, kept (#12): "no shell command was run in this sitting, in the container or on the device; no
memory tool was used." It was true when written and became false at the landing.)* **Landing:** the first
commit reported success and landed a stale copy without §B (18,613 bytes); the second, guarded by that
copy's modification time, landed the corrected text.

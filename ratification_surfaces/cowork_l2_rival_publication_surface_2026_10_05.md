# How much the layer publishes about rival readings — the family on withholding rivals — 2026-10-05

> STATUS: DECISION SURFACE, NOT RULED. No question on it has been put. Written by the Cowork sitting that
> booted on `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_ninety_three.md`. Tags: *checked* =
> read at the source this sitting; *relayed* = taken from a record and not re-read at its source; *my
> reading* = my inference. §A is the surface as delivered, corrected at its sites by the check; §B is the
> check, with every former wording kept (#12).

## §A. The surface

### 1. What this is about, and the cut

You are ruling, family by family, on how the new specification of the chord-and-key layer should read.
That layer decides together the key of each stretch, where one harmony gives way to the next, the chord
over each stretch, and which notes are chord notes and which are passing notes, suspensions and so on. One
complete answer of that kind is a **reading**. Besides its best reading, the layer publishes **rival
readings with their weights**: for each stretch, every other way it could be read (another chord, another
key, other boundaries), each with the share of the total weight it gets; and, separately, a ranked list of
the best complete alternative readings of the whole passage.

**The question here:** may the layer leave the weakest rivals out of what it publishes, provided they can be
worked out again? The derived statement **L2-S42** says yes (quoted whole in §2). Several standing texts of
yours say no truncation at all.

**The cut I propose.** Entry 293 names five derived statements for this family: L2-S42 (withholding),
L2-S35 (how the weights are normalised), L2-S40 (what a weight means), L2-S41 (rivals spanning several
stretches, and the whole-reading list), L2-S45 (what passes to the next layer). The comparison file names
them in 245 parts of rows between them (*checked* at its §7). I take **L2-S42 and L2-S41** here (28 parts),
because L2-S41's last clause publishes the whole-reading list "down to the threshold of L2-S42" and so
cannot be settled apart from it. I propose to leave out:

- **L2-S35 and L2-S40** (174 parts): they decide what a weight *is* — normalised over complete readings, a
  model quantity and not a calibrated probability, and how it is named against your confidence-class rule
  D-267 (open question OQ-L2-14). Whether a weak rival may be left out is the same question whatever the
  weights mean (*my reading*), so these two go together as the next family. Entry 293 joined L2-S35 to this
  one because the threshold is measured in its weights; that is true, but it does not change this choice.
- **L2-S45** (43 parts): what crosses to the next layer — a family of its own.

You may change this cut.

### 2. The statement, and the texts on each side

**L2-S42, whole** (*checked*, `cowork_blind_derivation_l2_2026_09_27.md`): "L2 may withhold from publication
rivals whose mass falls below a declared threshold, but only because every withheld rival is recomputable.
The model, its weights and its inputs are fixed and named, so the withheld mass can be recovered. The
threshold's value, and the withheld total mass per span, are published with the rivals." Its defence:
principle #12's recomputable clause, and that every published record names the tables, weights and program
version that produced it (D-275), "which is what makes regeneration possible"; "Publishing the withheld mass
keeps the absence visible." The threshold's value is to be measured (OQ-L2-15: "*Measured* against what the
consumers (L3, the display) actually read"). Its own stated weakness: a consumer that cannot rerun the
analysis, such as the display, loses the withheld rivals, and "D-295's 'every inferred object must be
displayable' then requires the display to be able to request them, which is a consumer's design and not
L2's."

**Texts that support withholding:**

- **Principle #12** (*checked*, `CLAUDE.md`): a ruled-out possibility is kept "unless the exclusion is
  recomputable from what is kept"; and a collapse is not a loss "where the collapsed value is derived
  deterministically from something still carried, or is regenerable from it".
- **D-297** (LIVE, *checked* at its group file): "NEVER COMPUTING a possibility is not information loss;
  only DISCARDING a computed one is." This covers the whole-reading list (§3).

**Texts that point the other way:**

- **D-006** (LIVE, *checked* at its group file): the current engine "publishes, per committed segment, the
  ESTABLISHED content-score uncertainty surface as two full candidate lists (no truncation constant)".
- **Your amendment of 2026-07-26** (Row 49.23, claim (i), *checked* at the comparison file; the date is the
  one Row 49.22 quotes for the same "second amendment" of that document's §3.3): "No truncation
  constant exists anywhere in the publication (a breadth "N" or a gap-window width would be a hand-set value
  with no basis, #1/#19); nothing computed is discarded at the boundary (#12 …); display subsetting is a
  downstream presentation read."
- **D-425** (LIVE, *checked* at its group file): the uncertainty surface's contract "IS" the full spread of
  weight over the readings, and a narrower form may never become the end state silently.
- **D-295** (LIVE, *checked* at its group file): "every inferred object must be displayable"; revealing it
  gradually is intended, leaving it unreachable is not.
- **D-099** (LIVE, *checked* at its group file, the rule's words as Row 21.72 quotes its home): a ruled-out
  reading is carried at low confidence "unless the elimination is recomputable from what that surface does
  keep". *My reading:* L2-S42's withheld rivals are recomputable from the named model plus the music, not
  from the published surface alone, so D-099's narrower wording is not plainly met.
- **D-331** (LIVE, *checked*): the dormant chord engine's carried alternatives are "never pruned".
  **D-380 and D-381** (both marked as concerning the dormant pipeline, *checked*): carry ruled-out chord roots
  at low confidence "rather than dropping them"; D-381 also allows caps whose depths are "fitted later".
- **Your word in the silence sitting today** (*checked* at that record): a very low-weight reading is still
  inferred and handed on, and whether it is shown is the display's decision.

**Do these texts bind the new layer?** D-006, D-425 and the amendment were written for the current engine,
whose lists are per stretch, over 24 keys and a counted chord list (*relayed*, sizing §2). The new layer's
lists are of a different size: the sizing counts about **60,000 to 12 million labels per stretch** (one key
with one chord; *checked*, sizing §3.3), so the full list of rivals at one point can run to that many
entries, times the stretch lengths considered (*my reading*). How many of them carry a weight above exactly
zero is not settled by anything I read. Whether texts written for the current engine's lists bind lists of
this size is part of what you decide here.

### 3. What the record already settles, so nothing here is asked

1. **The ranked list of complete readings is bounded in every position.** With two stretches alone there are
   already billions of complete readings (60,000², *my reading*), so beyond the shortest passages the list
   cannot in practice be complete; the search works out only the best of them (*my reading* of "the best
   whole readings, ranked"), and by D-297 the ones never worked out are not lost. Each single ambiguity still
   appears in the per-stretch rivals (L2-S41's own false-negative path: "The per-span marginals still carry
   each ambiguity", *checked*). So the open
   question is only about the **per-stretch rivals**, which, on the sizing's reading, are all computed
   whenever the weights are (a forward and a backward pass; *relayed*, sizing §5, marked there as its
   reading).
2. **Withholding changes no answer of this layer.** It concerns what is published, not what is weighed; the
   best reading and every weight stay as computed. What the next layer and the display receive is smaller
   (*my reading*). It is a saving in the size of the output, not in the analysis's time
   (*my reading*).
3. **Your rule on cost settings applies.** D-035 (index line only, *checked*): "every cost-driving choice is
   a setting, never a hardcoded constant". D-200 (*checked* at `CLAUDE.md`): make it work first; "compromise
   on performance only if performance proves to be a problem". And your word on the sizing today: build "clear
   and easy "entry points"" for an effort setting (*checked*, sizing §C).

### 4. The choice that remains — three positions

**Position 1 — L2-S42 as derived.** The layer may leave out rivals below a fixed threshold, a design value
measured against what the next layer and the display read; it publishes the threshold and the weight left
out at each stretch, and a left-out rival can be worked out again.

- *Towards the objective (#4):* no effect on the readings; the next layer gets a smaller list.
- *Towards the principles:* meets #12's recomputable clause and D-297. Against it stand the amendment's
  "no truncation constant … anywhere in the publication" and its reason (a cut-off value would be "a
  hand-set value with no basis, #1/#19"): the consumers OQ-L2-15 measures against, L3 and the display, are
  not yet specified for the new layer (*my reading*), so the measurement has little to stand on. D-099's "from what that surface does keep" is not plainly met. It puts a compromise for
  size in the design before size has proved a problem (D-200). It sits against your word today that
  low-weight readings go to the display, which decides.
- *Meta level:* the analysis's own specification only.

**Position 2 — nothing computed is ever left out.** Every per-stretch rival is published with its weight, at
every setting. L2-S42 would read: "L2 withholds no span-rival from publication. The ranked list of whole
readings is bounded by a declared length."

- *Towards the objective:* the same; the display and the next layer see everything.
- *Towards the principles:* carries your amendment, D-006, D-425 and D-295 into the new layer as written;
  #12 holds with nothing to excuse. But it fixes in the specification that the largest output the layer can
  produce is always produced, with no entry point to reduce it, which runs against D-035 (the size of the
  output being a cost, *my reading*) and your sizing word. The size is unmeasured, and at the high vocabulary bound it is
  millions of numbers per point in the music (*my reading*).
- *Meta level:* the analysis's own specification only.

**Position 3 — nothing left out at the top setting; leaving out only as an effort setting.** L2-S42 would
read: "At the top effort setting L2 withholds no span-rival from publication. Below it, an effort setting may
set a weight threshold: a span-rival below it may be withheld only because it is recomputable, and the
threshold and the withheld weight per span are published with the rivals. The ranked list of whole readings
is always bounded, and its length is an effort setting."

- *Towards the objective:* the same as both others at the top setting.
- *Towards the principles:* the top setting carries the amendment, D-006, D-425, D-295 and your word on the
  display; a lower setting keeps L2-S42's safeguards (recomputable, threshold and withheld weight shown, #12),
  and it is a setting you turn rather than a value fixed in the design, which is D-035 and your sizing word.
  D-200 is kept: nothing obliges a lower setting to be built before size proves a problem. *My reading:* the
  amendment's ground — a cut-off with "no basis" — does not reach a setting you choose yourself, though its
  literal words "anywhere in the publication" would be met only at the top setting.
- *Meta level:* the analysis's own specification only.

**Recommendation: Position 3.** It keeps everything your standing texts ask for as the default, puts the
derived safeguards on any reduction, and makes the reduction your setting rather than a constant. **The
strongest argument against it:** it adds an effort setting whose only saving is output size, which has not
been shown to matter; Position 2 is simpler, and a setting could be added later if size ever proves a
problem.

### 5. The rows, and how they follow

The words used: **carried** = the new specification already says this; **quarantined** = the old text
describes how a built program works, so it goes to the later audit as a question; **historical** = a rule or
plan replaced; **unplaced** = the comparison could not place it, and it is yours to place.

**In every position, following from the vocabulary — the comparison's proposals unchanged, recorded as this
side's derivation, not asked:**

- **L2-S42, carried (7):** Rows 5.231, 8.47, 9.361(ii), 21.72(ii), 44.74(ii), 47.17(iii), 49.23(ii) — each
  says uncertainty is carried, a ruled-out reading is information, a recomputable collapse loses nothing,
  nothing computed is narrowed or discarded at a boundary, or a display that asks for left-out rivals is a
  consumer's design.
- **L2-S42, quarantined (8):** Row 17.5(ii) (whether the shipped program's fitted values can drift); Rows
  3.20, 5.319, 6.192(ii), 23.2, 39.16(i), 39.336, 44.34 — the old and dormant engines' caps (top three, top
  four, a fixed top number), each with the comparison's audit question.
- **L2-S41, carried (6):** Rows 3.35, 3.36, 8.61, 21.35(ii), 43.51, 47.22(iii); **quarantined (2):** Rows
  6.123, 6.193 (the dormant engine leaving a carried rival's seventh unknown).
- **Row 8.59** — D-381's cap on distinct chord roots — **travels with Row 8.58** to the L2-S35/L2-S40
  family, where the comparison ties it (whether rivals are counted by chord root at all is that family's).

**Placed by your ruling (4 rows, unplaced in the comparison, which the vocabulary says you place):**

- Row 49.23(i) (your amendment), Row 8.48(ii) and Row 8.60 (D-380 and D-381: ruled-out roots carried at low
  confidence). **Position 1:** all three historical, replaced rules. **Positions 2 and 3:** all three
  adopted — proposed, carried by the amended L2-S42.
- Row 6.190 claim (ii) — D-331's "never pruned", which that text records as verified at the dormant chord
  engine. **Proposed quarantined in every position** (*my reading*: it states a property of a built
  program, like its neighbours that the silence ruling and today's first confirmation set placed so).

**Arithmetic:** 7 + 8 + 1 + 4 = 20 for L2-S42 (8 agreeing, 12 differing, *checked* at §7); 6 + 2 = 8 for
L2-S41. 28 in all.

### 6. What this surface does not do

It writes no dispatch, edits no tracked document, rules nothing, and allocates no register number. It does
not decide L2-S35, L2-S40 or L2-S45, what a weight means, how long the whole-reading list is, or any default
of an effort setting (D-202 stays deferred). The register status of D-006, D-331, D-380, D-381 and D-425 is
settled at the ratification act, as for D-383 in the fit family.

### 7. Read this sitting

The boot reads; entry 293, its surface and record whole; the derivation at L2-S35 to L2-S46 and OQ-L2-14,
-15; the comparison file at §5, §7 for the five statements, and §6 at every row named in §5 here plus Rows
8.39, 8.41, 8.58, 39.331, 47.23, 49.22, 49.24 and 49.25 (and neighbouring rows in passing); the route,
silence and fit ruling records whole; the sizing whole; D-006, D-008, D-098 and D-114's opening (group A), D-099, D-297 (group C), D-331, D-380, D-381 (group G), D-425 (group B), D-295
(group J) at their group files. **Not read:** `FRAMEWORK.md`; D-035, D-200 and D-275 at their group files
(D-035 from the register's index line, D-200 from `CLAUDE.md`, D-275 as the derivation cites it); the rows of
L2-S35, L2-S40 and L2-S45 beyond those named.

## §B. The check, run in the turn after "continue"

Over completeness, coherence, correctness and absolutes, at the staged sources. **Nine corrections, each
made at its site; former wordings kept here (#12).** One moves a row from the derivation to the question;
none moves the cut, a position or the recommendation.

1. §5, *former:* Row 6.190(ii) listed under "In every position, following from the vocabulary — recorded as
   this side's derivation, not asked", as "quarantined in every position". **Wrong in kind:** the comparison
   left that row UNPLACED, and its vocabulary says an unplaced row "is a row the user places"; today's first
   confirmation set put its two unplaced rows to you for that reason. Moved to the rows placed by your
   ruling, still proposed quarantined; *former* heading "Placed by your ruling (3 rows …)" and arithmetic
   "7 + 8 + 1 + 1 + 3 = 20" changed to 4 rows and "7 + 8 + 1 + 4 = 20".
2. §5, *former:* the seven carried rows "each says uncertainty is carried, a ruled-out reading is
   information, or a recomputable collapse loses nothing". Rows 47.17(iii), 49.23(ii) and 44.74(ii) say other
   things. Completed, and the list marked as the comparison's proposals unchanged.
3. §3 item 1, *former:* "so the list can never be complete; the search works out only the best few". An
   absolute wider than the arithmetic (a one-stretch passage is a finite list), and "only the best few" an
   untagged reading. Narrowed and tagged.
4. §3 item 1, *former:* "L2-S41's own stated fallback". The derivation calls it L2-S41's false-negative path;
   its words now quoted.
5. §3 item 2, *former:* "**Withholding changes no answer.**" The next layer and the display do receive less.
   Narrowed to this layer's answer, the smaller output stated.
6. §4 Position 1, *former:* "a value "measured against what the consumers read" has no consumer yet to
   measure". An absolute on an unexamined fact; narrowed to the consumers being unspecified for the new
   layer, tagged.
7. §4 Position 2, *former:* "(the size of the output is a cost)". My reading of D-035's reach; tagged.
8. §2, completeness: the amendment's date comes from Row 49.22's quotation of the same §3.3 amendment, not
   from Row 49.23 itself. Stated.
9. §3 item 3, *former:* "clear and easy entry points". Your words carry quotation marks around "entry points";
   restored. And §7, completeness: Rows 49.22, 49.24, 49.25 were read and are now named; D-114 was read at its
   opening only, now said.

**Checked and standing:** the 245, 174 and 43 row-part counts against §7 (L2-S35 3 + 54, L2-S40 52 + 65,
L2-S41 6 + 2, L2-S42 8 + 12, L2-S45 19 + 24); every quotation of L2-S42, L2-S41, OQ-L2-15, principle #12,
D-006, D-099, D-297, D-295, D-331, D-380, D-381, D-425, D-035's index line, D-200's heading and Row 49.23;
the 60,000 to 12 million labels and the sizing's 24-key current engine; every row number in §5 against its
proposal at §6; the arithmetic 20 and 28.

**What this check did not do:** read `FRAMEWORK.md`, D-035, D-200 or D-275 at their group files, or any row
of L2-S35, L2-S40 or L2-S45 beyond those named.

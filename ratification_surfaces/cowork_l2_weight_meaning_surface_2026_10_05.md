# What a weight means — the family on the meaning of the rivals' weights — 2026-10-05

> STATUS: DECISION SURFACE, NOT RULED. No question on it has been put. Written by the Cowork sitting that
> booted on `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_ninety_four.md`. Tags: *checked* =
> read at the source this sitting; *relayed* = taken from a record and not re-read at its source; *my
> reading* = my inference. §A is the surface as delivered.

## §A. The surface

### 1. What this is about, and the cut

The chord-and-key layer (L2) decides together, over the music loaded for the selection, the key of each
stretch, where one harmony gives way to the next, which notes are chord notes and which are passing notes,
suspensions and so on, and the chord over each stretch. One complete answer of that kind is a **reading**.
Beside its chosen reading the layer publishes **rival readings, each with a weight** (the derivation's word
is *mass*). This family decides **what that weight is**.

The two derived statements, whole (*checked*, `cowork_blind_derivation_l2_2026_09_27.md`):

- **L2-S35:** "The candidate score is normalised over whole readings: the masses of all readings of the
  working span sum to one. No span's alternatives are normalised against each other alone."
- **L2-S40:** "*Mass* is the probability the fitted, whole-reading-normalised model (L2-S35) assigns. A
  span-rival's mass is the marginal: the total mass of all whole readings that contain that span, with that
  start, that end and that reading of it. Until a reliability map is fitted, mass is a model quantity and not
  a calibrated probability. A consumer may compare masses within one working span's publication and may not
  read them as frequencies of being right."

In plain words: every complete reading of the selection gets a share of one whole; the weight of a rival
for one stretch is the sum of the shares of all complete readings that read that stretch that way; the
weights are the model's own and say nothing yet about how often the analysis is right.

**The cut.** Entry 294 names L2-S35 and L2-S40 (174 parts of rows at §7 of the comparison file: L2-S35 3
agreeing and 54 differing; L2-S40 52 agreeing and 65 differing, *checked*), the derivation's open question
**OQ-L2-14** (how the weight is named against your rule on confidence kinds, D-267), and Row 8.59, which
the rival-publication ruling sent here with Row 8.58. I take all of it and cut nothing. L2-S45 (what
crosses to the next layer) follows as its own family. Four rows this family places also name L2-S45 (Rows
17.16, 17.26, 17.58 claim (i), 49.22 claim (i)); placing them here settles them for that family too.
Row 8.41, which entry 294 also names as travelling, is one of L2-S40's own rows and is placed at §6 as the
comparison proposes it (quarantined).

### 2. What the record already settles, so nothing here is asked

**2.1 L2-S35 stands.** If each stretch's alternatives were normalised among themselves, later music could
change which reading wins but not how much weight flows to it (the derivation's defense, relaying Lafferty,
McCallum and Pereira, with the charter's ground). Your ratified decision on the uncertainty surface, D-425 (LIVE), chose exactly this: "per-span/
state marginal mass from exact forward-backward over the decode lattice, published as model probabilities
with their establishment status attached (model-internal quantities, NOT calibrated real-world confidences
until a #20-gated calibration is ever measured)" (*checked*, `cowork_notation_adoption_increment.md` §4,
the option D-425 adopts). The framework's rival set, whose members "need not share a segmentation", needs
weights comparable across different cuttings of the music, which a whole-reading share gives
(*checked*, `FRAMEWORK.md` §7; the last step *my reading*).

**2.2 L2-S40's substance stands.** The weight is the share described above, not a calibrated probability:
D-267 says "Until fitted, no layer may claim Class P" (*checked*), and D-425's words above say the same.
What stays open is only **what kind of quantity it is declared to be** — Decision 1.

**2.3 The weights are computed exactly at the top effort setting** (the sizing's Limit 1, *checked*:
"A safe bound protects the principal reading, not the masses"). The tractability ruling lets the search drop
a reading "only by a bound that provably cannot discard a reading that could win" (*checked*, its Ruling 1).
A reading dropped that way still had weight. D-425 says the weights come from "exact forward-backward over
the decode lattice" — a sum over every reading, not over the ones the search kept (*my reading* of
"the decode lattice"). So: a safe bound may speed
the search for the chosen reading; the weights come from the full sum; any approximation of the weights below
the top setting is an effort setting, declared, as the rival-publication ruling already rules for withholding
(*my reading* of the three texts together). The cost of the full sum is about twice the search's (the
sizing's own estimate, *checked* there as its estimate).

**2.4 D-008** (its register title: "The true probabilities are deferred to a later step"; its words: "GROUP
(ii) forward-backward marginals are NOT delivered here — OI-193's later step"; DEFERRED, *checked*) defers building
those sums in the current engine; L2-S40 specifies them. Its register status is settled at the ratification
act, as for D-383.

**2.5 A finding, recorded and not asked: the chosen reading need not carry the greatest weight at every
stretch.** The chosen reading is the best complete reading (L2-S18, for the applied-chord case: "decided by
the candidate score over the whole sequence" — its reach to every case is *my reading*; D-114, "The decoder commits its best path", LIVE, index line *checked*). The weight of a
stretch's reading is a sum over complete readings. *My example:* three complete readings with shares 0.40,
0.30 and 0.30; the first reads one stretch as X, the other two as Y. The chosen reading is the first; at that
stretch X carries 0.40 and Y carries 0.60. The framework's behavioural statement **B6** reads: "Where rivals
are published, the committed reading is among them and carries the greatest mass" (*checked*, §10.2). At the
level of complete readings B6 holds (tied readings sharing the greatest weight); per stretch it can fail. **Why this is not a question:** Ruling 2
of 2026-08-29 ratified "the layer decomposition, the charters and the boundary contracts" and, by name, the
behavioural statement B7 — not B6 (*checked*); D-114 and D-425 are ratified. So the specification follows
D-114 and D-425; B6's wording is carried **UNSETTLED** to the framework's text at the review of all
specifications together at the end of this phase (the detail-phase opening's Ruling 2 item 6, *relayed* from
the route record). Where a rival outweighs the chosen reading at a stretch, a consumer can see it, at the top
effort setting, from what is published; nothing extra is published (*my reading*).

**2.6 The old "forward override" (D-339)** has no place in L2 on the record's own terms — but its thirty
rows are UNPLACED, so they are yours to place; it is put as a confirmation at §5.1.

### 3. Decision 1 — what kind of quantity the weight is declared to be (OQ-L2-14)

**The rule it meets.** D-267 (LIVE, ratified 2026-07-02, *checked* at its home) allows "exactly one" of two
kinds for every published confidence: **Class M, decision margin** — "How much better is the chosen reading
than the best *different* reading, under this layer's own scoring?", "a rank statement, not a probability",
"published only squashed to [0,1] by a fixed monotone map"; and **Class P, calibrated probability** — not
claimable until a reliability map is fitted. The framework repeats it: every confidence crossing a layer
boundary "is declared to be either a ranking margin or a calibrated probability" (§7 and B9, *checked*).

**Why it does not fit.** A rival's weight is a share of a whole, not "how much better" one reading is than
another, and it is not produced by a fixed map of one number — it moves when any other reading's score moves
(*my reading*). It is not Class P either. D-425, ratified on 2026-07-26, after D-267 (2026-07-02), calls the same quantity
"model probabilities … NOT calibrated", and lists as a cost: "Model probabilities invite over-reading: the
#19 guard (status on the surface; no consumer load-bears on calibration) must be explicit in the contract"
(*checked*). No later amendment of D-267 was found in the contract file (*checked*, read whole). And the
framework says "Every published fact carries its own mass" (*checked*, §5), so the answer will also bind
the next layer's facts.

**Position A — declare the weight a decision margin (Class M), as the derivation leans** ("within that class
it behaves as a margin for the purpose of D-267", L2-S40's defense).
- *Towards the objective:* no change to any reading.
- *Towards the principles:* nothing amended. But the specification would state something untrue of the
  thing (#10: a specification as true as possible), and D-267's rule U3 would then let a consumer compare a
  weight, inside a declared frame, with true margins from other parts of the analysis — the over-reading
  D-425 warned of (*my reading*).
- *Meta level:* the analysis's own specification only.

**Position B — name a third kind in the confidence contract:** *the model's own distribution* — each value a
share in [0,1], the shares of one stretch's rivals summing to at most one, not calibrated, compared only
within one working span's publication, never read as a frequency of being right, and turned into a calibrated
probability only through a fitted reliability map. Amends D-267 (a third kind beside M and P) and the wording
of FRAMEWORK §7's confidence sentence and B9.
- *Towards the objective:* no change to any reading; a consumer is told in the contract that a weight is
  neither a margin nor a calibrated value.
- *Towards the principles:* #10 (the name is true); carries D-425's ratified words and does what D-425 said
  the contract owed; U1 to U5 unchanged. Against it: it amends a ratified cross-cutting contract and two
  framework sentences from inside one layer's family — the same kind of step the pivot ruling declined for
  L3's charter ("out of the route's order"). The two framework sentences are not among the parts Ruling 2
  named (*checked*); D-267 is ratified.
- *Meta level:* the specification and the cross-cutting confidence contract.

**Position C — leave D-267 as it is and add a true margin.** Publish, per stretch, beside the weights, how
much better the best complete reading is than the best complete reading forced to read that stretch
differently — the definition you ruled for the old key layer (D-349, LIVE, marked as concerning the dormant
pipeline: "how much better the winning sequence is than the best different-key sequence at that slice",
*checked*), which the contract's own table calls "The right definition (whole-sequence, not local top-2)"
(*checked*, §3). That margin becomes the stretch's declared confidence (Class M); the weights are declared
"mass", not a confidence.
- *Towards the objective:* one more fact per stretch — how decisively the best reading beat its strongest
  rival reading of that stretch, which the weights do not show (*my reading*).
- *Towards the principles:* D-267 untouched and D-349's principle carried. Against it: two numbers for one
  decision (#6; U1 attaches a confidence to a named decision, and two on one decision is a risk of
  confusion — *my reading*); a second computation over the readings, its
  cost not sized; and "a weight is not a confidence" is itself a new reading of FRAMEWORK §7 and B9 that
  you would have to make.
- *Meta level:* the analysis's own specification.

**Position D — state the substance in L2 and leave the naming to the end-of-phase review of all
specifications together**, recorded UNSETTLED.
- *Towards the objective:* no effect now; no consumer is built.
- *Towards the principles:* no cross-cutting text amended from one layer. Against it: L2 would be ratified
  knowing its weights match neither admissible kind (#10), and the same question returns for the next
  layer's facts, which also carry mass.
- *Meta level:* none now.

**Recommendation: Position B.** It names the thing truly, once, in the cross-layer contract, in the words of
the option you ratified with D-425, and it does what that option itself said the contract owed. **The strongest argument
against it:** it changes a cross-cutting contract from inside one layer's family before the other layers that
publish weights are derived; Position D would make the same change once, with all of them in view.

### 4. Decision 2 — whether a lowered effort setting may hide a whole chord root

**Background.** The rival-publication ruling (*checked*): at the top effort setting nothing is withheld;
below it a cut-off on weight, deeper or shallower by setting, may withhold a recomputable rival, the cut-off
and the withheld weight per stretch published. Two of your earlier texts, written for the old chord engine's
list of alternatives:
- **D-380** (LIVE, *checked*): "carry every above-threshold distinct root, each at its graded confidence;
  carry ruled-out roots at low confidence rather than dropping them" — measured there: "a ≥3rd distinct root
  clears threshold on 25.1 % / 16.1 % / 24.9 % of slices".
- **D-381** (DEFERRED, *checked*): a cap that counts voicings can be used up by the inversions and variants
  of the top two roots before a third root is reached; the carry must "preserve distinct roots explicitly,
  not as a by-product of a voicing cap".

The rival-publication ruling already adopted the second half of D-380 and D-381's matching sentence
(ruled-out roots kept at low weight, Rows 8.48(ii) and 8.60). Left open: Row 8.48(i) (every root above the bar carried), Row 9.330 (the same, restated), Rows 8.58,
9.331(ii) and 8.59 (the guarantee by root).

**The case, in musical terms** (*my reading*). Below the top setting the cut-off is applied to each rival
reading separately. A chord root whose total weight at a slice is well above the cut-off can be spread over
many readings — different inversions, sevenths, applied targets, or the same chord read in two keys — each
of them below the cut-off. Then that root disappears from the publication entirely; the withheld weight shows
that something is missing, not which root.

**Position A — the cut-off counts readings only, as ruled.** The five rows HISTORICAL (designs for the old
engine's carry).
- *Towards the objective:* nothing is lost at the top setting; below it, the case above can hide a root.
- *Towards the principles:* the simplest rule (#6); D-200: no lowered setting need ever be built until size
  proves a problem, so the case may never arise.
- *Meta level:* the analysis's own specification only.

**Position B — at any slice, a cut-off never removes every reading of a chord root whose readings there
together carry weight above the cut-off; that root's best reading is kept.** The five rows ADOPTED —
proposed, as one added sentence of the amended L2-S42. The grouping by root is internal to L2 (the root is
the degree read in its key); nothing extra is published.
- *Towards the objective:* the chord root is what your regression stop counts ("root governs", D-115, index
  line *checked*); at every setting the display and the next layer still see every root with real support.
- *Towards the principles:* #12 (a cut-off may not hide a whole root); completes D-380 and D-381's purpose,
  half of which you already adopted.
- *Meta level:* the analysis's own specification only.

**Recommendation: Position B.** **The strongest argument against it:** the 16 to 25 per cent figures were
measured on the old engine; whether weight spreads that way under the new layer is unmeasured, and the rule
guards a setting that may never be built.

### 5. Confirmations — rows the comparison left UNPLACED, which you place

**5.1 The forward override (D-339) has no site in L2 — twenty-nine rows HISTORICAL, one QUARANTINED.**
D-339 (LIVE, *checked*): "A confident earlier inference can be overturned by decisive later evidence, via one
general confidence-weighted forward-recompute mechanism", its two instances the old function layer's
"modulation recompute" (a cadence overturning the key layer's key) and its "fine-grain chord override". **Inside L2** there is no earlier decision to overturn: key, boundaries,
notes' roles and chord are one decision scored over the whole loaded music (the charter; L2-S35). **At L2's
boundary** the contract table reads "L3 → L2: **Nothing.** … A read-off fact may not revise the decision it
was read off" (*checked*), and L3 "publishes the contradiction as its own fact and does not act on it" (§6.8,
*checked*). The framework does not forbid the act in general (§8.4, Δ8, *checked*); this says only that L2
has no site for it. **Row 6.190 claim (iii), QUARANTINED** — it states, as verified at the dormant chord
engine, that the function layer overrides by selecting among that engine's carried readings; its neighbours
(ii) and (iv) are quarantined; audit question: does the dormant function layer override only by selecting
among the chord engine's carried readings? **The other twenty-nine, HISTORICAL — a rule of that mechanism:**
5.218(ii), 5.222, 5.223, 5.224, 5.225, 5.228(ii), 5.250(ii), 5.251, 5.255(i), 5.315, 6.188, 7.30, 18.1(ii), 21.33(ii), 21.36, 21.45(i),
22.98(iii), 43.55, 43.56, 43.57, 43.58, 43.60, 43.61(ii), 43.62, 43.63(ii), 44.63(i), 44.66(ii), 44.71(iv),
53.30. The register status of D-339 (and of D-509, whose Row 53.30 is here) is settled at the ratification
act, as for D-383.

**5.2 The other unplaced rows.**
- **The "open mark" rows, QUARANTINED with Row 5.153**, which you placed so earlier today (the no-early-discarding ruling): Rows 5.155,
  5.205(iii), 5.233, 5.270, 5.296 — the old function layer's mark for an undecided case; audit question as at
  Row 5.153. Ground: the silence family's Ruling 1 (doubt shown by the weights alone, no "uncertain" flag).
- **Row 7.109, HISTORICAL** — the old key layer's chosen design "Commit where sure, mark 'uncertain' where
  not", overtaken by the same ruling; the treatment you gave Row 7.110.
- **Rows 7.5(i), 52.11(i), 7.112(i), HISTORICAL** — the old key layer's declared confidence, the sequence
  margin (D-L3a, D-349), overtaken by D-425's full spread of weight. *If Decision 1 takes Position C, these
  three become ADOPTED — proposed instead.*

### 6. The rows that follow from the vocabulary — the comparison's proposals unchanged, recorded as this side's derivation, not asked

- **L2-S35, carried (3):** Rows 2.8, 5.250(i), 21.32(i).
- **L2-S35, quarantined (23)** — the old engines' change of key on a cadence and chord override, each with
  the comparison's audit question: Rows 4.3(i), 5.16, 5.61, 5.69(i), 5.138, 5.139, 5.140, 5.158, 5.159,
  5.200(ii), 5.203, 6.11, 8.17, 8.79, 8.83(i), 8.163, 9.25, 9.333, 9.390, 39.269, 52.17, 52.18, 53.8.
- **L2-S35, historical (1):** Row 18.2(ii).
- **L2-S40, carried (37):** Rows 6.127(i), 6.131(i), 6.190(i), 7.13(ii), 7.15(i), 7.33(i), 7.35(ii), 7.88(ii),
  7.97(ii), 7.100(i), 7.112(ii), 7.152(i), 8.45, 8.91, 8.139, 8.143, 10.53, 12.29(ii), 13.13, 21.18(i), 21.20,
  44.38, 44.47(i), 44.51(ii), 47.8, 47.19, 47.21, 47.22(i), 47.22(ii), 47.23(i), 47.24(ii), 49.3, 49.5, 49.25,
  49.26, 62.48(i), 62.48(ii) (the last two carried by L2-S15).
- **L2-S40, relocated to *the uncertainty surface* (17)** — the confidence contract's own rules: Rows
  5.213(ii), 5.218(i), 6.127(iii), 9.22, 9.23, 9.149, 21.47, 21.69, 41.92(i), 52.1, 52.2, 52.4, 52.5, 52.7,
  52.24, 52.29, 52.31.
- **L2-S40, quarantined (46)** — the old engines' confidences, uncertain marks and root-keyed carries, and the
  current engine's published candidate lists and gaps (Rows 17.16 to 17.58(i), 49.4, 49.22(i), 49.40), each
  with its audit question: Rows 5.51, 5.205(ii), 5.212, 5.214, 5.295, 6.17, 6.22(iv), 6.121(iv), 6.126,
  6.127(ii), 6.173, 6.192(i), 7.13(i), 7.13(iii), 7.14, 7.23, 7.28, 7.35(iii), 7.35(iv), 7.51, 7.88(iii),
  7.88(iv), 7.92(ii), 7.97(iii), 7.97(iv), 7.153, 7.154, 8.41, 8.42, 8.86, 8.87, 8.131, 8.132, 9.324,
  9.331(i), 9.334, 17.16, 17.18(i), 17.26, 17.50(ii), 17.58(i), 21.18(ii), 23.199, 49.4, 49.22(i), 49.40.
- **L2-S40, historical (1):** Row 2.6.
- **Travelling, not placed here (2):** Row 8.68(ii) with Row 8.155 to L2-S45's family (the no-early-discarding
  record); Row 8.69 with Row 8.68(i) to L2-S11's family.
- **Already placed (1):** Row 5.153 (QUARANTINED by the no-early-discarding ruling).

### 7. Arithmetic

L2-S35: 3 agreeing (3 carried) and 54 differing (23 quarantined, 1 historical, 30 yours at §5.1) — 57.
L2-S40: 52 agreeing (37 carried, 14 relocated, 1 travelling) and 65 differing (46 quarantined, 1 historical,
3 relocated, 1 already placed, 1 travelling, 13 yours: 5 + 1 + 3 at §5.2 and 4 at Decision 2) — 117.
With Row 8.59: 175 row-parts, of which 128 follow from the vocabulary, 3 travel or are already placed, and 44
are yours (30 at §5.1, 9 at §5.2, 5 at Decision 2).

### 8. What this surface does not do

It writes no dispatch, edits no tracked document, rules nothing, amends no contract or framework text, and
allocates no register number. It does not decide L2-S45, OQ-L2-6, any cut-off value or default (D-202 stays
deferred), or B6's wording (§2.5, carried). The register status of D-008, D-339, D-349, D-380, D-381 and D-509
is settled at the ratification act.

### 9. Read this sitting

The boot reads (`CLAUDE.md` at its six spans, `DECISIONS.md`, `STATUS.md`, the gating answer, entries 118,
152, 169 and 291 to 294 whole); the rival-publication surface and record whole; the derivation at §0 to §2,
L2-S31 to L2-S49, §4 and §5; the comparison file at §1 to §5, §7 whole, and §6 at every row
of this family and the neighbours on the same screens; D-008, D-267, D-268, D-339, D-349, D-380, D-381, D-425
at their group files; the confidence contract whole; `cowork_notation_adoption_increment.md` §4;
`FRAMEWORK.md` at §0, §5 (L2, NOT A LAYER, the contracts), §6, §7, §8, §10.2 B5–B9, R-3, Δ8 and the banner;
the sizing §5; the route, silence, no-early-discarding, pivot and fit records whole, the tractability record at
§0 and Ruling 1, the tonality record's placements; Ruling 2 of 2026-08-29. **Not read:** D-114, D-115, D-509
at their group files (index lines only); the detail-phase opening record; the L0/L1 files; the exemplars.

## §B. The check, run in the turn after "continue"

Over completeness, coherence, correctness and absolutes, at the staged sources. **Fourteen corrections, each
made at its site; former wordings kept here (#12).** One moves a row's proposed placement (Row 6.190(iii));
none moves a position, a recommendation or the arithmetic's totals.

1. §5.1, *former:* Row 6.190(iii) among the rows proposed "HISTORICAL — a rule of that mechanism", heading
   "thirty rows HISTORICAL". **Wrong in kind:** the claim states, as "VERIFIED at source", how the dormant
   engines work, and its neighbours (ii) and (iv) are quarantined. Now proposed QUARANTINED with an audit
   question; heading "twenty-nine rows HISTORICAL, one QUARANTINED".
2. §5.1, *former:* D-339's instances "the old key layer's change of key on a cadence and the old chord
   override". The modulation recompute is the old function layer's, overturning the key layer's key. Corrected
   with D-339's own names.
3. §3 Position C, *former:* "U1 ties one confidence to one named decision". U1 says a confidence "attaches to
   a named decision" and nothing about one per decision. Narrowed and tagged.
4. §4, *former:* D-381 "so a third root survives only 'as a by-product'". A quotation of words D-381 uses in
   the opposite construction; replaced by its own sentence.
5. §4, *former:* "already adopted the second half of D-380 (… Rows 8.48(ii), 8.60)". Row 8.60 is D-381's;
   corrected.
6. §4 recommendation, *former:* "the quarter-of-slices figure". The figures are 25.1, 16.1 and 24.9 per cent;
   restated.
7. §2.1, *former:* "which only a whole-reading share gives". An absolute: Position C's margin would also be
   comparable across cuttings. "only" struck.
8. §2.1, *former:* "relaying Lafferty and others". The others named.
9. §2.3, completeness: "a sum over every reading" rests on my reading of "the decode lattice"; tagged.
10. §2.4, *former:* D-008 quoted by its register title as if its words; both now given and labelled.
11. §2.5, *former:* L2-S18 quoted as the general rule for the chosen reading. It is written for the
    applied-chord case; its reach is tagged as my reading. And *former:* "B6 always holds" at the level of
    complete readings — ties noted. And *former:* "any consumer can see it" — true at the top setting only;
    narrowed.
12. §3 Position B, *former:* "no consumer can mistake a weight for a margin or a calibrated value"; Position D,
    *former:* "returns for every later layer's facts"; recommendation, *former:* "in the contract every layer
    reads, in words you already ratified (D-425)". Absolutes or loose attributions; narrowed (the words are
    those of the option D-425 adopted).
13. §1, completeness: entry 294 names Row 8.41 as travelling; it is one of L2-S40's own rows and is now said
    to be placed at §6 as proposed.
14. §6 and §9, correctness: the quarantined list was described as "the old engines'" though Rows 17.16 to
    49.40 describe the current engine; and §9 overstated or understated reads (entries 118 and 152 were read
    whole; the derivation also at §0 to §2; the tractability record only at §0 and Ruling 1; D-099 not read at
    all). Corrected.

**Checked and standing:** every quotation of L2-S35, L2-S40, D-267, D-339, D-349, D-380, D-425's option, the
contract's §3 table, `FRAMEWORK.md` §5, §6.8, §7, B6, B9, Ruling 2 of 2026-08-29, the tractability Ruling 1
and the sizing's Limit 1; the 174 row-parts and each row's verdict and proposal against §6 and §7; the
example's arithmetic; the totals 57, 117, 175, 128, 3 and 44.

**Declared departure:** two shell commands were run in error during this check — `echo` and then `true`, in
the container, the second right after the first had been declared; neither read nor wrote anything and no
claim rests on them.

**What this check did not do:** read D-114, D-115 or D-509 at their group files, the detail-phase opening
record, or any row beyond this family's and its neighbours.

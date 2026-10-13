# Music beyond the selection, and when L2 stops asking for more — L2-S22 — ratification surface, 2026-10-07

> **STATUS: RATIFICATION SURFACE, §A AND ITS CHECK §B.** *(Former wording, preserved (#12): "§A ONLY".)* Cowork, 2026-10-07 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_eighteen.md`. Written as text, nothing asked in
> the turn that delivers it. The check (§B) comes in a later turn, and the questions after that, one per turn.
> Nothing here is applied, and no tracked document but this one is written. Marks: *checked* = read at the object
> by this sitting; *relayed* = taken from another record and not re-read here; *my reading* = this side's
> interpretation.

---

## §A.1 The statement, whole, and what it means

From `cowork_blind_derivation_l2_2026_09_27.md`, its lines 575–597 (*checked*):

> **L2-S22. At the edge of the working span, L2's tonality (and the rest of its reading) depends on
> music before and after the span. L2 is the layer that asks for more music. It stops asking when its
> in-span publication stops changing between successive enlargements. What counts as "stops changing"
> for the masses of the rivals is open (OQ-L2-6).**
> - *Defense.* The output covers exactly the selection, and music beyond it is evidence [RULED — D-260].
>   A layer never guesses how much context it needs, and it extends until "the layer's in-selection
>   output stops changing" [RULED — D-261, clauses 3 to 6. **See §6: the same entry also carries an
>   as-built description, which this session saw and does not use.**]. On the input contract's side,
>   "the decision to enlarge, the increment and the stop test belong to the requester, never to L0 or
>   L1" [RULED — IC beside S-53, Ruling 46 (v)]. One settled indication does not fix the tonality at the
>   edge of the music being read, while a tonality established over a stretch of earlier music does [FACT
>   — ledger C43, the fact half]. The masses are real numbers, so "stops changing" needs a rule. Whether
>   the rule is identity of the principal reading, identity of the rival set, or a bound on the change in
>   mass is not derivable from the ruled words.
> - *Source class.* Given — design intent (D-260, D-261) and input contract (Ruling 46), for the
>   mechanism. Derived, for the point that the masses need their own rule.
> - *Status.* Settled for the mechanism. **Open** for the mass rule (OQ-L2-6).
> - *Premise.* Convergence happens within the score. **False-negative path:** a reading that never
>   converges, such as an oscillating pivot. The record edge (IC Ruling 46 (vi)) ends the loop, and the
>   record-edge mark says so.
> - *Falsifier.* CODE. **Observable:** the in-span publication after successive enlargements. **Decision
>   rule:** falsified if L2 stops while its principal in-span reading still changes, or if it asks L1 to
>   decide the increment. **Not falsified by:** a stop at the record edge.

And the open question it names, lines 1220–1222 (*checked*):

> **OQ-L2-6 (face (c), (h); L2-S22) — convergence of masses.** When L2 enlarges its context, what counts
> as its in-span publication "no longer changing": the principal reading only, the rival set, or the
> masses within a bound? D-261 says "in-selection output", and the masses are real numbers.

**In plain words.** The user selects some bars. L2 publishes its reading (tonality, chord, which notes are chord
tones) only for those bars — the *working span*. But the reading at the first and last bars of the selection can
depend on music outside it: the key the music was in just before the selection began, or the chord just after it
ends. So L2 asks for more music on either side, reads again over the larger stretch, and compares. When one more
enlargement no longer changes what it publishes for the selected bars, it stops. It never decides in advance how
much it needs. The beginning and end of the piece, and a safety limit, also stop it; neither of those is "the
amount it needed".

What is not settled is what "no longer changes" means. L2 does not publish one reading only: it publishes rival
readings, each with a *mass* (its share of the weight, L2-S40). Masses are numbers that may move a little with every
new bar, even when the best reading stays the same. So "stops changing" needs a rule: only the best reading must
stay the same? the list of rivals? the masses, to within some tolerance? That is OQ-L2-6.

## §A.2 What the record has already said

- **The register** (`decisions/group_C.md` and `decisions/group_F.md`, entries read whole, *checked*):
  - **D-260** (LIVE, ratified by you): the output covers exactly the selection; everything loaded beyond it is
    evidence, never a result.
  - **D-261** (LIVE, ratified by you), items 3 to 6 of the bounded-context contract: tell "not loaded" apart from
    "the piece starts or ends here"; output only for the selection; **never guess how much** — extend step by step,
    the amount discovered, not chosen; **the principled stop is convergence: extend until the layer's in-selection
    output stops changing**, applied "DIRECTLY, on the in-selection quantity the extension was requested for".
  - **D-622** (LIVE): the cheaper stop proposed in design ("a settled, stable prevailing key is in view") was
    measured false — one settled bar of context does not fix the key at the selection's edge, which flips only once
    a confident earlier key is established over a run — and dropped. On your ruling of 2026-08-07 the clause in
    D-261 that licensed **any** such stand-in ("a domain proxy that implies convergence") is struck as tried and
    closed, and the bounded-context design's own annotation says why the strike "reaches the general clause and not
    only its worked example" (`cowork_bounded_context_design.md` lines 73–90, *checked*).
  - **D-262** (the step size is the requesting layer's, "an efficiency knob only … never a different answer, because
    convergence (item 6) fixes the result"), **D-263** (a refused or truncated extension is marked on the output),
    **D-264** (any sequence of extensions equals one fresh run over the final loaded music), **D-624** (the hard
    bound and the start of the piece are safety caps for a loop that never settles, never the amount needed).
- **The tractability record of 2026-10-05**, Ruling 1 (ii) (read whole, *checked*): "the end" the search reads to
  is the end of the music loaded for the selection — the selection with its context, "the context extended by
  convergence (D-261) under the safety cap (D-624)". And: "What "stops changing" means for convergence (OQ-L2-6) is
  not decided" — and, at its §0, "open and another family's"; L2-S22 is the statement that names it. *(§B item 1;
  former wording, preserved (#12): "— left to this family." — the record does not name the family.)*
- **The rival-publication record of 2026-10-05**, Ruling 1 (read whole, *checked*): at the top effort setting L2
  withholds no span-rival; below it, the effort setting sets how deep the cut-off lies, **"continuous, not on/off:
  different effort settings cut off at different depths"** (your refinement). Cut-off values and defaults are
  decided when the effort setting is built (D-202 stays DEFERRED).
- **The sizing of 2026-10-05**, §C (*checked*): your word that the software must have "clear and easy entry points"
  for an effort setting, including to "restrict any temporal expansions beyond some limits"; the entry points it
  lists include "(c) the context extension's limit (D-261, under D-624's cap)"; "The top setting is exact, as L2-S36
  states." Rows 43.12 and 7.104(i) (old effort dials on candidate counts) were proposed there, as that sitting's
  reading ("he may place them otherwise"), as travelling with the effort setting's own design, not with L2's
  ratification. *(§B item 2; former wording, preserved (#12): "were recorded as travelling with" — a proposal, not
  a placement.)*
- **The no-early-discarding record of 2026-10-05**, §1b (*checked*): Row 45.52(i) carried under L2-S43; **Row 5.71**
  — the old function layer's "decision-context span", the bounded run of slices it decides within — QUARANTINED, as
  describing the dormant program.
- **The one-tonality-per-span record**, earlier today (*checked*): Row 5.72 claim (ii) carried under L2-S16. This
  family has claim (i).
- **The pivot-chord record of 2026-10-05** (*checked*): Row 45.21 named as L2-S22's family's; not placed there.

## §A.3 The rows — ninety-nine named by §7

§7 of `ratification_surfaces/cowork_comparison_l2_reading.md` lists for L2-S22 (lines 71154–71157, *checked*)
**78 AGREES and 21 DIFFERS**. Every one of the 99 row-parts was read at the comparison file (*checked*; member 45 —
`cowork_bounded_context_design.md` — read whole as tabulated, with its manifest and arithmetic). Members: 2 =
`ARCHITECTURE.md`, the Layer 3 section; 5 = `cowork_layer5_function_design.md`; 6 = `cowork_layer4_chordsymbol_design.md`;
7 = `cowork_layer3_keymode_design.md`; 21, 22, 23, 30 = `ARCHITECTURE.md` §2, §3, §4, §11; 42 =
`cowork_layer2_slicing_design.md`; 43 = `cowork_target_architecture.md`; 45 = `cowork_bounded_context_design.md`;
51 = `cowork_layer1_note_model_design.md`.

### Proposed ADOPTED — carried (L2-S22) (75), all AGREES

What they say, grouped by their content (each as the comparison proposes it):
- **The edge needs music from outside the selection, and L2 is the one that asks:** 2.16(i), 2.16(iii), 2.18(i),
  2.19, 5.74, 45.59(i), 6.52, 6.54, 6.55, 7.16, 7.59, 7.60, 7.61, 7.103(i), 7.155, 21.59(ii), 43.75(i), 43.76, 43.78, 45.3,
  45.32, 45.40, 45.54, 45.63, 45.84, 45.94(i), 51.15(ii), 51.21(i), 51.23(ii), 51.63, 45.69(ii).
- **The asking layer owns the decision to ask, the step and the stop:** 45.22(i), 45.25(i), 45.47(ii), 45.85.
- **Not loaded → ask; start or end of the piece → go on with what there is:** 6.53(i), 45.6, 45.7, 45.26(i),
  45.51, 45.53(i), 45.53(ii), 45.61(i), 45.65(ii), 45.67, 45.92(ii), 45.93(i), 45.93(ii).
- **Music outside the selection is evidence, never output:** 22.85(ii), 42.60, 43.77(ii), 45.9(ii), 45.49,
  45.52(ii), 45.64(ii), 45.83, 45.91(ii).
- **Never guess how much; extend step by step; stop on convergence:** 21.60(iii), 22.83(iii), 43.75(iii), 45.10,
  45.11(i), 45.11(ii), 45.12, 45.37(ii), 45.39.
- **The safety caps are not answers:** 2.13, 2.14(i), 2.15, 45.15(i), 45.15(ii), 45.21(ii), 45.21(iii).
- **The measured fact behind dropping the proxy** (one settled bar does not fix the edge; a run does): 2.48 (a row
  the deriving session did not see, marked WITHHELD — D-622), 45.19.

### Proposed QUARANTINED (2), AGREES — follow the proposal, not the axis (entry 314 §2)

- **2.49**: "So the facility uses the headline criterion directly and no proxy." *Audit question:* does the built
  facility stop on the headline criterion alone? (with 2.47(ii)).
- **45.20 claim (ii)**: item 5's rule "is what the as-built implements". QUARANTINED with 2.49.

### Proposed HISTORICAL (1), AGREES

- **23.255**: "the same winner survives repeated expansion" — a stop in an old plan (*Phase 1b — Minimal Monophonic
  Fallback*). HISTORICAL, a plan.

### Proposed QUARANTINED (13), DIFFERS — how the old and dormant programs reach back, and when they stop

- **2.10**: the backward re-reading facility "stays SWITCHED OFF in the shipped configuration" (WITHHELD — D-306).
  *Audit question:* is it off in the shipped configuration, and does anything on the production arm read before the
  start of the working span?
- **2.47 claim (ii)**: "the as-built tracks the leading-edge key itself and stops when that stops changing"
  (WITHHELD — D-622). *Audit question:* what does the built reach-back facility track, and what is its stop test?
  Travelling with it, directly or through Row 7.64: **7.64** (the built loop: trigger, action, stop "until the
  leading-edge **settled** key stops changing across iterations"), **7.89** and **7.95** (each travelling with Row
  7.64), **45.14** *(§B item 3; former wording, preserved (#12): "Travelling with it: **7.64** (…), **7.89**,
  **7.95**, **45.14**")* (D-261's as-built sentence, which the deriving session
  saw and did not use), **45.50**, **45.92(i)**, **51.21(ii)**, **51.52(i)**.
- **7.62**: the reach-back's direction, stop and hard bound — stop = *"the prevailing key before the selection is in
  view"*. Proposed QUARANTINED travelling with 7.64. *(See §A.5 point 3: this side proposes a change.)*
- **5.72 claim (i)**: the function layer's span "is bounded by a look-ahead window (≈ one punctuation-span's
  extent …)". *Audit question:* as at Row 5.71 — does the dormant function layer decide within a bounded
  decision-context span, and what bounds it?
- **30.75 claim (i)**: the Roman-numeral annotate path reads past the selection "by up to
  `kMaxPivotLookaheadRegions × 1 whole note`". QUARANTINED, travelling with Row 22.107 (as Row 30.72 travels, in the
  applied-or-new-tonality record).

### Proposed HISTORICAL (3), DIFFERS — an old plan's stopping tests

- **23.243** ("bounded local-context expansion only when confidence is weak"), **23.253** ("confidence crosses
  threshold"), **23.254** ("top-vs-second margin crosses threshold") — all *Phase 1b* plan text. HISTORICAL, a plan.

### UNPLACED (5), DIFFERS — the comparison left these to you

- **45.13 claim (i)** — D-261 item 6, inside the ruled text: "A layer applies that criterion DIRECTLY, on the
  in-selection quantity the extension was requested for: it re-infers over the enlarged span, compares that quantity
  step against step, and stops when it repeats." The comparer: "a disposition would choose between a ruled answer and
  a derived one".
- **5.73** — the function design, §5.0: "Its extent is PINNED (2026-07-02 …): the span extends forward until the
  FIRST of (i) a cadence-anchored function, (ii) a punctuation boundary …, (iii) the hard bound of `K` slices / `B`
  beats (settings, the safety cap)."
- **45.58** — the same pin in the bounded-context design, §5, Architectural Layer 5. Travels with 5.73.
- **45.59 claim (ii)** — the same layer's forward extension: "stop = any of (i)–(iii); increment = its natural
  unit, slices". Travels with 5.73.
- **45.55** — the old chord layer's trigger: "the request fires only when the truncation is decision-relevant —
  the decision under the truncated window is not already a full-margin `Commit` (a truncated window whose evidence
  sufficed requests nothing)."

**Arithmetic, as proposed.** AGREES 78 = 75 carried + 2 quarantined + 1 historical. DIFFERS 21 = 13 quarantined + 3
historical + 5 unplaced. 99 in all.

## §A.4 The search for rows already placed

The 30 ruling records of 2026-10-04 to 2026-10-07 and the 29 `cowork_l2_*` files then in `ratification_surfaces`
(28 surfaces and the sizing) *(§B item 4; former wording, preserved (#12): "the 28 `cowork_l2_*` files")* were
searched for "L2-S22", "OQ-L2-6", "converg" and each of this family's row numbers, and the travelling heads (Rows
5.71, 6.67, 7.10, 18.2, 22.107) (*checked*; every hit read at its line). **Hits on this family's own row-parts:
none places one.** Hits on other claims of the same rows or on travelling heads: Row 5.72(ii) carried (L2-S16);
Row 45.52(i) carried and Row 5.71 quarantined (no-early-discarding); Row 30.72 travelling with Row 22.107
(applied-or-new-tonality); Row 45.21(iv) and Row 30.75 named as this family's (pivot chord, surface lines 115–131 and
236–248); Rows 7.64, 45.13, 45.14, 45.50, 45.92 listed as "using the word in another sense" (working-order surface
line 156 — the word *repeat*); Rows 45.7 to 45.15 named as the rows the derivation's stop-on-meeting record reaches
(route record line 65). **No row-part of §A.3 is placed by any record searched.**

## §A.5 What this side found when reading the rows against each other

1. **Row 45.13(i) does not conflict with L2-S22 — my reading.** D-261 item 6 states the criterion first: "extend
   until the layer's **in-selection output** stops changing" (Row 45.12, AGREES, carried). Row 45.13(i) then says how
   it is applied: **directly** — on the thing itself, never through a stand-in — "on the in-selection quantity the
   extension was requested for". The word "directly" is the point of the sentence: the 2026-08-07 annotation that
   sits under it strikes the stand-in clause (D-622). In the old stack each layer asked for music for one thing (the
   key layer for the key at the selection's leading edge). **L2 asks for more music for its reading** — L2-S22's first
   sentence: "L2's tonality (and the rest of its reading) depends on music before and after the span". So for L2 the
   quantity the extension is asked for *is* its in-span publication, and L2-S22 is D-261 item 6 applied to a layer
   that decides tonality, chord and assignments together. A narrower test — watching only the tonality at the edge,
   as the old key layer did — could stop while L2's principal reading of the selection still changes away from the
   edge, which is what L2-S22's falsifier forbids *(§B item 5; former wording, preserved (#12): "while something else
   L2 publishes for the selection still changes" — the falsifier names the principal reading, not everything
   published)* ("falsified if L2 stops while its principal in-span reading still changes").
   So no real choice remains: **ADOPTED — carried (L2-S22)**, with this reading recorded beside the row.

2. **The old function layer's pinned look-ahead (Rows 5.73, 45.58, 45.59(ii)) has two jobs, and L2 does each
   otherwise.** *Job one — how much music one decision reads:* the old function layer decided cadence votes,
   resolutions and persistence slice by slice, each over a bounded "decision-context span". L2 has no such per-slice
   window: the reading is one decision over the whole loaded music (L2-S11, L2-S23), and "No reading is discarded
   before the whole working span, context included, has been scored" (L2-S43). The neighbouring Row 5.71 — the
   decision-context span itself — was already quarantined (no-early-discarding record). *Job two — when to stop
   extending forward:* "stop = any of (i)–(iii)", i.e. at the first cadence-fixed chord, the first picked phrase
   boundary, or a hard bound. For L2 the stop is convergence (D-261 item 6), the hard bound being D-624's safety
   cap. Stopping at "a cadence is in view" in place of testing whether the reading still changes is the kind of
   stand-in D-622's strike closes — its annotation says why "the strike reaches the general clause and not only its
   worked example" (*my reading*: the annotation names no layer other than the key layer's reach-back, and the
   bounded-context design's §5 bullet for Architectural Layer 5, lines 175–183, carries no annotation of the strike;
   so the outgoing document still carries this stop). *(§B item 6; former wording, preserved (#12): "closes "in the
   general clause and not only its worked example"" — not the source's words — and "was not edited when the strike
   was made — §A.2", a citation to a section that does not show it.)* **So
   these three rows are a dated rule of the superseded per-layer design, and HISTORICAL fits them** (the vocabulary's
   superseded plan; compare Row 45.30(ii), the old per-layer stepping units, proposed HISTORICAL with Row 18.2(i)).
   QUARANTINED would ask the audit whether the dormant function layer implements this pin; the acceptance list of the
   same design (Row 45.78, HISTORICAL) lists "L5's pinned extent + discovery rule" among the things still to be
   coded (*relayed* through the comparison), so the question may well come back "no" (*my reading*; not checked).
   *(§B item 7; former wording, preserved (#12): "would most likely come back "no"".)* *Is there reason to
   suspect that L2 loses precision by not carrying the pin?* The pin's purpose is to look "far enough to reach the
   cadence a few slices later". Convergence keeps asking while the reading changes, so if the cadence moves the
   reading, L2 reads on to it. The one way convergence could stop too early is if one step adds nothing and the
   decisive music lies beyond the next step (see point 5). A pinned cadence-or-phrase stop does not cure that in
   general — it would itself stop at the first cadence. *My reading*; no new open measurement is proposed beyond
   point 5's.
   **What survives of the pin's idea:** a forward limit at the next cadence or phrase end is a natural candidate for
   one of the effort setting's lower settings — your "restrict any temporal expansions beyond some limits" and the
   sizing's entry point (c). That is the effort setting's design (D-202, DEFERRED), not L2's top setting.

3. **Row 7.62's stop condition is the proxy D-622 dropped.** Its stop — "the prevailing key before the selection
   is in view" — is word for word the stop the bounded-context design struck at its §5 on your ruling of 2026-08-07,
   with its former wording kept ("the stop formerly read "the prevailing key before the selection is in view" — the
   proxy, not the criterion", lines 159–163, *checked*); D-261's provenance records the same correction at its §10
   (`decisions/group_C.md`, *checked*; §10 itself not opened). *(§B item 8; former wording, preserved (#12): "struck
   at its §5 and §10 … lines 159–163, *checked*" — the §10 half was not read at the document.)* The comparison proposes QUARANTINED travelling
   with Row 7.64 (the built loop). But Row 7.62 does not say how the built program works; it states a design's
   stopping rule that was measured false and dropped. **This side proposes HISTORICAL, travelling with Row
   2.47(i)** ("a proposal measured and dropped") and with Rows 45.16 to 45.18 (the tried-and-closed annotation),
   changed from the comparison's proposal. The audit question about the built loop is still asked through Row 7.64.

4. **Row 45.55 (ask only when the decision is not already a full-margin commit) is a way to save work, not a
   different reading.** *My reading:* skipping the request when the truncated reading already looks confident
   saves an enlargement at the cost of sometimes not seeing music that would change the reading — the same shape
   as the failure D-622 measured for a different stand-in ("a settled, stable prevailing key is in view"). *(§B item
   9; former wording, preserved (#12): "exactly the failure D-622 measured for a confidence-looking stand-in" — D-622
   measured another rule, not a margin trigger.)* And L2 has no "Commit" state to test: it shows its
   doubt by the masses alone (silence family, Ruling 1, *relayed* through the no-early-discarding record). At the top
   setting it is therefore not L2's rule. As a cheaper lower setting it belongs with the effort setting's design, as
   the sizing's §C sent Rows 43.12 and 7.104(i). **Proposal: not placed now; travels with the effort setting's
   design (D-202), its proposal recorded there** — the same treatment as Row 7.104(i).

5. **A risk the record already guards, recorded rather than raised.** Convergence "between successive enlargements"
   could stop too early if one step adds music that changes nothing while the decisive music lies one step further
   — D-622's measurement is a case of that shape for a stand-in (one settled bar did not fix the key at the edge; a
   confident key over a run, "a V–I two measures back, say", did). D-262 says the step size is "never a different
   answer", which, on *my reading*, holds only if this does not happen. *(§B item 10; former wording, preserved (#12):
   "(one settled bar changed nothing; a run two bars back flipped the key)" — a gloss wider than D-622's words — and
   "which is true only if this never happens", unmarked as a reading.)* The record's guard is the requirement that the result not depend on the step size: D-264 (any sequence
   of extensions equals one fresh run) and Rows 45.71 (carried, L2-S48), 45.24 (proposed: L2's publication not depend
   on the step), 45.72 ("A required test", RELOCATED to the measurement of the analysis), and D-622's own "a
   determinism test over extension step size is what validates the criterion". None of those rows is this family's.
   **So this side proposes no new measurement: the step-size independence test already owed is the one that would
   catch it.** How the stopping rule chosen under §A.7 bears on it is stated there.

6. **The edge of the piece and the safety cap.** Rows 2.13, 2.14(i), 2.15, 45.15, 45.21(ii)–(iii) carry D-624 as
   L2-S22's premise states it ("The record edge … ends the loop, and the record-edge mark says so"). The maximum
   distance (Rows 2.14(ii), 45.21(i), 45.70, 45.86, proposed ADOPTED — proposed) and the guard against oscillation
   (45.21(iv)) are THE DERIVATION IS SILENT rows, not in this family's list. They are named in §A.9.

**Arithmetic after §A.5.** Carried 76 (75 + Row 45.13(i)); QUARANTINED 14 (2 AGREES + 12 DIFFERS: the 13 proposed
less Row 7.62); HISTORICAL 8 (1 AGREES + 3 DIFFERS as proposed + Row 7.62 + Rows 5.73, 45.58, 45.59(ii)); travelling
with the effort setting's design 1 (Row 45.55). 76 + 14 + 8 + 1 = 99. By the axis: 78 AGREES = 75 carried + 2
quarantined + 1 historical; 21 DIFFERS = 1 carried + 12 quarantined + 7 historical + 1 travelling.

## §A.6 Confirmation 1 — the 99 parts; documentation only

**Documentation — what is filed.**
- **ADOPTED — carried (L2-S22) (76):** the 75 of §A.3, and **Row 45.13 claim (i)** from UNPLACED, with §A.5 point 1
  recorded beside it (for L2 the quantity the extension is asked for is its in-span publication).
- **QUARANTINED (14), with the comparison's audit questions:** Rows 2.49 and 45.20(ii); Row 2.10; Row 2.47(ii) with
  Rows 7.64, 7.89, 7.95, 45.14, 45.50, 45.92(i), 51.21(ii), 51.52(i) travelling with it; Row 5.72(i) (as at Row
  5.71); Row 30.75(i) travelling with Row 22.107.
- **HISTORICAL (8):** Rows 23.255, 23.243, 23.253, 23.254 (plans); **Row 7.62, changed from QUARANTINED**, travelling
  with Row 2.47(i) (§A.5 point 3); **Rows 5.73, 45.58, 45.59(ii) from UNPLACED** — the old function layer's pinned
  look-ahead, superseded for L2 by L2-S43 (what one decision reads) and by D-261 item 6 with D-622 (when to stop)
  (§A.5 point 2).
- **Not placed now, travelling with the effort setting's design (1): Row 45.55** (§A.5 point 4).

**Algorithm — what changes:** nothing. No statement's wording changes; no term is added or removed. The question of
what "stops changing" means is §A.7, separately.

**No real choice remains** (the decision-surface block, step 2). The 93 proposals kept follow from the comparison's
vocabulary (§5) and the records of §A.2; the one change (Row 7.62) and the five from UNPLACED follow *(§B item 11; former wording,
preserved (#12): "The 94 proposals follow" — 99 less 5 unplaced is 94, of which Row 7.62 is the one changed)* from D-261's own
wording, D-622 and its strike, L2-S43, and the sizing's §C precedent for effort rows (D-599). The alternatives
considered and why they fall: Row 45.13(i) as a narrower edge-only test (against L2-S22's falsifier and #4); Rows
5.73, 45.58, 45.59(ii) as QUARANTINED (possible, but they state a design rule, not how a program works) or as an L2
rule (a stand-in for convergence, the class D-622's strike closes); Row 45.55 as an L2 rule (the same).

**Recommendation: confirm.** Towards the objective (#4): no reading changes; L2 keeps asking for music until its
reading of the selection stops changing, never stopping on a stand-in. Towards the principles: D-599; D-261, D-622,
D-624 as ruled; #12 (every row keeps its proposal, the ruled label beside it); #6 (one stopping rule, at L2-S22; the
old per-layer windows get no second home in L2); D-035 and the sizing's §C for the cheaper shortcuts. Meta level:
the analysis's own specification — filing only.

## §A.7 Question 2 — what "stops changing" means (OQ-L2-6); this one changes the algorithm

**What is being decided.** L2-S22's last sentence leaves open when the in-span publication counts as "no longer
changing". Filling it changes the algorithm as the specification defines it: it fixes L2's stopping rule for
reading more music.

**Why it matters musically.** Take a selection that opens on a C major chord after a passage in G. With one bar of
earlier music L2 may already read the opening as IV in G with most of the weight, and I in C as a rival with less.
Adding one more bar may leave IV in G on top but shift weight between the two. If L2 stops as soon as the top reading
holds, it publishes weights that more music would still have moved. If it waits until the weights hold too, it reads
further back, which costs time.

**Three positions.**

1. **The principal reading only.** Stop when the best whole reading's part inside the selection is the same after an
   enlargement as before it; the rivals and their masses may still move.
   - *Towards the objective:* the rivals and their weights are published (rival-publication Ruling 1: at the top
     setting nothing is withheld) and passed to the next layer and the display, so they would be published from a
     reading that has not settled. Weaker.
   - *Towards the principles:* D-261 says "in-selection **output**", and the output includes the rivals and masses
     (D-006, D-425: the uncertainty surface's contract is the full posterior). Against D-261's wording.
   - *Cost:* the fewest enlargements.
2. **The whole in-span publication, graded by the effort setting.** At the top effort setting, stop when the in-span
   publication — the readings, the span-rivals and their masses — is the same after an enlargement as before it.
   Below the top, the effort setting sets a tolerance on the change in mass within which the publication counts as
   unchanged, continuously across settings. At every setting the principal in-span reading must be unchanged (L2-S22's
   falsifier). The safety cap (D-624) ends a loop that does not settle, and the publication is then marked as
   truncated (D-263).
   - *Towards the objective:* at the top setting nothing published is left unsettled, unless the safety cap
     ends the loop and the publication is marked truncated *(§B item 12; former wording, preserved (#12): no
     exception stated)*; it also narrows §A.5 point 5's
     risk, since a step that changes nothing at all is a stronger sign than a step that leaves the top reading in
     place (*my reading*; it does not remove the risk, and the step-size test still decides it).
   - *Towards the principles:* D-261 applied to the whole output, directly (D-622); the same pattern as your
     rival-publication Ruling 1 (exact at the top, graded continuously below) and the sizing's §C entry point (c);
     D-035 (a cost-driving choice is a setting, not a constant); D-200 (precision first, speed traded only as a
     setting); D-624 and D-263 for a loop that does not settle.
   - *Cost and an unknown:* at the top setting L2 may read far before every mass is exactly unchanged. Whether that
     happens before the safety cap in ordinary music is **not established** — it needs the build. If it often does
     not, the top setting will often read to the cap and mark the result truncated, which D-624 permits but which
     would be worth knowing; that is a measurement at the build, under the effort setting's design.
3. **The whole publication, within one fixed tolerance written into the design.** A single measured value, the same
   at every setting.
   - *Towards the objective:* close to position 2 at its middle settings.
   - *Towards the principles:* a cost-driving choice fixed as a constant (against D-035); the same shape as Position 1
     of the rival-publication family, which you declined (its record gives the grounds: against the amendment's
     wording and its reason, against D-200's order); and no measured value was found in what this sitting read.
     *(§B item 13; former wording, preserved (#12): "which you declined for that reason; and no measured value
     exists to write in" — D-035 was that record's ground against Position 2, not Position 1, and the negative was
     wider than the reads.)*

**Recommendation: position 2.** Towards the objective: the top setting publishes nothing that more music would still
move. Towards the principles: D-261 as worded, D-622 (directly, no stand-in), D-035, D-200, and consistency with your
rival-publication ruling. Meta level: the analysis's own specification — one sentence of L2-S22 written and OQ-L2-6
closed; the tolerance values and defaults are decided when the effort setting is built (D-202 stays DEFERRED), as the
cut-off depths are.

**Proposed wording for the application act**, replacing L2-S22's last sentence: "At the top effort setting it stops
when its in-span publication — the readings, the span-rivals and their masses — is the same after an enlargement as
before it. Below the top, the effort setting sets a tolerance on the change in mass within which the publication
counts as unchanged, continuously across settings. At every setting the principal in-span reading must be unchanged.
The safety cap (D-624) ends a loop that does not settle, and the publication is then marked as truncated (D-263)."

## §A.8 The method that stands

**Unchanged by Confirmation 1** — quoted or summarised from the derivation, *checked* this sitting:
- **L2-S22** (lines 575–597, §A.1): at the edge of the working span L2's reading depends on music before and after
  it; L2 asks for more music; it stops when its in-span publication stops changing between successive enlargements;
  the record edge ends a loop that never converges and is marked; the increment and the stop test are L2's, never
  L1's or L0's.
- **L2-S48** (as quoted at Rows 21.59(i) and 22.83(i)): L2's publication covers exactly the working span; the result
  after any sequence of enlargements equals a single fresh run over the final loaded span.
- **L2-S43** (as quoted at Row 5.71): no reading is discarded before the whole working span, context included, has
  been scored; "the end" is the end of the music loaded for the selection (tractability Ruling 1 (ii)).
- **L2-S20's premise** (lines 547–549): with no earlier music loaded, recency has nothing to recall at a long tonic
  opening, "and the edge rule (L2-S22) is what supplies it".
- **D-260, D-261, D-622, D-624** as in §A.2.

**Changed only if Question 2 goes as recommended:** L2-S22's last sentence, as proposed in §A.7.

## §A.9 Carried, not decided here

- The maximum distance on the enlargement loop and the guard against oscillation — Rows 2.14(ii), 45.21(i),
  45.21(iv), 45.70, 45.86, proposed ADOPTED — proposed, THE DERIVATION IS SILENT, not in this family's list.
- The step size (Rows 45.22(ii), 45.23(ii), 45.29(ii), 45.30(i), proposed), the publication's independence of it
  (Row 45.24, proposed) and the test (Row 45.72, RELOCATED to the measurement of the analysis) — §A.5 point 5.
- The provenance an L2 publication carries when decided on truncated evidence (Rows 45.26(ii), 45.61(ii), proposed;
  D-263).
- Row 45.55 and a cadence-or-phrase forward limit as possible lower effort settings — the effort setting's design
  (D-202).
- Row 45.60(ii) (an extension may settle an open decision, never reopen a closed one), UNPLACED against L2-S48 — not
  this family's.
- The outgoing bounded-context design's §5 bullet for Architectural Layer 5 still states a stop the 2026-08-07
  strike's reasoning covers (§A.5 point 2). The outgoing documents are not edited in this phase; recorded for the
  application act and the audit.

## §A.10 What this sitting read

At the objects: the derivation at L2-S20 (its premise, lines 540–553), L2-S21, L2-S22 (lines 575–597), §4 OQ-L2-1 to
OQ-L2-18 (lines 1195–1273), and §6.3's lines 1525–1540; the comparison file at §7's entries for L2-S11 to L2-S23
(lines 71095–71161), all 99 rows of §A.3, member 45 whole as tabulated (lines 59129–60427), and on the way Rows 2.11,
2.12, 2.17 (heading), 2.20, 2.50, 5.71, 5.75, 6.56, 7.17, 7.63, 7.65, 7.90, 7.96, 7.104, 7.156, 21.61, 22.84,
22.86, 23.244, 23.256, 30.76, 43.79, 43.80, 51.16, 51.17, 51.22, 51.24, 51.25, 51.53, 51.54, 51.64, 51.65 in part;
`cowork_bounded_context_design.md` lines 1–200; `decisions/group_C.md` at D-260 to D-264 and D-624, and
`decisions/group_F.md` at D-622; the ruling records of tractability, rival publication, no-early-discarding (whole)
and of the route (lines 50–79), the pivot chord (lines 60–89) and one tonality per span (lines 20–59); the sizing at
§3.1, §7, §8 and §C; the no-early-discarding surface at lines 95–114; the working-order surface at lines 150–161;
the L2-S14 surface whole; entries 291, 310 to 318 (291, 317, 318 whole; the others at §2); entry 118's bridge-fault
section, entry 152's (v) to (x), entry 169 whole; the ordinary session-start read. Searched, not read whole: the
other records and surfaces of 2026-10-04 to 2026-10-07. **Not opened:** `FRAMEWORK.md`, the input contract (Ruling
46 relayed through the derivation), the other outgoing member documents, the ledger (C43 relayed), the silence
record (its Ruling 1 relayed through the no-early-discarding record). Nothing was read through a shell.

## §B The check at the sources

Run in the turn after the user's "continue", before any question was put. Every quotation and cited line in §A was
re-read against the staged copies: the derivation at L2-S20, L2-S22, OQ-L2-6 and §6.3; the comparison file at §7's
entry and the 99 rows; `decisions/group_C.md` at D-260 to D-264 and D-624, `decisions/group_F.md` at D-622;
`cowork_bounded_context_design.md` lines 1–200; the tractability, rival-publication, no-early-discarding, pivot-chord,
one-tonality and route records and the sizing at the lines §A.10 names; the search hits of §A.4, each at its line.
The writing was swept for absolutes (never, nothing, every, all, only, none, no, always, whole, exactly), each hit
read against the act that established it. The arithmetic was re-added: 75 + 2 + 1 = 78 AGREES; 1 + 12 + 7 + 1 = 21
DIFFERS; 76 + 14 + 8 + 1 = 99; the carried list of §A.3 counted at its seven groups (30 + 4 + 13 + 9 + 9 + 7 + 2 =
74 at the first writing — Row 45.59(i) had been left out; added before the first commit (whose landing came back without it — the bridge fault; landed again), now 31 in the first group,
75). **Thirteen findings, corrected at their sites with the former wording kept. None moves a placement, a position,
the recommendations, or the statement that Confirmation 1 changes nothing in L2's algorithm.**

1. **§A.2, a placement wider than its source.** The tractability record says OQ-L2-6 is "open and another family's";
   it does not name this family.
2. **§A.2, a proposal reported as a placement.** The sizing's §C proposed, as its reading, that Rows 43.12 and
   7.104(i) travel with the effort setting's design.
3. **§A.3, a travelling chain flattened.** Rows 7.89 and 7.95 travel with Row 7.64, which travels with Row 2.47(ii).
4. **§A.4, a count.** 29 `cowork_l2_*` files were searched (28 surfaces and the sizing), not 28.
5. **§A.5 point 1, a paraphrase wider than the falsifier.** L2-S22's falsifier names the principal in-span reading.
6. **§A.5 point 2, a quotation not in the source's words, and a citation to a section that does not show the fact.**
   Now quoted as the annotation writes it, and the §5 bullet for Architectural Layer 5 cited at its lines.
7. **§A.5 point 2, an unmarked prediction** about what the audit would find. Now marked as a reading.
8. **§A.5 point 3, a read claimed wider than made.** §10 of the bounded-context design was not opened; the §10
   correction is relayed through D-261's provenance.
9. **§A.5 point 4, an overstatement.** D-622 measured another stand-in, not a margin trigger; "the same shape as".
10. **§A.5 point 5, a gloss wider than D-622's words, and a claim unmarked as a reading.**
11. **§A.6, a count.** 94 proposals before the change; 93 kept and one changed.
12. **§A.7 position 2, an absolute without its exception** (the safety cap).
13. **§A.7 position 3, a misattributed ground and a negative wider than the reads.** The rival-publication record's
    grounds against its Position 1 were the amendment's wording and D-200's order; D-035 was its ground against
    Position 2.

**A departure in this turn, declared.** One shell command was run in the cloud container during the check — `true`,
which reads and writes nothing; no finding rests on it. It breaks entry 318's "no shell at any point".

**What the check did not do.** It did not open `FRAMEWORK.md`, the input contract, the ledger, the silence record,
the outgoing member documents other than the bounded-context design's lines 1–200, or that design's §10. It did not
test the readings marked *my reading* in §A.5 and §A.7, among them whether the top setting's identity test settles
before the safety cap in ordinary music, which stays unestablished.

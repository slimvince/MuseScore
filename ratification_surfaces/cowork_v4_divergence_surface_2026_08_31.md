# DECISION SURFACE — the V4 divergence: a ratified sentence that is false at its primary

> **STATUS: A DECISION SURFACE, DELIVERED TO THE USER 2026-08-31. NOTHING HERE IS EXECUTED.**
> No document is amended, no register row or entry is written, no code is opened, and no choice
> question is asked in the turn that delivers this. **The choice question follows in a separate,
> later turn** (the 2026-07-05 mandate, D-249: the whole surface is delivered as user-visible text
> first, and a decision answered blind is voidable).
>
> **This is the FIRST of four items the user holds.** One decision surface per turn; the other three
> — row 7, the DP-K amendment candidate, and the row-19 double-extract residual — are named at §8 and
> are **not** put here.
>
> *Written to disk as well as delivered in conversation. The three sittings of 2026-08-28, 08-29 and
> 08-30 each had to declare "delivered in conversation, not written to disk beforehand" as a
> departure; this closes that.*
>
> **★ AMENDED 2026-08-31, THE SAME DAY, ON THE USER'S CHALLENGE.** He observed that the alternatives
> had not been weighed against the ultimate objective. **The challenge is upheld**: §6 labelled an
> axis "objective" and rated three of four options on it as *"nothing improves"*, which is not a
> rating — what it actually weighed was record correctness. **§6a is the weighing that was missing**,
> and it also corrects a **principle #18 (Class A) defect in this surface's own reasoning**: §4 and §5
> rested on an unchecked causal claim about our own system. **§6's original ratings stand unedited
> (#12); the recommendation is unchanged and its reason is replaced.**

---

## 1. What is being decided, in one sentence

**Whether — and by what route — to correct one sentence of `FRAMEWORK.md` §5 (the L1 charter) that
states its supporting measurement wrongly**, the framework being ratified and this pass having no
licence to amend anything itself.

---

## 2. Background, from nothing

The framework document derives the architecture of the harmonic analysis. Each layer's charter says
what that layer is for and **why it earns its place**, and those justifications carry `[FACT]` tags
pointing at published measurements. **L1** is the layer that reads the notation for change points and
covariates and *decides nothing*; one of the covariates it publishes is each change point's **metric
strength class**, and the charter defends carrying it with a measured claim.

The reading pass was commissioned (Ruling 2, 2026-08-30) partly to **verify the framework's
load-bearing cited figures at their primary sources** — because the framework was derived from
sources read on our side, and a figure that has never been checked at the paper is a citation, not a
fact. Thirteen such figures were enumerated. **All thirteen were read at the object** — the held PDFs
staged through the bridge and read as page images, which is the strongest grade this environment
offers. **Twelve verified. One did not.** That one is target **V4**, and the commission's §6 makes a
DIVERGES verdict on a load-bearing figure a **STOP**: written up on its own and put to the user
before the pass continues past it. It was written up on 2026-08-30
(`reading_pass/stop_v4_divergence_2026_08_30.md`) and has been open since.

---

## 3. What the framework says, and what the paper says

**The sentence, verbatim from `FRAMEWORK.md` §5, L1, "Why metric strength earns its place"** — read at
the file this session:

> "It is measured to constrain where harmonies change — **harmonic change was counted at 71.5% of
> tactus beats against 2.4% of the lowest metrical level** — and removing metrical-accent features
> from a segmental analyser costs about six points of F-measure. **[FACT — both.]**"

**The primary: Temperley 2009, "A Unified Probabilistic Model for Polyphonic Music Analysis", JNMR
38(1), Table 1, journal p. 6** — "Harmonic changes at beats of different metrical levels in the
Kostka–Payne corpus", the caption glossing **"Metrical level (2 = tactus)"**:

| Metrical level | % of beats carrying a harmony change |
|---|---|
| 3 (the highest shown) | **71.5** |
| 2 — **the tactus** | **22.3** |
| 1 | **2.4** |

**So both numbers in the framework's clause exist at the primary, and the clause attaches the wrong
one to the tactus.** 71.5% is the level *above* the tactus; the tactus itself reads 22.3%. The clause
also calls level 1 "the lowest metrical level" where Temperley's model carries a level 0 beneath it
that Table 1 simply does not list — his claim about sub-tactus changes being rare is qualitative
text, not a tabulated row.

**The second half of the sentence — the six-point ablation — is VERIFIED exactly** (Masada & Bunescu
2019, Table 5: F-measure 77.6 → 71.2 without accent features). **This concerns the first half only.**

---

## 4. What is affected, and what is not

**NOT affected — and this is most of it:**

- **The design point's direction is untouched and, if anything, sharpened.** The primary's own
  gradient — **71.5 → 22.3 → 2.4 by descending metrical level** — is precisely the "metric strength
  constrains where harmonies change" ground the L1 charter rests on. A monotone relationship across
  three levels is stronger evidence for the claim than a single contrast between two.
- **No rival gains anything.** Nothing about the correction favours any alternative decomposition.
- **No other verification target moves**, no other framework sentence is implicated, and no chosen
  design point is falsified. The pass found **no falsifier anywhere.**

**AFFECTED:**

- **The `[FACT]` label on that clause is, as the clause is worded, unearned.** The theory-grounding
  corollary to #1/#2 requires a load-bearing claim labelled FACT to be *stated or measured in a paper
  actually fetched and read*. The paper does not state what the clause states.
- **A detail specification of L1 derived inside this charter would read the wrong number.** That is
  the live consequence, and it is the one that matters: the detail-specification phase is open, L1 is
  named in the ratified routing, and a session deriving L1's covariates from its charter would take
  "71.5% of tactus beats" as its ground for how strongly to weight tactus-level change points. **It
  would be weighting the tactus with the level above it.**

---

## 5. What the standing principles already decide

Per D-599 — apply the standing principles first, and only where they do not decide is there a genuine
user choice.

- **#10's worth test** asks whether leaving an issue unfixed risks *"something being built that does
  not serve maximum-precision inference"*. **It does**, by the route in §4: an L1 detail
  specification is exactly what the open phase derives next, and this clause is its cited ground.
  **So the issue is worth fixing rather than DISCARDED.**
- **The theory-grounding corollary** requires the FACT label to be earned at the paper. It is not.
- **#12** requires the former wording preserved in place wherever it is replaced — the record keeps
  what it used to say and why it changed.
- **The 2026-08-15 supersession does NOT bind here.** Its rule — *a disagreement between
  specification and code is evidence, reserved for the audit; no document is corrected on the ground
  that the code says otherwise* — is about **code**. This is a disagreement between a document and a
  **published primary source**, which is the reading pass's own subject and not the audit's.

**Derivation: the sentence should be corrected, with the former wording preserved.** What remains for
the user is ratifying that derivation, and settling the two things the principles do not reach —
**how much the correction should say**, and **by what route and when**.

---

## 6. The options

Rated on the two axes the record uses: **what it does for the ultimate objective** (enabling the best
possible inference), and **what it costs and risks**. The principle behind each pro and con is named.

### Option A — Correct the sentence minimally, by the ruled route

Replace the clause with the primary's own three-level gradient; preserve the former wording in place.
The corrected wording, already drafted at the STOP memo:

> "harmonic change was counted at 71.5% of the strongest-level beats against 22.3% of tactus beats
> and 2.4% of the level below (Temperley 2009, Table 1, Kostka–Payne corpus)"

- **Objective:** the L1 charter's ground becomes true at its primary, and an L1 detail specification
  derived from it reads the right number for the tactus. **The evidence for carrying metric strength
  is strengthened, not weakened** — three levels, monotone.
- **Cost and risk:** one amendment to a ratified document, which needs the user's word (the framework
  is his ratification, and this pass amends nothing). It costs a dispatch cycle, or a slot in the next
  dispatch that opens the framework for another reason. **Risk: none identified.**
- **Principles:** #10's worth test (the fix is owed); the theory-grounding corollary (the FACT label
  becomes earned); #12 (former wording preserved).

### Option B — Correct it *and* add the stronger fact the primary carries

As A, plus the primary's own further finding: **Temperley's model, on this very evidence, permits
harmonic change only at tactus beats** — *"harmonic changes are allowed only on tactus beats"*, with
Table 1 cited as the ground, and *"the probability of change is higher for L3 beats than L2 beats,
reflecting the greater likelihood of chord changes on stronger beats."*

- **Objective:** a published model constraining its own search on this measurement is stronger
  evidence that metric strength is informative than the bare gradient is.
- **★ Cost and risk — and this is why I do not recommend it.** **The added fact, sitting in L1's
  charter, invites precisely the reading that charter forbids.** L1's own stated ground is that its
  change-point set is **exhaustive** — every onset *and every release* opens a candidate, so *"a real
  harmony change can never be missed, and over-grab is structurally impossible rather than merely
  discouraged."* A sentence in that same charter reporting that a respected published model **prunes
  its candidate set to tactus beats** is one step from a later session reading it as licence to prune
  ours. That would trade a structural guarantee for a distributional prior — the exact shape of
  defect the exhaustiveness argument exists against.
- **Principles:** the L1 exhaustiveness ground (§5 of the framework, its own words); #12's direction
  of travel (carry the possibility rather than cut it); #13 (a surprise is surfaced, not built
  around).

### Option C — Record only; do not amend now

Leave the ratified text as it stands. The correction lives in the STOP memo and the findings surface,
and is folded in whenever the framework is next opened for another reason.

- **Objective:** nothing improves now. **The live consequence of §4 stays live for as long as the
  text does** — and L1 is in the ratified routing for the phase that is currently open, so the window
  in which a session could derive from the wrong number is not hypothetical.
- **Cost and risk:** no dispatch cycle spent. **Risk: a known-false `[FACT]`-labelled sentence stands
  in a ratified governing document, and the record's own experience is that a correction deferred to
  "the next time we open the file" is a correction that waits for an unrelated act.**
- **Principles:** against #10's stated purpose — the specification is meant to be *as correct and
  complete as possible* so that what is built can be compared against it.

### Option D — Row it in the open-items register

Create a row and work it under whatever gate applies.

- **Objective:** the same as C in the short run — nothing changes until the row is worked.
- **Cost and risk:** **the register's rule (c) is under suspension**
  (`cowork_register_rule_c_suspension_2026_08_28.md`), so a row cannot be created by the ordinary
  route right now; and a row about a *governing document's account of its own evidence* would sit
  near the apparatus boundary, where D-676's lapse rule applies and rows stop being owed. **This
  route risks the correction quietly ceasing to be owed at all.**
- **Principles:** D-438/D-676 (apparatus rows gate nothing and stop being owed) — which is precisely
  why this is the wrong container for something #10's worth test says is inference-bearing.

---

## 6a. ★ THE WEIGHING AGAINST THE ULTIMATE OBJECTIVE — added 2026-08-31 on the user's challenge, with the defect it corrects named

**The user's challenge, and it is upheld: §6 above labelled an axis "objective" and did not use it.**
Three of the four options were rated on that axis as *"nothing improves now"* or *"the same as C"* —
which is not a rating. What §6 actually weighed was **record correctness**, and it called that the
objective. **The original ratings stand above unedited (#12); this section is the weighing that was
missing, and it changes the recommendation's reason.**

**★ AND A DEFECT IN MY OWN REASONING, WHICH IS THE MORE SERIOUS HALF.** §4 asserted that *"an L1
detail specification derived from this charter would take '71.5% of tactus beats' as its ground for
how strongly to weight tactus-level change points"*, and §5 rested the whole worth-test argument on
it. **That is a causal claim about our own system, it is checkable, and I did not check it.** It is
principle **#18 (Class A)** — and the framework's own §8.4 states the identical test for the identical
shape of claim: *"the comparison is a causal claim about our own system, it is checkable, and until
the scales are declared it is unchecked."* **A decision surface that argues from an unchecked causal
premise is arguing from an assumption wearing a citation.** Checked below.

### What the number actually feeds — derived from the record, not asserted

- **L1 publishes a *class*, not a percentage.** §5's L1 charter: *"per change point, its **metric
  strength class**"*. Temperley's figures appear nowhere in what L1 hands on.
- **L1 does not judge.** §8.3: *"The layers that carry facts — L0 and L1 — are style-agnostic and
  lossless. Style-specificity enters only through the priors and weights of the layers that judge."*
  **So no weight on metric strength lives at L1 at all.**
- **The weight lives at L2 and is FITTED, not transcribed.** DP-P: *how the terms of L2's score are
  combined and fitted* is **NOT DECIDED HERE — detail specification and measurement design**; and
  fitted values are fit once against ground truth under the fit gates (#20, **D-096**). **#17f /
  D-431** additionally forbids hand-transcribed measurement numbers entering documents at all.

**Conclusion, and it corrects §4: the wrong number cannot propagate into a fitted value. There is no
path from Temperley's table to a weight in our system.** My asserted inference consequence was
wrong, and the #18 defect was load-bearing on it.

### So what IS the consequence for the objective — three, honestly graded

1. **[ESTABLISHED, and it is the real one] The document's WARRANT.** Principle **#1** admits only
   established fact and theory; the theory-grounding corollary requires a `[FACT]` label to be earned
   in *a paper actually fetched and read*. **A `[FACT]`-tagged clause that misstates its primary is
   exactly the failure that corollary exists to catch.** Its cost is not to any one number — it is to
   the standing of the document as a knowledge base. **And that is the objective at the width Ruling 2
   widened it to:** the architecture is evaluated **as a whole**, and a whole whose citations are
   unchecked is not knowledge-based. **The user's own ground for commissioning this pass was that
   very sentence — *"We should act knowledge-based, right? Knowing we have research that is not yet
   read brakes that rule."*** **Running the pass, finding the false citation, and then leaving it in
   place is self-defeating on the pass's own stated purpose.**
2. **[A READING, NOT ESTABLISHED — labelled so it does not travel as a fact] The classing of metric
   strength.** The charter says *"metric strength class"* and **does not fix how many classes or
   where their boundaries fall** — an L1 detail-specification question the open phase will reach.
   The **wrong** version is a two-way contrast (71.5 against 2.4), which supports a coarse or binary
   classing. The **corrected** version is a monotone gradient across three levels (71.5 / 22.3 / 2.4),
   which supports a finer one. **If the classing is derived from this evidence, the correction changes
   what the evidence supports.** *Whether it is so derived is not stated anywhere in the record, and
   I am not asserting it — that is the same #18 trap, and naming it as a reading is how it is
   avoided.*
3. **[ESTABLISHED] Reader belief, which shapes design judgement rather than values.** A session
   reading L1's charter today believes metric strength is roughly three times more discriminative at
   the tactus than the primary says. That bears on judgements like whether the covariate earns its
   place at all and how much structure to build around it — **not on any fitted quantity.**

### What that does to the option ratings

| Option | Objective, re-rated honestly | Cost |
|---|---|---|
| **A** | **Repairs (1) directly, and puts (2) on the right footing before the phase reaches L1.** No effect on any fitted value — there is none to affect | **Effectively nil** — one sentence, and a batch is already pending |
| **B** | Same as A on (1), **plus a standing invitation to misread L1's exhaustiveness commitment** | Nil in effort; the misreading risk is the cost |
| **C** | **(1) stays impaired for as long as the text stands** — during the phase whose ratified routing names L1. **But my §6 urgency was overstated: no fitted value is at risk, so this is a warrant cost, not a precision cost** | Saves nothing, because A costs nothing |
| **D** | Same as C, **and** risks the correction lapsing out of being owed | Register rule (c) is suspended; the row would sit near the apparatus boundary |

**★ The honest bottom line: this decision's value to inference is INDIRECT and small in the near
term. Its value to the framework's warrant is direct.** §6 argued the opposite emphasis, and was
wrong to.

---

## 7. Recommendation, with its reason — REASON REVISED at §6a

**Option A — correct minimally, by the ruled route — and record option B's added fact where it
already lives, in the STOP memo and the findings surface, rather than promoting it into the charter.**

**The recommendation is unchanged; its reason is not.** §6a establishes that no fitted value is at
risk, so the case for A is **not** that a detail specification would compute something wrong. **The
case is that the pass was commissioned to make the framework's citations real, this is the one it
found unreal, and the correction costs a sentence on a batch that is already pending.** Leaving it
would be the pass defeating its own purpose at the only point where it found something to fix.

**B stays declined, on the asymmetry between its halves.** The correction itself is owed on the
principles and carries no identified risk. The extra fact is true, is at the primary, and is
genuinely stronger evidence — **but it is stronger evidence for a claim adjacent to the one L1's
charter is making**, and placing it inside a charter whose central structural commitment is an
exhaustive candidate set creates a standing invitation to misread it. A charter should carry the
evidence for what it does, not the evidence for what a different system did.

**On timing:** the correction does not need its own dispatch cycle. It is a single sentence in one
file, and it can ride the next dispatch that opens `FRAMEWORK.md` or lands anything — of which there
is one pending in any case, since **three handoff entries (eighty-two, eighty-three, eighty-four) are
staged and awaiting prepend by the next batch that lands.** *This is a recommendation about
efficiency, not about the correction's standing; if you would rather it went alone, that is a clean
choice too.*

---

## 8. What this surface does NOT decide, and what is still yours

**Not decided here, and not asked in this turn:**

- **Row 7 — the Modal Harmony Ontology.** The pass's other STOP. Unidentifiable without the workbook,
  which the ruling forbids opening; five searches failed. **Live lead:** it may dissolve into row 6 if
  the workbook's rows R170–R173 describe the NTUA description-logic family.
- **The DP-K amendment candidate.** New with the findings surface: DP-K's recorded defense rests a leg
  on an off-domain measurement that a sibling study contradicts, and the pass found a stronger
  on-domain replacement. **The design point itself is not in question.**
- **The row-19 residual.** Whether an at-the-object whole read substitutes for the double extract the
  commission asks of a central paper.
- **And, after those, the first-deriving-subject decision**, deferred at Ruling 2 and returning per
  the commission's own §8 once you have ruled on the findings.

**Each is its own surface in its own turn.**

---

*Provenance: written by the third session of the reading pass, 2026-08-31, under the ruled
decision-surface form (D-249, D-424, D-599, D-658). `FRAMEWORK.md` §5 read at the file this session;
Temperley 2009 Table 1 and pp. 6–7 read AT THE OBJECT by session 1 and recorded at
`reading_pass/stop_v4_divergence_2026_08_30.md`. No document is amended, no register identity is
allocated, no code is opened, and no choice question is asked in the turn that delivers this.*

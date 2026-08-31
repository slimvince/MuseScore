# CROSS-CHECK — population row 19 (Hamanaka, Hirata & Tojo 2013, chapter 8), the two extracts compared

> **STATUS: THE CROSS-CHECK REQUIRED BY THE COMMISSION'S §4 FOR A CENTRAL PAPER, PERFORMED 2026-08-31
> UNDER THE USER'S RULING OF THE SAME DAY (row-19 residual surface, Option A).** With this file, **all
> EIGHT central papers carry cross-checked double extracts**, and the commission's §8 condition is met
> literally for every one of them.
>
> Compared:
> - **First pass** — `reading_pass/extracts/hamanaka-hirata-tojo-2013-computational-music-theory-gttm.md`
>   (session 3, earlier the same day)
> - **Second pass** — `reading_pass/extracts_second_pass/hamanaka-hirata-tojo-2013-computational-music-theory-gttm.md`
>
> **Both reads are AT THE OBJECT, WHOLE — all thirty PDF pages read as page images.** This is the only
> pair in the pass with **no relay on either side**, and therefore the only pair whose independence is
> not bounded by the read-tool finding. **Disagreements below were resolved by me at the paper**, by
> reading the pages concerned again; the pages consulted for this cross-check are named at each item.

---

## 0. How independence was obtained, and what it does and does not cover

The second pass was performed by a **cleanly separated reader** — the second of the two routes the
commission names in terms: *"a fresh session, **or a cleanly separated re-read that does not consult
the first extract**"*. It was given the PDF, the routing metadata from the population table (R-7's
time-span-reduction alternative; DP-O; L3 grouping) and `FRAMEWORK.md` to read for itself. It was
barred from `reading_pass/extracts/`, `reading_pass/extracts_second_pass/`,
`reading_pass/cross_checks/`, `population.md`, `additions.md`, `continuation.md`, the findings
surface, every handoff entry and everything under `ratification_surfaces/` and
`docs/research_papers/`. **Its own banner declares it opened none of them**, and its content is
consistent with that: it reaches several of the first pass's conclusions by different routes and
misses others the first pass holds.

**What this does NOT buy, stated plainly rather than discovered later.** Independence here is of
**session, prompt and extract — not of reader.** The read-tool finding's lesson was that shared
machinery survives both passes and no cross-check can see it; the shared machinery here is the model
and the framing of the instruction. **The seven existing pairs have exactly the same limitation and
were accepted.** What this pair adds over them is that **neither side is relayed**.

**A fresh Cowork session would have been WORSE here, not better**, and the reason is worth recording:
the standing boot (P-1) requires a new session to read the newest handoff entry, which by then carried
row 19's findings in summary — the 46 parameters, F ≈ 0.49, DP-O unmoved. **A "fresh session" would
have consulted a summary of the first extract before opening the paper.** The separated reader
consulted none of it.

---

## 1. Every measured value agrees. No exceptions.

Checked value by value against both extracts and, where listed below, re-read at the page:

| Value | First pass | Second pass | At the paper |
|---|---|---|---|
| Table 8.4 Total (100 melodies), grouping | 0.46 → 0.77 | 0.46 → 0.77 | **Confirmed, p. 230** |
| Table 8.4 Total, metrical | 0.84 → 0.90 | 0.84 → 0.90 | **Confirmed, p. 230** |
| Table 8.4 Total, time-span tree | 0.44 → 0.60 | 0.44 → 0.60 | **Confirmed, p. 230** |
| FATTA fully automatic (running text, not a table) | 0.48 / 0.89 / 0.49 | 0.48 / 0.89 / 0.49 | **Confirmed, p. 230**, and both passes map them to grouping / metrical / time-span in the paper's own order |
| Baseline defaults | S^rules=0.5, T^rules=0.5, Ws=0.5, Wr=0.5, Wl=0.5, σ=0.05 | same | **Confirmed, p. 230** |
| Table 8.5 values | 575 vs 891 | 575 vs 891 | **Confirmed, p. 231** |
| Parameter counts | 15 + 18 + 13 = 46 | 15 + 18 + 13 = 46; "there are 46 parameters" p. 216 | **Confirmed** |
| Hand-tuning cost | ~10 min per piece | ~10 min per piece | **Confirmed, p. 230** |
| Ground truth | 100 sections, 8-bar, monophonic, classical; three further experts crosschecked | identical | **Confirmed, pp. 228–230** |
| Dataset | 300 pairs at `music.iit.tsukuba.ac.jp/hamanaka/gttm.htm` | identical | **Confirmed, p. 233** |
| Morphing evaluation | ten pairs, all satisfied eq. 8.8, no numeric values | identical | **Confirmed, p. 231** |
| Metric | F = 2PR/(P+R), eq. 8.7 | identical | **Confirmed, p. 228** |

**No value disagreed anywhere.** That now holds across **all eight** cross-checked central papers and
**sixteen** extracts. It is the pass's most consistent single result.

---

## 2. ★ ONE VERBATIM-QUOTATION DISAGREEMENT — resolved at the paper, and the FIRST pass was wrong

Both extracts transcribe the chapter's reference [6], the entry for the JNMR paper row 19 was
originally flagged on. **They disagree on one character.**

- **First pass:** *"Hamanaka M, Hirata K, **Tojo S** (2007) Implementing 'a generating theory of tonal
  music'. J New Music Res (JNMR) 35(4):249–277."*
- **Second pass:** *"Hamanaka M, Hirata K, **Tojo T** (2007) …"*, flagged explicitly as a hazard: the
  initial differs from "Tojo S" in every other Hamanaka–Hirata–Tojo entry ([7], [8], [14], [15], [23],
  [24]) and from the chapter's own byline, "Satoshi Tojo" (p. 205).

**RESOLVED AT THE PAPER, p. 234, read again as a page image for this cross-check: the reference list
prints "Tojo T". THE SECOND PASS IS CORRECT.**

**What went wrong in the first pass is worth naming precisely: it silently normalised a misprint.**
The initial "T" is almost certainly the publisher's error — Satoshi Tojo is the third author, as
[7] and [8] print — and the first pass produced the *correct-in-the-world* string while presenting it
as a *verbatim quotation of the page*. **It is right about the person and wrong about the page**, and
the section it appears in is the bibliographic by-catch that routes to the bibliography
reconciliation, where what the page prints is exactly what matters.

**This is the fourth error class the pass's cross-checks have caught** (after row 2's structural
divergence, row 18's mis-attached table value and row 21's omission), and it is a new one: **a
verbatim quotation silently improved.** It is a smaller error than those three, and it is a purer
instance of why quotations get checked.

**Routed:** the bibliography reconciliation now carries, for this reference, *chapter prints* **year
2007, pages 249–277, third author initial "T", title "a generating theory"** — against our records'
2006, no page range, and the correct title. **Our title is still the right one** (both passes agree
the chapter misprints *generative* as *generating*, and the chapter's own [9] prints Lerdahl &
Jackendoff correctly).

---

## 3. ★ WHAT THE SECOND PASS CAUGHT THAT THE FIRST MISSED — five items, three of them load-bearing

### 3.1 ★★ The "configured" column may be FITTED ON THE GRADED DATA. The first pass did not raise it.

The second pass, at its §8 item 4: *"the ATTA parameters were hand-tuned per piece against the same
expert analyses used as ground truth (p. 230), [so] the 0.77 grouping / 0.90 metrical / 0.60 time-span
'configured' figures may be fitted on the graded data. The paper does not address this."* It adds that
**the chapter never mentions train/test separation, cross-validation, or held-out data.**

**Confirmed at the paper, p. 230:** *"In this test, the parameters were configured manually because the
optimal values of the parameters depend on the piece of music"*, and *"It took an average of
approximately 10 min per piece to find each plausible tuning."* **Per piece.** The tuning is
per-item, against the very analyses the F-measure is computed against.

**This is the most consequential thing either pass found about the row's headline numbers, and only
one pass found it.** It is exactly this project's own **#20** (fit and evaluation are separate acts)
and **#96/D-096** territory, read into someone else's paper. **The 0.77 / 0.90 / 0.60 column is not a
generalisation figure**, and any future use of it must say so. **The 0.46 / 0.84 / 0.44 baseline and
the 0.48 / 0.89 / 0.49 automatic figures are unaffected** — no per-piece tuning enters either.

**And the two passes are complementary here, which is the cross-check working in both directions.**
The first pass holds the quotation the second missed — p. 211, on how the parameter set was built:
*"Whenever we find a correct result that exGTTM cannot generate, we introduce new parameters and give
them appropriate values so that exGTTM can then generate this result. In this way, we repeatedly
externalize and introduce new parameters until we have obtained all of the results that are generally
considered correct."* **Put beside the second pass's finding, that is the same phenomenon one level
up: the parameter SET was grown against results already considered correct, and then the parameter
VALUES were tuned per piece against the graded analyses.** Neither extract alone states this; the pair
does.

### 3.2 ★ Table 8.5's "Total (100 melodies)" row cannot be a total — the first pass reported it as one

The first pass wrote: *"Operation time over 100 melodies: interactive GTTM analyzer 575 s against the
GTTM manual editor 891 s."* Read as a total over 100 melodies that is **5.75 seconds per piece**,
which contradicts the chapter's own ~10-minutes-per-piece figure by two orders of magnitude.

The second pass caught it: the values *"are lower than four of the five itemised rows, so they behave
as averages per piece, not sums. The paper does not say which."*

**RESOLVED AT THE PAPER, p. 231, re-read for this cross-check.**
- **The second pass's conclusion is right and is corroborated by a figure it did not cite:** 575 s
  ≈ 9.6 minutes per piece, which agrees with p. 230's *"approximately 10 min per piece"*. A sum over
  100 melodies would be ≈ 57,500 s.
- **The second pass's supporting count is WRONG, and the cross-check catches it.** Table 8.5's itemised
  rows are 326, 541, 724, 621, 876 (analyzer) and 624, 791, 1,026, 915, 1,246 (manual editor).
  **575 is lower than THREE of the five, not four**; 891 likewise. **The substance survives, the
  arithmetic does not.** Corrected here; the second extract is left unedited under #12.
- **The paper's own label is "Total (100 melodies)" and it never says whether it means a mean.** That
  ambiguity is the paper's and is recorded as such, not resolved away.

**Neither pass got this row entirely right, and the pair plus a look at the page did.** That is the
plainest single argument in this file for having done the exercise.

### 3.3 ★ Precision and recall are never defined, so the F-measures are not comparable to anything

Second pass §8 item 1: eq. 8.7 gives the formula, but the chapter nowhere says what counts as a true
positive for a grouping boundary, a metrical dot, or a time-span branch. **Confirmed — neither pass
found such a definition, and I did not find one.**

The first pass hedged in the right direction without stating the fact: its L3 note says the comparison
with V5's metrical-feature finding involves *"different corpora, different objects and different
metrics, and no arithmetic joins them."* **The second pass converts that hedge into a stated property
of the paper**, and it is stronger: the numbers are not even internally interpretable as to what they
count. **This bounds every downstream use of 0.46/0.84/0.44/0.77/0.90/0.60/0.48/0.89/0.49.**

Related and also second-pass-only, and it matters under **#21** and **#24**: **no inter-annotator
agreement figure is reported.** Four experts were involved (one analyst, *"three other further experts
crosschecked"*, p. 230) with no agreement rate, no disagreement rate and no resolution procedure.
**The ground-truth ceiling for every figure above is unstated.**

### 3.4 ★ The GTTM feedback links are incompatible with the framework's forward-only boundary contracts

The first pass records the feedback links as facts — GPR7 as *"a link from the time-span and
prolongational trees to the grouping structure"*, MPR9 from the time-span tree to metrical structure
(pp. 220–221) — and draws from them the **dependency-direction** reading (below, §4). It does **not**
connect them to `FRAMEWORK.md` §5.

The second pass does, at its §7.2: the framework's boundary contracts are **forward only**, with
**"L3 → L2: Nothing"**; GPR7, TSRPR5 and MPR9 are backward links; therefore *"a hierarchical reading
of the GTTM kind, as implemented here, is not achievable under a forward-only contract without
dropping GPR7/TSRPR5/MPR9 — which is exactly what ATTA-without-FATTA does (p. 214), and FATTA's
fully-automatic figures (0.48 / 0.89 / 0.49) are the price paid for closing the loop automatically
rather than by hand."*

**This is a chain-level observation of exactly the kind Ruling 2's joint-evaluation widening asked
for, and it is not a falsifier.** It does not say the framework's contracts are wrong; it says the
one working implementation of the alternative R-7 names **requires a link those contracts forbid**,
and that the measured cost of automating that link on its own corpus is that grouping recovers
essentially none of its hand-tuned gain (0.48 against a 0.46 baseline, versus 0.77 hand-tuned).
**Routed to the findings surface as an addition to the chain-level section; it takes no verdict.**

### 3.5 Four author-stated limits the first pass did not carry

All confirmed as quotations; none changes a value.

- **p. 220** — *"multiple implementations of GPR6 are possible, although our system utilizes only
  one."* An arbitrariness admission on the parallelism rule.
- **p. 218** — *"The ATTA may not always produce a result which reflects the user's interpretation."*
- **p. 228** — *"It is difficult to compare the performance of this system with that of previous
  systems because the approaches taken are so different."* The first pass correctly reported that no
  sequence-model comparison appears; **the second supplies the authors' own explicit refusal to
  compare**, which is stronger and is the right citation for DP-O's silence.
- **p. 230** — *"100 pieces from the 300 scores (with human-validated grouping-structure analysis,
  metrical structure, and time-span tree) were utilized."* A sentence the first pass does not carry
  at all, and the one that makes the 300/100 relation legible as far as it goes. **Confirmed at
  p. 230.**

**And an internal inconsistency in the paper's own parameter list, second-pass only:** the default set
on pp. 216 and 230 names **Wr**, which is **not a row in Tables 8.1–8.3** (they list W_m, W_l, W_s).
**Confirmed at p. 230** — the printed default line reads *"Ws,=0.5 Wr =0.5, Wl = 0.5"*. Whether Wr is
a misprint for W_m or a parameter omitted from the tables **is not determinable from the chapter** and
is recorded unresolved.

---

## 4. What the FIRST pass holds that the second does not

Recorded so the pair is not read as one-sided. The doubling paid in both directions.

- **★ The dependency-direction reading, which is the row's single most useful contribution and is
  first-pass-only as a synthesis.** Both passes hold the underlying facts — D_GPR7 consumes Lerdahl's
  tonal pitch space (region distance + chord distance + basic space difference, pp. 214–216); there is
  no automated tonal-pitch-space analyzer (p. 220); ATTA *"utilizes rules based on the results of the
  tonal pitch space approach"* (p. 217). **The first pass draws the conclusion the second leaves
  implicit:** in the most developed implementation of the time-span-reduction line, **the hierarchy
  sits DOWNSTREAM of tonality and harmony, not upstream of them**, and a proposal to use a GTTM-style
  hierarchy *to help decide* harmony meets a circularity that this implementation resolved by
  requiring the harmony first. The second pass instead files the same facts under *"silent on L2's
  core question"* — true but weaker.
- **The parameter-growth quotation, p. 211** (§3.1 above) — first-pass only, and it is half of that
  section's finding.
- **The parameter classification's third category read as the point to notice** — *"Unaware …
  parameters that are not utilized in the original theory, because they lack clear musicological
  meaning"* (p. 211). Both passes quote it; the first foregrounds it.
- **The tractability reading and its cross-link to row 5.** The first pass reads the 46 parameters,
  the *Unaware* class and F ≈ 0.49 automatic together as *"a measured statement about tractability …
  the same shape as HarmTrace's parse-space finding (row 5) from a different direction: a rich
  hierarchical formalism becomes runnable by having something taken out of it or bolted onto it."*
  **The second pass could not have made this link** — row 5 was outside what it was given, correctly.
- **The R-7 framing** — that this is the third of R-7's three named unread alternatives, all now read.
  Also outside the second pass's brief.

**Both passes independently reach the row's load-bearing fact** — that the prolongational reduction,
GTTM's one chord-bearing subtheory, is the one not implemented (p. 209) — **and both quote it
verbatim and identically.** They also independently reach: monophonic-only (pp. 222, 227), the
46-parameter cost, the *Unaware* admission, and DP-O neither supported nor falsified.

---

## 5. ★★ WHAT NEITHER EXTRACT HELD — found by this cross-check, at the page, and it is a caveat on the row's load-bearing fact

Reading p. 232 for this cross-check, **the chapter's own conclusion (§8.7) contradicts its body,
twice, and both extracts missed it.** Verbatim, p. 232:

> *"A music analyzer has been introduced – the interactive GTTM analyzer – which can derive the
> grouping structure, metrical structure, time-span tree, **and prolongational tree** based on GTTM.
> **The analyzer also derives analysis results for chord progressions based on the tonal pitch space
> theory.**"*

**Both clauses conflict with the body, and the second clause conflicts with the reading BOTH extracts
built the row on.**

| Conclusion says (p. 232) | Body says | Independent corroboration |
|---|---|---|
| the analyzer derives the **prolongational tree** | p. 209: *"we have not implemented it at present"* | p. 216: *"A prolongation tree analyzer is also being developed"*; p. 230: *"not included in this, because its analyzer is still under development"* |
| the analyzer **derives chord-progression results** from tonal pitch space | p. 220: *"there is no automated analyzer for tonal pitch space … in the interactive GTTM analyzer"* | p. 217: ATTA *"utilizes rules based on the results of the tonal pitch space approach"* — i.e. consumes them; p. 219: the Tonal Pitch Space **editor** sits on the manual-editor side of Fig. 8.8 |

**THE READING THAT SURVIVES, AND WHY.** The body's statements are **specific, technical, repeated at
three separate pages, and carry a workaround** (*"attempts have been made to implement the tonal pitch
space system, so those results can be used as an input"*, p. 220, ref. [25]). The conclusion's is **a
single summary sentence describing the analyzer-plus-editor suite as a whole**, and the suite does
contain a prolongational tree *editor* and a tonal pitch space *editor* — both manual. **The body
reading stands: neither the prolongational tree nor the chord-progression analysis is automated.**

**But the contradiction is on the record and is not resolved away.** Under the commission's *"resolved
at the paper or recorded as unresolved"*, this is **resolved by weight of evidence, not by the paper
stating which it means** — the paper never reconciles the two — and the distinction matters:

> **★ ROUTING BAR.** Any claim in our documents that this system produces no automated harmonic output
> **must cite pp. 209, 217 and 220. It must never cite the conclusion, and it must not be written as
> though the paper says it once and plainly.** The paper says the opposite once, on p. 232.

**This is the strongest single result of the exercise the user ruled.** It was found by neither reader
alone; it was found by re-reading the pages a disagreement pointed at. **It qualifies the fact the
whole row rests on** — and it is a qualification of *how we may cite it*, not of whether it is true.

---

## 6. Consequences to route — nothing is amended here

1. **The findings surface** gains: the fitted-parameters bound on the 0.77/0.90/0.60 column (§3.1);
   the undefined-P/R and no-inter-annotator-agreement bounds on every figure of the row (§3.3); the
   forward-only-contract observation as a chain-level addition (§3.4); and **the §5 routing bar**.
2. **The bibliography reconciliation** gains the corrected reference-[6] transcription (§2).
3. **`population.md`** records that row 19 now carries a cross-checked double extract, so **§8 is met
   literally for all eight central papers** and the pass's DONE condition is unqualified.
4. **No design point moves. No falsifier anywhere.** Every point this row touches — DP-O above all —
   is underived and open, so nothing here is a STOP under the commission's §6. **DP-O stays open, for
   the sharper reason both passes give independently.**

---

## 7. What this cross-check says about the exercise itself, since the user paid for it deliberately

**The at-the-object read was NOT clean, and the position this side had argued for three times in the
pass's files — that an at-the-object whole read needs no doubling because the double pass catches
relay error — would have kept every one of these defects.** In order of consequence:

1. The headline "configured" column's fitted status, unnoticed (§3.1).
2. A table row reported as a total that cannot be one (§3.2).
3. The metric's undefined terms and the missing agreement figure (§3.3).
4. A verbatim quotation silently corrected (§2).
5. And the paper's own self-contradiction about its most load-bearing fact, which **neither** reader
   caught and the cross-check did (§5).

**None of the five is a relay error.** Four are the reader-class failures — omission, arithmetic,
normalisation — that the row-19 residual surface's fact (c) predicted an at-the-object read would have
no immunity to, and the fifth needed a third look at the page. **The prediction held.**

**The honest counterweight:** no measured value moved, the row's load-bearing fact survived intact,
and the first pass holds the row's single most useful synthesis (§4), which the second did not reach.
**The doubling improved the row's bounds and its citations; it did not change what the row says.**

---

*Provenance: written 2026-08-31 by the third session of the reading pass, under the user's ruling of
the same day (Option A on the row-19 residual surface). The second extraction was performed by a
cleanly separated reader per the commission's own second route; this comparison and every resolution
in it were performed by this session, re-reading pp. 230–234 of the chapter as page images. No
document is amended, no design point is moved, no register row or entry is written, no code is
opened. The workbook was not opened.*

# D-580's transfer cell — the facts, gathered and cited, with nothing decided

> **★ STATUS: A FACT-GATHERING SURFACE. NO VERDICT IS TAKEN HERE**, and none is recommended.
> Written 2026-08-09 (CC, `cc_instruction_return_continuation_4.md` Task 4) on the user's
> **Ruling 27** of `cowork_rulings_2026_08_09_fourth_stop.md`, which carries the user's instruction
> verbatim:
>
> > *"follow the rule: fact based decisions or exploration to gather facts are allowed, not decided
> > on unsure/fabulated/misremembered facts."*
>
> The ruling orders a read-only pass over **D-580**'s and **D-429**'s full records — the two gates'
> purely-local characterization and its measurement basis, the dissolution ruling's scope and its
> carrying ruling's exact words — with **every claim cited at its source** and **anything the record
> does not settle marked UNSETTLED rather than filled**. The user then rules on facts.
>
> **Nothing here authorizes a fix, a design or an inference change.** Phase 1 remains open and #8's
> three-clause gate stands.

---

## 1. The question, stated exactly as it stands

**D-580**'s REACHABILITY verdict is settled and is not in question. Its **TRANSFER** cell —
whether any ruling carries the decision's principle across to the live design — was authored
`undetermined` in the OI-354 establishment, and the user's **Ruling 23** ratified the other ten
verdicts whole while holding **this one cell open pending this pass**.

The cell is undetermined because of a specific tension, and the tension is what the facts below are
about:

- **D-580 carves TWO gates OUT of a dissolution**, saying they must SURVIVE it.
- **D-429 states the principle behind that dissolution**, and a user ruling carried that principle
  across to the live design.

**Does the carve-out ride across with the principle, or was it scoped to a legacy dissolution that
never ran?** That is a ruling, and no session may take it.

---

## 2. The facts, each located at its source

### F1 — What D-580 actually carves out, in its own words

Its home text (`docs/scoring_model.md` §8, the bullet beginning *"Two of the post-scoring gates are
PURELY-LOCAL VERTICAL refinements"*) says:

> Most of the after-the-fact repair steps exist only because the decision preceding them could not
> see enough context, and they disappear once that decision can. Two do not: they refine the reading
> from the notes alone and compensate for nothing, so they are carried across rather than deleted
> alongside the others.

**The carve-out's ground is therefore a property of the two gates — they compensate for nothing —
and not an exemption granted to them.**

### F2 — The measurement basis for "purely-local", and what it measured

D-580's recorded defense says the characterization was *"measured at the code rather than assumed
from the design"*. The measurement is at `cowork_phase2_architecture_review.md`, which records it as
a tally verified at HEAD:

> **CC tally (verified at HEAD): of the 12 live gates, 10 read cross-region/key context =
> compensation; B/C/D are already-removed dead code (Stage 3.4b, byte-identical). ★ Two gates — A
> (Maj-add6↔m7 enharmonic) and J (inverted dom-7 completeness) — are PURELY-LOCAL vertical
> refinements that must be PRESERVED through the dissolution, not deleted with the rest.**

**What that measurement establishes:** which gates READ context beyond their own stretch. **What it
does not address:** whether a gate that reads nothing outside the sonority may nevertheless sit in a
post-hoc layer under D-429's principle. The tally answers *is this compensation?*, not *where does
this belong?*

### F3 — The two named gates at the code, today

- **Gate A is RETIRED.** `src/composing/analysis/chord/postscoringgates.cpp` records, in the comment
  above the surviving rule: *"The surviving rule name for the whole flip is FM2 (Gate A was retired
  at the promotion unification …; the provably-unreachable Gates B/C/D were removed earlier in Stage
  3.4b)."* D-580's own home text states the same bookkeeping fact and adds that **the unification
  did not perform the dissolution and does not discharge this constraint.**
- **Gate J is LIVE in that file**, guarded on `PostScoringRule::GateJ`, and its entry conditions are
  pitch-class arithmetic plus a presence test — a root-position diminished triad whose would-be
  dominant root is also sounding. Its own comment states the reason it cannot misfire: *"A genuine
  standalone vii° / vii°7 never voices the dominant root, so the present-root guard means this cannot
  misfire on real leading-tone chords."*

**Both are consistent with the purely-local characterization**, and the §8 policy for judging a
proposed post-scoring gate states the matching test in its own words: a gate that *"turns on a
structural condition — pitch-class arithmetic plus a presence constraint, not temporal evidence — is
likely architecturally sound."*

### F4 — One condition of the surviving flip is a PRESET preference, and production inference is preset-independent

The surviving flip's entry condition includes `prefs.preferMinorOverMajorAdd6`, which the file's own
comment ties to particular presets (*"When preferMinorOverMajorAdd6 is set (Standard/Baroque)"*).

`CLAUDE.md` gate block (A) records, as a ratified mode decision, that **inference is
PRESET-INDEPENDENT** — presets are presentation concerns.

**This is stated as a fact and not as an argument.** It bears on the question because one of the two
carved-out gates has an entry condition that has no counterpart on a preset-independent arm; it does
not by itself decide whether the carve-out transfers.

### F5 — D-429's principle, its carrying ruling's exact words, and its stated SCOPE

The principle is quoted in the same words at two places in the record. `open_items/OI-226.md` states
it as a block quotation, introduced as *"a principle the user ruled binding on the family design that
will eventually answer this row"*:

> **A correction belongs in a factor's fitted value, never in a layer of after-the-fact corrections
> laid over the decode.**

`ARCHITECTURE.md`'s pointer beside the joint estimator's standing rules states the same principle and
fixes its recording: *"It is not restated as a rule here because it is the same separation rule (a)
makes on the fitting side, and a second copy would be a #6 violation; it is recorded once, at
**D-429**, as a binding constraint on the phase-3 family design."*

**THE SCOPE, as the record states it.** D-429's own provenance records the ruling as binding *"on the
phase-3 family design over the candidate-admission and emission family"*, and names the eight
open-items rows that carry the cross-reference. `open_items/OI-226.md`'s dated cross-reference states
the same scope from the other end — the principle is recorded there as a **phase-3 design constraint
this row's family must satisfy**.

**So the carrying ruling's stated reach is a named family, and the gate layer is not that family.**

### F6 — D-580's own text assigns the disposal to a different route

Its home text closes the point in its own words:

> **The dissolution was never executed on this path** — the production estimator replaced the
> pipeline instead — so the constraint stands DEFERRED and what it says about those two gates is a
> fact about this code that the retirement map still has to dispose of (#12).

**D-580 therefore names the retirement map, not the phase-3 family design, as what has to dispose of
its content.** That is the entry's own account of where its unfinished business goes.

### F7 — Neither gate is reachable on the production arm

D-429's own provenance records the control-flow finding, established at the code rather than assumed:
the joint module contains no reference to the legacy chord path's symbols, the record adapter does
not either, and all four notation seams return the record path when the record flag is set — which is
its default. The gate layer is reached only through the enumerated non-default paths.

**And the joint module carries no construct of the added-sixth kind** — a search of
`src/composing/analysis/joint/` for that term returns nothing. **What that does NOT establish**, on
exactly the reasoning `OPEN_ITEMS.md` OI-357 applies to a neighbouring question: absence of a named
construct is not absence of the behaviour, since a factor model may express the same content without
carrying the legacy rule's name.

### F8 — The retirement map, which D-580 names as its disposal route, records NO carve-out

D-580 routes its unfinished business to the retirement map (F6). That map is in
`docs/implementation_roadmap.md`, under the heading *"Retirement map (nothing retires by silence)"*,
and its first entry reads:

> R1 legacy chord competition + Gates A–L (E4, or Stage 5 if first — the OWED refactor #2)

**R1 names Gates A–L as a whole. It does not name Gate A or Gate J as surviving, and it records no
exception of any kind.**

**This is stated as a located fact and not as a contradiction to be resolved here.** Two recorded
items describe the same subject differently: D-580 says two of the gates must SURVIVE the
dissolution, and R1 — the route D-580 itself names — retires Gates A–L without qualification. **Which
governs, or whether the two are about different acts (a dissolution INTO the competition versus a
deletion of the legacy path), is not settled by any text this pass found, and is not settled here.**

---

## 3. What the facts SETTLE

1. **The carve-out's ground is a measured property of the two gates**, not an exemption (F1, F2).
2. **The measurement behind "purely-local" answers a different question from the one D-429's
   principle asks.** It establishes which gates read outside their own stretch; it does not address
   where a non-compensating refinement belongs (F2).
3. **One of the two carved-out gates no longer exists under its own name**, its surviving half being
   a rule of the unified promotion primitive; the other is live in the legacy file (F3).
4. **The carrying ruling's stated scope is the phase-3 candidate-admission and emission family**, and
   the gate layer is not a member of it (F5).
5. **D-580's own text routes its unfinished business to the retirement map**, not to that family
   design (F6).
6. **Neither gate is reachable on either production surface** (F7).
7. **The retirement map D-580 names as its disposal route records NO carve-out for the two gates** —
   its R1 retires Gates A–L as a whole (F8). So the routing D-580 relies on does not, as it stands,
   carry the exception D-580 asserts.

## 4. What the record does NOT settle — marked UNSETTLED rather than filled

- **UNSETTLED — whether a principle ruled binding on one named family reaches a decision outside it.**
  The record states the scope (F5) and states D-580's own routing (F6). It does not say whether the
  two are alternatives, whether one supersedes the other, or whether both are true of different halves
  of D-580's content. **No text in the record addresses the question.**
- **UNSETTLED — whether a purely-local vertical refinement is a "correction" in the principle's
  sense.** The principle forbids *a layer of after-the-fact corrections laid over the decode* (F5).
  D-580's carve-out asserts its two gates *compensate for nothing* (F1). The record contains no
  statement reconciling those two descriptions, and the §8 policy's structural test (F3) is about
  whether a gate is architecturally sound, not about whether it may sit after a decode.
- **UNSETTLED — whether the live estimator already expresses either gate's content as a factor.** The
  joint module carries no construct of the added-sixth kind (F7), and no document consulted states
  whether the model's factors cover the two readings. Absence of a name is not absence of the
  behaviour.
- **UNSETTLED — what the preset-independence fact implies for the carve-out.** F4 is a fact about one
  gate's entry condition and about the production arm's mode decision. The record nowhere connects
  them, and connecting them would be an inference this pass does not make.
- **UNSETTLED — which of the two conflicting records governs the two gates' fate.** F8 establishes
  that the retirement map's R1 retires Gates A–L as a whole while D-580 says two of them must survive.
  **The conflict is now located; what is not settled is its resolution.** Two readings are visible and
  the record states neither: that R1 simply predates or overlooks the carve-out; or that the two speak
  of different acts — a DISSOLUTION into the competition, which is what D-580's carve-out is about,
  versus a DELETION of the legacy path, which is what R1 performs, in which case both are true and the
  carve-out's content has nowhere to survive TO unless the live design carries it. **Nothing in the
  record chooses between them, and this pass does not.**

## 5. What this file does NOT do

It takes **no transfer verdict** and recommends none. It proposes no fix, no design and no inference
change. It moves no status, no home and no register entry, and assigns no identifier. It touches no
`src/`, no golden, no corpus of scores and nothing in `tools/robust_stop/`.

**No claim above rests on memory.** Every quotation is taken from the file it is attributed to, read
in place; where a fact could not be established, it is in §4 rather than in §3.

**Phase 1's completion statement is not written, not drafted and not partially written here.**

*Provenance: the user's Ruling 27 of 2026-08-09 (`cowork_rulings_2026_08_09_fourth_stop.md`), which
holds D-580's transfer cell UNDETERMINED pending this pass and states that the user then rules on
facts. The cell's authored `undetermined` verdict and its ground are at
`ratification_surfaces/cowork_oi354_legacy_mark_establishment_2026_08_09.md` §3 and, as applied, in
`tools/audit/decisions/gen_phase1w_legacy_verification.py`'s verdict table.*

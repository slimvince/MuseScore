# PLAN v4 — reconstructing the specifications, fact-based, depth-varied, and written to be attacked

> **STATUS: DRAFT FOR THE USER'S RATIFICATION. NO WORK BEGINS UNTIL THIS PLAN IS RULED.**
> Cowork, 2026-08-19, at branch tip `891bacc5d2`. It orders no act, touches no document, moves no
> candidacy. **Supersedes v3 of the same date**, withdrawn and preserved on disk (#12).
>
> **★ §15 IS THE ATTACK SURFACE.** The brief to the reviewing side is *refute these*, never *assess
> these*. **A review returning "the plan looks sound" is a failed review.**

---

## 0. What changed from v3 — the reading depth is no longer uniform

v3 read every section to the same depth. That is wrong in both directions: it over-reads areas music
theory settles by itself, and under-reads areas where the value is entirely in what this project
measured. **Depth now varies, is declared before reading, and is ratified with the source list** (§4,
B1), so it is a stated decision rather than discretion exercised mid-pass — discretion mid-pass being
how the previous programme grew.

Five things bear on depth. **Four are derived** and one is not:

| what bears on depth | derived from |
|---|---|
| **Blast radius** — how many later sections consume this one | the dependency order (a wrong segmentation statement corrupts chord tones, root, bass and key; a wrong emission statement corrupts one label) |
| **Error mass** — how much measured failure this section accounts for | A4's clustering of the failing runs |
| **How much theory settles** — what a first-inversion triad is, theory settles; where a boundary falls in chorale texture, it does not | authored per section, with its reason |
| **Density of prior attempts** — where many attempts were made, many dead ends were recorded, and that is where irrecoverable knowledge lives | **the size of the declared source list at B1, which exists before any reading** |
| **★ What the system is meant to become** — an area may matter because of where the project is going rather than because of anything currently measurable | **NOT DERIVABLE. The user's, and reserved to the user.** |

---

## 1. The facts this plan rests on

Each established during the sitting that produced it, at a git object by explicit hash or by opening a
snapshot with the file tools.

| fact | established at |
|---|---|
| The instruction that caused the pollution is dead; a specification/code disagreement is now evidence reserved for the audit | `CLAUDE.md`, read in full |
| No artifact in `tools/audit/` takes either specification's provenance as its subject | `git ls-tree` + `git grep` at `891bacc5d2` |
| `ARCHITECTURE.md` 532,289 bytes; 19 numbered sections, the joint-estimator standing rules, 2 appendices | git object read (headings only; body unread) |
| `docs/scoring_model.md` 127,593 bytes; ratified banner states its mechanism content describes a scorer **dormant on both production surfaces**; §8's constraints remain in force | staged snapshot, file tools |
| Every hand-set scoring magnitude on that surface is declared **UNFALSIFIED, NOT ESTABLISHED** | `docs/scoring_model.md` §8 |
| `DEFECT_TYPES.md` is 26 rows of **engineering and method** defect types, carrying almost no musical knowledge | read in full |
| Decisions register: 677 entries — 411 with a nameable deciding act, 182 with none, 84 ambiguous | `decisions_filter_classification.json` |
| Of the 411: 244 design intent, 167 implementation management, 0 needing the user | `rulings_sort_classification.json` |
| Project markdown: 21.79 MB across 1,211 files, roughly 13 MB of it process record | `git ls-tree -r -l`, summed |
| The phase-1 finish line publishes nine gating items and quotes, inside itself, the banner announcing its own supersession | `phase1_finish_line.json` |
| Production baselines: root 77.03 %, Roman numeral 64.12 %, key against local 78.42 %, against global home 56.14 %, at 326/352 coverage, preset-independent | `CLAUDE.md` gate block (A) |
| A wider search cannot reach the arpeggio root failure — the wrong reading is the global optimum; only re-weighting or a different segmentation reaches it | `docs/scoring_model.md` §8 |
| The third-above ambiguity is non-local; two discriminators were built and both regressed | `docs/scoring_model.md` §8 |
| The progression contradiction does not predict which root is correct: the vertical commit is the better predictor even where the alternative is its vertical equal | `docs/scoring_model.md` §8, **D-490 FALSIFIED** |

---

## 2. What is AUTHORED here, and therefore challengeable

- That a document's **section structure** is less polluted than its sentences.
- That **deriving blind before reading** beats the reverse.
- That the work is **separable per section at all**.
- That **three depth tiers** are the right granularity, and that the five axes at §0 are the right axes.
- That **depth can be decided before reading**.
- The **order** of the phases and steps, and the **guardrails** at §9.

---

## 3. PHASE A — establish the frame and prove the format, before any content work

**A1 — Derive the document set.** The documents that specify the analysis are the **home population**
admitted by the delegation bar (`CLAUDE.md` decisions-register rules (g)–(k), applied over the whole
home population 2026-08-03, generated and never hand-classified). Read that derivation rather than
listing documents by hand.

**A2 — Enumerate the frame at the current versions**, from headings alone. Mechanical.

**A3 — Enumerate every section ever DELETED from those documents.** The only place history is consulted
at this phase, because **a removed section is a dropped perspective and is invisible in the present text
by construction.** Mechanical, from git.

**A4 — CC reconciles the frame against three populations Cowork cannot reach**, both ways, halting on
anything unplaceable: the decisions the implementation actually makes; the fields of the ground-truth
annotation schema; **the failing runs clustered by which decision they turn on — which also produces the
error mass per section that feeds both the ordering and the depth tier.**

**A5 — The frame test, which catches a category error rather than a missing member.** A **declared sample
of 60 statements** drawn from outside the frame — ruling records, decision surfaces, dossiers, DEFERRED
register entries, the evidence inventory, declared dormancies — each **placed**. **An unplaceable
statement is a finding about the FRAME.** Adversarial by construction: *place these, report every one you
cannot.* **Run by CC, not by the side that authored the frame.**

*Why A4 cannot replace A5:* a both-ways reconciliation runs INSIDE a frame, so a missing axis produces
agreement on both sides. The gap that produced v2 was found by placing one real example — a
chord-progression library — and watching it not fit.

**A6 — Prove the statement format before anything is written in it.** Cowork writes **five** statements in
the §5 form, deliberately of different kinds: a boundary rule, a knowledge item, an enablement constraint,
a numeric threshold, an abstention rule. **CC judges from the delta side whether field five is sufficient
to return conforms / diverges / not implemented / undocumented-extra without interpretation.** If it is
not, the format is fixed here — not after ten sections have been written in it.

**Output:** a ratified frame with its derivation, its exclusions, the unplaceable statements, the error
mass per section, and a format proven usable. **Phase B does not begin until it is ruled.**

---

## 4. PHASE B — per section of the ratified frame

**B1 — Declare the sources AND the depth tier, before reading, and show both.**

The sources: the passages of every A1 document covering the section; **every deletion from those
passages**; the register entries whose subject it is; the `docs/scoring_model.md` §8 constraints that bind
it; the `DEFECT_TYPES.md` rows that apply; the code sites; the failing runs that turn on it.

The depth tier, from a **closed set of three**:

| tier | what is read |
|---|---|
| **Shallow** | current text and register entries. **No history walk.** |
| **Standard** | plus every deletion from those passages, the §8 constraints, the code sites |
| **Deep** | plus the region's full history, the process record searched for the vocabulary of intent, and the failing runs read **individually** rather than as a cluster |

**Proposed by Cowork with its evidence** — blast radius from the dependency order, error mass from A4,
theory-settlement with its reason, prior-attempt density from the size of the source list itself —
**and ratified by the user**, whose own axis (§0, row five) is not derivable and governs.

Sources and tier are then **fixed for the pass**.

**B2 — Derive blind.** Write what the section should say from music theory, the published research and the
annotated corpus, with the current text and the code **closed**. Every statement carries its defense in the
same breath. What cannot be settled is written as an open question, never filled with the most plausible
reading.

**B3 — Open the declared sources and grade the derivation.** Four outcomes, closed set: **confirms** →
stands, cited · **contradicts** → open question, both readings stated · **adds** → salvage, admitted with
its own defense · **records a dead end the derivation walked into** → the statement is withdrawn, *and this
is the measurement of whether the derivation method can be trusted at all.*

**B4 — Reconcile into a statement set** in the form of §5.

**B5 — ADVERSARIAL READ, by CC, before the user sees it.** Brief: *refute these statements.* Find the
defense that does not support its statement; the statement that contradicts a recorded dead end; the
statement whose only support is the implementation; the field five that cannot be checked. **A review
returning "sound" is not a completed review.**

**B6 — Ratification.** One surface: the statements, the open questions, the sources read, the tier and its
reason, the exclusions, and what B5 refuted. No question in the turn that delivers it.

**B7 — Land it**, under §6.

---

## 5. The form of every statement

Atomic — **one rule per statement** — with five fields: **the statement**; **its defense** (music theory,
published research, or measurement — *"because the implementation does this"* is not a defense, and a
statement supported only by the code is marked UNSUPPORTED); **its source class** (derived · salvaged ·
measured); **its status** (settled · open); **what would falsify it in code**. A6 proves the fifth field is
writable before the format is committed to.

---

## 6. The end state, declared now rather than discovered later

**Two specifications of one system would violate #6.** The interim is therefore declared as a **bounded
migration under #23** — a temporary, declared, pre-ratified violation of an end-state principle, with a
retirement map.

- While the programme runs, new sections accumulate as their own document and `ARCHITECTURE.md` stands
  unedited. **The two-document state is the declared transition, not an oversight.**
- As each section is ratified, the passages it covers are marked **superseded by the new section**, with the
  former wording preserved in place (#12). Nothing is deleted.
- **The terminus is one ratified replacement**, at which `ARCHITECTURE.md` becomes the new text or becomes a
  pointer to it — **ruled at the start, not at the end** (§14), because a migration with no ruled terminus is
  how the last one ended.

---

## 7. What runs BESIDE this plan and is not gated by it

**The ground-truth ceiling — `OPEN_ITEMS.md` OI-179.** `CLAUDE.md` #21 establishes that no published
per-axis annotator-agreement value exists for this repertoire; that BCMH and the Mozart sonatas are
consensus-built and can never yield one; that ABC has no overlap by design — while **TAVERN released
duplicate annotations that were never computed**, and Dilemmadata identifies dual-annotated pieces and
computes nothing. It is a #19 obligation, so it **always gates whatever its subject**, it is computable from
data that already exists, and it is independent of this plan. **Until it exists, no residual on any axis can
be interpreted.**

Nothing else is claimed as parallel.

---

## 8. What is read

**Once, standing for the whole programme — three of four done:** `CLAUDE.md` principles and conventions ✔ ·
`CLAUDE.md` gate block and its reading caveats ✔ · `DEFECT_TYPES.md` ✔ · `docs/scoring_model.md` §8 — read to
line 1328, **about 130 lines remain**.

**Derived at A1:** the document set. **Declared per section at B1**, with its tier, before it is read.

---

## 9. Guardrails

1. A pass produces statements, an open-questions list and a findings note — **nothing else**.
2. Findings attach to their section; **no numbers, no rows**.
3. **No mechanism is built during a pass.** What needs a tool is recorded as unchecked, with its reason.
4. Sources **and tier** declared before reading; **never extended mid-pass**.
5. **Every phase and every unit carries a declared budget**; overrun is a stop, not a continue.
6. The done condition is written **before** the work starts.
7. **No ruling is taken during a pass.**
8. One file per unit; **no record about the record**.
9. A ratified unit is **closed**.
10. The frame is closed once ratified; an addition is the user's.
11. **One tell at every pass end:** *did this pass produce anything other than statements, open questions and
    a findings note? If yes — name it.* **A proposal to build something that checks these guardrails is
    itself the tell firing.**

---

## 10. Stop conditions

A declared source cannot be located · the derivation and the record contradict on a point the pass cannot
leave open · a budget is reached · a unit turns out not to be separable from another · the pass would have to
build something, change code, or take a ruling to continue.

**The tier branch:** a section that opens and proves to need a deeper tier than was declared is a **STOP and
a request to raise it**, never a silent expansion. Without that clause, *this one is important* becomes every
one.

**The frame branch:** if A5 cannot place **more than ten of its sixty** sampled statements, the frame is the
wrong frame. **That is a STOP to the user and a rebuild is a different act needing its own ruling.**

A stop records what was done, what was not, and that the remainder is untouched rather than half-worked.

---

## 11. Budget

**Phase A:** one working session for A1–A3, one for A4–A5, one for A6. Overrun on any is a stop.

**Phase B:** budgeted **per tier, not per unit** — because a shallow unit and a deep unit are not the same
job and one number for both was always going to be wrong. **The first unit at each tier is done alone and
measured** — effort, statements produced, salvage found, open questions raised, how much of the declared
reading mattered, what B5 refuted — and those numbers set that tier's budget. No number is fixed here,
because no honest basis for one exists yet.

---

## 12. Done conditions

**Phase A:** frame derived at A2 and A3, reconciled both ways at A4, tested at A5 with every unplaceable
statement listed, format proven at A6, and the whole ratified.

**Per Phase-B unit:** every statement carries its five fields; every open question listed rather than filled;
sources, tier and exclusions recorded; B5's refutations answered; ratified.

**The whole:** every section of the ratified frame reconstructed and the terminal replacement of §6 performed
— described as *the best reconstruction obtainable from the named sources at the ratified depth, with these
open questions*, and never as *correct*.

---

## 13. What this plan does NOT do

No `src/` change, no build, no test, no measurement tool, no guard run. Nothing deleted, archived or moved. No
open-items row created, flipped or discarded. No finding number allocated. No pin taken. It does not measure
how polluted the documents are and does not need to. It does not recover provenance. It does not repair the
decisions register. It does not re-open any ruling. **It does not authorize the delta analysis against the
implementation**, which is a separate act under its own ruling.

---

## 14. Open questions for the user at ratification

1. **Is the structure kept, tested-then-kept, or rebuilt?**
2. **At the terminus, does `ARCHITECTURE.md` become the new text, or a pointer to it?** (§6.)
3. **Does this replace the ruled PILOT phase, or execute it?**
4. **Is the curated boot list still needed?**
5. **Is `docs/scoring_model.md` in the frame at all**, given its subject is dormant on both production
   surfaces and awaits the OI-180 retirement map?
6. **Is #8 scoped for §7's parallel track?**
7. **Are three tiers the right granularity**, and is the depth decision yours per section or delegated once?

---

## 15. ★ THE ATTACK SURFACE — for the reviewing side

**REFUTE, do not assess.** Each item is load-bearing: if it falls, the plan changes or dies. Each names what
would refute it.

**L1 — Section structure is less polluted than sentences.** *Refuted by:* finding sections of
`ARCHITECTURE.md` that exist because a code module exists — §3 Directory Structure is the obvious candidate —
or by showing the structure was itself edited under the doc-sync programme.

**L2 — A specification statement can carry a code-falsifiable condition.** *Refuted by:* taking A6's five
statements and showing field five cannot be written, or cannot be checked without judgment, for one or more.
**This one would invalidate the entire output after all the work is done.**

**L3 — The problem is separable per section at all.** *The deepest risk, and it comes from the domain.* Key
and chord are mutually determining; **the production layer is a JOINT estimator precisely because they cannot
be decided independently.** A specification split into independent sections may produce statements that are
individually defensible and jointly incoherent. *Refuted by:* showing the joint estimator's own standing rules
cannot be stated as per-section statements without loss.

**L4 — Failing runs can be attributed to a section at all.** *Refuted by:* clustering them and finding most
are multi-causal, which would make the error-mass input to both ordering and depth meaningless.

**L5 — The annotation schema is a valid enumeration of what the analysis must decide.** Annotators record
**conclusions**, not decisions. *Refuted by:* naming a decision the analysis must make that no annotation
field reflects.

**L6 — The delegation-bar home population is the right document set.** It was derived for a different purpose.
*Refuted by:* naming a document that specifies the analysis and is not in it, or one in it that specifies
nothing.

**L7 — Deriving blind before reading beats the reverse.** *Refuted by:* showing blind derivation on this
subject produces so little that the check dominates, making the ordering waste.

**L8 — Phase A terminates.** A3 walks the deletion history of every A1 document. *Refuted by:* measuring that
history and finding it does not fit the declared budget.

**L9 — Depth can be decided BEFORE reading.** The tier rests on evidence available in advance — mass, blast
radius, source-list size. *Refuted by:* showing that whether a section is contested is only discoverable once
it is open, in which case the tier is systematically wrong and the stop at §10 fires every time, which is not
a tier system but a delay.

**L10 — Three tiers are enough, and the five axes are the right axes.** *Refuted by:* naming a section that
fits no tier, or an axis that changes the answer and is on neither list.

---

*Provenance: Cowork, 2026-08-19, at branch tip `891bacc5d2`, in the remote Cowork environment. Every fact in §1
was established at a git object by explicit hash or by opening a snapshot staged through the device bridge with
the file tools. `CLAUDE.md` was read in full by the drafting session, lines 1–1844; `DECISIONS.md` was read in
full BY DELEGATION, which is a departure and not a discharge. `git status` was not run — it is measured to time
out on this mount. §2 and §15 state what is authored; everything else is cited to where it was established.*

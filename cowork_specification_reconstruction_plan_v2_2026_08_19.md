# PLAN v2 — reconstructing the specifications, fact-based

> **STATUS: DRAFT FOR THE USER'S RATIFICATION. NO WORK BEGINS UNTIL THIS PLAN IS RULED.**
> Cowork, 2026-08-19, drafted at branch tip `891bacc5d2`. It orders no act, touches no document,
> moves no candidacy and opens no question. **It supersedes the v1 plan of the same date**, which is
> withdrawn for the reasons at §0 and preserved on disk (#12).

---

## 0. What changed from v1, and why — three corrections, each forced by a fact

**(1) The ten questions are WITHDRAWN.** They were authored by Cowork in conversation and carried into
v1 as the unit of work. They were an ASSUMPTION under #17(a), not a derivation, and at least five
candidate gaps were visible on inspection — metric position, cadence, mode, abstention, voice
structure. **A plan whose unit of work is invented is not fact-based.**

**(2) The unit was also the WRONG SHAPE, not merely under-derived.** "Questions the analysis answers"
cannot hold a thing the analysis *knows* — a chord-progression library answers no question — nor a
requirement that the implementation *not preclude* something it does not yet do. Both classes are
real and both are ratified concerns of this project: `CLAUDE.md`'s fact-publication corollary
(2026-07-10, amended 2026-07-12) requires an unconsumed derived fact to be either **declared dormancy
with its future consumer named** or waste, and requires evidence-class facts to be **published broadly
even without a named consumer**. That is "enable but do not do yet", already ruled.

**(3) The frame already exists and is not Cowork's to invent.** `ARCHITECTURE.md` — which **D-091**
makes the canonical architecture document that wins every disagreement — already carries the
perspectives v1 was reaching for: §5 Planned Analysis Extensions, §7 The Knowledge Base, §8 Planned
Generation Components, §9 The Constraint System, §14 ML Readiness, §6 The Style System, and §10–§13
(Visualization, Intonation, User Interface, File Persistence), which are consumers of the analysis
rather than parts of it. **Read at the git object; the body is unread.**

**And the correction that governs all three:** `ARCHITECTURE.md` is **one of several polluted
documents, not the polluted document** — and there is nothing better available, unless the historical
versions are read as well. A section that was once there and was removed is a perspective that was
dropped, and it is invisible in the present text by construction.

---

## 1. The facts this plan rests on

Every one established during the sitting that produced it, at a git object by explicit hash or by
opening a snapshot with the file tools.

| fact | where it was established |
|---|---|
| The instruction that caused the pollution is dead; a spec/code disagreement is now evidence reserved for the audit | `CLAUDE.md`, read in full |
| No artifact in `tools/audit/` takes either specification's provenance as its subject | `git ls-tree` + `git grep` at `891bacc5d2` |
| `ARCHITECTURE.md` 532,289 bytes, 19 numbered sections + the joint-estimator standing rules + 2 appendices | git object read |
| `docs/scoring_model.md` 127,593 bytes; its ratified banner states its mechanism content describes a scorer **dormant on both production surfaces**; §8's constraints "remain in force" | staged snapshot, file tools |
| Every hand-set scoring magnitude on that surface is declared **UNFALSIFIED, NOT ESTABLISHED** | `docs/scoring_model.md` §8 |
| `DEFECT_TYPES.md` is 26 rows of **engineering and method** defect types — it holds almost no musical knowledge | read in full |
| The decisions register: 677 entries, 411 with a nameable deciding act, 182 with none, 84 ambiguous | `decisions_filter_classification.json` |
| Of the 411, 244 are design intent and 167 implementation management; 0 need the user | `rulings_sort_classification.json` |
| Project markdown: 21.79 MB across 1,211 files, of which roughly 13 MB is process record | `git ls-tree -r -l`, summed |
| The phase-1 finish line still publishes nine gating items and quotes, inside itself, the banner announcing its own supersession | `phase1_finish_line.json` |
| The preparation phase's five ruled outputs: two done, one drafted 2026-08-19, one never built, one measured but not run | phase-definition surface §3.1; tree search |

---

## 2. What in THIS plan is authored, and is therefore challengeable

Stated so it is not mistaken for derivation.

- That a document's **section structure** is less polluted than its sentences. Reasoning, not measured:
  a sentence written from the code is the ordinary case, a section created because a module exists is
  rarer and more visible. **Unmeasured. §3's A3 is what tests it.**
- The **order** of the steps, and that the frame is settled before any content work.
- The **guardrails** at §7 — each is aimed at an observed failure, but the guardrail itself is authored.

Nothing else in this plan is authored. Where a fact is missing, the plan says so rather than filling it.

---

## 3. PHASE A — establish the FRAME before any content work

The frame is the set of perspectives a specification of this system must cover. **It is derived, not
composed.**

**A1 — Derive the document set.** The documents that specify the analysis are already computed: they
are the **home population** admitted by the delegation bar — `CLAUDE.md`'s decisions-register rules
(g)–(k), applied in one pass over the whole home population on 2026-08-03, generated and never
hand-classified. **This plan reads that derivation rather than listing documents by hand.** It is the
one part of the register apparatus that bears directly on this work.

**A2 — Enumerate the frame at the current versions.** The section structure of every document in the
A1 set, from the headings alone. Mechanical.

**A3 — Enumerate the frame's HISTORY: every section ever deleted.** For each document in the A1 set,
the sections that once existed and no longer do. **This is the only place history is consulted at this
phase**, and it is consulted because a removed section is a dropped perspective and is invisible in
the present text by construction. Mechanical, from git.

**A4 — CC reconciles the frame against three populations Cowork cannot reach.** Both ways, halting on
anything unplaceable: the decisions the implementation actually makes; the fields of the ground-truth
annotation schema; the failure clusters in the corpus. **Nothing in the frame that no population
supports; nothing in any population the frame cannot hold.**

**A5 — The frame test, which is the step that catches a CATEGORY ERROR rather than a missing member.**
Draw real statements from outside the frame — ruling records, decision surfaces, dossiers, the DEFERRED
register entries, the evidence inventory, the declared dormancies — and **attempt to place each one**.
**An unplaceable statement is a finding about the FRAME.** It is run adversarially by construction —
*place these; report every one you cannot* — and never as *does this frame look complete?*, which
reconciles inside whatever frame it is handed and comes back satisfied. This is the audit protocol's
own P5 shape.

*Why A5 exists and A4 cannot replace it:* a both-ways reconciliation runs INSIDE a frame, so a missing
axis produces agreement on both sides. The gap that produced this v2 was found by placing one real
example — a chord-progression library — into the frame and watching it not fit.

**Phase A's output:** a frame, ratified, with its derivation, its exclusions, and the statements A5
could not place. **Phase B does not begin until it is ruled.**

---

## 4. PHASE B — per section of the ratified frame, reconstruct the content

The unit is **one section of the ratified frame.** Steps, in this order and no other.

**B1 — Locate and declare the sources, and show the list before reading it.** For that section: the
passages of every A1 document that cover it; **every deletion ever made from those passages**; the
register entries whose subject it is; the `docs/scoring_model.md` §8 constraints that bind it; the
`DEFECT_TYPES.md` rows that apply; the code sites; the failing runs that turn on it. Fixed for the
pass once shown; never extended mid-pass.

**B2 — Derive blind.** Write what this section should say, from music theory, the published research
and the annotated corpus, with the current text and the code **closed**. Every statement carries its
defense in the same breath. What cannot be settled is written as an open question, never filled with
the most plausible reading.

**B3 — Open the declared sources and grade the derivation.** Four outcomes, a closed set:
**confirms** → the statement stands, cited · **contradicts** → an open question, both readings stated ·
**adds** → salvage, admitted with its own defense · **records a dead end the derivation walked into** →
the statement is withdrawn, *and this is the measurement of whether the derivation method can be
trusted at all.*

The order of B2 and B3 is load-bearing: reading first anchors the derivation, reading after tests it.

**B4 — Reconcile into a statement set** in the form of §5.

**B5 — Put it up for ratification** as one surface: the statements, the open questions, the sources
read, and what was excluded and why. No question in the turn that delivers it.

**B6 — Land it beside the old text.** The ratified section stands as its own document; the passages it
covers are re-bannered as reference. **Nothing is deleted; no former wording is lost.**

---

## 5. The form of every statement

Atomic — **one rule per statement**, because a paragraph cannot be compared against code — carrying
five fields: **the statement**; **its defense** (music theory, published research, or measurement —
*"because the implementation does this"* is not a defense, and a statement supported only by the code
is marked UNSUPPORTED); **its source class** (derived · salvaged · measured); **its status** (settled ·
open); and **what would falsify it in code**, without which the later comparison is interpretive rather
than mechanical.

---

## 6. What is read, stated as documents rather than as classes

**Read once, standing for the whole programme — three of four already done:** `CLAUDE.md`'s principles
and conventions ✔; `CLAUDE.md`'s gate block with the measured baselines and the caveats on reading them
✔; `DEFECT_TYPES.md` ✔; `docs/scoring_model.md` §8 — read to line 1328, **about 130 lines remain**.

**Derived at A1, not listed here:** the set of documents that specify the analysis.

**Found per section at B1**, and shown before it is read.

---

## 7. Guardrails

1. A pass produces statements, an open-questions list and a findings note — **nothing else**.
2. Findings attach to their section; **no numbers, no rows**.
3. **No mechanism is built during a pass.** What needs a tool is recorded as unchecked, with its reason.
4. Sources declared before reading; **never extended mid-pass**.
5. A declared budget per unit; **overrun is a stop, not a continue**.
6. The done condition is written **before** the work starts.
7. **No ruling is taken during a pass**; open questions accumulate to one ratification.
8. One file per unit; **no record about the record**.
9. A ratified unit is **closed**; re-opening takes the user's word.
10. The frame is closed once ratified; an addition is the user's, never a session's.
11. **One tell, checked at every pass end:** *did this pass produce anything other than statements, open
    questions and a findings note? If yes — name it.* Checked by the user reading one short thing.
    **A proposal to build something that checks these guardrails is itself the tell firing.**

---

## 8. Stop conditions

A declared source cannot be located · the derivation and the record contradict on a point the pass
cannot leave open · the budget is reached · the unit turns out not to be separable from another · the
pass would have to build something, change code, or take a ruling to continue. **A stop records what
was done, what was not, and that the remainder is untouched rather than half-worked.**

---

## 9. Budget and cadence

**Phase A is done and measured before any budget is set for Phase B.** The first Phase-B unit is then
done alone and measured — effort, statements produced, salvage found, open questions raised, and how
much of the declared reading mattered. **Those numbers set the budget for the rest.** No number is
fixed here, because no honest basis for one exists yet.

---

## 10. Done conditions

**Phase A:** the frame is derived from A2 and A3, reconciled by A4 in both directions, tested by A5
with every unplaceable statement listed, and ratified.

**Per Phase-B unit:** every statement carries its five fields; every open question is listed rather than
filled; sources read and exclusions recorded; ratified.

**The whole:** every section of the ratified frame reconstructed — described as *the best reconstruction
obtainable from the named sources, with these open questions*, and never as *correct*.

---

## 11. What this plan does NOT do

No `src/` change, no build, no test, no measurement tool, no guard run. Nothing deleted, archived or
moved. No open-items row created, flipped or discarded. No finding number allocated. No pin taken. No
existing specification text edited before a ratified section covers its subject. It does not measure how
polluted the documents are and does not need to. It does not recover provenance. It does not repair the
decisions register. It does not re-open any ruling. **It does not authorize the delta analysis against
the implementation**, which is a separate act under its own ruling.

---

## 12. Open questions, for the user at ratification

1. **Is the structure kept, tested-then-kept, or rebuilt?** This plan tests it (A3, A5) and keeps what
   survives. Rebuilding from nothing is available and is not assumed.
2. **Does this replace the ruled PILOT phase, or execute it?** The 2026-08-15 six-phase ruling aims the
   pilot at `docs/scoring_model.md` derived blind — the same shape as B2/B3, but aimed at a document
   whose own ratified banner says its mechanism content describes a **dormant** scorer. Unsettled here.
3. **Is the curated boot list still needed?** Drafted 2026-08-19 as the pilot's prerequisite; if this
   plan replaces the pilot's shape, it may fall away.
4. **Who runs A4 and A5 — CC, or Cowork?** A4 needs the code, the corpus and the annotation data, so CC.
   A5 could be either, but a side that authored the frame is the wrong side to test it.
5. **Does Phase A's frame cover `docs/scoring_model.md` as well**, or is the legacy scorer out of scope
   given it is dormant on both production surfaces and awaiting the OI-180 retirement map?

---

*Provenance: Cowork, 2026-08-19, at branch tip `891bacc5d2`, in the remote Cowork environment. Every
fact in §1 was established at a git object by explicit hash or by opening a snapshot staged through the
device bridge with the file tools. `CLAUDE.md` was read in full by the drafting session, lines 1–1844;
`DECISIONS.md` was read in full BY DELEGATION, which is a departure and not a discharge. `git status`
was not run — it is measured to time out on this mount. No value in this file is transcribed from a
surface that repeats it. §2 states what is authored; everything else is cited.*

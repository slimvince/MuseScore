# CC instruction — the OI-207 decision-conformance adjudication: build the decisions register from the layer specifications, and give every one of the 15,224 harvested statements a recorded disposition

> **★ THIS DISPATCH IS FOR THE HIGHER-CAPACITY SESSION.** It is the one the whole preparation arc
> was for. It is large, and a **feasibility stop with a proposed partition is an accepted and
> expected outcome** — the same outcome the Layer-4, Layer-5 and OI-199 pass-1 audits reached.
> Stopping honestly beats finishing thinly.
>
> **Read first (every session):** `C:\s\MS\CLAUDE.md` IN FULL — in particular the Conventions
> entries **never work from memory instead of documented facts** (open the primary source and cite
> it, file:line; being right from memory does not satisfy it), **music-theory words are reserved
> for their musical meaning — the bare word is always the musical one**, and the pointer to
> **`cowork_design_doc_template.md`**, the home of this project's writing standards (predicates
> must be qualified; defined terms, plain vocabulary, no shorthand). Also `C:\s\MS\STATUS.md`,
> `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\OPEN_ITEMS.md` (INDEX), and these detail files:
> **`open_items/OI-208.md`** — its dated note of 2026-07-28 carries the user's **ratified shape**
> for the register and **governs this dispatch**; **`open_items/OI-207.md`** — the audit itself;
> **`open_items/OI-228.md`**, **OI-215**, **OI-226**, **OI-227** — the struck-versus-sounding
> family, the worked example of what this audit exists to find.
>
> **Current state:** branch `master`; expected HEAD `c9e0f17b61` — verify; mismatch = STOP. Riding
> Cowork edits, if any, ride your first commit. This dispatch file stays untracked.
>
> **Hard stops:** origin only; **no `src/` change of any kind**; no golden, `tools/corpus/` or
> `tools/robust_stop/` movement; **no fix, no design, no inference change** — you are auditing.
> A surprise is a STOP (#13). VS Code bash rules on every command.

**Dispatch author:** Cowork, 2026-07-28, for the Friday session.

---

## §A — What you are building, and the two rules the user ratified

**The decisions register** records **what was decided and its status. Nothing else.** There is
**no conformance field** — the user ruled it out because a decision's status changes only when
someone rules again, while conformance changes every time the code moves, and holding both in one
row produces a register that silently goes stale. **Non-conformance is recorded in
`OPEN_ITEMS.md` as ordinary rows**, each pointing back at the decision it violates.

**A decision belongs, wherever possible, in the OWNING LAYER'S SPECIFICATION** — that layer's
section of `ARCHITECTURE.md`. The register is the **index and pointer**, never a substitute home.
So a decision whose proper home is a layer specification and which is **not recorded there** is a
**documentation gap → an `OPEN_ITEMS.md` row**, distinct from a non-conformance row.

**And the user's coverage requirement, which governs Task 3: every one of the 15,224 harvested
statements must be taken care of in some way or another.**

## §B — Why the method is specification-first, and why that is not a shortcut

The harvest cast a wide net over decision *vocabulary*. It cannot see a decision written as plain
specification — three load-bearing ones are already known to be absent from its 15,224 candidates:
the priority-of-evidence ranking (`ARCHITECTURE.md:3134-3141`), the slicer's boundary rule
(`:1045`), and the piece-start shortcut (`:3128-3130`). The clustering then established that this
repository restates decisions by **paraphrase, not by copying** — 14,274 of 14,460 clusters are
singletons, and loosening the similarity threshold across its whole useful range moves the count
by 79. So neither tool reduces the judgment work, and neither can be the backbone.

**The layer specifications can.** They are bounded, structured, and are where the decisions are
supposed to live. Reading them is the only method that catches the plainly-phrased ones at all.
The harvested candidates then serve their genuine purpose: as a **searchable index** for
provenance, and as the **backstop** that finds rulings which never reached a specification.

## Task 1 — the backbone: enumerate the decisions from the layer specifications

Read `ARCHITECTURE.md`'s per-layer sections **in full**. For each layer, enumerate every decision
it states about how that layer should work — including those phrased as plain specification with
no ruling vocabulary anywhere near them. For each: the decision in the document's own words, its
location, and what it governs.

**Cite everything file:line.** Do not summarise a section you have not opened. The standing rule
binds hardest here: this task exists precisely because a previous session reasoned about note
collection from memory of a neighbouring section and reported the position as ambiguous, when the
specification stated it explicitly and twice.

## Task 2 — status, provenance, and supersession

For each backbone decision, determine from the record — never from inference:

- **status**: live · superseded-by (name it) · shelved-with-evidence (cite the evidence) ·
  falsified (cite the measurement);
- **date and who ratified it**, where recorded;
- **provenance**: the linked harvested statements that restate or evidence it (use the candidate
  and cluster lists as the index they are — repetition across documents is evidence the decision
  stands, so link the occurrences, never discard them).

Where the record does not say, **record "not stated" — do not infer a status.**

## Task 3 — every cluster reaches a recorded disposition (the coverage guarantee)

The clustering is a **partition**: all 15,224 candidates sit in exactly one of the 14,460 clusters.
Working cluster by cluster therefore provably touches every statement, and that is how the user's
requirement is discharged.

**Every cluster gets one recorded disposition.** The permitted set, and most clusters will take
seconds:

- **restates** a backbone decision (name it) — expected to be the large majority;
- **not a decision** — narrative, an instruction to a working session, a heading;
- **boilerplate** — the labelled bucket, confirmed;
- **a decision with no layer-specification home** — this is the valuable class; it goes to Task 4;
- **unresolved** — you could not tell. **Permitted and wanted.** An honest unresolved beats a
  guessed disposition, and the count of them is a finding about the record's legibility.

**Bulk disposition is permitted where it is defensible and the rule is stated** — for example, a
cluster whose only occurrences are in Claude Code session reports and whose text restates a named
backbone decision. **State every bulk rule you apply and the number of clusters it covered**, so
the judgment is reviewable rather than hidden inside a total.

**The completeness check is mechanical and must be in the report:** count clusters carrying a
disposition against 14,460. Anything less than all of them is an incomplete pass — say so.

## Task 4 — the two kinds of gap, as open-items rows

- **Documentation gaps:** a decision whose proper home is a layer specification and which is not
  recorded there. One row each, naming the layer and what the specification should say. **Do not
  edit `ARCHITECTURE.md`** — writing the specification entry is a separate, ratified act.
- **Non-conformance:** a decision the current implementation contradicts. One row each, with the
  decision cited and the contradicting code at file:line, **both sides quoted**. The known worked
  example is the struck-versus-sounding family (OI-215/226/227/228) — already rowed; do not
  duplicate it, but do record anything further you find in the same class.

**No fixes. No specification edits. Rows only.**

## Task 5 — the register, written to be read

Write the decisions register in the ratified shape, in the established index-plus-detail pattern
if the volume warrants it. **The user reads this document.** He has deep music-theory and software
architecture knowledge, is a working developer but **not a C++ programmer and not a
statistician**, and does not know this project's internal vocabulary.

Every entry: the decision **verbatim**, a **one-or-two-sentence plain restatement** beneath it,
its status, its home, its provenance links. Grouped by subject. Every internal term defined where
it first appears. No statistics vocabulary left standing unexplained. No C++. **No music-theory
word in a non-musical sense — the bare word is always the musical one** (bare *score* is the
music; the numerical sense is *candidate score*. Bare *measure* is the bar; the gauging sense is
*measurement*. Bare *key* is tonality. A script is a *measurement tool* or a *check*, never an
*instrument*). Quoted repository text stays verbatim, collisions included; your own prose does not.

**Also re-banner `tools/audit/decisions/decision_inventory.md`.** It currently presents itself as
"the canonical, load-bearing decisions", which is a completeness judgment made inside a dispatch
that forbade adjudication. Restate its opening honestly as a **reading sample, not an authoritative
or complete set**, and note that the register supersedes it.

## Task 6 — notes and close

Dated notes on OI-207 and OI-208; the new rows from Task 4; `STATUS.md` entry — **a pointer, not
content** (the standing remedy: withheld findings never enter a mandatory session-start read).
Commits per change-class. Push origin.

## Report

Hashes. **Task 1:** the backbone count, per layer. **Task 2:** status distribution, and how many
came back "not stated". **Task 3:** the disposition table, every bulk rule with its count, the
unresolved count, and **the mechanical completeness check — dispositioned clusters against
14,460**. **Task 4:** documentation gaps and non-conformances, counted and listed. **Task 5:** the
register's path and its entry count. Any decision you could not restate in plain words — that is a
finding, because a decision nobody can state plainly is a decision nobody can check. Anomalies each
diagnosed; a surprise is a STOP.

**If you must stop for feasibility: stop, and propose a partition with the measured counts as its
basis.** Say which task you completed, which you started, and what the remainder is. That is a
successful outcome, not a failed one.

Standing self-check before reporting: re-read the actual diff of every touched file against the
guiding principles, the conventions, the gate policies, and `DEFECT_TYPES.md`.

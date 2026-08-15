# CC instruction — cluster the decision candidates mechanically, and show the user a worked preview (READ-ONLY, NON-DESTRUCTIVE; no adjudication)

> **Read first (every session):** `C:\s\MS\CLAUDE.md` — in particular the Conventions entries
> **never work from memory instead of documented facts**, **music-theory words are reserved for
> their musical meaning (the bare word is always the musical one)**, and the pointer to
> `cowork_design_doc_template.md`, which is the home of this project's writing standards. Also
> `C:\s\MS\STATUS.md`, `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\OPEN_ITEMS.md` (INDEX), and
> `open_items/OI-208.md` — **its dated note of 2026-07-28 carries the user's ratified shape for the
> decisions register and governs this dispatch.**
>
> **What this is.** The decision harvest produced 15,224 candidate statements. Most are the same
> ruling restated: the Stage 3.1b shelving alone appears 21 times in near-identical words, and
> roughly 57 % of all candidates are Claude Code session reports restating rulings made elsewhere.
> A higher-capacity session on Friday will decide **which statements are the same decision, which
> statement is its authoritative home, whether it still stands, and whether the implementation
> obeys it.** That is judgment work. **This dispatch does only the part that is mechanical**, so
> Friday's capacity is spent judging rather than re-reading one sentence twenty-one times.
>
> **The one rule that matters more than any other here: NON-DESTRUCTIVE.** You **propose**
> groupings. You never merge two candidates into one row, never rewrite a candidate's text, never
> delete a candidate, and never drop an occurrence because a similar one exists. Every cluster
> keeps every one of its members visible and individually readable. **A wrong merge is invisible
> afterwards and would corrupt the register; an over-large cluster is merely untidy and Friday can
> split it.** When in doubt, do not group.
>
> **Current state:** branch `master`; expected HEAD `11ec8a4c3b` — verify; mismatch = STOP.
> Riding Cowork edits: `OPEN_ITEMS.md` (the OI-208 row) and `open_items/OI-208.md` (the ratified
> shape), plus `cowork_handoff.md` and `STATUS.md` — all ride your first commit. This dispatch file
> stays untracked.
>
> **Hard stops:** origin only; **no `src/` change**; no golden, `tools/corpus/` or
> `tools/robust_stop/` movement; **no adjudication of any kind** — do not fill status, do not
> decide whether a candidate is really a decision, do not judge conformance, do not name a
> supersession. A surprise is a STOP (#13). VS Code bash rules on every command.
>
> **No mid-flight steering:** self-sufficient; anything uncovered waits for the report.

**Dispatch author:** Cowork, 2026-07-28, at the user's direction.

---

## Task 1 — the mechanical clustering

Extend the existing harvest tool, or add a sibling beside it under `tools/audit/decisions/` —
your call, but **one tool per concern** (#6): do not create a second harvester. Emit the clusters
as a **layer over** `decision_candidates.json` (cluster identifier → the member candidate
identifiers), leaving that file untouched.

Group by these mechanical signals, and **record which signal produced each grouping** so Friday
can weigh it:

1. **Near-identical text.** Normalise whitespace, case, punctuation and formatting, then group by
   textual similarity above a threshold you declare and justify. Report the threshold and what
   moving it would do to the cluster count.
2. **Shared evidence pointer.** Occurrences citing the same commit hash, the same document and
   section, or the same open-item identifier are candidates for one decision. **A weaker signal
   than (1) — mark it as such**, never treat it as equivalent.
3. **Same date and same ratifier**, where both are discoverable. Weakest of the three; a
   corroborating signal only.

**Within each cluster, propose a representative** — the occurrence most likely to be the
authoritative statement — by source authority, not by length: the governing documents
(`CLAUDE.md`, `ARCHITECTURE.md`, the ratified `cowork_*` decision documents, `docs/`) above the
handoff and status files, and those above the Claude Code session reports, which are restatements
by construction. **Label it "proposed representative", never "the decision"** — Friday decides.

**Two things to flag rather than cluster.**

- **Boilerplate.** Phrases repeated across dispatches as instructions rather than decisions ("plain
  language everywhere", "a surprise is a STOP", "origin only") will cluster enormously and are not
  project decisions about how the analysis works. Put them in a separate, clearly-labelled
  boilerplate bucket — **kept, not deleted** — so Friday can confirm the judgment cheaply.
- **Clusters whose members disagree.** If grouped occurrences appear to say different things,
  **flag the cluster as internally divergent and do not resolve it.** That flag is valuable: a
  decision restated inconsistently is where a supersession or a drift is most likely hiding.

**Report the cluster-size distribution** — how many clusters of size 1, 2–5, 6–20, 21+ — and the
total cluster count. That number is the real size of Friday's work and the user wants it.

## Task 2 — the worked preview, written for the user to read

The user will read this. He has deep knowledge of music theory and of software architecture and
design; he is a working developer but **not a C++ programmer and not a statistician**; he does not
know this project's internal vocabulary and should not have to.

**Take the three to five clusters with the most occurrences** (excluding the boilerplate bucket)
and write them up in `tools/audit/decisions/cluster_preview.md` as **worked examples of what a
register entry will look like on Friday**. The purpose is for the user to say "yes, that is
readable" or "no, change it" **before** the expensive session commits to a shape.

Per cluster, in this order:

- **What was decided** — one or two sentences, plain words, no internal vocabulary undefined.
- **When, and who ratified it**, if the record says.
- **Where its authoritative statement appears to live** — file and section — marked as your
  proposal, not a finding.
- **How many times it is restated, and across how many documents.** Repetition is evidence the
  decision stands; say so plainly.
- **Whether the occurrences agree**, or whether the cluster is flagged divergent.
- **Two or three of the actual occurrences quoted verbatim**, so the reader can see the raw
  material behind the restatement.
- **A mock register entry** in the ratified shape from `open_items/OI-208.md` — what was decided,
  its status left empty for Friday, its evidence pointer, its home. **No conformance field: the
  user ruled it out; non-conformance is tracked in `OPEN_ITEMS.md` as ordinary rows.**

**Writing rules, graded:** every project-internal term defined where it first appears; no
statistics vocabulary left standing unexplained; no C++; **no music-theory word used in a
non-musical sense — the bare word is always the musical one** (bare *score* is the music, the
numerical sense is *candidate score*; bare *measure* is the bar, the gauging sense is
*measurement*; bare *key* is tonality; a script is a *measurement tool* or a *check*, never an
*instrument*). Quoted repository text stays verbatim, collisions included; your own prose does
not.

## Task 3 — notes and close

Dated note on OI-208 (the clustering layer exists; the cluster count is the size of the
adjudication). `STATUS.md` entry — a pointer, not content. Commits per change-class. Push origin.

## Report

Hashes. The clustering signals and the similarity threshold with its justification. The cluster
count and the size distribution. The boilerplate bucket's size. **The count of clusters flagged
internally divergent — and name the largest few**, because that is where Friday should look first.
The preview document's path. Anomalies each diagnosed — a surprise is a STOP.

Standing self-check before reporting: re-read the actual diff of every touched file against the
guiding principles, the conventions, the gate policies, and `DEFECT_TYPES.md`. **And confirm
explicitly that the clustering is non-destructive: every one of the 15,224 candidates is still
present and individually readable after it.**

**After this dispatch:** the Friday adjudication reads the clusters — not the raw occurrences —
decides which are one decision, which statement is authoritative, and whether each still stands;
records any decision whose proper home is a layer's section of `ARCHITECTURE.md` but is not there
as a documentation gap in `OPEN_ITEMS.md`; records non-conformance as ordinary `OPEN_ITEMS.md`
rows; and populates the decisions register in its ratified shape. It must also read the
architecture document's layer sections **in full**, because a search for decision vocabulary
cannot catch a decision written as plain specification — three load-bearing ones are already known
to be absent from the candidate list.

# The commissioning surface — everything standing between HEAD and phase 1's completion statement, grouped by WHOSE act each needs

> **STATUS: CC READING SURFACE, written 2026-08-11 at the thirteenth return continuation's close
> (`cc_instruction_return_continuation_13.md`, Task 3). NOT ratified, NOT a specification, and NOT a
> decision surface — nothing here asks for a choice.** Its one job is to put in front of the user, in
> one place, what remains and whose act each remaining thing needs, so that the completion statement
> can be commissioned from facts rather than from a search.
>
> **★ PHASE 1'S COMPLETION STATEMENT IS NOT WRITTEN, NOT DRAFTED AND NOT PARTIALLY WRITTEN HERE, and
> not one sentence of it is attempted.** The statement is the user's to commission; the finish line's
> own ninth item says so and this file does not move it. **This surface is not a claim that phase 1
> is close, or far** — it says what is outstanding and who owns it, and nothing about how long any of
> it takes.
>
> **★ EVERY POPULATION AND EVERY PER-ROW FIELD BELOW IS DERIVED, AND THE ARTIFACT IS THE HOME.** This
> file is a READING of `tools/audit/phase1_finish_line.json`, `tools/audit/gating_row_sizing.json`
> and `tools/audit/phase1_completion_inventory.json`, never a second home for what they hold (#6). The
> tables in §3 are transcribed from the sizing artifact's own fields by a generated pass, not
> re-authored. **Where this file and an artifact disagree, the artifact is right.** **No count,
> percentage or population size is restated anywhere here (D-431)** — identities are listed, because
> an identity is not a quantity and it is what lets a reader find the thing.

---

## 1. What this is, and the one distinction it rests on

The finish line divides into **ITEMS** (register entries owed a home, and open rows owed a
correction) and, inside the largest item, **ROWS**. Every item carries a closing act; every gating
row has been sized from its own text.

**The distinction that makes this surface useful is between a SIZE and a BLOCKER**, and the sizing
pass separates them deliberately. A size says how big the act is. A blocker says what stops it
starting. **They are independent**: a one-line act can be blocked by a ruling, and a large act can be
blocked by nothing but capacity. A commissioning reader wants the blocker first, which is why §3
groups by blocker and carries the size beside each row rather than the other way round.

**A size is AUTHORED and can be wrong. A population is DERIVED and cannot.** The sizing artifact says
this of itself in its own opening, and it is repeated here because everything in §3 inherits it.

---

## 2. The finish line's end state, derived fresh at this commit

**Read it at `tools/audit/phase1_finish_line.json`.** What follows is a guide to its shape, not a
copy of its values.

Its **nine items** stand in three groups.

- **Five are per-entry HOMING items** — register entries whose home document no user-ratified surface
  names; entries a delegation reaches only in a form the bar excludes; entries whose admitting
  delegation does not reach the section they sit in; entries the delegation reaches in a section that
  records findings rather than stating rules; and entries with no home at all. **Their closing act is
  settled and is not a question:** re-homing into the owning layer's specification is the ruled
  default (**D-664**), and the registered procedure (**D-668**) binds every act — try the pointer
  move first, judge the receiving section's kind BEFORE any write, and HOLD rather than write by
  stretch where the owning section records findings.
- **Two are ROW items** — the open rows asserting a specification states something false at HEAD,
  which gate; and the apparatus-classed documentation rows whose place inside the doc-sync half
  **D-639**'s test decides. **The second of those has RUN**: its derivation is whole, its IN-verdicts
  were applied on the user's Ruling 56, and what it hands on is nothing further.
- **One is CLOSED and is listed because a distance map showing only what remains would misrepresent
  the position** — the defense-gap population reads zero.

**The ninth is phase 1's completion statement itself.**

### What moved under it during this batch, derived rather than claimed

Two gating rows left the TRUE-half item by being performed, one register entry left the
findings-not-rules item by being re-homed, and one new gating row entered from this batch's own
reading. **One homing item is HELD rather than owed** — see §3's first note.

### What the artifact does NOT say, repeated because a reader will look for it

It does not say how much work remains: an item's population is a count of obligations, not of
sessions. **A green guard set says nothing about the finish line** — it is a statement about the
record's own machinery. And it is not the completion statement, not a draft of one, and not an
authorization for any fix, design or inference change.

---

## 3. Every remaining gating row, grouped by whose act it needs

**Transcribed from `tools/audit/gating_row_sizing.json` by a generated pass.** Each row carries its
authored **sizing label** — one of the four the user named, and no fifth is invented — the owner of
the act, and the act in one line. Where a row carries a **further half of a different kind**, that
half is named in its own right rather than folded into the label, so no row reads smaller or larger
than it is.

**★ THREE THINGS TO READ THE TABLES WITH.**

1. **`NEEDS-RULING` means no session act exists at all** — not that the work is large. Four of the
   rows in the first group carry it, and their acts are one edit each once the choice is made.
2. **The first group is the one that decides scheduling.** Everything in it is stopped by a decision,
   not by effort; every other group is stopped by time, by an event, by the phase order or by the
   `src/` freeze.
3. **One homing item is HELD and is not in these tables at all**, because its subject is a register
   entry rather than a row: the finish line's *no home at all* item names one entry the user has
   already ruled SUPERSEDED with no specification home owed, while the item's closing act asks for a
   write. That contradiction is [[OI-369]], and it is the user's — both of its closing acts change a
   derived surface.

---

### What blocks it: a user ruling

| Row | Sizing | Whose act | The act, in one line |
|---|---|---|---|
| [[OI-95]] | **SESSION-LARGE** | a session on this side | Unify the two disposition generators into one layer-selected generator, the way the sweep tool was unified, and re-stamp the line-stale l1l2 artifacts. |
| [[OI-141]] | **NEEDS-RULING** | the user | The key-menu design conversation itself. The row records the diagnosis, the drift grounding, the mechanism pinned at the code and the design opening as all delivered — what is left is the user's. |
| [[OI-292]] | **REAL-WORK** | a session on this side | Per member of the defect class, the measured establishment #19 requires — a detection rate against real violations and a false-positive rate on legitimate work — and then the user's ruling on whether to build the mechanism at all. |
| [[OI-309]] | **SESSION-LARGE** | a session on this side | Per artifact, the diagnosis the row asks for — STALE or HISTORICAL — and then either a regeneration or a verify mode that says the artifact is a point-in-time record and must not be regenerated over. |
| [[OI-311]] | **SESSION-SMALL** | a session on this side | Add the verify-only mode the tool's siblings carry, plus the one judgment the row names: how a census whose scope is the tree reports a file-count field that moves by construction. |
| [[OI-320]] | **NEEDS-RULING** | the user | Decide which of the four stale sites become the retired diagnostic and which become the governing robust unit — a filing decision about how a user-ratified gate is presented in the document every score-touching task is sent to first. |
| [[OI-322]] | **NEEDS-RULING** | the user | Decide whether a completed audit describing deleted code is re-bannered as a historical record or rewritten — a filing question the row says applies to every completed audit in the tree, not to this one. |
| [[OI-324]] | **NEEDS-RULING** | the user | Rule which arm the priority-of-evidence table binds — a cross-cutting evidential rule for both arms, or a legacy-path rule whose dependent open item needs a different source. **A FURTHER HALF of a different kind:** The smaller defect in the same paragraph pair — an unqualified predicate naming no argument, and two sentences that read plainly as contradicting each other. (*SESSION-SMALL*, a session on this side, blocked by nothing beyond capacity) |
| [[OI-341]] | **SESSION-SMALL** | a session on this side | Make the check enforce the design its own docstring states — stop comparing a line number the tool itself dates as an observation — or re-run the apply mode instead. |
| [[OI-352]] | **SESSION-SMALL** | a session on this side | Compose the guard sweep so the classification's own check runs — a second runner stage, a wrapper with a declared order, or an authored entry carrying that order. |
| [[OI-357]] | **REAL-WORK** | a session on this side | Establish BY WHAT MEANS the production arm reads this repertoire, and make the per-case reading the row also names — both read-only, and every comparable establishment in this arc has run on an explicit licence. |
| [[OI-359]] | **REAL-WORK** | a session on this side | Build the per-corpus breakdown check the measurement convention's uncovered half needs — after the measured establishment a member of that backlog owes, and after the user's ruling on whether to build it at all. |
| [[OI-360]] | **REAL-WORK** | a session on this side | Design and measure a second candidate signal for the verbatim-versus-subject check against the committed labelled corpus, adopting nothing that does not separate. |
| [[OI-369]] | **NEEDS-RULING** | the user | Rule which of the two acts the row names closes it: the item subtracts superseded entries whose successors are homed, by the sibling item's own machinery; or it keeps the entry and its CLOSING ACT is corrected to say that no home is owed. |
| [[OI-363]] | **REAL-WORK** | a session on this side | Make the per-case reading the row gates on — per disagreement, is it a defect, a defensible modal reading the major/minor ground truth cannot represent, or a global-versus-local comparison artifact. |

### What blocks it: nothing beyond capacity

| Row | Sizing | Whose act | The act, in one line |
|---|---|---|---|
| [[OI-47]] | **SESSION-SMALL** | a session on this side | Mark the four submission-era sections of `STATUS.md` historical — the row's own words, and the act it calls the BANNER half, its triage half being discharged. |
| [[OI-45]] | **SESSION-SMALL** | a session on this side | Re-aim the stale §4/§6 anchors in `docs/scoring_model.md` and give `kHalfDimFirstInversionBonus` its §6 entry. |
| [[OI-90]] | **SESSION-SMALL** | a session on this side | Correct the L1/L2 file-table reason strings under `tools/audit/l1l2/`, which the L3 pass made stale. |
| [[OI-107]] | **SESSION-SMALL** | a session on this side | Re-label `ARCHITECTURE.md` §4.1h's iteration-era baselines and test counts as a dated historical snapshot — the second of the two routes the row's own text gives; the first, re-measure, is a measurement rather than a labelling act. |
| [[OI-150]] | **SESSION-SMALL** | a session on this side | Build at HEAD, run both suites, re-stamp both `BUILD_AND_TEST.md` baselines from those runs, and make the notation line name the four key-emission cases that fail by design. |
| [[OI-183]] | **SESSION-SMALL** | a session on this side | Give the twelve unmentioned scoring constants a by-name mention in `docs/scoring_model.md`, or state per constant which table cell already covers it. |
| [[OI-207]] | **SESSION-LARGE** | a session on this side | The residual second pass over the clusters the mechanical disposition could not classify, and the reading of the remaining design documents — which the row's own proposal says to read whole rather than sampling through a yield proxy it declares unestablished. |
| [[OI-274]] | **SESSION-SMALL** | a session on this side | Give `docs/scoring_model.md` the scoping sentence its two sibling rows closed on, re-stamp its footer date, and correct the two DRAFT-UNCOMMITTED banners standing on tracked files. **A FURTHER HALF of a different kind:** Whether `CLAUDE.md`'s mandatory-read instruction should also name the joint estimator's specification — which the row calls a governing-document question and therefore the user's. (*NEEDS-RULING*, the user, blocked by a user ruling) |
| [[OI-282]] | **SESSION-SMALL** | a session on this side | Append a dated annotation to `cowork_style_clustering_plan.md` scoping its title and its opening to the half that is still future work, and recording that the other half was delivered and ratified the next day. |
| [[OI-304]] | **SESSION-SMALL** | a session on this side | Append a dated correction remark to each of the two annotation blocks, naming D-428's corrected text — an annotation act, not an edit, which is what the row's own status calls for. |
| [[OI-315]] | **SESSION-SMALL** | a session on this side | Correct `docs/key_path_design.md`'s §2.1/§5 self-contradiction and the two further `docs/` surfaces that still state the removed piece-start shortcut as live. **A FURTHER HALF of a different kind:** The stale comment in `src/composing/tests/regionanalysis_tests.cpp`, the fourth surface the row enumerates. (*SESSION-SMALL*, a session on this side, blocked by the freeze on `src/`) |
| [[OI-318]] | **SESSION-SMALL** | a session on this side | Correct the Layer-6 paragraph so it names the punctuation-span rather than the word the ratified rename reserved, and add that word to the scope correction's own enumeration, which the row establishes is one short. |
| [[OI-321]] | **SESSION-SMALL** | a session on this side | Correct the two plainly false statements — the header calling a phase deferred that the code says was executed, and the named directory that does not exist. **A FURTHER HALF of a different kind:** Item (3) — whether the implode path applying the display-duration gate discharges the parked divergence's decision rule or is a divergence that closed by drift, which the row says a session may not answer. (*NEEDS-RULING*, the user, blocked by a user ruling) |
| [[OI-332]] | **SESSION-SMALL** | a session on this side | Correct the *no code* banner standing over two operations the row itself verified built, and re-aim the drifted as-built anchors. **A FURTHER HALF of a different kind:** Item (3) — the falsified design carrying no supersession note, which raises the same filing question OI-322 poses and does not answer. (*NEEDS-RULING*, the user, blocked by a user ruling) |

### What blocks it: an event the record schedules elsewhere

| Row | Sizing | Whose act | The act, in one line |
|---|---|---|---|
| [[OI-11]] | **SESSION-SMALL** | a session on this side | Correct the stale audit §3 file-table entry. The primitive itself needs no act — the row's own words are that it retires WITH the decoder, which the retirement map deletes. |
| [[OI-12]] | **REAL-WORK** | a session on this side | The `findTemporalContext` ownership move itself, which the record reassigns to the E4 engage step, plus the same stale audit §3 table entry. |
| [[OI-57]] | **REAL-WORK** | a session on this side | Make the extra-scores registry accurate and mechanically validated against the files on disk, at the corpus-onboarding event the row assigns it to. |
| [[OI-146]] | **REAL-WORK** | a session on this side | Write each layer's published-facts contract into its `ARCHITECTURE.md` section from the evidence inventory, which the row gates on the key-layer completion; and keep the inventory live as new evidence kinds are found. |
| [[OI-223]] | **SESSION-LARGE** | a session on this side | Regenerate each layer's deep inventory at HEAD and re-stamp it, which the row assigns to each layer's own owner. |
| [[OI-283]] | **SESSION-SMALL** | a session on this side | Stamp the decisions register's coverage claim to a COMMIT rather than a line count, or have that register's generator compute it — the row's own two acts, the second removing the failure entirely (#17f). |

### What blocks it: the phase order (D-231 and #8)

| Row | Sizing | Whose act | The act, in one line |
|---|---|---|---|
| [[OI-109]] | **REAL-WORK** | a session on this side | Answer the P5-over-diminished scoring question the adjudication makes this row the one home of — whether a sounding perfect fifth over a diminished template is correctly a hard contradiction — which the record parks to the precision phase with a #17 ledger. **A FURTHER HALF of a different kind:** The orphaned `BUG-10` marker in `chordanalyzer.cpp`, re-pointed at this row — a one-line comment correction the adjudication already decided. (*SESSION-SMALL*, a session on this side, blocked by the freeze on `src/`) |
| [[OI-224]] | **REAL-WORK** | a session on this side | The certification the row names as still owed — the pass-2 blind reading with its seeded error rate and its partitions, to the standard the L4 precedent set. |
| [[OI-239]] | **REAL-WORK** | a session on this side | Two separable acts the row names: record the event-lattice rule in a layer specification, and decide whether the two boundary computations unify — the second belonging WITH the struck-versus-sounding family design. |
| [[OI-249]] | **REAL-WORK** | a session on this side | The one design surface the row names with OI-248 — what metrical facts the adapter derives, from what, and where they are specified. |

### What blocks it: the freeze on `src/`

| Row | Sizing | Whose act | The act, in one line |
|---|---|---|---|
| [[OI-105]] | **SESSION-SMALL** | a session on this side | Correct the `isSemitoneStep` naming imprecision in `chordslicedecoder.cpp` and the `tools/param_manifest.json` consuming-path statement that denies a call the tool makes. |
| [[OI-220]] | **REAL-WORK** | a session on this side | Establish at the CALL GRAPH whether each joint-internal module named by a dormancy comment is on the live decode path, and then correct or leave each comment on that finding. |

### What blocks it: the role separation

| Row | Sizing | Whose act | The act, in one line |
|---|---|---|---|
| [[OI-121]] | **SESSION-SMALL** | the writing side (Cowork) | Re-word `cowork_layer5_function_design.md` §5.0/§15-12 and the handoff line to record the grammar completion as landed at the commit the row names. |

---

## 4. The two registers' own health, checked at this commit rather than assumed

Every check below was RUN for this surface, not read off a previous run. Verdicts, and nothing else:

| Check | Subject | Verdict |
|---|---|---|
| `tools/audit/register_lint.py` | Open-items row identifiers unique | **PASS** |
| `tools/open_items_split_check.py` | INDEX ↔ detail-file bijection; no detail file carrying a status of its own; the original items byte-verbatim | **OVERALL PASS** |
| `tools/audit/index_status_lint.py --check` | Every status cell opens with one canonical token, and every row splits | **PASS** |
| `tools/audit/decisions/gen_decisions_register.py --check` | The rendered register matches its data, index and group files alike | **PASS** |
| `tools/audit/decisions/gen_cluster_dispositions.py --verify` | Every cross-reference resolves; every verbatim found at its cited home; every cited line number correct | **PASS** (the exceptions are cited to a file with no line number, by design) |
| `tools/audit/decisions/gen_cluster_dispositions.py --check` | Every cluster dispositioned | **OVERALL PASS** |
| `tools/audit/decisions/gen_cluster_dispositions.py --producible` | Every register pattern compiles; the whole derivation dry-runs | **OVERALL PASS** |
| `tools/audit/decisions/reaim_home_anchors.py --check` | Register home anchors against the files | **zero drift** |

**★ AND ONE THING IS SAID PLAINLY ABOUT WHAT THESE VERDICTS ARE WORTH.** They establish that the two
registers are internally consistent and that every quote resolves where it says it does. **They
establish nothing about whether the decisions are right, whether the code obeys them, or how much of
phase 1 remains** — the first is not what a register records, the second is what the open-items
register tracks, and the third is §2 and §3 above. A green check is a statement about the record's
own machinery.

---

## 5. The orientation the commissioning opens with

**`cowork_target_document_structure_2026_08_09.md`** — the seven surfaces phase 1 builds toward, and
who points at whom. It is a CC reading surface, not ratified and not a specification, written at the
user's direction and confirmed in conversation on 2026-08-09.

**It is pointed at rather than summarized here (#6).** Read it first if the completion statement is
to open with what the system's document structure is FOR; §2 and §3 above then say how far from that
structure the record currently stands, and the two are not restated into each other.

---

## 6. What this surface does NOT do

It writes no sentence of phase 1's completion statement, and drafts none. It authorizes no fix, no
design and no inference change; phase 1 (**D-231**) remains open and #8's three-clause gate stands.
It moves no open-items status, no register entry, no home and no gate verdict. It changes no
derivation and re-sizes no row. It touches no golden, no corpus of scores and nothing in
`tools/robust_stop/`. **It asks no question and offers no option** — every choice it names is already
recorded on the row that owns it.

*Provenance: CC, 2026-08-11, dispatch `cc_instruction_return_continuation_13.md`, Task 3, at the
thirteenth return continuation's close. The tables in §3 are transcribed from
`tools/audit/gating_row_sizing.json` by a generated pass over that artifact's own fields; §2 reads
`tools/audit/phase1_finish_line.json`; §4's verdicts are this session's own runs.*

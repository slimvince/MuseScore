# Decision surface — what L2's deriving session reads at boot, and two loose ends from the write-back batch (2026-09-05)

> **STATUS: DECISION SURFACE, put to the user. Nothing here is executed.** Written by the Cowork
> writing side on 2026-09-05, the session that booted on `cowork_handoff_entry_one_hundred_and_nine.md`,
> after the ordinary session-start read in full and after the write-back batch
> (`cc_instruction_l2_ruling_writeback_2026_09_05.md`) was verified closed at the objects, tip
> `911f5f7cdaa3fb53b9b5a2bdefb82e793c65eafb` at both ref files.
>
> Every fact below was read at the file named beside it, in this session, with the file tools from
> bridge-staged copies. No shell touched the repository. Where a claim rests on a report rather than an
> object, it says so. The choice questions are NOT in this document: they come one decision per turn,
> after this surface has been read and after its own fact check has been delivered as a turn of its own.

---

## 0. The words used here, explained from scratch

**A deriving session** is a fresh Cowork session that writes what the analysis SHOULD do for one unit of
the architecture, from music theory, from published research and from the design intent you have
ratified — without reading what the current code or the current specifications say the analysis DOES.
The rule that makes it blind is the phase definition's standing constraint (§3.2 and §3.8 of
`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md`, as Ruling 11 of the 2026-08-31
sitting record cites them).

**L2** is the unit the next deriving session derives. Its charter is one sentence at `FRAMEWORK.md`,
under the heading `### L2 — The tonal reading. The one entangled decision.`: *"over this music, what is
the tonality at each moment, where does each harmony give way to the next, which sounding notes belong to
the harmony and which elaborate it, and what chord is read over each span?"* The charter fixes what L2
consumes (everything L0 and L1 publish, nothing else), what it publishes (the segmentation, the tonality
per span, the chord per span, the chord-tone assignment and elaboration relation per note, and the rivals
with their mass), and two boundary conditions on the score it forms; it leaves the score's terms, tables
and fitting to the detail specification the session derives.

**The boot pack** is the self-contained directory such a session opens at boot, and nothing else. It is
rendered by `tools/audit/gen_derivation_boot_pack.py` into `tools/audit/derivation_boot_pack/<subject>/`.
Three packs exist and all three are frozen because their sessions have run: `harmony-boundary` (the
pilot), `scoring-model` (the sizing pilot) and `l0-l1` (the first derivation of this phase, delivered
2026-09-02). L2's pack does not exist.

**The six ruled members** go into every pack, unchanged and in order (ruled 2026-08-22, Ruling 1 of
`cowork_rulings_2026_08_22_boot_list_sitting.md`; imported into the generator's `MEMBERS` table): (1) the
phase definitions section; (2) `CLAUDE.md` at two spans, the guiding principles through the delegation
pointer and the conventions through the self-check; (3) the writing standards; (4) the dispatch-protocol
section of the audit protocol; (5) the ratified design intent — the `DESIGN-INTENT` class of the rulings
sort, rendered with four fields per entry and CUT by the withheld family; (6) the defect-type catalog at
its type and definition columns.

**Per-subject EXTRAS** are members a subject carries AFTER the six (ruled 2026-08-31, Ruling 16 of
`cowork_rulings_2026_08_31_decision_surface_sitting.md`, your words "extend generator"). The `l0-l1` pack
carries three: (7) `FRAMEWORK.md` §5 and §9 with three passages removed; (8) five research extracts with
one named section cut from each; (9) the empirical findings ledger, whole. The generator's `EXTRAS` table
carries an entry for every subject; an empty list is authored, never left absent, and a subject without an
entry stops the tool.

**The withheld family** is what is cut out of member (5) for one subject so that the session cannot read
the answer it is chartered to derive. For L2 it is now RULED: 111 register entries IN (withheld), 133 OUT
(admitted), none unplaced (`cowork_rulings_2026_09_05_l2_withheld_family_sitting.md`; written back to
`VERDICTS["l2"]` and rendered RULED at `ratification_surfaces/cowork_withheld_family_l2_reading.md` by the
batch verified this session). The generator's `WITHHELD` table for a subject also carries withheld
DOCUMENTS and withheld PASSAGES — the pilot's carries one document and two `CLAUDE.md` passages — and
`WITHHELD` has no `l2` key yet. Ruling 81 (§3cj of the 2026-08-31 record) rules that *"no identity is
withheld that the user has not ruled"*; the ORDER — the family authored from LIST ONE after the boot-list
members are ruled — is the plan the hundred-and-ninth handoff entry records as the pilot's pattern, and
this surface is the boot-list step of it.

**The brief** is the separate document the session is opened on; it stages scores to the session by name
and states what the session may read beyond the pack. The brief is not this surface's subject, except
where a decision here fixes what the brief must later stage (Decision 7).

**Task B** is the research-reading task of the reading pass's remedial commission
(`cowork_reading_pass_remedial_commission_2026_08_31.md` §3, ordered by you as Ruling 3 of the 2026-08-30
sitting): derive, from the bibliography, every held paper whose METHOD is a live candidate for a charter
decision, then *"read whole, at the object, every paper the derivation admits, in priority order … L2's
entangled decision first."* Its derivation is `reading_pass/candidacy_upgrades.md`: 47 rows admitted.

---

## 1. Where the plan stands, and what this surface does for it

The plan stands at: L2's criterion written → the group gloss repaired → L2's 244 candidates published →
the verdict pass run → the reading file rendered → the three lists ruled → the rulings written back
(verified closed this session) → **L2's boot-list members (this surface)** → then `WITHHELD["l2"]`
authored from the ruled LIST ONE, the pack built with the derived cross-reference additions and the leak
check, and the `DATE` fix → then the blind deriving session → then L2's comparison reading.

What this surface does for it: it puts every decision the pack-build dispatch needs and cannot take
itself, so that the dispatch can be written as exact edits to the generator's authored tables — `EXTRAS`,
`WITHHELD` — and nothing in it is a judgment the executing side makes.

---

## 2. Two facts found in this session's reading that bear on the whole surface

**Fact A — a standing gate stands in front of L2's derivation, and L2's slice of it is not read.** The
eighty-seventh handoff entry states: *"No derivation may begin before the chosen subject's slice of Task
B is in."* Ruling 10 of the 2026-08-31 record (§3j, your words "L0+L1 first, then L2") restates it in its
"what it does not do": *"The eighty-seventh entry's gate stands unchanged: no derivation may begin before
the chosen subject's slice of Task B is in."* For L0+L1 the slice was five papers, all read at the object
before that session ran (`reading_pass/candidacy_upgrades.md`, the reading-progress table and the section
headed "THE L0+L1 SLICE IS COMPLETE"). For L2 the same file says: *"Not read: the whole of Task B outside
this slice — the L2 and L3 groups … headed by L2's entangled decision. The remainder is untouched."*

Counted at that file: 47 rows are admitted; 5 are read (rows 4, 7, 37, 38, 39 — the L1 slice); 5 cannot
be read from here (rows 2, 6, 9, 22, 44 — paywalled, books, or image-only). That leaves **37 admitted,
readable, unread rows**, almost all of them in the file's groups 1 to 4 and 6, which are L2's (the joint
tonality-and-chord decision, segmentation decided with labelling, the scoring architecture and its
fitting, what L2 must publish, and the grammar branch). Which of the 37 are L2's rather than L3's is a
derivation this side has not made; the figure is an upper bound. The commission's own words also bind
the depth: each admitted paper is read WHOLE at the object and extracted, and a paper marked central
owes a second independent extraction. **No later ruling this session read discharges the gate for L2.**
The hundredth, hundred-and-first and hundred-and-ninth handoff entries, read this session, do not mention
it — which is how it dropped out of the plan's narrative, not out of the record; the entries between those
were not read for it.

**Fact B — member (2) of every pack carries passages, beyond the two the pilot withheld, that describe
this project's current L2 mechanism.** The generator's own docstring states this bound: *"That member (2)
carries no other leak"* is NOT asserted, because the pilot's leak search *"was searched for the oracle's
own phrases and not for every paraphrase."* This session read both spans of `CLAUDE.md` that member (2)
renders — the guiding principles through the delegation pointer, and the conventions through the
self-check — for passages that state what this project's L2 currently does or how its score is built.
The findings are at Decision 5.

---

## 3. The decisions

Each is stated self-contained. "Towards the objective" means towards the best possible inference;
"towards the principles" means towards `CLAUDE.md`'s guiding principles, cited by number.

### Decision 1 — the order: does L2's pack wait for Task B's L2 slice, and what is ruled now?

**What is being decided.** Whether this surface rules L2's pack members now — with the research-extract
member defined by rule and filled when the slice is read — or whether the boot-list decision itself waits
until the L2 slice of Task B is in and the extracts exist by name.

**The facts.** Fact A above. The `l0-l1` order was: the slice read (2026-08-31) → the members ruled
(Rulings 11 and 12, 2026-08-31) → the pack rendered → the brief → the session (2026-09-02). Ruling 11
Decision 2 ruled the extracts by NAME (*"the five L1-slice extracts go in"*), which was possible because
they existed. The generator's `EXTRAS` entry for `l0-l1` names its five extract files by stem
(`gen_derivation_boot_pack.py`, the member-8 entry). D-250 says a dispatch is written only when it is
next. Under P2 (Ruling 13 of the 2026-08-31 record) the deriving session may fetch and read published
research, unbounded, whatever the pack carries.

**The positions.**

*Position 1 — rule the members now; the extracts member is ruled as a CLASS (the extracts of the L2
slice of Task B, as they stand when the pack is rendered, each with this side's conclusion section cut),
and the pack is rendered only after the slice is in.* Towards the objective: the same session, with the
same reading, opens at the same time as under Position 2 — the gate governs when the session opens, not
this surface. Towards the principles: it keeps D-250's order (the pack-build dispatch is written when it
is next, which is after the slice); it puts the whole boot-list question to you once rather than twice;
its cost is that you rule a class rather than named members, which the pilot did not do, so the names
must be published to you before rendering — a read, not a second ruling.

*Position 2 — defer this surface's extracts decision; work the L2 slice first; return with the names.*
Towards the objective: identical outcome. Towards the principles: it follows the `l0-l1` precedent to the
letter (members ruled by name); its cost is a second surface later and a plan whose next several sessions
are reading sessions with the boot-list question half-open.

*Position 3 — render L2's pack now without an extracts member and let the session fetch its own research
under P2.* Towards the objective: it rates lowest — Ruling 2 of the 2026-08-30 sitting commissioned the
reading pass precisely so the primary-read debt is pre-paid rather than left to the deriving session, and
Ruling 11 Decision 2 chose to put extracts in for that reason. Towards the principles: it does not
satisfy the gate at all, which is a user ruling (Ruling 10) and not this side's to lift; it is not
available without a new ruling that lifts the gate.

**Recommendation: Position 1.** The strongest argument against it is the pilot's practice: every earlier
member was ruled by name, and a class ruling asks you to trust that the class will be filled correctly.
What answers it is that the class is mechanical — the rows of the L2 slice are derived at
`candidacy_upgrades.md`'s own verdict table, the extract files are named by stem in the same file's
reading-progress table as each is read, and the generator STOPs on a missing file — and that the names
are published to you before anything renders.

**What Position 1 does NOT do.** It does not lift the gate, shorten the slice, or open the session. It
does not decide which of the 37 rows are L2's; that derivation is this side's and is put to you when
made.

### Decision 2 — the research extracts: which populations, and what is cut from each

**What is being decided.** Which extracts L2's pack carries as a member, and what is cut from them.

**The facts.** Two extract populations exist on disk. *(i)* Task B's, under `reading_pass/extracts/`,
written in the original commission's §4 form; each carries a section headed *"What an L1 [or L2] detail
specification could adopt, adapt, or must argue against"* — this side's conclusions over the paper — which
Ruling 11 Decision 2 ordered CUT for `l0-l1`, the generator recording the ground as *"this side's
conclusion about what an L1 specification should do with the paper, which is the deriving session's own
work."* The five L1 extracts exist; the L2 slice's do not yet. *(ii)* The first reading pass's, also under
`reading_pass/extracts/` (twenty files there are first-pass extracts, counted at the directory listing;
the other five are Task B's) and `reading_pass/extracts_second_pass/` — extracts of the framework-phase
population, several of them squarely L2's subject (the McLeod & Rohrmeier 2021 modular
system and 2024 chord-tone alterations, the unified chord model, the local-keys and modulations paper,
HarmTrace, Sapp's key analysis, wavescapes, the GTTM paper, BACHI's boundary-aware recognition, the
DCML mode-collapse note). These were written in a different form: their conclusion section is headed
*"Bearing on the framework (first-pass reading; verdicts belong to the findings surface)"*, read at
`reading_pass/extracts/mcleod-rohrmeier-2021-modular-harmonic-analysis.md`. Seven of their rows carry
at-the-object reads under `reading_pass/object_reads/` (rows 1, 2, 3, 5, 17, 18 and 21, counted at the
directory listing). The `l0-l1` pack carried Task B's
five only; no first-pass extract was an L1 candidate, so the question of the first-pass population never
arose there.

**The positions.**

*Position 1 — Task B's L2-slice extracts only, with the "could adopt, adapt, or must argue against"
section cut: the `l0-l1` precedent exactly.* Towards the objective: the session meets every paper the
candidacy derivation admitted, read at the object. Towards the principles: #1 and #2 served; the cut is
the ruled mechanism, verified both ways by the generator. Its cost: the first-pass extracts of papers that
are L2's own subject stay outside the pack although they are read, extracted and in part re-read at the
object.

*Position 2 — Position 1 PLUS the first-pass extracts whose paper bears on L2, with their "Bearing on the
framework" section cut, the L2-bearing set derived by this side and put to you by name before
rendering.* Towards the objective: highest — the session meets more of the literature already read at the
object, and Ruling 11 Decision 2's reasoning (*"the session meets five papers already read at the object
… while reaching its own conclusions over them"*) applies to these papers exactly as to Task B's.
Towards the principles: the same as Position 1, plus one more cut rule in the generator (a second heading
string) and one more derivation by this side. Its cost is that derivation and its check.

*Position 3 — no extracts; the session fetches under P2.* Rated at Decision 1 Position 3 and excluded on
the same ground.

**Recommendation: Position 2.** The strongest argument against it is scope: a second population, a second
cut rule, a second derivation, each a place to err, for papers the session may fetch itself under P2.
What answers it is that P2 makes the extracts falsifiable, not redundant — Ruling 13 declined a reading
bound for exactly that reason — and that the first-pass extracts of the McLeod & Rohrmeier family are the
closest published relatives of L2's charter in the whole record; leaving them out while putting in the
Task B rows would be a filing accident, not a design.

**What it does NOT do.** It does not decide which first-pass rows bear on L2; that list is derived and put
to you. It does not re-read anything. It does not touch the cut heading of Task B's extracts.

### Decision 3 — the charter member: `FRAMEWORK.md` §5 and §9 with the three ruled removals — the alternatives have collapsed to one

**What was open.** Whether L2's charter member is the `l0-l1` pack's member (7) unchanged — §5 and §9
whole, with three passages removed — or whether L2 needs a further sweep for passages describing what
this project currently has.

**The facts, and why they close it.** The three removals ruled for `l0-l1` (Ruling 14's two, carried by
Ruling 16; Ruling 17(b)'s third) are, read at `FRAMEWORK.md`: §5's second-axis provenance parenthetical
(*"This is adopted from this project's material…"*); DP-N's stage-two parenthetical (*"Stage two
established that this project's own layer specifications do not state the answer either…"*); and DP-Q's
(*"Stage two found the same question open in this project's own record…"*). Two of the three sit in
L2's own underived design points and state what this project's specifications say about L2's subject —
so they are removed for L2 on a stronger ground than for L1. This session then searched §5 (lines 288 to
493) and §9 (lines 620 to 817) for every other mention of this project's own material: the only further
hits are DP-K's two added grounds (about the repertoire and two published studies, not this project's
system) and L1's release clause note (*"This corrects the first-stage draft…"*, a note about the
document's own history). Ruling 17(b) already recorded the candidates it declined and why (DP-N's two
disagreeing analyses and DP-Q's three exemplar analyses describe corpus material and are evidence for the
design points). Appendix A never enters, §5 and §9 being all that is taken.

**So there is no choice here**: L2's member (7) is `l0-l1`'s, byte for byte in its authored filter, and
the generator renders it from the same three anchors. It is stated as a decision only so that the record
shows the sweep was made for L2 and found nothing further. If you want the DP-N and DP-Q parentheticals
KEPT for L2 — on the ground that they tell the session the question is open in this project's record
too — say so; the ground against is that they also tell the session what this project's specifications
currently say (the six-four *"functionally folded into the dominant's approach"*; the decoder *"always
commits on the tonality axis"*), which is implementation content.

### Decision 4 — the empirical findings ledger: whole and unfiltered — no choice

`EMPIRICAL_FINDINGS_LEDGER.md` enters every deriving session's pack *"by the phase definition's own
naming and not by any decision taken here"* (Ruling 12's correction of record, citing §3.4 of the phase
definition surface: *"the same independent sources and ledger as the framework phase"*). The `l0-l1` pack
carries it as member (9), whole. The ledger's own banner states that an entry in it *"is a fact a deriving
session may read: it has crossed the blindness barrier."* Nothing in the record makes L2 different.
Stated, not asked.

### Decision 5 — withheld passages of member (2): the pilot's two, and four more this session found

**What is being decided.** Which passages of `CLAUDE.md`'s two rendered spans are cut out of L2's
member (2), each as an authored withheld passage with its finding, date and reason (the D-677 shape the
generator already uses: a scope anchor naming the bullet, an opening and a closing anchor inside it,
matched exactly once or the tool STOPs).

**The facts.** The pilot withholds two passages (`WITHHELD["harmony-boundary"]["withheld_passages"]`):
*(a)* the founding-instance clause of the never-work-from-memory rule, which states that slice identity is
the eligible sounding-note set with releases as boundaries and that actual sounding notes rank as the
strongest evidence — the ruled evidence ranking, which for L2 is the first limb's answer (D-057 is IN for
L2 at the reading file's line 166); *(b)* the founding-instances sentence of the design-defense rule,
which names *"the decode segment cap's value (4), the legacy 16-beats-back/8-forward window, the
boundary-tick-belongs-to-the-segment-it-starts convention"* — the segment cap is a value of L2's own
decode (register entry D-004, group A). D-004 is NOT a candidate of L2's family — no row of the reading
file carries it — although the ruled group term reaches every entry of group A; so D-004 is outside the
population the criterion walks, no verdict reaches it, and this passage is the one route by which that
value could reach the session. Both grounds hold for L2 at least as strongly as for the pilot.

This session's sweep of the two spans found four further passages that state what this project's L2
currently does or how its score is shaped, none of them reached by any withheld identity:

- *(c)* In principle #17, the block *"EVERY DESK-SIMULATION TRACE RUNS AT IDENTITY WEIGHTS"*: *"runs
  the generative product with every weight at one — exactly the mandatory ablation baseline the design
  already carries. The desk simulation therefore tests the structure and the tables, not the weight
  layer."* It states the ruled shape of L2's score — counted tables combined by fitted weights, with an
  equal-weights ablation arm — which is D-525's content, and D-525 is IN.
- *(d)* In the conventions, the bullet *"CANDIDATE ADMISSION IS COMPLETION, NOT REFINEMENT"*: *"The rule
  that decides which chord classes the joint decoder will even consider is a piece that was never
  finished … what the admission rule actually is, and that it has no specified form … NOT loosening a
  threshold until orchestral scores pass."* The L2 charter itself makes the admission rule part of L2's
  specification; this passage states what this project's current one is (threshold-based, unspecified)
  and names the joint decoder.
- *(e)* In the conventions, the bullet *"ONE FIX IS DESIGNED ONCE OVER THE WHOLE ENUMERATED FAMILY"*:
  *"the empty-decode cliff turned out to have a sibling at the opposite end of the density spectrum … and
  an emission-side twin."* It states current failure behaviour of the decoder and its emission — what the
  code does.
- *(f)* In the conventions' issue-exhaustion block, the D-437 qualification's family sentence: *"could
  this item's search space contain a fact about (a) what the decoder or the emission READS — struck
  versus sounding tones, note counting, pitch representation — or (b) how candidates are ADMITTED?"* It
  names the decoder's and emission's inputs as an open defect family — L2's third limb.

Not swept: member (4), the dispatch-protocol section of `cowork_audit_protocol.md`, which the pilot also
did not sweep; this session did not read it. That is a bound, not a finding. Two further facts about the
mechanism, read at `render_what_was_cut`: a withheld passage is *"marked in place where it was removed"*
and counted in the read-me, so the session learns that a passage was cut and where, never what it said;
and the leak check does not run over member (2) at all, by design, so a passage is the only mechanism that
reaches it.

**Why this matters beyond independence.** The brief's stop-on-meeting clause makes the session stop when
it meets implementation-derived material. The `l0-l1` session met eight register entries in member (5)
and stopped *"without opening the rest of the largest member"* (Ruling 81's facts, citing §3al.4 of the
2026-08-31 record). A passage known to
be in member (2) is a known place for L2's session to stop at boot.

**The positions.**

*Position 1 — withhold (a) and (b) with L2's own findings and reasons, and nothing more: the pilot's
precedent.* Towards the objective: the two disclosures of ruled content are cut; (c) to (f) stay, and a
session that meets one either stops or reads it. Towards the principles: least authored input; but the
generator's own docstring already declares the residual (*"That member (2) carries no other leak"* is not
asserted), and knowingly leaving four found passages in is #19's merely-unfalsified shape with the
falsification in hand.

*Position 2 — withhold (a) to (f), all six.* Towards the objective: highest — every passage this side
found that states L2's current mechanism or score shape is cut, and the session's chance of stopping at
boot on member (2) is reduced to what the sweep missed. Towards the principles: #19 served (the cut is
mechanical, verified both ways); the cost is four more authored passages, each with anchors that must
match exactly once, and each a place for an anchor to drift when `CLAUDE.md` grows — which is the drift
that froze two packs. (f) is the weakest of the four: it names a defect family rather than a mechanism,
and a reader could argue it discloses existence, not content.

*Position 3 — withhold (a), (b), (c), (d), (e); leave (f).* The same as Position 2 with the weakest cut
left in, on the pilot's own distinction (*"the disclosure is content, not existence"*, the second
passage's reason).

**Recommendation: Position 2.** The strongest argument against it is the anchor cost and the precedent
of two frozen packs; what answers it is that L2's pack will itself be frozen once its session runs, that
the STOP on a drifted anchor is loud rather than silent, and that (f) does state content — that the
decoder's inputs are struck-versus-sounding tones is a fact about what the code reads, which is the
third limb's subject.

**What it does NOT do.** It amends no word of `CLAUDE.md`; a withheld passage governs what a pack
carries, not what the document says. It reopens neither frozen pack. Its anchors are written by the
dispatch and verified at the file before it is released.

### Decision 6 — withheld documents for L2

**What is being decided.** Which documents are named in `WITHHELD["l2"]["withheld_documents"]`.

**The facts.** A withheld document is not a pack member in any case — no project document beyond the
members is in the pack, and the brief stages no project document. Naming a document there does two
things, read at the generator: the leak check over members (5) and (6) strikes any rendered entry whose
four fields carry the withheld document's name and lists it under `LEAKS` for you; and the manifest
records the document with its finding, date and reason. The pack's read-me does NOT name withheld
documents — its what-was-cut section is derived from the withheld entries, the withheld passages and the
extras' filters only (read at `render_what_was_cut`), so a withheld document is invisible to the session. The leak check already strikes any entry carrying a withheld identity string, a
`docs/` or `src/` path, or the string `ARCHITECTURE.md`. The pilot names one document,
`cowork_joint_estimator_factorization.md`, on the ground that it is the oracle's second arm. For L2 no
ruling names an oracle (reading file §3, sourced there). L2's IN entries are homed, among other places,
in `cowork_joint_estimator_architecture.md` (D-524 to D-528, all IN), `cowork_joint_estimator_factorization.md`
(D-565, IN), `cowork_layer3_keymode_design.md` (the group-F entries, 16 IN), `cowork_layer4_chordsymbol_design.md`
and `docs/scoring_model.md` (the group-G entries, 27 IN) — read at `DECISIONS.md`'s index rows for those
groups. An OUT entry whose verbatim names one of those documents would, without a withheld-document
entry, render into the pack with the name in it.

**The positions.**

*Position 1 — the two joint-estimator documents, by hand.* Towards the objective: the two documents that
carry the ruled architecture of L2's decision are struck wherever named. Towards the principles: small
and checkable; its cost is that the layer design documents are not, and their names in an OUT entry's
verbatim would pass.

*Position 2 — every home document of an IN entry, the list DERIVED by the pack-build dispatch from the
register's data file and STOPPED for your confirmation before it is authored into the table.* Towards the
objective: the strike covers every document that houses a withheld answer, and nothing is named that the
family does not already withhold from. Towards the principles: it is the criterion-shown-first shape
Ruling 12 used (*"the criterion written and shown to the user BEFORE the selection is run"*); the list is
derived, not hand-typed (#17f, D-431), and authored only after you have seen it. Its cost is one STOP in
the dispatch and a longer authored table.

*Position 3 — none.* Towards the objective: lowest; a document name in an OUT entry's verbatim passes
into the pack. Excluded.

**Recommendation: Position 2.** The strongest argument against it is that the list will be long and
will include documents whose names are already struck by the standing `docs/` string
(`docs/scoring_model.md` among them), so part of it changes nothing the session sees; what answers it is
that a withheld document is invisible to the session in any case, so the cost of a long list falls on the
authored table alone, while a short list leaves a named home of a withheld answer able to pass in an OUT
entry's verbatim.

### Decision 7 — what the brief stages: scores, and whether their published analyses

**What is being decided.** Whether L2's deriving session is given notation to read, and whether the
scores it is given come with their published human analyses. This is the brief's business, not the
pack's, but the pilot and `l0-l1` each ruled it beside the boot list (Rulings 12 and 15 of the 2026-08-31
record), and the dispatch that builds the pack is the one that would prepare the staged set.

**The facts.** For `l0-l1` you ruled PLAIN SCORES ONLY, selected by a criterion shown first (Ruling 12,
your words "B it is"), then widened the set to span named notational phenomena (Ruling 15). Ruling 12's
declined option C — *"scores with their published analyses, pilot-style"* — was declined for L1 on the
ground that an analysis *"answers a DIFFERENT LAYER's question … a Roman-numeral analysis says where an
analyst heard a chord, never where the sounding set changes."* For L2 that ground inverts: where an
analyst heard a chord, in which tonality, with what elaborations, is L2's question exactly. The framework
was itself read off the ground truth's form (§9.0: *"the ground truth is a record of decisions"*), and
DP-N's evidence is two independent analyses of the same bar disagreeing (`i6/4` against `Cad64`). Ruling
12's second ground against C stands unchanged: one annotation family, BCMH, is not established as an
instrument (D-475), and only *When in Rome*/DCML is ground truth under the ruled grading conventions.
The standing bars carry over whatever is chosen: files staged BY NAME and never a directory; EXEMPLARS,
NOT A CORPUS; the session builds, designs, scopes and runs no measurement over them.

**The positions.**

*Position 1 — the `l0-l1` staged set unchanged, plain scores only.* Towards the objective: the session
meets notation but never an analyst's decision; it derives what an analysis IS from the framework's
account alone. Towards the principles: no new selection; its cost is that the primary evidence for L2's
question — what analysts actually decided, and where they disagreed — is withheld from a session whose
charter question is that decision.

*Position 2 — a small set of scores WITH their *When in Rome*/DCML analyses, selected to exhibit named
phenomena of L2's four limbs (a modulation with a tonicization beside it; a cadential six-four; a passage
where the annotation records a rival reading in the same stream; a suspension or passing-tone texture
where the chord-tone assignment is non-trivial), each claim checked at the file before staging — plus the
plain-score set of Ruling 15 for the notation it exercises.* Towards the objective: highest — the session
sees the decisions it must specify how to make, in the form the ground truth records them. Towards the
principles: #1 (the ground truth is fact); #21 (the analyses are an instrument and only the established
family is used); Ruling 15's own test (a selection claiming named phenomena is checkable at the score);
its cost is this side's selecting hand, bounded as Ruling 15 bounded it.

*Position 3 — Position 2 without the plain-score set.* Cheaper by a few files; loses the notation-only
cases Ruling 15 chose for L1's faces, which L2 consumes through L1's publications.

**Recommendation: Position 2.** The strongest argument against it is fit/evaluation separation (#20): the
DCML chorales are what the current implementation is fitted on and graded against, and a derived
specification written with some of them open could later be said to have seen the test. What answers it
is that a derived specification fits nothing — #20 governs fitted values, and the session is barred from
measurement — and that the pilot staged analyses on exactly this footing (Ruling 12's own words for its
option C: *"scores with their published analyses, pilot-style"*).

**What it does NOT do.** It selects no score and names none; the named set with each claim beside it is
a later read put to you, as Ruling 15 ordered for L1.

### Decision 8 — the two guard reds the write-back batch left standing

**What is being decided.** Whether two derived artifacts the write-back batch's own ordered acts staled
are regenerated in the pack-build dispatch, or left.

**The facts, each read at the object this session.** The committed `tools/audit/guard_state.json` reports
77 run, 12 failing: the ten inherited plus `gen_evidence_pin_membership.py --check` and
`gen_l0_l1_outgoing_population.py --check`. The report `cc_report_l2_ruling_writeback_2026_09_05.md` §5
establishes both causes: the first because Task 0 landed a root-level `cowork_rulings_*.md` whose leading
blockquote names the generated reading surface, and that tool derives from every such record, so
regenerating would publish the reading surface's generator as a pinned-evidence member UNRESOLVED; the
second because the Task 5 `STATUS.md` entry put the word *"identities"* into that file, whose substring
*tie* is one of the tool's seven recorded single words — checked by this session at `STATUS.md`: across
the whole file the only match of any of the seven words is that one, on line 8; the 27 admitting phrases
were not checked by this session and CC's "one hit of 34" is relayed for them. The hit is recorded tier,
so the population is unchanged and a recorded-hit count moved. The batch declined to regenerate either
because its dispatch authorised two artifacts and each of these is a third, and declined to reword its
own entry to turn a check green (*"adjust nothing to reach a number"*).

**The positions.**

*Position 1 — regenerate both in the pack-build dispatch, the evidence-pin artifact publishing its new
member UNRESOLVED as its own rule provides, for you to resolve at that artifact.* Towards the objective:
nothing — these are apparatus. Towards the principles: the tree matches its derivations (#10's sync
purpose); the UNRESOLVED member is the tool's designed way of putting a question to you, and leaving it
unpublished is not answering it. Cost: two regenerated artifacts in a dispatch about something else, each
declared.

*Position 2 — leave both standing, the guard set at twelve.* Towards the principles: the failing set
grows by two apparatus reds that every later batch must re-establish as inherited; the entry-109 standing
item that the pruning bound is unmaintained already shows how inherited debt accumulates.

**Recommendation: Position 1**, as Task 0 or a rider of the pack-build dispatch. The argument against is
the one CC gave — an artifact whose job is to put a question to you should not be moved by a batch about
another subject; what answers it is that regenerating publishes the question rather than answering it.

### Decision 9 — the `STATUS.md` entry that says "ELEVEN FAILING"

**The fact.** The Task 5 entry of the write-back batch (`STATUS.md` line 8) says *"77 GUARDS RUN, ELEVEN
FAILING"*. The end-state artifact committed one commit later says twelve, the twelfth caused by that very
entry. The report and the close section were corrected; `STATUS.md` was not, and CC did not flag it. So
the session-start read carries a count the committed artifact contradicts.

**What the record says.** D-674: a dated report is re-bannered and never rewritten; a live governing
surface has its body corrected. `STATUS.md`'s own banner calls it a living document; its entries are dated
batch records that move whole to the archive when superseded (the 2026-08-17 archiving rule quoted at its
foot). Ruling 4 of the 2026-08-17 governing-surface split makes an entry SUPERSEDED the moment a later
batch's close exists — so the pack-build batch's own close supersedes this entry in any case.

**The positions.** *Position 1 — correct the word in place in the pack-build dispatch, the former wording
preserved beside it (D-674's branch two, the shape the batch used for the report itself).* *Position 2 —
leave it; the next batch's entry supersedes it and the close section already carries the correction.*

**Recommendation: Position 2.** The entry is a dated record whose falsity is already corrected in the two
records that outlive it, and the next close supersedes it mechanically; correcting it costs a read-size
regeneration for no reader who would otherwise be misled. The argument against: the session-start read is
the one surface every session reads, and P-1 makes that read binding — a false count there is met by
every session until the next close. If the pack-build dispatch is more than a few days away, Position 1
is the better answer.

---

## 4. What this surface does NOT do

It renders no pack, writes no dispatch, authors nothing into `EXTRAS` or `WITHHELD`, and boots no
session. It lifts no gate and reads no paper. It takes no position on any verdict of the ruled family,
which is closed. It amends no governing document. It does not write the brief, whose P1 (a fresh Cowork
session derives — and Ruling 13's own ground applies to L2 with more force, since the ordinary
session-start read includes `DECISIONS.md` whole, which lists L2's decisions), P2 (research allowed,
unbounded) and P4 (one dated output file) it expects to inherit unchanged from `l0-l1`, stated so that
they are not re-decided by silence. The `DATE` mechanism owed at the pack-build batch (four sites in the
generator, per the hundred-and-ninth entry) is dispatch work and needs no ruling. No decisions-register
identity is allocated; that register cannot accept one and
`cowork_register_rule_c_suspension_2026_08_28.md` is the route.

---

*Provenance: Cowork, 2026-09-05, at tip `911f5f7cdaa3fb53b9b5a2bdefb82e793c65eafb` read at both ref
files. Read whole with the file tools this session: `CLAUDE.md`, `DECISIONS.md`, `STATUS.md`, the
derived gating answer at its field; `cowork_handoff_entry_one_hundred_and_nine.md`;
`cc_report_l2_ruling_writeback_2026_09_05.md`; `cowork_curated_boot_list_draft_2026_08_19.md`;
`cowork_rulings_2026_08_22_boot_list_sitting.md`; `cowork_rulings_2026_09_05_l2_withheld_family_sitting.md`;
`reading_pass/candidacy_upgrades.md`; `cowork_reading_pass_remedial_commission_2026_08_31.md`. Read at
the named sections: `FRAMEWORK.md` §5 and §9; `cowork_rulings_2026_08_31_decision_surface_sitting.md`
§3j to §3q and §3cj; `tools/audit/gen_derivation_boot_pack.py` lines 1 to 878 (the docstring, `MEMBERS`,
`FROZEN`, `EXTRAS`, `WITHHELD`, the criteria), the two ruled tuples, `render_what_was_cut` and
`render_read_me`; the directory listings of `reading_pass/` and its subdirectories; `tools/audit/gen_withheld_family_reading.py`
`SUBJECTS["l2"]`; `ratification_surfaces/cowork_withheld_family_l2_reading.md` §1 to §7;
`reading_pass/population.md` §3 and §3a; `EMPIRICAL_FINDINGS_LEDGER.md`'s banner; the extract headings
under `reading_pass/extracts/`. No count in this document is a measurement of the analysis; the counts
are counts of rows of the files named. TOWARDS the ultimate objective and TOWARDS the guiding principles.*

# Decisions group D — Layer 1 — the note model

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-037 — The note model is the single source of truth for what sounds, and reads the score once

> **The lossless, tie-resolved NOTE MODEL — the single source of truth for "what sounds."** `NoteModel::build(score)` reads the score **once**

**In plain words.** One component reads the score and works out which notes are sounding when. Everything else asks it, and nothing else reads the score.

**Why.** Stated constraint, ARCHITECTURE.md:1173: one read of the score into one queryable set is what makes the note model the single source of truth for what sounds; the alternative is several readers that can disagree.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1575`

**Provenance.** ARCHITECTURE.md:1162-1173 (Layer 1 - Built+Live) ★ THE DECIDING ACT RECORDED AND KEPT (user's ruling of 2026-08-17, cowork_rulings_2026_08_17_residue_sitting.md §2 (Ruling 2) — a ratification of a document reaches the decisions that document carries): the recovered act ratifies `OPEN_ITEMS.md`, and that document carries this entry's own subject recogniser the decisions register's own recogniser `note model` at line 208, reading — "| OI-241 | ★ A MISSING RULING (the user's to make): no GENERAL rule states which existing MuseScore code our code may depend on — only scoped forms exist | Checked rather than assumed, at the dispatch's direction. What EXISTS: D-227 (§2.8 — follow MuseScore's patterns, never invent parallel infrastructure: a rule about imitation), D-072 (§3.3 — the dependency ORDER is enforced, analysis depends on no engraving type), D-228 (§3.3 — the bridge PATTERN: shape and location of the functions that touch engraving types), D-073 (§2.10 — shared logic has one implementation), D-120 (§17.1 — coding style), D-143 (§19.4 — the future language-model module confined to the Core Access Layer, the ONE permitted-interface rule stated anywhere, scoped to a module that does not exist yet). What does NOT exist: any statement of which MuseScore interfaces the BRIDGE layer may call — whether it must go through" The match is quoted from `tools/audit/ratified_document_check.json`; no other field of this entry is touched.

### D-040 — The tie-unresolved atoms are republished additively for the joint estimator

> `notatedNotes()` republishes the tie-UNRESOLVED atoms — EVERY notated note incl. tie continuations, each with its OWN notated span, a `tieContinuation` flag, a `hasFermata` flag, and `resolvedIndex` linking to its tie-resolved `NoteEvent`

**In plain words.** As well as merging tied notes, the note reader also publishes them separately, each with a marker saying it is a continuation. The joint estimator needs both views.

**Why.** Stated constraint, ARCHITECTURE.md:1173: the tie-unresolved atoms carry the facts the tie-resolved surface discards and the joint estimator's event lattice and emission covariates need; publishing them additively keeps every existing consumer byte-identical.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1575`

**Provenance.** ARCHITECTURE.md:1173 records it as 'Purely additive' under the OI-180 dual-path sanction ★ THE DECIDING ACT RECORDED AND KEPT (user's ruling of 2026-08-17, cowork_rulings_2026_08_17_residue_sitting.md §2 (Ruling 2) — a ratification of a document reaches the decisions that document carries): the recovered act ratifies `cowork_handoff.md`, and that document carries this entry's own subject recogniser the decisions register's own recogniser `notatedNotes` at line 2407, reading — "`notatedNotes()` additive publication landed under both proofs, catching and fixing a latent infinite-loop on partial ties. Task C DELIVERED and verified (`8416b2c84c`, `020baca347`, pushed): the fact adapter reads only the published surface; input parity 300/326 byte-perfect with ONE mechanically-unmappable class (metric position — music21 read the xml's EDITORIAL measure bookkeeping, the production engraving model normalizes it; ~26 pathological-measure pieces; end-to-end 320/326 identity, 316/326" The match is quoted from `tools/audit/ratified_document_check.json`; no other field of this entry is touched.

### D-569 — Collecting, filtering and weighting are THREE separate responsibilities; the collection layer collects and annotates, and does nothing else

> ## §1 — Intended role (the single responsibility) — REVISED per user review 2026-06-21
> **Collect — and only collect — every sounding note in a region, annotated, losslessly, by ONE path.** It is the
> boundary between the engraving model (Score/Segment/Note) and the analysis types. It answers exactly one factual
> question: "for region `[startTick, endTick)`, what notes sound?" — and returns the **note set**, each note
> annotated with the facts needed downstream (pitch, tpc/spelling, staff, voice, onset, offset, in-region
> duration, `isGrace`, `plays`, `visible`, staff-eligibility). It must **NOT** filter (drop grace/non-playing/
> invisible), **NOT** weight or aggregate into pitch-class evidence, **NOT** select a bass, and **NOT** make any
> harmonic/segmentation/key decision. Those are *separate* responsibilities (see §5):
> - **Collection** (this layer): the facts — every sounding note, annotated, preserved, one path.
> - **Filtering** (a distinct, explicit decision): which annotated notes are eligible for harmonic analysis.
> - **Weighting** (a distinct derived layer): the pitch-class evidence + bass, computed as a *view* over the
>   collected notes — never replacing them.

**In plain words.** Finding out which notes sound in a stretch of music, deciding which of them the harmonic analysis should consider, and turning them into weighted evidence are three different jobs. The first is a matter of fact, the second a decision, the third an interpretation. The collection layer answers only the factual question and hands the notes on annotated with everything a later step could need.

**Why.** The reason is given as the consequence of merging them, which the document traces at the code: doing all three in one pass is what forces the notes to be thrown away, what makes the dropping silent, and what produced two divergent collection paths. The corrected role was written on the user's own review of 2026-06-21, whose three comments the document records — no multiple paths, collect don't drop, separate collecting from weighting.

**Status.** LIVE · decided 2026-06-21 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_layer1_tone_collection_design.md:33-44`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **the opening block (above the first section heading)** — `# Layer 1 — TONE COLLECTION — Design Document (for user sign-off)` (heading at line 1). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** `cowork_layer1_tone_collection_design.md`, the Layer-1 tone-collection design put to the user for sign-off. Read in full by READ WAVE 4, 2026-08-04. The section is marked *REVISED per user review 2026-06-21* and records the three review comments it was corrected against. **The decision LANDED**: the note model carries the facts losslessly and the weighting survives as a derived view over it — the entries for that as-built state are **D-039** (ineligible notes kept and flagged, never dropped) and **D-038** (spans answered by overlap with no horizon), both homed in `ARCHITECTURE.md`. This entry is the RULE those two implement, with its own defense.

### D-570 — An upstream layer's correctness oracle is the SCORE, not the Roman-numeral ground truth

> ## §6 — Correctness oracle for this layer (it is NOT the RN oracle)
> This layer is upstream of key and chord, so its correctness is judged against the **score**, not DCML/music21:
> does it collect exactly the notes a human reading the score would say sound in `[start,end)` (right staves,
> right sustains, right filters), with bass and weights that faithfully reflect the notation? Completeness = all
> note cases handled (sustains past the cap, ties, tuplets, grace, cross-staff, multi-voice unisons, pedal,
> invisible/non-playing). The audit builds score-level test cases for each; the per-event tiered metric does **not**
> cover this layer.

**In plain words.** Because this layer sits before any decision about tonality or chords, whether it is right is judged against the notation itself: does it collect exactly the notes a musician reading the score would say are sounding in that stretch, from the right staves, with the right sustains. The published harmonic analyses cannot judge it, and the per-event agreement measurement does not reach it.

**Why.** It follows from what the layer decides: a layer that makes no harmonic claim cannot be graded by a harmonic annotation, and grading it by one would make an unrelated downstream disagreement look like a collection error. The document states the completeness condition beside it — every note case handled, enumerated — so the oracle is checkable rather than a sentiment.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_layer1_tone_collection_design.md:198-204`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **“§5”** — `## §5 — Proposed target design (for ratification/amendment)` (heading at line 171). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** `cowork_layer1_tone_collection_design.md`, the Layer-1 tone-collection design put to the user for sign-off. Read in full by READ WAVE 4, 2026-08-04. Recorded as the document's §6, headed in terms *it is NOT the RN oracle*. The record states no date and no ratifier for this clause. It is the layer-level statement of the standing rule that ground truth is itself an instrument (`CLAUDE.md` #21). ★ THE DECIDING ACT RECORDED AND KEPT (user's ruling of 2026-08-17, cowork_rulings_2026_08_17_residue_sitting.md §2 (Ruling 2) — a ratification of a document reaches the decisions that document carries): the recovered act ratifies `OPEN_ITEMS.md`, and that document carries this entry's own subject recogniser the entry's own identity at line 371, reading — "| OI-333 | **The cluster-disposition layer CANNOT BE REGENERATED at HEAD** — six register patterns are invalid regular expressions, and the guard that watches that tool is structurally incapable of seeing it | Found by ATTEMPTING the regeneration (CC, READ WAVE 6, 2026-08-04), not by reading. The write mode of `tools/audit/decisions/gen_cluster_dispositions.py` terminates with an uncaught `re.PatternError: multiple repeat at position 3`, raised at `:407` where each entry's `patterns` are compiled. **The cause, enumerated at the data:** six entries carry a pattern containing UNESCAPED markdown emphasis — a literal `**`, which the compiler reads as a repeat applied to a repeat — and all six were authored by READ WAVE 5 on 2026-08-04: **D-555**, **D-570**, **D-576**, **D-577**, **D-578**, **D-581**. Every other pattern in the register escapes its emphasis or avoids it, which is what makes t" The match is quoted from `tools/audit/ratified_document_check.json`; no other field of this entry is touched.

### D-606 — The binding metric for the modulation detector is modulation CORRECTNESS — explicitly not the agreement percentage, which the change under test can game

> - **THE BINDING METRIC FOR A MODULATION DETECTOR IS MODULATION CORRECTNESS — explicitly NOT the
>   agreement percentage** (2026-06-14; the record states no ratifier). A change that decides where
>   the music changes key is judged on whether the key changes it commits are real ones (precision)
>   and whether it finds the real ones (recall) — the track rate together with the de-masked partial
>   split — and never on the overall agreement percentage. *Why:* stated with the decision — the
>   agreement percentage is **gameable by the change under test**, so it cannot be that change's own
>   bar. It is the same defect the abstain-aware convention above exists against on the root axis: an
>   agreement percentage a behaviour change can move without analysing anything better is not a
>   measurement of that change. The honesty measurement named with it is the de-masking diagnostic,
>   which exposes a committed home-key label being credited against a ground-truth local key.

**In plain words.** A detector that decides where the music changes key is judged on whether the key changes it commits are real ones and whether it finds the real ones — not on the overall agreement percentage, which a detector can raise without detecting anything better.

**Why.** Stated with the decision: the agreement percentage is gameable by the change under test, so it cannot be the bar for that change. It is the same defect the abstain-aware convention (**D-212**) exists against on the root axis — an agreement figure that a behaviour change can move without analysing anything better is not a measurement of that change.

**Status.** LIVE · decided 2026-06-14 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `CLAUDE.md:965-974`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `docs/stage4d_local_modulation_design.md`, the Stage-4d local-modulation design, DRAFT and ratification-gated, 2026-06-14. Read in full by READ WAVE 5, 2026-08-04. Recorded in the staged-build section, which also names the de-masking diagnostic as the honesty measurement — it exposes a committed home-key label credited against a ground-truth local key. ⚠ The detector is on the LEGACY key path and the staged build described was never carried past its own gate on the arm that now runs; the rule about which metric may bind is not legacy-scoped. The record states no ratifier. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Ruled a GRADING CONVENTION — the binding metric for a modulation detector is modulation correctness — and homed in `CLAUDE.md` gate block (A) beside D-604, where the abstain-aware convention it cites already lives; the home text cites that convention rather than restating it (#6). Written in the gate block's own voice and with its defense. The D-645 licence covers `CLAUDE.md` for homing acts. The edit is ADD-ONLY. FORMER HOME, PRESERVED (#12): `docs/stage4d_local_modulation_design.md:78-80`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 74, "section": "## §5 — Staged build (measure-first, per discipline)", "label": "“§5”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**The binding metric is modulation
  CORRECTNESS (track-rate + the de-masked partial split), NOT the gameable rn_agree** — a span we commit
  must be a real DCML modulation (precision) without missing the real ones (recall)." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-625 — Spelling presence is tested with the validity predicate, never with a non-negative test — the flat side of the line of fifths is negative and a non-negative guard silently drops it

> - **Spelling presence is tested with the VALIDITY PREDICATE, never with a non-negative test.** The
>   shared line-of-fifths primitive the spelling-pin above reads — the one interpreter, not a
>   per-layer copy — represents a spelling as a signed position on the line of fifths, and its
>   presence test is `tpcIsValid()`, **never** `tpc >= 0` and never `tpc != -1`. *Why:* established
>   at the source rather than asserted — the flat side of the line of fifths is **negative** (down to
>   the triple-flat spellings), so a non-negative guard silently discards every heavily flattened
>   spelling; and the value a `!= -1` guard treats as absent is itself a **legitimate** spelling. The
>   honest bound is recorded with the rule: the validity test cannot tell a real flattest spelling
>   from a default-initialised field, and what actually keeps an absent value out is the build-path
>   invariant, not this predicate. §5.14, which specifies the enharmonic disambiguation this
>   primitive serves, points here and does not restate it (#6).

**In plain words.** How a note is spelt is stored as a position on the line of fifths, and that position is negative for the flattest spellings. Code that checks whether a spelling is present by testing for a non-negative number therefore throws away every heavily-flattened spelling — including one that happens to share its number with the field's empty value. The validity test is the correct check.

**Why.** Established at the source: the mapping, the constant, the real range and the two named flat-side spellings were all read in the engraving header, and the consequence of the wrong guard is derived from them rather than asserted. The design also states what the check does NOT do — the validity test cannot tell a real flattest spelling from the field's default — and names the build-path invariant as the thing that actually keeps an absent value out, which is the honest bound on the rule.

**Status.** LIVE · decided 2026-06-26 · ratifier not stated

**Home.** `ARCHITECTURE.md:2063-2073`

**Provenance.** `cowork_tpc_capability_design.md` §1, the shared spelling primitive's detail design, BUILT as a capability with no production consumer. Read in full by READ WAVE 6, 2026-08-04. The same section records that the chord scorer's existing inline spelling reads carry the wrong guard and that correcting them rides the fold into the primitive — an open unification question the document flags rather than closes. The record states no ratifier. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The ruling routes it to THE SECTION SPECIFYING THE SHARED LINE-OF-FIFTHS PRIMITIVE — the Layer-4 section per the record — with §5.14 pointing, and it carries a STOP: STOP IF THE PRIMITIVE IS SPECIFIED ELSEWHERE. ★ THE STOP WAS DISCHARGED BEFORE WRITING AND DID NOT FIRE: `ARCHITECTURE.md` names the primitive in exactly three places and specifies it in none — §3.3's terminology note DEFINES the term Layer 1.5 and lists the primitive among its two views; the Layer-4 section names it as the interpreter the symmetric-root spelling-pin reads through and states the one-interpreter rule about it; and Layer 1's own derived-views list does not mention it at all. Written into the Layer-4 section in that section's own voice, with its defense and with the honest bound the record states (the validity test cannot tell a real flattest spelling from a default-initialised field). §5.14 gains a POINTER, never a copy (#6). ★ AN ADJACENT FACT THE STOP SURFACED IS ROWED AND LEFT, not acted on: the sibling Layer-1.5 primitive is sited at Layer 1 with its reason stated in full, so the two Layer-1.5 primitives sit in different sections — `OPEN_ITEMS.md` OI-347. FORMER HOME, PRESERVED (#12): `cowork_tpc_capability_design.md:39-43`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 20, "section": "## 1. The shared tpc-interpretation primitive (the capability)", "label": "§1", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**Validity & mapping (verified at source, 2026-06-26).** Line-of-fifths position = `tpc − TPC_C` with `TPC_C = 14`
(+1 tpc = +1 fifth; `pitchspelling.h`). Sharp/flat sense = the sign of that offset. **The primitive must test presence
with `tpcIsValid()` (= `−8 ≤ tpc ≤ 40`), never `tpc >= 0` / `tpc != −1`:** the flat side of the line of fifths is
**negative** (`TPC_F_BB = −1`, down to `TPC_F_BBB = −8`), so a `>= 0` guard silently drops every double-flat-ish
spelling — and `−1` is a *legitimate* spelling (Fbb), not "absent."" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).


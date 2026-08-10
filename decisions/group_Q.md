# Decisions group Q — Scope and the development toolchain

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-162 — The development tools are not part of the shipping product

> The following tools live in `tools/` and are **not part of the shipping product**.
> They are compiled/run only in development builds (`MUE_BUILD_ENGRAVING_DEVTOOLS=ON`).

**In plain words.** The batch analysis tool, the comparison scripts and the remaining measurement tools are built only in development builds and never ship to a user.

**Why.** SEARCHED 2026-08-09 (CC, `cc_instruction_return_continuation_3.md` Task 2). The record holds no reason. The home states the rule and then its MECHANISM — the tools are compiled and run only in development builds, behind a named build option — and a mechanism is how the rule is enforced, not why it was adopted. Nothing is said about why they must not ship, no alternative is weighed, and no date or ratifier is stated.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:7620`

**Provenance.** ARCHITECTURE.md:6419-6422 (§15). No date or ratifier stated.

### D-163 — The batch tool deliberately skips post-load layout

> and `iex_musicxml` — no notation module required. Because the tool only consumes
> logical score structure, it deliberately skips forced post-load layout; this avoids
> legacy native MSCX cache-overflow crashes (for example Mozart `K533-3`) without
> changing the emitted harmonic-analysis JSON.

**In plain words.** The headless analysis tool never lays the music out on the page, because it only ever reads the logical structure.

**Why.** Stated constraint, ARCHITECTURE.md:6431-6433: skipping the layout avoids a legacy cache overflow crash on some scores (Mozart K533-3 is named) without changing the harmonic-analysis output at all.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:7629`

**Provenance.** ARCHITECTURE.md:6424-6433 (§15). No date or ratifier stated.

### D-164 — What is out of scope, and what degrades gracefully at the boundary

> Live and real-time operation, film synchronization, adaptive game music, non-Western
> traditions (graceful degradation at boundary), post-tonal and serial music (graceful
> degradation at boundary), audio transcription from recording, spatial music, extended
> techniques as primary language.

**In plain words.** Live performance, film and game synchronization, audio transcription, spatial music and extended techniques as a primary language are not attempted. Non-Western traditions and post-tonal music are not attempted either, but the system is required to fail gracefully where it meets them rather than producing confident nonsense.

**Why.** SEARCHED 2026-08-09 (CC, `cc_instruction_return_continuation_3.md` Task 2). The record holds no reason. The home is a LIST under an "Out of Scope" heading, inside a section that sorts the whole feature set into core, important, prepared and out-of-scope tiers: the classification is recorded, its ground is not, and no item carries an individual justification. The two graceful-degradation parentheticals — on non-Western traditions and on post-tonal and serial music — state a FURTHER REQUIREMENT at the boundary rather than a defense of the exclusion, and are recorded as that. No date and no ratifier are stated.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:7839`

**Provenance.** ARCHITECTURE.md:6594-6643 (§16), which sorts the whole feature set into Core / Important / Prepared / Out of scope. No date or ratifier stated.

### D-308 — A newly acquired corpus enters as research material; the frozen regression corpus stays the gate until a deliberate re-baseline

> - **A NEWLY ACQUIRED CORPUS ENTERS AS RESEARCH MATERIAL; the frozen corpus above stays the gate until a
>   deliberate re-baseline** (user-ratified 2026-07-02; homed here 2026-08-02 from `STATUS_ARCHIVE.md`,
>   `OPEN_ITEMS.md` OI-272). Music brought into the project for study does not become part of the pass/fail

**In plain words.** Music brought into the project for study does not become part of the pass/fail check by arriving. The frozen set the regression check runs on changes only by a separate, deliberate act.

**Why.** derivation not recorded

**Status.** LIVE · decided 2026-07-02 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `CLAUDE.md:699-701`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Recorded in `STATUS_ARCHIVE.md` (session 21, at the user's ratification of the external architecture review's corpus-expansion amendment). Related but distinct from **D-225** (a corpus is regenerated before its baseline figures are updated) and from the re-baseline discipline in `CLAUDE.md` gate block (A). Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue). ★ HOMED 2026-08-02 (CC, phase 1j, executing the user's per-kind ruling on [[OI-272]] — measurement conventions go to the gate block): written into `CLAUDE.md` gate block (A) beside the re-baseline discipline it bounds. Former home preserved (#12): `STATUS_ARCHIVE.md:250`. The same rule is stated on the corpus side at `cowork_score_census.md`'s decision-tier block, which the homed text names.

### D-309 — A corpus the analysis handles badly stays on the roadmap marked deferred; it is more valuable than one that confirms what already works

> 7. **A corpus the analysis currently handles BADLY is kept on the roadmap and marked
>    deferred — never dropped.** Music that produces poor results under the analysis as it
>    stands stays listed, becoming the validation target of the next capability built

**In plain words.** Music our analysis currently does poorly on is not dropped from the plan. It is marked as waiting, and becomes the test of the next capability we build.

**Why.** The reason is stated with the rule: a corpus that exposes a gap is worth more than one that confirms an existing strength, so a poor result is treated as information about what to build rather than as a reason to discard the material.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `docs/score_inventory.md:357-359`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Recorded in `STATUS_ARCHIVE.md` as the stated design principle of the validation-corpus roadmap. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue). ★ HOMED 2026-08-02 (CC, phase 1j, executing the user's per-kind ruling on [[OI-272]]): written as hard rule 7 of `docs/score_inventory.md`, the document `CLAUDE.md` directs every score or corpus task to read first. Former home preserved (#12): `STATUS_ARCHIVE.md:2938`, the validation-corpus roadmap.

### D-310 — Jazz accuracy is not measurable on the corpora held: the low agreement is missing bass and piano voicings, not a scoring failure

> **The standing consequence: jazz accuracy is NOT MEASURABLE on the corpora we hold, and no
> jazz-specific scoring work is planned on them.** The low agreement on the jazz material in the
> project is a property of the material — melody-and-chord-symbol transcriptions with the bass and

**In plain words.** The jazz scores we hold are melody-and-chord-symbol transcriptions with the bass and the piano chords left out, so our analysis has too few notes to work from. The poor agreement measures the material, not the analysis, and no jazz-specific scoring work is planned until scores with the missing parts written out are available.

**Why.** Measured: a bass-injection experiment that supplied the missing root before analysis raised one jazz corpus from 39.8 % to 98.3 % and another from 18.0 % to 99.9 % agreement, which is what identifies the shortfall as missing material rather than mis-scoring (`STATUS_ARCHIVE.md:1575-1583`).

**Status.** LIVE · decided 2026-04-08 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:3355-3357`

**Provenance.** Recorded in `STATUS_ARCHIVE.md` (the jazz-corpus status block). It is the standing evidence behind [[OI-7]] (establish a jazz ground-truth corpus or de-scope the Jazz correctness claims) and behind the A-7 empirically-unvalidated mark. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue). ★ HOMED 2026-08-02 (CC, phase 1j, executing the user's per-kind ruling on [[OI-272]]): written into `ARCHITECTURE.md` §4.2's jazz-validation block, directly beneath the bass-injection measurement that is its defense. Former home preserved (#12): `STATUS_ARCHIVE.md:1580`, the jazz-corpus status block.

### D-359 — Discovering a new corpus counts as a CENSUS DEFECT — the fix is to enumerate its container to closure, never to ingest the one repository

> **The standing process rule this census institutes:** from now on, *"a new corpus was discovered" is a census
> defect* — the fix is to add its **container** to the table above and re-enumerate that container to closure, not to
> ingest one repo and move on. **Re-sweep cadence: yearly** (new ISMIR proceedings + the `mirdata` loader list + the
> `ismir/mir-datasets` index are the mechanical catch-alls), and at any Stage-5/6 corpus decision.

**In plain words.** When a collection of music or of published analyses turns up that the census does not list, that is treated as a fault in the census rather than as good luck. The remedy is to add the whole container it came from — the organization, the meta-collection, the index — and walk that container to its end. Ingesting the single find and moving on is what produced the recurring pattern of rediscovery. The census is re-swept yearly against fixed indexes, and again at any corpus decision.

**Why.** Diagnosed from the project's own history: every previous hunt was keyword-driven sampling — search, take the good hits, stop when the current question is answered — which finds exemplars and never closure. The census's opening section states that diagnosis, and the trigger case is named: the DCML Wagner overtures corpus, found only during the 2026-07-02 architecture review.

**Status.** LIVE · decided 2026-07-02 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:30-33`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§1** — `## 1. Why corpora kept being "discovered" — and the method that closes it` (heading at line 13). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL. The document's banner records `Status: v1 DELIVERED (Cowork, 2026-07-02); for user disposition of the acquisition tiers (§5)` — the user disposition it names covers the acquisition tiers, not this rule. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-360 — A corpus enters the registry only with all five admission fields decided — annotation type, score alignment, format, licence class, decision tier

> A source enters the registry only with all five fields decided: **(a) GT type** (RN / chords / key / cadence /
> phrase / none); **(b) machine-readable score alignment** (symbolic score + annotation anchored to it — chords-only or
> audio-aligned sets are research-tier at best); **(c) format** (parseable today vs converter needed); **(d) license
> class** (PD/CC0/CC-BY committable; NC/unclear → hash-pin-only, the established mechanism); **(e) decision tier** (§5).

**In plain words.** No collection is recorded as usable until five things are settled about it: what kind of published analysis it carries, if any; whether that analysis is anchored to a machine-readable score; whether the format can be read today or needs a converter; which licence class it falls in; and which decision tier it enters at. A collection whose annotations are not anchored to a score, or that is aligned only to audio, is research material at best.

**Why.** The five fields are the ones the downstream decisions actually consume: the licence class is what the shipped-parameter constraint reads (**D-292**), the alignment field is what separates gradable material from research material, and the tier is what the acquisition instruction acts on. Sources whose licence is non-commercial or unclear are admitted hash-pinned only, which the census records as the established mechanism.

**Status.** LIVE · decided 2026-07-02 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:67-70`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§3** — `## 3. Inclusion criteria (what "a corpus we can use" means)` (heading at line 65). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-361 — Corpora are de-duplicated by WORK, not by container — and a work in the regression corpus is excluded as reference data from every other container

> The containers re-encode the same works (WiR↔DCML↔ChoCo; KernScores↔craigsapp↔music21↔MuseData; GigaMIDI absorbs
> Lakh/MetaMIDI). **Dedupe by work, not by container** — the registry keys on (composer, work, movement), and a work
> entering the gate corpus from one container is excluded as GT from every other (the M3 contamination lesson,
> generalized).

**In plain words.** The big collections re-publish each other's music, so counting collections double-counts the music. The registry is therefore keyed on composer, work and movement. And once a piece is in the corpus a change is graded against, that same piece may not be used as reference data from any other collection it also appears in.

**Why.** The exclusion rule is the generalization of a failure the project already had: the census names it the M3 contamination lesson — the shared-directory failure mode in which one style setting's output was measured against another's. Contamination by re-encoding is the same failure arriving through a different door.

**Status.** LIVE · decided 2026-07-02 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:74-77`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4** — `## 4. Overlap hazard (the accounting rule)` (heading at line 72). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-362 — What the census may claim, stated exactly: closure over the enumerated containers, a citation-closure argument for gradable harmony reference data, and a BOUNDED claim for everything else

> **What the census can prove:** closure **over the enumerated container classes** (§1). **The strong claim:**
> gate-grade common-practice RN/harmony GT is **citation-closed** — the field is small and cross-citing, so every
> serious GT corpus is used by a SOTA paper, aggregated by WiR/ChoCo, or indexed by mirdata/awesome-lists within ~a
> year of release; a corpus outside all of those is almost certainly not gate-grade. **The bounded (not closed)
> claim:** plain-score collections and peripheral/niche GT — the risk lives in **unknown containers** (Zenodo-only
> deposits, national-library editions, non-English sources, brand-new releases), which no enumeration can prove absent.

**In plain words.** The census proves only closure over the containers it lists. Its strong claim is narrower: published Roman-numeral and harmony reference data good enough to grade against is closed by citation, because the field is small and cross-citing, so any serious such corpus is used by a leading paper, absorbed into one of the two meta-collections, or listed in the standard indexes within about a year. Plain music collections and niche reference data get only a bounded claim: the risk sits in containers nobody has named, and no enumeration can prove those absent.

**Why.** Stated as the answer to a user question of 2026-07-02, and written this way for a named reason recorded elsewhere in the register: `DEFECT_TYPES.md` DT-26, scope-assumed enumeration — a sweep complete inside its own file set reads as complete about the whole question unless its scope and remainder are said out loud.

**Status.** LIVE · decided 2026-07-02 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:119-124`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8** — `## 8. The comprehensiveness claim, precisely stated — and the mitigation plan (added 2026-07-02, user question)` (heading at line 117). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-363 — Four named reasons license leaving a source un-enumerated — and non-Western symbolic music is closed by RULING, not by enumeration

> **Why some sources are deliberately not fully enumerated:** (a) **unwalkable** (MuseScore.com ToS beyond PDMX; IMSLP
> = PDF scans without a symbolic index) — cost exceeds value, content mostly non-machine-readable; (b) **mechanically
> closable later** (craigsapp via `humdrum-tools/humdrum-data`; DLC piece counts at clone time) — closure rides the
> acquisition instruction; (c) **snippet-verified rows** ([reported] marks) — a budget choice made visible, verified at
> acquisition; (d) **out of analytical scope by decision** (non-Western symbolic sets — the tonal model class does not
> cover them; review F-15) — closed by ruling, not enumeration.

**In plain words.** Some sources are deliberately not walked to the end, and each has a stated reason: the source cannot be walked at all, or its content is not machine-readable; it can be closed mechanically later and that closure rides the acquisition step; a row was verified only from a search snippet, a budget choice made visible and settled when the source is acquired; or the material is outside what the analysis covers by decision. Non-Western symbolic music is in that last class: the tonal model does not cover it, so it is closed by ruling rather than by counting.

**Why.** Each reason is tied to what it costs or to what already decides it: the unwalkable sources are ones where cost exceeds value and the content is mostly not machine-readable; the mechanically closable ones ride an acquisition step already scheduled; the snippet-verified rows are verified at the moment of acquisition; and the scope ruling on non-Western material cites the external architecture review's finding F-15.

**Status.** LIVE · decided 2026-07-02 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:126-131`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8** — `## 8. The comprehensiveness claim, precisely stated — and the mitigation plan (added 2026-07-02, user question)` (heading at line 117). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-364 — Every new analysis purpose triggers its own corpus sweep BEFORE its design document is signed — having enumerated the container does not discharge the duty to ask the new question of it

> **The standing trigger instituted (complements the yearly re-sweep + the wave triggers):** whenever a **new
> analysis purpose** enters the project — a new axis, a new component with a GT need, a new lever class — a
> **targeted, purpose-specific census sweep runs for that purpose** before its design doc is signed (the axis-2
> §6b sweep is the founding precedent: three census-grade finds in one pass, two on corpora already held). The
> sweep's finds enter via the census as always; "we already enumerated the container" does not discharge the duty
> to ASK THE NEW QUESTION against it.

**In plain words.** A census is only as complete as the list of questions it was asked with. So whenever a new purpose enters the project — a new analytical axis, a new component needing reference data, a new class of evidence — a search aimed at that purpose runs before that component's design is signed off. Already having walked a collection is not a reason to skip it: the new question must be put to it.

**Why.** Diagnosed from the repeated pattern the user observed, with two mechanisms named: collections are walked lazily by design, so their contents surface only when a wave walks them; and enumeration done with one axis's questions in mind cannot see reference data for a purpose that did not yet exist. The founding precedent is recorded — the second axis's own sweep returned three census-grade finds in one pass, two of them on collections already held.

**Status.** LIVE · decided 2026-07-03 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:166-171`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8b** — `## 8b. The recurring-discovery finding, and the PURPOSE-DRIVEN sweep trigger (user observation, 2026-07-03)` (heading at line 150). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL. The section is headed as a user observation of 2026-07-03; the record says the trigger is instituted but does not name who instituted it. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-365 — A corpus search driven by the SUM of all needs is worth running, but it is step 3 of 3 — the needs list and the re-scoring of what is already enumerated come first

> **The question that created this section:** is a corpus search useful that is NOT driven by one architectural
> need — the "need" being the sum of all needs? **Answer: yes, but the search is step 3 of 3.** The sum of all
> needs must first exist as an artifact, and once it does, re-scoring the EXISTING enumeration against it is
> cheaper and likely higher-yield than new searching (the Wave-2 lesson: the finds were already inside enumerated
> containers — the dismissals were purpose-relative, made with harmonic-axis eyes only).

**In plain words.** Searching against everything the project needs at once is useful, but only after two cheaper steps. First the full list of needs has to exist as a written artifact. Then every collection already enumerated is re-scored against that list, without searching at all. Only what is still uncovered afterwards is searched for.

**Why.** Measured by the second wave's own outcome: its finds were already inside collections the census had enumerated — what had missed them was that the earlier dismissals were purpose-relative, made with only the harmonic axis in mind. Re-scoring what is already listed is therefore both cheaper than searching and likelier to yield.

**Status.** LIVE · decided 2026-07-03 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:189-193`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8c** — `## 8c. The FULL-NEEDS AUDIT — the union-of-needs mechanism (user question, 2026-07-03)` (heading at line 187). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Its class before the phase-1n staged application was `gap`.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL. The section is headed as a user question of 2026-07-03; its first run is recorded EXECUTED and DISPOSED 2026-07-04, with the user's rulings at that disposition recorded in the same paragraph. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-367 — A corpus found FOR one need is scored against the WHOLE needs list at intake, and every annotation layer it carries is inventoried — never tagged to the purpose that found it

> **The intake rule (user, 2026-07-03 — the converse of step 2):** a find made FOR one need is **scored against
> the FULL needs-vector at intake**, never single-purpose-tagged. Three consequences, each binding:
> 1. **Already-satisfied needs stay open to supersession** — a new find may serve a "passed" need better or
>    cheaper than its current bed; the intake scoring records that even when no action follows.
> 2. **Future/inactive needs get pre-coverage** — a find's coverage of a not-yet-active column is recorded at
>    intake, so when that purpose's §8b sweep eventually runs it starts non-empty.
> 3. **Every GT LAYER of a container is inventoried at intake, not just the layer that motivated the find** — the
>    founding counter-example: the JHT entered for the harmonic idiom study and its hierarchical TREE annotations
>    (a distinct GT layer, lever R-7's footing) went unrecorded until a different question was asked at it a week
>    later. The registry's per-row needs-coverage note (audit step 2) is where the intake scoring lands.

**In plain words.** When a collection is acquired for one purpose, it is assessed against every need the project has, not just that one. Three things follow and all bind: a need already considered covered stays open to being covered better or more cheaply; a need not yet active gets its coverage recorded now, so that when its own sweep runs it starts non-empty; and every distinct layer of annotation the collection carries is inventoried, not only the layer that motivated acquiring it.

**Why.** The third consequence has a founding counter-example on the record: a jazz collection was acquired for a study of harmonic idiom, and its hierarchical tree annotations — a separate annotation layer, and the footing for a later analytical lever — went unrecorded until a different question was put to it a week later.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:255-264`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8c** — `## 8c. The FULL-NEEDS AUDIT — the union-of-needs mechanism (user question, 2026-07-03)` (heading at line 187). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Its class before the phase-1n staged application was `gap`.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL. The rule is recorded as the user's, 2026-07-03. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-368 — When new material bears on an already-settled conclusion, the rework question is settled by a recorded protocol — record, measure cheaply, then fork on whether it CONTRADICTS or merely enriches

> **The supersession decision protocol (user, 2026-07-03 — what happens when a find serves an already-passed
> need):** a "go back and rework now" vs "postpone" question is NEVER decided by enthusiasm or by default silence.
> The protocol, reusing the project's standing shapes:
> 1. **Record first:** the finding lands as an open item in the affected component's §15 (open items) + a STATUS
>    plan line — it cannot get lost regardless of the decision.
> 2. **Cheap impact measurement before any decision** (investigate-by-default): a read-only re-validation of the
>    component's signed conclusions against the new material. The question it answers: does the new bed
>    **contradict** a conclusion the design rests on, or merely **enrich/extend** the validation?
> 3. **The fork, by measured outcome:**
>    - **Contradiction (a premise-invalidation):** surfaced IMMEDIATELY as a tripwire event (the D5-test pattern) —
>      the user decides rework-now vs accept-with-recorded-caveat; downstream work that builds on the invalidated
>      conclusion is named in the surfacing (the compounding cost of waiting is part of the decision material).
>    - **Enrichment only:** DEFAULT = postpone to the component's next natural touch (the §15 item carries it);
>      pulling the rework forward is a user priority call, informed by the measurement.
> 4. **The decision is the user's in both branches** — the protocol fixes what is measured and what is recorded,
>    never the outcome. (This is the corpus-side analogue of the gate re-baseline discipline: evidence first,
>    deliberate ratification second, nothing reopened by silence.)

**In plain words.** If material turns up that bears on a question already considered closed, whether to go back and redo the work is never decided by enthusiasm or by saying nothing. The finding is recorded first, so it cannot be lost either way. Then a cheap read-only check asks one question: does the new material contradict a conclusion the design rests on, or does it only enrich the checking of it. A contradiction is surfaced at once as a tripwire, naming the later work that would compound, and the user decides between redoing it now and accepting it with the caveat recorded. Enrichment alone is postponed by default to the component's next natural touch. In both branches the decision is the user's; the protocol fixes only what gets measured and what gets written down.

**Why.** The protocol is assembled from shapes the project already uses, and the record says so: it is the corpus-side analogue of the discipline for re-baselining a regression gate — evidence first, deliberate ratification second, nothing reopened by silence — and the contradiction branch reuses the existing tripwire pattern.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:266-282`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8c** — `## 8c. The FULL-NEEDS AUDIT — the union-of-needs mechanism (user question, 2026-07-03)` (heading at line 187). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Its class before the phase-1n staged application was `gap`.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL. The protocol is recorded as the user's, 2026-07-03. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-369 — The DCML figured-bass repository is a REALIZATION SCRIPT, not reference data — walked and recorded so it is never mistaken for reference data again

> **DCMLab/figured-bass WALKED = a realization SCRIPT, N10-NEGATIVE** (never re-mistake it for GT).

**In plain words.** A repository long listed as a possible source of figured-bass reference data was opened and read: it contains code that realizes a figured bass, not annotations to grade against. It is recorded as a confirmed negative so the mistake is not repeated. The real figured-bass reference data is the Bach chorale figured-bass set, and a third source is a column already present in the corpora held, which the reader currently drops.

**Why.** Established by walking the repository, at the third corpus wave, 2026-07-04, provenance `cc_corpus_wave3_report.md`; the finding also promoted the row out of the residual-risk list into the enumerated containers. It is exclusion evidence in the sense principle #12 names: a ruled-out possibility recorded rather than dropped, because the exclusion is not recomputable from what is kept.

**Status.** LIVE · decided 2026-07-04 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:216`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8c** — `## 8c. The FULL-NEEDS AUDIT — the union-of-needs mechanism (user question, 2026-07-03)` (heading at line 187). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Its class before the phase-1n staged application was `gap`.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-370 — Reference data for implied polyphony does not exist and the negative is FINAL — the two candidate sets were never released

> **implied-polyphony half CONFIRMED ABSENT** (VoiSe/Gray-Bunescu never released; final).

**In plain words.** For music where a single line implies several voices, there is no published set of human annotations to grade against: the two datasets that would have provided it were never released. The negative is recorded as final, so the search is not repeated. The related but distinct case — music where the separate voices are actually written out — does have candidates, and three of them have been acquired.

**Why.** Established by the union search of 2026-07-04, recorded in `cowork_union_search_record.md` §1, which separates the two halves of the need and reports the outcome of each. Recorded rather than dropped under principle #12: a confirmed absence is information, and it bounds what the voice-leading axis's own target task can be validated against.

**Status.** LIVE · decided 2026-07-04 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:215`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8c** — `## 8c. The FULL-NEEDS AUDIT — the union-of-needs mechanism (user question, 2026-07-03)` (heading at line 187). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Its class before the phase-1n staged application was `gap`.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-371 — No dataset pairs an ornament sign with its written-out realization — confirmed absent, so the ornament expansion ships rule-based and unvalidated, as predicted

> **negative CONFIRMED** — no symbol→realization dataset exists; nearest = Batik-plays-Mozart (trill realizations recoverable by heuristic, unlabeled; ★ multi-need: also carries harmony+cadence GT on 12 Mozart sonatas); R-1 ships rule-based/unvalidated as predicted; build-paths recorded

**In plain words.** Nothing published pairs an ornament as notated with the notes a performer would actually play, so there is no way to grade an ornament expansion against human reference data. The nearest thing is a performance corpus from which trills could be recovered by rule, unlabelled. The consequence is accepted and was predicted in advance: the ornament expansion ships as rules, unvalidated, and the routes by which such a dataset could be built are recorded.

**Why.** Established by the union search of 2026-07-04, recorded in `cowork_union_search_record.md` §2. The record notes that the nearest source is multi-purpose — it also carries harmony and cadence reference data over twelve Mozart sonatas — which is the intake rule (**D-367**) working as written.

**Status.** LIVE · decided 2026-07-04 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:219`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8c** — `## 8c. The FULL-NEEDS AUDIT — the union-of-needs mechanism (user question, 2026-07-03)` (heading at line 187). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Its class before the phase-1n staged application was `gap`.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-372 — Marked part-writing errors must be BUILT, not downloaded — no public dataset exists and the two commercial holders keep theirs closed

> **no public dataset exists — CONFIRMED build-not-download** (Harmonia/Artusi hold it commercially closed). Validation seeds found: the Dahn manuscript-checked 46 consecutive-5th/8ve instances in the Bach chorales + Fitsioris-Conklin 18 (real-music positives, small transcription job) + the synthetic-violation route. Construction owned by VL-H's design gate

**In plain words.** There is no public collection of part-writing exercises with the mistakes marked, and the two teaching products that hold such material keep it closed. Building one is therefore the only route, and that construction belongs to the design step of the component that needs it. Seeds for validating it were found: a manuscript-checked list of consecutive fifths and octaves in the Bach chorales, a small second list of real-music instances, and the route of generating violations deliberately.

**Why.** Established by the union search of 2026-07-04, recorded in `cowork_union_search_record.md` §5, which names the two commercial holders and the three validation seeds. The need itself was adopted by the user on 2026-07-04 at the full-needs audit's disposition.

**Status.** LIVE · decided 2026-07-04 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:225`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8c** — `## 8c. The FULL-NEEDS AUDIT — the union-of-needs mechanism (user question, 2026-07-03)` (heading at line 187). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Its class before the phase-1n staged application was `gap`.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL. The user's act recorded on this row is the ADOPTION of the need (2026-07-04); the build-not-download conclusion is a measured search outcome and names no ratifier. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-373 — The only dual-annotator reference data actually on disk is the 27 TAVERN A/B pairs — the assumed second source was measured to have ZERO overlap

> the on-disk co-located dual set = **the 27 TAVERN A/B pairs** (Beethoven 17 + Mozart 10, verified at the WiR clone AND by Cowork glob). The audit's "Tymoczko-vs-DCML pairs" are NOT co-located: within WiR the two analyst sets sit on disjoint pieces (overlap **0**; DCML 988 / Tymoczko 419 analyses); CROSS-container pairs (WiR-Tymoczko × the separate `tools/dcml/` DCML corpora) remain possible but need identity work — recorded, not assumed.

**In plain words.** Calibrating how far human analysts disagree needs two independent analyses of the same music. Only one such set is actually held: twenty-seven pieces analysed twice. The other source that had been assumed to provide it does not: inside the meta-collection the two analysts' sets sit on entirely different pieces, with no overlap at all. Pairing across separate collections might still be possible, but that would need identity work first, and it is recorded as a possibility rather than assumed.

**Why.** Measured at the third corpus wave, 2026-07-04, and verified twice independently — at the checked-out copy and by a second glob. The correction matters because it bounds what the confidence-calibration work can be fitted on, and because principle #21 makes the accuracy of reference data itself a measured quantity rather than an assumption.

**Status.** LIVE · decided 2026-07-04 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:208`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8c** — `## 8c. The FULL-NEEDS AUDIT — the union-of-needs mechanism (user question, 2026-07-03)` (heading at line 187). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Its class before the phase-1n staged application was `gap`.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL. The cell marks it `(Wave-3 MEASURED, corrects the audit)`. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-374 — The flexible multi-reading chorale annotations are RECORD-ONLY — they overlap the regression repertoire, so any use over those pieces is a future user ruling

> ⚠ **RECORD-ONLY** (its 371 Bach chorales overlap the gate repertoire; any use over gate pieces is a future user ruling — census §4 dedupe)

**In plain words.** A second set of human analyses over Bach chorales was found, one that records several valid readings per moment rather than a single one. Most of its chorales are the same pieces the analysis is graded against, so using it over those pieces would be exactly the contamination the de-duplication rule forbids. It is recorded and pinned but not used, and putting it to work over those pieces is a decision reserved for the user.

**Why.** The restriction follows directly from the registered de-duplication rule (**D-361**): a work already in the corpus a change is graded against is excluded as reference data from every other container it appears in. The record also carries the walk's own caveat — the analyses ship as a package binary, with only the scores in plain notation.

**Status.** LIVE · decided 2026-07-04 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:208`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8c** — `## 8c. The FULL-NEEDS AUDIT — the union-of-needs mechanism (user question, 2026-07-03)` (heading at line 187). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Its class before the phase-1n staged application was `gap`.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL, in the Wave-3 addendum text of the dual-annotator row. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-487 — The eleven snapshot source scores are frozen and hash-pinned; changing the set or bumping a pin is a deliberate golden and gate re-baseline

> 2. **Do NOT add/remove the 11 snapshot sources** (in `tools/dcml/*/MS3/`, listed
>    above) or bump their clone pins without coordinating — they are the snapshot
>    baseline and are hash-pinned in `tools/snapshot_sources_manifest.json`. A pin
>    bump is a deliberate golden + BIR re-baseline.

**In plain words.** Eleven scores are the fixed input to the refactor-safety test. They are recorded by content hash and by the exact upstream version they came from. Adding, removing or updating one is not maintenance — it changes what the test compares against, and counts as deliberately re-setting the baseline.

**Why.** Stated with the rule and grounded in the mechanism beside it: the sources live in unpinned, gitignored clones, so the goldens are byte-meaningful only against the manifest's recorded commits — which makes a pin bump a change to the comparison, not to the material.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/score_inventory.md:344-347`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Hard rule 2 of the score inventory, the document `CLAUDE.md` directs every score-touching task to read first. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) It is the snapshot-corpus counterpart of **D-226** (the music21 export is version-pinned; regenerating it is a deliberate re-baseline) and of the block-(A) re-baseline discipline.

### D-488 — The two Bach chorale collections are independent selections, not sub- and superset — and the diff between them is not recoverable in-repo

> The 353 are music21's bach corpus filtered by `_is_bach_chorale` (has `bwv`, not a
> variant suffix, not a non-chorale BWV, exactly 4 SATB parts) — the `410 → 353`
> filter. (`corpus_registry.json` records an earlier "352 genuine SATB from 410"; the
> current filter yields 353. The +1 is not separately logged.) **These are NOT a
> subset of DCML `bach_chorales/MS3` (361):** they use music21 **BWV** identifiers
> (`bwv10.7`), DCML uses **Riemenschneider** numbers with no BWV in its
> `metadata.tsv`. A stem-level diff is **not recoverable in-repo** without an
> external BWV↔Riemenschneider concordance — the two are independent selections, not
> super/subset. Corpus-expansion / cross-validation is a Stage-5 decision; do not
> silently treat one as a superset of the other.

**In plain words.** The chorales the gate measures and the chorales the annotated corpus holds are two different selections of Bach's chorales, picked by different criteria and named by two incompatible numbering systems. Which pieces they share cannot be worked out from anything in the repository. Neither may be treated as containing the other.

**Why.** Established by reading the two selections' own identifiers rather than assumed: one keys pieces by BWV number, the other by Riemenschneider number with no BWV anywhere in its metadata, so a stem-level diff would need an external concordance the repository does not hold. The consequence is stated with it — corpus expansion and cross-validation across the two is a Stage-5 decision, not a silent identification.

**Status.** LIVE · decided 2026-06-11 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/score_inventory.md:180-189`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** The chorale-selection provenance finding of the score inventory (audit C3), restated as its hard rule 4; the document is the one `CLAUDE.md` directs every score-touching task to read first. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.)

### D-513 — A corpus registry's content summary is enumeration provenance, not evidence that an annotation layer is present — per-slice presence must be measured

> Lesson recorded: a registry `content` summary is enumeration provenance, not presence-of-layers evidence —
> per-slice presence must be measured (which is exactly what the wave's Task 5 was for). The census §8c
> N2/N5 state columns carry the corrections.

**In plain words.** A one-line description of what a corpus contains records where the corpus came from. It does not establish that a particular kind of annotation is actually in it. Whether a layer is present is a measurement, made file by file.

**Why.** The lesson is drawn from two of the audit's own claims being falsified by measurement in the same week — a supposed pair of overlapping annotation sets that do not co-occur at all, and a textbook corpus that turned out to hold scores and no analyses at the pinned commit. Both were sourced from a registry content field and treated as stronger than they were.

**Status.** LIVE · decided 2026-07-04 · ratifier not stated

**Home.** `cowork_census_full_needs_audit.md:256-258`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§7** — `## 7. POST-WAVE CORRECTIONS (Wave 3 measured, 2026-07-04 — two audit claims falsified, owned)` (heading at line 240). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** Recorded as the lesson of the audit's own post-wave corrections, which the document owns in its own §7 rather than quietly amending. It is #19 applied to corpus bookkeeping: a layer is trusted after being positively established, never because a summary mentions it. The surviving measured fact about on-disk dual annotation is **D-373**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-514 — A newly acquired annotation set whose works OVERLAP the regression corpus is RECORD-ONLY: it may not be wired to, compared against, or bulk-diffed with the gate corpus without a user ruling

>    spine. GPLv3. **⚠ RECORD-ONLY this dispatch:** its 371 Bach chorales overlap the gate repertoire (Breitkopf/Dörffel
>    371 Four-Part Chorales, KernScores lineage = the music21 gate corpus's works); it must NOT be wired to /
>    compared against / bulk-diffed with the gate corpus — any use over gate pieces is a future **user** ruling
>    (census §4 dedupe / the M3 contamination lesson). The 200 Praetorius chorales are new and outside the gate.

**In plain words.** One acquired collection of chorale analyses covers the same works the accuracy gate is measured on. It is recorded and left alone: it may not be connected to the analysis, compared against the gate corpus, or diffed against it in bulk. Using it over those pieces at all is a decision for the user. The part of it that covers other repertoire is outside the gate and unaffected.

**Why.** Grounded in the contamination lesson the corpus discipline already carries: a work that is in the regression corpus cannot also be a free-standing check on it, because the two uses are not independent. The document also records what the walk actually found — the analyses ship as a packaged binary and the score files carry no analysis spine — so the constraint is stated together with the reason the material is not usable as-is anyway.

**Status.** LIVE · decided 2026-07-04 · ratifier not stated

**Home.** `cowork_census_full_needs_audit.md:280-283`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§7.1** — `### 7.1 WAVE-3 ADDENDUM — the two DDMAL direct pickups (2026-07-04, `cc_wave3_addendum_report.md`)` (heading at line 260). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** Recorded at the Wave-3 addendum with the acquisition itself. It is the corpus-side companion of the de-duplication rule **D-361** (corpora are de-duplicated by WORK, not by container) and of the research-tier-on-entry rule at `CLAUDE.md` gate block (A). Bears directly on `OPEN_ITEMS.md` OI-179: it is a second annotation layer over gate-class chorales, and this is the ruling that says it may not be used as one without the user. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-515 — Pedal-point ground truth gets its OWN needs row rather than riding as a note on another — the user's reason: it can improve inference precision and nothing is lost

> 4. Pedal-point GT: N4-family note (default) or its own needs row? → **OWN ROW (N20)** — user: can improve
>    inference precision AND no information loss; also completes the §2.15 span-kind↔needs mapping.

**In plain words.** Every corpus in one large held collection carries a column marking pedal points. Rather than mentioning that in passing under a neighbouring need, it becomes a tracked need of its own.

**Why.** The user's own rationale is recorded with the ruling and has two parts: the material can improve inference precision, and giving it a row loses no information — the no-information-loss principle applied to the tracking surface itself. The document adds that it also completes the mapping between the span kinds the architecture names and the needs list.

**Status.** LIVE · decided 2026-07-04 · ratified by user

**Home.** `cowork_census_full_needs_audit.md:227-228`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§6** — `## 6. Wave-3 disposition surface (user disposes — nothing below is commissioned)` (heading at line 213). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** One of the four rulings the audit's banner records as taken on the day it was delivered. The material it tracks was verified at the source file in the same session. The pedal-point work it would serve is **D-103**/**D-207**/**D-385**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-516 — Two ground-truth classes with named consumers but no needs row were ADOPTED at the first full-needs audit — contrapuntal/imitative structure, and marked part-writing errors

> **C. Rulings sought from the user — ★ ALL RULED (2026-07-04, see status banner):**
> 1. Adopt **N18** (contrapuntal/imitative structure GT)? Candidates already enumerated. → **ADOPTED.**
> 2. Adopt **N19** (part-writing error/exercise GT)? Would join the union search. → **ADOPTED.**

**In plain words.** Scanning the list of things the project intends to build against the list of ground truth it tracks turned up two kinds of annotation that a named future tool needs and nothing was tracking: analyses of fugal and imitative structure, and graded exercises with their mistakes marked.

**Why.** The gap was found by the mechanism rather than by intuition — the audit's first step is a currency check that scans the consumer registers against the needs vector — and each proposal is recorded with whether the enumeration already holds a candidate: one does, one does not and therefore joins the search round.

**Status.** LIVE · decided 2026-07-04 · ratified by user

**Home.** `cowork_census_full_needs_audit.md:223-225`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§6** — `## 6. Wave-3 disposition surface (user disposes — nothing below is commissioned)` (heading at line 213). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** Two of the four rulings the audit's banner records. The part-writing half later produced its own measured verdict, **D-372** (marked part-writing errors must be BUILT, not downloaded — no public dataset exists). The intonation-scope ruling taken in the same act is **D-366**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-553 — A reference corpus's notation convention is DISCOVERED per entry by the comparison run, never declared as an input to it

> Earlier drafts had each catalog declare its stripping convention
> as test fixture setup ("this catalog uses degree=7,
> preserveAlterations=false"). Under the progressive comparison
> protocol, that's no longer needed — the convention is *discovered*
> empirically from the comparison run, per entry.

**In plain words.** When our analysis is compared against a published collection, the collection's habit of writing chords more plainly than we do is not declared in advance as a setting. The comparison tries each level of simplification per entry and reports which one matched — so the convention is a measured property of the run. A collection whose entries settle at different levels then shows up as mixed rather than being mis-scored.

**Why.** Stated with the rule and defended by the failure of the alternative: declaring one convention per collection forces a single parameter onto a collection that may not have one, and reports the entries that disagree with the declaration as real analytical differences. Discovering it per entry also makes drift within one collection visible.

**Status.** LIVE · decided 2026-04-25 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/extension_stripping_policy.md:121-125`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `docs/extension_stripping_policy.md`, the design memo `ARCHITECTURE.md`:1004 names for the test-only simplification utility; the document's own banner reads *"Direction settled."* and states no ratifier. Read in full by READ WAVE 4, 2026-08-04. **Distinct from D-304**, which is the production-side rule that the analyzer always emits its fullest reading: this is the measurement-side rule about how the comparison decides what the other side's convention IS. #19 bears on it — a comparison whose convention is asserted rather than measured is an unestablished measurement tool.

### D-612 — The corpus-search convention: a NEGATIVE is recorded so it is never re-searched, and every claim is RE-VERIFIED at acquisition rather than trusted from the search

> **[verified] tags are the agents' (primary page fetched)** — per the census convention, every claim is
> re-verified at acquisition. Negatives are recorded so they are never re-searched. This doc is the
> census-grade record; findings enter the census/registry only via a future acquisition dispatch.

**In plain words.** When a search for annotated music comes back empty, the emptiness is written down as a result, so nobody spends a second session looking for the same thing. And nothing a search reports is trusted as it stands: when the material is actually fetched, every claim about it — what it contains, how big it is, how it is licensed — is checked again at the material itself.

**Why.** Measured at the very next step, which is why the convention earns its place rather than being a preference: the acquisition round of the same day CORRECTED two licence claims the search had recorded — one collection graded CC-BY by its documentation site turned out to be CC-BY-NC-SA at its own licence file (and the non-commercial clause is what the shipped-value licence constraint turns on), and a second recorded as unstated turned out to be MIT. A search reads a page; an acquisition reads the object.

**Status.** LIVE · decided 2026-07-04 · ratifier not stated

**Home.** `cowork_union_search_record.md:16-18`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_union_search_record.md`, the census §8c step-3 union search round, DISPOSED by the user 2026-07-04. Read in full by READ WAVE 6, 2026-08-04. The convention is stated in the document's own status block as *the census convention*; the record names no ratifier for it. It is the search-side companion of **D-372**, whose build-not-download conclusion this same document supplied, and of **D-308** (a newly acquired corpus enters as research material) — those govern what happens to a find; this governs what a search result is worth before it is checked.

### D-613 — Ground truth for IMPLIED polyphony is confirmed ABSENT — and the voice labels that do exist come from engraved notation, which must be said at intake

> **Negatives (do not re-search):** implied-polyphony GT over monophonic instruments — CONFIRMED ABSENT
> (VoiSe 2005 and Gray & Bunescu's perceptual-stream pop corpus were never released; VISA excerpt sets not
> public; Chew&Wu/Guiomard-Kagan reused notated voices). Caveat to carry: piano_svsep/vocsep labels
> originate from engraved notation — for piano, engraving-voice ≈ the inference target (the SOTA field
> accepts this), but say so at intake.

**In plain words.** For music where several lines are implied by a single melodic instrument, no published collection of correct line assignments exists — every candidate was either never released or simply reuses the voices the engraver wrote. Where voice labels do exist, they come from the engraving rather than from a listener's judgment, which is close enough for keyboard music but is a property of the labels that has to be stated when the material is taken in.

**Why.** Established by a targeted search reported per candidate, with the reason each fails named rather than summarised — two corpora never released, one excerpt set not public, and three that reuse notated voices instead of annotating heard lines. The caveat half is a statement about what the surviving labels MEASURE, which is the same distinction principle #21 makes about ground truth generally.

**Status.** LIVE · decided 2026-07-04 · ratifier not stated

**Home.** `cowork_union_search_record.md:32-36`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§1** — `## 1. N9 — stream / voice-separation GT: the GAP is now materially smaller` (heading at line 20). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** `cowork_union_search_record.md` §1, the union search round, DISPOSED by the user 2026-07-04. Read in full by READ WAVE 6, 2026-08-04. The user's disposition of this section approves the three acquisitions and records that implied polyphony *stays a recorded gap*; the negative itself names no ratifier. A fact-of-absence of the same shape as **D-474** (no published per-axis annotator agreement for this repertoire), and recorded under the same discipline: the absence is the finding, not a reason to keep looking.


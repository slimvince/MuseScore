# The 16 decisions pending ratification (D-300…D-315) — complete entries

> **GENERATED REVIEW AID (Cowork, 2026-08-02).** Found by phase 1f (the STATUS archive completed
> in full + two design documents). Entered with status from the record only — RATIFICATION IS
> YOURS. Notable: three do-not-retry prohibitions absent from the scoring model's own dead-end
> section (D-300/301/302), and D-310 — the measured jazz bass-injection evidence behind the
> OI-7 jazz-validation gate.


## Group G — Layer 4 — chord identity

### D-300 — Gate M (minor read as diminished) is DEFERRED and must not be retried without a new runtime signal

> **Gate M (Minor→Diminished TYPE-A): DEFERRED — do not retry.** See Iter 37 entry above.
> Requires DCML harmonic context not available at runtime.

**In plain words.** A proposed correction rule that would have re-read a minor chord as a diminished one on the same root is abandoned. It is not to be attempted again unless some new evidence becomes available while the music is being analysed.

**Why.** Measured: 8 genuine cases against 25 false positives, and the record states that no field or combination of fields available at analysis time separates the two — the eight genuine cases split into two groups, each sharing an identical structural profile with a large false-positive cluster, and the leading-tone hypothesis was tested and falsified on all eight (`STATUS_ARCHIVE.md:1090-1106`).

**Status.** DEFERRED · decided 2026-05-09 · ratifier not stated

**Home.** `STATUS_ARCHIVE.md:1136`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `STATUS_ARCHIVE.md` (the Iter-37 carried-forward block and its fenced deferral record at `:1090-1106`). `docs/scoring_model.md` §8, the standing home for scoring dead ends, does not mention Gate M — checked, not assumed. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue.

### D-301 — Gate N (major read as an inverted minor) is DEFERRED and must not be retried without a multi-region model

> **Gate N (Major→Minor TYPE-A): DEFERRED — do not retry.** See Iter 39 entry above.
> FP:genuine = 45:1 (270:6 at threshold=0.30). Same limitation as Gate M.
> The 6 genuine cases (vi/3 in major key) remain as unresolvable BIR=true errors.

**In plain words.** A proposed correction rule that would have re-read a root-position major chord as the first inversion of a minor chord is abandoned. Six real cases were found against roughly two hundred and seventy wrong firings, so it is not to be attempted again without a model that reads several chords together.

**Why.** Measured and diagnosed: the pattern is architecturally endemic — the submediant in first inversion always scores close to the tonic in any major key, so it recurs across more than 125 corpus pieces, and neither a diatonic-root check, a key-mode guard nor a tighter margin reduces the false-positive count (`STATUS_ARCHIVE.md:1110-1131`).

**Status.** DEFERRED · decided 2026-05-09 · ratifier not stated

**Home.** `STATUS_ARCHIVE.md:1138`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `STATUS_ARCHIVE.md` (the Iter-39 carried-forward block and its fenced deferral record at `:1110-1131`). Absent from `docs/scoring_model.md` §8 — checked. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue.

### D-302 — No further local scoring fix for inversions may be attempted — the remaining divergence is not an analyzer defect

> **Current baseline is the correct production baseline. Do not attempt
> further local scoring fixes for inversions.**

**In plain words.** Trying to correct which note of a chord is treated as its root by adjusting the numbers a single sonority earns in isolation is closed as a line of work. What remains is a genuine difference between reading a sonority on its own and reading it by its role in the music.

**Why.** Six weeks of investigation across four corpora and six fix attempts, with five stated conclusions: 95.8 % of the genuine cases are bare three-note triads for which bass-as-root is the statistically correct default; the four-note cases already score correctly; the added-sixth against seventh-chord ambiguity is a data impossibility; no spelling-bonus window exists (a bonus large enough to correct the triads breaks every sixth-chord convention — 20 catalog regressions against 0 corpus improvements); and the remainder is legitimate divergence between vertical sonority analysis and functional annotation (`STATUS_ARCHIVE.md:2731-2769`).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `STATUS_ARCHIVE.md:2768`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `STATUS_ARCHIVE.md` as the closing statement of the “Inversion Fix — Final Conclusion” block. Absent from `docs/scoring_model.md` §8. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue.

### D-303 — Non-chord-tone detection is deferred, and if built it must be chord identification that knows about non-chord tones, never stripping after the fact

> NCT detection deferred until LLM-triage corpus data exists; if pursued, must be Shape A (NCT-aware chord ID) not Shape B (post-analysis stripping)

**In plain words.** Deciding which sounding notes do not belong to the chord is postponed. When it is built, the knowledge must enter the chord decision itself; removing notes from an answer after the chord has been named is ruled out.

**Why.** derivation not recorded

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `STATUS_ARCHIVE.md:963`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `STATUS_ARCHIVE.md`'s “architectural memos retained as guardrails” list. It is load-bearing now: the non-chord-tone filter is the named lever at [[OI-55]] and [[OI-68]], and `docs/nct_detection_design.md` exists on disk. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue.


## Group J — Presentation and output conventions

### D-304 — The analyzer always emits its fullest reading; simplifying it happens only when comparing against a corpus, never in the product

> Extension-stripping policy implemented as test-only utility (`stripSymbol`, `classifyComparison`); never in production. Per principle in memory `project_no_stripping_in_production.md` — analyzers always emit maximal output, stripping happens only at corpus-comparison boundaries. Design memo: `docs/extension_stripping_policy.md`.

**In plain words.** When our analysis names a chord it states everything it found, including the added notes above the basic triad. Cutting that back to a plainer name is something only the comparison machinery may do, so that a difference of notation is not counted as a difference of analysis.

**Why.** The stated principle is that the analyzer reports what it found; the record shows the measured consequence — applying the comparison-side simplification reduced the pinned baseline from 135 differences to 10 (`STATUS_ARCHIVE.md:944`), which is the size of the notation-convention difference the rule keeps out of the analysis.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `STATUS_ARCHIVE.md:943`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `STATUS_ARCHIVE.md`; the design memo it names, `docs/extension_stripping_policy.md`, exists on disk. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue.


## Group G — Layer 4 — chord identity

### D-305 — The ban on reading written harmony as analyzer input is decided by what an annotation says, not by how it is stored

> Generalized chord-symbol-ban (content-based, not storage-type-based — covers Romans, function/cadence/key annotations; structural metadata like key sig still allowed)

**In plain words.** Our analysis must not read any harmonic annotation already in the score — not a chord symbol, not a Roman numeral, not a function, cadence or key label — whatever kind of score object holds it. Ordinary notational metadata such as the key signature is still allowed.

**Why.** derivation not recorded

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `STATUS_ARCHIVE.md:961`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `STATUS_ARCHIVE.md`'s “architectural memos retained as guardrails” list. It sharpens **D-066** (chord symbols written in the score are never analyzer input) from one annotation kind to a content test over all of them. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue.


## Group F — Layer 3 — key and mode

### D-306 — The key layer's backward re-reading stays switched off in the shipped configuration

> ★ USER DECIDED (2026-07-02): KEEP OFF.** `ReachBackOptions.enabled=false` stays the shipped default; activation re-opens only on the evidence follow-up

**In plain words.** The key analysis has a facility for going back and re-reading an earlier stretch once later evidence arrives. It is built but switched off, and turning it on is reopened only when a specific piece of evidence has been gathered.

**Why.** Measured and judged insufficient: an A/B run showed the designed effect is material (roughly 35–45 % of interior range queries change, almost all of them anchoring the leading key) but the timing comparison was confounded (one arm cold, the other warm), so the evidence needed to justify switching it on — interleaved timing plus an adjudicated sample of the changed outputs — was named and not yet gathered (`STATUS_ARCHIVE.md:232`).

**Status.** LIVE · decided 2026-07-02 · ratified by the user

**Home.** `STATUS_ARCHIVE.md:232`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `STATUS_ARCHIVE.md` (session 21j). The Layer-3 specification records the reach-back facility but not this shipped-default ruling. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue.


## Group K — Documentation governance

### D-307 — A specification cites code by function or section anchor, never by raw line number

> **(#9 stale line-number citations)** RULED with a POLICY: specs cite by **function/§ anchor, not raw line number** (numbers rot)

**In plain words.** When a design document points at the code, it names the function or the section, not the line. Line numbers go stale as soon as the file above them changes.

**Why.** The defect it answers is measured in the record: the gap analysis found stale line-number citations across the layer specifications, and the rule was made a policy at the same ruling that fixed them (`STATUS_ARCHIVE.md:242`).

**Status.** LIVE · decided 2026-07-02 · ratified by Cowork

**Home.** `STATUS_ARCHIVE.md:242`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `STATUS_ARCHIVE.md` (session 21e, the gap-analysis rulings). It is NOT in `cowork_design_doc_template.md`, which is the ratified home of the writing standards and states the implementation/test locator rule without this constraint on the locator's form — checked at the source. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue.


## Group Q — Scope and the development toolchain

### D-308 — A newly acquired corpus enters as research material; the frozen regression corpus stays the gate until a deliberate re-baseline

> new corpora enter as research-tier, the frozen Bach gate stays the regression gate until a deliberate re-baseline

**In plain words.** Music brought into the project for study does not become part of the pass/fail check by arriving. The frozen set the regression check runs on changes only by a separate, deliberate act.

**Why.** derivation not recorded

**Status.** LIVE · decided 2026-07-02 · ratified by the user

**Home.** `STATUS_ARCHIVE.md:250`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `STATUS_ARCHIVE.md` (session 21, at the user's ratification of the external architecture review's corpus-expansion amendment). Related but distinct from **D-225** (a corpus is regenerated before its baseline figures are updated) and from the re-baseline discipline in `CLAUDE.md` gate block (A). Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue.

### D-309 — A corpus the analysis handles badly stays on the roadmap marked deferred; it is more valuable than one that confirms what already works

> **Corpora that produce poor results under current vertical analysis
> are kept on the roadmap and labeled "Deferred".** They become
> validation targets as the analyzer gains new capabilities (melodic
> accumulation, arpeggio inference, jazz mode). A corpus that exposes
> a gap in our analysis is more valuable than one that confirms what
> we already do well.

**In plain words.** Music our analysis currently does poorly on is not dropped from the plan. It is marked as waiting, and becomes the test of the next capability we build.

**Why.** The reason is stated with the rule: a corpus that exposes a gap is worth more than one that confirms an existing strength, so a poor result is treated as information about what to build rather than as a reason to discard the material.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `STATUS_ARCHIVE.md:2938`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `STATUS_ARCHIVE.md` as the stated design principle of the validation-corpus roadmap. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue.

### D-310 — Jazz accuracy is not measurable on the corpora held: the low agreement is missing bass and piano voicings, not a scoring failure

> The lower agreement rates on available jazz corpora are therefore corpus artifacts —
> missing bass and piano voicings — not scoring failures. No accepted jazz-specific
> scoring changes remain in the analyzer, and no new jazz scoring work is planned on the
> current corpora.

**In plain words.** The jazz scores we hold are melody-and-chord-symbol transcriptions with the bass and the piano chords left out, so our analysis has too few notes to work from. The poor agreement measures the material, not the analysis, and no jazz-specific scoring work is planned until scores with the missing parts written out are available.

**Why.** Measured: a bass-injection experiment that supplied the missing root before analysis raised one jazz corpus from 39.8 % to 98.3 % and another from 18.0 % to 99.9 % agreement, which is what identifies the shortfall as missing material rather than mis-scoring (`STATUS_ARCHIVE.md:1575-1583`).

**Status.** LIVE · decided 2026-04-08 · ratifier not stated

**Home.** `STATUS_ARCHIVE.md:1580`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `STATUS_ARCHIVE.md` (the jazz-corpus status block). It is the standing evidence behind [[OI-7]] (establish a jazz ground-truth corpus or de-scope the Jazz correctness claims) and behind the A-7 empirically-unvalidated mark. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue.


## Group I — Module boundaries and code structure

### D-311 — The chord-analyzer file split happens once, after the retirements have settled — not before

> **the `chordanalyzer.cpp` file split (refactor #1) stays parked BY the ratified engage map** (R9 sequences it AFTER the E4 removals — "split once"; pulling it now would violate, not honor, the ratified order)

**In plain words.** Breaking the large chord-analysis source file into smaller ones waits until the code that is going to be deleted has been deleted. Splitting first would mean splitting twice.

**Why.** The reason is stated with the rule — “split once”: the retirement map already sequences the split after the removals, so performing it earlier would produce a structure the removals then invalidate.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `STATUS_ARCHIVE.md:166`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `STATUS_ARCHIVE.md` (session 22i, the Stage-5 planning checkpoint) as a ruling read off the ratified retirement map. It is load-bearing now beyond its original subject: [[OI-205]] half (b) cites it as “the ratified Stage-3.5 file-split lesson (restructure ONCE, after the boundaries stabilize)” to time the `ARCHITECTURE.md` restructure. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue.


## Group G — Layer 4 — chord identity

### D-312 — The carried alternative readings are inside the byte-identity acceptance contract — same winner with different alternatives is a behavior change

> RULED:
> `alternatives[]` IS inside the byte-identity acceptance contract** — the carried alternatives are a
> load-bearing output surface (the L4 §15 O1b carry contract: L5 overrides select among carried
> readings; E-14 makes them user-visible), so "same winner, different alternatives" is a behavior
> change.

**In plain words.** When a change is claimed to leave the analysis untouched, the claim covers the ranked runner-up readings as well as the chosen one. A change that keeps the same answer but alters the alternatives beneath it is a change in behaviour and must be ratified as one.

**Why.** Grounded in two recorded facts: the function layer selects among the carried readings rather than re-deriving them, so they are an input to a later decision; and they are shown to the user, so altering them alters the product. The founding case measured it — a retirement that was winner-identical on all 352 scores altered the alternatives on 36 of them (`cowork_stage5_fitter_design.md:1299-1308`).

**Status.** LIVE · decided 2026-07-05 · ratified by the user

**Home.** `cowork_stage5_fitter_design.md:992`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_stage5_fitter_design.md` (SIGNED, user, 2026-07-04) at open item O-11, and again in `STATUS_ARCHIVE.md:186`. It is the origin of the full-output-surface half of principle #15 (**D-178**): the same entry records the evidence-method lesson that inertness evidence must measure the winner AND the carry. Found by the phase-1f final-partition wave, 2026-08-02, reading `cowork_stage5_fitter_design.md` in full (SIGNED, user, 2026-07-04). NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue.


## Group C — Cross-cutting analysis contracts

### D-313 — A confidence map is monotone or it is not fitted — a non-monotone curve is an upstream finding, not a mapping target

> **D-8 Calibration maps are monotone or deferred.** A non-monotone empirical curve (L5 combinedBoundary) is
> an upstream finding, not a mapping target — fitting a non-monotone map would launder an inference defect
> into the confidence semantics. (Contract R4/R5 monotonicity carries this.)

**In plain words.** Turning a layer's internal confidence number into a statement about how often it is right is only done when a higher number really does mean more often right. Where the measured curve goes the wrong way in places, that is reported as a fault in the layer, not smoothed over by the map.

**Why.** Stated with the rule: fitting a non-monotone map would launder an inference defect into the confidence semantics — the map would make a mis-ordered confidence read as a well-ordered probability. The confidence contract's monotonicity rules carry the same requirement.

**Status.** LIVE · decided 2026-07-04 · ratified by the user

**Home.** `cowork_stage5_fitter_design.md:673`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_stage5_fitter_design.md` (SIGNED, user, 2026-07-04) as the eighth of its numbered architecture decisions, and applied in the same document at §4.5: the one measured non-monotone row was deferred and declared rather than mapped. Found by the phase-1f final-partition wave, 2026-08-02, reading `cowork_stage5_fitter_design.md` in full (SIGNED, user, 2026-07-04). NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue.


## Group T — Standing process rules and local patches

### D-314 — A correction rule kept for structural reasons must keep producing evidence that it still fires

> **O-10 (lesson from the user's methodology challenge, 2026-07-05): RETAINED structural rules carry
> ongoing LIVENESS evidence.**

**In plain words.** When a rule is kept because it encodes something structural rather than because a fitted number could replace it, its firing counts are re-measured at every adoption event. A kept rule that has quietly stopped firing then shows up at the next checkpoint instead of being discovered much later.

**Why.** The failure it answers is on the record: two rules' founding cases were silently absorbed upstream, leaving the rules dead and undetected for weeks, because nothing measured rule liveness (`cowork_stage5_fitter_design.md:1471-1478`).

**Status.** LIVE · decided 2026-07-05 · ratified by the user

**Home.** `cowork_stage5_fitter_design.md:1471`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_stage5_fitter_design.md` (SIGNED, user, 2026-07-04) at open item O-10, and tracked as a standing obligation at [[OI-36]] — which is an open-items row, not a home. Found by the phase-1f final-partition wave, 2026-08-02, reading `cowork_stage5_fitter_design.md` in full (SIGNED, user, 2026-07-04). NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue.


## Group L — Licensing, contribution, and coding standards

### D-315 — A one-line fix was made to MuseScore's own chord-symbol parser and is live in the fork

> One-line fix in MuseScore core `src/engraving/dom/chordlist.cpp:993` — removed `tok1 = u"sus"` from the susPending re-attachment block in `ParsedChord::parse()`. This was a genuine MuseScore core bug causing double-sus render for all sus+alteration chord suffixes. Should be reported upstream.

**In plain words.** One line was deleted from MuseScore's own chord-symbol parser because it made every suspended chord with an alteration render its suffix twice. The change is in this fork and has not been sent upstream.

**Why.** Diagnosed at the source: the lowercase parsing path was already correct, and the parallel assignment beside it was the cause of the doubled suffix — stated in the commit message of `b1ba746` and in the drafted upstream report `docs/chordlist_bug_report.md`.

**Status.** LIVE · decided 2026-04-15 · ratifier not stated

**Home.** `STATUS_ARCHIVE.md:2251`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `STATUS_ARCHIVE.md`. VERIFIED AT THE OBJECTS 2026-08-02: commit `b1ba746` deletes exactly that one line from `src/engraving/dom/chordlist.cpp`, only an upstream header-update commit has touched the file since, and the line is absent at HEAD. This is a THIRD edit to MuseScore's own code beside **D-198** and **D-199**, and it is not in `CLAUDE.md`'s “Local patches — do not revert” section, which carries exactly two subsections; the non-conformance against the ruled **D-229** is rowed at [[OI-273]]. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue.


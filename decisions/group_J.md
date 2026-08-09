# Decisions group J — Presentation and output conventions

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-086 — Roman numerals and Nashville numbers are presentation choices, not separate analyses

> Roman numerals and Nashville numbers are **presentation choices**, not
>   separate analyses — they are alternative formatters on the same `ChordAnalysisResult`.

**In plain words.** Showing the harmony as Roman numerals or as Nashville numbers is a choice of how to display one and the same analysis.

**Why.** Stated constraint, ARCHITECTURE.md:5854-5856: Roman numerals and Nashville numbers encode identical information, so showing both on one staff would be redundant and would destroy legibility - which makes the choice a display preference, not two analyses.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4034-4035`

**Provenance.** ARCHITECTURE.md:3253-3257; consistent with D-016

### D-087 — Display options live with the formatter, not with the analyzer preferences

> Display options (`Options`) live in `ChordSymbolFormatter`, not in
> `ChordAnalyzerPreferences`, enforcing the analysis/display separation (principle 2.3).

**In plain words.** Which spelling convention to use on screen is a formatter setting, kept away from the settings that affect the analysis itself.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3735-3736`

**Provenance.** ARCHITECTURE.md:2918-2958

### D-088 — No automatic key signature injection

> No automatic key signature
> injection is planned.

**In plain words.** The program will never add a key signature to your score by itself. It shows what it inferred in the chord staff and leaves the decision to you.

**Why.** Stated constraint, ARCHITECTURE.md:527-532 (§2.9): writing a key signature into the score would be the system modifying the music without the user asking.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4700-4701`

**Provenance.** ARCHITECTURE.md:3850-3858; an instance of D-074

### D-089 — The legacy confidence exposure gates - 0.5 tentative, 0.8 assertive

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - Above 0.8 — display without qualifier
> - 0.5–0.8 — append "?" to key/mode label
> - Below 0.5 — suppress key-dependent chord-track annotations rather than exposing a low-confidence key

**In plain words.** On the old path, a key the program is unsure of is shown with a question mark, and one it is very unsure of is not shown at all rather than shown wrongly.

**Why.** derivation not recorded.

**Status.** SUPERSEDED BY D-018 · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4385-4387`

**Provenance.** The record arm replaces the 0.5/0.8 literals with the fitted nats constants (ARCHITECTURE.md:175-177); the literals are legacy-arm-only (sectionanalyzer.cpp::legacyKeyExposureBucket)

### D-090 — Abstention is a valid outcome - high precision before coverage

> - high precision on exposed results
> - calibrated abstention when evidence is weak

**In plain words.** The aim is not to put a label on everything. It is to be right about what we do label, and to say nothing when the evidence is thin.

**Why.** Stated constraint, ARCHITECTURE.md:3556-3564 and its consumer rules at :5604-5612: the stated product target is not 'always emit a label' but high precision on exposed results, calibrated abstention when evidence is weak, and coverage gains only after precision is acceptable - so below the confidence bar the key-dependent annotations are suppressed rather than printed tentatively.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4405-4406`

**Provenance.** ARCHITECTURE.md:3549-3601

### D-106 — The augmented-sixth labels are gated to the Standard and Baroque presets

> **Preset gating is NOT implemented — corrected 2026-08-02 (`OPEN_ITEMS.md` OI-112(c); this section
> asserted "Gated to Standard and Baroque presets only", and the code defers exactly that).**

**In plain words.** The specific Italian, French and German augmented-sixth labels are shown only under the classical presets.

**Why.** derivation not recorded.

**Status.** SUPERSEDED IN FACT · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4716-4717`

**Provenance.** open_items/OI-112 already records this preset-gating as stale; open_items/OI-201 records that the record arm collapses the family to a plain major triad symbol ★ Verbatim RE-TAKEN 2026-08-02 (the phase-1 truth-sync): §5.11's assertion 'Gated to Standard and Baroque presets only' was corrected, since the formatter explicitly defers that gate for want of preset context (`chordsymbolformatter.cpp:882-883`) and emits the labels under every preset (OPEN_ITEMS OI-112(c) discharged). The decision's own words survive at the home, quoted inside the correction.

### D-234 — A chord symbol string must be valid under chords_std.xml; chords.xml is not relied on

> **Rule 16 — Do not rely on chords.xml**
>
> MuseScore has two chord description files:
> - `share/chords/chords_std.xml` — the active standard chord list used by default in all scores
> - `share/chords/chords.xml` — legacy file, likely deprecated, contains known bugs and inconsistencies with the parser
>
> When our formatter produces a chord symbol string, it must be valid according to `chords_std.xml` only. Do not add chord symbol strings that exist only in `chords.xml` — they will fail to parse correctly under the Standard chord style and may produce corrupted output.

**In plain words.** MuseScore ships two chord description files. Everything our formatter emits must parse under the active one, chords_std.xml. A string that exists only in the legacy chords.xml is not used.

**Why.** The measurement that decided it is cited in the record: `9sus` exists in chords.xml (id=134) and not in chords_std.xml, and under the Standard chord style it triggers `generateDescription()`, producing the corrupted `Fsussus9` render (ARCHITECTURE.md:672). The remedy named there is `sus(add9)`.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:883-889`

**Provenance.** ARCHITECTURE.md:664-674 (Rule 16), restated in the retired-session record at STATUS_ARCHIVE.md:2247 ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-295 — Zero information loss to the end user - every inferred object must be displayable

> **The governing requirement over everything in this section: ZERO INFORMATION LOSS TO THE END USER — every
> inferred object must be displayable.** Anything the analysis works out has to be capable of being shown.
> Revealing it gradually, so that a display is not overwhelming, is the intended design; leaving something the

**In plain words.** Anything the analysis works out must be capable of being shown to the user. Showing it gradually, so the display is not overwhelming, is fine; leaving something permanently unreachable because the interface has no place for it is not.

**Why.** A user-stated principle. It is the display-side counterpart of the no-information-loss principle (D-099, principle #12), which governs what the analysis may discard internally; this governs what the interface may withhold.

**Status.** LIVE · date not stated · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:7313-7315`

**Provenance.** Recorded in `cowork_handoff_archive.md` (the standing-records block) as item E-14 of `cowork_product_tool_register.md`, with a note that a pointer into the architecture document was owed at its next edit. This pass found no such pointer in the register's own home census, so the owed act appears undischarged. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue). ★ HOMED 2026-08-02 (CC, phase 1j, executing the user's per-kind ruling on [[OI-272]]): written at the head of `ARCHITECTURE.md` §12 as the governing requirement over the user interface. This also discharges the pointer-into-the-architecture-document act the archive recorded as owed at its next edit. Former home preserved (#12): `cowork_handoff_archive.md:2507`, the standing-records block, as item E-14 of `cowork_product_tool_register.md`.

### D-304 — The analyzer always emits its fullest reading; simplifying it happens only when comparing against a corpus, never in the product

> - **The analysis always emits its FULLEST reading; simplifying a reading is a comparison-side act and
>   never a product one.** When a layer names a chord it states everything it found, the added notes above
>   the basic triad included. Cutting a name back to a plainer one — dropping an extension so that two

**In plain words.** When our analysis names a chord it states everything it found, including the added notes above the basic triad. Cutting that back to a plainer name is something only the comparison machinery may do, so that a difference of notation is not counted as a difference of analysis.

**Why.** The stated principle is that the analyzer reports what it found; the record shows the measured consequence — applying the comparison-side simplification reduced the pinned baseline from 135 differences to 10 (`STATUS_ARCHIVE.md:944`), which is the size of the notation-convention difference the rule keeps out of the analysis.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:1177-1179`

**Provenance.** Recorded in `STATUS_ARCHIVE.md`; the design memo it names, `docs/extension_stripping_policy.md`, exists on disk. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue). ★ HOMED 2026-08-02 (CC, phase 1j, executing the user's per-kind ruling on [[OI-272]]): written into `ARCHITECTURE.md` §2.15 as a cross-cutting analysis contract, which is that section's declared scope. Former home preserved (#12): `STATUS_ARCHIVE.md:943`.

### D-471 — The sub-beat annotation duration gate is not retired on argument — it is kept or dropped on a measured observation run, with the verdict stated in advance

> **The sub-beat annotation duration gate is KEPT OR DROPPED ON A MEASURED OBSERVATION RUN, and the
> verdict is fixed in advance.** A gate hides very short chords from the Roman-numeral annotation
> while the chord track and the status bar still show them. Whether it survives is **not** settled by
> argument; the decision rule is written down before the measurement and is binding:
>
> - if the gate **measurably reduces clutter or false annotations without suppressing correct ones**
>   → it is KEPT, as a documented emitter option with its current default, settable;
> - if it **suppresses equally many correct and incorrect annotations** → it is RETIRED, the duration
>   parameter's default becomes *no gate*, and the option is removed in the follow-up cleanup.
>
> *Why:* stated with the rule — the question is whether the gate removes clutter or removes correct
> labels, which is a measurement and not a preference; and fixing the verdict **before** the
> measurement is what stops a live result from being argued into whichever reading suits it. It is
> the pre-declared-protocol discipline (#22) applied to a display gate, and it is the pattern the
> premise gate (#17b) later made general. **The gate is undischarged at HEAD:** the observation run
> has not been made, so neither branch has fired.

**In plain words.** A rule hides very short chords from the Roman-numeral annotation. Whether to keep it was not settled by opinion: the decision was written down in advance as a comparison — run the annotation with and without it on real scores, and keep it only if it removes clutter without also removing correct labels.

**Why.** Stated with the rule: the gate silently drops sub-beat regions from Roman-numeral annotation while the chord track and the status bar still show them, so the question is whether it removes clutter or removes correct labels — which is a measurement, not a preference. The rule fixes the verdict before the measurement, which is the pattern the premise gate (#17b) later made general.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:7207-7222`

**Provenance.** Stated as the divergence-C decision rule of the unification design; the document's own header records divergence C as PARKED, so the rule stands undischarged. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The recorded owner question was that what is recorded is a measurement protocol rather than a rule. The user ruled that a GATE'S PRE-DECLARED KEEP-OR-DROP PROTOCOL is exactly what principle #22 gives a kind to — a hard gate carries a pre-declared protocol for the change it will face — so the protocol belongs at the section that owns the gate. Written into §11.5 in that section's own voice, with both branches of the pre-declared verdict, its defense, and the statement that the observation run has not been made so neither branch has fired. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `docs/unified_analysis_pipeline.md:225-233`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 215, "section": "### Divergence C (duration gate)", "label": "“Divergence C”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "Decision rule:

- If the gate measurably reduces clutter or false annotations without
  suppressing correct ones → keep as documented emitter option (default
  0.5, settable).
- If the gate suppresses equally many correct and incorrect annotations
  → retire, either immediately in Phase 3b or folded into Phase 5.
  `minimumDisplayDurationBeats` becomes `std::nullopt` default and the
  option is removed in follow-up cleanup." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-498 — RATIFIED AMENDMENT A-9: a product stance is owed for output that is mostly uncertain, and for music outside the tonal vocabulary altogether

> - **A-9 (from F-13, F-15). Write the product stance for dense abstention and out-of-domain input** (what the user
>   sees; when the system says "this is outside my tonal vocabulary"). Product-level, small, prevents the honest-marks
>   design from becoming a UX failure.

**In plain words.** The design deliberately says 'uncertain' rather than guessing. Nobody has decided what the user should see when most of a passage comes back uncertain, or what the program should say about music that is not tonal at all — where the right answer is to state that plainly rather than to produce a confident reading. The amendment requires that stance to be written.

**Why.** Derived from the review's stress simulation, which produced both halves concretely: in suspension-chain textures the anchor a reading depends on is itself uncertain, so the honest marks cascade and the output can be dominated by them; and on music that breaks the tonal model class the confidence collapses correctly but nothing INTERPRETS the collapse. The review's own framing is that this is what prevents an honest design from becoming a usability failure.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_architecture_review_2026_07.md:333-335`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§9** — `## 9. Proposed amendments (ranked; each ratification-gated; none is code)` (heading at line 307). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** Amendment A-9 of the external architecture review, in a document whose banner records amendments A-1…A-10 as RATIFIED by the user on 2026-07-02. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) ★ NOT A FRESH DECISION, stated so that nothing is counted twice (dispatch cc_instruction_reads_3.md §1.3): the amendment itself was ratified by the user at the 2026-07-02 architecture review, which is what this entry's Status line already records. Ratifying the ENTRY records only that the register transcribes that ratification correctly — it neither re-makes the decision nor adds a second ratification event to it. No register entry and no located product answers it; the review records the underlying findings as F-13 (no display policy for dense abstention) and F-15 (no explicit out-of-domain stance).

### D-584 — The perfect/imperfect cadence call is made on the BASS-DERIVED inversion; the soprano arrival degree is demoted to a soft optional nudge and the tool never attempts melody identification

> - **The perfect/imperfect cadence call is made on the BASS-DERIVED INVERSION; the soprano arrival
>   degree is a soft optional nudge and this layer never attempts melody identification (D-584).**
>   Standard theory decides a full close from the melody note, and this layer may not: the highest
>   sounding voice is often a doubling, and in some textures the lead sits below the top, so the
>   structural melody the criterion needs is not reliably recoverable. The top voice may nudge the
>   confidence in a chordal texture; it never decides. *Why:* the constraint that forces it is the
>   unavailability of the structural melody — orchestral doubling and a lead below the top are the two
>   cited counter-cases — and the bass-derived inversion criterion is chosen because the catalog

**In plain words.** Whether a cadence is a full close or a weaker one is decided from the bass and the chord's inversion, not from which note the melody lands on. Standard theory uses the melody note, but the program cannot reliably tell which line is the melody: the highest sounding voice is often a doubling, and in some music the lead sits below the top. The top voice may nudge the confidence in a chordal texture; it never decides.

**Why.** The constraint that forces it is named in the decision itself: the criterion needs the structural melody, and the highest sounding voice is not reliably that line — orchestral doubling and a lead below the top are the two cited counter-cases. The bass-derived inversion criterion is chosen because the catalog records the root-position flags as bass-derived and robust.

**Status.** LIVE · decided 2026-06-26 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:2023-2030`

**Provenance.** ★ RE-HOMED 2026-08-04 (CC, dispatch `cc_instruction_finish_line_item1.md`, Task 3.3, ruling R3): written into the OWNING LAYER SPECIFICATION in that section's own voice, with its defense. Register rule (e) prefers this route in terms, and D-231's purposive clause (criterion C4) is why it is preferred over a delegation: at completion the specifications must suffice to measure conformance against WITHOUT consulting the register, and a decision reachable only by following a pointer satisfies C1's letter and defeats C4. The classification that selected this entry, with its reason and the whole 94-entry population, is `tools/audit/decisions/finish_line_item1_routes.json`. Its former home class was `gap` — a decision governing a layer but not findable from that layer's section — which is precisely what the re-homing discharges; the field is cleared because a layer-specification home is not a non-specification home. **THE FORMER HOME, CLASS AND VERBATIM, PRESERVED (#12)** — former home `cowork_layer5_function_methods.md:75-79`; former verbatim: “- **★ The "soprano arrival degree" (1̂=PAC vs 3̂=IAC) is theory-standard but implementation-fragile, so DEMOTED in the
  spec (user, 2026-06-26).** It needs the *structural melody*, and the **highest sounding voice is not reliably that line**
  (orchestral doubling; barbershop lead *below* the top). So the spec makes the perfect/imperfect call on the
  **bass-derived inversion** criterion and uses the top-voice arrival only as a *soft, optional* confidence nudge in
  homophonic textures — never the hard test. The tool does not attempt melody identification.” — `cowork_layer5_function_methods.md`, the research-first methods catalog that grounds the Layer-5 specification (2026-06-26). Read in full by READ WAVE 5, 2026-08-04. The record marks the demotion *user, 2026-06-26* and points at the Layer-5 specification §5.2 / §15-0 for where it lands. Distinct from **D-336** (cadence detection is key-agnostic), which governs what the detector may READ; this governs how the perfect/imperfect call is MADE.

### D-585 — The bass-scale-degree / Rule-of-the-Octave prior is admitted as a SOFT prior and tie-breaker only, never a gate

> - **The bass-scale-degree / Rule-of-the-Octave prior is admitted as a SOFT prior and TIE-BREAKER
>   only, never a gate (D-585).** Which harmony a bass degree usually carries may break a tie between
>   otherwise equally good readings and may never rule a reading out. *Why:* two reasons, both
>   load-bearing — the mapping is theoretically authoritative (the partimento tradition and
>   functional-bass theory) but **largely unexplored as an explicit computational prior**, so it is not
>   established (#19); and it is structurally many-to-one and direction-dependent, with the surrounding

**In plain words.** Which harmony a bass note usually carries — the partimento Rule of the Octave — is allowed to break a tie between readings that are otherwise equally good, and nothing more. It may never rule a reading out, because one bass note maps to several harmonies, the mapping depends on which way the bass is moving, and the surrounding progression overrides it.

**Why.** Two reasons, both stated with the decision: the mapping is theoretically authoritative (the partimento tradition and functional-bass theory) but LARGELY UNEXPLORED as an explicit computational prior, so it is not established (#19); and it is structurally many-to-one and direction-dependent, which is what makes it a tie-breaker rather than a decision rule.

**Status.** LIVE · decided 2026-06-26 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:2032-2037`

**Provenance.** ★ RE-HOMED 2026-08-04 (CC, dispatch `cc_instruction_finish_line_item1.md`, Task 3.3, ruling R3): written into the OWNING LAYER SPECIFICATION in that section's own voice, with its defense. Register rule (e) prefers this route in terms, and D-231's purposive clause (criterion C4) is why it is preferred over a delegation: at completion the specifications must suffice to measure conformance against WITHOUT consulting the register, and a decision reachable only by following a pointer satisfies C1's letter and defeats C4. The classification that selected this entry, with its reason and the whole 94-entry population, is `tools/audit/decisions/finish_line_item1_routes.json`. Its former home class was `gap` — a decision governing a layer but not findable from that layer's section — which is precisely what the re-homing discharges; the field is cleared because a layer-specification home is not a non-specification home. **THE FORMER HOME, CLASS AND VERBATIM, PRESERVED (#12)** — former home `cowork_layer5_function_methods.md:126-131`; former verbatim: “The partimento Rule of the Octave maps each **bass** scale-degree to a first-choice harmony (1̂/5̂/8̂→stable 5/3;
4̂/7̂→6/5,6/3; 2̂→inverted dominant-seventh; descending 6̂→applied-dominant), and functional-bass theory biases bass
5̂/7̂→D, 4̂/2̂→S/predominant, 1̂/3̂→T. It is theoretically authoritative and **largely unexplored as an explicit
computational prior** — a defensible, **low-risk SOFT prior / tie-breaker** for L5's resolver (§5) and cadence test
(§3), **never a gate** (it is many-to-one, direction-dependent, overridden by sequence/cadence/applied context).” — `cowork_layer5_function_methods.md`, the research-first methods catalog that grounds the Layer-5 specification (2026-06-26). Read in full by READ WAVE 5, 2026-08-04. Recorded in the catalog's §6. The record states no ratifier for this item. It sits beside **D-383**, which ranks a licensed progression as a tie-break among already-plausible readings rather than a decider — the same posture for a different evidence channel.

### D-607 — Polyphonic phrase-boundary detection has NO validated deterministic rule set in the literature — the extension is engineering on monophonic cues, validated against our own corpus, and is not settled science

> **Polyphonic phrase-boundary detection has NO validated deterministic rule set in the literature —
> the L1.5 primitive is our own engineering and may not be presented as established method (D-607;
> re-homed into this specification 2026-08-04 from the methods document that formerly carried it).** Almost
> all published work on locating phrase endings addresses a single melodic line; for several
> simultaneous voices nothing comparable has been established. Carrying the monophonic cues over to
> polyphony is therefore engineering of ours, and it is validated against our own annotated corpus
> rather than cited. *Why:* a stated **fact of absence**, established by the survey behind the method
> catalog — the monophonic canon has a benchmarked literature and the polyphonic case has no
> comparable validated rule set. What DOES transfer is named rather than assumed: the **gap cue**
> generalizes cleanly, because a phrase boundary in polyphony is a near-simultaneous rest or long note
> across all voices — which is what makes chorale texture an unusually favourable case and is a reason
> to distrust a figure measured only there. (This bounds what the primitive whose contract is
> delegated two paragraphs above may claim; it does not change what that contract specifies.)

**In plain words.** Almost all published work on finding phrase endings is about single melodic lines. Our music has several lines at once, and nothing comparable has been established for that case. So carrying the single-line cues over to several voices is our own engineering and has to be checked against our own annotated music; it may not be presented as established method.

**Why.** A stated fact of absence, established by the survey behind the catalog: the monophonic canon has a benchmarked literature and the polyphonic case has no comparable validated rule set. What DOES transfer is named rather than assumed — the gap cue generalises cleanly, because a phrase boundary in polyphony is a near-simultaneous rest or long note across all voices, which makes chorale texture an unusually easy polyphonic case; the pitch-interval cue does not transfer cleanly, because there is no single line whose leap it would measure.

**Status.** LIVE · decided 2026-06-26 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:1524-1536`

**Provenance.** ★ RE-HOMED 2026-08-04 (CC, dispatch `cc_instruction_finish_line_item1.md`, Task 3.3, ruling R3): written into the OWNING LAYER SPECIFICATION in that section's own voice, with its defense. Register rule (e) prefers this route in terms, and D-231's purposive clause (criterion C4) is why it is preferred over a delegation: at completion the specifications must suffice to measure conformance against WITHOUT consulting the register, and a decision reachable only by following a pointer satisfies C1's letter and defeats C4. The classification that selected this entry, with its reason and the whole 94-entry population, is `tools/audit/decisions/finish_line_item1_routes.json`. Its former home class was `gap` — a decision governing a layer but not findable from that layer's section — which is precisely what the re-homing discharges; the field is cleared because a layer-specification home is not a non-specification home. **THE FORMER HOME, CLASS AND VERBATIM, PRESERVED (#12)** — former home `cowork_phrase_boundary_methods.md:83-85`; former verbatim: “- **No validated deterministic rule set exists for polyphonic phrase boundaries** comparable to the monophonic
  canon. Treat polyphonic extension as engineering on the monophonic cues, **validated against our own chorale
  ground truth** — not as settled science.” — `cowork_phrase_boundary_methods.md`, the research-first methods catalog grounding the phrase-boundary design (2026-06-26). Read in full by READ WAVE 5, 2026-08-04. Recorded in the catalog's §3. It is the ESTABLISHMENT STATUS (#19) of the mechanism **D-479** specifies — the cues run per eligible voice and aggregate to the texture — and no other home states it. The record states no ratifier.


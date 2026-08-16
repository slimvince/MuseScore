# Decisions group E — Layer 2 — the slicer

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-605 — The local-key hypothesis derives from key-agnostic signals ONLY and never from the key-area grouping, which is a post-grouping of the resolved key — a hard design rule, not a preference

> - **A local-key hypothesis derives from KEY-AGNOSTIC signals only, and NEVER from the key-area
>   grouping — a hard design rule, not a preference.** Deciding that a passage has moved to another
>   key may use the cadence detector, which is key-agnostic by construction, and the raw region
>   structure — root motion, diatonic-collection consistency. It may **not** read the key-area
>   grouping, which is a downstream post-grouping of the already-resolved key. The flow stays
>   strictly feed-forward: chords → key-agnostic cadence → local-key hypothesis → re-keyed key path →
>   key areas, rebuilt downstream. *Why:* named in the decision as the load-bearing soundness
>   property, and the circularity is concrete rather than argued — the grouping is built FROM the
>   resolved key, so a detector reading it would find the key it was given. It is the same discipline
>   that made the cadence detector usable, applied to the local-key hypothesis and naming the exact
>   surface that would make it circular. **Scope:** the mechanism this rule was written for sits on
>   the legacy key path, but what it constrains is *what evidence a modulation decision may read*,
>   which binds any such decision on any arm.

**In plain words.** Deciding that a passage has moved to a new key may only use evidence that does not already assume a key: the closure detector, which works without being told the key, and the plain shape of the music. It may not read the key-area grouping, because that grouping is built FROM the key already decided — using it would mean the detector confirming its own input.

**Why.** Named in the decision as the load-bearing soundness property, and grounded in a precedent: the same discipline is what made the cadence detector usable. The circularity is concrete and cited — the key-area grouping is built downstream of the resolved stay-home key, so a detector reading it would find the key it was given.

**Status.** LIVE · decided 2026-06-14 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:1866-1878`

**Provenance.** `docs/stage4d_local_modulation_design.md`, the Stage-4d local-modulation design, DRAFT and ratification-gated, 2026-06-14. Read in full by READ WAVE 5, 2026-08-04. The document's banner marks it DRAFT and ratification-gated, and its §7 lists this rule as item 2 for user ratification; the record does not state that the ratification happened, so no ratifier is recorded here. ⚠ The MECHANISM this rule governs is on the LEGACY key path — the joint estimator decides key and segmentation together and is the production inference layer (**D-001**, **D-005**) — but the RULE is about what evidence a modulation decision may read, which binds any such decision. It is the same principle **D-336**/**D-081** state for the cadence detector, applied to the local-key hypothesis and naming the specific surface that would make it circular. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The recorded owner question was that the rule's two ends sit in different sections — Layer 3 for the hypothesis, the key-area grouping for what it may not read. The user ruled that THE INPUT RULE BINDS THE HYPOTHESIS'S DERIVATION, so Layer 3 owns it and the grouping section points. Written into the Layer-3 section in that section's own voice, with its defense and with the scope statement the record carries: the mechanism it was written for is on the legacy key path, while what the rule constrains — what evidence a modulation decision may read — binds any such decision on any arm. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `docs/stage4d_local_modulation_design.md:51-56`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 49, "section": "## §3 — No circularity / key-agnosticism (the architecture constraint)", "label": "“§3”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**The local-key hypothesis MUST derive from key-agnostic signals — the cadence instrument (key-agnostic by
construction) + raw region structure (root motion, diatonic-collection consistency) — NOT from the current
KeyArea**, which is a downstream post-grouping of the resolved (stay-home) key (`sectionanalyzer.cpp:930`)
and would make the detector circular. The flow stays strictly feed-forward: chords → key-agnostic cadence →
local-key hypothesis → re-keyed key path → KeyArea (rebuilt downstream). This is the same discipline that
made the cadence detector usable; it is the load-bearing soundness property and a hard design rule." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).


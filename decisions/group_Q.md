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

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6421`

**Provenance.** ARCHITECTURE.md:6419-6422 (§15). No date or ratifier stated.

### D-163 — The batch tool deliberately skips post-load layout

> and `iex_musicxml` — no notation module required. Because the tool only consumes
> logical score structure, it deliberately skips forced post-load layout; this avoids
> legacy native MSCX cache-overflow crashes (for example Mozart `K533-3`) without
> changing the emitted harmonic-analysis JSON.

**In plain words.** The headless analysis tool never lays the music out on the page, because it only ever reads the logical structure.

**Why.** Stated constraint, ARCHITECTURE.md:6431-6433: skipping the layout avoids a legacy cache overflow crash on some scores (Mozart K533-3 is named) without changing the harmonic-analysis output at all.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6430`

**Provenance.** ARCHITECTURE.md:6424-6433 (§15). No date or ratifier stated.

### D-164 — What is out of scope, and what degrades gracefully at the boundary

> Live and real-time operation, film synchronization, adaptive game music, non-Western
> traditions (graceful degradation at boundary), post-tonal and serial music (graceful
> degradation at boundary), audio transcription from recording, spatial music, extended
> techniques as primary language.

**In plain words.** Live performance, film and game synchronization, audio transcription, spatial music and extended techniques as a primary language are not attempted. Non-Western traditions and post-tonal music are not attempted either, but the system is required to fail gracefully where it meets them rather than producing confident nonsense.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6640`

**Provenance.** ARCHITECTURE.md:6594-6643 (§16), which sorts the whole feature set into Core / Important / Prepared / Out of scope. No date or ratifier stated.

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


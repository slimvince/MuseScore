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

**Home.** `ARCHITECTURE.md:6205`

**Provenance.** ARCHITECTURE.md:6203-6206 (§15). No date or ratifier stated.

### D-163 — The batch tool deliberately skips post-load layout

> and `iex_musicxml` — no notation module required. Because the tool only consumes
> logical score structure, it deliberately skips forced post-load layout; this avoids
> legacy native MSCX cache-overflow crashes (for example Mozart `K533-3`) without
> changing the emitted harmonic-analysis JSON.

**In plain words.** The headless analysis tool never lays the music out on the page, because it only ever reads the logical structure.

**Why.** Stated constraint, ARCHITECTURE.md:6215-6217: skipping the layout avoids a legacy cache overflow crash on some scores (Mozart K533-3 is named) without changing the harmonic-analysis output at all.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6214`

**Provenance.** ARCHITECTURE.md:6208-6217 (§15). No date or ratifier stated.

### D-164 — What is out of scope, and what degrades gracefully at the boundary

> Live and real-time operation, film synchronization, adaptive game music, non-Western
> traditions (graceful degradation at boundary), post-tonal and serial music (graceful
> degradation at boundary), audio transcription from recording, spatial music, extended
> techniques as primary language.

**In plain words.** Live performance, film and game synchronization, audio transcription, spatial music and extended techniques as a primary language are not attempted. Non-Western traditions and post-tonal music are not attempted either, but the system is required to fail gracefully where it meets them rather than producing confident nonsense.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6418`

**Provenance.** ARCHITECTURE.md:6372-6421 (§16), which sorts the whole feature set into Core / Important / Prepared / Out of scope. No date or ratifier stated.


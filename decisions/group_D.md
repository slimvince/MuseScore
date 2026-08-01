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

**Home.** `ARCHITECTURE.md:1173`

**Provenance.** ARCHITECTURE.md:1162-1173 (Layer 1 - Built+Live)

### D-038 — Tied notes are one event; spans are answered by overlap with no horizon

> Tied groups are merged into **one** span/onset (via the DOM `firstTiedNote`/`lastTiedNote`/`playTicksFraction`); spans are true `[onset,release)` answered by **overlap with no horizon** (the old 4-whole-note backward cap is gone).

**In plain words.** A note tied across a barline counts once, starting where it was struck and ending where it stops. Asking what is sounding at a moment looks back as far as needed, with no arbitrary cut-off.

**Why.** Stated constraint, ARCHITECTURE.md:1173: tied groups are merged into one span and one onset via the score model's own tie links, and spans are answered by overlap with no horizon - which retires the old four-whole-note backward cap that could miss a longer sustain.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1173`

**Provenance.** ARCHITECTURE.md:1173; the behaviour change it caused is the ratified trade-off at :1026-1032

### D-039 — Ineligible notes are kept and flagged, never dropped

> Grace / non-playing / invisible / staff-ineligible notes are **kept and flagged, never dropped**.

**In plain words.** Notes that should not drive the analysis - grace notes, hidden notes, notes on a non-musical staff - are still recorded, marked as such. Nothing is thrown away.

**Why.** Stated constraint, ARCHITECTURE.md:1173, and #12: a dropped note is information lost for good, so ineligible notes are kept and flagged and each consumer decides what to do with them.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1173`

**Provenance.** ARCHITECTURE.md:1173; the standing no-information-loss principle is CLAUDE.md #12

### D-040 — The tie-unresolved atoms are republished additively for the joint estimator

> `notatedNotes()` republishes the tie-UNRESOLVED atoms — EVERY notated note incl. tie continuations, each with its OWN notated span, a `tieContinuation` flag, a `hasFermata` flag, and `resolvedIndex` linking to its tie-resolved `NoteEvent`

**In plain words.** As well as merging tied notes, the note reader also publishes them separately, each with a marker saying it is a continuation. The joint estimator needs both views.

**Why.** Stated constraint, ARCHITECTURE.md:1173: the tie-unresolved atoms carry the facts the tie-resolved surface discards and the joint estimator's event lattice and emission covariates need; publishing them additively keeps every existing consumer byte-identical.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1173`

**Provenance.** ARCHITECTURE.md:1173 records it as 'Purely additive' under the OI-180 dual-path sanction


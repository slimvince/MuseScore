# CC instruction — voice-leading idiom discovery (axis-2 study: the fuller follow-on the pilot warranted)

> **DISPATCH note (Cowork, 2026-07-03): ACTIVE — the one dispatched instruction** (the grammar-completion increment
> is landed, verified, ratified — STATUS 22c). Roadmap step 4, first half: *"the fuller voice-leading-idiom
> discovery … → the spec's voice-leading layer"* (`docs/implementation_roadmap.md`, forward sequence). This is a
> **read-only research/measurement increment**: Python pipeline only, no `src/` change, no build, no gate-corpus
> touch — the BIR gate is untouched **by construction** (state this in the report; no regen needed).
> Premises verified by Cowork at source this session: `idiom_discovery/parsers/voiceleading.py` (the pilot
> extractor + its hardcoded stale sandbox path in `__main__`), the pilot verdict + the follow-on scope
> (`cowork_idiom_discovery_findings.md` §"Voice-leading — is it a separate axis?"), the method contract
> (`cowork_idiom_discovery_design.md` — read it in full before running anything).

## The two questions (settled scope — the axis question itself is already answered YES, do not re-litigate it)

1. **What are the voice-leading idioms?** Beyond the pilot's chorale-vs-piano split (ARI 0.683): does the
   note-level corpus organize into stable VL idioms (contrapuntal/chorale part-writing, pianistic figuration,
   jazz-comping/arrangement textures, …)? Names are **post-hoc** readings of cluster signatures, per the contract.
2. **The formal orthogonality test.** On the pieces carrying BOTH views, the cross-ARI between the VL clustering and
   the harmonic-idiom clustering, plus the 2-D contingency (VL idiom × harmonic idiom). The pilot's implication —
   the full structure is ≥ 2-D: (harmonic idiom, VL idiom) + mode + chromaticism — measured formally.

## Method contract (binding, from `cowork_idiom_discovery_design.md`)

Discover → then name (no theory features in the encoding — no "species", no "Alberti", no schema labels);
**source-leakage confound test as a first-class gate** (VL clusters vs source-corpus vs tradition vs piece-length —
a cluster that is really "which corpus" is not an idiom); **granularity from stability** (K sweep + seed + cap
robustness, the v1.5/v1.6 discipline); post-hoc naming against theory features allowed only as interpretation.

## Tasks

**0 — Portability + premise fixes (mechanical).** `voiceleading.py` `__main__` hardcodes a stale sandbox corpus
root — make the root a CLI argument/environment default. Keep `vl_profile` byte-compatible (the pilot baseline must
stay reproducible).

**1 — Coverage (note-level only, enumerated + declared).** The VL axis is a notated-music axis (pilot scope note).
Extend loading to: **(a)** every DLC/DCML corpus on disk that carries `notes/*.tsv` (enumerate which of the
onboarded corpora qualify — report the list and per-corpus piece counts); **(b)** the full music21 4-part Bach
chorale set (drop the pilot's limit=60; declare the count); **(c)** the curated full-arrangement scores
(steely_dan / piazzolla / hiromi) read at **note level per notated (staff, voice)** via music21 — *not* chordify
(chordify destroys voices; VL needs them). **Declared limitation to state, not solve:** we read **notated** voices
only — implied polyphony / voice separation is its own future task (`cowork_polyphony_phrase_harmony_research.md`);
a piano staff whose single notated voice carries compound melody will read as leapy — that is a property of the
representation, recorded, not corrected by any inference.

**2 — Feature views (low-level, two declared views, mirroring the harmonic study's two-view discipline).**
- **View A (baseline, the pilot's):** per-piece per-voice |interval| histogram + repeat/step/leap rates —
  unchanged, so the pilot is a strict subset.
- **View B (new, declared):** **voice-pair motion-type rates** — for concurrent voice pairs at successive onsets,
  the rates of parallel / similar / contrary / oblique motion (directions of simultaneous moves; still purely
  interval-arithmetic, no theory labels). State the simultaneity rule you implement (onset alignment window) in the
  report. Run A alone, B alone, A+B — the ablation says which features carry the structure (the analogue of the
  harmonic study's root-motion-only test).

**3 — Discovery + the confound gate.** K sweep (at least 2–8) × ≥5 seeds × per-source caps (three cap levels scaled
to the note-level counts); report the stability table (ARI ± sd, self-stability) exactly in the v1.5/v1.6 format.
The confound gate: check clusters against source-corpus, tradition, era, piece length, and **voice-count/texture**
(a VL clustering that merely finds "4 voices vs 2 staves" needs to be *shown* to be more than instrumentation —
report the voice-count confound explicitly; if the structure IS instrumentation-shaped, that is a finding to state
honestly, not hide).

**4 — The orthogonality test.** On the intersection pieces (both a harmonic-view vector from the existing pipeline
and a VL vector): cross-ARI(VL clusters, harmonic clusters), the contingency table, and the curated-probe read
(do Steely Dan / Piazzolla / Hiromi — one *harmonic* idiom, per v1.6 — split by voice-leading?). Also project the
Bach chorales: the pilot predicts they are VL-tight/harmonically-scattered; confirm at the fuller coverage.

**5 — Report:** `cc_vl_idiom_discovery_report.md` — per-source counts, the stability + confound tables, the idiom
table (cluster → tradition/texture mix → signature features → post-hoc name), the ablation, the cross-ARI +
contingency, the curated/chorale probes, cost measured (if a full run exceeds the sandbox budget, run the scaled
version that fits and name the full run for the user's machine, per the v1.5 precedent), caveats. Reuse-vs-new
(expected: reuse the discovery machinery — `model.py`/`discover.py`/`stab.py`; new = the View-B extractor + loaders)
and what-retires (expected: nothing) per the standing rule. **No commit of findings-doc edits** — Cowork folds
`cowork_idiom_discovery_findings.md` after ratification; commit the pipeline code + your report only.

## Hard limits

- Nothing under `src/`; no build; no gate regen (by-construction statement instead). Fork-only.
- The frozen gate corpus and the held-out research beds stay untouched (`docs/score_inventory.md` governs; the
  engage-criteria E2 discipline applies to held-out splits).
- No inference problem-fixing anywhere — this increment *measures*; any lever it suggests is recorded for its
  proper layer, never coded here.
- The L1/L2↔music21 neutral-extractor cross-check (design D6) stays a SEPARATE build task — out of scope here.

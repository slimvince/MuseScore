# CC Instruction — LAYER 1 (Note Model): READ-ONLY audit + test-case spec

> The layer-1 design is **SIGNED** (`cowork_layer1_note_model_design.md`, user 2026-06-21): layer 1 = the
> lossless, annotated, **tie-resolved** note model; **all gaps to be closed**. This is the **read-only audit**
> that precedes implementation — verify the `[verify]` items at source, map the consumers, and **specify** the
> score-level test cases. **READ-ONLY: no code/behavior change, no test files built yet, no production touched.**
> Deliverable: `cc_layer1_audit_dossier.md`. North star: the note model must faithfully represent the **score**.

## §1 — ★ Tie handling, end-to-end (the critical item — do this first)
Cowork verified the `engravingbridge` module has **no tie logic** (grep, 0 matches) and computes per-note
duration from `cr->actualTicks()` (a chordrest's own length), with tied continuations skipped by `!n->play()`.
**Confirm or refute that tied sounding-spans are truncated to the first segment, end-to-end:**
- Trace whether **any** upstream/sibling layer merges ties before or inside tone collection — the engraving DOM
  tie API (`Note::tieFor()/tieBack()`, `firstTiedNote`/`lastTiedNote`), `cr->actualTicks()` vs any
  playback/duration helper, and the `scoreharvest` helpers. Does anything compute a tied-group total duration?
- Determine the **exact current behavior** for a note tied across a barline/region: what `onset` and `release`
  does the pipeline effectively see? Is the backward-reach (`collectRegionTones`/`collectSoundingAt`) able to find
  it when it sustains via tie into a later region, or does the truncated `release` drop it?
- If a read-only probe is possible without a build (e.g. inspecting an existing corpus score with a known
  tie-across-barline), use it; otherwise reason from the DOM API + the verified duration computation. **State the
  verdict with evidence; do not guess.**

## §2 — Confirm the gaps at source (the rest of §4 / the `[verify]` items)
For each, confirm the as-is + note the exact code location:
- **Drop-not-annotate (§4.1):** grace (`cr->isGrace()`), `!play()`, `!visible()`, staff-eligibility — each a hard
  `continue`. Confirm there is no annotation path. Flag the boundary cases: cue notes, unpitched-but-visible,
  editorial-invisible.
- **Fixed backward cap (§4.2):** `Fraction(4,1)` in both collectors; confirm both, and that nothing represents a
  note's true span (so range membership relies on the walk + cap).
- **PC-collapse (§4.3):** `collectRegionTones` aggregates to `accum[12]`, keeping only lowest pitch/tpc per PC;
  confirm what note-level facts are lost.
- **Two paths (§4.4):** `collectRegionTones` (weighted/PC) vs `collectSoundingAt`+`buildTones` (per-note);
  confirm they are the only two and how they differ semantically.
- **Multi-responsibility module (§4.5):** confirm slicing detectors / temporal-context / pitch-context co-located.

## §3 — ★ Consumer map (scopes what must adapt when the note model becomes first-class)
List **every call-site** of `collectRegionTones`, `collectSoundingAt`, `buildTones` (production + bridge +
`batch_analyze` + tests), and for each: **what representation it needs** — the weighted PC view, the per-note
list, the bass, specific annotations. This tells us which consumers become *queries/derived-views over the note
model* and which need the raw note set. (Reuse the grep from the step-1/2 work; report the full set.)

## §4 — Specify the score-level test cases (the §6 oracle) — SPEC ONLY, do not build
For each case, give: a concrete fixture (an existing corpus score + tick, or a minimal described score) and the
**correct note model** the implementation must produce (the notes that truly sound, with onset/release/voice/
flags). Cover at least:
- **Tie across a barline** (and a tie chain of ≥3) — release = last tied note's release; one span, not three.
- **A sustain longer than 4 whole notes** (the cap case) — must still be found by a later-region query.
- **Grace note** — kept, flagged `isGrace`, attached-to-next per the target (not dropped, not its own slice).
- **Cross-staff** and **multi-voice unison** (two voices, same pitch) — both represented with voice identity.
- **Invisible / non-playing** notes — kept + flagged, not dropped.
- **Percussion / hidden / chord-track staff** — correctly flagged `staffEligible=false` (annotation, not silent
  drop).
These specs become the implementation's acceptance tests; the audit only enumerates them + the expected output.

## §5 — Deliver
`cc_layer1_audit_dossier.md`: the §1 tie verdict (with evidence), the §2 gap confirmations (file:line), the §3
consumer map, the §4 test-case spec. State which `[verify]` items you confirm vs correct. **READ-ONLY — HEAD
`edd33901ed`, no code/test/production change.** Cowork reconciles; user ratifies before the implementation
(which closes all gaps) is scoped.

## §6 — Stop conditions
- Any code/behavior/test-file change → STOP (this is read-only spec).
- The tie behavior cannot be determined from source/DOM without a build → say so, give the best-evidenced
  reading, and propose the minimal read-only probe; do not guess a verdict.
- A consumer needs a representation the note model (§5 of the design) does not provide → flag it (the model spec
  may need a field); do not silently assume.

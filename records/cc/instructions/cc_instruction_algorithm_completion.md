# CC instruction — algorithm completion, step 1 of 2: fermatas, cadence features, and the missing chord classes (instrument layer; user-ratified option 2)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + 2026-07-19
> entries), `C:\s\MS\BUILD_AND_TEST.md`, `cowork_joint_estimator_factorization.md` §3 items 7–9
> (the boundary, fermata, and cadence factor forms), `cowork_term_theory_grounding.md` §1 the
> cadence-evidence derivation (the published feature forms and their named false-positive guards),
> and your probe-decoder record (`e3d17c325d` and its report).
>
> **Current state:** branch `master`, HEAD `e3d17c325d` (verify). TWO Cowork-authored uncommitted
> doc edits ride YOUR commit: `OPEN_ITEMS.md` (the OI-184 "executed" annotation left over from the
> prior arc — verify it is that row only) and `cowork_handoff.md` (state lines). **PYTHON-ONLY;
> instrument layer only (`tools/joint_estimator/`); no `src/`, no build, no test suite, no golden,
> no re-baseline. The firewall as always: no value adjusted in response to any measured number;
> the weight-fitting stage is NOT this dispatch — every new feature enters WIRED BUT WEIGHTLESS
> (weight 0, i.e. inert) until that stage.** Pinned instruments import-only.
>
> **Explorational-run status:** Task 3's re-measurement is explorational (surprises allowed,
> reported loudly, never adjusted for).

**Dispatch author:** Cowork, 2026-07-19, at the user's direction — executing the user's option-2
ruling (complete the algorithm in the instrument layer BEFORE any production build). This is step
1 (extraction + features + vocabulary); step 2 (the weight fit under the ratified held-out and
capacity gates) is its own later dispatch.

## Task 1 — the fermata extraction addendum

Extend `gen_note_events.py` to extract fermata marks (music21 expressions on notes/chords) into
the note-event data: per note, a fermata flag; per event, whether any sounding note carries one.
Regenerate `note_events/note_events.json`. **Invariance obligation: every previously existing
field must be byte-identical after regeneration** — prove it mechanically (field-wise comparison,
not eyeball) and report the fermata census (pieces with fermatas, fermata events per piece —
chorales should show them at nearly every phrase end; a piece with ZERO fermatas is worth listing).
**Do NOT re-count any existing table.** ONE addition is counted, because the ratified boundary
factor names it: the fermata-conditioned boundary cells — P(segment boundary | fermata at or
adjacent to the event) — counted under the same protocol as every table (folds, reliability rule,
exclusions, the interim misalignment leave-out), published as a small addendum artifact beside the
boundary table.

## Task 2 — the cadence features, wired but weightless

Implement in the probe decoder the ratified cadence-evidence features (factorization §3.9; the
published forms from the theory-grounding derivation), computed from note events on the fly, each
toward a candidate key at a candidate boundary site: the leading-tone resolution (the candidate
key's seventh degree rising to its tonic across the boundary); the tritone pair (the candidate
key's fourth and seventh degrees both sounding in the approach window); dominant-to-tonic bass
motion (root of the dominant to root of the tonic, root positions); the fermata as a
cadence-location prior with the weak-beat displacement convention (the arrival may sit one strong
beat before a metrically weak fermata). Carry the derivation's named false-positive guards as
feature definitions, not exceptions. **All feature WEIGHTS are 0 in this dispatch** — the features
compute and are logged in the decode artifact (fire counts per piece), but move no score, so the
Task-3 measurement isolates the vocabulary change alone. **Establishment: the mechanism-fires
check** — on the desk simulation's synthetic cases (injected-table parity mode), the features must
FIRE exactly where the desk-sim hand arithmetic applied its cadence credits (the authentic
cadence, the relative-pair resolution event, the tonicization's non-firing, the deceptive
cadence's key-vote) — report the fire/no-fire table against the desk-sim text; a mismatch is
examined and reported (the parity record already noted the hand arithmetic has minor slips — where
the mismatch is a documented desk-sim slip, say so with the evidence; where it is the feature
implementation, STOP).

## Task 3 — complete the chord-class vocabulary, re-decode, re-grade

Add the missing chromatic classes (the Neapolitan and the augmented-sixth family — their templates
already exist in the fit layer's chord-member mapping, their classes in the fitted tables) to the
probe decoder's vocabulary. Re-run the corpus decode and the side-by-side grading, identical
configuration otherwise. **Prediction (Cowork, written here): every axis moves by less than ±1
percentage point** — the classes are rare (the count inventory holds a handful of augmented-sixth
tokens and few Neapolitans); a larger movement on any axis is a prominently-reported surprise with
named-piece diagnosis. Report the same axes table beside the probe baseline, plus the fire counts:
how many segments decode to the new classes, on which pieces.

## Commit

**One commit:** `tools: algorithm completion step 1 — fermata extraction + counted fermata-boundary cells; cadence features wired weightless; chromatic classes completed; re-measured` —
the amended extractor and decoder, the regenerated substrate, the addendum artifact, the re-decode
and re-grading artifacts, this file (force-add), the two riding Cowork doc edits. Push **origin
only** (the standing hard stop on the upstream remote).

## Self-check before reporting (standing rule)

Diff scope proven (instrument layer + this file + the two named doc edits); substrate invariance
proven field-wise; no weight non-zero; firewall grep clean; all figures generated. **Report:** the
fermata census; the counted fermata-boundary cells; the feature fire/no-fire establishment table;
the Task-3 axes table with the ±1-point prediction verdict and new-class fire counts;
reuse-versus-new; anomalies (reported, never built around).

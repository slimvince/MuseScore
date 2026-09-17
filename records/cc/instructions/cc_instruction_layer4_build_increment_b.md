# CC Instruction — Layer 4 build, Increment B: per-note membership + two-pass + adaptive window (isolated, the lever)

> Increment A (`48909fb752`) is verified and ratified: the per-slice chord path + grading are stood up, byte-identical,
> and the baseline measured (per-slice 45.8/45.7 vs per-region 73.8/73.7 — the −28pt embellishment over-read; **22.2%
> of notes are ground-truth non-chord-tones the decoder currently swallows**). Increment B adds the **membership
> decision** — the lever that closes that gap. Still **isolated** (under `--decode-chords`, production byte-identical);
> wiring and the spelling-pin/new-types come later (Increment C, then wiring).

## §0 — Push Increment A first
Push `48909fb752` to **`origin` only** (`slimvince/MuseScore`). **NEVER `upstream`** (disabled; hard stop). Confirm
`origin/master` advanced by 1 via `git ls-remote`. Held WIP (the key-decoder/tpc/B2 hunks) stays unstaged. Then build B.

## §1 — The membership decision (binary chord-tone vs non-chord-tone)
For each slice and a candidate chord, classify **each sounding note** as a **chord-tone** or a **non-chord-tone**,
using only:
- **metric weight** — a weak, short, off-beat note is embellishment-like (read the note's **metric position
  per-note** from the Layer-1 `NoteEvent` stream via the **indexed** `NoteModel::overlapping`, NOT from the aggregated
  pc view — the audit §3 confirmed the per-note metric is not retained in `weightedPcView`'s aggregate);
- **local stepwise treatment** — a note approached and left **by step** between two chord-tones is a passing/neighbour
  non-chord-tone. This is the *local* membership cue **within the window**; it is **not** relational voice-leading or
  progression grammar (those are Layer 5 — do not reach for them).

The classification **feeds back into the candidate's score**: a reading that needs many implausible chord-tones is
penalised, so the chosen chord is the one that best explains the slice as *a chord plus its non-chord-tones*. **Fill
the membership sets** (chord-tone set + non-chord-tone set) in the result carrier (no longer stubbed). The added notes
(6th/9th/…) fall out of this — a chord-tone beyond the basic triad/seventh *is* the extension (do not add a separate
detector; that is the spec's reconciliation, but the new chord *types* and the spelling-pin are Increment C — here just
let the membership-decided chord-tone set carry the extras).

## §2 — Two-pass resolution (the neighbour chicken-and-egg)
Membership needs the neighbouring chords, which are the decoder's own output. Resolve in **two passes** (spec §4):
- **Pass 1:** name each slice provisionally from its own notes + the Layer-3 key prior alone (no neighbour-chord
  context).
- **Pass 2:** re-decide each slice's chord-and-membership using the provisional neighbours on **both** sides (a
  passing tone needs the chord it leaves *and* the chord it resolves to).
Use the neighbour **chords as context only** — **no** chord-to-chord transition cost, **no** progression smoothing
(Layer 5). A single refinement pass is the baseline; do not build the bounded-joint alternative (spec §15, deferred).

## §3 — Adaptive lazy-extend window (spec §2)
The base window is narrow (slice + immediate neighbours); **lazy-extend** it to cover the local figure (a broken
chord, a run of embellishments) **until the prevailing harmony is in view, and no further** — bounded by one harmony's
worth of figuration. Reuse the indexed builders (`weightedPcView`/`NoteModel::overlapping`); do **not** add a new
window builder. Window extent + the two-pass + the membership thresholds are **settings** (effort hygiene), not
constants.

## §4 — Grade (the key directional result, both presets, held-out)
- **Membership metric (now non-trivial):** the precision/recall of the non-chord-tone calls vs the human-analysis
  chord-tones (the harness stood up in A). Report both presets.
- **Chord-root metric:** report the per-slice+membership held-out chord-root vs (a) the Increment-A baseline (45.8%)
  and (b) the **per-region baseline (73.8/73.7)**. **The decisive question:** does per-slice **+ membership** now
  *meet or beat* the per-region baseline? That is the validation of the whole per-slice thesis — report it plainly,
  per preset, with the residual broken down (where does membership still over- or under-call?).
- Report the result; **do not tune toward a target** beyond the honest measurement. If per-slice+membership lands
  *below* per-region, that is a real finding to surface, not to hide.

## §5 — Gate (still isolated, byte-identical)
- Production byte-identical: the decoder still runs only under `--decode-chords`; the live per-region path is
  untouched. composing/notation/snapshot tests unchanged (modulo the known held-WIP notation failures, which must
  stay *exactly* the same set — if a new notation failure appears, STOP). BIR identity sets unchanged.
- Behaviour tests: a weak-beat passing note → flagged non-chord-tone, the chord stays the neighbours' chord; a
  sustained strong-beat extension → chord-tone (a sixth/ninth chord); a suspension → non-chord-tone; determinism.

## §5a — Unification (standing rule)
Membership reads the **indexed** per-note stream (`NoteModel::overlapping`); candidate scoring stays on
`weightedPcView` — two *views* for two purposes, not a duplicated builder, and **no DOM walk, no third window
builder**. Report the reuse-vs-new ledger and what retires at wiring; end with *"No new parallel path or logic
duplication was introduced."*

## §6 — Deliver
Commit **locally (unpushed)** on top of A: the membership decision + two-pass + window + the filled carrier + any
harness extension. Leave held WIP unstaged; `cc_*` report gitignored. Write `cc_layer4_build_b_report.md`: the
membership decision as built, the §4 directional result (the meet-or-beat-per-region answer, per preset), the
membership precision/recall, the byte-identity confirmation, and the §5a ledger.

## §7 — Stop conditions
- The decoder gets wired into the live path, or production output moves → STOP (still isolated).
- Membership needs **function/cadence** evidence to decide → STOP (that is Layer 5; the genuinely function-dependent
  case is flagged "uncertain" and carried, not resolved here).
- You start the spelling-pin, the new chord types, or a chord-sequence/progression smoothing → STOP (Increment C / Layer 5).
- A new window builder, a DOM walk, or a second scorer appears → STOP (unification).
- A new notation test fails (beyond the known held-WIP set) → STOP (something leaked into production).
- A push would target `upstream` → STOP.

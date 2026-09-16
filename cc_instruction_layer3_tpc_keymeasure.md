# CC Instruction — Layer 3: MEASURE whether a tpc-aware (spelling) key emission improves key accuracy (read-only)

> **Purpose:** a single read-only number to set a build-order decision. The key decoder is currently **pitch-class**
> (spelling-blind). The maximal-information principle says it should use the notated **tonal pitch class (tpc)** the
> Layer-1 note model already carries. Before we decide whether to retrofit Layer 3 (tpc) **before** building Layer 4
> or after it, measure whether a tpc-aware key emission actually beats the pitch-class baseline on the held-out key
> metric. **No production change, no commitment** — this is a measurement, not the retrofit.

## §1 — Build a tpc-aware key-emission VARIANT (decode-only)
- The note model carries **tpc** per note (`NoteEvent`), but the key emission's `PitchContext` passes only MIDI
  `pitch` (spelling-blind). Thread the **tpc** through to a **decode-only** tpc-aware emission variant — a parallel
  scoring path, the production `keyPrefs`/`analyzeScore` untouched (same pattern as the Step-2 scaleMembership
  decode-only measurement).
- Add a **tpc-based key-fit term** to the emission: score each candidate key by how well the notes' **spellings**
  (their **line-of-fifths** positions) fit that key's diatonic region — the standard spelling-aware key signal
  (Temperley's "roots/notes close on the line of fifths"; Chew's Spiral-Array center-of-effect). Keep it a **first
  reasonable variant**, not a full retrofit — the goal is "is there signal," not the final design. The variant =
  *existing pitch-class emission + the tpc term*, so the delta isolates the tpc contribution.
- Settings, not constants (effort hygiene); the tpc term's weight is a swept setting so a too-small/too-large weight
  doesn't hide the signal.

## §2 — Grade vs the pitch-class baseline (held-out, both presets, one grading path)
- On the held-out **TEST** split, per preset, reusing the existing key harness (`cc_layer3_keymode_baseline.py`,
  extended not forked), grade **(a) the committed pitch-class emission** vs **(b) the tpc-aware variant** — same
  decoder, same slices, decode-only.
- Report the **key-accuracy delta** (b − a), and **break it down by region type** (stable `loc==global` vs
  modulation `loc!=global`) — tpc/accidental-direction should help most at modulations/tonicizations and on
  sharp-vs-flat-side and relative/enharmonic-ambiguous keys. Sweep the tpc-term weight and report the best.

## §3 — Reliability caveat (state it, don't hide it)
The Bach/Jazz corpus is **engraved** (reliable spelling), so this measures the **upper bound** of the tpc benefit —
where the spelling is trustworthy. A MIDI import carries arbitrary enharmonics and would see less (or none). Note
this in the verdict: the number is "tpc benefit *where spelling is reliable*."

## §4 — Verdict (the build-order input)
State plainly: **does the tpc-aware emission beat the pitch-class baseline on held-out key, and by how much, where?**
- **Material gain** (clear, beyond noise, concentrated where expected) → the disciplined order is **L3-tpc retrofit
  before L4** (upstream-first: build Layer 4 on the corrected key, not re-tune it later).
- **Marginal / none** → **L4-first** is fine; the tpc retrofit is low-priority later polish.
Report the evidence; Cowork + user make the order call.

## §5 — Constraints
- **Read-only / decode-only.** Production analysis byte-identical (composing/notation/snapshots unchanged); no
  decoder or scorer **default** changed (the tpc variant is a decode-only override, like the Step-2 measurement). One
  grading path. No wiring.
- **No commit required** — this is speculative measurement; keep the variant + harness extension **local
  (uncommitted)** and deliver the report. Only if the verdict says "pursue tpc" does a proper increment commit
  anything. `upstream` untouched regardless.

## §6 — Deliverable
`cc_layer3_tpc_keymeasure_report.md` (held/gitignored): the tpc term used, the per-preset held-out delta (overall +
stable/modulation split + the weight sweep), the reliability caveat, and the §4 verdict.

## §7 — Stop conditions
- Any production output moves, or a decoder/scorer default changes → STOP (decode-only measurement).
- The tpc term needs chord/function evidence to compute → STOP (out of L3 scope; tpc is a note property, line-of-fifths
  is note-only — if you find yourself reaching past the notes, surface it).
- A push would target `upstream` → STOP.

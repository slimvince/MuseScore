# CC instruction — joint module Task C: the fact adapter, input parity by divergence class, end-to-end parity (+ four small closeouts)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + newest
> entries), `C:\s\MS\BUILD_AND_TEST.md`, the amended dual-path sanction in
> `cowork_prefit_gates.md`, and your Task-A/B record (`869e75e0a0`, `1e35415ee0` — the published
> `notatedNotes()` surface this task consumes).
>
> **Current state:** branch `master` at `1e35415ee0`, pushed, tree clean but for the
> pre-existing non-yours untracked files (verify). One Cowork-authored uncommitted doc edit rides
> your FIRST commit: `cowork_handoff.md`. **Touchable set:** the joint module, new test files,
> `tools/joint_estimator/` instruments, the riding doc edit — plus, ONLY if input parity proves a
> further L1 publication gap, additive L1 extension under the amendment's two proofs (name the
> gap first in the report, then extend). Anything else: STOP. Suites + snapshots proven per
> commit. Push **origin only**.

**Dispatch author:** Cowork, 2026-07-20, at the user's direction — the deferred Task C, now
standing alone on the surface Tasks A/B prepared.

## Task C — the fact adapter and the two parities

1. **The adapter:** the joint module builds its inputs — the note stream with spellings, voices,
   ties, fermatas; the event lattice; the covariates (metric class, step approach/departure,
   tie); meter, signature, declared mode — from the PUBLISHED fact surface (`notatedNotes()` and
   the existing published facts), never the raw score (include-closure audit re-run and
   reported).
2. **Input parity (the two-readers-agree establishment):** all 326 covered pieces, the adapter's
   facts against the committed `note_events/note_events.json`, field by field. The known mapping
   questions resolved mechanically and stated: the music21 part index ↔ the score's part/staff
   structure (voice threading — the covariates depend on it), tick and spelling encodings.
   **Divergences enumerated by CLASS** (count + 2–3 verified examples each); a mechanically
   unmappable class is a STOP-for-review with the evidence. The parity result is a generated
   artifact.
3. **End-to-end parity:** the module decodes all 326 from its OWN adapter (not the committed
   JSON); the decode must match the §5 oracle (`decode_parity_ref.json`) segment-exactly on BOTH
   arms. Any residual is diagnosed to its divergence class before anything else is claimed.

## The four closeouts (small, riding along)

1. The diagnostic decoder path (`maxplus_decode`) still carries the pre-§5 tie-break — §5-ify it
   (and re-run the stability diagnostic's equal-score check if cheap, else note it relaxed and
   why).
2. The superseded identity entry for `bwv362` in the old probe decode artifact: mark the artifact
   header as superseded-by `decode_parity_ref.json` for §5 purposes (do NOT churn a full
   re-timing regeneration).
3. The two cosmetic compiler warnings in `jointdecoder.cpp` (the shadow, the unreferenced local).
4. The CPython-3.12+ compensated-summation coupling: record it in the module's and the parity
   artifacts' provenance blocks (the reproducibility note — a future Python version changing
   `sum()` would surface as a parity break, which is exactly how it should surface).

## Commits

Up to TWO, each green (suites + snapshots; the two proofs if any L1 addition happens): (1) the
adapter + input parity (+ closeouts); (2) end-to-end parity artifacts. This file force-added
with the first; the riding handoff edit with the first. Push **origin only**.

## Self-check before reporting (standing rule)

Include closure; diff scope; coverage of the adapter's new paths named; all figures generated.
**Report:** input parity by divergence class (with the voice-mapping resolution stated);
end-to-end parity both arms; the closeouts; reuse-versus-new; timings; anomalies — surprises
reported, never built around.

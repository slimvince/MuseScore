# CC instruction — joint module Task 1: the L1 fact-surface extension, input parity, the tie-break, and the push

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + newest
> entries), `C:\s\MS\BUILD_AND_TEST.md`, **the amended dual-path sanction in
> `cowork_prefit_gates.md`** (the touchable set now includes ADDITIVE L1/L1.5 fact-surface
> extension under two proofs — read the amendment verbatim), **the tie-break rule newly recorded
> in `cowork_joint_estimator_factorization.md` §5**, and your own module-build report
> (`e0efd495f1` and its three-commit record).
>
> **Current state:** branch `master` at `e0efd495f1` — three LOCAL unpushed module commits sit on
> `3ff9017f4d` (verify). TWO Cowork-authored uncommitted doc edits ride your FIRST commit:
> `cowork_joint_estimator_factorization.md` (the tie-break rule) and `cowork_prefit_gates.md`
> (the sanction amendment); `cowork_handoff.md` + `STATUS.md` edits also on disk, riding (verify
> the four are the only non-yours diffs). **The three user ratifications this dispatch executes:**
> the two build-session artifacts are RATIFIED as committed (mode marginal + parity reference);
> the TIE-BREAK rule is ratified for implementation in BOTH decoders; the L1 EXTENSION is the
> ratified Task-1 architecture (a module-private raw score walk stays forbidden).
>
> **Hard rules:** touchable files = the joint module, the L1 fact-layer files needed for the
> ADDITIVE publication (under the amendment's two proofs per commit: every existing test
> unmodified and green, snapshots untouched; full coverage of the new published paths), new test
> files, `tools/joint_estimator/` instruments, the four riding doc files. Anything else: STOP.
> Suites + snapshots proven per commit. Push **origin only**, and this time DO push (the three
> existing commits plus this dispatch's — the user's standing instruction).

**Dispatch author:** Cowork, 2026-07-20, at the user's direction.

## Task A — the tie-break, both decoders, parity to 326/326

Implement the ratified §5 total order (fewer segments; then earliest boundary-tick sequence;
then canonical class-key order) in the C++ decoder AND the Python probe decoder (and the cached-
lattice fit path if it decodes). Regenerate the Python decode artifacts and the parity reference
(declared regeneration — provenance re-stamped); re-run full-corpus decode parity: **expected
326/326 path-exact on both arms.** Re-grade the regenerated Python decode; report any grading
delta on the previously-divergent pieces (expected below 0.05 pp per axis — equal-score paths
differing by one boundary; a larger movement is a reported finding). The committed CV headline
figures are NOT edited; the regeneration note lives in the artifacts.

## Task B — the L1 fact-surface extension (the ratified architecture)

Publish, additively, on the note model's output surface (structure yours; report it): the
notated-note facts the joint module needs and the model currently resolves away — per notated
note: tie-continuation flag, notated (unresolved) span, and the link to its tied group; plus
whatever minimal kin the input-parity work proves necessary (each addition named in the report).
The two proofs per commit, per the amendment: byte-identity for existing consumers (every
existing test unmodified and green; pipeline snapshots untouched — the additions must be pure
publication) and full test coverage of the new paths (new test files).

## Task C — the module's fact adapter + input parity (the two-readers-agree establishment)

The joint module's fact adapter consumes the published surface (never the raw score) and builds
its event lattice and covariates. Then the establishment the build dispatch defined: for all 326
covered corpus pieces, the adapter's extracted facts against the committed
`note_events/note_events.json` — note count, per-note (tick, duration, pitch class,
line-of-fifths spelling, voice threading, tie, fermata), the event lattice, meter, signature,
declared mode. Known mapping questions to resolve mechanically and state: music21 part index ↔
the score's part/staff structure (the flagged voice-assignment divergence — covariates depend on
it); tick and spelling encoding conventions. **Divergences are enumerated by CLASS with counts
and 2–3 verified examples each; a class that cannot be mapped mechanically is a STOP-for-review
with the evidence** — the fact surface disagreeing with the established extraction is a finding,
never papered over. Then: the module decodes from its OWN adapter (not the committed JSON) on all
326, and the decode must match the (tie-break-regenerated) oracle path-exactly on both arms —
the full end-to-end parity the build's "done" requires.

## Commits

Up to THREE, each green under the two proofs: (1) tie-break both sides + regenerated artifacts +
parity 326/326 (the four riding doc edits + this file force-added here); (2) the L1 additive
publication + its tests; (3) the adapter + input parity + end-to-end parity artifacts. **Push
origin only, including the three prior local commits.**

## Self-check before reporting (standing rule)

Diff scope per the amended sanction; the include-closure audit re-run (the adapter reaches the
published fact surface, not the raw score reader beyond it); byte-identity proofs per commit;
coverage named per new path; all figures generated. **Report:** parity results (path 326/326 both
arms, before/after the tie-break; input parity by divergence class; end-to-end); the grading
delta note; what the L1 surface now publishes (and that existing consumers are untouched);
reuse-versus-new; anomalies — surprises reported, never built around.

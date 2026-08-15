# CC instruction — the notation record assembly (output-surface contract §3.1–§3.4 built, dormant)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + newest
> entries), `C:\s\MS\BUILD_AND_TEST.md`, `OPEN_ITEMS.md`, and the ratified
> `C:\s\MS\cowork_notation_output_contract.md` IN FULL — this dispatch BUILDS its §3.1–§3.4
> record (with the ★ full-list amendment now in §3.3) as a dormant module surface. The seams
> (§1) and the switch are LATER dispatches; nothing here may touch the notation path's behavior.
>
> **Current state:** branch `master`; expected HEAD `56439ebad7` (the C++ slice commit, pushed)
> — verify via `git show --stat 56439ebad7` and that HEAD matches; mismatch = STOP. Riding
> Cowork edits (verify only non-yours diffs): `cowork_notation_output_contract.md` (the §3.3
> full-list amendment) and `cowork_handoff.md`. This dispatch file stays untracked.
>
> **Hard stops, always:** origin only; files outside the touchable set; ANY change to committed
> corpus bytes, goldens, `tools/robust_stop/`, or the notation path's output; a surprise is a
> STOP (#13) — surfaced, never built around. VS Code bash rules on every command. **Never
> hand-derive a music-theory table silently: every derived mapping below must carry its
> derivation in comments and pass its establishment step — a mapping that fails establishment
> is a STOP, not a tweak.**
>
> **No mid-flight steering:** self-sufficient; anything uncovered waits for the report.

**Dispatch author:** Cowork, 2026-07-26, at the user's option-1 ruling (the §3.3 full-list
amendment). **Purpose:** the joint module gains the CONTRACT RECORD — the §3.1 piece block, the
§3.2 committed-reading fields with the derived chord facts, the §3.3 group (i) slice (already
delivered — attached, not rebuilt), and the §3.4 modal reading — assembled by one module
function, DORMANT (declared dormancy, fact-publication corollary: the named consumer is the
seams dispatch). **No inference change, no output change anywhere.**

**Touchable set:** `src/composing/analysis/joint/**` + its tests + CMake lists;
`tools/batch_analyze.cpp` (ONLY the formatter re-point + any new default-OFF dump driver);
NEW `tools/joint_estimator/gen_spelling_establishment.py` + its artifact; `ARCHITECTURE.md`,
`STATUS.md`; the riding Cowork files. Pinned instruments import-only, as always.

---

## Task 0 — ratification-record commit (ONE commit, first)

Commit the two riding Cowork files exactly, message: `ratification record: contract §3.3
full-list amendment (user-ratified option 1, 2026-07-26)`. Push origin. Report the hash.

## Task 1 — the render/formatter primitives single-sourced into the module (ONE commit)

`jointOursQuality` and `jointRenderRn` currently live in `tools/batch_analyze.cpp` (the batch
render). The record needs the same derivations (§3.2 chord symbol + Roman numeral; §5.6
formatter continuity). One path per concern (#6):

1. Move them (public, documented) into the joint module (a small
   presentation-derivations unit beside the decoder is acceptable — they are DERIVED PUBLISHED
   FACTS of the module's own output, the ratified derived-fact family, not notation-layer code).
2. Re-point `batch_analyze.cpp` to the module functions; delete the tools-side copies.
3. **Establishment:** full-corpus regen via `--joint-inference`, all three preset dirs,
   **byte-identical** to the committed corpus (the render moved, values must not) — any diff is
   a STOP. Suites green.

## Task 2 — the record struct + assembly (ONE commit)

A module type (descriptive name, e.g. `NotationRecord`) + ONE assembly function
(score-decode-independent: it takes the `Piece`, the `DecodeResult`, the adapter/vocab/cache —
it never re-decodes):

1. **§3.1 piece block:** analyzed span; the signature-fifths + declared-mode INPUT ECHO (from
   `AdapterFacts`; include any mid-piece notated signature-change re-anchor points the adapter
   exposes — if it exposes none, say so in the report rather than adding score reads); the §2
   provenance block — the D1 embedded constants (`kTableArtifacts` hashes,
   `kWeightVectorIdentity`, `kDecoderVersion`). **This discharges the D1 declared dormancy —
   note it in the commit body.**
2. **§3.2 per segment:** the committed fields (span, tonicPc, isMajor, degree, quality,
   inversion, target, classKey) verbatim from `SegmentSummary`; PLUS the derived chord facts,
   each computed ONCE here: the key's signature-fifths value (REUSE the existing
   dependency-free (tonic, mode)→fifths primitive if one exists — locate it (the audit named
   `keySignatureFifthsForKey`); if it is not dependency-free, implement the module-local
   mapping with a comment naming the duplicate-to-retire and report it — do NOT include a
   heavy header, #7/OI-180 isolation); `rootPc`; the member pitch classes with factor roles
   (from the existing `ChordCache`/`chordFactorPcs` — reuse, don't re-derive); the chord-symbol
   and Roman-numeral strings (Task 1's module functions); `diatonicToKey` as the class's own
   diatonic-vs-chromatic/applied answer (derive from the class: plain diatonic degree classes
   true, applied/chromatic classes false — document the rule); the per-event bass factor role
   (bass pc vs members); the augmented-sixth display sub-type (It/Ger/Fr) from the SOUNDING
   pitch classes over the segment (§3.2's corrected derivation — presence of the
   characteristic tones; document the theory rule in a comment).
3. **§3.3 group (i):** attach the delivered `computePosteriorSlice` output (full lists, the
   amendment's form). Do not recompute anything.
4. **§3.5/§3.6:** ornament fields RESERVED-absent (a comment naming OI-194); none of the §3.6
   excluded fields exists on the record.
5. **Coverage:** unit tests over a small synthetic piece + at least 2 real corpus pieces
   (decode via embedded tables): every derived fact checked against independently-stated
   expectations (not against the code under test); the provenance block checked against the
   embedded constants; the aug-sixth sub-type exercised on a constructed case.

## Task 3 — the spelling derivation + its establishment artifact (ONE commit)

§3.2's root/bass SPELLINGS (tonal pitch classes) derived from (key, degree/class) — a NEW
deterministic mapping, the §5.2 establishment instrument:

1. Implement in the module: root line-of-fifths = the key tonic's lof + the degree/class's lof
   offset (mode-aware; the chromatic classes — applied targets, Neapolitan, augmented-sixth —
   per their standard-theory spellings). **Write the full derivation as a comment block** (every
   degree × mode × alteration, with the theory rule it follows); bass spelling = root lof
   adjusted by the sounding chord-factor's interval spelling (third/fifth/seventh per quality).
   No table entry exists without its derivation line.
2. **Establishment (§5.2), generated artifact (#17f):** NEW read-only
   `tools/joint_estimator/gen_spelling_establishment.py` — over the committed corpus decode
   (selected arm), wherever a committed segment's root pitch class ACTUALLY SOUNDS as a notated
   note in the segment span, compare the derived root spelling against the notated tpc
   (likewise the bass factor where it sounds). Output `spelling_establishment.json`: agreement
   counts overall and per (mode, degree/class) cell, and EVERY divergence enumerated
   (stem@tick, derived vs notated, class). **Read the divergences and classify them in the
   report:** an enharmonic-notation convention class (explainable, e.g. the OI-168 D♯/E♭
   family) is a finding to enumerate; an unexplained systematic cell (a wrong table row) is a
   STOP — fix the derivation and re-run, never special-case a piece.
3. Unit tests: the mapping on hand-derived cases across modes, applied classes, and the
   chromatic classes.

## Task 4 — the §3.4 modal-reading counter + its establishment (ONE commit, with doc sync)

1. Implement in the module, over the record's key runs (maximal same-key segment runs): for
   each scale degree 1..7 of the run's key, the sounding duration and onset count of EVERY
   chromatic inflection of that degree observed in the run (from the `Piece`'s note facts,
   pitch classes relative to the tonic; inflection identity by pitch-class offset, with the
   notated tpc recorded beside where available). Un-rounded counts only — no label, no
   threshold, no rounding (C1's publication; the presentation layer formats later).
2. **Establishment (§5.4):** (a) determinism + a unit test on a synthetic run with hand-counted
   expectations; (b) the bwv254 hand-check — the genuinely modal desk-sim piece: report the
   counter's minor-key variable-degree cells (the B♭/B♮ and C♯/C♮ traffic) and verify them by
   hand against the piece's notes (cite ticks in the report); mismatch = STOP.
3. **Doc sync (#10, this commit):** `ARCHITECTURE.md` joint as-built — the record (§3.1–§3.4
   delivered dormant, ornament fields reserved, seams pending), the spelling instrument + its
   artifact, the modal counter; `STATUS.md` closing entry (figures from artifacts only).

## Report

Hashes (Task 0 + the three build commits); the Task-1 byte-identity result; the record's field
list as built vs the contract §3 (any gap named — a contract field you could not build is a
FINDING returned to Cowork, not silently dropped, #12); the spelling establishment figures
(agreement overall + per-cell, the divergence enumeration with your classification); the
bwv254 modal-reading hand-check (cells + tick citations); suite totals (all three suites, every
task); reuse-vs-new / what-retires (Task 1 retires the tools-side formatter copies — say so;
name any located-but-not-reused primitive and why); anomalies. Standing self-check before
reporting: re-read every commit's actual diff against the principles and `DEFECT_TYPES.md`.

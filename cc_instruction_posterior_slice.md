# CC instruction — the OI-195 line-ending fix + the posterior slice (output-surface contract §3.3 group (i))

> **★ DATED AMENDMENT + RESUME NOTE (Cowork, 2026-07-26, user-ratified option A at CC's correct
> Task-2 STOP):** Task 1 is DELIVERED and Cowork-verified (`4565830c82`); resume at Task 2 with
> expected HEAD `4565830c82`. The riding Cowork edit now is `cowork_handoff.md` only (the
> Task-1-verified + ruling block). **Task 2's establishment paragraph is REPLACED by the
> two-half form below** (the original named `probe_corpus_decode.json` — the IDENTITY-weight,
> pre-§5 slice — as the oracle for a SELECTED-weights deliverable; unsatisfiable, a Cowork spec
> error, owned):
>
> **Establishment (#19), the ratified two-half form — both halves against frozen committed
> objects, no pinned-instrument edit:**
> **(a) The slice arithmetic (mechanism half):** run the SAME generator additionally at
> IDENTITY weights (the §5-current decoder). For every piece whose identity-arm committed
> segmentation equals `probe_corpus_decode.json`'s stored segments (the §5-unaffected pieces —
> expected ≈320 of 326), the derived key-axis runner-up and gap, rounded to the stored 4
> decimals, must reproduce the committed artifact's `posterior` entries EXACTLY, segment for
> segment. The remaining pieces (expected: the ~6 §5-canonicalized ones) are PRE-ENUMERATED by
> comparing identity-arm segments vs the stored ones BEFORE any slice comparison, and each must
> be individually explained as the ratified §5 tie-break (equal-score segmentation difference —
> show the equal scores). A seventh unexplained piece, or any divergence not attributable to
> the tie-break, is a STOP. This is the explained-diff pattern, not a tolerance.
> **(b) The decode half:** the generator's SELECTED-weights committed segments must equal
> `decode_parity_ref.json`'s selected-arm segments EXACTLY on all 326 pieces. Any mismatch is
> a STOP.
> The committed reference artifact (`posterior_slice_ref.json`) is the SELECTED-weights slice
> (both axes, full lists, full precision) — the composition of the two established halves — and
> is the Task-3 C++ parity oracle. Record the identity-arm establishment result (piece counts,
> the enumerated exception list with its per-piece equal-score evidence) in the artifact's
> manifest block (#17f) and the report. Everything else in Tasks 2–3 stands as written.
> **Also, small row touch (Task 2's commit):** append the real Task-1 hash `4565830c82` to the
> OI-195 row's resolution note (the row currently says "this Task-1 commit" because a commit
> cannot embed its own hash).

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + newest
> entries), `C:\s\MS\BUILD_AND_TEST.md`, `OPEN_ITEMS.md` (note the NEW row **OI-195**, riding
> your Task-1 commit), and the ratified `C:\s\MS\cowork_notation_output_contract.md` §3.3 —
> THIS dispatch delivers its **group (i)** (the established content-score slice), NOT group (ii)
> (the marginals stay OI-193's later step).
>
> **Current state:** branch `master`; expected HEAD `83fbb9e661` (the D1 codegen commit,
> pushed) — verify via `git show --stat 83fbb9e661` and that HEAD matches; mismatch = STOP.
> Riding Cowork edits (verify they are the only non-yours diffs): `OPEN_ITEMS.md` (the OI-195
> row) and `cowork_handoff.md` (the D1-verified block). This dispatch file stays untracked.
>
> **Hard stops, always:** origin only; files outside the touchable set; any change to the
> committed corpus bytes, `tools/robust_stop/`, or any golden (NOTHING may move in this
> dispatch); a surprise is a STOP (#13). VS Code bash rules on every command.
>
> **No mid-flight steering:** self-sufficient; anything uncovered waits for the report.

**Dispatch author:** Cowork, 2026-07-26. Two purposes, three commits: (1) fix OI-195 (the
embedded artifacts' line-ending canonicalization — instrument hygiene, zero value change);
(2) build the POSTERIOR SLICE — the contract §3.3 group (i) uncertainty surface — first as a
Python reference instrument, then on the C++ module surface with bit-identical parity. **No
inference value changes; no committed output changes; the notation path stays untouched.**

**Touchable set:** `src/composing/analysis/joint/**` + its tests + their CMake lists;
`tools/joint_estimator/gen_embedded_tables.py` (the OI-195 fix), NEW
`tools/joint_estimator/gen_posterior_slice.py` + its output artifact; `tools/batch_analyze.cpp`
(ONLY to add the default-OFF slice-dump driver); `ARCHITECTURE.md`, `STATUS.md`,
`OPEN_ITEMS.md` (row flips only); the riding Cowork files. Nothing else. **Pinned instruments
(`probe_decoder.py`, `a8_rebaseline_measure.py`, `robust_stop_diff.py`, `compare_rn.py`) are
import-only — not edited.**

---

## Task 1 — the OI-195 fix (ONE commit; carries the riding Cowork edits; flips the row)

The finding (verified at the objects, row OI-195): `gen_embedded_tables.py` embedded the CRLF
working-tree checkout form; the git-canonical blobs are LF (`.gitattributes` `* text=auto`;
`tables_all.json` blob 114,787 bytes vs 118,460 embedded), so the recorded hashes, the
regeneration, and the drift guard are checkout-configuration-dependent (#16; the OI-34 class).

1. Amend the generator: normalize every input artifact's bytes to the **git-canonical LF form**
   (strip `\r` before `\n`) before embedding AND hashing; state the canonical form in the
   generated header. The extracted weight vector's serialization is already generator-owned —
   make its line endings LF by construction too.
2. Regenerate `jointembeddedartifacts.{h,cpp}`; the JSON VALUES are untouched by construction
   (line endings only) — any parsed-structure difference is a STOP.
3. Amend the drift guard symmetrically: the file side of every byte/hash comparison normalizes
   to the same canonical LF form (so the guard now establishes against the committed OBJECT
   content, checkout-independent — the intended #19 form). `loadEmbedded == load` structural
   equality stays as is.
4. Re-establish: the drift guard green; `composing_tests` green; a regen spot-check —
   `batch_analyze --joint-inference` on ≥3 covered stems, output byte-identical to the
   committed corpus (the full-corpus regen was proven at D1 and the values cannot move; the
   spot-check guards against a generator slip). Any diff = STOP.
5. Commit (with the riding Cowork edits: the OI-195 row FLIPPED ✅ RESOLVED with this commit's
   hash + one-line mechanism, and `cowork_handoff.md`): message
   `joint: OI-195 — embedded artifacts canonicalized to git-blob LF form (generator + drift
   guard checkout-independent; values unchanged)`. Push origin.

## Task 2 — the Python posterior-slice reference instrument (ONE commit)

**What the slice IS (contract §3.3 group (i); the ratified full-list form — no truncation
constant exists anywhere):** for every COMMITTED segment of a piece's §5 decode:

- **Key axis:** for EVERY candidate key the decode evaluated for that piece (the decoder's own
  declared candidate key set — the same set `probe_decoder._segment_posterior` iterates), the
  segment's weighted content score under (that key, the committed chord class), where scoreable.
  The committed key is flagged; gaps are derived facts (score differences), not stored
  separately.
- **Chord axis:** under the COMMITTED key, for EVERY vocabulary class that is scoreable on the
  span (members/root defined, content score finite), the segment's weighted content score. The
  committed class flagged.

New generator `tools/joint_estimator/gen_posterior_slice.py` (imports `probe_decoder`
IMPORT-ONLY — `decode_piece`, `score_segment_content`, the vocabulary/cache machinery; no
pinned-file edit): decodes all 326 covered pieces from the committed `note_events.json` at the
selected weights (the §5 decode is deterministic), computes both axes per segment, writes
`tools/joint_estimator/posterior_slice_ref.json` with FULL-precision floats (`repr`-style
round-trip — this artifact is the C++ parity oracle) + a provenance/manifest block (#17f:
instrument, inputs, corpus hash, weight identity).

**Establishment (#19) — the new instrument against the existing published slice:** for all 326
pieces, the key-axis argmax-over-alternatives and its gap, rounded to the stored 4 decimals,
must reproduce `probe_corpus_decode.json`'s committed `posterior` entries (`runner_key`,
`runner_key_content_score`, `gap`) EXACTLY, segment for segment. Any mismatch = STOP (it means
the new instrument does not compute the established slice). Also: a re-run reproduces the
artifact byte-identically (determinism; LF by construction).

Commit: the generator + the artifact + (in the same commit) the `ARCHITECTURE.md` note is NOT
yet needed (C++ lands next task) — keep this commit instrument-only. Push origin.

## Task 3 — the C++ slice on the module surface (ONE commit, with doc sync)

1. **Additive surface extension:** the joint decoder's result gains the slice — per
   `SegmentSummary` (or beside it, keyed by segment), the two §3.3 group (i) lists (key-axis:
   candidate key + content score; chord-axis: class key + content score; committed entries
   flagged). Computed POST-decode by re-scoring held spans (the exact
   `_segment_posterior`/`score_segment_content` mechanism, already ported for the decode);
   every float sum on these paths uses the module's Neumaier summation (the established
   bit-parity discipline). The batch `.ours.json` render is **UNCHANGED** — the a8 grading
   schema keeps `"alternatives": []` (it is the pinned grading form; the record build consumes
   the slice later, on the notation surface).
2. **The parity driver:** a default-OFF `tools/batch_analyze.cpp` flag (name it descriptively,
   e.g. `--joint-posterior-slice <artifact-dir>`) that decodes the committed `note_events.json`
   corpus and writes the C++ slice in the reference artifact's schema, then (in-process or as a
   comparison step) verifies **bit-identical** equality against
   `posterior_slice_ref.json` — every piece, every segment, every candidate, both axes; writes
   a small pass/fail + first-divergence report file. Any divergence = STOP (the Neumaier lesson
   says exact parity is achievable; a near-miss is a defect, not a tolerance case).
3. **Coverage (the standing full-coverage objective):** unit tests for the new slice paths —
   a small synthetic piece with hand-checkable content scores (the desk-sim S1 shape is
   suitable), the committed-flag invariants, the scoreability edge (a class with no root), and
   the empty/degenerate span guard.
4. **Nothing moves:** full three-suite run green, NO golden touched; the committed corpus
   untouched (the render did not change — verify by the same ≥3-stem byte-identity spot-check);
   `tools/robust_stop/` untouched.
5. **Doc sync (#10, same commit):** `ARCHITECTURE.md` joint-estimator as-built section — the
   published slice (both axes, full-list, content-score semantics, group (ii) marginals
   explicitly NOT yet delivered = OI-193 open); `STATUS.md` closing entry (figures from your
   artifacts).
6. Commit + push origin.

## Report

The three commit hashes; the OI-195 flip (before/after hash values of one artifact demonstrating
LF canonicalization); Task-2 establishment result (the 326-piece reproduction of the committed
runner-up slice — counts, zero-mismatch statement); Task-3 parity result (pieces × segments ×
candidates compared, divergences = 0, the report file path); suite totals; the spot-check
result; reuse-vs-new / what-retires (expected: the slice reuses the ported content-scoring +
Neumaier primitives, one mechanism both axes; nothing retires — the legacy alternatives retire
only at the switch); anomalies (a surprise is a STOP — especially any parity or byte-identity
miss). Standing self-check before reporting: re-read all three commits' actual diffs against
the principles and `DEFECT_TYPES.md`.

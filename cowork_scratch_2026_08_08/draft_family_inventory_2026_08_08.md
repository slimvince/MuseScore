# DRAFT — the struck-versus-sounding family: the knowledge inventory for the phase-3 design

> **STATUS: COWORK READING SURFACE — landed at the return STOP 2026-08-09, ⟲ cells re-derived
> at that HEAD (away batch stopped clean after Tasks 0–2). NOT ratified, NOT a design, NOT a
> specification.** Written during the away batch from repo reads only. Purpose: one sourced
> surface holding every recorded fact about the family, so the phase-3 fix plan and the user's
> ratification read one document instead of eight rows and five reports. The DESIGN itself
> remains forbidden until phases 1–2 close (D-231); this is reading, not designing.
>
> **Ground stability:** the family rows' recorded facts are stable records (the away batch's
> tasks do not touch them). Anything below marked ⟲ derives from a regenerable artifact or a
> row CC may annotate mid-batch and must be RE-READ at the return STOP before carrying load.

## The family, as the gate defines it

`CLAUDE.md`'s phase-3 qualification names the members: **OI-215, OI-226, OI-227, OI-228,
OI-243, OI-244, OI-246, OI-277**, and defines the family question: *what the decoder or the
emission READS (struck versus sounding tones, note counting, pitch representation), and how
candidates are ADMITTED.* The one-fix-per-family rule (user, 2026-07-28) requires ONE design
over all of it; candidate admission is ruled COMPLETION, not refinement, so #8 permits the work
once phases 1–2 close — the licence is deriving the correct rule from the model, never
loosening thresholds until scores pass (DT-2).

## Member facts, sourced

**OI-215 — the sparse cliff (admission gate 2).** An event is uncoverable iff every ≤segCap(4)
covering window has <2 distinct ONSET pitch classes; one uncoverable event guarantees a
whole-piece EMPTY decode (`jointdecoder.cpp:444-445`, `:838-841`; code-proven theorem, not a
correlation). 13 of 23 committed large scores are theorem-guaranteed empty — every symphony in
the set; 0 instances on all 326 chorale fits and the perf corpus (the fit population cannot
express the failure). All-or-nothing emptiness is itself a #12 failure (no partial result, no
explanation). Any bounded-window extent candidate inherits the cliff on uncoverable runs.

**OI-227 — the dense cliff (admission gate 3).** Real-`candidateStates` scan over 172,611
events: 312 uncoverable = 291 member-overlap (sparse) + 21 fit/NCT-budget
(`(nOnset − present) > max(1, j−i)`, `jointdecoder.cpp:448`) on chromatic tutti (Holst 14,
1812 5, Beeth9 1+1). Opposite density extremes, same empty result. OI-215's <2-pc proxy
undercounts by exactly these 21. Named follow-up not run: whether the full 24-key set (no
top-6 prune) recovers some fitBlocked events.

**OI-226 — admission has NO ratified basis.** The four production rules (root-present;
member-overlap; NCT budget; top-6 key prune by onset-pc overlap, `kKeyPruneTopK=6`) appear
NOWHERE in the ratified §5 decode plan / premise ledger / prefit gates / output contract; §5's
only contemplated prunes are the segment cap and a RESERVED circle-of-fifths fitted-mass
neighborhood ("requiring its own established-loss measurement, never a silent heuristic") —
a DIFFERENT prune than the shipped one. Entered via the byte-for-byte probe_decoder port.
Mitigation on record: OI-188 measures the filters' COST (GT reachability ~72 %, GT state
force-added on 14,257 spans) — the form's derivation is what is absent.

**OI-228 — the emission reads STRUCK, the ratified spec says per tone/sounding.** The
factorization specifies P_emit per tone with the bass factor "each event's SOUNDING bass" and a
tied-over-preparation covariate; the Layer-2 spec makes slice identity the SOUNDING-note set
(`ARCHITECTURE.md:1045-1053`) and ranks actual sounding notes the STRONGEST evidence
(`:3134-3141`). The implementation walks onset-only `notesByEvent` (`jointdecoder.h:67`,
`jointdecoder.cpp:298-301`) and computes the "sounding bass" from the onset set (`:117`,
`:369-370`); the sounding set is consulted in exactly one place (missing-tone penalty), so a
held note can spare a chord a penalty but never support it. Measured 20–37-point presence
differences ON CHORALES — not confined to orchestral textures. **The refit caveat (recorded
2026-07-28): the note tables were FITTED under onset counting, so a decode-side correction
without a refit reads one thing through numbers calibrated to another.** User position on
record: a sounding note is part of the sonority; membership is what the emission's
chord-member/NCT categories are for. The decay defense was refuted (fit corpus is voices and
organ — sustaining).

**OI-277 — note-COUNT weighting (the third face; fit and decode AGREE).** Emission and
spelling sum per note record, so octave doubling (no new pc, same bass, same lattice) moved
committed readings on 13.2 % of segments, re-cut boundaries on 9 of 12 pieces; only emission
and spelling factors move (bass/missing-tone/boundary deltas exactly 0.0). NOT the OI-228
mismatch class: per-note is the TRAINED semantics — a model property, so pc-level or
voice-deduplicated emission is a MODEL CHANGE requiring a refit. A family-design input, not a
defect row.

**OI-243 — spelling factor not transposition-equivariant (ESTABLISHED, re-run 2026-08-03).**
`key_lof` anchors a canonical per-tonic spelling (`probe_decoder.py:743`); uniform respells
re-bin diatonic tones as pooled chromatic (396/413 violations); 66.26 % segment equivalence
(811/1224), boundaries moved in 27/36 conditions, near-collapses at +6. Separation
established: the defensible-enharmonic share is a small minority; boundary movement is the
overwhelming majority. Signature fold exonerated.

**OI-244 — key-prune tie-break not transposition-covariant (ESTABLISHED, same re-run).** Ties
break on (−fit, ABSOLUTE tonic pc, mode) before top-K (`probe_decoder.py:1039-1052`); the
shifted key can be pruned outright (LBL_PRUNE counted mechanically). Compounds OI-226: whatever
basis admission gets must STATE its invariance properties.

**OI-246 — concert/written pitch MIXED in one record on transposing staves.** pc from sounding
`ppitch()` (`note_model.cpp:93`), line-of-fifths from WRITTEN tpc (`:94`, `note.cpp:826-829`),
signature prior CONCERT (`jointfactadapter.cpp:360`). No layer statement records which
representation the spelling field must use; unexercised by the chorale corpus. A first-class
input-representation decision for the design's input-surface specification. (Adjacent, not a
member: OI-245 — three eligibility rules for one Layer-1 note surface; resolves with OI-239's
input-surface specification act + the family design.)

## What the ONE design must therefore cover (enumeration, not design)

(a) Candidate admission derived from the model with a ratified basis (both cliffs; the key
prune; stated invariance properties). (b) What the emission reads: struck vs sounding, per-tone
semantics, note-count vs pc/voice weighting — WITH the refit consequence stated (the tables'
counting rule and the decode's must match; a fit event under the fit gates). (c) The input
representation on transposing staves (and the OI-245 eligibility unification via OI-239).
(d) The no-partial-result shape (#12): what a decode reports when coverage fails.
(e) Established invariance targets: transposition equivariance (OI-243/244's probes become
regression checks per channel 3's pattern).

## Gate state before design may start ⟲ (re-derived 2026-08-09 at the post-batch STOP)

Phase 1 complete + phase 2's GATING channels. **Partition state at HEAD, read at
`tools/audit/phase3_gate_partition.json`:** 17 items, 14 GATING, 3 NON-GATING (P2-C4,
P2-TRUST, P2-OI288a); every item's check block records `has_run: false` — **no classified
item has run, so the partition stands unfalsified and the gate has not widened** (a
NON-GATING item yielding a family member remains a #13 STOP by the partition's own terms;
re-read when any item runs). **OI-349's probe was NOT run** — the away batch stopped before
its Task 7; the probe bears on D-472's precondition, not on this family, but its finding is
analysis-bearing and is read whenever it lands. **No family row gained a batch annotation**
(checked: no 2026-08-08/09 dated entry on any of the eight). Premise Gate (#17) applies in
full at design time: ledger, per-assumption predictions, desk simulation at identity weights
with provisional values, proxy links as premises.

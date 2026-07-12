# The key-grading re-baseline — OI-142 arithmetic correction + OI-143 dual home/local key columns

**CC, 2026-07-12.** Executes `cc_instruction_key_grading_rebaseline.md` (Cowork). Two
measurement corrections the user decided (register rows OI-142 and OI-143) landed as ONE
re-baseline event under the standing ritual: outgoing reference snapshotted first (O-12),
every run-level diff explained, the manifest re-stamped, the new figures **ratified by the
user before the reference commit** (guiding principles 14, 16). Measurement-layer only —
**no `src/` change, no constant tuned, no corpus file and no ground-truth file edited, no
golden refreshed.** Corpus frozen `c50002fee1`.

## The two corrections

1. **OI-142 — arithmetic corpus-transposition correction.** 12 of 326 WiR-covered Bach-chorale
   editions are transposed relative to their When-in-Rome reference (a constant whole-piece root
   offset; our reading follows the notated signature, the WiR edition is in another key — NOT a
   key-inference error). Each piece's committed offset is applied to the ground truth at **one
   shared substrate**, `dcml_parser.load_wir_regions`, so those editions grade against what our
   score actually contains. No consumer-side special-casing: every graded consumer reads the
   corrected view through the one path.
2. **OI-143 — dual home/local key columns.** The key-agreement column becomes two: vs the DCML
   **home/global** key (as before) and vs the DCML **local** key (the key in effect, crediting
   modulation-following). Both computed, both reported, nothing dropped.

## Commits (this event)

| step | commit | what |
|---|---|---|
| Task 0 register | `ebd37dfc7b` | Cowork's OI-142/OI-143 decisions + OI-141 direction + the instruction |
| Task 1 O-12 snapshot | `bd9e9c1ab2` | outgoing R10-b reference preserved byte-for-byte at `tools/robust_stop/snapshot_2026-07-12_pre_oi142_oi143/` |
| Task 5 adoption | `d9b52ba969` | substrate + local column + offsets file + re-baselined reference + re-stamped manifest + CLAUDE.md gate text |
| Task 5 fold | *(this commit)* | this report + OI-142/OI-143 closed + OI-141 note + STATUS + handoff |

## The offsets + independent re-verification (per-stem, before trusting them)

The 12 offsets (`our_root − dcml_root` mod 12) were **re-verified independently at the artifacts**
— the RAW `parse_rntxt_file` + the stated reproducible rule (`classify_key_disagreement._piece_transposition`,
modal offset ≥ 0.70 coverage) — on the frozen corpus, **all three presets**. The modal offset is
**identical across presets for every stem** (a whole-piece score transposition is preset-independent,
so one offset per stem applies to all presets). Full record: `tools/robust_stop/corpus_transposition_offsets.json`.

| stem | offset | coverage (Baroque/Jazz/Default) | notated-signature confirmation |
|---|---|---|---|
| bwv115.6 | +4 | 1.0 / 0.95 / 1.0 | notated 1♯ = G; WiR Eb |
| bwv126.6 | +2 | 0.962 / 0.957 / 0.962 | — |
| bwv145.5 | +2 | 0.946 / 0.892 / 0.944 | — |
| bwv148.6 | +1 | 0.967 / 0.962 / 0.967 | — |
| bwv177.5 | +3 | 0.815 / 0.833 / 0.808 | — |
| bwv180.7 | +2 | 0.971 / 1.0 / 0.971 | — |
| bwv184.5 | +7 | 0.875 / 0.919 / 0.875 | — |
| bwv244.62 | +10 | 0.933 / 0.9 / 0.903 | — |
| bwv267 | +11 | 0.946 / 0.914 / 0.947 | notated 1♯ = G; WiR Ab |
| bwv30.6 | +2 | 0.833 / 0.889 / 0.862 | — |
| bwv39.7 | +3 | 0.806 / 0.879 / 0.806 | — |
| bwv73.5 | +3 | 0.929 / 1.0 / 0.929 | — |

All 12 re-verified (offset matches the recorded value, coverage ≥ 0.70 on every preset). No stem
failed. The offset ADDS to every WiR `root_pc` + `global_key` + `local_key` tonic; the Roman-numeral
/ chord-symbol strings are key-relative and stay verbatim (a transposed edition plays the same
functional progression). Internally consistent: `V` under the shifted local key roots at the shifted
`root_pc`.

## The run-diff explained — confined to the 12, the other 314 byte-identical

The regression-stop instrument re-ran to a candidate; `robust_stop_diff` diffed it against the
snapshotted reference. **Every changed variant-(b) run — added AND removed — is on one of the 12
corrected stems**, and the non-transposed 314 stems' runs are **byte-identical** (proven per preset):

| preset | added | removed | changed stems | 314 byte-identical |
|---|---|---|---|---|
| Baroque | 237 | 599 | 12 (⊆ the 12) | ✅ (6269 unchanged) |
| Jazz | 245 | 592 | 12 (⊆ the 12) | ✅ (6444 unchanged) |
| Default | 237 | 598 | 12 (⊆ the 12) | ✅ (6285 unchanged) |

**Why added AND removed (not removals only):** a run's identity includes `dcml_root`, which shifts
by the offset for a corrected piece. The old false fail-runs (untransposed root) are REMOVED; the
residual non-modal-offset chords — genuine per-chord disagreements now surfaced once the constant
offset is removed — are RE-ADDED with the transposed root. The 12 pieces were 100 % root-disagree
by construction before, so on those pieces fail-runs can only shorten, never grow: per-stem
variant-(b) root-fail duration dropped on all 12 (total −222,480 / −216,480 / −222,000 ticks
Baroque/Jazz/Default). **No added run on a non-corrected stem; no non-corrected stem changed.**

## The hard stop — PASS on all three presets

Class-(b) (pitch-class-decidable-root) root-disagree **duration is non-increasing** — it decreases:
Baroque −218,400 · Jazz −213,360 · Default −217,920 ticks → **OVERALL PASS** (`robust_stop_diff`
exit 0). The two-tier class policy text is unchanged.

## Old → New baselines (from the generated `manifest.json` / `summary.json`)

| preset | root-agree | RN-agree | key-agree **home** | key-agree **local** (new) |
|---|---|---|---|---|
| Baroque | 63.3581 → **66.0406** | 44.5785 → **46.3293** | 68.1251 → **71.2909** | **65.7238** |
| Jazz | 62.3664 → **64.9772** | 42.3990 → **44.1010** | 64.4321 → **67.4887** | **62.4942** |
| Default | 63.2539 → **65.9307** | 44.4107 → **46.2280** | 67.4972 → **70.5183** | **65.3852** |

`scored_dur` unchanged (coverage stays 326) — the correction re-grades, it drops nothing. The new
reference self-reproduces (`robust_stop_diff` +0/−0, PASS, both key columns populated on the
reference side).

## The batch diagnostic (superseded, not the gate) — 52/24/52 → 54/24/54

`characterise_bir_false.py`, re-run through the corrected substrate, reports **54/24/54** (Baroque
+2, Default +2, Jazz unchanged). The two new Baroque/Default cases are **both on corrected stems**:
`bwv39.7@21600` (our C9/E vs a half-diminished seventh) and `bwv73.5@18240` (our D7♭9/F♯ vs a
diminished seventh) — the correction aligns WiR to our score, surfacing 2 residual share-tone /
diminished chord ambiguities. This is a superseded diagnostic, reported not gated.

## The test suites are unaffected (stated, not assumed)

No `src/` was touched, so the C++ suites are unaffected; the composing suite was run once as the
cheap sanity check — **1101/1101 pass** (2 disabled). The Python metric-primitive suites
(`test_metric_primitives_l0l1`, `test_metric_scripts`, `test_dcml_parser_figbass_pedal`) also pass
(**94/94**) — the substrate degrades to the plain parse for the 314 non-transposed stems and all
test fixtures (fake stems absent from the offsets file), so behavior there is byte-identical.

## Surprises / findings (surfaced, not buried)

1. **key-agree LOCAL is lower than HOME** (e.g. Baroque 65.72 vs 71.29). Honest and informative:
   our analyzer tracks the tonal **home** key more faithfully than DCML's shifting **local** key.
   Crediting the modulations we do follow (the tonicization label-gap, ~43 % of the home failures)
   is outweighed by the DCML local tonicizations we DON'T follow (staying home), which become
   local-disagreements. Both partitions are complete (each sums to `scored_dur`); the keyfail
   duration is identical for home and local (= our-key-unparseable). Both views are kept — the dual
   column is exactly what exposes this. Relevant to the OI-141 "wrong-key-area drift" line.
2. **The classifier's own transposition detector is now downstream of the correction.** Because
   `classify_key_disagreement` loads WiR through the corrected substrate, its internal
   `_piece_transposition` is fed already-corrected regions and would report 0 transposed pieces —
   the honest post-correction state (the correction moved upstream). Its `transposition_contamination`
   section is now effectively inert; a future touch can retire it or re-point it at the raw parser
   for provenance. Recorded as a note, not a code change this event.
3. **Scoping of the substrate routing.** The four graded consumers named in the instruction are
   routed through `load_wir_regions`; the correction logic is single-sourced there. The ~50
   historical / secondary WiR-reading scripts (e.g. `oracle_root_metric`, `compare_rn --wir-bach`,
   the `cc_*`/`diag_*`/`iter*` one-offs) still read the raw parse — out of scope for this event.
   Any that later become graded surfaces should adopt the one path (`load_wir_regions`). Noted as a
   boundary, not a silent gap; a register row (OI-144) tracks it.

## Self-check (mandated re-read of every diff on disk)

- **#6 total unification** — the offset logic lives in ONE place (`dcml_parser.load_wir_regions` +
  the one committed offsets file); the four consumers call it. A pc→note map I first duplicated was
  caught by the self-check and single-sourced (`_PC_TO_NOTE`, reused by `_resolve_dcml_key` and the
  transposition helper); the refactor is behavior-neutral (a8 summary byte-identical, 94/94 tests).
- **#9 non-stale corpora** — the corpus (`c50002fee1`) and every score/GT file are untouched; the
  correction is at the GT loading substrate, not the data.
- **#12 no information loss** — both key columns kept; the transposition is APPLIED (arithmetic
  correction), not excluded; the 12 pieces stay in the graded set.
- **#16 reproducibility** — outgoing reference snapshotted first (O-12); the manifest carries the
  corpus hash + the offsets-file sha256; a8's self-validation (grid == `grid_score_regions`) held on
  all 326×3 pieces; the new reference self-reproduces +0/−0.
- **#17f no hand-transcribed numbers** — the offsets file is generated from the re-verification
  artifact; the baselines enter via the generated `summary.json`/`manifest.json`.
- **No self-invented labels** — "home / local key", "OI-142/143", plain words throughout.
- **Gate policy** — the hard stop (class-(b) duration non-increase) holds with a decrease on all
  presets; the run-diff is explained and proven confined to the 12; the two-tier class policy text
  is unchanged.

## Boundary + push

Read-only w.r.t. production (no `src/`, no golden, no corpus/GT edit). Ratified by the user
2026-07-12 before the reference landed. Fork-only: all commits pushed to `origin` only, `upstream`
push confirmed disabled (`git remote -v`); nothing touches `musescore/MuseScore`.

*CC, 2026-07-12. The measurement substrate now grades the 12 transposed editions against what our
score contains, and reports key agreement against both the home and the local key. The governing
root-agree hard stop passed with a decrease; the reported baselines rose because ~12 % of the prior
"failure" was a corpus-integrity artifact, not inference error. The OI-141 key-inference research
now grades against honest columns.*

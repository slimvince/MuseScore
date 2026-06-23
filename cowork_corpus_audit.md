# Corpus & Test-Score Audit — Are we testing against the right files?

*Cowork, 2026-06-10. Direct inspection of the tree + `docs/score_inventory.md` (dated
2026-05-04, found significantly stale) + `tools/REPRODUCIBILITY.md` + registries.
Questions asked: do we risk missing files? are we treating our own annotations as
ground truth? what is stale?*

---

## C1 — HIGH: the snapshot gate depends on unpinned, gitignored external clones

The 11 pipeline-snapshot source scores are NOT in the repo. `pipeline_snapshot_tests.cpp`
loads them from `tools/dcml/*/MS3/*.mscx` (verified: bach_chorales ×3, bach_en_fr_suites
×2, mozart ×2, chopin ×2, corelli ×1, schumann ×1) — gitignored clones, and
`REPRODUCIBILITY.md` clones them at **floating upstream HEAD** (`git clone …` with no
commit pin, verified). Consequences:

- A fresh machine following REPRODUCIBILITY gets whatever DCMLab has at that moment;
  if upstream edits a score (they do — these are living research repos), the snapshot
  gate breaks or, worse, silently shifts meaning.
- The refactor gate we've called "decisive byte-identity proof" all season rests on
  files with no recorded identity.

**Recommendation (CC task, small):** record a `snapshot_sources_manifest.json` —
per-file sha256 + upstream repo + commit hash for the 11 .mscx (and the WiR/DCML
annotation files the gate corpus consumes); make `pipeline_snapshot_tests` (or a cheap
pre-check) verify hashes and fail with a clear "source corpus drifted" message; pin the
clone commits in REPRODUCIBILITY.md. Committing the 11 scores in-tree would be stronger
but DCML corpora carry CC BY-NC-SA-style licenses — **license check required before
any in-tree copy** (the GPL repo must not redistribute incompatible content).

## C2 — HIGH (conceptual): what our "ground truth" actually is — provenance taxonomy

| Asset | Annotated by | Used as | Risk |
|---|---|---|---|
| WiR rntxt + DCML harmonies TSV | **Humans** (research corpora) | The only real correctness ground truth (BIR three-way, rn metrics) | unpinned clones (C1); coverage gaps (C6) |
| `*.music21.json` (353) | **Algorithm** (music21's analyzer) | One leg of the three-way gate (counted only when music21 ∩ DCML agree against us — conservative, good design) | **the music21 version that generated them is recorded NOWHERE** (verified: no version string anywhere in tools/). Regenerating with a newer music21 would silently shift the gate denominators. |
| `chordanalyzer_catalog.musicxml` + expected JSON | **Us** (hand-built synthetic) | Unit-test ground truth + mismatch report | fine as a self-consistency pin; but the "4 RealDiff" number measures agreement with OUR OWN catalog choices — never quote it as real-music accuracy (inventory says this; worth repeating) |
| Pipeline snapshot goldens | **Us** (our own output, pinned) | Regression baseline ONLY | correctness enters only via the discipline of DCML-verifying each golden refresh — that discipline has held this season; keep it mandatory |
| s1c `.mscx` fixtures | **Us** (CC-authored, hand-derived expectations) | Unit pins | fine |
| `extra scores/`, jazz corpora | nobody (`ground_truth: false`) | qualitative only | correctly fenced |

**Answer to the user's question:** the headline gates do NOT rest on our own annotations
— but be precise about what they DO rest on. **The only ground truth is the human
annotation (WiR/DCML). music21 is NOT ground truth — it is an algorithm**, used as a
conservative noise filter: a case counts as a "genuine" error only when music21 sides
with DCML against us. Two consequences (user-flagged 2026-06-10): (a) the 13/7 numbers
are a *music21-filtered lower bound* on human-adjudicated errors — cases where music21
happens to agree with US against DCML, and `all_differ` cases, are excluded from the
error count by an algorithm's opinion; (b) the BIR=true/false split's denominators move
if music21's analyzer changes (hence C2's version pinning matters doubly). The filter is
a reasonable engineering choice (it suppresses DCML alignment noise) but it must never
be described as "ground truth agreement" — and Stage 5's metric redesign must evaluate a
human-only (DCML-only) gate variant alongside it. Remaining provenance holes: the
unrecorded music21 version (C2) and the unpinned human-annotation clones (C1). The
self-annotated assets (catalog, goldens) are used appropriately as regression pins, not
correctness claims.

**Recommendation:** record the music21 version + generation date in
`tools/corpus/README.md` and in the corpus manifest schema (one field); if
unrecoverable, freeze the current JSONs as canonical-by-fiat with a note.

## C3 — MED: the 353-chorale gate corpus has undocumented selection provenance

Verified counts: flat `tools/corpus` = **353** xml + 353 music21.json; DCML
`bach_chorales/MS3` = **361**; registry notes mention "352 genuine SATB chorales (from
410 retrieved)" in pre-registry runs. So the gate corpus is a filtered music21 export
whose filter criteria ("genuine SATB") and the identity of the excluded scores are
documented nowhere current. We are *probably* not missing anything that matters — but
"probably" is exactly what this audit is for.

**Recommendation (CC task, small):** produce the diff list (DCML 361 vs our 353 stems +
the 410→353 filter rule, recovered from `music21_batch.py`/REPRODUCIBILITY history),
document in `score_inventory.md`, and consciously decide: keep filter as-is (likely) or
expand. No silent exclusions.

## C4 — MED: stale artifacts that can mislead

1. **Flat `tools/corpus/*.ours.json` (353 files)** — pre-2.2a outputs frozen at the
   last flat-dir regen, bypassing all manifest validation. `analyze_inversion_errors.py`
   still reads them by default until Rider 1 lands (in flight, 2.2-ii). **Delete the
   flat .ours.json after Rider 1**, leaving xml + music21.json + README (the actual
   inputs).
2. **Empty accident dirs `tools/corpus/corpus/` and `tools/corpus/reports/`** (verified
   empty) — delete.
3. **`src/composing/tests/scores/` (7 files incl. one literally named `xxxxx.mxl`) is
   referenced by NOTHING** — no .py/.cpp/.cmake/CMakeLists match anywhere (verified).
   The inventory claims this dir is "the pipeline snapshot suite (eight scores)" —
   doubly wrong (lists 7, and the real suite is the 11 DCML scores per C1). These are
   dead committed binaries; delete after one final repo-wide sweep, or document a real
   consumer if one is found outside the grep surface.
4. **`docs/score_inventory.md` is stale across the board**: snapshot section (wrong
   files, wrong count, wrong location), `tools/corpus` section (pre-2.2a layout — no
   mention of `baroque/`/`jazz/` subdirs or manifests), mismatch-count drift. Needs a
   refresh pass referencing the 2.2a layout.

## C5 — LOW/OPPORTUNITY: human-annotated mass we own but never use

- `bach_en_fr_suites` (89 scores): no validation runner; only 2 scores used (as
  snapshot sources). 
- `cpe_bach_keyboard` (66): excluded from cross-corpus ("0 regions, stem mismatch" —
  known, but it's been parked since May).
- `when_in_rome` non-Bach (~700 of 762): only the Bach chorale slice feeds the gate;
  `compare_when_in_rome.py` exists but isn't part of any baseline.

Not a defect today — but Stage 5 (weight fitting) needs exactly this: more held-out
human-annotated data. Flagging now so Stage 5 doesn't fit and validate on the same
narrow slice. Also note 5 stray `bwv*_dcml.xml` QA artifacts in `tools/dcml/` root —
documented as intentional (gitignored), fine.

## Disposition summary

| # | Action | When |
|---|---|---|
| C1 | Pin + manifest the snapshot/gate source corpora (license check before any in-tree copy) | next hygiene instruction after 2.2-ii |
| C2 | Record music21 version or freeze-by-fiat; add field to corpus manifest | same instruction |
| C3 | Document 361/353/410 provenance + diff list | same instruction |
| C4.1–.2 | Delete stale flat .ours.json (post-Rider-1) + accident dirs | rides with the same instruction |
| C4.3 | Delete unused `src/composing/tests/scores/` after final sweep | same instruction (separate commit — removes committed binaries) |
| C4.4 | Refresh `score_inventory.md` | same instruction |
| C5 | Corpus-expansion decision (en_fr/cpe/WiR-full) | Stage 5 entry, recorded in roadmap 5.1/5.2 |

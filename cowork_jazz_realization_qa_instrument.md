# The jazz realization loop — a candidate phase-2 QA instrument (user-initiated 2026-08-02)

> **STATUS: CANDIDATE DESIGN — not built, not rowed yet** (the register is phase 1i's surface;
> the OI-7/OI-38 dated notes ride the next quiet window or the next dispatch as a named rider).
> Origin: the user's proposal 2026-08-02 — open a jazz lead sheet, realize its chord symbols,
> run the inferrer on the realized notes, compare against the original symbols. This document
> records the verified feasibility facts (the realizer's source read; the corpus licences
> web-verified) and the design that survives them. No build before phase 2 (D-231).

## §1 What the loop tests, and what it cannot

The chord symbols on a lead sheet are human annotations of harmonic intent per span. Realizing
them and inferring from the realized notes creates a closed loop with known intended harmony:
a scaled-up version of this repository's own established fixture pattern (the
`chordanalyzer_catalog.musicxml` tests), covering the REAL-WORLD DISTRIBUTION of jazz symbols
(extensions, alterations, sus, slash chords) plus known harmonic-rhythm boundaries (symbol
changes). It tests the VOCABULARY/IDENTIFICATION axis and segmentation on jazz harmony — the
axis OI-7 (EG-6) has lacked since it was written — at zero annotation cost, every failure
auto-diagnosable. It does NOT test real jazz performance texture (comping, walking bass,
arpeggiation); the claim it supports must say so. Human-annotated real performances (D-205,
OI-38/OI-56) remain the texture-validation path; this loop complements, never replaces (D-294
intact: the symbols are the human annotation; the notes are synthetic and declared as such).

## §2 The realizer, read at the source (all citations `src/engraving/dom/realizedharmony.{h,cpp}`)

- **The engine is `RealizedHarmony`** — the same machinery chord-symbol playback and the
  "Realize chord symbols" command use. Symbol → tone set via `getIntervals(rootTpc, literal)`
  with a MUSICAL ranking (h:92; cpp:284-299): rank 0 the 3rd/altered 5th/suspensions
  ("characteristic notes"), rank 1 the 7th, rank 2 the 9ths, rank 3 the 13ths/(minor) 11ths and
  other alterations, rank 4 the 5th and (major/dominant) 11th. Voicings SELECT the top-ranked
  tones — so the reduced voicings keep the identity-bearing tones by design.
- **The voicing axis (h:35-44, cpp:119-191) is free texture augmentation with IDENTICAL ground
  truth:** CLOSE (all tones, close position above middle C); DROP_2 (four tones, second-highest
  dropped an octave); SIX_NOTE / FOUR_NOTE (top 5/3 ranked tones, alternating octaves);
  **THREE_NOTE (bass + the two top-ranked tones — with the ranking, typically bass+3rd+7th: the
  classic jazz SHELL voicing)**; ROOT_ONLY (degenerate; skip). The bass note is always placed
  two octaves below middle C (cpp:112-117), and a slash chord's named bass replaces the root
  there — slash-chord ground truth is realized faithfully.
- **The `literal` flag (h:105)** doubles the axis: literal = exactly the symbol's tones (the
  strict grading mode); non-literal permits added tones per the ranking (a robustness mode with
  known-color added).
- **Spelling is carried:** the pitch map is pitch→tpc (h:64), so realized notes have real
  line-of-fifths spelling — our spelling-aware factors receive genuine input.
- **A built-in exclusion signal:** AUTO renders root-only when the parse is not
  `understandable()` (cpp:122-126) — unparseable symbols are mechanically detectable and
  excluded from grading rather than silently mis-realized.
- **Harmonic rhythm:** `HDuration::UNTIL_NEXT_CHORD_SYMBOL` (h:47-52) realizes each symbol until
  the next — the ground-truth segmentation, directly.
- **A cheap extension of our own:** deleting the realized bottom note post-hoc creates ROOTLESS
  variants (ground truth unchanged) — the classic rootless-comping test of root inference the
  voicing enum itself does not offer.

## §3 Establishment before trust (#19 — the user's own flagged premise, made a checked one)

Per symbol class: parse with the established parser (`chords_std.xml`, D-234) → realize
(literal, CLOSE) → verify realized pitch-class set = the parsed tone set. The output is a
per-symbol-class trust table; classes that fail are excluded from grading (and are themselves
findings — the realizer is MuseScore's own feature, so a defect there is upstream-reportable
under the D-229/D-316 pattern). Only established classes enter the graded loop.

## §4 The corpus, licence-verified (web, 2026-08-02; validation-only use per the reaffirmed D-292)

- **PRIMARY: OpenEWLD** (github.com/00sapo/OpenEWLD) — public-domain lead sheets in compressed
  MusicXML, harmony elements guaranteed by its README; MIT tooling. The clean backbone;
  repertoire skews pre-1929 (early standards) — a declared envelope bound.
- **SECONDARY: the iRealPro Corpus of Jazz Standards** (Zenodo 3546040, CC BY 4.0) — 1,186
  jazz standards' chord changes, **kern (convertible), no melody — which is exactly the clean
  realization-only variant; modern-repertoire coverage OpenEWLD lacks.
- **OPTIONAL: the Weimar Jazz Database** (ODbL) — beat-aligned chord annotations over real solo
  transcriptions; not lead sheets, but a future bridge toward the texture half.
- **Effendi (effendi.me/jazz): ADMITTED — the user's explicit risk ruling, 2026-08-02** ("Effendi
  is ok to use"), for validation-only use in the private research fork. 400+ MusicXML lead
  sheets with real `<harmony>` elements (verified on samples). Because its licence class is
  UNCLEAR, it follows the census's own established mechanism for that class
  (`cowork_score_census.md:70`): **hash-pin-only — the source files and their realized variants
  are never committed to the repository**; the manifest records their hashes, and regeneration
  re-downloads. OpenEWLD/iRealPro variants, being properly licensed, may be committed.
- **PlayThatSheet: excluded** — no file downloads exist, no licence exists, user-uploaded
  copyrighted material.
- D-361 applies (de-duplicate by work — standards recur across collections); ingestion follows
  the OI-38/OI-57 registry discipline.

## §4b The two-stage pipeline (the user's architecture, 2026-08-02)

**Stage A — PREPARATION, run once per corpus revision.** For each source MusicXML file: read it
with MuseScore; realize the chord symbols in EACH graded way (the voicing × literal grid of §2,
plus the rootless post-transform); save each realization as its OWN file — one file set per
tune, one file per realization variant (naming: `<tune>__<voicing>_<literal>.musicxml`). The
set is stamped with a `corpus_manifest.json` in the established discipline (source-file hash,
realizer establishment-table version, variant parameters, MuseScore commit) — the
`tools/REPRODUCIBILITY.md` / `run_bach_preset.py` pattern: regenerate-once, manifest-stamped,
licence-classed (committed for OpenEWLD/iRealPro; hash-pin-only for Effendi). Stage A is where
the §3 establishment check runs — a variant whose realized tones fail the parser check never
enters the set. Mechanically, stage A is a small batch tool over `RealizedHarmony` (the
`batch_analyze`/test-driver pattern), since the GUI command is per-score.

**Stage B — TESTING, run as often as wanted.** Open our own prepared files (never re-realize);
run the inferrer; compare against the original symbols through the §5 equivalence layer. A
`validate_corpus_dir`-style guard refuses to measure a set whose manifest or hashes mismatch —
the anti-contamination discipline the measurement layer already enforces everywhere else. The
separation means the realizer's establishment is paid once per corpus revision, testing is
cheap and deterministic, and any future MuseScore realizer change is a DECLARED corpus revision
(new manifest, new establishment run) rather than silent drift (#16).

## §5 The grading design

Two variants per piece × the voicing axis × literal on/off: (a) realization-only (clean
vocabulary/segmentation test — the iRealPro corpus is natively this); (b) melody + realization
(the melody's non-chord tones against a KNOWN chord = a labeled NCT test nothing else provides).
Comparison through a CONVENTION-EQUIVALENCE layer before any disagreement counts (the OI-31
class: C6 vs Cmaj7, implied sevenths, enharmonic kinds) — otherwise the loop measures notation
conventions, not inference. Symbols never feed the analyzer (D-066; the realized NOTES are the
input — deliberate closed loop, not the OI-204 self-feedback defect). Per-symbol-class and
per-voicing result tables; the rootless extension reported separately.

## §6 Where it slots

Phase 2's exhaustion program (a channel-1 population + channel-2 oracle instrument), beside the
sealed measurement-tools partition; the concrete candidate answer to OI-7, and an input to
OI-38's onboarding event. Rowing: dated notes on OI-7 and OI-38 naming this document — the next
quiet register window or the next dispatch's rider. Building it is a phase-2 act; nothing is
built now.

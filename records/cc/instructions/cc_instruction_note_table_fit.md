# CC instruction — the note-side table fit (the fit event, part 2 of 2; OI-176/OI-177 protocols in force)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + 2026-07-19
> entries), `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\cowork_prefit_gates.md`,
> `cowork_joint_estimator_factorization.md` §1/§3 (the event definition and factor forms; the §2
> granularity amendment), the §5a non-chord-tone decision in
> `cowork_joint_estimator_architecture.md`, and your own part-1 record
> (`cc_label_table_fit_report.md`, on disk).
>
> **Current state:** branch `master`, HEAD `c7094c71b3` (verify; the working tree carries ONE
> Cowork-authored uncommitted doc edit riding YOUR commit — `cowork_handoff.md`, the part-1
> acceptance + this dispatch's state line; verify it is the only non-yours diff). **PYTHON-ONLY; no
> `src/` edit, no build, no test suite, no golden, no corpus REGEN (the corpus `.xml` are read-only
> INPUTS), no re-baseline, NO DECODING, NO EVALUATION, no accuracy metric consulted (the DT-2
> firewall, as in part 1 — grep-prove it).** music21 9.9.1 (the established corpus toolchain) may be
> used read-only to parse `tools/corpus/*.xml`.
>
> **Hard stops, always:** any edit under `src/`; any edit to pinned instruments or
> `tools/robust_stop/` — import only; any golden/corpus/baseline touch. Nothing fit in part 1 is
> re-fit here (the declared staging).

**Dispatch author:** Cowork, 2026-07-19, at the user's direction — the fit event part 2: the tables
that need the NOTE stream. Layer home: `tools/joint_estimator/`. Three deliverables: the
note-event extraction, the pitch-emission table, the spelling table — plus the event-level boundary
denominator that part 1's table 6 declared owed.

## 1. The note-event extraction (new instrument; the substrate for everything below)

`tools/joint_estimator/gen_note_events.py` → per-piece note-event data (committed as ONE compact
artifact or per-piece cache under `tools/joint_estimator/note_events/` — your call on layout, report
it). From each covered piece's `tools/corpus/<stem>.xml` (music21 read-only; reuse any applicable
`music21_batch.py` machinery — report reuse-vs-new):
- per note: onset tick, duration, pitch, **notated spelling** (step + alter → line-of-fifths
  position), part/voice, tie-from-previous flag;
- the **event lattice**: the ratified event definition (factorization §1 — minimal segments between
  consecutive onsets/offsets), each event with its beat class (part 1's four classes, meter from the
  xml as in part 1);
- per note, the **chord-independent covariates** (§5a decision 4): metric class of its onset;
  approach from the previous note in the same voice (step ≤2 semitones / leap / none); departure to
  the next note in the same voice (step / leap / none); tied-over flag. Chromatic-neighbor motion is
  subsumed by step approach+departure with net return — do NOT add a fifth feature; the four above
  are the declared set (capacity discipline).
- **Establishment of the extractor (#19):** byte-reproducible; and a spot reconciliation on 3 pieces
  (incl. `bwv145.5`) — the extracted pcs sounding in a named span must equal the committed
  `.ours.json` region `pitchClassSet` for a region covering that span (cite the regions used; a
  mismatch is a STOP — two readers of the same score disagreeing).

## 2. GT-segment alignment and the counting population

GT segments from `dcml_parser.load_wir_regions` mapped to ticks through the established
`compare_analyses` measure-anchor machinery (imported, untouched). **OI-184 consequences, declared:**
for the 207 anacrusis pieces, the WiR `m0`-labeled segment is EXCLUDED from all note-side counts
(counting starts at m1 b1); the 7 flagged pieces (`bwv384, bwv274, bwv140.7, bwv113.8, bwv110.7,
bwv123.6, bwv112.5`) and part 1's 2 multi-meter pieces are excluded entirely from tick-anchored
counts. State the resulting counted-piece and counted-token totals in the artifact.

## 3. The pitch-emission table (factorization §3.1; the §5a NCT decision)

For each note within a GT segment (label normalized by the part-1 `normalize.py`, unchanged; local
key from the GT), classify its pc:
- **chord member** — against the realized template of the class: root = local tonic + the degree's
  interval (accidental prefixes like `bVI` honored; applied classes anchor to the TARGET's
  tonicized key); member pcs from the quality's template (the new template mapping is fit-layer
  logic in `tools/joint_estimator/` — document it; any unmappable class → a counted
  `template_unmapped` bucket, never guessed; report its size);
- **within-collection non-chord tone** — the LOCAL key's collection; minor = the ratified composite
  (natural + raised 6̂/7̂);
- **outside-collection tone.**
Table: P(category | covariate combo), fit per training fold + all-326 under the part-1 budget
mechanics (threshold 20; back-off chain declared here: full 4-feature combo → approach × departure →
the binary "covariate-supported" (any of: step approach or departure, weak metric class, tied) →
category base; α = 1 at the base). Presence/absence per note — NO duration weighting (the Temperley
warning, F1).

## 4. The spelling table (factorization §3.2)

P(spelled position | local key): each note's line-of-fifths position RELATIVE to the local key's
tonic spelling, binned: the seven diatonic degrees; raised 6̂ and raised 7̂ (minor); a flatward-
chromatic and a sharpward-chromatic pooled bin; fit per fold + all-326, same budget mechanics
(chain: fine bin → diatonic/raised/chromatic → base). The minor leading-tone vs subtonic contrast
must be a reportable cell (the F3/F4 discriminator). The signature-mask collection question is NOT
this table (it is the OI-168 form inside A's factor) — no signature input here, local key only.

## 5. The event-level boundary denominator (discharging part 1's table-6 caveat)

Refit table 6 with the denominator = EVENTS (the §1 lattice) instead of the 16th grid: per event,
boundary iff a GT label starts at its tick; same beat classes, same exclusions as §2. Published
BESIDE part 1's grid variant (both in the artifact, the grid one marked superseded-for-A); the
part-1 file is NOT edited (frozen — the new values live in part 2's artifacts).

## 6. Capacity, artifacts, establishment

- Artifacts: `note_tables_fold{0..4}.json` + `note_tables_all.json` +
  `note_table_fit_inventory.json` (+ summary txt), provenance-stamped as in part 1.
- **Combined capacity check:** the inventory reports part-1 + part-2 free parameters combined
  against combined training tokens, per fold — the ≥ 10 bound on the TOTAL (as well as per table).
  STOP if any fold fails.
- **Sensitive-cell hand-checks (the desk-sim anchors, verified segments):** show the classification
  arithmetic for (a) `bwv145.5` m10 b1–b2 under (E major, V6/V6-5): D♯/F♯/B/A all chord members
  (the desk-sim C1 finding — the fitted table must agree); (b) `bwv352` m1 b4 under (a minor,
  `vi/o7`): C/E/F♯/A all members, and under (a minor, `i`): F♯'s category + covariates (the C2
  pair); (c) one V-labeled minor segment showing the raised-7̂ chord-member classification.
- **Sanity anchors (report, no tuning):** in minor V-labeled segments, raised 7̂ frequency ≫ ♭7̂;
  the spelling table's minor leading-tone cell ≫ its subtonic cell (the Temperley direction). If an
  anchor FAILS, that is a #13 finding to report prominently — not to fix.
- **BCMH validation (protocol-reserved):** `tools/BCMH_dataset/` is NOT currently on disk — the
  ornament-cell validation against the 87-stem reduction is DEFERRED to a user-triggered follow-up
  (flag it in the artifact; do not block).
- Byte-reproducibility on all artifacts, as always.

## 7. Commit

**One commit:** `tools: the note-side table fit — note-event extraction, emission + spelling tables, event-level boundary (fit event part 2)` —
code + artifacts + this file (force-add) + the one named Cowork doc edit. Push **origin only**.

## 8. Self-check before reporting (standing rule)

The part-1 checklist applies verbatim (diff scope, pinned instruments untouched, no
grading/decoding import, generated figures only). **Report:** extraction layout + reuse-vs-new; the
counted-population totals after exclusions; per-table raw/kept/pooled/params per fold + the combined
capacity table; the emission table's headline cells (member/NCT/outside base rates; the
covariate-support effect); the spelling table's leading-tone/subtonic contrast; the event-level
boundary values beside the grid ones; the three hand-checks; `template_unmapped` size; anomalies
(#13). A surprise is reported, never built around.

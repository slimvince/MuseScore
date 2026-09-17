# CC report — the note-side table fit (the fit event, part 2 of 2)

**Dispatch:** `cc_instruction_note_table_fit.md` (Cowork 2026-07-19). **Branch** `master`, on top of HEAD
`c7094c71b3`. **PYTHON-ONLY**; no `src/` edit, no build, no test suite, no golden, no corpus regen, no
re-baseline, **NO DECODING and NO EVALUATION** — this produces the note-event substrate + fitted TABLES
as committed artifacts; nothing is graded. All figures below are read from the generated artifacts
(`tools/joint_estimator/note_events/note_events.json`, `note_tables_{fold0..4,all}.json`,
`note_table_fit_inventory{.json,_summary.txt}`), never hand-typed (#17f/DT-11).

## What was built (reuse vs new)

New under `tools/joint_estimator/` only, two instruments:

- **`gen_note_events.py`** (§1) — the note-event extraction. **Layout chosen:** ONE compact artifact
  `note_events/note_events.json` (all 326 WiR-covered stems; per-note arrays + the event lattice),
  provenance-stamped; the fitter reads this cache (no second music21 parse). **Reuse:** music21 9.9.1
  (the established corpus toolchain — same `TICKS_PER_QUARTER=480`, `round(offset*480)` tick convention
  as `music21_batch.py`, reading the same corpus xml); `gen_label_tables._beat_class` (the ONE
  metric-class definition — imported, not copied; part 1 is frozen, #6). **New:** the per-note/event
  extraction itself + the line-of-fifths spelling. music21 native `.measureNumber` (0 = anacrusis,
  **matching the WiR m0 convention** — verified) and `.beat` supply metric position + the anacrusis
  marker with no ours-anchor dependency.
- **`gen_note_tables.py`** (§3/§4/§5) — the fitter. **Reuse:** `gen_label_tables.katz_distribution` /
  `estimate_conditional` / `THRESHOLD` / `ALPHA` / `N_FOLDS` / `OI184_FLAGGED` (the part-1 fit
  machinery); `compare_analyses._dcml_time_spans` (the established GT (measure,beat)→tick measure-anchor
  resolver, **imported untouched**); `compare_rn._dcml_key_tonic` (the one key reduction);
  `normalize.normalize_label` (the OI-186a class); `dcml_parser.load_wir_regions` (OI-142 substrate).
  **New:** the chord-template mapping (§3, below) and the three tables. **DT-2 firewall:** no grader/
  decoder/robust-stop/a8 function imported or called (grep-verified — the only hits are doc comments);
  `compare_analyses` is used only for `load_analysis` (a loader) + `_dcml_time_spans` (the tick
  resolver); `music21.roman` is the template ORACLE for establishment only, never a decode.

The report `cc_note_table_fit_report.md` and the dispatch file follow part 1's tracking policy (the
report stays untracked; the instruction is force-added).

## §1 — extraction + establishment

`note_events.json`: **326 stems, 76,107 notes, 26,698 events**, 0 parse failures. Per note: onset/dur
ticks, pc, midi, line-of-fifths spelling, part/voice, measure (0=anacrusis), beat, metric class,
melodic approach/departure (step ≤2 semitones / leap / none, temporal same-voice adjacency),
tied-from-previous. The event lattice = the minimal segments between consecutive onsets/offsets with
≥1 sounding note (Pardo & Birmingham). **`beat_fallbacks_total = 0`** (the defensive `.beat` fallback
never fires — DT-23 counter).

**Establishment (#19):** (i) byte-reproducible — both instruments re-run byte-identical (all 8
artifacts). (ii) **pc reconciliation** on 3 pieces incl. bwv145.5: the extracted sounding-pc union
equals the committed Default `.ours.json` `pitchClassSet` on **every pitch-class-constant region**
(bwv145.5 26/26, bwv352 7/7, bwv254 10/10; cited clean regions in the artifact). The analyzer's own
region set is finer than a raw span union on *non*-pc-constant regions (its Layer-2 segmentation), so
the reconciliation is on pc-constant regions, where the two readers of the score must agree exactly —
they do (a mismatch there would be a STOP; none occurred).

## §2 — the counting population (OI-184 exclusions BIND)

**Counted stems = 317** (326 covered − 7 OI-184-flagged − 2 multi-meter `{bwv304, bwv362}`), all 4/4 or
3/4. *(The lone 3/2 piece, bwv123.6, is already one of the 7 flagged — so the meter-in-{4/4,3/4}
guard removed nothing further; reported.)* **213** of the counted stems are anacrusis pieces whose WiR
m0 segment was dropped (counting starts m1 b1; music21 measure-0 notes/events skipped). **Counted
tokens (all-326 fit):** emission 72,712 notes; spelling 72,712 notes; boundary 25,586 events. (Of
72,722 notes landing in a kept GT segment, 10 are `template_unmapped`, 0 indeterminate-key; 47 notes
fall in no GT segment — all surfaced in diagnostics, none silently dropped, #12/DT-23.)

## §3 — the pitch-emission table + the template mapping

**The template mapping** (`member_pcs`, fit-layer logic, dispatch §3): root = tonic + the degree's
interval (accidental prefixes honored); applied classes anchor to the TARGET's tonicized key (framework
mode = the target's own case); members from the quality template; the augmented-sixth and Neapolitan
chromatic classes carry their textbook pc content. **Two documented minor-mode rules** (the standard
DCML/rntxt convention): a diatonic diminished/half-diminished chord on degree 7 is the LEADING-TONE
chord (root +11, not the +10 subtonic), on degree 6 the RAISED-submediant chord (root +9).
**Established (#19) against music21 `RomanNumeral`:** **18,407 / 18,418 GT tokens agree (99.94 %)**;
`template_unmapped` = **3 tokens** (the multi-level applied labels `V6/5/V/III`, `V2/V/III`, `V/V/III`
→ counted, never guessed); the **8-token residual** is enumerated (rare edge cases: `VI2`, `III+6/5`,
`V9[b9]`, a `III7`-as-Maj7 and a `vi`-as-raised-6 spelling nuance — all ≤2 tokens each, understood).

**The fitted table** = P(category | covariate combo), category ∈ {member, within-collection NCT,
outside}, covariate combo = (metric class, approach, departure, tied); presence/absence per note, NO
duration weighting (the Temperley/F1 warning). Back-off chain: full 4-feature → (approach×departure) →
the binary covariate-supported → category base (α = 1). 38 combos observed, all well-populated (every
row sits at L0; row sums = 1 verified).

**Headline (all-326):**
- **Base category rates: member 0.824 / within-collection NCT 0.166 / outside 0.0094** — ~82 % chord
  tones, ~17 % in-collection non-chord tones, <1 % chromatic.
- **Covariate-support effect** — a note with NO figuration covariate (leap-in AND -out, strong beat,
  untied): **member 0.951 / within 0.043 / outside 0.006**; a note WITH one (step approach/departure OR
  weak metric OR tied): **member 0.816 / within 0.175 / outside 0.010**. The covariate ≈**4×**s the
  in-collection-NCT rate — exactly the Masada-Bunescu figuration signal.

## §4 — the spelling table

P(spelled line-of-fifths position relative to the local tonic | mode), per mode, seven diatonic degrees
+ raised 6̂/7̂ (minor) + pooled flatward/sharpward chromatic bins; local key only (no signature input —
that is the OI-168 form in A's spelling factor, a different factor). Chain fine bin → diatonic/raised/
chromatic → base; row sums = 1.

**The F3/F4 discriminator cell (minor):** **P(raised 7̂ leading tone) = 0.0753 ≫ P(♭7̂ subtonic) =
0.0355** — the Temperley minor-mode leading-tone dominance, the required reportable contrast. Major
dist peaks at the tonic (0.204) and dominant/5th (0.200); minor at the 5th (0.210) and tonic (0.208),
with raised 6̂ present (0.022).

## §5 — the event-level boundary denominator (discharging part 1's table-6 caveat)

Denominator = EVENTS (the §1 lattice); per event, boundary iff a GT label starts at its tick; same beat
classes, same exclusions. Published **beside** part 1's grid variant (reproduced in the inventory,
marked superseded-for-A; the part-1 file is NOT edited).

| beat class | event-level P (exact) | robust first-event P | part-1 grid P (superseded-for-A) |
|---|---|---|---|
| downbeat | 0.9734 (4288/4405) | 0.9741 | 0.9911 |
| mid_strong | 0.9607 (3054/3179) | 0.9610 | 0.8958 |
| other_tactus | 0.8612 (6666/7740) | 0.8619 | 0.7670 |
| sub_tactus | 0.3071 (3151/10262) | 0.3043 | 0.0656 |

The event denominator raises sub_tactus from the grid's silent-slot-diluted 0.066 to the true
per-event 0.307 — the correction the semi-Markov boundary factor needs. The **exact-tick** and the
**robust first-event-of-GT-segment** variants agree to <0.3 pp (both reported).

## §6 — capacity, hand-checks, sanity

**Combined capacity (part 1 + part 2, per fold) — PASS on every fold:**

| fit | combined params | combined tokens | tokens/param |
|---|---|---|---|
| all | 666 | 294,930 | 442.8 |
| fold0 | 618 | 235,577 | 381.2 |
| fold1 | 604 | 236,586 | 391.7 |
| fold2 | 602 | 237,527 | 394.6 |
| fold3 | 597 | 235,463 | 394.4 |
| fold4 | 612 | 234,567 | 383.3 |

Part-2 free params (all-326): emission 63, spelling 18, boundary 4 = **85**; per-table tokens/param all
≫ 10 (tightest: boundary 25,586/4 ≈ 6,397). The ≥10 bound passes ~38× over on the combined total.

**Hand-checks (dispatch §6a/b/c) — all agree with the desk sim:**
- **(a) bwv145.5 m10 b1–b2 (E major):** each note classified against its own onset's GT segment (the
  real fit logic) — b1 is **V6** (members D♯/F♯/B), b2 is **V6/5** (adds A as the seventh); **all
  sounding pcs are chord members, no spurious NCT** (`all_chord_members = true`; the C1 finding).
- **(b) bwv352 m1 b4 (a minor):** under **viø7** (member_pcs {C,E,F♯,A} via the minor raised-6 rule),
  C/E/F♯/A **all members**; under **i** (member_pcs {A,C,E}), F♯ is a **within-collection NCT** (rel
  line-of-fifths +3 = raised 6̂), covariates {approach step, departure step, metric other_tactus,
  untied} — the covariate-supported in-collection NCT the C2 desk sim predicted.
- **(c) minor V raised-7̂:** bwv10.7 (g minor, `V4/3`), member_pcs {0,2,6,9}; the raised 7̂ (F♯, pc 6) is
  the **third of V — a chord member** ✓.

**Sanity anchors (report, no tuning) — both hold:**
- minor V-labeled segments: raised-7̂ note count **1564 ≫** ♭7̂ **238**.
- fitted minor spelling: leading-tone cell (0.0753) **≫** subtonic cell (0.0355).

## Anomalies surfaced (#13 — reported, never built around; NONE is an inference problem)

1. **GT-start ↔ event-lattice jitter (measurement layer, OI-184 domain).** 270 of 17,667 kept GT starts
   (**1.53 %**) land between note onsets/offsets — sub-beat analyst-vs-note beat placement, and in a few
   pieces (e.g. bwv324) a score/analysis length mismatch drifting the mandated measure-anchor resolution
   at the piece end. Emission/spelling assign each note by onset-in-span (robust to this); the boundary
   table reports both the exact-tick and the robust first-event variants (agree <0.3 pp). This is a
   property of the *imported, mandated* GT-tick machinery — reported as a caveat, not altered, and it
   relates to OI-184. It does **not** implicate inference.
2. **The analyzer's `pitchClassSet` is not a raw span union** on non-pc-constant regions (its Layer-2
   segmentation is coarser than the pc-change granularity) — hence the establishment is on pc-constant
   regions. Expected, not a surprise; recorded so the reconciliation method is transparent.
3. **8-token template residual** vs music21 (0.04 %) — rare figured-bass/spelling edge cases, enumerated
   in the inventory; the class-consistent (decode-consistent) template is used, the oracle divergence
   reported.

No STOP raised. No inference problem was discovered; the above are measurement-alignment / table-design
reporting items for Cowork, within the OI-184 measurement domain.

## Self-check (post-work, on the actual diff)

Re-read every touched file's diff against the guiding principles / conventions / gate policy /
`DEFECT_TYPES.md`. Nothing touched outside `tools/joint_estimator/` + the instruction file + the one
named Cowork `cowork_handoff.md` edit (verified the sole non-mine tracked diff). Pinned instruments
untouched (`compare_analyses._dcml_time_spans` and `_dcml_key_tonic` imported, never modified; no
`a8`/`robust_stop`/decoder/grader import — DT-2 grep-clean). No decode, no evaluation, no accuracy
consulted. All figures generated (#17f). **#6:** the metric-class primitive is imported from part 1, not
copied (part 1 frozen); one note reader, one template mapping. **DT-23:** every drop path counts
(`note_unassigned`, `template_unmapped`, `note_indeterminate_key`, `gt_starts_off_lattice`,
`beat_fallbacks`) — none silent; `gen_note_events` STOPs loud on any parse failure. **DT-24:** outputs
go only to new `tools/joint_estimator/` paths — no committed corpus/golden/manifest is a default write
target (Default `.ours.json` is read-only). **DT-26:** the template oracle validation sweeps the full
18,418-token GT population, not a scoped subset. American English; internal keys (L0/L1/L2/BASE,
member/within/outside, raised6/raised7, chr_flat/chr_sharp) are descriptive mechanism identifiers
documented in the artifacts.

# The L3 UNPLACED rows — which the family rulings already reach, and which stay open (tier item 14, the inventory)

> **STATUS: WORKING INVENTORY, NOT A DECISION SURFACE.** Cowork, 2026-11-04 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_two.md`. It asks the user nothing and places no
> row. It records, for each row the reading file left UNPLACED, whether a ruling record (or its surface) of the L3 family
> work of 2026-11-02 to 2026-11-04 has already taken the row up, and what that record did. **Documentation only; no
> algorithm change.** Written member by member; members not yet done are listed as NOT YET DONE in §0.

---

## 0. Why this exists, and progress

**Why.** Tier item 14 (entry 481 §2 item 14) is *"the 451 UNPLACED rows by member and subject"*. The figure 451 is the
reading file's §13 total (`ratification_surfaces/cowork_comparison_l3_reading.md`, last modified on the device on
2026-11-01). The L3 family ruling records are dated 2026-11-02 to 2026-11-04, so they came after that count, and some
of them take up UNPLACED rows by number. Under D-599 (*"apply the standing principles FIRST, and only where they do not
decide is there a genuine user choice"*, LIVE, 2026-08-04 · user), a row a ruling already settles is not put to the
user again. So the rows still open have to be found before any item-14 surface is written.

**Method.** The member's UNPLACED list is taken from its foot table in the reading file (`| UNPLACED | n | … |`). Each
row number is searched in the ruling records whose file names carry `l3` (dated 2026-10-14 to 2026-11-04 in the
rulings folder's listing of this day; the family work is the records of 2026-11-02 onwards); the rows not found reached there are searched again in the `cowork_l3_*`
surfaces in `ratification_surfaces`; each hit is read at its line, in context. A row counts as **reached** only where a record
names that row-part (or the row with no part) in a ruling, a derivation ratified with a ruling, or an explicit
carrying-on. A row named only in a record's list of what was read is **not** counted as reached.

**What "reached" does not mean.** The records leave the re-marking of every row to the application dispatch (route
record §2 step 2). Several rulings decide a row against *"in so far as"* it says one thing; this inventory does not
judge whether the remainder of such a row needs a disposition of its own — the application act re-reads each row at §6.

**Progress.**

| Member | UNPLACED (reading file §13) | Status here |
|---|---|---|
| 7 — `cowork_layer5_function_design.md` | 44 | **DONE** (§1) |
| 8 — `cowork_layer6_grouping_design.md` | 62 | **DONE** (§1A) |
| 36 — `cowork_phrase_boundary_design.md` | 44 | **DONE** (§1B) |
| 46 — `cowork_progression_schema_dictionary.md` | 32 | **DONE** (§1C) |
| 44 — `cowork_progression_schema_design.md` | 22 | **DONE** (§1D) |
| 19 — `ARCHITECTURE.md`, *2. Architectural Principles* | 21 | **DONE** (§1E) |
| 38 — `cowork_target_architecture.md` | 21 | **DONE** (§1F) |
| 53 — `cowork_idiom_entry_mapping.md` | 21 | **DONE** (§1G) |
| 48 — `cowork_notation_output_contract.md` | 14 | **DONE** (§1H) |
| 4 — `ARCHITECTURE.md`, *4.3 ChordSymbolFormatter* | 11 | **DONE** (§1I) |
| 40 — `cowork_evidence_inventory.md` | 11 | **DONE** (§1J) |
| 23 — `ARCHITECTURE.md`, *6. The Style System* | 8 | **DONE** (§1K) |
| 2 — `ARCHITECTURE.md`, *Layer 5 — the function/cadence layer* | 7 | **DONE** (§1L) |
| 3 — `ARCHITECTURE.md`, *Layer 6 — the grouping layer* | 4 | **DONE** (§1M) |
| 24 — `ARCHITECTURE.md`, *7. The Knowledge Base* | 4 | **DONE** (§1N) |
| 54 — `cowork_bounded_context_design.md` | 4 | **DONE** (§1O) |
| 37 — `cowork_voiceleading_axis_design.md` | 3 | **DONE** (§1P) |
| 50 — `cowork_layer1_note_model_design.md` | 2 | **DONE** (§1Q) |
| the single rows of members 9, 10, 12, 21, 22, 32, 47, 52 and 56 | 9 | **DONE** (§1R) |
| 57 — the L2 transfer input, part 1 of 5 (the foot table at reading file line 73993) | 19 | **DONE** (§1S) |
| 57 — the L2 transfer input, part 2 of 5 (the foot table at reading file line 75342) | 24 | **DONE** (§1T) |
| 57 — the L2 transfer input, part 3 of 5 (the foot table at reading file line 76579) | 34 | **DONE** (§1U) |
| 57 — the L2 transfer input, part 4 of 5 (the foot table at reading file line 77808) | 20 | **DONE** (§1V) |
| 57 — the L2 transfer input, part 5 of 5 (the foot table at reading file line 78371) | 10 | **DONE** (§1W) |

**Every member is done.** The table's UNPLACED column sums to 451 (44 + 62 + 44 + 32 + 22 + 21 + 21 + 21 + 14 + 11 + 11
+ 8 + 7 + 4 + 4 + 4 + 3 + 2 + 9 + 19 + 24 + 34 + 20 + 10), the reading file's §13 total.

*(Former wordings of the last row, kept (#12): "every other member with UNPLACED rows | 407 | NOT YET DONE", true until
member 8 was done; "every other member with UNPLACED rows | 345 | NOT YET DONE", true until member 36 was done;
"every other member with UNPLACED rows | 301 | NOT YET DONE", true until member 46 was done; "every other member with
UNPLACED rows | 269 | NOT YET DONE", true until member 44 was done; "every other member with UNPLACED rows | 247 | NOT
YET DONE", true until member 19 was done; "every other member with UNPLACED rows | 226 | NOT YET DONE", true until
member 38 was done; "every other member with UNPLACED rows | 205 | NOT YET DONE", true until member 53 was done; "every
other member with UNPLACED rows | 184 | NOT YET DONE", true until member 48 was done; "every other member with UNPLACED
rows | 170 | NOT YET DONE", true until member 4 was done; "every other member with UNPLACED rows | 159 | NOT YET DONE",
true until member 40 was done; "every other member with UNPLACED rows | 148 | NOT YET DONE", true until member 23 was
done; "every other member with UNPLACED rows | 140 | NOT YET DONE", true until member 2 was done; "every other member with UNPLACED rows | 133 | NOT YET DONE", true until
member 3 was done; "every other member with UNPLACED rows | 129 | NOT YET DONE", true until member 24 was done; "every other member with
UNPLACED rows | 125 | NOT YET DONE", true until member 54 was done; "every other member with UNPLACED rows | 121 | NOT
YET DONE", true until member 37 was done; "every other member with UNPLACED rows | 118 | NOT YET DONE", true until
member 50 was done; "every other member with UNPLACED rows | 116 | NOT YET DONE", true until the single rows were
done; "every other member with UNPLACED rows | 107 | NOT YET DONE", true until member 57's first foot table was done —
that row was member 57 alone, 19 + 24 + 34 + 20 + 10 = 107 over its five foot tables; "57 — the L2 transfer input,
parts 2 to 5 (the foot tables at lines 75342, 76579, 77808, 78371) | 88 | NOT YET DONE", true until part 2 was done —
24 + 34 + 20 + 10 = 88; "57 — the L2 transfer input, parts 3 to 5 (the foot tables at lines 76579, 77808, 78371) | 64 |
NOT YET DONE", true until part 3 was done — 34 + 20 + 10 = 64; "57 — the L2 transfer input, parts 4 and 5 (the foot
tables at lines 77808, 78371) | 30 | NOT YET DONE", true until part 4 was done — 20 + 10 = 30; "57 — the L2 transfer
input, part 5 of 5 (the foot table at line 78371) | 10 | NOT YET DONE", true until part 5 was done.)*

---

## 1. Member 7 — `cowork_layer5_function_design.md` (44 row-parts)

The foot list (reading file line 8592): 7.1(i), 7.1(ii), 7.8, 7.31(i), 7.31(ii), 7.33(ii), 7.34, 7.35, 7.36, 7.37,
7.44(i), 7.47, 7.48(i), 7.68(i), 7.85, 7.94, 7.96, 7.100, 7.101(i), 7.101(ii), 7.102, 7.103, 7.104, 7.105, 7.106,
7.107(i), 7.107(ii), 7.110(ii), 7.112(ii), 7.114(ii), 7.115(i), 7.115(ii), 7.116(ii), 7.189(i), 7.199, 7.249, 7.269,
7.273, 7.294(v), 7.301(i), 7.301(ii), 7.329(i), 7.331, 7.336.

### 1.1 Reached by a ruling record — 34 row-parts

Record short names: **phrase ends** = `cowork_rulings_2026_11_02_l3_phrase_ends_sitting.md`; **cadence placement** =
`…_2026_11_02_l3_cadence_placement_sitting.md`; **cadence features** = `…_2026_11_03_l3_cadence_features_sitting.md`;
**cadence type** = `…_2026_11_03_l3_cadence_type_sitting.md`; **cadence mass** = `…_2026_11_03_l3_cadence_mass_sitting.md`;
**six-four** = `…_2026_11_03_l3_cadential_six_four_sitting.md`; **sections** = `…_2026_11_03_l3_sections_sitting.md`.

| Row-part | Record, place | What the record did |
|---|---|---|
| 7.1(i), 7.31(ii), 7.100, 7.101(i), 7.102, 7.103, 7.106, 7.107(ii), 7.189(i), 7.269, 7.301(i) (11) | cadence type, Ruling 1 (§1) | decided against *"in so far as they make the bass-derived inversion the only criterion"* |
| 7.1(ii), 7.31(i), 7.101(ii), 7.105, 7.107(i), 7.301(ii) (6) | cadence features, Ruling 1 item b (§2) | decided against *"in so far as they keep the fact unpublished"* (the highest sounding pitch's degree at the arrival) |
| 7.8, 7.35, 7.44(i), 7.329(i) (4) | cadence type, Ruling 2 (§1a) | decided against *"in so far as they fix one list as the only one"*; their lists remain candidates for declared vocabularies |
| 7.104 | cadence type, Ruling 3 item b (§1b) | derivation ratified: the perfect/imperfect split computable wherever its features carry values |
| 7.115(i) | cadence type, Ruling 3 item c (§1b) | derivation ratified: the evaded cadence published as *type not computable* with its reason until OQ-L3-5 |
| 7.112(ii), 7.114(ii), 7.115(ii), 7.249 (4) | cadence mass, Ruling 1 (§1) | decided against *"in so far as they lower confidence by a fixed rule"*; Row 7.249's forecast is not decided against, only its by-rule part |
| 7.37, 7.94, 7.273 (3) | six-four, Ruling 1 (§1) | 7.94 decided against (the collapse); 7.273 in so far as it picks one theory; 7.37 in so far as it fixes one label for the output — its stated purpose belongs to *the measurement of the analysis* |
| 7.33(ii), 7.68(i) (2) | phrase ends, Ruling 1 (§2, documentation) | recorded as overtaken by the charter and Ruling 48 |
| 7.34 | sections, the ruling's documentation paragraph | recorded as overtaken by item (3) of that ruling |
| 7.336 | phrase ends §2 (carried) → cadence placement, Ruling 2 item e | D-495's flat-profile fallback *"loses its subject at L3"*; the old fallback rule drops out |

11 + 6 + 4 + 1 + 1 + 4 + 3 + 2 + 1 + 1 = 34.

*Named in a record but NOT counted as reached on that naming:* Rows 7.100 and 7.102 to 7.106 appear in the cadence
features record §5 only in its list of rows read in passing (they are reached by the cadence type record, above). Row
7.96 appears in the cadence type record §0 only as a heading read.

### 1.2 Still open — 10 row-parts

Each read at its §6 entry in the reading file (line given). *The D-599 note* is this side's preliminary reading of
whether the record already settles the row; **it is not a placement**, and each is tested again at its sources on the
surface that carries it.

| Row-part (line) | Subject, in plain words | The D-599 note (preliminary) |
|---|---|---|
| 7.96 (4665) | The old authentic-cadence rule requires the leading tone to resolve to the tonic as an event; L3-S17's types read only L3-S16's six features, which hold no motion within a voice (DIFFERS). | **Left open by the record:** the cadence type surface §A.5 carries it *"UNSETTLED"* — a seventh feature would be needed, possibly from the voice-leading axis, which L3 does not read (L3-S42). A genuine choice is likely. |
| 7.110(ii) (4922) | A half cadence on an inverted or seventh dominant is admitted *"at lower weight"*. The reading file could not tell whether the weight is the cadence's vote for the tonic or its own confidence. | **Both readings look settled:** as confidence, cadence mass Ruling 1 (no fixed, by-rule lowering); as the vote, it follows Row 7.53, which the S38 first-cut record places QUARANTINED by derivation. Candidate derivation. Part (i) is reached (cadence type Ruling 3 item e). |
| 7.116(ii) (5028) | *"In the chorale corpus the fermata is the reliable marker"* of a phrase boundary; L3-S8 says no item of evidence forces or forbids a phrase end (DIFFERS). | **Looks settled:** phrase ends Ruling 1 decides against forcing markers; the fermata still enters as evidence. Candidate derivation — the same shape as the eight rows of §1A.2. Part (i) is ADOPTED — carried in the reading file. |
| 7.36 (3733) | *"No simplification"*: wherever the label standard defines a fuller label, emit it, never a reduced stand-in. Travels with 7.35. | **Possibly settled:** the display ruling's part A (display strings produced outside the analysis from published facts) and #12. To be tested; not certain. |
| 7.199 (6320) | The old function layer's contract to the grouping/display layer above it: the numeral, the cadence and key markers, the open mark. | **Possibly settled:** in the derivation the cadence and the grouping are one layer's facts, so there is no contract between them; the same shape as the rows the phrase-ends and sections records mark *"overtaken by the charter"*. To be tested. |
| 7.47 (3903) | Prolongational or Schenkerian reduction is out of scope. | **Not settled by any record found.** `FRAMEWORK.md` §5 names no charter for reduction (as the reading file reports; not read by this sitting). The four reduction rows go together; a genuine placement for the user is likely. |
| 7.48(i) (3918) | Reduction *"belongs to a later layer"*. Travels with 7.47. | As 7.47. Part (ii) is ADOPTED — carried in the reading file. |
| 7.294(v) (7712) | Among the old design's discarded options: prolongational reduction, *"a later layer"*. Travels with 7.47. | As 7.47. Parts (i) and (ii) are reached (display Ruling B; cadence features Ruling 1 item a). |
| 7.331 (8277) | *"Prolongation/reduction — explicitly a later layer, not this one."* Travels with 7.47. | As 7.47. |
| 7.85 (4494) | The named progressions and substitutions live in a catalog (the *Harmonic Vocabulary*); the layer never enumerates them. | **Not settled by any record found.** No charter names such a catalog — the same gap the cadence type record notes for Row 46.14. Belongs with member 46 (the progression dictionary, 32 UNPLACED rows), where the catalog question arises. |

**Count:** 34 reached + 10 open = 44, the member's total.

---

## 1A. Member 8 — `cowork_layer6_grouping_design.md` (62 row-parts)

The foot list (reading file line 11214): 8.4(i), 8.11(i), 8.11(ii), 8.14(ii), 8.16(i), 8.16(ii), 8.18, 8.21, 8.22, 8.24,
8.25, 8.26(i), 8.28(ii), 8.32, 8.33, 8.34, 8.35(ii), 8.36(i), 8.40(i), 8.40(ii), 8.42, 8.43, 8.47(ii), 8.49, 8.50, 8.51,
8.52(iii), 8.59(i), 8.59(ii), 8.60(i), 8.64, 8.65, 8.66, 8.68, 8.69, 8.70, 8.72, 8.77, 8.84(i), 8.86, 8.87, 8.88(i),
8.92, 8.93, 8.94, 8.95, 8.96(i), 8.96(ii), 8.97, 8.101(i), 8.101(ii), 8.105(ii), 8.109, 8.112, 8.113(i), 8.114(i), 8.115,
8.116(ii), 8.129(ii), 8.130, 8.140, 8.141.

Further record short names: **phrase units** = `…_2026_11_02_l3_phrase_units_sitting.md`; **edge of span** =
`…_2026_11_03_l3_edge_of_span_sitting.md`; **mass and status** = `…_2026_11_03_l3_mass_and_status_sitting.md`;
**boundaries** = `…_2026_11_03_l3_boundaries_sitting.md`.

### 1A.1 Reached by a ruling record, named by number — 44 row-parts

| Row-part | Record, place | What the record did |
|---|---|---|
| 8.4(i), 8.68, 8.69, 8.70, 8.72 (5) | phrase units, Ruling 1 (§2) | decided against (the codetta as an annexe; the phrase reading tiles with two kinds of unit) |
| 8.84(i) | phrase units, Ruling 2 item b (§2a) | derivation ratified: the cadential arrival not held to a fixed window |
| 8.24, 8.26(i), 8.95, 8.96(i), 8.97, 8.101(i), 8.105(ii), 8.112 (8) | phrase ends, Ruling 1 (§2, documentation) | recorded as overtaken by the charter and Ruling 48 (rows that place the phrase ends in an earlier layer or say the grouping layer detects nothing); 8.24's section side also in the sections record |
| 8.35(ii), 8.36(i), 8.113(i), 8.114(i), 8.115, 8.140, 8.141 (7) | sections, Ruling 1 (documentation) | recorded as overtaken by the charter (rows that put sections outside the layer) |
| 8.21, 8.22, 8.25, 8.34, 8.96(ii) (5) | sections, Ruling 2 (§3a) | decided against (the rows that call the grouping flat) |
| 8.64, 8.65 (2) | edge of span, Ruling 1 (§2) | decided against (the grouping layer only tags the edge and never acts on it) |
| 8.47(ii), 8.86, 8.116(ii), 8.129(ii), 8.130 (5) | cadence placement, Ruling 1 (§2) | decided against (the "internal cadence"; a cadence only at a decided phrase end) |
| 8.11(ii), 8.59(ii), 8.101(ii) (3) | cadence placement, Ruling 2 item a (§2a) | derivation ratified: the cadence is L3's, read off L2's decided chords at L3's decided phrase ends |
| 8.40(i) | cadence type, Ruling 1 | decided against in so far as the bass-derived inversion is the only criterion |
| 8.11(i), 8.59(i) (2) | cadence type, Ruling 2 | decided against in so far as they fix one list as the only one |
| 8.88(i) | cadence type, Ruling 3 item a | decided against (the type made by the old function layer and carried verbatim) |
| 8.40(ii) | cadence features, Ruling 1 item b | decided against in so far as it keeps the highest pitch's degree unpublished |
| 8.77 | mass and status, §2 item (d), ratified with Ruling 2 (§4b) | HISTORICAL — a rule replaced by L3-S34 (the contingency, L3-S34's ratification, met by Ruling 2) |
| 8.42, 8.109 (2) | boundaries, §2, ratified with Ruling 2 (§4b) | HISTORICAL — replaced by L3-S37 (8.109 also by mass-and-status Ruling 1) |

5 + 1 + 8 + 7 + 5 + 2 + 5 + 3 + 1 + 2 + 1 + 1 + 1 + 2 = 44.

**A stale carry found, Row 8.105(ii).** The phrase ends record (2026-11-02, §2) names 8.105(ii) among the rows recorded
as overtaken by the charter and Ruling 48. The architecture-rules record (2026-11-04, §1 part F and §2) and the
literature-facts surface (its line 164) carry the same row-part as UNPLACED, *"with tier item 14"*. The row's claim (ii)
is *"it stays a thin assembly and grows no detection of its own"* (reading file line 10440), DIFFERS with L3-S8 — the
shape the phrase-ends ruling names. On this side's reading the later records did not see the earlier naming; the row is
counted here as reached by the phrase-ends ruling. The later records' carry lines are not edited by this inventory.

*Named in a record but NOT counted as reached on that naming:* Row 8.32 appears in the key-areas record §6 only in its
list of rows read; Rows 8.26, 8.36, 8.96, 8.97, 8.113, 8.116, 8.140 also appear in the sections record's list of rows read
(each is reached elsewhere, above).

### 1A.2 Reached in substance by a ruling's wording, but not named by number — 8 row-parts

Each DIFFERS with L3-S8 on the same point: the old design has the phrase boundaries chosen upstream, by the
phrase-boundary primitive's picked peaks, and the grouping layer only consuming them. Phrase-ends Ruling 1 (2026-11-02)
decides that *"the phrase reading is an L3 decision"* over every candidate position, records as overtaken *"the rows of
the L3-S8 family that only place the phrase ends in an earlier layer or say the grouping layer detects nothing (among
them …)"*, and says *"The method rows (peak-picking, forcing markers …) are the rows Ruling 1 decides against"*. The
words *"among them"* make that list open; these rows fit its description but are not in it. **Candidate derivations —
to be confirmed by number on a surface, not asked as a choice.**

| Row-part (line) | Subject, in plain words |
|---|---|
| 8.14(ii) (8906) | The grouping unit's boundaries are the notated punctuation, delimited through the primitive. (Part (ii) also AGREES with L3-S10.) |
| 8.16(i) (8959) | A boundary is a tick where the primitive places a picked peak. |
| 8.16(ii) (8959) | Choosing which ticks are boundaries is the primitive's job, upstream. |
| 8.28(ii) (9165) | The spans are delimited by the primitive. |
| 8.43 (9424) | The grouping consumes the primitive's boundary ticks and strengths, local maxima picked as boundaries. |
| 8.60(i) (9696) | The span is partitioned at the primitive's ticks. |
| 8.66 (9799) | The grouping consumes the primitive's picked peaks as they are and never re-detects. |
| 8.87 (10159) | An internal cadence is recorded, not resolved, because the boundary and the cadence are decided upstream. Also reached in substance by cadence-placement Ruling 1, which drops the "internal cadence". |

### 1A.3 Still open — 10 row-parts: recognised progression schemas

All ten carry the same reading-file ground (*"read as at Row 8.18"*): *"the derivation names no recognised progression
schema, and none of `FRAMEWORK.md` §5's charters names the recognition of one or the span it covers"*. No ruling record
or `cowork_l3_*` surface was found naming any of them.

| Row-part (line) | Subject, in plain words |
|---|---|
| 8.18 (8995) | Glossary: a progression-schema span is a recognised schema's span, emitted by a recognition consumer and hosted by the grouping. |
| 8.32 (9231) | The recognised-schema spans are hosted as cross-cutting labels. |
| 8.33 (9246) | The grouping is the schemas' annotation home and recognises none. |
| 8.49 (9528) | The recognised-schema spans are produced. |
| 8.50 (9543) | A schema span cuts across the phrase spans. |
| 8.51 (9556) | The schema spans are read-only and additive, produced by the consumer. |
| 8.52(iii) (9569) | A schema span may straddle a phrase boundary. |
| 8.92 (10240) | Each recognised schema span is carried verbatim and exposed as a cross-cutting label. |
| 8.93 (10255) | The grouping recognises no schema; it hosts the result. |
| 8.94 (10269) | Without the consumer, the schema output is empty. |

**A cluster across members.** The same ground (*"read as at Row 8.18"*) is given at ten further UNPLACED proposals in
the reading file's member 44 (`cowork_progression_schema_design.md`, lines 61110 to 62010; inventoried at §1D, group B).
*(Former wording, kept (#12): "eight further UNPLACED proposals in the reading file's member 44
(`cowork_progression_schema_design.md`, lines 61110 to 61886, found by search, not yet inventoried)". Corrected by the
sitting that booted on entry 524: a search for the phrase finds nine in that range and a tenth at line 62010, Row
44.50 (iii).)* The question these rows share — whether recognised progression schemas belong to any charter, and if not
how their rows are placed — looks like one family, together with Row 7.85 (the named-progression catalog, §1.2) and
Row 46.14 (the cadence type record: *"no charter names its catalog"*). This is this side's reading, to be settled when
members 44 and 46 are inventoried.

**Count:** 44 + 8 + 10 = 62, the member's total.

---

## 1B. Member 36 — `cowork_phrase_boundary_design.md` (44 row-parts)

*Added by the Cowork sitting of 2026-11-04 that booted on entry 523.*

The foot list (reading file line 43007): 36.4(i), 36.4(ii), 36.6(ii), 36.10(ii), 36.11(ii), 36.12(ii), 36.14(iii),
36.16(i), 36.21, 36.36(i), 36.37(ii), 36.37(iii), 36.38(ii), 36.40(i), 36.45(ii), 36.48(ii), 36.58(i), 36.60(i),
36.60(ii), 36.61, 36.63, 36.64, 36.65, 36.74(i), 36.76(ii), 36.77(ii), 36.78(ii), 36.79(ii), 36.80(ii), 36.81(ii), 36.82,
36.86(ii), 36.91(i), 36.94(iii), 36.109(i), 36.111(ii), 36.113(i), 36.113(ii), 36.115(ii), 36.124, 36.125(ii),
36.130(i), 36.133(ii), 36.146.

Further record short names: **S38 ratification** = `…_2026_11_03_l3_s38_ratification_sitting.md`; **architecture
rules** = `…_2026_11_04_l3_architecture_rules_sitting.md`; **literature facts** =
`…_2026_11_04_l3_literature_facts_sitting.md`; **fit and rest** = `…_2026_11_04_l3_fit_and_rest_sitting.md`.

### 1B.1 Reached by a ruling record — 18 row-parts

| Row-part | Record, place | What the record did |
|---|---|---|
| 36.21, 36.38(ii), 36.40(i), 36.86(ii), 36.109(i) (5) | phrase ends, Ruling 1 (§2, documentation) | recorded as overtaken by the charter and Ruling 48 |
| 36.6(ii), 36.12(ii), 36.14(iii), 36.58(i), 36.133(ii) (5) | phrase ends §2 (*"Ruling 1 settles their phrase side only"*; cadence side carried) → cadence placement, Ruling 2 item d (§2a) | derivation ratified: the cadence is read at L3's decided phrase ends, *"not at a gate fed by peaks picked from the page"* |
| 36.10(ii), 36.113(ii) (2) | phrase units, Ruling 1 (§2) | decided against (the next phrase's start *"not separately marked"*) |
| 36.63 | phrase units, Ruling 2 item a (§2a) | derivation ratified: the phrase end is where L3 decides it, not at a picked peak |
| 36.74(i), 36.146 (2) | phrase units, Ruling 2 item c (§2a) | derivation ratified: the phrase-length term is in the model from the start as a fitted weight |
| 36.36(i), 36.130(i) (2) | cadence features, Ruling 1 item b (§2) | decided against *"in so far as they keep the fact unpublished"* (the highest sounding pitch's degree at the arrival) |
| 36.111(ii) | S38 ratification, Ruling 1 (§1), which ratifies *"the 100 DIFFERS as the eight cuts file them"* → the fifth-cut surface §3 (`cowork_l3_s38_fifth_cut_surface_2026_11_03.md`) | HISTORICAL — the old design's cadence as *"a means to key"* is the superseded route of nothing-from-L3 Ruling 2 (2026-10-07); the record reaches the row through the cut it ratifies, not by naming it |

5 + 5 + 2 + 1 + 2 + 2 + 1 = 18.

**A stale carry found, Row 36.111(ii)** — the same shape as Row 8.105(ii) in §1A.1. The fifth-cut surface (2026-11-03)
filed the row HISTORICAL, and the S38 ratification record of the same day ratified that filing. The architecture-rules
record (2026-11-04, §1 part F: *"Claims (ii) of both rows (UNPLACED) stay with tier item 14"*, and §2), the
literature-facts record (its line 57) and the literature-facts surface (its line 164) still carry the row-part as UNPLACED.
On this side's reading the later records did not see the earlier filing. The row is counted here as reached. The later
records' carry lines are not edited by this inventory.

*Named in a record but NOT counted as reached on that naming:* Rows 36.4 and 36.65 appear in the phrase-ends record only
in its list of rows read at §6 (§2 and §5). Rows 36.4(i), 36.4(ii), 36.16(i), 36.81(ii) and 36.94(iii) appear in the
fit-and-rest third-cut surface §2, and the fit-and-rest record §1 says such claims *"are not placed by this ruling"*.

### 1B.2 Reached in substance by phrase-ends Ruling 1's wording, but not named by number — 26 row-parts

Each DIFFERS with L3-S8 (*"No item of evidence forces or forbids a phrase end"*, or *"publishes the principal partition
with its rivals and their mass"*). Phrase-ends Ruling 1 (2026-11-02) decides L3-S8 as derived. It names what it
supersedes: **D-478** *"at its L3 home, as a rule deciding a phrase end"*, and **D-481** *"at its L3 home: no marker is a
phrase end unconditionally"*. It also says *"The method rows (peak-picking, forcing markers, the primitive's worked
examples) are the rows Ruling 1 decides against."* That sentence names kinds of row, not rows; these 26 fit its
description and are not named in it. **Candidate derivations — to be confirmed by number on a surface, not asked as a
choice.**

**(a) Peak-picking: the primitive's picked peak taken as the phrase end — 14**

| Row-part (line) | Subject, in plain words |
|---|---|
| 36.4(i) (39932) | Terms table: a phrase boundary is a tick where the surface marks a phrase end. |
| 36.4(ii) (39932) | Terms table: the primitive's picked boundary is the cue that delimits the grouping layer's span. |
| 36.11(ii) (40074) | The picked boundary ticks and the "ends a phrase" region flag are derived from the profile. |
| 36.16(i) (40177) | The picked boundary delimits the grouping layer's span. |
| 36.37(ii) (40633) | Product: the picked ticks, the peaks of the texture profile. |
| 36.37(iii) (40633) | Product: a region "ends a phrase" when a picked tick falls within it. |
| 36.60(ii) (41063) | Only the surface-cue strength is peak-picked. Inside D-481's home. |
| 36.61 (41094) | Surface picking: a local maximum above the whole-profile mean plus k standard deviations. |
| 36.64 (41150) | A region ends a phrase when a picked tick falls within it. |
| 36.91(i) (41699) | The boundary is a peak in a continuous strength profile. Inside D-478's home. |
| 36.94(iii) (41770) | The texture boundaries the primitive picks are exposed. Inside D-479's home (see the note below). |
| 36.113(i) (42149) | Glossary: a phrase boundary is a tick picked as a peak of the profile. |
| 36.115(ii) (42186) | Glossary: the texture profile is what the cadence gate consumes and peak-picking runs on. |
| 36.124 (42329) | Glossary: peak-picking selects the local maxima above the adaptive threshold as boundaries. |

**(b) Forcing markers: a notated marker makes a phrase end by rule — 5**

| Row-part (line) | Subject, in plain words |
|---|---|
| 36.45(ii) (40791) | Each marker adds a fixed spike above any surface strength, so it dominates wherever it occurs. |
| 36.48(ii) (40851) | A double, final or repeat bar line is treated as a phrase boundary. |
| 36.60(i) (41063) | The picked set is the surface peaks together with every marker, the markers emitted unconditionally. Inside D-481's home. |
| 36.65 (41167) | The score's last bar line ends the last region's phrase automatically. |
| 36.125(ii) (42348) | Glossary: the large fixed strength added at each marker. |

**(c) The primitive's worked examples (its §5 scenarios), each ending in a boundary or none read off the profile — 7**

| Row-part (line) | Subject, in plain words |
|---|---|
| 36.76(ii) (41394) | Chorale phrase end: a high-strength picked boundary. |
| 36.77(ii) (41416) | A rest with no fermata: a boundary. |
| 36.78(ii) (41438) | Lengthening without a rest: a moderate-strength boundary. |
| 36.79(ii) (41460) | A section break: a double bar line spikes the profile, a boundary. |
| 36.80(ii) (41480) | A passing leap does not clear the threshold: no boundary. |
| 36.81(ii) (41501) | One voice phrasing alone: no texture boundary reported. |
| 36.82 (41524) | The cadence gate, reading the texture profile, sees no whole-texture phrase end. |

14 + 5 + 7 = 26.

**Notes for the surface that carries these rows.**
1. **Row 36.94(iii) and D-479.** The row lies inside D-479's home (*"BOTH the per-voice and the texture boundaries are
   published"*, as the reading file relays it at the row). The phrase-ends record names D-479 only inside the range
   *"D-476 to D-485"*; it states no supersession for it, as it does for D-478 and D-481. Claim (iii) concerns the texture
   boundaries the primitive picks, which is the peak-picked boundary Ruling 1 replaces. Whether D-479 needs a
   supersession statement of its own at L3 is for that surface to state.
2. **Row 36.65** is also met by L3-S8's *"both span edges are candidate phrase ends"*, and by phrase-units Ruling 1: a
   stretch after the last phrase (a codetta) is a unit of its own, so the music's last unit need not be a phrase.
3. **Row 36.82** is also met in substance by cadence-placement Ruling 2 item d (no cadence gate fed by picked peaks).
4. The reading file grounds most of these rows *"as Rows 7.68 (i), 8.16 and 19.41"*. Row 7.68(i) is reached by number
   (§1, phrase ends Ruling 1); Row 8.16 is a candidate derivation of the same kind (§1A.2); Row 19.41 belongs to member
   19, not yet inventoried.

### 1B.3 Still open — none

In the records and surfaces §0's method searches, every row-part of member 36 met a record that reaches it, by number
(§1B.1) or in substance (§1B.2).

**Count:** 18 + 26 + 0 = 44, the member's total.

---

## 1C. Member 46 — `cowork_progression_schema_dictionary.md` (32 row-parts)

*Added by the Cowork sitting of 2026-11-04 that booted on entry 523.*

The foot list (reading file line 64462): 46.1(i), 46.8(ii), 46.14, 46.16, 46.17, 46.18(i), 46.18(ii), 46.19(i),
46.19(iii), 46.20, 46.21(ii), 46.23, 46.24, 46.25, 46.26, 46.27, 46.28, 46.29, 46.30, 46.31, 46.32, 46.33, 46.34,
46.35(i), 46.37, 46.38, 46.40, 46.43, 46.44(i), 46.45, 46.46(i), 46.49.

The document is the old design's catalog of named progressions, substitutions and schemas, *"knowledge and not a tool
that acts"* (the reading file's manifest for the member, line 63347). Searched as §0 states: of this member's UNPLACED
rows, only Row 46.14 is named in the records and surfaces, in the cadence type record and its surface. (The fit-and-rest
surface names a Row 46.12, but of the L2 reading file, not this member.)

### 1C.1 Reached by a ruling record — none

**Row 46.14** (line 63750; the catalog's cadential entries: authentic, *"perfect/imperfect by inversion"*, half,
deceptive, plagal, Phrygian half) is named by the cadence type record twice: Ruling 1 reads its inversion clause *"the
same way"* as the rows decided against in so far as they make the bass the only criterion; Ruling 2 records it as
decided against *"in so far as they fix one list as the only one"*. The same paragraph then says: *"Row 46.14's
reading-file proposal stays UNPLACED as the surface states (no charter names its catalog)."* The record therefore leaves
the row open, and it is counted open here (§1C.2, group E).

### 1C.2 Still open — 32 row-parts, in five groups by the reading file's own ground

Each was read at its §6 entry (line given). Every one is graded THE DERIVATION IS SILENT except Row 46.14 (DIFFERS with
L3-S17). Every ground is the same kind of gap: **`FRAMEWORK.md` §5 names no charter for the subject** (as the reading
file reports; `FRAMEWORK.md` not read by this sitting).

**(A) Entries of the catalog of named progressions — ground *"read as at Row 7.85"* or *"as at Row 44.1"*: no charter
names a catalog of named progressions — 12**

| Row-part (line) | Subject, in plain words |
|---|---|
| 46.1(i) (63496) | The catalog owns the named progressions and substitutions. Inside D-406's home (LIVE, as relayed at the row). |
| 46.8(ii) (63638) | The catalog owns only the named progressions. |
| 46.16 (63787) | The ii–V family as entries; the incomplete ii–V a unit of its own. |
| 46.17 (63802) | The turnarounds as entries. |
| 46.18(i) (63819) | The sequence entries (circle of fifths, descending thirds, galant step sequences). |
| 46.19(i) (63849) | The bass-line and pop loops as entries (lament bass, Andalusian, doo-wop, Axis, Pachelbel). |
| 46.20 (63884) | The galant schemata as entries, each held by its harmonic pattern. |
| 46.21(ii) (63904) | The catalog holds only a galant schema's harmonic pattern. |
| 46.23 (63939) | The advanced jazz cycles as entries. |
| 46.37 (64156) | Every entry usable in both directions, analysis and composition. |
| 46.45 (64285) | One catalog, not one per style; a shared convention is a single entry. |
| 46.46(i) (64300) | The catalog holds structural content and returns ranked structural matches. |

**(B) Recognition of a schema in the music — ground *"read as at Row 8.18"* (or Row 44.1 for the recognition
consumer): no charter names the recognition of one or the span it covers — 3**

| Row-part (line) | Subject, in plain words |
|---|---|
| 46.18(ii) (63819) | Recognition rules: a realisation may enter the circle of fifths at any member; the descending thirds may be continued. |
| 46.19(iii) (63849) | The Axis loop's other rotations admitted as rotation-tolerant matching on its one entry. Inside D-411's home (DEFERRED, as relayed at the row). |
| 46.43 (64249) | Style behaviour belongs to the consumer — the old recognition consumer. |

**(C) Substitution, the relation of a chord to the chord it stands in for — ground *"read as at Row 44.4"* or
*"travelling with Row 46.24"*: no charter names that relation — 12**

| Row-part (line) | Subject, in plain words |
|---|---|
| 46.24 (63954) | Substitution operates on every functional family, not on the dominant alone. |
| 46.25 (63969) | The tonic, pre-dominant and dominant families each have substitutes. |
| 46.26 (63984) | Only the tritone substitution is dominant-specific, and it applies to a dominant of any degree. |
| 46.27 (63999) | Each operation: analysis recognises the substituted surface as the function; composition offers it. |
| 46.28 (64015) | The operation: secondary dominant or tonicization. |
| 46.29 (64030) | The operation: the related ii–V. |
| 46.30 (64044) | The operation: tritone substitution. |
| 46.31 (64059) | The operation: diatonic, same-function substitution. |
| 46.32 (64074) | The operation: modal interchange. |
| 46.33 (64088) | The operation: the diminished approach chord. |
| 46.34 (64102) | The operation: the deceptive resolution (a substitution of the chord a dominant resolves to, not a cadence type). |
| 46.35(i) (64117) | The line cliché, held by its harmonic pattern. |

**(D) Style tags carried by the catalog's entries — ground *"read as at Row 44.11"*: the tags are attributes of the
catalog's entries — 4**

| Row-part (line) | Subject, in plain words |
|---|---|
| 46.38 (64172) | Entries tagged from the one style vocabulary the presets also select on. |
| 46.40 (64209) | The tags are multi-valued. |
| 46.44(i) (64263) | The catalog carries the style label; the preset selects the active subset. |
| 46.49 (64350) | The tags are multi-valued; an entry can carry several idioms. |

**(E) The catalog's cadential entries — 1**

| Row-part (line) | Subject, in plain words |
|---|---|
| 46.14 (63750) | The cadential entries (§1C.1). Its cadence types are L3's subject, already decided at L3-S17 (cadence type Rulings 1 and 2); what stays open is the catalog record that lists them. |

12 + 3 + 12 + 4 + 1 = 32.

**The D-599 note (preliminary, not a placement).** No record found settles any of the five groups. All rest on one
question: **does a catalog of named progressions, substitutions and schemas, and the recognition of them in the music,
belong to any charter — and if none, how are its rows placed?** On this side's reading that is one family, together with
Row 7.85 (§1.2), the ten schema rows of member 8 (§1A.3) and the ten member-44 rows grounded *"as at Row 8.18"*
(§1A.3's cluster note; §1D group B). *(Former wording, kept (#12): "the eight member-44 rows"; corrected by the sitting
that booted on entry 525, after §1A.3's own count was corrected to ten.)* Groups C and D hang on groups A and B: a substitution operation and a style tag are attributes of
catalog entries. **A genuine placement for the user is likely.** One link for the surface that carries it: the
nothing-from-L3 record of 2026-10-07 (Ruling 2, as the S38 fifth-cut surface quotes it whole) leaves open, as DP-O,
*"whether L2 should see"* a progression longer than two chords *"whole"* — the same subject seen from L2.

**Count:** 0 reached + 32 open = 32, the member's total.

---

## 1D. Member 44 — `cowork_progression_schema_design.md` (22 row-parts)

*Added by the Cowork sitting of 2026-11-04 that booted on entry 524.*

The foot list (reading file line 62144): 44.1, 44.2, 44.4, 44.10 (i), 44.11, 44.16, 44.19 (iii), 44.20 (i), 44.20 (ii),
44.21, 44.28 (ii), 44.32 (i), 44.33 (i), 44.34 (i), 44.34 (ii), 44.35, 44.36 (i), 44.37 (i), 44.39, 44.44, 44.45,
44.50 (iii).

The document is the old design of the consumer that recognises named progressions in the committed chords and reports
them as evidence to the function layer and as a named span to the grouping layer; its catalog is member 46's.

### 1D.1 Reached by a ruling record — none

Searched as §0 states, every row number with and without the space before its part. No row of this member is named in
the L3 ruling records or the `cowork_l3_*` surfaces. The only hits, in the harmonic-rhythm record (lines 45 and 71:
Rows 44.27 (ii), 44.33 (ii), 44.50 (vi), 44.76 (iii)), are rows of the **L2** reading file, placed by the L2
nothing-from-L3 Ruling 4; Rows 44.50 (vi) and 44.76 (iii) do not exist in this member, which ends at Row 44.50 (v).

A search of the same records and surfaces for the subject words (*schema*, *catalog*, *Harmonic Vocabulary*, *named
progression*, *substitution*, *knowledge base*, *latent*, *typology*, *span type*, *new layer*, *additive*, *read-only*,
*cross-cut*) found no ruling that takes up the recognition of a named progression, its catalog or its span. The
cadence type record's line 66 (Row 46.14, §1C) and its surface's line 95 say only that no charter names the catalog.

### 1D.2 Still open — 22 row-parts, in five groups by the reading file's own ground

Each was read at its §6 entry (line given). Every one is graded THE DERIVATION IS SILENT. Every ground is the same kind
of gap: **`FRAMEWORK.md` §5 names no charter for the subject** (as the reading file reports; `FRAMEWORK.md` not read by
this sitting).

**(A) The catalog of named progressions — ground *"read as at Row 7.85"* or *"travelling with Row 44.1"* — 3**

| Row-part (line) | Subject, in plain words |
|---|---|
| 44.1 (60929) | Terms: a named progression is a progression with a conventional name and an entry in the catalog. |
| 44.2 (60946) | Terms: a member is one chord position in a catalog entry, fixing the degree and quality a chord must have to fill it. |
| 44.39 (61739) | The named progressions and substitutions are owned by the catalog, which is queried as knowledge (the member's D5). |

**(B) Recognising a named progression in the music, and the span it covers — ground *"read as at Row 8.18"* (10) or
*"as at Row 8.52 (iii)"* / *"as at Row 8.51"* (3) — 13**

| Row-part (line) | Subject, in plain words |
|---|---|
| 44.10 (i) (61095) | Terms: the match score is the catalog's value for "this stretch of the chords realises this entry". |
| 44.16 (61200) | Terms: the progression-schema span is the span a recognised named progression covers, emitted for the grouping layer. |
| 44.28 (ii) (61479) | A single internally sequential entry (circle of fifths, Monte, Fonte) carries its key motion in its span, not as a separate sequence. Inside the homes of D-504 and D-505 (LIVE, as relayed at the row). |
| 44.33 (i) (61631) | The matcher is the same for every idiom. |
| 44.34 (i) (61650) | The member's D1: recognition yields evidence and a name. |
| 44.35 (61666) | The member's D2: recognition looks at chords only. |
| 44.36 (i) (61681) | The member's D3: only exact matches for now. |
| 44.44 (61851) | The member's D6: the span is named *progression-schema span*. Inside D-502's home (LIVE, as relayed at the row). |
| 44.45 (61875) | Not a new kind of span: the old span typology's never-used "sequence span", now instantiated. |
| 44.50 (iii) (61980) | Audit: the span cuts across the punctuation spans; one owner per concern, no second matcher; the catalog makes no decisions; no layer added. |
| 44.20 (i) (61276) | The name goes to the grouping layer as a span cutting across the punctuation spans (as at Row 8.52 (iii)). |
| 44.20 (ii) (61276) | That span is read-only and additive (as at Row 8.51). |
| 44.37 (i) (61699) | The member's D4: recognition is additive (as at Row 8.51). Inside D-506's home (LIVE, as relayed at the row). |

**(C) Substitution — ground: the catalog's mappings, read as at Row 7.85; no charter names the relation of a chord to the
chord it stands in for — 1**

| Row-part (line) | Subject, in plain words |
|---|---|
| 44.4 (60980) | Terms: a substitution is a chord standing in for another of the same function, by the catalog's mappings (the tritone substitution the standard case). |

**(D) Style tags on the catalog's entries — ground *"travelling with Row 44.1"* or *"with Row 44.11"* — 2**

| Row-part (line) | Subject, in plain words |
|---|---|
| 44.11 (61117) | Terms: the five idiom tags and their cross-attributes on every catalog entry. |
| 44.32 (i) (61611) | The catalog carries the idiom tags. (Part (ii), the idiom weights, is RELOCATED to L2.) |

**(E) No layer for the recognition, and the catalog as a knowledge base — ground *"read as at Row 38.20 (i)"* or
*"beside"* it, or *"travelling with Row 44.19 (iii)"* — 3**

| Row-part (line) | Subject, in plain words |
|---|---|
| 44.19 (iii) (61252) | No stage is added for the recognition. (Parts (i) and (ii) are RELOCATED to L2.) |
| 44.34 (ii) (61650) | The member's D1: recognition adds no new layer. |
| 44.21 (61293) | The catalog lives in the Harmonic Vocabulary, queried and not owned: no charter, nor `FRAMEWORK.md` §5's NOT A LAYER items, names a knowledge-base component. |

3 + 13 + 1 + 2 + 3 = 22.

**The D-599 note (preliminary, not a placement).** No record found settles any of the five groups. They rest on the
question §1C names: **does a catalog of named progressions, substitutions and schemas, and the recognition of them in
the music, belong to any charter — and if none, how are its rows placed?** Member 44 is the design of the recognition
itself, so its groups A, C and D are the catalog side of §1C and its group B is the recognition side of member 8's ten
schema rows (§1A.3). Group E hangs on the same answer: whether a recognition exists at all, and where its knowledge
lives. Group E's ground, Row 38.20 (i), belongs to member 38 and is open there (§1F.4 group A). *(Former wording, kept
(#12): "Group E's ground, Row 38.20 (i), belongs to member 38, not yet inventoried.")* **A genuine placement for the user
is likely**, one family with §1C, §1A.3 and Row 7.85.

**Notes for the surface that carries these rows.**
1. **If the recognised span is placed in L3**, two parts of the span-kinds Ruling 1 (2026-11-04) bear on group B: part A
   (each kind of span named by what bounds it, D-028) and part C (the specification states, for each pair of kinds,
   whether they nest or cut across). That ruling lists the kinds it covers, and a progression span is not among them.
   This is a bearing, not a reach.
2. **Register homes, as relayed at the rows:** D-502 (Row 44.44), D-504 and D-505 (Row 44.28), D-506 (Row 44.37), each
   LIVE in group M with no entry ratification shown. Not opened by this sitting.

**Count:** 0 reached + 22 open = 22, the member's total.

---

## 1E. Member 19 — `ARCHITECTURE.md`, *2. Architectural Principles* (21 row-parts)

*Added by the Cowork sitting of 2026-11-04 that booted on entry 524.*

The foot list (reading file line 25397): 19.30(ii), 19.31(ii), 19.38(iii), 19.38(v), 19.38(vi), 19.39(ii), 19.39(v), 19.41,
19.56(i), 19.57(i), 19.57(ii), 19.58(iii), 19.59(i), 19.59(iv), 19.65, 19.66(i), 19.66(ii), 19.67, 19.68, 19.69, 19.70.

### 1E.1 Reached by a ruling record — 6 row-parts

| Row-part | Record, place | What the record did |
|---|---|---|
| 19.30(ii), 19.31(ii), 19.58(iii) (3) | phrase ends, Ruling 1 (documentation, line 84), for their phrase side; sections, Ruling 1 (documentation, lines 63–64), for their section side | recorded as overtaken by the charter (rows that say coarser groupings are derived views, or that the grouping layer decides nothing) |
| 19.59(iv) | sections, Ruling 1 (documentation, line 63) | recorded as overtaken by the charter (sections anticipated *"above"* the grouping layer, deferred) |
| 19.38(iii) | sections, Ruling 2 (line 113) | decided against (the punctuation span as *"the flat"* grouping span) |
| 19.38(v) | S38 ratification, Ruling 1 (line 33), which ratifies *"the 100 DIFFERS as the eight cuts file them"* → the third-cut surface §3 D (`cowork_l3_s38_third_cut_surface_2026_11_03.md`, lines 87–101) | HISTORICAL — *"one cadence detector feeds both grouping and key"* is a superseded plan on both halves; the record reaches the row through the cut it ratifies, as with Row 36.111(ii) (§1B.1) |

3 + 1 + 1 + 1 = 6.

*Note on Row 19.31(ii).* Its claim names *"phrases, key-areas, and sections"* as groupings derived from the per-slice
analysis. The reading file grades it only against L3-S8 and L3-S22, and the two records above reach its phrase and
section sides. Its key-area side is not judged here (§0, *"What 'reached' does not mean"*).

*Named in a record but NOT counted as reached on that naming:* Rows 19.30 to 19.32, 19.38 to 19.44, 19.58 and 19.59
appear in the sections record's list of rows read (line 214); Row 19.38 in the span-kinds record (line 35: *"Row 19.38 keeps its own
placements"*); Rows 19.59(i) and 19.59(iv) in the fit-and-rest third-cut surface §2 (lines 61–65), which the fit-and-rest
record §1 (line 66) says *"are not placed by this ruling"*.

### 1E.2 Reached in substance by phrase-ends Ruling 1's wording, but not named by number — 1 row-part

| Row-part (line) | Subject, in plain words |
|---|---|
| 19.41 (24527) | The cue that delimits the grouping span is supplied upstream, by the phrase-boundary primitive. DIFFERS with L3-S8 (*"No item of evidence forces or forbids a phrase end"*). |

It fits both descriptions in phrase-ends Ruling 1's documentation paragraph (lines 82–87): *"the rows of the L3-S8 family
that only place the phrase ends in an earlier layer"* (a list it opens with *"among them"*) and *"The method rows
(peak-picking, forcing markers …)"*. **A candidate derivation — to be confirmed by number on a surface, not asked as a
choice.** It is the same shape as the eight rows of §1A.2 and the 26 of §1B.2, whose reading-file ground often cites it
(§1B.2 note 4).

### 1E.3 Still open — 14 row-parts, in three groups

Each was read at its §6 entry (line given).

**(A) The progression-schema span — 2.** Ground: *"as at Row 8.18"*, or travelling with Row 19.38(vi). THE DERIVATION IS
SILENT.

| Row-part (line) | Subject, in plain words |
|---|---|
| 19.38(vi) (24447) | The progression-schema span is emitted by the recognition consumer and hosted by the grouping layer. |
| 19.39(v) (24490) | Progression-schema spans cut across both key spans and punctuation spans. |

These belong to the catalog-and-recognition family of §1C, §1D and §1A.3.

**(B) Whether a chord span always lies inside one grouping span — 1.** Ground: *"read: the two texts above"*. DIFFERS
with L3-S8.

| Row-part (line) | Subject, in plain words |
|---|---|
| 19.39(ii) (24490) | Chord spans nest inside punctuation spans. L3-S8: *"Every change point and both span edges are candidate phrase ends"* — a change point is not only a boundary of L2's spans. |

**Named as open by two records**: span-kinds Ruling 1 part C (*"whether a phrase end may fall inside a harmonic span
is NOT decided by this ruling — Row 19.39 (ii), UNPLACED, tier item 14's"*; §2 there) and architecture-rules §2. A
genuine choice is possible. The surface should test first whether L3-S8's wording, ratified with phrase-ends Ruling 1,
already answers it.

**(C) Rules of the framework's decomposition as a whole — 11.** Ground: *"read: the outgoing sentence; a rule of the
framework's decomposition, which names no single charter"* (Row 19.56(i)), the others *"as at Row 19.56 (i)"* or
travelling with Row 19.66. THE DERIVATION IS SILENT at each.

| Row-part (line) | Subject, in plain words |
|---|---|
| 19.56(i) (24761) | Each layer owns one contribution of one evidence source to one question, with what it does not own stated. |
| 19.57(i) (24785) | The layers are not one homogeneous stack. |
| 19.57(ii) (24785) | Their count is not a cap. |
| 19.59(i) (24825) | Six is the current decomposition of the harmonic spine, not a ceiling. |
| 19.65 (24935) | Growth is by axis and by component, not by climbing a fixed tower. |
| 19.66(i) (24949) | A new layer or axis is admitted only when it clears three gates. |
| 19.66(ii) (24949) | The three gates are co-equal and all required. |
| 19.67 (24964) | Gate 1: separation of concerns, sufficient on its own. |
| 19.68 (24978) | Gate 2: verifiability. |
| 19.69 (24991) | Gate 3: proportionality. |
| 19.70 (25005) | Gate 1 is not subordinate to the other two. |

**The D-599 note (preliminary, not a placement).** Two of these rows lie in the homes of LIVE register entries (the
reading file's list of homes, line 25432; titles read at `DECISIONS.md`): **D-033** (line 263, LIVE): *"Each layer owns
one evidence-source-times-question contribution and uses all of L1's information"*, home of Row 19.56; **D-034** (line
264, LIVE): *"A new layer or axis is admitted only through three co-equal gates"*, home of Row 19.66, with Rows 19.67 to
19.70 travelling with it. The architecture-rules Ruling 1 (2026-11-04) adopted other rows of this member *"applied to
L3"* on their register homes, among them Row 19.56(iii) on D-033 (part C). So Row 19.56(i), and Row 19.66 with its
four travelling rows, may be candidate derivations on the same precedent. **To be tested; not certain.** These rows speak
of the whole stack of layers, not of L3's subject. Whether a rule about all layers is placed at L3 at all is part of the
question, and so is how it relates to `FRAMEWORK.md`, whose banner says *"the decomposition, charters and boundary
contracts govern"* (relayed through the sections record, line 36; `FRAMEWORK.md` not read by this sitting). Rows 19.57 and
19.65 have no register home in the member's list. Row 19.59 lies in the home of **D-085** (line 432, LIVE: *"The
voice-leading axis is a separate axis with its own layers"*), whose title speaks to the row's claim (ii), not to claim (i).

3 groups: 2 + 1 + 11 = 14.

**Count:** 6 reached by number + 1 reached in substance + 14 open = 21, the member's total.

---

## 1F. Member 38 — `cowork_target_architecture.md` (21 row-parts)

*Added by the Cowork sitting of 2026-11-04 that booted on entry 525.*

The foot list (reading file line 48706): 38.1 (ii), 38.11 (i), 38.18 (i), 38.20 (i), 38.20 (ii), 38.21 (i), 38.21 (ii),
38.22 (i), 38.22 (ii), 38.26 (i), 38.50, 38.71, 38.76, 38.77 (ii), 38.78, 38.79 (i), 38.79 (ii), 38.80 (i), 38.80 (ii),
38.81 (ii), 38.82.

The reading file's marks for the member (line 48732): no decision of the register is homed in this document (it was
retired as a home document on 2026-08-08). So none of these rows lies in a register home.

### 1F.1 Reached by a ruling record — 3 row-parts

| Row-part | Record, place | What the record did |
|---|---|---|
| 38.1 (ii) | phrase ends, Ruling 1 (documentation, line 85) | recorded as overtaken by the charter and Ruling 48 (*"everything coarser a derived view"*); the same content as Row 19.30 (ii), §1E.1 |
| 38.26 (i) | cadence type, Ruling 3 item a (line 82) | derivation ratified: *"Rows 8.88 (i) and 38.26 (i) recorded as decided against"* (*"A cadence is a V→I"*) |
| 38.76 | S38 ratification, Ruling 1 (line 33), which ratifies *"the 100 DIFFERS as the eight cuts file them"* → the sixth-cut surface §3 E (`cowork_l3_s38_sixth_cut_surface_2026_11_03.md`, lines 118–124) | HISTORICAL — the cadence as *"a key confirmation — the reason one detector feeds both"*, filed as the third cut filed Row 19.38 (v); the record reaches the row through the cut it ratifies, as with Rows 19.38 (v) and 36.111 (ii) |

1 + 1 + 1 = 3.

*Named in a record but NOT counted as reached on that naming:* Row 38.76 appears in the third-cut surface (lines 102 and
124) only as a bearing and in its list of rows read; Row 38.26 in the cadence type record's list of rows read (line 17);
Rows 38.77 and 38.77 (i), (iii) in the sections and pivot-label records, whose named parts are not part (ii).

### 1F.2 Proposed by a record's own derivation, not ruled — 1 row-part

| Row-part (line) | Record, place | What the record says |
|---|---|---|
| 38.11 (i) (46765) | chord symbol, §2 (a) (line 67), under the heading *"Settled by the record — this side's derivation, not a ruling (documentation only)"* | *"Row 38.11(i), UNPLACED: proposed placed as Row 10.14(i) is — RELOCATED to L2, the chord that layer decided being L2's chord. Challengeable at the row."* |

The record's only ruling (Ruling 1, the spelled root) does not name the row, and the record's §5 says *"the family is
placed"*. The row is therefore neither reached by a ruling nor left open by the record: a placement is proposed and not
ratified. It is kept apart from §1F.1 and §1F.4 so that the application act, or a surface, ratifies or challenges it by
number.

### 1F.3 Reached in substance by phrase-ends Ruling 1's wording, but not named by number — 1 row-part

| Row-part (line) | Subject, in plain words |
|---|---|
| 38.71 (47796) | The phrase is *"bounded by"* phrase markers supplied by the phrase-boundary primitive. DIFFERS with L3-S8 (*"No item of evidence forces or forbids a phrase end"*); the reading file grounds it *"as at Row 19.41"*. |

The same shape as Row 19.41 (§1E.2): it fits phrase-ends Ruling 1's open list of rows *"that only place the phrase ends in
an earlier layer"* and its *"method rows (… forcing markers …)"*. **A candidate derivation — to be confirmed by number on
a surface, not asked as a choice.**

### 1F.4 Still open — 16 row-parts, in four groups

Each was read at its §6 entry (line given). Every one is graded THE DERIVATION IS SILENT. No record or `cowork_l3_*`
surface was found naming any of them, and a search of both for *suggest*, *generation* and *knowledge base* found no
ruling on their subjects (the display surface's Rows 19.4, 19.6 and 19.8, lines 147–149, concern suggestions shown to the
user, not a tool that suggests chords).

**(A) The catalog as a knowledge-base component, not a layer — ground: *"none of `FRAMEWORK.md` §5's charters, nor its
NOT A LAYER items, names a knowledge-base component"*, or travelling with Row 38.20 (i) — 6**

| Row-part (line) | Subject, in plain words |
|---|---|
| 38.20 (i) (46933) | The catalog of progressions, schemas and substitutions is a resource beside the layers, not one of them. |
| 38.20 (ii) (46933) | It has no evidence-source-by-question contract, being reference knowledge queried read-only. |
| 38.21 (i) (46953) | It is consumed by the function layer and the grouping layer. |
| 38.22 (i) (46970) | Durable curated knowledge (this catalog, the chord templates, the key profiles) is a component the layers query, distinct from their per-piece inference. |
| 38.22 (ii) (46970) | The style labels live in the component; style-aware behaviour lives at the consumer. Read beside Row 19.33 (style-specific behaviour only in fitted values). |
| 38.79 (i) (47940) | The catalog is finite and specific to an idiom, the preset selecting it. |

**(B) Recognising a named progression in the music, and the span it covers — ground *"as at Row 19.38 (vi)"* (the
derivation names no recognised progression schema, and no charter names its recognition) — 6**

| Row-part (line) | Subject, in plain words |
|---|---|
| 38.18 (i) (46896) | The harmonic-skeleton progression schemas (ii–V–I, turnarounds, the harmonic outline of the galant schemata) can be recognised at the function layer without a voice-leading axis. (Part (ii) is RELOCATED to the voice-leading axis.) |
| 38.77 (ii) (47891) | The progression-schema span, produced by the recognition and hosted by the grouping layer. |
| 38.78 (47924) | The progression-schema span and the cadential-approach span hold the knowledge of multi-chord progression schemas. |
| 38.79 (ii) (47940) | Whole progressions are composed from the catalog by the pairwise functional grammar. |
| 38.80 (i) (47957) | The recognition belongs in the function layer, added over the decided progression. |
| 38.80 (ii) (47957) | Its hardest problem is fuzzy matching against prototypes, which needs the substitution overlay. |

**(C) A future tool that suggests chords — ground: *"no charter of `FRAMEWORK.md` §5 names a tool that suggests chords,
generation lying outside the analysis"*, or travelling with Row 38.21 (ii) — 3**

| Row-part (line) | Subject, in plain words |
|---|---|
| 38.21 (ii) (46953) | The catalog is built to be shared with a future chord-suggestion tool. |
| 38.81 (ii) (47975) | Multi-chord knowledge would be core to such a tool. (Part (i), the deferral for the analysis, is HISTORICAL.) |
| 38.82 (47992) | The catalog would be one asset shared by the analyser and the suggester. |

**(D) A rule of the decomposition as a whole — 1**

| Row-part (line) | Subject, in plain words |
|---|---|
| 38.50 (47452) | Each layer owns the contribution of exactly one evidence source to one question, delivered once and forward. Ground: `FRAMEWORK.md` §5 divides the analysis by question, makes L2 one entangled decision over everything L0 and L1 publish, and L3-S9 and L3-S23 give each L3 decision several families of evidence. |

6 + 6 + 3 + 1 = 16.

**The D-599 note (preliminary, not a placement).** Groups A and B are the catalog-and-recognition family of §1C, §1D,
§1A.3, §1E.3 group A and Row 7.85; Row 38.20 (i), the ground of §1D group E, is in group A here and is open. Group C is a
subject not met in the members done so far — a tool outside the analysis — and hangs on the same family's answer, since
what it would share is the catalog. Row 38.50 says what Row 19.56 (i) says (§1E.3 group C) and should go with it; unlike
19.56 (i) it lies in no register home, so the precedent noted there (architecture-rules Ruling 1 adopting rows on their
register homes) does not carry to it as it stands. **To be tested; not certain.** A genuine placement for the user is
likely for groups A to C.

**Count:** 3 reached by number + 1 proposed, not ruled + 1 reached in substance + 16 open = 21, the member's total.

---

## 1G. Member 53 — `cowork_idiom_entry_mapping.md` (21 row-parts)

*Added by the Cowork sitting of 2026-11-04 that booted on entry 525.*

The foot list (reading file line 69520): 53.1, 53.2, 53.3, 53.4, 53.5, 53.6, 53.7 (i), 53.8, 53.9, 53.10, 53.11, 53.12 (i),
53.13, 53.14, 53.15, 53.16, 53.17, 53.18, 53.19, 53.20, 53.21 (i).

The document is a provisional working mapping that tags each entry of member 46's catalog — the named progressions and
schemas (its §5.2 table) and the substitution operations (its §5.3 table) — with one or more of five idioms (the reading
file's manifest for the member, lines 69103–69137). The register homes nothing in it (line 69069).

### 1G.1 Reached by a ruling record — none

Searched as §0 states, every row number with and without the space before its part, and the word *idiom*. No row of this
member is named in the L3 ruling records or the `cowork_l3_*` surfaces. The one numeric hit, *53.18(i)* in the sixth-cut
surface (line 142), is a row of the **L2** reading file, put under the L2 nothing-from-L3 Ruling 2; this member has no
claim (i) at Row 53.18. The surfaces' two hits for *idiom* (the fit-and-rest second-cut surface, lines 60 and 65) concern
Row 23.44's idiom mixtures, not catalog tags.

### 1G.2 Still open — 21 row-parts, one group: the idiom tag of a catalog entry

Each was read at its §6 entry (line given). Every one is graded THE DERIVATION IS SILENT, and every one carries the same
ground: *"read as at Row 44.11 and Row 46.40: the entry's idiom tag is an attribute of a catalog entry, and no charter of
`FRAMEWORK.md` §5 names the catalog of named progressions"*.

| Row-part (line) | The entry, and the tag the row gives it |
|---|---|
| 53.1 (69141) | The authentic, half and plagal cadential entries — idiom 1. |
| 53.2 (69158) | The deceptive and Phrygian half cadential entries — idiom 1, idiom 2 added. |
| 53.3 (69176) | The ii–V family — idiom 3. |
| 53.4 (69192) | The turnarounds — idiom 3; the secondary dominant on VI also idiom 2. |
| 53.5 (69208) | The circle-of-fifths sequence — idiom 1 in triads, idiom 3 in sevenths. |
| 53.6 (69224) | The descending-thirds sequence — idiom 1. |
| 53.7 (i) (69239) | The galant Monte and Fonte — idiom 2. (Part (ii), their definition by voice leading, is RELOCATED to the voice-leading axis.) |
| 53.8 (69258) | The doo-wop and Axis loops — idiom 4. |
| 53.9 (69274) | The Pachelbel loop — idiom 4, idiom 1 added. |
| 53.10 (69289) | The Andalusian loop — idiom 4, idiom 5 added. |
| 53.11 (69305) | The lament bass — idiom 2 or idiom 5. |
| 53.12 (i) (69321) | The galant schemata — idiom 2, provisionally. (Part (ii) is RELOCATED to the voice-leading axis.) |
| 53.13 (69342) | The Coltrane changes and the backdoor progression — idiom 5. |
| 53.14 (69357) | The secondary dominant or tonicization — idiom 2. |
| 53.15 (69372) | The related ii–V — idiom 3. |
| 53.16 (69387) | The tritone substitution — idiom 5. |
| 53.17 (69402) | The diatonic substitution — idiom 1. |
| 53.18 (69417) | Modal interchange — idiom 2, idiom 4 for the triadic borrowings. |
| 53.19 (69432) | The diminished approach — idiom 2. |
| 53.20 (69447) | The deceptive resolution (read as a substitution of the chord a dominant resolves to, not a cadence type) — idiom 2. |
| 53.21 (i) (69463) | The line cliché — idiom 5. (Part (ii), *"voice-leading-adjacent"*, is RELOCATED to the voice-leading axis.) |

**The D-599 note (preliminary, not a placement).** No record found settles the group. The rows are the same kind as §1C
group D and §1D group D (style tags on catalog entries), and they hang on the catalog question of §1C: if the catalog is
placed nowhere, its entries' tags go with it. The reading file states one alternative and does not take it (its
placement (l), line 69126): **RELOCATED** to L2, as Rows 46.39 and 46.41 placed the five-idiom taxonomy and the presets'
idiom weightings — declined there because a row stating which idioms an entry belongs to is not a row about how an idiom
weighs. Rows 53.1 and 53.2 name cadence types, which L3-S17 already decides (cadence type Rulings 1 and 2); their claim is
only the entries' tag (the reading file's placement (m)). **A genuine placement for the user is likely, as one family with
§1C, §1D, §1F groups A to C, §1A.3 and Row 7.85.**

**Count:** 0 reached + 21 open = 21, the member's total.

---

## 1H. Member 48 — `cowork_notation_output_contract.md` (14 row-parts)

*Added by the Cowork sitting of 2026-11-04 that booted on entry 526.*

The foot list (reading file line 66600): 48.1 (i), 48.3 (i), 48.4, 48.15, 48.17 (iii), 48.19, 48.20 (ii), 48.26 (ii),
48.27 (ii), 48.31, 48.32 (ii), 48.35, 48.36 (i), 48.36 (iii).

The document is the old design's contract for the one record the application's notation path reads: two ways in to it
(a caller names a span, or a note), the record's fields, and the old consumers mapped onto it. The reading file's
weighing for the member (lines 65754–65788) states the grounds of all fourteen and the alternatives it did not take.

### 1H.1 Reached by a ruling record — none

Searched as §0 states, every row number with and without the space before its part: no row of this member is named in
the L3 ruling records or the `cowork_l3_*` surfaces. **The display surface leaves these rows open in terms**: its §1
(line 32) says *"The UNPLACED display statements of member 48 (the reading file at 65770–65777) are tier item 14's, not
this cut's."* So display Ruling 1 (2026-11-04) does not reach them, by the surface's own exclusion. A search of the same
records and surfaces for *factor role*, *bass role*, *per-event bass*, *chromatic inflection*, *modal colour* and
*seam* found nothing.

### 1H.2 Still open — 14 row-parts, in four groups by the reading file's own ground

Each was read at its §6 entry (line given). Every one is graded THE DERIVATION IS SILENT, except Rows 48.19 and
48.20 (ii), whose display claim is graded AGREES with L3-S5's premise.

**(A) How a published fact is displayed — ground *"read as at Row 4.6"*: `FRAMEWORK.md` §3.3 keeps presentation outside
what the analysis depends on, and no charter of §5 is a display layer (the reading file's placement (l)) — 8**

| Row-part (line) | Subject, in plain words |
|---|---|
| 48.17 (iii) (66070) | The augmented-sixth sub-type, read from the sounding notes, is a presentation read of L1's facts. |
| 48.19 (66112) | The display chord symbol and the Nashville number are presentation derivations from published facts. AGREES with L3-S5. |
| 48.20 (ii) (66131) | Each is rendered by one shared presentation formatter and never published on the record. AGREES with L3-S5. |
| 48.26 (ii) (66235) | The old confidence gates' numbers become the emitting code's declared presentation constants. |
| 48.27 (ii) (66255) | The number shown after an alternative shows the stamped uncertainty quantity. |
| 48.35 (66396) | The accessibility string is formatted downstream of the formatter that reads the record. |
| 48.36 (i) (66412) | The old exposure and annotation gates keep their function: whether to show a key run, merge a region, write a cadence label. |
| 48.36 (iii) (66412) | Their numbers are declared presentation constants, outside the inference, each with a stated reason. |

**(B) The two ways in to the record, as interfaces of the application's code — ground *"read as at Row 4.16"*: no
charter of §5 holds the code's interfaces (placement (m)) — 4**

| Row-part (line) | Subject, in plain words |
|---|---|
| 48.1 (i) (65792) | A caller names a span of the score and gets the record for that span. |
| 48.3 (i) (65827) | A caller names a note or a position and gets a view of the same record: segment, key, chord, alternatives, uncertainty, display facts. |
| 48.4 (65849) | No second computation: the note view is a lookup into the span record. |
| 48.31 (66329) | The old single-note consumers read that note view. |

**(C) The bass's role in the chord, note by note — 1**

| Row-part (line) | Subject, in plain words |
|---|---|
| 48.15 (66033) | For each sounding event, which chord member the lowest note is, found by comparing L1's per-slice lowest pitch with the members of L2's chord. The reading file's ground: no charter lists it, and L3-S4 speaks to the chord symbol's bass, not to a role per event (placement (o)). |

**(D) Counts of chromatic inflections per key run — 1**

| Row-part (line) | Subject, in plain words |
|---|---|
| 48.32 (ii) (66344) | The modal colour of a key run carried as counts of the chromatic inflections of each degree. The reading file's ground: no charter lists such counts among its publications, L2 publishing the tonality as tonic and mode. |

8 + 4 + 1 + 1 = 14.

**The D-599 note (preliminary, not a placement).**
1. **Groups A and B hang on member 4.** Their grounds are Rows 4.6 and 4.16, both UNPLACED in member 4 and open there
   (§1I.3, groups A and B); they go together with those rows. *(Former wording, kept (#12): "Their grounds are Rows 4.6
   and 4.16, both UNPLACED in member 4 (`ARCHITECTURE.md`, 11 UNPLACED, the next member in §3 of entry 526's order), not
   yet inventoried. They should be taken together with Rows 4.6, 4.16, 4.18 and 4.19 when member 4 is done." Corrected
   by the same sitting once member 4 was done.)*
2. **For group A, display Ruling 1 part A bears directly.** It ratified Row 4.2's proposal as a derivation: every display
   string is produced outside the analysis, from published facts, and the analysis carries no display convention; its
   statement of the decided method ends *"a display turns published facts into text"*. The reading file's placement (l)
   names an alternative it did not take: Rows 48.19 and 48.20 (ii) **ADOPTED — proposed**, travelling with Row 4.2. That
   lead row is now ratified. Whether that makes the two rows candidate derivations, and what placement the other six
   display rows get when no charter is a display layer, is for the surface to test. **To be tested; not certain.**
3. **Group C** meets two neighbouring rulings without being reached by either: figured-bass Ruling 1 (2026-11-03) has
   L1 publish the spelled intervals above the lowest sounding pitch at every slice and L3 publish a figure under every
   bass note; and the chord symbol record (its check, item 9, line 105) says the derivation's flag on L3-S4 was *"settled
   in wording by the 2026-10-08 structural-bass record"* (that L2 record not opened by this sitting). A bearing, not a
   reach. A genuine placement is possible.
4. **Group D** met no record. Its subject — what L2 publishes about a key run's colour beyond tonic and mode — lies on
   L2's side. A genuine placement is possible.

**Count:** 0 reached + 14 open = 14, the member's total.

---

## 1I. Member 4 — `ARCHITECTURE.md`, *4.3 ChordSymbolFormatter* (11 row-parts)

*Added by the Cowork sitting of 2026-11-04 that booted on entry 526.*

The foot list (reading file line 2593): 4.6, 4.16, 4.17, 4.18, 4.19, 4.20, 4.23(i), 4.24(ii), 4.26, 4.28, 4.29.

Further record short name: **figured bass** = `…_2026_11_03_l3_figured_bass_sitting.md`.

### 1I.1 Reached by a ruling record — 3 row-parts

| Row-part | Record, place | What the record did |
|---|---|---|
| 4.23(i), 4.28, 4.29 (3) | figured bass, Ruling 1 (OQ-L3-7, the user's word "B"), its documentation paragraph (line 99) | *"Rows 4.23(i), 4.28 and 4.29 placed with the new output — how they are re-marked is the application act's"*: the second figured bass, at the continuo grain, under every bass note, read off L1's per-slice intervals above the lowest sounding pitch |

### 1I.2 Settled by a record's own derivation, not ruled — 3 row-parts

| Row-part (line) | Record, place | What the record says |
|---|---|---|
| 4.17 (2321) | figured bass, §2 (b) (line 57), under the heading *"Settled by the record — this side's derivation, not a ruling (documentation only)"* | the row *"differs only where it treats the figured bass as a formatting choice rather than a published fact; the charter places it among L3's outputs, and a display may still render it (L3-S27's views)"* |
| 4.24(ii) (2429), 4.26 (2460) | figured bass, §2 (c) (line 59), the same heading | octave reduction and the omission table as steps of computing: *"L3-S27's full figure, short forms a view under a named convention — on this side's reading of D-295"* |

The record's only ruling (Ruling 1, OQ-L3-7) does not name these three, and its §5 says *"the family is placed"*. As with
Row 38.11 (i) (§1F.2), they are neither reached by a ruling nor left open by the record. Unlike Row 38.11 (i), the record
names no placement for them: it decides against what they differ on and says no more. Kept apart so that the application
act, or a surface, ratifies or challenges this by number.

### 1I.3 Still open — 5 row-parts, in two groups

Each was read at its §6 entry (line given). Every one is graded THE DERIVATION IS SILENT. No ruling record or `cowork_l3_*`
surface names any of them (the one numeric hit, *"section 4.6"* in the eighth-cut surface, line 52, is a section of
another document).

**(A) Display conventions — ground: a display convention, no charter of `FRAMEWORK.md` §5 being a display layer (Row 4.6;
the others *"as at Row 4.6"*) — 3**

| Row-part (line) | Subject, in plain words |
|---|---|
| 4.6 (2160) | The chord symbol's root and bass names follow the score's chord-symbol spelling setting. |
| 4.18 (2338) | Planned spelling conventions: American, German/Nordic (H and B), jazz, classical augmented-sixth names. |
| 4.19 (2352) | Planned symbol vocabulary: ø or m7b5, Δ or maj7, + or aug. |

**(B) Plans for the code's interfaces — ground: a plan for the code's interfaces, which no charter holds (Row 4.16; Row
4.20 travelling with it) — 2**

| Row-part (line) | Subject, in plain words |
|---|---|
| 4.16 (2305) | The chord-symbol formatter is to become a replaceable interface. |
| 4.20 (2366) | Its options become that interface's configuration. |

3 + 2 = 5.

**The D-599 note (preliminary, not a placement).**
1. **Group A is one group with §1H group A** (the eight member-48 rows read *"as at Row 4.6"*). Display Ruling 1 part A
   (2026-11-04) already decides where a display convention lives: outside the analysis, which carries none; L3-S5's
   premise has a display choose *"its own convention, as a display act"*. The chord symbol record's §2 (e) says the same of
   the augmented-sixth respelling (OQ-L3-9: *"a display's own act"*), which touches Row 4.18's last item. So what looks
   left is not where these statements belong but which of the five dispositions a statement about a display convention
   takes when no charter is a display layer. That may be one answer for the eleven display rows (§1H group A's eight and this group's three), and the
   surface should test whether the disposition vocabulary's own definitions already give it. **To be tested; not
   certain.**
2. **Group B is one group with §1H group B** (the four member-48 rows read *"as at Row 4.16"*): statements about how the
   program's code is organised. The question is the same kind: which disposition a statement about code structure
   takes when no charter holds code structure. A genuine placement for the user is possible.

**Count:** 3 reached + 3 settled by a record's derivation, not ruled + 5 open = 11, the member's total.

---

## 1J. Member 40 — `cowork_evidence_inventory.md` (11 row-parts)

*Added by the Cowork sitting of 2026-11-04 that booted on entry 527.*

The foot list (reading file line 55225): 40.6, 40.12 (iii), 40.12 (iv), 40.24 (ii), 40.24 (iii), 40.40 (ii), 40.40 (iii),
40.41 (ii), 40.60, 40.61, 40.64.

The document is the old design's inventory of the facts available to the analysis — those in the score, those each old
layer produced or left undiscussed — with the old key layer's list of the evidence it wanted (the reading file's manifest
for the member, line 53847 onwards).

Further record short names: **harmonic rhythm** = `…_2026_11_03_l3_harmonic_rhythm_sitting.md`; **display** =
`…_2026_11_04_l3_display_sitting.md`.

### 1J.1 Reached by a ruling record — 3 row-parts

| Row-part | Record, place | What the record did |
|---|---|---|
| 40.24 (iii) | phrase units, Ruling 2 item d (line 95) | derivation ratified: accelerating harmonic rhythm before a candidate position, read from L2's published boundaries, enters as a candidate term admitted only if a held-out measurement repays it |
| 40.64 | cadence placement, Ruling 2 item b (line 98) | derivation ratified: evidence-class facts are published without a named consumer, each with its establishment status; the pattern evidence has a consumer in any case, L3's phrase decision |
| 40.40 (ii) | S38 ratification, Ruling 1 (line 33), which ratifies *"the 100 DIFFERS as the eight cuts file them"* → the seventh-cut surface §3 A (`cowork_l3_s38_seventh_cut_surface_2026_11_03.md`, lines 58–63) | HISTORICAL — the piece's map of cadences and phrases *"feeds phrase-aligned key spans from the top down"*, the route nothing-from-L3 Ruling 2 names as superseded (its L2 twin, Row 44.49 (ii), ruled so); the record reaches the row through the cut it ratifies, as with Rows 19.38 (v), 36.111 (ii) and 38.76 |

1 + 1 + 1 = 3.

No later record was found carrying any of the three as UNPLACED.

### 1J.2 Settled by a record's own derivation, not ruled — 2 row-parts

| Row-part (line) | Record, place | What the record says |
|---|---|---|
| 40.24 (ii) (54437), 40.41 (ii) (54744) | harmonic rhythm, §2 (d) (lines 70–73), under the heading *"Settled by the record — this side's derivation, not a ruling (documentation only)"* | proposed UNPLACED, *"corrected to HISTORICAL — a superseded plan, as their twins Rows 44.33(ii), 44.50(vi) and 44.76(iii) were ruled by the nothing-from-L3 Ruling 4; the slice-duration reading of harmonic rhythm is also met by Ruling 62 item 3"* |

The record's only ruling (Ruling 1, the root-and-quality grouping) does not name the two, and its §5 says *"the family is
placed"*. As with Row 38.11 (i) (§1F.2) and Rows 4.17, 4.24 (ii), 4.26 (§1I.2), they are neither reached by a ruling nor
left open by the record. Like Row 38.11 (i), and unlike the three of §1I.2, the record names a placement: HISTORICAL.
Kept apart so that the application act, or a surface, ratifies or challenges it by number.

### 1J.3 Still open — 6 row-parts, in four groups

Each was read at its §6 entry (line given). No ruling record or `cowork_l3_*` surface names any of them by number except
Row 40.6, named only in the phrase-ends record's list of rows read at §6 (its line 90), which is not counted as reached
(§0). A search of the same records and surfaces for *lyric*, *verse*, *tempo*, *character mark*, *style hint*, *tension
curve*, *harmonic tension*, *explainab*, *show me why*, *evidence trail*, *late-bound* and *D-522* found no ruling on
their subjects; the only hits are the architecture-rules record (line 45) and its surface (lines 144–145), which cite
D-522 for Row 19.82, not for these rows.

**(A) The fermata as the phrase-end marker in the chorales — 1.** DIFFERS with L3-S8.

| Row-part (line) | Subject, in plain words |
|---|---|
| 40.6 (54115) | *"In Bach chorales the fermata IS the phrase-end marker"*, the most reliable phrase-boundary fact in the corpus; the clause on a comparable product's key-detection gain from a phrase-end alignment fix is taken with the sentence. |

**(B) Sources of evidence no derived statement names — 2.** THE DERIVATION IS SILENT.

| Row-part (line) | Subject, in plain words |
|---|---|
| 40.12 (iii) (54224) | Lyrics and verse structure as chorale phrase structure, *"probably redundant with fermatas"*. The reading file's ground: L3-S9's four families, and `FRAMEWORK.md` §5's list of what L0 gives, which names no lyrics. |
| 40.12 (iv) (54224) | Tempo and character markings as hints of style or of a preset, weak. The reading file's ground: no charter names a style hint, and under L3-S37 L3 reads only what L0, L1 and L2 publish. |

**(C) A candidate published fact on no charter's list — 1.** THE DERIVATION IS SILENT.

| Row-part (line) | Subject, in plain words |
|---|---|
| 40.40 (iii) (54716) | A curve of harmonic tension, *"weak, research-flavored"*. The reading file's ground: L3's list of what it publishes, and L3-S24, under which adding an output to L3 is a ruling. |

**(D) Explaining an inference to the end user — 2.** THE DERIVATION IS SILENT. Both lie in the home of **D-522**
(`DECISIONS.md` line 302, read: *"Explaining an inference to the end user is a late-bound DISPLAY consumer of facts that
already exist — not a new analysis"*, LIVE, no entry ratification shown, home `cowork_evidence_inventory.md` §8b, marked
*⚠gap*).

| Row-part (line) | Subject, in plain words |
|---|---|
| 40.60 (55061) | The end user may want to know how a mode, chord or function was inferred. The reading file's ground: a want of the product's display, which no charter names. |
| 40.61 (55083) | If the evidence behind every inference is published, *"show me why"* is a late-bound display consumer of facts that already exist, not a new analysis. The reading file's ground: a rule on how a display reads the published facts, which no charter names; read with L3-S29. |

1 + 2 + 1 + 2 = 6.

**The D-599 note (preliminary, not a placement).**
1. **Group A is the same subject as Row 7.116 (ii)** (§1.2: *"In the chorale corpus the fermata is the reliable
   marker"*), which the sitting that booted on entry 522 left open with the note *"Looks settled … Candidate
   derivation"*. One treatment for the two (#6): phrase-ends Ruling 1 declined its alternative C (*"notated markers
   (fermata, final bar line) force a phrase end"*) and keeps the markers as evidence entering as fitted terms (L3-S9
   (i), whose family (i) names FERMATA, as the reading file quotes it at the row). Whether the row's claim is a rule
   (then decided against, like §1B.2 group b) or a statement of how reliable the evidence is (then possibly adopted as
   evidence) is for the surface. The key-detection clause speaks of L2's subject. **To be tested; not certain.**
2. **Group B.** Row 40.12 (iii): whether L0 publishes lyrics is L0's input contract, not read by this sitting; if it
   does, the row looks like a candidate term under the same held-out-measurement rule as its neighbour 40.12 (ii)
   (ADOPTED — carried, L3-S9 family (iv)). Row 40.12 (iv): architecture-rules Ruling 1 part B (style-specific behaviour
   of L3 only in the fitted values of its model, D-024) bears on it without reaching it. A genuine placement is possible
   for both.
3. **Group C.** No record found. Under L3-S24 adding an output is a ruling, so a genuine placement is likely (adopt as a
   candidate output, or decline). The row's own words call it weak.
4. **Group D joins the display rows** (§1H group A, §1I.3 group A, entry 527 §2 item 3). Display Ruling 1 part A
   (*"Every display string is produced outside the analysis, from published facts"*; *"a display turns published facts
   into text"*) bears directly, and Row 40.61 restates D-522 almost word for word. On the precedent of architecture-rules
   Ruling 1 (rows adopted on their register homes), the two may be candidate derivations on D-522. Weak points: D-522
   shows no entry ratification and its home is marked as a gap; Row 40.60 states a want, not a rule. **To be tested; not
   certain.**

**Count:** 3 reached + 2 settled by a record's derivation, not ruled + 6 open = 11, the member's total.

---

## 1K. Member 23 — `ARCHITECTURE.md`, *6. The Style System* (8 row-parts)

*Added by the Cowork sitting of 2026-11-04 that booted on entry 527.*

The foot list (reading file line 33101): 23.2, 23.30(i), 23.31, 23.36(i), 23.37, 23.39, 23.40, 23.41.

The member is the old design's style system. Seven of the eight rows come from its sub-section *6.8 The user-facing
preset layer*, whose own status line records it as *"RECORDED and DEFERRED product work"* (as the reading file relays it
at Row 23.30, line 32778).

### 1K.1 Reached by a ruling record — none

Searched as §0 states, every row number with and without the space before its part: no row of this member is named in
the L3 ruling records or the `cowork_l3_*` surfaces. A search of the same records and surfaces for *preset*, *mixture*,
*metadata*, *user-defined propert*, *custom propert*, *selectable*, *style file* and *problems vs features* found only
the fit-and-rest second-cut surface (lines 60 and 65), on Row 23.44's idiom mixtures, which is not one of these rows.

### 1K.2 Still open — 8 row-parts, in two groups

Each was read at its §6 entry (line given). Every one is graded THE DERIVATION IS SILENT.

**(A) The user-facing preset layer — 7.** The reading file's ground: no charter of `FRAMEWORK.md` §5 names the product's
presets, their naming, what its user may select, or where a piece's chosen mixture is stored, and no derived statement
speaks to a preset.

| Row-part (line) | Subject, in plain words | The L2 twin (L2 reading file line) |
|---|---|---|
| 23.30(i) (32773) | A preset is shown to its user as a familiar genre-and-era label with exemplars the user knows, never as an idiom name or an obscure exemplar. (Part (ii) is RELOCATED to L2.) | 25.34 (i) (43388) |
| 23.31 (32795) | A preset is named after a period and style the user recognises, anchored by known musicians. | 25.35 (43409) |
| 23.36(i) (32868) | Every idiom mixture is selectable; the discovered cloud is the map of the evidence, not the boundary. (Part (ii) is RELOCATED to the uncertainty surface.) | 25.40 (43488), the whole sentence |
| 23.37 (32888) | Named presets are cluster centres; a custom selector admits any point. | 25.41 (43504) |
| 23.39 (32919) | The piece's own metadata is the primary home of its mixture; a user-set mixture is never silently overwritten. | 25.43 (43535) |
| 23.40 (32936) | The mixture is stored in the score's own user-defined properties, so a later analysis starts warm. | 25.44 (43551) |
| 23.41 (32951) | The stored value records its provenance; a user-set one is never silently replaced, an auto-detected one may be refreshed. | 25.45 (43567) |

**(B) A style's analysis dimension — 1.**

| Row-part (line) | Subject, in plain words | The L2 twin (L2 reading file line) |
|---|---|---|
| 23.2 (32343) | A dimension of the planned style file: which findings the analyzer reports as problems and which as features of the style. The reading file's ground: no charter names such flagging, the nearest being the part-writing advice the second axis owns (Row 19.60). | 25.11 (43028) |

7 + 1 = 8.

**The D-599 note (preliminary, not a placement).**
1. **Group A: every twin is ruled.** Each L2 twin is the same outgoing sentence at the same lines of `ARCHITECTURE.md`
   (5628–5659), found by sentence search in the L2 reading file and read at its row. At each, the L2 reading file
   records: *"RULED DISPOSITION (cowork_rulings_2026_10_10_l2_tail_style_and_idiom_sitting.md, Ruling 1).
   **RELOCATED — outside the framework** — to `ARCHITECTURE.md` §6.8, "the user-facing preset layer, recorded and
   deferred product work", placed from UNPLACED"*, with the note that RELOCATED is *"stretched to a home outside the
   framework, because no charter is the home of the style system"* **[relayed — the L2 record itself not opened by this
   sitting; quoted as the L2 reading file records it]**. On the twin precedent the earlier L3 records used (harmonic
   rhythm §2; the seventh-cut surface §2 and §3 A), and one treatment for one sentence (#6), the seven look like
   **candidate derivations: RELOCATED — outside the framework, travelling with their L2 twins**. Weak point: the
   stretched use of RELOCATED was ruled at L2; whether an L3 surface may apply it without a ruling of its own is for
   that surface. **To be tested; not certain.**
2. **Group B: the twin is proposed only.** Row 25.11 is proposed **HISTORICAL — a plan** in the L2 reading file, with no
   ruled line at its row. No record found settles Row 23.2. A placement is possible; the L2 twin's proposal is the
   nearest lead.

**Count:** 0 reached + 8 open = 8, the member's total.

---

## 1L. Member 2 — `ARCHITECTURE.md`, *Layer 5 — the function/cadence layer* (7 row-parts)

*Added by the Cowork sitting of 2026-11-04 that booted on entry 528.*

The foot list (reading file line 1693): 2.7(i), 2.7(ii), 2.8, 2.9, 2.15, 2.16(ii), 2.18.

The member is the old design's function layer as `ARCHITECTURE.md` describes it (the reading file's manifest, line
1159). All seven rows lie inside the homes of D-584 (Rows 2.7 to 2.9) or D-495 (Rows 2.15, 2.16, 2.18), as the reading
file marks them WITHHELD at each row.

### 1L.1 Reached by a ruling record — 7 row-parts

Searched as §0 states, every row number with and without the space before its part. Each hit was read at its line.

| Row-part | Record, place | What the record did |
|---|---|---|
| 2.7(i) | cadence type, Ruling 1 (line 38) | decided against *"in so far as they make the bass-derived inversion the only criterion"* |
| 2.7(ii), 2.8 (2) | cadence features, Ruling 1 item b (line 62) | decided against *"in so far as they keep the fact unpublished"* (the highest sounding pitch's degree at the arrival) |
| 2.9 | cadence type, Ruling 1 (line 38), for *"its perfect/imperfect half"*; cadence mass, Ruling 1 (line 48), for its *"confidence half"*, carried there by the cadence type record (line 44) | each half decided against: the first in so far as the bass is the only criterion; the second in so far as it lowers confidence by a fixed rule (*"the top note does not nudge the mass"*, line 46) |
| 2.16(ii) | phrase ends, Ruling 1 (documentation, line 83) | named by number among the rows recorded as overtaken by the charter and Ruling 48 |
| 2.15, 2.18 (2) | phrase ends §2 (carried, line 92: *"Ruling 1 settles their phrase side only"*) → cadence placement, Ruling 2 item e (line 108), ratified on the user's word *"yes"* (line 91) | D-495's flat-profile fallback *"loses its subject at L3"*; the old fallback rule drops out — the same treatment as Row 7.336 (§1.1) |

1 + 2 + 1 + 1 + 2 = 7.

*Named in a record but NOT counted as reached on that naming:* Rows 2.15 and 2.16 also appear in the phrase-ends record's
list of rows read at §6 (line 90); Row 2.9 in the cadence features record's list of rows read (line 141); Rows 2.16 and
2.7 in the cadence placement record's list of rows read (lines 140–141). Each is reached elsewhere, above.

No later record was found carrying any of the seven as UNPLACED.

### 1L.2 Still open — none

**Count:** 7 reached + 0 open = 7, the member's total.

---

## 1M. Member 3 — `ARCHITECTURE.md`, *Layer 6 — the grouping layer* (4 row-parts)

*Added by the Cowork sitting of 2026-11-04 that booted on entry 528.*

The foot list (reading file line 2038): 3.1(i), 3.1(ii), 3.3, 3.5(iii).

The member is the old design's grouping layer as `ARCHITECTURE.md` describes it (the reading file's manifest, line
1725). Row 3.5 lies in D-472's home (marked WITHHELD at the row); Rows 3.1 and 3.3 lie in no home.

Further record short name: **pivot label** = `…_2026_11_03_l3_pivot_label_sitting.md`.

### 1M.1 Reached by a ruling record — 2 row-parts

Searched as §0 states, every row number with and without the space before its part. Each hit was read at its line.

| Row-part | Record, place | What the record did |
|---|---|---|
| 3.1(i), 3.3 (2) | sections, Ruling 2 (§3a, line 112) | decided against, among *"the ten rows that call the grouping flat"* (3.1(i): *"the **flat** structure"*; 3.3: *"Hierarchy … out of the validatable core"*) |

*Named in a record but NOT counted as reached on that naming:* Row 3.1 also appears in the sections record's
corrections (line 86, a quotation joined across Rows 3.1 and 8.25) and its list of rows read (line 213), and in the
key-areas record's list of rows read (line 144); the key-areas record adopts Row 3.1(iii), not an UNPLACED part.

### 1M.2 Proposed by a record's own derivation, not ruled — 1 row-part

| Row-part (line) | Record, place | What the record says |
|---|---|---|
| 3.5(iii) (1811) | pivot label, §2b (lines 79–88), headed *"placed by this side's derivation, not a ruling"* | the wobble-suppression (Roman numerals written against an enclosing key rather than the span's own) *"decided against as a consequence of the key-areas Ruling 2"*, which declined D-472's grouping; *"the remainder consistent with L2's publication, a display matter"*. *"Challengeable at the row. Documentation only."* |

The key-areas record carried the row there (its line 117: *"travels to the pivot-label family (L3-S7)"*). As with Row
38.11 (i) (§1F.2) and Rows 40.24 (ii), 40.41 (ii) (§1J.2), a placement is proposed and not ratified.

**The L2 twin, checked by this sitting.** The pivot-label record says it did not read the L2 comparison's Row 22.92(iii).
That row (L2 reading file line 34376) is the same outgoing sentence, and its ruled line reads: *"RULED DISPOSITION
(cowork_rulings_2026_10_08_l2_chord_as_degree_sitting.md, Ruling 2). (iii) **RELOCATED to *L3 — The read-off facts***"*,
with *"Whether L3 offers a view relative to an enclosing key area is L3's derivation's question; L2's degree stands
whatever L3 shows"* **[the ruled line checked at the L2 reading file; the L2 record itself relayed, not opened]**. So the
twin ruling sends the question to L3, and the pivot-label record's proposal is L3's answer to it. The twin does not
conflict with the proposal; it does not ratify it either.

### 1M.3 Reached in substance by phrase-ends Ruling 1's wording, but not named by number — 1 row-part

| Row-part (line) | Subject, in plain words |
|---|---|
| 3.1(ii) (1738) | The punctuation-spans come *"from the L1.5 phrase-boundary primitive"*, the layer beneath. DIFFERS with L3-S8 (*"The phrase reading is an L3 decision"*). |

It fits phrase-ends Ruling 1's open list of rows *"that only place the phrase ends in an earlier layer"* (a list it opens
with *"among them"*), which names Row 2.16 (ii) of the same kind. The same shape as Rows 19.41 (§1E.2) and 38.71 (§1F.3).
**A candidate derivation — to be confirmed by number on a surface, not asked as a choice.**

### 1M.4 Still open — none

**Count:** 2 reached + 1 proposed by a record's derivation, not ruled + 1 reached in substance + 0 open = 4, the
member's total.

---

## 1N. Member 24 — `ARCHITECTURE.md`, *7. The Knowledge Base* (4 row-parts)

*Added by the Cowork sitting of 2026-11-04 that booted on entry 529.*

The foot list (reading file line 33404): 24.1, 24.2, 24.4, 24.6.

The member is three passages of the old design's knowledge base (the reading file's manifest, lines 33136–33223). The
four UNPLACED rows are all in its first passage (`ARCHITECTURE.md` lines 5705–5721), the two bullets on the Harmonic
Vocabulary, the catalog of named progressions and substitutions. Rows 24.1 and 24.2 lie in the home of **D-419**, Rows
24.4 and 24.6 in the home of **D-496**, neither withheld (the reading file's marks for the member, line 33427; the titles
relayed from the reading file's manifest, line 33172, `DECISIONS.md` not read at those rows by this sitting).

### 1N.1 Reached by a ruling record — none

Searched as §0 states. No row has a part, so there is no spaced form to search. No row of this member is named in the
L3 ruling records or the `cowork_l3_*` surfaces. A search of the same records and surfaces for *D-419*, *D-496*,
*recognition consumer*, *Harmonic Vocabulary*, *second store*, *one store*, *pairwise grammar*, *by drift* and
*dormancy* found nothing outside this inventory.

### 1N.2 Still open — 4 row-parts, in two groups

Each was read at its §6 entry (line given). Every one is graded THE DERIVATION IS SILENT. The reading file's ground at
each: no charter of `FRAMEWORK.md` §5 names the Harmonic Vocabulary or its recognition consumer (*"as Row 8.18 found"*).

**(A) The catalog's dormancy and what its recognition would make of it — 2**

| Row-part (line) | Subject, in plain words |
|---|---|
| 24.1 (33227) | Until the recognition consumer is built, the old function layer does not use the catalog at all; the connection is absent, not partial. |
| 24.2 (33245) | That consumer is the separate piece of work that would make the catalog a prior for choosing between chord readings over several chords, and a source of the grouping layer's sequence spans; it is also where the old idiom weights would first do anything. |

**(B) One store or two for the knowledge of which chord may follow which — 2**

| Row-part (line) | Subject, in plain words |
|---|---|
| 24.4 (33274) | Whether the rules of which chord may follow which (the pairwise grammar) fold into the catalog or stay a second store is a decision owed, made when the recognition consumer is built. |
| 24.6 (33306) | That choice is made explicitly at that build, never by drift. |

2 + 2 = 4.

The rows beside them in the same bullets, Rows 24.3 and 24.5 (the present state: no use of the catalog; two stores),
are QUARANTINED in the reading file, not UNPLACED, and are not part of this inventory.

**No L2 twin.** The L2 reading file's member for the same section (its §6.26, line 43751) lists five ranges of
`ARCHITECTURE.md` §7 — lines 5686–5700, 5757–5763, 5765–5767, 5769–5772 and 5774–5785 — and none covers lines
5705–5721. A search of the L2 reading file for four phrases of the four outgoing sentences (*"RECOGNITION CONSUMER is
built"*, *"multi-chord disambiguation prior"*, *"SECOND store"*, *"settled by drift"*) found none of them.

**The D-599 note (preliminary, not a placement).**
1. **Group A is the catalog-and-recognition family** of §1C, §1D, §1F groups A and B, §1G, §1A.3, §1E.3 group A and
   Row 7.85. Its rows state when and how the recognition would use the catalog; they hang on whether the recognition
   and its catalog are placed anywhere.
2. **Group B has a second side.** The pairwise grammar is already placed with L2 (the reading file cites Rows 7.73 to
   7.84). So the question in Rows 24.4 and 24.6 is whether L2's pairwise grammar and the catalog are one store. It
   cannot be settled until the catalog's own placement is: if the catalog is placed nowhere, there is no second store to
   fold into. It goes with the same family, one step after it.
3. **A bearing on the whole family, met while looking for the twin.** The L2 nothing-from-L3 record (2026-10-07),
   Ruling 5, user's word *"confirmed"*, placed 124 parts RELOCATED to *L3 — The read-off facts*, among them *"named
   progressions and the recogniser 23"*, and the record states with the question that *"relocating a claim to L3 does
   not decide L3's design"* **[checked at the record, lines 181–192]**. One of those parts is the L2 reading file's
   Row 5.91 (line 5607: *"The named progressions and substitutions live in the Harmonic Vocabulary"*), whose ruled line
   also carries a tension *"noted … for whoever derives L3"*: D-503 seeds the recogniser's mixture from the user's
   preset, while `FRAMEWORK.md` §3.3 says the analysis depends on no preset (relayed from the L2 tail style-and-idiom
   record, §1, as the reading file quotes it; that record not opened by this sitting). So the L2 side sent this subject
   to L3. The L3 reading file grounds the family's rows on L3 having no charter for it. The two are not in conflict,
   since the L2 ruling decides nothing of L3's design, but the family's surface should state both. **This is a bearing,
   not a reach**, and it was not met by the members done before this one (a search of this inventory for *Ruling 5*
   of that record finds none before §1N).

**Count:** 0 reached + 4 open = 4, the member's total.

---

## 1O. Member 54 — `cowork_bounded_context_design.md` (4 row-parts)

*Added by the Cowork sitting of 2026-11-04 that booted on entry 529.*

The foot list (reading file line 70506): 54.14 (i), 54.14 (ii), 54.36 (i), 54.36 (ii).

The document is the old design of bounded context: how much music each old layer reads, and how it asks for more. The
two rows are its two sentences about the old grouping layer (*"Layer 6"*), which only passes on the edge marks and the
*extension-cue* tag and never asks for more music (Row 54.14, line 70024; Row 54.36, line 70444). Each is graded DIFFERS
with L3-S40 (*"L3 asks for a larger span from the caller, as L2 does"*) at both parts. Row 54.14 lies in D-263's home
(as the reading file relays it at the row).

### 1O.1 Reached by a ruling record — 4 row-parts

Searched as §0 states, every row number with and without the space before its part. Each hit was read at its line.

| Row-part | Record, place | What the record did |
|---|---|---|
| 54.14 (ii), 54.36 (i) (2) | edge of span, Ruling 1 (OQ-L3-10, the user's word *"yes"*), documentation paragraph (lines 76–78) | decided against: *"the grouping layer only tags the edge and never acts on the tag"* |
| 54.14 (i), 54.36 (ii) (2) | the same paragraph (line 78), with the record's check, item 5 (line 92) | decided against for their tag-only part; *"their marking part agrees with L3-S40's cut mark"*, the tag's information surviving as the truncation mark (D-263) |

2 + 2 = 4.

The record also names all four in its §0 (line 15) as the family's DIFFERS rows read at §6, and the outgoing design it
declines as alternative C (line 56). This is the treatment §1A.1 records for Rows 8.64 and 8.65.

*What "reached" does not mean, at this member:* Rows 54.14 (i) and 54.36 (ii) are reached in two parts by one paragraph,
decided against in so far as they are tag-only and agreeing in so far as they mark. How each is re-marked is the
application act's (§0).

**The L2 twins, checked by this sitting.** The same two sentences are the L2 reading file's Rows 45.27 (line 62763) and
45.62 (line 63255), found by sentence search and read at their rows. Each carries only a PROPOSED disposition,
**RELOCATED to *L3 — The read-off facts***, travelling with Row 41.78, and no RULED or RECORDED line, so each is still a
proposal at L2 (the L2 reading file's banner, lines 24–26). The edge-of-span record does not list the L2 reading file
among what it read (its §6). The twins do not conflict with the ruling: L2 proposes sending the statements to L3, and L3's
ruling decides them there.

### 1O.2 Still open — none

**Count:** 4 reached + 0 open = 4, the member's total.

---

## 1P. Member 37 — `cowork_voiceleading_axis_design.md` (3 row-parts)

*Added by the Cowork sitting of 2026-11-04 that booted on entry 530.*

The foot list (reading file line 46330): 37.18, 37.31 (i), 37.46.

The document is the old design of the second axis, voice leading (the reading file's manifest for the member, from line
43059). Of its 241 statements, 181 are proposed RELOCATED (the member's distribution table, line 46326). The three UNPLACED rows are each
graded DIFFERS: Row 37.18 with L3-S42, Row 37.31 (i) with L3-S15, Row 37.46 with L3-S9 (the reading file's list, line
46347). None lies in a register home (the member's marks, lines 46351–46356, name homes only at other rows).

Record short names as in §1, §1A and §1B (**fit and rest** is named in §1B's list).

### 1P.1 Reached by a ruling record — 3 row-parts

Searched as §0 states, every row number with and without the space before its part. Each hit was read at its line.

| Row-part | Record, place | What the record did |
|---|---|---|
| 37.18 | fit and rest, Ruling 1, its rows item 1 (lines 47–49), the user's word *"ratified"* (line 30) | **HISTORICAL**: the old rule that the harmonic-grouping unit is always the punctuation-span and never "phrase" is replaced by the charter's L3 block and L3-S42, which keep the two senses apart by two names rather than by banning the word. The record's §2 (line 70): *"Row 37.18 is to be marked HISTORICAL in the reading file"*, at the application dispatch |
| 37.31 (i) | cadence placement, Ruling 2 item a (line 95), the user's word *"yes"* (line 91) | derivation ratified: *"the cadence is L3's, read off L2's decided chords at L3's decided phrase ends, not detected by the old function layer"* — with Rows 8.11 (ii), 8.59 (ii), 8.101 (ii), 9.89 (iii); the row is also among the thirteen DIFFERS rows the record lists at its §0 (line 14) |
| 37.46 | phrase units, Ruling 2 item e (line 98), the user's word *"yes"* (line 78) | derivation ratified: *"no conflict of substance with L3-S9: reading per-voice surface cues as phrase evidence is not modelling voice leading, which the framework gives its own axis. Documentation only."* |

1 + 1 + 1 = 3.

*What "reached" does not mean, at this member:* the ratified item for Row 37.46 names **no disposition**. It finds the
DIFFERS grade to be no conflict of substance and stops there. The cadence-placement item for Row 37.31 (i) likewise names
none. How each row is re-marked is the application act's (§0); this inventory does not pick a disposition for either.

No later record was found carrying any of the three as UNPLACED. The only other hits are the fit-and-rest surfaces, on
the way to Ruling 1 (first cut, its §2 among other lines; second cut line 123; third cut lines 16, 30, 100–104 and 121), which agree with it.

**The L2 twins, checked by this sitting.**
- **Row 37.18:** the first fit-and-rest surface (§2, line 134) read its twin, the L2 reading file's Row 46.12, ruled
  RELOCATED to L3 by nothing-from-L3 Ruling 5; it *"moved the row to this layer; it did not decide the word"*. Not
  re-read here.
- **Row 37.31 (i):** the same sentence is the L2 reading file's Row 46.24 (line 64143), found by sentence search and read
  at its row. Its claim (i) carries the ruled line *"RELOCATED to L3 — The read-off facts — as proposed"*
  (nothing-from-L3 Ruling 5, line 64153). The cadence placement record does not say that it read the twin. The twin does
  not conflict with the ruling: L2 sent the cadence to L3, and L3's Ruling 2 item a decides it there.
- **Row 37.46:** the L2 reading file lists the same sentence only under *not a statement* (line 65843, *"a defense: the
  document's motivation"*), so it has no twin row.

### 1P.2 Still open — none

**Count:** 3 reached + 0 open = 3, the member's total.

---

## 1Q. Member 50 — `cowork_layer1_note_model_design.md` (2 row-parts)

*Added by the Cowork sitting of 2026-11-04 that booted on entry 531.*

The foot list (the member's distribution table, reading file line 68233): 50.2 (i), 50.20.

The document is the old design of the note model that the old *Architectural Layer 1* builds (the member's heading,
reading file line 67448; Row 50.21, line 67993). Both UNPLACED row-parts are graded THE DERIVATION IS SILENT (the
member's current-text axis, lines 68238–68247). Neither lies in a register home: the member's marks (lines 68254–68258)
say no home lies inside the tabulated ranges, and the four retired entries homed in the document are homed in the cut.

### 1Q.1 Reached by a ruling record — none

Searched as §0 states, each row number with and without the space before its part, and as a bare number: no row of this
member is named in the L3 ruling records or the `cowork_l3_*` surfaces. A search of the same records and surfaces for
*chord-symbol track*, *chord track*, *caller's responsibility* and *rebuild* found two hits, both for *rebuild* and
neither on these rows' subjects: the key-areas record line 106 (*"Row 3.2 calls that layer a planned rebuild"*, of the grouping layer) and the
mass-and-status record line 103 (*"rebuildable by a consumer"*).

### 1Q.2 Still open — 2 row-parts, in two groups

Each was read at its §6 entry (line given).

**(A) Where the tool's chord annotations are written — 1.** The reading file's ground: *"read as at Row 4.6: the staff a
display writes its annotations to is a display concern, and no charter of `FRAMEWORK.md` §5 is a display layer"*.

| Row-part (line) | Subject, in plain words |
|---|---|
| 50.2 (i) (67642) | The chord-symbol track is the staff the tool's chord annotations are written to, not a sounding musical part. (Part (ii), how the track is detected, is QUARANTINED with an audit question; part (iii), its notes kept and marked ineligible, is RELOCATED to L1.) |

**(B) Who decides on and requests a rebuild of the note model — 1.** The reading file's ground: *"read as at Row 4.16 and
§6.48's placement (m): the caller named is the application's score editor and its integration code, and no charter of
`FRAMEWORK.md` §5 names the application's interfaces"*.

| Row-part (line) | Subject, in plain words |
|---|---|
| 50.20 (67974) | Deciding that the note model must be rebuilt, and requesting that rebuild, is the caller's responsibility: the score editor and its integration code. |

1 + 1 = 2.

**The L2 twins, checked by this sitting.** Both sentences were found by exact sentence search in the L2 reading file and
read at their rows. Neither row carries a RULED or RECORDED line, so each is still a proposal at L2 (the L2 reading
file's banner, lines 24–26).
- **Row 50.2:** the L2 reading file's Row 51.3 (line 69620), tabulated there as one claim, proposed **RELOCATED to *L0 —
  The notated record*** (the input contract), travelling with Row 17.36 (not read by this sitting).
- **Row 50.20:** the L2 reading file's Row 51.26 (line 69908), proposed **RELOCATED to *L0 — The notated record***,
  travelling with Row 51.14 (not read by this sitting).

**The D-599 note (preliminary, not a placement).**
1. **Group A joins the display rows** (§1H group A, §1I.3 group A, §1J.3 group D) on the reading file's own ground, and
   display Ruling 1 part A bears on it as on them. Two things for the surface to weigh: the claim says where the tool
   writes its output into the score, which may be the application's concern rather than a display convention; and the
   L2 twin proposes L0 for the whole sentence. **To be tested; not certain.**
2. **Group B joins the code-interface rows** (§1H group B, §1I.3 group B) on the reading file's own ground. Its
   neighbour in the same bullet, Row 50.21 (*"Architectural Layer 1 only builds the note model, or widens it, when it is
   told to"*, line 67991), is proposed RELOCATED to L0 in the L3 reading file, and the L2 twin proposes L0 for Row 50.20
   itself. So L0 is a lead on the record beside the reading file's ground. **To be tested; not certain.** A genuine
   placement is possible.

**Count:** 0 reached + 2 open = 2, the member's total.

---

## 1R. The single rows — members 9, 10, 12, 21, 22, 32, 47, 52 and 56 (one row-part each, 9)

*Added by the Cowork sitting of 2026-11-04 that booted on entry 531.*

The nine row-parts, as entries 530 and 531 §3 list them: 9.89 (iii), 10.9, 12.35 (iii), 21.157, 22.58 (i), 32.1,
47.44 (iii), 52.11 (iii), 56.24. Each row was found by its exact heading in the reading file and read at its §6 entry
(line given); each row number was searched as §0 states, and as a bare number. The L2 twin was looked for by an exact
sentence (or a fragment of it) in the L2 reading file and, where found, read at its row.

### 1R.1 Reached by a ruling record, named by number — 1 row-part

| Row-part (line) | Record, place | What the record did |
|---|---|---|
| 9.89 (iii) (12599) | cadence placement, Ruling 2 item a (line 95), the user's word *"yes"* (line 91); also among the rows the record lists at its §0 (line 14) | derivation ratified: *"the cadence is L3's, read off L2's decided chords at L3's decided phrase ends, not detected by the old function layer"* — with Rows 8.11 (ii), 8.59 (ii), 8.101 (ii), 37.31 (i). How the row is re-marked is the application act's (§0). |

The L2 twin is Row 8.94 (L2 reading file line 17235), the whole sentence as one row: *RECORDED DISPOSITION* QUARANTINED
(the publication-to-next-layer record, §1d), a derivation, not a ruling. Recorded here as a bearing; this inventory does
not judge how the two combine.

### 1R.2 Reached in substance by phrase-ends Ruling 1's wording, but not named by number — 1 row-part

| Row-part (line) | Subject, in plain words |
|---|---|
| 10.9 (14606) | Terms table: the punctuation-span is the grouping layer's *"surface-punctuation-delimited"* span. DIFFERS with L3-S8 (*"No item of evidence forces or forbids a phrase end"*); the reading file's ground names Row 8.14 (ii), where the same unit's definition is placed. |

The same shape as Row 8.14 (ii) (§1A.2). **A candidate derivation — to be confirmed by number on a surface, not asked as a
choice.** The L2 twin is Row 6.8 (L2 reading file line 10262), ruled **RELOCATED to *L3 — The read-off facts*** by
nothing-from-L3 Ruling 5 **[the ruled line checked; the L2 record not opened]**; no conflict: L2 sent the unit to L3.

### 1R.3 Still open — 7 row-parts

| Row-part (line) | Subject, in plain words | The reading file's ground | The L2 twin |
|---|---|---|---|
| 12.35 (iii) (19546) | Choosing not to compute a possibility measured to be worthless is not information loss. | A general reading of #12 applied to the shelved joint step; names no L3 fact; no charter owns a reading of a guiding principle. | The sentence is listed in the L2 reading file only under *not a statement*, *"a defense of Row 15.30"* (line 28869). |
| 21.157 (29722) | The planned orchestration layer must carry the fields taken from a written chord symbol through, whichever engine produced the result. | A rule binding a planned orchestration layer, which no charter names. | None found (two sentence-fragment searches). |
| 22.58 (i) (31590) | Whether the augmented-sixth labels of the Roman-numeral rendering should depend on the style preset is open. | L3-S5 (i) speaks to the augmented sixth's chord symbol, not to its Roman-numeral label or a preset. | None found (two sentence-fragment searches). |
| 32.1 (36092) | The product's core scope: the capabilities that must be built. | No charter names the product's scope. | Row 34.1 (line 47528), **ruled** (tail scope and single rows, Ruling 2): RELOCATED to *the uncertainty surface* for *"musical language detector and graceful degradation"*, **HISTORICAL** for the rest as the product's scope status **[the ruled line checked; the L2 record not opened]**. |
| 47.44 (iii) (65508) | What of the old segment-first machinery moves to the grouping layer and what is deleted is decided as that layer is built. | A decision about which of the older stack's code is moved or deleted, which no charter names. | Row 42.90 (line 58469), proposed only; it tabulates claims (i) and (ii) and not this clause. |
| 52.11 (iii) (68873) | The second notation entry point (the single-note surface) is in the scope of the record contract, both seams reading the joint estimator's record. | As at Row 4.16 and §6.48's placement (m): which application interfaces read which record. | None found (three sentence-fragment searches). The L3 records' hits for *52.11* (mass-and-status record, lines 39 and 62) are the L2 reading file's Row 52.11, not this row. |
| 56.24 (71540) | The surface-cue strength rises with both the degree of local change and the size of the value; a large gap is a stronger boundary. | Two placements on the record: L1 (Rows 36.41, 36.118) and L3 for the computed half (the L0/L1 comparison's Ruling 48). | Row 40.43 (line 53607), proposed **RELOCATED to *L3 — The read-off facts***, travelling with Row 6.7 (ii). |

**The D-599 notes (preliminary, not placements).**
1. **Row 12.35 (iii)** restates **D-297** (`DECISIONS.md` line 290, read: *"never computing a possibility is not
   information loss; only discarding a computed one is"*, LIVE, 2026-08-02 · user, home `ARCHITECTURE.md`). The row's
   document, `cowork_engage_arc_plan.md` (member 12), is not that home, so the architecture-rules precedent (rows adopted
   on their register homes) does not carry to it as it stands. A candidate derivation on D-297 is possible. **To be
   tested; not certain.**
2. **Row 21.157** joins the code-structure rows (§1H group B, §1I.3 group B, §1Q group B) on the kind of its ground. Its
   neighbour Row 21.156 (*"score metadata rather than engine metadata"*) is proposed RELOCATED to L0, AGREES with L3-S29.
   **To be tested; not certain.**
3. **Row 22.58 (i)** joins the display rows (§1H group A, §1I.3 group A, §1J.3 group D, §1Q group A). The chord symbol
   record's §2 (e) (OQ-L3-9, the augmented-sixth respelling *"a display's own act"*, as §1I.3 note 1 relays it) and
   architecture-rules Ruling 1 part B (as §1J.3 note 2 relays it) bear on it without reaching it. **To be tested; not
   certain.**
4. **Row 32.1** has a ruled twin: on the twin precedent (§1K group A), a candidate derivation travelling with Row 34.1.
   The same weak point as there: whether an L3 surface may apply an L2 ruling without one of its own. **To be tested;
   not certain.**
5. **Row 47.44 (iii)** is a plan about the old code's fate; the L2 twin calls the neighbouring claim a build state. A
   genuine placement is possible (HISTORICAL as a plan is one candidate). **To be tested; not certain.**
6. **Row 52.11 (iii)** joins the code-structure rows with Row 21.157 (note 2).
7. **Row 56.24** has two placements on the record, between which the reading file *"cannot defend one in one sentence"*; the L2 twin
   proposes L3. A genuine placement for the user is possible unless the surface finds that Ruling 48 already decides it.

**Count:** 1 reached by number + 1 reached in substance + 7 open = 9, the single rows' total.

---

## 1S. Member 57 — the L2 transfer input, part 1 of 5: the foot table at reading file line 73993 (19 row-parts)

*Added by the Cowork sitting of 2026-11-05 that booted on entry 532.*

**The member.** Member 57 is the L2 reading file's §10, *"The TRANSFER LIST — every RELOCATED row, by target
charter"*: the L2 rows the L2 comparison sent to L3 (the member's manifest, reading file line 71701 onwards). Each row
here is an L2 row, tabulated again against the L3 derivation. The member's UNPLACED row-parts stand in **five foot
tables**, not one: at lines 73993 (19), 75342 (24), 76579 (34), 77808 (20) and 78371 (10); 19 + 24 + 34 + 20 + 10 = 107.
This section takes the first table only. The other four are the next parts, each a stopping point.

The foot list (line 73993): 57.50, 57.60 (i), 57.97, 57.107 (i), 57.107 (ii), 57.108, 57.109, 57.110, 57.111, 57.112,
57.113, 57.114, 57.115, 57.116, 57.117, 57.118, 57.124 (i), 57.124 (ii), 57.153 (ii).

**The search.** Every staged L3 ruling record (the rulings folder's files with `l3` in the name, 2026-10-14 to
2026-11-04) and every `cowork_l3_*` surface was searched once for any number of the form *57.n*. Every hit on a row of
this table was read at its line. The rows were found in the reading file by one pattern listing only this table's row
numbers as exact headings. **The L2 side of each row** (whether the L2 move to L3 is ruled or only proposed) was read at
the L2 row's own block in the L2 reading file, found by its exact heading.

### 1S.1 Reached by a ruling record, named by number — 2 row-parts

| Row-part | Record, place | What the record did |
|---|---|---|
| 57.50 | phrase ends, Ruling 1 (documentation, line 85) | named by number among the rows recorded as overtaken by the charter and Ruling 48 |
| 57.60 (i) | cadence type, Ruling 2 (line 64) | decided against *"in so far as they fix one list as the only one"*; its list remains a candidate for a declared vocabulary. The same record's line 74 names Row 57.60 (ii) only as a mapping *"only proposed"*, which is not this row-part |

1 + 1 = 2. Neither row was re-read at its §6 entry by this sitting; the record names each by number.

*Named in a record but NOT counted as reached on that naming:* Row 57.60 also appears in the cadence-type record's list
of row headings read (line 17), its surface (lines 38, 94, 101, 106, 145) and the cadence-vocabulary-point record
(lines 21, 44, 86), which cites Ruling 2 for it.

### 1S.2 Reached in substance by phrase-ends Ruling 1's wording, but not named by number — 1 row-part

| Row-part (line) | Subject, in plain words |
|---|---|
| 57.153 (ii) (73625) | The old boundary-strength profile *"then peaks are picked"*. DIFFERS with L3-S8; the reading file grounds it *"as Rows 36.37 (ii) and 36.61"*, both in §1B.2 group (a). Part (i), the profile itself, is proposed RELOCATED to L1. |

The same shape as §1B.2 group (a), peak-picking: phrase-ends Ruling 1's *"The method rows (peak-picking, …) are the rows
Ruling 1 decides against"*. **A candidate derivation — to be confirmed by number on a surface, not asked as a choice.**
The L2 row (Row 40.36, L2 reading file line 53523) carries only a proposed RELOCATED to L3, no ruled line.

### 1S.3 Still open — 16 row-parts, in three groups

Each was read at its §6 entry (line given). Every one is graded THE DERIVATION IS SILENT. No ruling record or `cowork_l3_*`
surface names any of them.

**(A) The catalog and its recognition — ground *"as at Rows 38.18 (i) and 38.80 (i)"* (Row 57.97) or *"as at Row 38.20"*
(the others) — 6**

| Row-part (line) | Subject, in plain words | The L2 row (L2 reading file line) |
|---|---|---|
| 57.97 (73039) | The planned progression-schema recognizer recognises multi-chord patterns and substitutions from the catalog over the decided chords and annotates them. | 22.98 (i) (34482): **ruled** RELOCATED to L3, nothing-from-L3 Ruling 5 |
| 57.107 (i) (73080) | The progressions and substitutions form an independent knowledge-base component: a static, curated catalog with a read-only query returning ranked candidates. | 26.1 (i) (43798): proposed only |
| 57.107 (ii) (73080) | The catalog is read both ways: forward for the analysis, predictively for a future chord-suggestion tool. Also grounded *"as at Row 38.21 (ii)"* (§1F.4 group C). | 26.1 (ii): **ruled** RELOCATED to L3, nothing-from-L3 Ruling 5 |
| 57.108 (73129) | It is reference knowledge the layers and future tools query, not a pipeline layer. | 26.2 (43824): proposed only |
| 57.109 (73167) | Its entries carry their provenance in established theory, not a validation status. | 26.3 (43837): proposed only |
| 57.111 (73240) | The dictionaries of the old §7.1 to §7.3 are the data; the catalog is the queried component over them. | 26.6 (43877): proposed only |

**(B) Substitution — ground *"as at Row 46.24 (and Row 44.4)"*: no charter names the relation of a chord to the chord
it stands in for — 8**

| Row-part (line) | Subject, in plain words | The L2 row (L2 reading file line) |
|---|---|---|
| 57.110 (73205) | Substitution works on every functional family; only the tritone substitution is specific to the dominant. | 26.5 (43864): proposed only |
| 57.112 (73275) | For every chord type, the substitution network defines the substitutions available. | 26.7 (43891): proposed only |
| 57.113 (73305) | The tritone substitution. | 26.8 (43904): proposed only |
| 57.114 (73335) | The secondary dominant. | 26.9 (43917): proposed only |
| 57.115 (73365) | The backdoor dominant. | 26.10 (43930): proposed only |
| 57.116 (73395) | Modal interchange. | 26.11 (43942): proposed only |
| 57.117 (73425) | The relative substitution. | 26.12 (43955): proposed only |
| 57.118 (73455) | Each substitution carries its voice-leading implications and style weights. The reading file adds that these touch the voice-leading axis and the style system, neither defended as the whole subject. | 26.13 (43967): proposed only |

**(C) A reader outside the analysis — 2.** Ground: the sentence concerns a planned bridge to a language model, outside
the analysis; no charter names a reader outside the analysis.

| Row-part (line) | Subject, in plain words | The L2 row (L2 reading file line) |
|---|---|---|
| 57.124 (i) (73527) | The language model does not derive the harmony again from the pitches. | 36.1 (47766): **ruled** RELOCATED to L3, nothing-from-L3 Ruling 5 (*"Readers of the published record"*), the whole sentence |
| 57.124 (ii) (73527) | It receives the analysis as given. | as (i) |

6 + 8 + 2 = 16.

**The D-599 notes (preliminary, not placements).**
1. **Groups A and B are the catalog-and-recognition family** of §1C, §1D, §1F groups A to C, §1G, §1N, §1A.3, §1E.3
   group A and Row 7.85. Group A is the same subject as §1N (the same section of `ARCHITECTURE.md`, its §7); group B is
   the same kind as §1C group C. Where the L2 move is ruled (Rows 57.97 and 57.107 (ii)), it is the nothing-from-L3 Ruling
   5 that §1N note 3 records: it sent the subject to L3 and, as that note relays from the record, decides nothing of L3's
   design. That is a bearing, not a reach. The rest are L2 proposals only.
2. **Group C is near §1F group C** (a future chord-suggestion tool, outside the analysis); here the tool outside the
   analysis is a reader of it, a language model. The reading file places
   it on content and says it departs from §6.33's listing of the same sentence as *not a statement*. The L2 ruling sent
   the sentence to L3 under *"Readers of the published record"*. The reading file names the shape of L3-S30 and L3-S39
   (consumers read and never re-derive), which bind L3 itself, not a reader outside it. A retired entry, **D-142**
   (*"the model never re-derives harmony"*, status *deferred*, as the reading file relays it at the row), lies at the
   sentence's lines. No record found settles it. **A genuine placement is possible.**
3. **Hits for the later parts, recorded for the next sitting, not yet read at their lines:** Rows 57.249 and 57.290
   (phrase ends record line 85, the same documentation list as Row 57.50); 57.315 (sections record lines 113, 215);
   57.320 (sections record lines 63, 215); 57.372 (chord symbol record lines 85, 101); 57.502 (cadence placement record
   lines 16, 108; phrase ends record line 92, where it is carried to the cadence family as *"57.502 (i)"*). The search
   also found rows of this member that are in none of its five foot lists (57.119, 57.126, 57.157, 57.259, 57.278,
   57.318, 57.322, 57.352, 57.353, 57.354, 57.369), so not part of this inventory.

**Count:** 2 reached by number + 1 reached in substance + 16 open = 19, the first table's total.

---

## 1T. Member 57 — the L2 transfer input, part 2 of 5: the foot table at reading file line 75342 (24 row-parts)

*Added by the Cowork sitting of 2026-11-06 that booted on entry 533.*

The foot list (line 75342): 57.249, 57.290, 57.315 (i), 57.315 (ii), 57.320 (i), 57.362, 57.363, 57.364, 57.365,
57.366 (i), 57.368, 57.370, 57.371, 57.372, 57.373 (i), 57.373 (ii), 57.377, 57.498, 57.499, 57.500, 57.501, 57.511,
57.513, 57.514.

**The search.** Not rerun: the rulings folder's listing of 2026-11-06 shows no `l3` record dated after 2026-11-04, so
§1S note 3's hits stand for this part (`ratification_surfaces` was not listed by this sitting, so a `cowork_l3_*`
surface added since §1S's search would not have been seen). Each hit on a row of this table (57.249, 57.290, 57.315, 57.320, 57.372) was read
at its line. The rows were found in the reading file by one pattern listing only this table's twenty-two row numbers as
exact headings, and each entry was read whole. **The L2 side of each row** was read at the L2 row's own block in the L2
reading file, found by one pattern listing only those twenty-two L2 row numbers as exact headings.

### 1T.1 Reached by a ruling record, named by number — 5 row-parts

| Row-part (line) | Record, place | What the record did | The L2 row (L2 reading file line) |
|---|---|---|---|
| 57.249 (74147) | phrase ends, Ruling 1 (documentation, line 85) | named by number among the rows recorded as overtaken by the charter and Ruling 48 | 41.33 (55620): **ruled** RELOCATED to L3, nothing-from-L3 Ruling 5 |
| 57.290 (74323) | phrase ends, Ruling 1 (documentation, line 85) | the same list | 41.107 (56544): proposed only |
| 57.315 (i) (74374) | sections, Ruling 2 (documentation, line 113) | named among the ten rows that call the grouping flat, recorded as decided against | 41.122 (56738): proposed only |
| 57.315 (ii) (74374) | sections, Ruling 2 (line 113) | the same | as (i) |
| 57.320 (i) (74451) | sections, Ruling 1 (documentation, line 63) | named among the twelve rows that put sections outside the layer, recorded as overtaken by the charter | 41.47 (55804): proposed only |

2 + 2 + 1 = 5. Each row was read at its §6 entry: 57.249 and 57.290 DIFFER with L3-S8 (the grouping's signals all
computed earlier; the layer held to assembly); 57.315 DIFFERS with L3-S22 at both parts (*"Flat grouping, not
hierarchical"*); 57.320 (i) DIFFERS with L3-S22 (sections kept out of the grouping's core).

*Named in a record but NOT counted as reached on that naming:* Rows 57.315 and 57.320 also stand in the sections
record's list of rows read (line 215). Row 57.372 is named by the chord symbol record at §2 (g) (line 85) among the rows
*"to be read in the investigation"* of OQ-L3-1 (the declared convention for L2's degree field in minor), *"not read at
their entries"*, and in its check, item 6 (line 101); that is a reading list for an investigation, not a placement.

### 1T.2 Still open — 19 row-parts, in four groups

Each was read at its §6 entry (line given). No ruling record or `cowork_l3_*` surface places any of them.

**(A) The modal colour of a tonality run, published as counts — ground *"read as at Row 48.32 (ii)"*: a count per
tonality run of the chromatic inflections of each degree, which no charter of `FRAMEWORK.md` §5 lists among its
publications; THE DERIVATION IS SILENT at each — 10**

| Row-part (line) | Subject, in plain words | The L2 row (L2 reading file line) |
|---|---|---|
| 57.362 (74636) | By the decision of 2026-07-19, the un-rounded modal reading is published for the presentation layer. | 47.14 (66154): proposed only |
| 57.363 (74669) | The un-rounded modal reading is published. | 47.27 (i) (66352): proposed only (the ruled line there is claim (ii)'s) |
| 57.364 (74703) | It is published beside the tonality as a fact of its own. | 47.28 (ii) (66366): proposed only (the ruled lines there are claims (i) and (iii)) |
| 57.365 (74737) | By the user's condition, part of the decision, the un-rounded reading is preserved and published. | 48.31 (67132): proposed only |
| 57.366 (i) (74777) | The modal-variant evidence is published as a derived fact, so the presentation layer can show a modal name by preference. Part (ii) is proposed RELOCATED to L2. | 48.32 (67144): proposed only |
| 57.370 (74885) | The modal reading is the ratified un-rounded publication of modal colour. | 49.7 (67719): proposed only |
| 57.371 (74917) | For each tonality run and each degree of its scale, the sounding duration and onset count of every chromatic inflection observed. | 49.28 (68021): proposed only |
| 57.372 (74960) | These counts are the whole publication, un-rounded and set by no hand. | 49.29 (68033): proposed only |
| 57.373 (i) (75003) | The presentation layer may format a reading (*"Dorian-leaning"*) from the counts. | 49.30 (68045): proposed only |
| 57.373 (ii) (75003) | The published fact is the counts, with their establishment status. | as (i) |

**(B) The old output record and what the application reads from it — 4.** Ground: *"read as at Row 48.1 (i)"* (57.368,
57.377): no charter holds the code's interfaces (57.368) or what a display shows of the published lists (57.377); or
(57.513, 57.514) one surface carrying the posterior, the derived chord facts and the presentation facts together, where
no charter lists the presentation facts (57.513) or holds that record whole (57.514). THE DERIVATION IS
SILENT at 57.368 and 57.377; L3-S1 AGREES at 57.513 and 57.514 as to the derived chord facts.

| Row-part (line) | Subject, in plain words | The L2 row (L2 reading file line) |
|---|---|---|
| 57.368 (74824) | The record is the one output surface the notation path reads. | 49.1 (ii) (67631): **ruled** RELOCATED to L3, nothing-from-L3 Ruling 5 (*"Readers of the published record"*) |
| 57.377 (75049) | A subset of the published lists shown for display is a read the presentation makes downstream. | 49.23 (iii) (67947): **ruled**, the same |
| 57.513 (75249) | The estimator's surface carries what best-inference consumers need: the posterior, the derived chord facts, the presentation facts. | 47.17 (iv) (66196): **ruled** RELOCATED to L3 by L2 chord-as-degree Ruling 2, *"as to the derived chord facts"* |
| 57.514 (75287) | The estimator publishes its own record (segments, tonalities, chord classes, derived chord facts, posterior, presentation facts), and the notation consumers read it. | 47.18 (i) (66218): **ruled**, the same; the record adds that the rest of the list *"is what L2 publishes under L2-S1 and L2-S45, recorded beside the filing and not relocated"* |

**(C) A reader outside the analysis — the language model — 4.** Ground: *"read as at Row 57.124"*: no charter names a
reader outside the analysis. THE DERIVATION IS SILENT at each.

| Row-part (line) | Subject, in plain words | The L2 row (L2 reading file line) |
|---|---|---|
| 57.498 (75088) | The chord symbols from the analysis are in the language model's view. | 54.1 (72487): **ruled** RELOCATED to L3, nothing-from-L3 Ruling 5 (*"Readers of the published record"*) |
| 57.499 (75119) | The chord symbols and Roman-numeral analysis are handed to it per measure. | 54.2 (72501): **ruled**, the same |
| 57.500 (75150) | The inferred tonality and mode are handed to it. | 54.3 (72515): **ruled**, the same |
| 57.501 (75181) | Where the chords change is handed to it. | 54.4 (72529): **ruled**, the same |

**(D) Whether a chord span always lies inside one phrase — 1.** Ground: *"read: the two texts above, as Row 19.39 (ii)"*.
DIFFERS with L3-S8.

| Row-part (line) | Subject, in plain words | The L2 row (L2 reading file line) |
|---|---|---|
| 57.511 (75212) | Chord spans nest in phrase units, so every phrase boundary is a chord-span boundary. L3-S8: *"Every change point and both span edges are candidate phrase ends."* | 43.100 (ii) (60132): **ruled** RELOCATED to L3 by L2 notated-boundary-evidence Ruling 1 |

10 + 4 + 4 + 1 = 19.

**The D-599 notes (preliminary, not placements).**
1. **Group A is one group with §1H group D** (Row 48.32 (ii), the same ground). Two LIVE register entries lie at these
   rows' lines, as the reading file records and as read at their `DECISIONS.md` rows: **D-276** (LIVE, 2026-08-02 · user,
   home `cowork_notation_output_contract.md` §3.4, the lines of Rows 57.371 to 57.373): *"Modal colour is published as
   un-rounded per-degree counts; no mode label is inferred or published anywhere"*; and **D-524** (LIVE, no entry
   ratification shown, home `cowork_joint_estimator_architecture.md` §5a, the lines of Rows 57.365 and 57.366): *"The
   joint state's mode axis is TWO modes — major and composite minor; modal and chromatic colour lives in the pitch
   emission, and the un-rounded reading is published"*. Both titles say the un-rounded reading is published (D-276: as per-degree
   counts); neither title, as read, names the layer that publishes it. The L2 side proposes every group-A row-part
   RELOCATED to L3; none of those L2 row-parts carries a ruled line. **Whether D-276 makes the publication a derivation, leaving only its home to place, is to be
   tested on the surface; not certain.** §1H note 4's *"a genuine placement is possible"* stands until that test.
2. **Group B: the L2 move is ruled for all four**, nothing-from-L3 Ruling 5 or L2 chord-as-degree Ruling 2 — a bearing,
   not a reach, as §1N note 3 records for that Ruling 5. 57.368 and 57.377 go with §1H group B and §1I group B (the
   application's interfaces, read as at Rows 4.16 and 48.1 (i)); 57.377's subject is what a display shows, so display
   Ruling 1 part A (§1H note 2) may also bear on it. For 57.513 and 57.514 the reading file states that a disposition of
   the whole claim *"would choose between its components"*; L3-S1 AGREES as to the derived chord facts. A genuine
   placement is possible.
3. **Group C is one group with §1S group C** (Row 57.124): the same ground and the same L2 ruling.
4. **Group D is one group with §1E.3 group B** (Row 19.39 (ii)), which §1E.3 records as named open by two records,
   span-kinds Ruling 1 part C and architecture-rules §2. The L2 ruled line at Row 43.100 (line 60144) adds: *"how L3's phrases relate to L2's chord spans is
   L3's to state when it reads the phrases off."* §1E.3's test stands: whether L3-S8's wording, ratified with phrase-ends
   Ruling 1, already answers it.
5. **§1S note 3's hits for this part are now read** (57.249, 57.290, 57.315, 57.320, 57.372). The hit left for the later
   parts is 57.502.

**Count:** 5 reached by number + 19 open = 24, the second table's total.

---

## 1U. Member 57 — the L2 transfer input, part 3 of 5: the foot table at reading file line 76579 (34 row-parts)

*Added by the Cowork sitting of 2026-11-06 that booted on entry 534.*

The foot list (line 76579): 57.390, 57.391, 57.392 (ii), 57.393 (i), 57.393 (ii), 57.394, 57.396 (ii), 57.398 (i),
57.398 (ii), 57.399, 57.400, 57.401 (i), 57.401 (ii), 57.402, 57.405, 57.427, 57.428, 57.429, 57.430 (i), 57.430 (ii),
57.431, 57.432, 57.433 (i), 57.433 (ii), 57.434 (ii), 57.435 (i), 57.435 (ii), 57.445 (i), 57.445 (ii), 57.502 (i),
57.503, 57.504 (i), 57.535 (i), 57.535 (ii). They come from twenty-six rows. Twenty-five of those rows quote sentences of
`cowork_progression_schema_dictionary.md` (member 46's document, §1C); Row 57.502 quotes `cowork_architecture_review_2026_07.md`.

**The search.** Not rerun. The rulings folder's listing of 2026-11-06 shows no `l3` record dated after 2026-11-04, and
in the `ratification_surfaces` listing of the same day no `cowork_l3_*` surface carries a modification time later than
2026-11-04, so §1S note 3's hits stand. The one hit on this table, 57.502, was read at its lines. The rows were found in the reading file
by one pattern listing only this table's twenty-six row numbers as exact headings, and each entry was read whole. **The
L2 side of each row** was read at the L2 row's own block in the L2 reading file, found by one pattern listing only
those L2 row numbers as exact headings.

### 1U.1 Reached by a ruling record, named by number — 1 row-part

| Row-part (line) | Record, place | What the record did | The L2 row (L2 reading file line) |
|---|---|---|---|
| 57.502 (i) (76395) | cadence placement, Ruling 2 item e (line 108), carried there from phrase ends §2 (line 92) | ratified as a derivation with Rows 2.15, 2.18 and 7.336: D-495's flat-profile fallback *"loses its subject at L3"*; *"the old fallback rule drops out; no new mechanism"* | 57.8 (73336): **ruled** RELOCATED to L3, nothing-from-L3 Ruling 5 |

At its §6 entry, 57.502 (i) DIFFERS with L3-S8. Part (ii) of the row is QUARANTINED, not UNPLACED, so it is not in
this table.

### 1U.2 Still open — 33 row-parts, in five groups

Each was read at its §6 entry (line given). Every one is graded THE DERIVATION IS SILENT. No ruling record or
`cowork_l3_*` surface names any of them.

**The L2 side, common to most rows.** Rows 57.390 to 57.435 quote L2 rows of member 50 that the L2 reading file's §10
bullet B92 sends to L3 *"travelling with Row 5.91"*. Each of those L2 blocks carries a proposed RELOCATED to L3 and no
ruled line. Row 5.91, which they travel with, is **ruled** RELOCATED to L3 by
nothing-from-L3 Ruling 5 (L2 reading file line 5620: *"Named progressions and sequences, the recogniser and its
catalogue"*). The table gives *"proposed only (with 5.91)"* for these rows. Rows 57.503 and 57.504 quote L2 Row 62.41,
proposed only, travelling with Row 50.2. Row 57.445 quotes L2 Row 50.71, proposed only, travelling with Row 43.99, whose
block was not read.

**(A) The catalog and its recognition — 24.** Grounds, as the reading file gives them: *"as at Row 44.1"* (an entry is a
catalog record), *"as at Row 44.2"* (the functional skeleton), *"as at Row 7.85"* (how the catalog holds its entries),
*"as at Row 38.20"* (the catalog's read-only queries; no knowledge-base component is named), *"as at Row 57.97"* (no
charter names the recognition of a progression schema), or the row's own reading (57.427).

| Row-part (line) | Subject, in plain words | Ground | The L2 row |
|---|---|---|---|
| 57.390 (75512) | An entry is one catalog record, a named convention, of two kinds. | 44.1 | 50.1: proposed only (with 5.91) |
| 57.391 (75548) | A progression entry's functional skeleton: a sequence of scale degrees and chord qualities, relative to the tonality, parameterized by degree. | 44.2 | 50.2: as 50.1 |
| 57.392 (ii) (75584) | A generative slot is instantiated on demand. Part (i) is proposed RELOCATED to L2. | 7.85 | 50.3: as 50.1 |
| 57.393 (i) (75626) | A span is a contiguous run of committed chords, each with its decided function and tonality: the input of the catalog's queries. | 38.20 | 50.4: as 50.1 |
| 57.393 (ii) (75626) | A recognized entry's emitted span is the progression-schema span the older stack's grouping layer hosts. | 57.97 | as (i) |
| 57.394 (75667) | The match value and what it is for a span to realize an entry are the recognition semantics. | 57.97 | 50.5: as 50.1 |
| 57.396 (ii) (75740) | The catalog never defines or re-implements the licensed root motion. Part (i) is proposed RELOCATED to L2. | 7.85 | 50.7: as 50.1 |
| 57.399 (75836) | The browse query: every entry of the active styles. | 38.20 | 50.12: as 50.1 |
| 57.400 (75872) | The recognize query: a span in, the progression entries it realizes out. | 57.97 | 50.13: as 50.1 |
| 57.401 (i) (75907) | The test of realizing: the span's chords match the skeleton's members in order and contiguously, by degree and quality in the span's tonality. | 57.97 | 50.14: as 50.1 |
| 57.402 (75961) | The expand query: the generative slots for a scale degree. | 38.20 | 50.16: as 50.1 |
| 57.427 (76034) | Glossary: a progression is an ordered succession of chords or functions. | own reading: the derivation uses the word only of a cadential progression (L3-S9 (ii), L3-S16) and defines no progression in general | 50.60: as 50.1 |
| 57.428 (76069) | Glossary: a schema is a named, recurring progression of several chords. | 7.85 | 50.61: as 50.1 |
| 57.430 (i) (76138) | Glossary: an entry is one catalog record, a single named convention. | 44.1 | 50.63: as 50.1 |
| 57.430 (ii) (76138) | It is of two kinds, a progression entry and a substitution entry. | travels with (i) | as (i) |
| 57.431 (76176) | Glossary: the functional skeleton. | 44.2 | 50.64: as 50.1 |
| 57.433 (i) (76246) | Glossary: the span, a contiguous run of committed chords. | as Row 57.393 (i) | 50.66: as 50.1 |
| 57.433 (ii) (76246) | The span is the input to the recognize and suggest queries. | 38.20 | as (i) |
| 57.434 (ii) (76284) | Glossary: a generative slot is instantiated on demand, not enumerated. Part (i) is proposed RELOCATED to L2. | 7.85 | 50.69: as 50.1 |
| 57.435 (i) (76325) | Glossary: the match value measures how well an input realizes an entry. | 57.97 | 50.70: as 50.1 |
| 57.435 (ii) (76325) | The return is ranked by it; the consumer thresholds and weights it. | travels with (i) | as (i) |
| 57.445 (i) (76361) | The analysis direction reads an existing progression to recognize or disambiguate it. | 57.97 | 50.71: proposed only (with 43.99) |
| 57.503 (76441) | A progression entry's functional skeleton is a sequence of (scale degree, chord quality) pairs relative to the tonality. | 44.2 | 62.41 (i) (74629): proposed only (with 50.2) |
| 57.504 (i) (76480) | Being relative to the tonality, one entry instantiates in every tonality. Part (ii) is proposed RELOCATED to L2. | 7.85 | 62.41 (ii): as (i) |

**(B) Substitution — ground *"as at Row 44.4"*: no charter names the relation of a chord to the chord it stands in for —
3**

| Row-part (line) | Subject, in plain words | The L2 row |
|---|---|---|
| 57.401 (ii) (75907) | A chord may match a skeleton member through a substitution entry's mapping; the returned entry carries that mapping. | 50.14: proposed only (with 5.91) |
| 57.429 (76103) | Glossary: a substitution replaces a chord with another that fills the same functional slot. | 50.62: as 57.401 (ii) |
| 57.432 (76212) | Glossary: a substitution mapping maps a substituted surface chord to the function it replaces. | 50.65: as 57.401 (ii) |

**(C) How the catalog and the licensing grammar relate — 3.** Ground: *"as at Row 7.85"*: no charter's subject is a
catalog of named progressions, so none is that catalog's relation to the grammar. The reading file reads these sentences
as stating a rule, not a property of the built code, and says this departs from §6.46's items 3 and 6, which list them as
*not a statement*.

| Row-part (line) | Subject, in plain words | The L2 row |
|---|---|---|
| 57.398 (i) (75784) | The catalog and the grammar are not derived from each other. Marked SEEN (D-406). | 50.9: proposed only (with 5.91) |
| 57.398 (ii) (75784) | The only coupling between them is the consistency test, which runs one way, from the catalog to the grammar. | as (i) |
| 57.405 (75998) | The two are coupled one way by the consistency test (travels with 57.398 (ii)). | 50.22: as 57.398 (i) |

**(D) The composition direction — ground *"as at Row 38.21 (ii)"*: no charter names a tool that suggests chords — 1**

| Row-part (line) | Subject, in plain words | The L2 row |
|---|---|---|
| 57.445 (ii) (76361) | The composition direction reads a span to suggest what could follow, precede or replace it. | 50.71: proposed only (with 43.99) |

**(E) The catalog's idiom tags — ground *"as at Row 44.11"*: the tags are attributes of the catalog's entries — 2**

| Row-part (line) | Subject, in plain words | The L2 row |
|---|---|---|
| 57.535 (i) (76524) | The idiom tag is the multi-valued set of idioms on an entry, from the ratified five-idiom taxonomy shared with the presets. | 50.67 (69314): **ruled** RELOCATED to L3 by L2 tail-style-and-idiom Ruling 2, *"travelling with Row 5.91"*; the record adds *"The idiom set itself stays at `ARCHITECTURE.md` §6.7 (Ruling 1)"* |
| 57.535 (ii) (76524) | An entry also carries two orthogonal cross-attributes, mode and chromaticism. | as (i) |

24 + 3 + 3 + 1 + 2 = 33.

**The D-599 notes (preliminary, not placements).**
1. **Groups A and B are the catalog-and-recognition family** of §1S note 1. Their sentences stand in member 46's
   document but in its cut (the terms table, §3, §4 and the glossary), so member 46 (§1C) did not tabulate them; the
   reading file says so at each row. Where the L2 move is ruled (Row 5.91, which these rows travel with), it is the nothing-from-L3 Ruling 5 of §1N note 3:
   a bearing, not a reach.
2. **Group C: D-406** (LIVE, 2026-08-03 · user, home `cowork_progression_schema_dictionary.md` §1, read at its
   `DECISIONS.md` row): *"The catalog owns the NAMED progressions and substitutions; the pairwise licensing grammar is
   owned by the function layer — the two are never derived from each other"*. Its title states group C's claim (i). Its
   title does not mention the consistency test, which group C's claim (ii) and Row 57.405 state. Whether D-406 settles
   group C, or only its claim (i), depends on the family's answer for the catalog. **To be tested on the surface; not
   certain.**
3. **D-410** (DEFERRED, 2026-08-03 · user, home the same document §4, read at its `DECISIONS.md` row): *"The first
   version matches EXACTLY AND WHOLE; the partial matcher is deferred …"*. Its home overlaps the closing clause of Row
   57.401, as the reading file records; recorded as a fact beside group A and group B, not a reach.
4. **Group D is one group with §1F group C** and with Row 57.107 (ii) (§1S group A): a tool that suggests chords,
   outside the analysis.
5. **Group E is one group with §1G** (the idiom tag of a catalog entry). The L2 ruling sends the tag to L3 with the
   catalog and keeps the idiom set itself at `ARCHITECTURE.md` §6.7.
6. **Row 57.427** is grounded on its own reading, not on a member's row. It goes with group A unless the family's surface
   finds a reason to treat a general definition of a progression apart from the catalog.
7. **§1S note 3's hits are now all read** (57.249, 57.290, 57.315, 57.320 and 57.372 at §1T; 57.502 here). None is left
   for parts 4 and 5.

**Count:** 1 reached by number + 33 open = 34, the third table's total.

---

## 1V. Member 57 — the L2 transfer input, part 4 of 5: the foot table at reading file line 77808 (20 row-parts)

*Added by the Cowork sitting of 2026-11-06 that booted on entry 535.*

The foot list (line 77808): 57.448, 57.451, 57.453, 57.454, 57.455, 57.467 (i), 57.470 (ii), 57.478, 57.485,
57.487 (ii), 57.489 (i), 57.489 (ii), 57.490 (i), 57.493 (i), 57.493 (ii), 57.494 (i), 57.494 (ii), 57.495 (i),
57.495 (ii), 57.496. They come from sixteen rows, all quoting `cowork_progression_schema_design.md` (member 44's
document, §1D): sentences of its §3, §4.2, §4.5 and §9 item 2, which lie in member 44's cut, and four sentences of its
§6 dependency map (Rows 57.451, 57.493, 57.494, 57.495), which §6.44 lists under *not a statement* as its items 15, 14,
16 and 17. The group's header (read at reading file lines 76660–76754) reads those four as rules, departing from §6.44, and
states the alternative, QUARANTINED, as not taken (its case (5)).

**The search.** Not rerun. In the rulings folder's listing of 2026-11-06 no `l3` record is dated after 2026-11-04, and in
the `ratification_surfaces` listing of the same day no `cowork_l3_*` surface other than this inventory carries a
modification time later than 2026-11-04, so §1S note 3's hits stand; §1U note 7 records that none of them is on parts
4 and 5. §1D.1's subject-word search (*schema*, *catalog*, *substitution*, *additive*, and the rest listed there) found
no ruling taking up the recognition of a named progression, its catalog or its span; it was not rerun. The rows were
found in the reading file by one pattern listing only this table's sixteen row numbers as exact headings, and each
entry was read whole. **The L2 side of each row** was read at the L2 row's own block in the L2 reading file, found by
one pattern listing only those fifteen L2 row numbers as exact headings (L2 Row 53.79 serves two rows).

### 1V.1 Reached by a ruling record — none

### 1V.2 Still open — 20 row-parts, in three groups

Each was read at its §6 entry (line given). Every one is graded THE DERIVATION IS SILENT. §1S note 3's search of the
`l3` ruling records and `cowork_l3_*` surfaces found none of them. The other claims of Rows 57.467, 57.470, 57.487 and 57.490 are RELOCATED (to
L2's tonal reading, or to the uncertainty surface), not UNPLACED, so they are not in this table.

**The L2 side.** Five of the L2 rows carry a **ruled** RELOCATED to L3 by nothing-from-L3 Ruling 5 (*"Named
progressions and sequences, the recogniser and its catalogue"*): 53.21, 53.22 (both claims), 53.23, 53.28 and 53.35. The
others carry a proposed RELOCATED to L3 and no ruled line, each travelling with a row named in the table. Of those
rows travelled with, Row 5.91 is ruled (§1U) and Row 50.9 is proposed only (§1U, group C); the blocks of Rows 50.76 (ii),
50.41 (i) and 43.35 (i) were not read.

**(A) The catalog and its recognition — 9.** Grounds, as the reading file gives them: *"as at Row 57.97"* (no charter
names the recognition of a progression schema), *"as at Row 44.21"*, *"as at Row 44.20 (i)"* / *"Row 8.52 (iii)"* (the
span a recognized progression covers), *"as at Row 44.37 (i)"* / *"Row 8.51"* (the recognition additive over what it
reads), or *"as at Row 7.85"* (no charter's subject is a catalog of named progressions).

| Row-part (line) | Subject, in plain words | Ground | The L2 row (L2 reading file line) |
|---|---|---|---|
| 57.448 (76758) | Where nothing is recognized, nothing is produced. | 57.97 | 53.26 (71612): proposed only (with 5.91) |
| 57.453 (76833) | Frequent chord pairs in the corpora that the catalog lacks are the evidence for growing it. | 7.85 | 53.79 (ii) (72296): proposed only (with 5.91) |
| 57.454 (76873) | The recognition reads the committed progression, the catalog (queried, filtered by the idiom weights) and the idiom weights. | 44.21, 57.97 | 53.21 (71536): **ruled** RELOCATED to L3, nothing-from-L3 Ruling 5 |
| 57.455 (76909) | Phase one: the recognition is run over the committed progression. | 57.97 | 53.35 (71734): **ruled**, the same |
| 57.467 (i) (77043) | In the first version the recognition step does not depend on the weights, its matches being exact. Part (ii) is RELOCATED to L2. | 57.97 | 53.36 (71748): proposed only (with 50.76 (ii)) |
| 57.470 (ii) (77172) | Phase three then emits the recognition's outputs. Part (i) is RELOCATED to L2. | 57.97 | 53.39 (71784): proposed only (with 50.76 (ii)) |
| 57.478 (77395) | One progression-schema span per recognized progression. | 44.20 (i), 8.52 (iii) | 53.23 (71566): **ruled**, the same as 53.21 |
| 57.485 (77428) | What the recognition produces is additive over the function layer. | 44.37 (i), 8.51 | 53.22 (i) (71550): **ruled**, the same as 53.21 |
| 57.490 (i) (77580) | An entry defined by its lines is recognized by its chord skeleton alone. Part (ii), the chords-only mark, is RELOCATED to the uncertainty surface. | 57.97, 44.20 | 53.47 (i) (71880): proposed only (with 43.35 (i)) |

**(B) Substitution — 3.** Ground *"as at Row 44.4"*: no charter names the relation of a chord to the chord it stands in
for; or travelling with a row of that ground.

| Row-part (line) | Subject, in plain words | The L2 row (L2 reading file line) |
|---|---|---|
| 57.487 (ii) (77505) | A substitution is recorded only in the annotation. Part (i), the literal Roman numeral unchanged, is RELOCATED to L2. Travels with 57.489 (i). | 53.28 (71636): **ruled**, the same as 53.21 |
| 57.489 (i) (77546) | Where the catalog marks a member as filled by a substitution, what the chord stands in for is recorded. | 53.27 (71624): proposed only (with 50.41 (i)) |
| 57.489 (ii) (77546) | A ii–V–I whose V is tritone-substituted is still a ii–V–I. Travels with 57.401 (ii). | as (i) |

**(C) How the catalog and the licensing grammar relate: the dependency map and the asymmetry ruling — 8.** Ground
*"as at Row 57.398"*: no charter's subject is a catalog of named progressions, so none is that catalog's relation to the
grammar; Row 57.451's ground is Row 44.39 (the catalog the one owner of the named progressions, §1D group A).

| Row-part (line) | Subject, in plain words | The L2 row (L2 reading file line) |
|---|---|---|
| 57.451 (76792) | A change to the catalog (adding or editing a named progression or substitution) changes the catalog only. | 53.62 (72088): proposed only (with 5.91) |
| 57.493 (i) (77623) | A change of the grammar never needs an edit of the catalog. | 53.61 (72076): proposed only (with 50.9) |
| 57.493 (ii) (77623) | The consistency test then runs again, and a catalog entry that now fails it is flagged. | as (i) |
| 57.494 (i) (77665) | A change of the catalog never needs an edit of the grammar, but a new entry must pass the consistency test. | 53.63 (72100): proposed only (with 50.9) |
| 57.494 (ii) (77665) | A failure means a mis-encoded entry or a genuine gap in the grammar, to be escalated. | as (i) |
| 57.495 (i) (77707) | The grammar and the catalog are not derived from each other. | 53.64 (72112): proposed only (with 50.9) |
| 57.495 (ii) (77707) | The consistency test is the one coupling between them, and it runs one way, from the catalog to the grammar. | as (i) |
| 57.496 (77751) | A licensed pair in no catalog entry is not a gap of the catalog. | 53.79 (i) (72296): proposed only (with 50.9) |

9 + 3 + 8 = 20.

**The D-599 notes (preliminary, not placements).**
1. **Group A is the catalog-and-recognition family** of §1S note 1, §1U note 1 and §1D; group B is one group with §1U
   group B and §1D group C; group C is one group with §1U group C (Rows 57.398, 57.405). Where the L2 move is ruled, it
   is the nothing-from-L3 Ruling 5 of §1N note 3: a bearing, not a reach.
2. **Register entries whose titles state some of these claims**, read at their `DECISIONS.md` rows:
   - **D-506** (LIVE, no date or ratifier shown, home `cowork_progression_schema_design.md` §6): *"Progression
     recognition is ADDITIVE: the literal Roman numeral is never rewritten, and a substitution is recorded only in the
     annotation"* — the claims of Row 57.485 and Row 57.487 (ii).
   - **D-507** (LIVE, no date or ratifier shown, the same home): *"A catalog entry defined by its melodic or bass lines
     is recognised by its chord skeleton alone and carries a 'chords-only' mark, with its prior strength reduced"* — the
     claim of Row 57.490 (i).
   - **D-410** (DEFERRED, 2026-08-03 · user, home `cowork_progression_schema_dictionary.md` §4): *"The first version
     matches EXACTLY AND WHOLE; …"* — the exactness Row 57.467 (i) gives as its reason; the title does not mention the
     weights.
   - **D-406** (LIVE, 2026-08-03 · user, as §1U note 2): the claim of Row 57.495 (i). Its title does not mention the
     consistency test (Rows 57.493, 57.494, 57.495 (ii)), a licensed pair in no entry (Row 57.496), or what a change to
     the catalog changes (Row 57.451).

   The reading file records that no register home lies at any of these rows' lines (D-506 and D-507 are homed at the
   member's §6 decisions D4 and D7). Whether these entries make the claims derivations, once the family's answer for the
   catalog and its recognition is given, is **to be tested on the surface; not certain.**
3. **Row 57.467 (i):** the reading file reads its sentence as a rule of the first version's mechanism and states the
   alternative, QUARANTINED as a property of the first version as built, as not taken (its case (6)).

**Count:** 0 reached + 20 open = 20, the fourth table's total.

---

## 1W. Member 57 — the L2 transfer input, part 5 of 5: the foot table at reading file line 78371 (10 row-parts)

*Added by the Cowork sitting of 2026-11-06 that booted on entry 535.*

The foot list (line 78371): 57.516, 57.517, 57.518, 57.519, 57.520, 57.521, 57.522, 57.523, 57.532, 57.533. They come
from ten rows, each of one claim, all quoting `cowork_idiom_entry_mapping.md` (member 53's document, §1G): three
sentences of its opening block, the five body rows of its §5.1 table, and two of the three bullets of its *Notes for the
re-tag*. The reading file's header for this group (read at lines 77890–77957) records that the L2 comparison's member
55 covered these lines and this comparison's member 53 does not, which is why they reach the file only through the
transfer input; it states the alternative, RELOCATED to L2's tonal reading (as Rows 46.39 and 46.41), as not taken.

**The search.** Not rerun, on the same listings and for the same reason as §1V. The rows were found in the reading file
by one pattern listing only this table's ten row numbers as exact headings, and each entry was read whole. **The L2 side
of each row** was read at its own block in the L2 reading file, found by one pattern listing only the ten L2 row
numbers as exact headings.

### 1W.1 Reached by a ruling record — none

### 1W.2 Still open — 10 row-parts, one group: the idiom tags and cross-attributes of a catalog entry

Each was read at its §6 entry (line given). Every one is graded THE DERIVATION IS SILENT. §1S note 3's search of the
`l3` ruling records and `cowork_l3_*` surfaces found none of them. Grounds, as the reading file gives them (the idiom tag an
attribute of a catalog entry; no charter names the catalog of named progressions): *"as at Row 44.11"* with Row 46.40
(57.519 to 57.523) or with §1U's Row 57.535 (i) (57.516); *"as at Rows 46.40 and 46.49"* (57.517); or travelling with
Row 57.517 (57.532), or with Row 57.518 and Row 57.535 (ii) (57.518 with 57.535 (ii) alone; 57.533 with both).

**The L2 side, the same for all ten.** Each L2 block carries a **ruled** RELOCATED to *L3 — The read-off facts* by L2
tail-style-and-idiom Ruling 2, *"placed from UNPLACED"*, *"travelling with Row 5.91"*, adding *"The idiom set itself
stays at `ARCHITECTURE.md` §6.7 (Ruling 1)"*.

| Row-part (line) | Subject, in plain words | The L2 row (L2 reading file line) |
|---|---|---|
| 57.516 (77961) | Each entry of the catalog is tagged with its idioms from the ratified set. | 55.1 (72675) |
| 57.517 (77999) | The tags are multi-valued: an entry may belong to several idioms. | 55.2 (72689) |
| 57.518 (78036) | Each entry carries two cross-attributes, mode and chromaticism, tagged separately. | 55.4 (72717) |
| 57.519 (78076) | The diatonic functions are tagged with idiom 1. | 55.5 (72731) |
| 57.520 (78116) | The applied dominant and applied leading-tone chord are tagged with idiom 2. | 55.6 (72745) |
| 57.521 (78154) | The applied ii–V is tagged with idiom 3, and idiom 2. | 55.7 (72759) |
| 57.522 (78193) | The tritone-substitute dominant is tagged with idiom 5; its German-sixth reading with idiom 2. | 55.8 (72773) |
| 57.523 (78234) | Modal interchange is tagged with idiom 2; its triadic borrowings also with idiom 4. | 55.9 (72787) |
| 57.532 (78274) | Several tags on one entry are correct, not a defect: the functional idioms 1, 2 and 3 overlap by design. | 55.19 (72925) |
| 57.533 (78313) | Each entry also gets the two cross-attributes, independently of its idioms. | 55.22 (72963) |

**The D-599 notes (preliminary, not placements).**
1. **This group is one group with §1G and with §1U group E** (Row 57.535), the idiom tag of a catalog entry, inside the
   catalog-and-recognition family. The L2 ruling is a bearing, not a reach, as §1U note 5 records for Row 57.535.
2. **A fact of the document, recorded by the reading file at Row 57.533:** the mode cross-attribute's values are
   *"major/minor"* in the opening block (Row 57.518) and *"major / minor / either"* in the notes (Row 57.533).
3. **The reading file records that the decisions register's data file homes nothing in this document.**

**Count:** 0 reached + 10 open = 10, the fifth table's total. **Member 57 is done** (§1S to §1W: 19 + 24 + 34 + 20 + 10
= 107).

---

## 2. What this inventory does NOT do

It places no row, re-marks nothing in the reading file, edits no tracked document, writes no dispatch, and allocates no
decisions-register identity. The D-599 notes in §1.2 are preliminary readings, to be tested at their sources on the
surface that carries each row.

*Provenance: Cowork, 2026-11-04 (Stockholm). The user's words: the opening instruction; "narrow"; "continue". §1B, §1C
and the progress table's member-36 and member-46 rows: the sitting booted on entry 523; the user's words: the opening
instruction; "narrow"; "continue". §1D, §1E, the progress table's member-44 and member-19 rows and the correction in
§1A.3: the sitting booted on entry 524; the user's words: the opening instruction; "shorter"; "continue". §1F, §1G, the
progress table's member-38 and member-53 rows and the corrections in §1C and §1D: the sitting booted on entry 525; the
user's words: the opening instruction; "shorter"; "continue". §1H, §1I, the progress table's member-48 and member-4
rows and the correction in §1H: the sitting booted on entry 526; the user's words: the opening instruction; "narrow";
"continue". §1J, §1K and the progress table's member-40 and member-23 rows: the sitting booted on entry
527; the user's words: the opening instruction; "narrow"; "continue". §1L, §1M and the progress table's member-2 and member-3
rows: the sitting booted on entry 528; the user's words: the opening instruction; "narrow"; "continue". §1N, §1O and the
progress table's member-24 and member-54 rows: the sitting booted on entry 529; the user's words: the opening
instruction; "narrow"; "continue". §1P and the progress table's member-37 row: the sitting booted on entry 530; the
user's words: the opening instruction; "narrow". §1Q, §1R and the progress table's member-50 and single-rows rows: the sitting
booted on entry 531; the user's words: the opening instruction; "narrow"; "continue". §1S and the progress table's two
member-57 rows: the sitting booted on entry 532; the user's words: the opening instruction; "narroe" (read as
"narrow"); "resume". §1T and the progress table's two member-57 rows for parts 2 to 5: the sitting booted on entry
533; the user's words: the opening instruction; "narrow". §1U and the progress table's two member-57 rows for parts 3
to 5: the sitting booted on entry 534; the user's words: the opening instruction; "narrow". §1V, §1W, the progress
table's two member-57 rows for parts 4 and 5 and its line that every member is done: the sitting booted on entry 535; the user's words: the opening
instruction; "shorten".*

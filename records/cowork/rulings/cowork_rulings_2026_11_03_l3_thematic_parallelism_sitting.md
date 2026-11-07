# Rulings — the L3 OQ-L3-5 sitting (thematic parallelism: which layer publishes the restatement relation), 2026-11-03

> **STATUS: RULING RECORD.** Cowork, 2026-11-03 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_six.md`. An interim carrier under the standing
> clause that a sitting record is written in the turn its ruling is given and lands in git at the next dispatch's
> Task 0. **No act of this sitting is a commit.** The git reference files were not read by this sitting.

---

## 0. What was put, and in what form

OQ-L3-5, verbatim from the derivation (`cowork_blind_derivation_l3_2026_10_17.md`, lines 1224–1228):

> **OQ-L3-5 (faces (b), (d), (h); L3-S9, L3-S23, L3-S42) — thematic parallelism.** Section reading, the evaded
> cadence, and some phrase ends need a relation saying that a stretch restates an earlier one, transposed or not. No
> layer beneath publishes it. By IC-L1 S-51's test it is an L1-kind item. It may instead belong to the voice-leading
> axis. *The input-contract statements concerned:* IC-L1 S-50 and S-51, or the charter's spine–axis row. Which layer
> publishes it, and in what form?

Its order was fixed by Ruling 2 item k of `cowork_rulings_2026_11_02_l3_phrase_units_sitting.md` (lines 114–115, read):
*"OQ-L3-5 (thematic parallelism) — not decidable yet; under D-254 the step is focused research on published
definitions before the sections family. No decision now."* (Its "yes" relayed from entry 491.)

**The sources, and how each was read:**
- Cambouropoulos, "Musical Parallelism and Melodic Segmentation: A Computational Approach", *Music Perception* 23(3),
  2006, pp. 249–267 (`docs/research_papers/Camb_MusPerc2006.pdf`, 20 PDF pages, p. 268 blank) — **read whole at page
  images by this sitting, images present.** Exact repeated-pattern extraction (Crochemore) over melodic parametric
  profiles (pp. 253, 266); selection function on length, frequency and overlap (pp. 253–254); a boundary-strength
  profile, revised so only pattern beginnings contribute (pp. 255–256); representations compared — diatonic interval,
  step-leap with duration ratio, overlapping categories (pp. 258–260); melody only, accompaniment omitted (p. 262); no
  metrical structure assumed (pp. 255, 264); not a complete segmentation model, not tested on a large corpus (pp. 250,
  252); fails where matching intervals differ in direction (Fig. 17, p. 263). It quotes GTTM on GPR6 (p. 256, citing
  Lerdahl & Jackendoff 1983, p. 51): groups that "begin in parallel fashion and diverge".
- Hamanaka, Hirata & Tojo 2007, IPSJ Journal 48(1), pp. 284–299 (`A10383.pdf`) — **relayed from entries 495 and 496**,
  which read it at page images; not re-read here. Inputs as relayed: onsets, pitch changes between neighbouring notes,
  beat positions; the measure replaceable (p. 291); various definitions possible (p. 287); monophony only (pp. 287–288).
- `CMA2016.pdf` — Hirata, Tojo & Hamanaka, ch. 10, "An Algebraic Approach to Time-Span Reduction", from p. 251 (book
  title not on the page). `20068.pdf` — Tojo & Hirata, "Distance and Similarity of Time-span Trees", *J. Information
  Processing* 21(2), 256–263, 2013, DOI 10.2197/ipsjjip.21.256 (PDF page 1 is a JAIST cover sheet whose field text
  rendered blank; identity read at PDF page 2). **Each read at its opening page only**: both concern similarity of
  time-span trees, which presupposes a GTTM analysis. Whether either defines repetition over the notes elsewhere is
  unread.
- **Not held:** Lerdahl & Jackendoff 1983. GPR6's wording above is Cambouropoulos's quotation of it.

**Also read at the objects:** IC-L1 S-50 and S-51 at the copy
`tools/audit/derivation_exemplars/l3/the_l0_l1_specification_the_input_contract.md`, lines 1443–1532 (the ratified home
not opened); the derivation at L3-S9's premise (lines 394–397), L3-S23 (726–758), L3-S39 (1108–1114), L3-S42's premise
(1186–1188); `FRAMEWORK.md` lines 500–513 (the voice-leading axis) and 527–534 (the boundary contracts); D-599 and D-254
at their `DECISIONS.md` rows.

**Applying D-599 first:** the standing statements decide it, so no menu was presented. The derivation was set out as a
self-contained surface in one turn; checked at its sources in the next turn (seven corrections, §2); put as one
question in the turn after, alone, plain text, no widget, stating separately what changes the algorithm and what is
documentation only, and stating the currently decided method. **The user's word: "ratified".**

## 1. Ruling 1 — OQ-L3-5 RATIFIED: L1 publishes a restatement relation over the notes; its similarity measure is measured; L3 reads it

**The derivation, as ratified:**
1. *Not computed at L3.* Already settled: L3-S39 (*"L3 never re-derives a fact a layer beneath it publishes, and never
   supplies a fact of a lower layer's kind by computing it from the notation"*) and L3-S23's falsifier (*"falsified if
   any term reads a quantity no layer beneath or L3 itself publishes, in particular a melodic-repetition relation
   computed at L3"*).
2. *It passes S-51's test for an L1 output:* both methods read at source compute it from note facts (onsets, durations,
   pitches; beat positions in the 2007 paper, relayed) with no tonality, chord or boundary as input — for one melodic
   line.
3. *What L1 publishes, and what it does not:* S-50's naming rule bars a field named *boundary*, *phrase* and the rest,
   so L1 does not publish a boundary-strength profile. It publishes the relation itself; turning repetitions into
   boundary evidence (including GTTM's start-orientation) is L3's own terms.
4. *Not the voice-leading axis* (this sitting's argument; the derivation had left it open): the axis's objects are
   *"the accepted melodic phrase, chord voicing and arrangement, part-writing, the stock eighteenth-century outer-voice
   patterns"* (`FRAMEWORK.md` lines 502–504); a restatement relation over notes is none of these and needs no phrase.
   If the axis wants it, the spine–axis row lets it read L1's publication (line 534).
5. *The similarity measure is not chosen here.* Both sources state it is replaceable and that many definitions are
   possible; which one infers best is measured (D-254), and it is marked UNESTABLISHED until then.

**Algorithmic — what this changes in the method as specified:**
- **L1's published list (IC-L1 S-50) gains one item**: a restatement relation over the notes — each instance naming the
  stretch, the earlier stretch it restates, the transposition (none, or an interval), and the representation under
  which it matched; with its witnesses (the notes), its establishment status, its provenance and, where not computed, a
  named reason (the forms S-50 already requires); named for the pattern detected, never *boundary*, *phrase* or
  *theme*; the matching measure UNESTABLISHED until measured. An amendment to a ratified L1 face and to the charter's L1
  list, on the shape of Ruling 2 of `cowork_rulings_2026_10_08_l2_structural_bass_sitting.md` (S-50 lines 1508–1516,
  read). S-50's former wording is preserved at its site when applied (#12).
- **The charter's boundary-contracts row L1 → L3** (`FRAMEWORK.md` line 533, now *"Notated phrase evidence"*) gains the
  relation.
- **L3 gains an input:** L3-S23's family (iv), *thematic return*, changes from *"not filled"* to reading the published
  relation; L3-S9's phrase-end evidence (premise at lines 394–397) may read it; L3-S42's premise (lines 1186–1188) is
  answered — the relation is published by L1, not the axis. The weights stay measured and UNESTABLISHED (OQ-L3-11). L3's
  bar on computing the relation itself stands as written.

**Documentation only:** OQ-L3-5 recorded as answered; the relayed citations at derivation lines 395–397 recorded as now
read at source (Cambouropoulos 2006 at this sitting; the 2007 paper at entries 495–496); `BIBLIOGRAPHY.md`'s Local
cells for the four files are a later step (entry 496 §3 item 2).

**The currently decided method before this ruling, as stated with the question:** L1 publishes no such relation; L3
does without it; a section return or phrase start marked only by returning material is found only through cadences, key
changes and notated marks.

Meta level: the analysis itself.

**Carried, UNSETTLED (not decided by this ruling):** how the relation extends across several voices — both sources
define it on one melodic line; L1 already publishes per-notated-voice relations (S-50), and cross-voice matches (a theme
moving between voices, a fugue answer) are defined by neither; GTTM's own wording of GPR6, still not held; which
statement carries the evaded cadence named in OQ-L3-5's text, not located by this sitting.

## 2. The check of the surface, run before the question — corrections

Seven: (1) the 2007 paper's content marked relayed from entries 495–496, not read by this sitting; (2) `CMA2016.pdf`
and `20068.pdf` read at their opening pages only — "they do not define repetition over the notes" withdrawn as wider
than the read; (3) the evaded cadence wrongly attached to L3-S42, which is *"Two dependencies on out-of-scope
subjects"* (line 1171); (4) the charter's L1 → L3 row added to the algorithmic part; (5) the ground for measuring is
D-254, read at its row, not an unread 7 October record; (6) L3-S23's falsifier quoted whole; (7) "the alternatives have
collapsed to one" labelled this side's derivation, the axis argument being this sitting's.

## 3. What this record does NOT do

It writes no dispatch (D-250), edits no tracked document, amends neither S-50 nor the charter nor the derivation (those
are the application act's), re-marks no row of the reading file, and allocates **no decisions-register identity** (the
register's rule (c) is suspended).

## 4. Departures and bounds of this sitting

The device-info call was first; `C:\s\MS` was requested after it. **No shell command, in the container or on the
device; no git command**; no memory tool, widget, task list, subagent or web access. Folders listed: the handoff
folder, `docs/research_papers`, `ratification_surfaces`, the rulings folder; never the repository root. Every file
staged by its path and read with the file tools. **The ordinary session-start read was narrowed on the user's word
("yes")**: `STATUS.md` whole, the gating answer at its counts (222 of 247 open rows gate), D-599 at its row; `CLAUDE.md`'s
six spans and `DECISIONS.md` whole were not read. **Not read:** GTTM; `CMA2016.pdf` and `20068.pdf` beyond their
opening pages; the code.

*Provenance: Cowork, 2026-11-03 (Stockholm). The user's words: the opening instruction; "yes"; "continue";
"continue"; "continue"; "ratified".*

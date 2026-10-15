# Rulings — the L3 staged-score-set sitting, 2026-10-15

> **STATUS: RULING RECORD.** Cowork, 2026-10-15 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_six.md` (7,316 bytes at the handoff folder's listing).
> An interim carrier under the standing clause that a sitting record is written in the turn its ruling is given and
> lands in git at the next dispatch's Task 0. **No act of this sitting is a commit to git.** `.git/refs/heads/master`
> and `.git/refs/remotes/origin/master` both read `5499f3e2521c2bf4478469f30f3b9fb18f0af655`, read as files with the
> file tools over staged copies.

---

## 0. What was put, and in what form

Entry 406 §3: item (1) of its §2 — the staged score set, as Ruling 6 of
`records/cowork/rulings/cowork_rulings_2026_10_15_l3_boot_list_sitting.md` states it (read whole this sitting): a
small set of scores staged with their published analyses, chosen to exhibit six named L3 phenomena — an authentic
and a half cadence at phrase ends; a phrase end the notation does not mark; phrases grouping into a section; a
figured-bass passage; a change of harmonic rhythm — each claim checked at the file, the named set put to the user
with each claim beside it before anything is staged. L2's precedent,
`records/cowork/rulings/cowork_rulings_2026_09_21_l2_staged_score_set_sitting.md`, was read whole first.

One self-contained surface was delivered as text in its own turn, every identifier re-explained, three alternatives
each weighed towards the ultimate objective, towards the guiding principles and marked for its meta level, with a
recommendation (B). The choice question was put alone in a later turn, no widget.

## 1. The claims, checked at the files this sitting

**Mozart, Piano Sonata in C, K545, first movement** — `tools/dcml/mozart_piano_sonatas/MS3/K545-1.mscx`
(413,065 bytes at staging; already a member of L2's set). The published DCML analysis is inline. The table
`tools/dcml/mozart_piano_sonatas/harmonies/K545-1.harmonies.tsv` (9,164 bytes) was read whole; every cadence and
phrase label named below was found in the score file (labels `V|HC`, `I|PAC}`, `I|PAC}{` and the phrase marks).

- Perfect authentic cadences at phrase ends: bars 26, 42 and 71.
- Half cadences: bar 11 and bar 56, each on the downbeat; the analysis closes the phrase one bar later (bars 12 and
  57).
- A phrase end the notation does not mark: bar 42, labelled `I|PAC}{` (phrase end and phrase begin on one
  downbeat). Both staves read at bars 41–42: the right hand runs sixteenths into bar 42 with no rest after the bar's
  opening sixteenth rest; the left hand holds the dominant seventh into it; no fermata, repeat or barline element
  there (the file's only repeat marks are at the ends of bars 28 and 73 and the start of bar 29; its fermatas are at
  the end). A clef change in the left hand at bar 42 is the only notational event. Contrast, read at the file: the
  phrase ends at bars 4 and 12 carry a right-hand rest; bar 2 carries a rest and is no phrase end.
- A change of harmonic rhythm: two or three labels per bar in bars 1–4, one per bar in bars 5–9, `ii6` held through
  bars 22–23.
- Phrases grouping into a section — **partial at this file**: DCML marks phrase begins and ends, not sections. The
  exposition is closed by the notated repeat at the end of bar 28 and holds the published phrases 1–4, 5–12 and
  13–26, the local key moving to the dominant at bar 13.

**Corelli, Trio Sonata Op. 1 No. 8, first movement (Grave, C minor, 16 bars)** —
`tools/dcml/corelli/MS3/op01n08a.mscx` (94,825 bytes at staging; new). DCML analysis inline; the table
`tools/dcml/corelli/harmonies/op01n08a.harmonies.tsv` (4,598 bytes) read whole; every phrase and cadence label in
the score file found. The continuo staff carries figures in every one of its sixteen bars. The collection's
`README.md`, read at its "Score origin" section: the figures were added from the Pepusch prints and corrected
against the Rome first editions.

- Figured bass: bar 1, beats 3–4 — bass G figured `5 4`, then G with a lone accidental stored as prefix value 3
  (read as the natural sign from this side's knowledge of MuseScore's encoding, not checked at a specification); the
  labels on the same beats are `V(4)` then `V`.
- Cadences at phrase ends: half cadences closing phrases at bars 4 and 8; perfect authentic cadences at bars 12
  (`i/iv|PAC}{`, phrase end and begin on one beat) and 16.
- A change of harmonic rhythm: a label per beat through bars 1–3 (eighth-level in bar 3); one label for all of bar 4.
- Not a gate concern for staging: the file is one of the eleven pinned snapshot-test sources; reading a copy does not
  touch the pin. D-514 is not engaged.

**Noticed, not acted on:** the Corelli table carries an `alt_label` column with two entries (bars 9 and 13) — a
bearing on rival readings, L2's subject, outside this decision.

## 2. Ruling — OPTION B

**The user's word: "B".**

**What was decided.** L3's staged set is the K545 first movement and the Corelli Op. 1 No. 8 Grave, each as its score
file with the analysis inline, **plus** the second independent reading of K545's first movement,
`tools/dcml/when_in_rome/Corpus/Piano_Sonatas/Mozart,_Wolfgang_Amadeus/K545/1/analysis_DT.txt` (analyst Nathan
Martin, proofreader Dmitri Tymoczko), for the section phenomenon — **conditional on its section marks being checked
at the file before it is named.** The file lies eight folders below `C:\s\MS` and the bridge stages at most seven, so
the user connects that folder as its own and this side checks it. **If it carries no section marks, the ruling falls
back to A**: the two scores, with the section phenomenon shown by K545's exposition and marked in the brief as a
partial exhibit. The standing bars carry over: files staged by name, never a directory; exemplars, not a corpus; no
count rests on them.

**The ground, as put.** Towards the objective: the only route found to a published reading for all six phenomena.
Towards the principles: #1 (published analyses), #19 (each claim checked before it carries load). Meta level: one
step from the analysis. Strongest argument against: a folder connection and one more check.

**The alternatives not taken.** (A) The two scores alone, the section phenomenon partial — kept as B's fallback. (C)
A Bach-chorale figured-bass member from `corpora/gt/Bach_chorale_FB` (row 36's dataset, figures from the Neue
Bach-Ausgabe) instead of the Corelli — the chorales overlap the regression repertoire, so D-514 would need a judgment,
and no harmony analysis sits beside the figures; no file in it was opened.

**The two UNSETTLED items of Ruling 6, answered at the objects.** *A figured-bass source is held*: two — the Corelli
DCML scores' figures, and `corpora/gt/Bach_chorale_FB` (its `README.md` read whole). *The held DCML analyses mark
phrases*: yes, `{` and `}` in the label, checked in the two files above; not checked elsewhere.

**Documentation and algorithm.** This decides what a future session reads. It amends no specification and changes no
algorithm. The currently decided method for L3 is `FRAMEWORK.md` §5's L3 block with DP-I (*"split — cues at L1, type
at L3"*).

## 3. What follows, none of it executed here

1. The user connects the K545 When in Rome folder; this side checks `analysis_DT.txt` for section marks and records
   the result here, choosing B or its fallback A by that result.
2. Staging is the pack-build side's act. Nothing is staged by this record.

## 4. The condition, checked — B STANDS

The user connected `C:\s\MS\tools\dcml\when_in_rome\Corpus\Piano_Sonatas\Mozart,_Wolfgang_Amadeus\K545\1` as a
folder of its own. Its listing: `analysis_automatic.rntxt`, `analysis_DT.txt` (1,034 bytes), `analysis.txt`,
`remote.json`, `score.mxl`, and a `Working` folder. **`analysis_DT.txt` was read whole. It marks sections**, in
`Form:` lines placed before the bar each section starts: *exposition* before m1, *second theme* before m14,
*development* before m29, *recapitulation* before m42 (with the analyst's note *"recapitulation begins in the wrong
key"*), and *second theme* again before m59. **So the condition is met and B stands; the fallback to A does not
fire.**

Two facts the session will meet, recorded rather than interpreted:

- **The two readings place one section boundary differently.** This reading moves to G at m13 (`m13 G: V b3 V2`)
  and starts its *second theme* at m14; the DCML analysis opens a phrase in the dominant at m13 (`V.V{`).
- **The recapitulation boundary at m42 is the phrase end the notation does not mark** (§1): the DCML reading writes
  `I|PAC}{` there, and this reading starts a section there.

This file carries **no phrase marks** (no `||` was met in it as read); its contribution is the section grouping. The
other files in the folder were listed, not opened; `analysis.txt` is the DCML reading converted, excluded from L2's
set by its own ruling for that reason, and is not proposed here either.

## What this record does NOT do

It stages no file, writes no dispatch (D-250), edits no tool, boots no session, and allocates **no
decisions-register identity** — the register cannot accept one while
`cowork_register_rule_c_suspension_2026_08_28.md` is the route.

*Provenance: Cowork, 2026-10-15 (Stockholm). The user's words: the opening instruction; "continue" (the question);
"B" (the ruling).*

# The key signature, and the hidden "major/minor" tag — the ninth family surface for the chord-and-key layer — 2026-10-05

> STATUS: DECISION SURFACE, NOT RULED. No question on it has been put. Written by the Cowork sitting that
> booted on `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_eighty_eight.md`. Tags: *checked*
> = read at the source this sitting; *relayed* = taken from a record and not re-read at its source; *my
> reading* = my inference.

## 1. Where we are

You are ruling, family by family, on how the new specification of the analysis's central layer should
read. That layer decides together, in one pass: the key at each moment, where each harmony gives way to
the next, which sounding notes are chord notes and which are passing notes, suspensions and the like,
and which chord sounds over each stretch. Beside its winning reading it publishes the rival readings,
each with a weight.

Two documents feed each family. **The framework document** (`FRAMEWORK.md`), which you ratified on
2026-08-29, sets out the layers and the constraints every layer must honour. **The derivation**
(`cowork_blind_derivation_l2_2026_09_27.md`) is forty-nine statements of how this layer should work,
written by a session that was not shown the existing design documents. A comparison file then set
every sentence of the existing documents beside those statements, marked each as agreeing or
differing, and proposed where each should go. Nothing in it is applied yet.

Eight families are ruled. This one is about **the key signature written at the start of the staff, and
about a hidden "major" or "minor" tag that some score files carry**.

## 2. The music, and the facts (before any question)

**What a key signature tells us, and what it does not.** A key signature narrows the likely keys, but
it is not the key. One flat may mean F major or D minor; and a piece modulates without changing its
signature — a C-major piece can spend sixteen bars in G major with no sharp written at the clef. In
Baroque music there is a further wrinkle: pieces were often written with one accidental fewer than
modern practice would use. A chorale in D Dorian, or in what we would call G minor, may carry one flat
fewer than a modern edition would print. So the signature points the wrong way on a known class of
scores. (*checked*: `FRAMEWORK.md` constraint C-2, line 155, citing the empirical findings ledger,
entry C14; register entry D-056, "Notes always win - the notated key signature is a weak hint, not a bypass".)

**What the hidden tag is.** A MusicXML file can carry a `<mode>` element — "major" or "minor" — beside
the key signature. It prints nothing on the page; no copyist reading the score would see it. This
project preserves it on import into the key signature's mode field (*relayed* from Ruling 57 of
`records/cowork/rulings/cowork_rulings_2026_08_31_decision_surface_sitting.md`, which cites the local
patch in `CLAUDE.md`; the patch text itself was not read this sitting). One of the derivation's example
scores carries `<mode>minor</mode>` beside a one-flat signature (*checked*, derivation line 460).

**What you have already ruled about the tag.** On 2026-09-03, in the ruling on what the note-reading
layer admits (Ruling 57, *checked*, read whole), you ruled that the tag is **annotation, not
notation**: it fails the test that two copyists reading the same page would agree on it, and it is a
claim about the music's meaning. The file's tag is carried, labelled as read, and **no layer of the
analysis consumes it as evidence about the music**. The ruling names the framework's two clauses that
decide it: §8.6, "No user-written analytical content — chord symbols, Roman numerals, function,
cadence or tonality annotations — enters the analysis in any storage form", and C-2. It excluded the
alternative — the tag admitted and used by this layer as a prior, as the existing design has it — "at
the threshold", because §8.6 is a ratified clause later than that design and governs it. And it
**left one thing to this layer's surface**: the existing design's own use of the tag (register entries
D-528 and D-450) against §8.6 and C-2, "flagged, not decided".

**What the framework you ratified says about the signature.** C-2, in full (*checked*, lines 155–158):
"The key signature is not a statement of the tonality. Baroque scores are frequently notated one
accidental short of modern practice, so the signature under-determines the tonic, and the detecting
signal is itself musical. … The signature is a weak prior on the tonality at the start and at a
notated signature change, and nothing else." Its layer description in §5 gives only the short form,
"The key signature is a weak prior (C-2), never a fact about the tonality" (*checked*, line 300); the
first-stage draft kept in its appendix (§S5) says "at the start of the piece and at a notated signature
change, and nothing else" (*checked*, line 1710). A "prior" here means a gentle starting lean, counted from annotated music, that the notes
can always overrule.

**What the existing design says** (*checked* at the register entries and at the comparison rows):

- **Where the lean acts — D-450**, decided 2026-07-19 and ratified by you: the signature (and the tag)
  "sets the starting key state and is not applied again — except at a notated mid-piece signature
  change". The other form, "a persistent pull toward the signature at every step, is rejected", on
  these grounds: a hand-traced test on a Dorian-notated opening and on a genuinely modal piece showed
  the persistent form taxing every key away from the signature at every stretch, without limit; no
  published system carries a signature lean at all; and it brings back, in a softer form, a
  signature-pull bias an earlier measurement condemned — in exactly the stretches with no accidentals,
  where the signature should be silent.
- **How the lean is shaped — D-528**, same date, ratified by you: "a weak, fitted,
  transposition-invariant soft prior on (tonic, mode)", "a small categorical table … counted from
  ground truth"; the Dorian-written-one-flat-short case is "handled statistically as measured mass one
  fifth away in minor — no special case"; "the declared mode, where the score carries one, is a second
  conditioning input with its own fitted strength". No "if unsure, consult the signature" switch: a
  weak lean simply matters only where the notes leave the question open.
- **The ranking of evidence — D-057**: the sounding notes strongest, then the surrounding music, then
  the key signature, then the tag, weakest.
- **An older fix, now gone — D-575**: detect the missing flat and reinterpret the signature one step.
  The register records it as superseded in fact and as legacy.

**What the derivation says — its statement L2-S17** (*checked*, lines 452–476): "The written key
signature enters as one term of the candidate score, a weak prior over the spans' tonalities. It never
constrains them. The prior assigns non-trivial weight to the tonalities one accidental either side of
the signature, as well as to the signature's own major and minor. A tonality or mode tag the record file
declares is not read at all." Its own account of what can go wrong shows which form it means: "a
modulating section after which the signature is not changed. The prior then pulls toward the old
tonality, and it is outweighed by content terms because it is weak." So the derived lean acts **on every
stretch**, not only at the start. The values are left to measurement (open question OQ-L2-3, "the
key-signature prior's spread and weight", *checked*). Its defense cites the framework as "a weak prior
(C-2), never a fact about the tonality" — the layer description's short form; it does not quote C-2's
closing words, "at the start and at a notated signature change, and nothing else". Whether the copy of
the framework the deriving session was given carried those words was not checked this sitting.

**One note on independence** (*checked*, derivation §6.3 entry 1, lines 1509–1516). The deriving
session declared that it had seen one sentence it was not meant to see: the ledger entry on Baroque
signatures, whose second half names the older fix (detect and reinterpret one step, D-575). It flagged
L2-S17 for the comparison to check. What it then wrote is **not** that fix: it spread the lean to one
accidental either side for every score — which is the shape of D-528's "no special case", a text it was
not shown (*my reading*; the comparison marks Row 48.50 as an agreement on a withheld statement).

## 3. What the record already settles — no choice remains

Applying the standing principles and your rulings first (the decision-surface rule's step 1), each of
the three questions this family raises is answered by the record. I put them to you as
**confirmations, not choices**, and say for each why the alternative is closed.

### 3.1 The hidden tag is not read by this layer at all

The derivation says it; your Ruling 57 decided it for every layer and excluded the alternative by name;
the framework's §8.6 and C-2 are ratified clauses that govern the older design. What it changes in the
existing design: D-528's "second conditioning input", D-450's "and declared-mode", and the fourth rung
of D-057's ranking fall away; the first three rungs (notes, surrounding music, signature) stand.

*Why the alternative is closed* — keeping the tag as a lean, as D-528 has it: it would put a file's
opinion about the key, invisible on the page, into the analysis, which §8.6 forbids "in any storage
form", and it would overturn your Ruling 57 of 2026-09-03. Towards the objective: a tag is a claim,
not evidence the notes can test; where it is right the notes say the same, and where it is wrong it
pushes the wrong way. Towards the principles: build on established fact (#1); one home for each fact —
the tag is carried, labelled, at the note-reading layer, for any reader outside the analysis (#6, #12).
Meta level: the analysis's own specification.

### 3.2 The signature leans on the key at the start, and again at each written signature change — nowhere else

The framework you ratified says exactly this (C-2), and so does the existing design's D-450, with a
traced, stated ground. The derivation's "a weak prior over the spans' tonalities", acting on every
stretch, is the one text out of line; I recommend L2-S17's first sentence be amended to C-2's form, and
the persistent pull be excluded by name, as D-450 excludes it.

In musical terms: a one-flat chorale starts with a gentle lean toward F major and D minor (and their
neighbours, §3.3). If it then modulates to C major for a phrase, nothing taxes the C-major stretch for
not matching the signature — the notes decide. If the composer writes a new signature for a new section,
the lean re-applies there, because that is new written evidence.

*Why the alternative is closed* — the derivation's lean on every stretch. Towards the objective: D-450's
trace showed it biasing exactly the passages without accidentals, where the signature says least, and
growing without limit over a long modulating passage; the derivation itself names the modulating case
as its weak point. Towards the principles: it contradicts a ratified framework clause (C-2) and a
ratified decision with a recorded trace (D-450), and has no published basis (#1); the derivation gives
no ground for the every-stretch form beyond the phrase itself. Meta level: the analysis's own
specification; it would also require amending the framework.

### 3.3 The lean's shape: wide enough for the one-accidental-short case; its sizes counted from annotated music

The derivation's spread — non-trivial weight on the signature's own major and minor and on the keys one
accidental either side — and D-528's small table counted from annotated music, by distance on the
circle of fifths and by mode, say the same thing in substance; the comparison marks them as agreeing
(Rows 48.50 and 10.60). The sizes are a measurement, kept apart from the music they are graded on
(open question OQ-L2-3; D-528 adds that the signature's influence is measured by switching it off and
published at every fit, with the expectation that it is small). Nothing to choose; the derived wording
stands, read as the minimum the counted table must allow rather than a ceiling.

*The alternative, closed long ago*: the older fix (detect the missing flat, reinterpret the signature) —
superseded in fact, legacy, and a special case where a counted lean handles every score the same way.

## 4. Where the existing sentences would go (my proposals)

The comparison file lists forty-nine sentence-parts of the existing documents under L2-S17: twenty-four
agree and twenty-five differ (*checked*, §7, line 71131–71132; every row below read at its place in §6).
Twenty-six are already placed by the comparison's own proposals; twenty-three are left for you to place
("unplaced"). "Carried" means the derived statement already says it; "proposed" means it is added to
the derived statement; "moved" means it belongs to another layer's specification; "set aside for the
audit" means it describes the current code and becomes a question for the later audit; "historical"
means it records a past plan or status.

**Already placed by the comparison, unchanged under §3:**

- **Carried (19):** the signature a weak hint, never the truth, the key from the notes — Rows 1.29(i),
  1.50, 1.51, 7.41(i), 7.68, 24.2(i), 24.5, 24.6, 24.8; no hard promotion of the tag's key (24.3(i));
  re-anchoring at a written signature change (1.38(ii), 44.50(v), 48.51, 58.3(ii)); the one-short
  Baroque habit (2.54); the counted weak lean, no switch, Dorian handled by counting (48.8(i),
  48.48(i), 48.49, 48.50).
- **Moved to the note-reading layer (2):** no harmonic annotation read as input; the key signature
  admissible as notation (Rows 23.214, 23.215).
- **Set aside for the audit (2):** the old key engine's fixed −0.6-per-fifth preference (Row 23.187);
  "does the shipped adapter expose any key-signature change after the first, and does the decode read
  one?" (Row 17.24(i)).
- **Historical (3):** the older detect-and-reinterpret fix (Rows 2.52, 2.55); a planned test case
  (10.60).

**The twenty-three for you to place:**

- **The tag used as a lean — 14 rows.** Rows 1.29(ii), 10.36, 12.43(iii), 24.2(ii), 24.9, 44.50(iv),
  48.8(ii), 48.48(ii) state the existing design's use of the tag. Proposed: **historical** — a rule
  superseded by §8.6 and Ruling 57, as confirmed in §3.1. Row 24.4 ("what remains of the declared
  mode's influence is only the small hint … applied at every tick", `ARCHITECTURE.md` §5.2) states what
  the code does. Proposed: **set aside for the audit**, with the question "does any path at the current
  commit still apply the file's major/minor tag to a key's candidate score, on either the current or
  the older engine?" Rows 60.2(i), 60.2(ii), 60.3, 60.4, 60.7 are the older engine's planned "small
  declared hint" (register entry D-571, superseded in fact). Proposed: **historical**, with Row 24.4's
  audit question covering what may survive in code.
- **Where the lean acts — 7 rows.** Rows 1.37, 1.38(i), 1.39 (D-450's home text), 10.14(i), 10.37(i),
  10.37(ii) (its restatement in the factorization document) and 58.3(i) (the hand-traced test's
  record). Proposed: **proposed for addition** to L2-S17 — the lean at the start and at each written
  signature change only, the every-stretch pull excluded — each row's mention of the tag falling under
  §3.1.
- **Harmonic annotations in the score — 2 rows.** Row 44.17 (chord symbols and the like in a score, "a
  user-provided ground-truth hint the analysis ignores entirely"): proposed **moved to the note-reading
  layer**, which carries such annotation labelled and never as evidence (Ruling 57, its clauses (i) and
  (ii); `FRAMEWORK.md` §8.6). Row 44.50(x) (the old key layer's wish for "chord-symbol annotations where
  present (user-provided truth)"): proposed **historical** — a wish list item excluded by §8.6.

Counted: twenty-four agree (19 carried, 2 moved, 1 set aside, 1 historical, 1 now placed historical —
Row 60.7); twenty-five differ (2 historical and 1 set aside already; of the remaining twenty-two, 7
proposed for addition, 1 moved, 1 set aside, 13 historical). With these placed, the family is placed
whole.

## 5. What was read, what was not, and what is unsettled

- **Read:** the derivation at L2-S1, L2-S16 to L2-S18, its open questions on measured values, its
  statement on what L2 reads from below (lines 1150–1161) and its §6.3 record; `FRAMEWORK.md` at its
  banner, C-1 to C-9, §3.1, the note-reading layer's description in both its places, §8.6 and the
  agreement table item 4; the comparison file at its vocabulary (§5), at §7's entry for L2-S17, and at
  every row named in §4, plus Rows 44.3 to 44.5 and the flagged item 62.55; Ruling 57 whole; register
  entries D-450 and D-528 whole, D-056 and D-057 at their entries; the note-reading derivation at S-6.
- **Not read:** `ARCHITECTURE.md` and the older design documents beyond the sentences the comparison
  quotes; the ledger itself (C14 is relayed through the framework and the derivation); the `CLAUDE.md`
  import-patch text; D-571, D-572, D-575 beyond their register titles; the deriving session's copy of
  the framework.
- **Unsettled, for the writing of the specification** (*my reading*, none a choice now): "at the start"
  of what — the piece, or the stretch of music the user selected and the analysis loaded (the ratified
  C-2 says "at the start"; only the first-stage draft adds "of the piece"); whether a written signature
  change that falls between two note changes becomes a point where the lean re-applies; the lean's sizes (OQ-L2-3, a measurement). And, outside this layer: the register entries D-056 (whose
  quoted text passes the tag on as "a weak hint (`declaredMode`)"), D-450, D-528 and D-057 lose their
  tag half, a status change that waits for the register's own route
  (its same-commit rule is suspended); no register number is allocated here.

This surface writes no instruction for Claude Code, edits no tracked document, amends neither the
framework nor the register, and allocates no register number.

**The questions, to be put later, one per turn, each as a confirmation:** first §3.1; then §3.2; then
§3.3 with the placements in §4.

---

## §B. The check, run in the turn after the user's "continue"

Run over completeness, coherence, correctness and absolutes, at the sources staged this sitting.
**Corrections, each made at its site, the former wording kept here (#12):**

1. §2: *former* "Its layer description repeats it: "a weak prior on the tonality at the start of the
   piece and at a notated signature change, and nothing else" (*checked*, line 1710)." Line 1710 lies in
   the first-stage draft kept as the framework's appendix (§S5), not in §5's layer description, which
   carries only the short form (line 300). Now both stated, each at its place.
2. §4: *former* "whether the shipped importer hands on any signature change after the first (Row
   17.24(i))." That was half of the comparison's audit question; now quoted whole.
3. §5: *former* "the register entries D-450, D-528 and D-057 lose their tag half". D-056's quoted text
   also passes the tag on as a weak hint (`decisions/group_F.md`, its entry); now named.
4. §5: the "at the start of what" item now records that the ratified C-2 says "at the start" and only the
   first-stage draft adds "of the piece" — the distinction the first correction exposed.

**Checked and standing:** the forty-nine row-parts and every placement in §4, re-counted: 24 agree (19
carried, 2 moved, 1 set aside, 2 historical counting Row 60.7) and 25 differ (7 proposed, 1 moved, 2 set
aside, 15 historical), 49 in all; Ruling 57's quoted phrases; D-450's and D-528's quoted phrases; L2-S17's
quoted sentences and its false-negative path; the independence note against derivation §6.3 entry 1.
**None of the corrections moves a confirmation, the recommendation in §3.2, or a placement.**

**Declared:** no shell command was run in this sitting, in the container or on the device; no memory
tool was used.

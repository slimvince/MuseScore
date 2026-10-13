# Rests, silence, and "no chord" — the eighth family surface for the chord-and-key layer — 2026-10-05

> STATUS: DECISION SURFACE, NOT RULED. No question on it has been put. Written by the Cowork sitting that
> booted on `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_eighty_seven.md`. This is the
> second version. The first was delivered in conversation earlier in the sitting and withdrawn at the
> user's instruction ("describe all positions better, in musical terms — free from self invented
> jargon"), because it used project identifiers without explaining them and described the silence case
> only as complete silence. Nothing in the first version was ruled on. Tags: *checked* = read at the
> source this sitting; *relayed* = taken from a record and not re-read at its source; *my reading* = my
> inference.

## 1. Where we are

You are ruling, family by family, on how the new specification of the analysis's central layer should
read. That layer decides, together and in one pass: the key at each moment, where each harmony gives way
to the next, which sounding notes belong to the harmony and which are passing notes, neighbour notes,
suspensions and the like, and which chord is heard over each stretch. For each stretch it publishes the
key, the chord (its degree in the key, its quality, its inversion and figures, and the key it is applied
to, as in V/V), and alongside the winning reading the rival readings with a weight for each. The weight
is the model's own measure of how strongly the evidence favours a reading; it is not yet a calibrated
probability (*checked*, `FRAMEWORK.md` §5, and the derivation's statement on weights).

Two documents feed each family:

- **The framework document** (`FRAMEWORK.md`), which you ratified on 2026-08-29. It sets out the layers
  and lists the design questions it deliberately left open.
- **The derivation** (`cowork_blind_derivation_l2_2026_09_27.md`): forty-nine statements of how this
  layer should work, written by a session that did not see the existing design documents. A comparison
  file then set every sentence of the existing documents beside those statements, marked each as
  agreeing or differing, and proposed where each sentence should go. Nothing in it is applied yet.

Seven families are ruled. This one is about **rests and silence, and about whether the analysis may
ever answer "no chord" over music that is sounding**.

## 2. How the analysis meets a rest (the facts, before any choice)

The layer below the chord-and-key layer cuts the music wherever any note starts *or stops*
(*checked*, `FRAMEWORK.md` §5, the layer that publishes change points). So when one voice drops out
for a rest, that moment is a point where a new harmony *could* begin. At each such point that layer
also publishes what the notation shows there; the framework's list is "bar line, fermata, rest, repeat
sign, double bar" (*checked*, same place).

The chord-and-key layer may place a harmony change only at one of those points, and it weighs the
notated evidence there as one consideration among others. The derived statement on notated evidence
says it plainly: "No flag forces or forbids a boundary" (*checked*, derivation lines 375–377). How much
a rest counts is learned from the annotated music.

So a rest in one voice is already treated the way you described: a fact the inference weighs, which may
or may not mean the harmony changes. The list of what the note-cutting layer hands upward is more
specific than the framework's (*checked*, `cowork_blind_derivation_l0_l1_2026_08_31.md`, statements
S-31, S-39 and S-50): at each cutting point it publishes a flag "REST-BEGINS (a notated voice's silence
begins at this change point, by rest or by unwritten gap, naming the voice)" and a flag "ALL-SILENT (the
slice starting here is a silent slice)", and its reason is to keep "the difference between one voice
resting and all resting". A silent stretch "is published as a slice like any other … and is not merged
into a neighbour", because merging it "would decide that the harmony before the silence continues
through it, which is L2's question" — the chord-and-key layer's. The chord-and-key derivation cites these
statements by number as its input contract, and the wording matches at S-31; whether a later amended
file, rather than this derivation, is the contract proper was not established this sitting.

**When every voice rests at once**, the stretch has no sounding notes at all. The derivation's
statement on silence (*checked*, derivation lines 1082–1100) says the analysis carries two rival
readings of such a stretch and lets the evidence weigh them:

1. **The harmony continues through the silence** — the normal hearing of a rest inside a phrase: an
   accompaniment pattern with rests between the chords, short detached chords, a dramatic rest before
   a cadence resolves. Since a stretch can be joined to the harmony on either side, this covers both
   "the chord before carries on" and "the next chord has already begun" (*my reading*).
2. **A silent stretch with no harmony**, labelled as silent — the hearing of a general pause before a
   new section.

The derivation gives the grounds: the silent stretch has no notes to read a chord from, and continuing
the harmony through a rest is how analysts write across one. The annotations the analysis is graded
against are written so that a label holds until the next label, so they too run across rests (general
knowledge about those formats; not checked at the files).

## 3. The open question about sounding music

The framework document left this question open on purpose. Its words (*checked*, `FRAMEWORK.md` §9):
"May the analysis decline to read a span at all? NONE CHOSEN — underived: open. Some published schemas
carry a no-chord label and a no-cadence verdict; the three exemplar analyses contain neither. The
question is whether *no confident reading* and *no chord here* are the same publication." Its risk list
adds that this and two other open questions are left open and that none is to be "filled with the most
plausible reading" (*checked*, §11). The first draft of the framework says it is settled by "a decision
about what the published output means" (*checked*), so — unlike this morning's cadential six-four, which
was a question of music theory — this is a question you can decide on the record as it stands.

What "no chord" would mean musically. Some analysis traditions write a no-chord mark: jazz lead sheets
write "N.C." over breaks and unison figures, and chord-recognition systems for recordings use a no-chord
label (general knowledge, not checked at any source in the repository). In the classical repertoire
the analysis is graded on, the analyses read so far contain no such label (*checked* in the framework,
*relayed* from the derivation; the analyses of exemplars 4 and 6 and the other graded collections were
not checked for it). How those analysts label a bare octave or a unison passage was not checked.

Three facts shape the choice:

- **Doubt is already published.** The layer has no "uncertain" flag. Where the notes do not decide, the
  winning reading carries a low weight and its rivals carry the rest. The framework rules out a separate
  doubt marker: "there is no layer whose job is uncertainty … A separate uncertainty layer would put one
  fact in two homes" (*checked*, §5). So "I am not sure which chord this is" is already said, by the
  weights. A "no chord" answer could only add a different claim: "there is no harmony here".
- **The derived specification already names a chord over every sounding stretch.** Its statement on the
  shape of a reading allows a chord to be replaced by a named reason only over a silent stretch
  (*checked*, derivation lines 124–128). It also admits "a chord … over a span whose sounding set lacks
  its root, or lacks its third" (*checked*, derivation lines 308–311), which is what reading an implied
  harmony over a bare octave needs. The words "uncertain", "abstain" and "abstention" occur nowhere in
  the derivation (*checked* by a search of the file).
- **The existing rules pull in both directions.** One rule says the current engine always names a key
  and never declines; its record names the conflict with a planned "calibrated abstention" target in
  `ARCHITECTURE.md` §5.7a and leaves it for later (*checked*, decisions register entry D-114). That
  target's own words, "calibrated abstention when evidence is weak", are quoted in comparison row 1.19
  (*checked* there; `ARCHITECTURE.md` itself not opened). Another says a layer is to be measured on how accurate it is where it answers *and* on
  whether it declined the right cases (*checked*, D-602). The regression check counts a declined chord
  root as a wrong answer (*checked*, D-212). And a ratified amendment says a decision is still owed on
  what the user sees when most of a passage is doubtful, or when the music is not tonal at all —
  "when the system says 'this is outside my tonal vocabulary'" (*checked*, D-498).

## 4. The positions

### Position one — always name a chord over sounding music; leave the framework's question open (recommended)

Over every stretch where notes sound, the analysis names its best reading of the harmony, with the
rival readings and their weights. As an illustration (not a computed result): over a bare octave on G it
might name G major, with E minor and C major as rivals, the weights spread to show the notes do not
decide. A thin or ambiguous passage is shown as such by the weights, never by a blank. **Even a reading
with a very low weight is inferred and handed on.** Whether the user then sees it, sees it greyed, or
sees "N.C." in its place is the display's decision — the one the ratified amendment D-498 says is still
owed — and could include a user setting for a minimum confidence (your view, given this sitting). One
caution for that later decision: the weights are not yet calibrated, and the derivation says a consumer
"may compare masses within one working span's publication and may not read them as frequencies of being
right" (*checked*, derivation lines 988–992), so a minimum-confidence setting that means the same in
every piece needs a fitted calibration first. Withholding very low-weight readings from the display
instead would break the no-information-loss principle (#12) and the ratified rule that "every inferred
object must be displayable" (D-295, *checked*); the derivation lets the analysis hold back only weak
*rivals*, and only because they can be recomputed and the held-back weight is published (*checked*,
derivation lines 1039–1042). The framework's open question stays open, exactly as
you ratified it, for a later stage to take up — for example when the owed decision about doubtful and
non-tonal music is written, or when an idiom whose analysts write "N.C." is added. For the first
specification, "no chord over sounding music" is excluded by name, so that if a graded collection turns
out to contain such a label, the exclusion is already on record. Its cost, stated: such a label would
never be matched.

- *Towards the ultimate objective* (the most precise inference possible): every sounding stretch gets
  the reading the evidence most supports, together with everything else the analysis weighed. Nothing it
  computed is hidden behind a blank.
- *Towards the guiding principles:* build only on established fact (#1) — no open question is filled
  without evidence, as the framework's risk list requires; one home for each fact (#6) — doubt lives in
  the weights alone; no information loss (#12) — no computed reading is withheld; no value is graded on
  data it was not fitted to, and the annotations are themselves the measuring stick (#20, #21) — no
  answer is created that no annotation read so far contains, so nothing would have to be learned from
  nothing. It agrees with the rule that the engine always names a key (D-114).
- *What it costs:* the owed decision about doubtful and non-tonal music (D-498) is not answered inside
  this layer; it stays owed, to be met by whatever reads the weights. Over music that is not tonal at
  all, the layer will still name a tonal reading; whether its weights actually spread out there is
  unmeasured. The cost of never matching a "no chord" label is not counted.
- *Meta level:* acts on the analysis's own specification only.

### Position two — allow "no chord" as one of the rival answers over sounding music

The analysis could answer "no harmony here" — over a bare unison line, or music outside
the tonal language — and it would sit among the rivals with its own weight.

- *Towards the ultimate objective:* it could say something true that position one cannot, in music
  that has no harmony to name, and could carry the "outside my tonal vocabulary" message inside the
  analysis. But where "no chord" wins, the chord reading the notes most supported is pushed down to a
  rival; if it is still published as a rival, the label adds a claim but no information about the
  notes (*my reading*). And it moves into the analysis a choice that belongs to the display: whether
  a weak reading is shown as a chord or as "N.C." can reasonably differ from user to user, which the
  analysis cannot know.
- *Towards the guiding principles:* no annotation read so far writes the label, so its weight has
  nothing to be learned from; it would have to be set by hand (against #20 and #21, and against the
  register's rule that fitted values are fitted to the annotations, never tuned case by case — D-096,
  read at its title only). If it were used for weak evidence it would duplicate the weights — one fact
  in two homes (#6). The regression check would count every "no chord" winner as a wrong root (D-212).
  It changes the framework document you ratified.
- *Meta level:* acts on the analysis's specification and on the ratified framework document.

### Position three — never "no chord" over sounding music, and write that into the framework now

The first specification behaves exactly as in position one; the difference is that the framework's
open question is closed for good.

- *Towards the ultimate objective:* no difference from position one in what the analysis produces.
- *Towards the guiding principles:* it fills an open question with the most plausible answer, which the
  framework's risk list says shall not be done; and a later idiom that needs "N.C." would have to reopen
  a ratified document rather than take up an open question.
- *Meta level:* acts on the analysis's specification and on the ratified framework document.

### Recommendation: position one

Towards the objective: every sounding stretch is read and published with its full uncertainty; nothing
computed is hidden. Towards the principles: doubt has one home, the weights (#6); no answer is invented
that no annotation contains (#20, #21); no open question is filled without evidence (#1 and the
framework's risk list); and the exclusion is on record by name. Meta level: the specification only; the
framework stays as you ratified it. Position three buys nothing over it now and costs an amendment to a
ratified document. The price of position one is that the owed decision about doubtful and non-tonal
music must be made elsewhere, and that a "no chord" label, if one exists in a graded collection, is never
matched.

## 5. The silence half — put to you as a confirmation, not a choice

The record answers it: the derivation settles it, the six existing sentences about silence agree with
it (§6), the framework's lowest layers already produce the silent stretch, and your statement this
sitting — that a rest, in one voice or in all, is a fact the inference weighs and that may or may not
mean a chord change — is what the derived statements already do (§2). Carrying both readings of a
complete silence, with their weights, is what no information loss (#12) asks.

I will put it as: **the derived statement on silence stands as written** — a rest in any voice is
evidence the inference weighs; a complete silence carries two rival readings, the harmony continuing
through it or a silent stretch with no harmony.

Two details for the later writing of the specification, neither a choice now (*my reading*): from which
side a harmony may extend into a silence, and which key a silent stretch carries, since every stretch
has exactly one.

## 6. Where the existing sentences would go, under position one (my proposals)

The comparison file lists twenty sentences of the existing documents under the derived statement on
silence (*checked*; each read at its place). "Moved" means written into another part of the
specification; "set aside for the audit" means the sentence describes the current, unused engine and
becomes a question for the later audit of the code.

- **Six sentences that agree — all about silence.** From `ARCHITECTURE.md`'s description of the old
  slicing layer and from the old slicing design document: a stretch where every voice rests is recorded
  as an explicit empty stretch, not skipped (comparison rows 22.69, 42.15(ii), 42.34, 42.41, 42.63,
  42.83). Proposed: **moved to the specification of the layer that cuts the music**, since that layer
  produces the empty stretch; the derived statement on silence goes with them as the account of how
  the chord-and-key layer reads it.
- **Twelve sentences that differ — the old chord engine's "uncertain" flag.** From `ARCHITECTURE.md`'s
  section on the dormant chord engine, the old chord design document and the progression design
  document: the engine commits a chord, inherits the previous one, or declines and flags the stretch
  "uncertain", naming whether the root, the quality or one note's membership is in doubt (rows 3.21,
  6.16, 6.22(v), 6.49, 6.76, 6.100, 6.109, 6.118, 6.121(v), 6.128, 6.174, 53.6). Proposed: **set aside
  for the audit**, with the questions "when does the dormant engine decline, on what test, and what does
  it hand on?". The new specification has no such flag; the weights do that work.
- **One sentence that differs — the conflict between "never decline" and "calibrated abstention".**
  From `ARCHITECTURE.md`'s rules for the current engine (row 1.19). Proposed: **moved to the part of the
  specification that governs how doubt is presented** — the framework's "uncertainty surface", which it
  lists as "not a layer" (*checked*, `FRAMEWORK.md` §5) — because "declining when evidence is weak" needs a calibrated weight, which this layer does not
  yet have, and deciding to decline on it is a matter of reading the weights, beside the owed decision
  about doubtful music. Alternative: set aside for the audit.
- **One sentence that differs — "treat abstention as a valid outcome".** From a plan in
  `ARCHITECTURE.md`'s planned extensions (row 24.33(ii)). Proposed: **recorded as historical**, with the
  other half of the same sentence, which is already proposed historical as a plan. Alternative: moved
  to the measurement of the analysis, beside the rule on measuring correct declines (D-602).

Counted: six agree (six moved); fourteen differ (twelve set aside, one moved, one historical). With
these placed, the family is placed whole.

If position two is ruled instead: the derived statements on silence and on the shape of a reading are
amended to allow "no chord" over sounding music, the two abstention sentences are carried into the
specification, and the framework's open question is amended by its own act. If position three: the
derived statement on silence is amended to state the exclusion as final, the sentences go as above, and
the framework's open question is amended.

## 7. What was read, what was not, and what is unsettled

- **Read:** `FRAMEWORK.md` at its descriptions of the two lowest analysing layers and of the chord-and-key
  layer, the "not a layer" list, the open question on declining, its risk list, the agreement table's
  row on declining, and the first draft's version and settling route; the derivation at its statements
  on the shape of a reading, on admitting what analysts write, on notated evidence, on weights, on
  withholding and ties, and on silence; the comparison file at its list under the silence statement and
  at every row named in §6, with the rows on the abstention counter, the fitted abstention thresholds and
  leading and trailing silence; register entries D-114, D-212, D-295, D-498 and D-602; this morning's
  cadential six-four ruling; `cowork_blind_derivation_l0_l1_2026_08_31.md` at S-31, S-39 and S-50.
- **Not read:** the rest of the note-cutting layer's derivation; the exemplar files; `ARCHITECTURE.md` itself; the old
  design documents beyond the sentences the comparison file quotes; D-096 beyond its title; any jazz
  source.
- **Unsettled:** whether any graded collection writes a no-chord label; how an annotation over a silence
  is graded; whether the weights spread out over non-tonal music; where the owed decision about doubtful
  and non-tonal music is written; the two details in §5.

This surface writes no instruction for Claude Code, edits no tracked document, amends neither the
framework nor the decisions register, and allocates no register number.

**The questions, to be put later, one per turn:** first, the choice in §4; then the confirmation in §5,
with the placements in §6.

---

## §B. The check, run in the turn after the user's "ok, go on"

Run over completeness, coherence, correctness and absolutes, at the sources. Two additions came from the
user's own remark between delivery and check (that a very low-weight reading is still inferred and the
display decides whether to show it, perhaps as "N.C.", perhaps on a user minimum); they are folded into
§4 and marked as his view, not as a ruling. **Corrections, each made at its site, the former wording
kept here (#12):**

1. §2: *former* "Not checked: the exact list in the contract for the music's input …, which the
   derivation relays as including relations between individual voices. That contract was not opened
   this sitting." The note-cutting layer's derivation was then read at S-31, S-39 and S-50; it publishes
   REST-BEGINS naming the voice and ALL-SILENT. Now quoted, with the bound that this file's standing as
   the contract proper was not established.
2. §3: *former* "the analysts whose work has been read so far never write one; they name the implied
   harmony even over a bare octave or a unison passage". The second half was checked at no source. Now
   limited to "contain no such label", with the octave and unison claim marked unchecked.
3. §3: *former* "It also admits a chord whose root or third is not sounding (*relayed* from the
   comparison file's quotation …)". Now *checked* at the derivation's own statement, lines 308–311.
4. §3: *former* "its record notes that this conflicts with a planned target of "calibrated abstention
   when evidence is weak"". D-114's record names the conflict with "calibrated abstention" at §5.7a; the
   longer phrase is quoted in comparison row 1.19, not in D-114. Attribution corrected.
5. §4 position one: *former* "Over a bare octave on G it would name, say, G major, with E minor and C
   major as rivals" — stated as if computed. Now marked as an illustration.
6. §6: *former* "(the framework names it as a concern, not a layer)". Now the framework's own name, "the
   uncertainty surface", checked at §5.

**None of these moves the recommendation, a position's substance or a sentence's proposed placement.**
The search for "uncertain", "abstain" and "abstention" in the derivation returned nothing, which
supports §3's statement that the derived specification carries no such flag; that is a word search, not
a reading of every statement.

**Declared, in the act of this check:** one shell command (`true`, a command that does nothing) was run
in the container in error during the check. It read and wrote nothing, and no claim rests on it; it
breaks entry 287's "no shell at any point". This is the same slip entry 287 reports from the previous
sitting.

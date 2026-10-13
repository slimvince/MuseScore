# The L2-S32 family — the span content term — ratification surface, 2026-10-09

> **STATUS: RATIFICATION SURFACE, §A AND ITS CHECK §B.** *(Former wording, preserved (#12): "§A ONLY".)* Cowork, 2026-10-09 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_twenty_three.md`. Written as text, nothing asked in the
> turn that delivers it. The check (§B) comes in a later turn, and the questions after that, one per turn. Nothing here
> is applied, and no tracked document is edited. Marks: *checked* = read at the object by this sitting; *relayed* =
> taken from another record and not re-read here; *my reading* = this side's interpretation.

---

## §A.1 What this family is

The derived statement, whole (*checked*, `cowork_blind_derivation_l2_2026_09_27.md`, its lines 801–820):

> **L2-S32. The span content term rates how the span's events, under the reading's assignments, fit
> the chord in its spelled form. It counts both what sounds and does not belong (purity) and what
> belongs and does not sound (coverage), each with duration-weighted and metric-weighted forms. Chord
> tones, elaborations and the absence of chord members each contribute. The coverage part is a cost,
> never a requirement (L2-S10).**
> - *Defense.* The feature families of the published segmental system are purity, coverage (root, third,
>   fifth, added note, all members), bass, bigrams and metrical accent, each in plain, duration-weighted
>   and accent-weighted forms, with "figuration-controlled" twins that ignore the notes detected as
>   figuration [FACT (relayed, 08) — Masada & Bunescu, §4 and Appendix C]. Segment-level coverage is
>   credited for correct labels where the first event lacks the root [FACT (relayed, 08) — Masada &
>   Bunescu, §6.2.1]. A neural system adds an "absence" score for pitches that do not sound. It was not
>   shown to help on its data [FACT (relayed, 08) — Yang, Cwitkowitz & Duan 2023, Table 2], and that is
>   recorded so the absence side is not over-weighted by assumption.
> - *Source class.* Derived. Weights *measured*, UNESTABLISHED.
> - *Status.* Settled in shape.
> - *Premise.* Figuration-controlled forms are well defined because the assignments are part of the
>   reading. **False-negative path:** none beyond L2-S24's.
> - *Falsifier.* CODE. **Observable:** the content term's inputs. **Decision rule:** falsified if the
>   term reads an unspelled pitch class where the spelled pitch is available, or if it treats a missing
>   chord member as disqualifying. **Not falsified by:** a fitted weight near zero on some form.

**In plain words.** For each stretch of a candidate reading, L2's candidate score has a part that asks how well the
notes sounding in that stretch fit the proposed chord. It looks both ways: notes that sound but are not in the chord
(purity), and chord members that never sound (coverage). Each is counted plainly, weighted by how long the notes
last, and weighted by how strong their beats are. It reads the notes as the reading assigns them: a note the reading
calls a passing note is counted as a passing note, not as a wrong chord tone. It compares spelled notes with the
spelled chord (G♯ is not A♭). A missing chord member costs something but never rules a chord out. How much each of
these counts is fitted from annotated music (L2-S38), not set by hand.

**What the derivation says beside it** (*checked*): its source table names Masada and Yang as the extracts consulted
and no pack member, no input-contract statement and no exemplar (line 1357); the count table lists L2-S32 among the
statements with a measured part left UNESTABLISHED (line 1303). A search of the derivation for "S32" finds no open
question naming it. L2-S10 (lines 308–327, *checked*) is the rule that membership is by spelled pitch class and that
a chord is admissible over a stretch lacking its root or third; the enharmonic allowance — whether a note may count
as a chord member it sounds like though spelled differently — is left to the closure measurement OQ-L2-1 (line 1205,
*checked*), as the chord-tone-membership record of 2026-10-07 ruled (its lines 24–37, *checked*).

**So the family is two confirmations** (§A.6): the 31 row-parts filed under L2-S32, five of them placed by
derivation from UNPLACED; and the two rows the reading-parts record of 2026-10-07 sent to this family.

## §A.2 The research, searched before writing (entry 319 §2)

**At `docs/research_papers/BIBLIOGRAPHY.md`** (*checked*, the lines a search for the authors returned): Masada &
Bunescu 2019 (line 24, held), Yang, Cwitkowitz & Duan 2023 (line 33, held), Raphael & Stoddard 2003 (line 15, held).

**At the reading-pass extracts** (*checked* at the lines named; none read whole):
- **Masada & Bunescu 2019** (lines 138–187). The five feature families are "a function of the CANDIDATE SEGMENT and
  the CANDIDATE LABEL" (the extract's heading); purity and coverage each "come in a plain, a duration-weighted and an
  ACCENT-weighted form"; coverage tests root, third and fifth present, all chord notes present, and the added note
  present or absent (p. 16). The figuration decision is made "INSIDE the segment scoring, relative to the candidate
  label", and "every purity, coverage and bass feature has a 'figuration-controlled' twin" (pp. 15–19); the authors
  call their figuration rules "only approximations" (p. 15). On spelling, the paper normalises chord labels to
  canonical roots and says of the notes: "Whether they are spelled with sharps or flats is immaterial, as long as
  they are enharmonic with the root, third, fifth, or added note of the labeled chord" (p. 5, extract lines
  138–143). *My reading:* L2-S32 takes this system's shape and departs from it on spelling — L2-S32 rates the
  spelled pitch; the published system collapses spelling.
- **Yang, Cwitkowitz & Duan 2023** (lines 148–157, 231–257). The absence score "allow[s] the model to filter out
  pitch activations that are not active within the input music" (p. 679). Table 2 (p. 681): removing it changes root
  accuracy by −0.001, quality by +0.003, overall by −0.008; the authors: "The effect of removing the absence score is
  less significant." No spread is printed. The input is twelve unspelled pitch classes (the extract, line 99: "the
  spelling the score carries is discarded at input", seen in search lines only).
- **Micchi, Gotham & Giraud 2020** (lines 320–368), an extract that compares spelled with unspelled input. I did
  not search the other extracts for such comparisons; this extract itself relays one more, Temperley 2002's key
  finder, 83.8 → 87.4 with spelling (its lines 529–530, seen in search lines only — a key finder, not a chord
  term). *(§B item 1; former wording, preserved (#12): "the one extract I found that compares spelled with unspelled
  input" — no search of the other extracts was run.)* Table 6 (p. 50) averages fifteen models each way: spelled input 36.5% on the full Roman-numeral label,
  unspelled 0.4 points lower. The authors: "using full pitch spelling generally leads to slightly higher results
  overall, but the results are not statistically significant", and, because spelled analysis has more keys and roots
  to tell apart, "the spelling representation is preferable where the data is available." *My reading:* this is a
  model-input comparison, not a content term; it does not show that spelling helps, only that a harder,
  spelling-distinguishing task loses nothing on its data (#24 — no difference is read as a gain here).
- **Raphael & Stoddard 2003** (lines 84–99): the emission is per pitch, by the pitch's category relative to the
  label — in the extract's words, "root, third, fifth of the chord; in the scale but not the triad; otherwise" —
  with the metrical position as a covariate, the output distributions learned from unlabelled music (pp. 3–4). D-527
  names this as "the Raphael-Stoddard structure"; its three categories (chord member, within-scale, outside-scale)
  group the paper's five. I found no measurement in the extract, as read, of the scale/other split against a model
  without it. *(§B item 2; former wording, preserved (#12): "the category weights learned from data (p. 3). My
  reading: this is the published source of the three emission categories" — the paper has five categories, not
  three; that it is the source is D-527's own statement, not my reading; and training is unsupervised, pp. 3–4.)*

**What the research does not give.** No source I read measures, on the same data and with its uncertainty, a content
term that reads spelling everywhere against one that reads it only for a few labels; nor one that splits elaborations
by key collection against one that does not.

## §A.3 The 31 row-parts, as the comparison proposed them (*checked*, each at its row)

§7 of `ratification_surfaces/cowork_comparison_l2_reading.md` (*checked*, its lines 71204–71207) files 31 row-parts
under L2-S32: 23 AGREES, 8 DIFFERS.

**Group 1 — AGREES, proposed ADOPTED — carried under L2-S32 (21):**
Rows 1.33 (*WITHHELD — D-449*), 1.35 (*WITHHELD — D-449*), 1.44 (*WITHHELD — D-534*), 6.18 claim (i), 6.44, 6.71
claim (ii) (*WITHHELD — D-329*), 6.74 claim (ii), 6.84 claims (ii) and (iii), 6.112 claim (i), 6.114, 8.71 claim (i),
10.14 claim (ii), 10.17 claims (i) and (iii), 44.45 claim (ii), 44.50 claim (viii), 44.76 claim (i), 48.7 claim (ii),
58.2 claims (ii) and (iii).
They say, each in its own words: the pitch emission is scored per tone (Rows 1.33, 10.17(i), 58.2(iii)); the
missing-tone penalty is paid in proportion to how long the tone is missing (Rows 1.35, 10.17(iii), 58.2(ii)) and is
counted per chord factor, "root, third, fifth, seventh" (Row 1.44); the note evidence includes "the slice's
pitches, their notated spelling, their metric weight" (Row 6.18(i)); the layer uses "the notated spelling … which
names a chord's root where pitch class cannot" (Row 6.44); each candidate is "scored by how well the pitches fit it"
(Row 6.71(ii)); a reading "that needs implausible chord tones … is penalised" (Row 6.74(ii)); present chord tones are
credited, an absent one is "a *mild* shortfall", and a note outside the candidate goes to the membership decision
"rather than scored as a wrong pitch" (Row 6.84(ii), (iii)); a run of notes forms a chord "only when they are
genuinely its chord tones" (Row 6.112(i)); a clear triad with all notes chord tones (Row 6.114); spelling
"disambiguates enharmonic/symmetric roots pitch-class-blind fit cannot" (Row 8.71(i)); the joint estimator's pitch
emission term (Row 10.14(ii)); the elaboration relation "cleans the key layer's emission input" (Row 44.45(ii), with
Rows 44.50(viii) and 44.76(i) travelling with it); the cleaned content entering an "emission `P(pitches | tonic,
mode, chord)`, metric-weighted" (Row 48.7(ii), travelling with Row 10.14(ii)). *(§B item 3; former wording, preserved
(#12): 'as "a pitch emission … metric-weighted"' — "a pitch emission" is the comparison's claim summary, not the
source's words.)*

**Group 2 — AGREES, but proposed QUARANTINED (2).** The rule entry 314 §2 states applies: follow the proposal, not the
axis.
- **Row 1.32** — "the pitch and bass emissions reading the STRUCK set where the design says sounding" (OI-228, a
  declared conformance gap). *Audit question:* "do the shipped pitch and bass terms read the struck set rather than
  the sounding set, and where?"
- **Row 6.95** — "A candidate needing many such implausible chord tones is penalised". Travelling with Row 6.94,
  which the chord-tone-membership record of 2026-10-07 ruled QUARANTINED with the comparison's audit question (its
  Ruling 5, lines 170–174, *checked*).

**Group 3 — DIFFERS, proposed QUARANTINED (3).** Each says how an old component reads pitch — Row 8.71(ii) in the
engagement design's channel table, the other two in descriptions of legacy and dormant code; whether the code does
what the text says is the audit's question. *(§B item 4; former wording, preserved (#12): "Each describes how an old
component reads pitch" — Row 8.71(ii) is a sentence of a design document; see §A.4 B.)*
- **Row 8.71 claim (ii)** — the function-layer engagement design (`cowork_layer5_engagement_design.md`): spelling is
  "Read only where the distinction *is* a spelling distinction". *Audit question:* "where, if anywhere, does the
  dormant function layer read spelling, and under what condition?"
- **Row 23.5** — `ARCHITECTURE.md`'s legacy chord analyzer: "TPC (Tonal Pitch Class) data is used for enharmonic
  disambiguation when available." *Audit question:* "does the legacy chord analyzer rate unspelled pitch classes and
  read the notated spelling only to choose between enharmonic readings, at the current commit?"
- **Row 39.9 claim (i)** — `docs/scoring_model.md`'s dormant scorer: "Build a 12-element pitch-class weight
  histogram from the input tones". *Audit question:* "what does the dormant scorer collect from the sounding notes
  before it computes its candidate scores — pitch classes or spelled pitches — and with what weights?"

**Group 4 — DIFFERS, UNPLACED (5): Rows 5.19, 5.22, 5.194 claim (ii), 5.229, 5.230 claim (ii).** §A.4.

**Arithmetic.** 21 + 2 = 23 AGREES; 3 + 5 = 8 DIFFERS; 31 in all, matching §7's list.

## §A.4 The five UNPLACED row-parts — how far spelling reaches

**The rows, whole** (*checked* at the reading file; all five from member 5, `cowork_layer5_function_design.md`, the
ratified design of the outgoing function layer — the reading file's member table names its layer "design ratified",
line 48, and `DECISIONS.md` lists D-335 to D-338, homed in it, as ratified by the user 2026-08-02, *checked*):
- **Row 5.19** (lines 4043–4058): "**Spelling-aware where, and only where, the distinction is a spelling
  distinction.**" — §2.
- **Row 5.22** (lines 4090–4102): "Elsewhere it does not depend on spelling." — §2.
- **Row 5.194 claim (ii)** (lines 6765–6781): the German sixth is separated from the dominant seventh only by
  spelling and resolution — "the one place the layer must read spelling to choose the label." — §5.6.
- **Row 5.229** (lines 7335–7344): "**Spelling is read only where the distinction is a spelling distinction** (§5.6
  German sixth; the applied secondary leading tone)." — §8.
- **Row 5.230 claim (ii)** (lines 7348–7364): "Reading spelling everywhere would re-introduce a second spelling
  interpreter; the layer reads through the one shared interpreter …, and only for the labels that require it." — §8.

The comparison, at Row 5.19: **UNPLACED** — "the outgoing rule confines spelling to two label distinctions, and L2-S10
and L2-S32 read spelled pitch in every chord-tone and content decision; the two texts give different reach to the same
evidence, and a disposition would choose between them." The other four are filed "with Row 5.19".

**In plain words.** The old design of the function layer read the spelling of a note in two places only: to tell a
German sixth from a dominant seventh (same keys on a piano, different spelling and resolution), and to name an applied
leading tone. Elsewhere, in its own words, it "does not depend on spelling" (Row 5.22). *(§B item 5; former wording,
preserved (#12): "Everywhere else it worked as if G♯ and A♭ were the same note." — a paraphrase stronger than the
source.)* L2-S32 reads the spelling everywhere it is
available, and is falsified if it does not.

**What the rule was for, read at its own text and its neighbours** (*checked*):
- **Its stated reason** is in Row 5.230 itself: reading spelling everywhere "would re-introduce a second spelling
  interpreter". The first half of that sentence, "the layer reads through the one shared interpreter", is Row 5.230
  claim (i), which the comparison proposes RELOCATED to *L0 — The notated record* with Row 5.21, under the input
  contract's IC S-3 (lines 4077–4087, 7363). On the L0/L1 side the same §2 sentence is Row 9.4, proposed ADOPTED —
  carried under S-3 and S-14: "the fact is given, once, and read rather than derived — which is what 'one shared
  interpreter' asks for" (`ratification_surfaces/cowork_comparison_l0_l1_reading.md`, lines 4757–4766, *checked*;
  whether that proposal has since been ruled I did not establish). *My reading:* the reason is met without the
  restriction — L2 reads the spelling L0 gives, once, and interprets nothing. This rests on the input contract's
  S-3 and on the two proposals just named, neither of which I found ruled. *(§B item 6: the last sentence added.)*
- **The layer it belonged to** did not read notes for its chords: the old function layer "resolves by selecting among
  the readings Layer 4 carried … never by re-deriving a chord from the raw notes" (Row 5.14; the quotation *relayed*
  from the L2-S30 surface's line 141–142, not re-read at the reading file; the row ruled QUARANTINED in the L2-S30
  record of 2026-10-09, its line 32, *checked*). *(§B item 7; former wording, preserved (#12): "(Row 5.14, ruled
  QUARANTINED in the L2-S30 record of 2026-10-09, its line 32, checked)" — the quotation was not read at its row.)* And the old chord layer it selected from read spelling as a
  main input — "most importantly the **notated spelling** …, which names a chord's root where pitch class cannot"
  (Row 6.44, Group 1 above). *My reading:* in the old two-layer design spelling had already entered at the chord
  layer, so the function layer needed it only for the two labels the chord layer did not name. In L2's one decision
  (L2-S11) there is no second layer, and the content term is where spelling enters.

**The alternatives, weighed.**

- **A. HISTORICAL — a rule of a superseded design.** Towards the objective (#4): nothing lost — L2-S32 already reads
  the spelled pitch, so the two distinctions the old rule protected (German sixth against dominant seventh; the
  applied leading tone) are still separated, and more besides — the German sixth against the dominant seventh is
  carried under L2-S1 as Row 5.194 claim (i), ruled in the reading-parts record of 2026-10-07 (its line 26,
  *checked*) *(§B item 8: this clause added)*; whether a misspelled note may still count as the chord
  member it sounds like is the enharmonic allowance, open under OQ-L2-1. Towards the principles: #12 (each row keeps
  its text and proposal; the label is added beside it); #6 (whether the dormant function layer reads spelling only
  there is already the audit question of Row 8.71(ii), Group 3, which carries the same sentence from the engagement
  design); D-599; and the precedent of the score-decomposition record's Ruling 3 of 2026-10-07 (its lines 59–78,
  *checked*), which placed another rule of a superseded design — D-330's "never a pooled recompute" — HISTORICAL and
  declined QUARANTINED because "these are rules, not descriptions of code; the dormant decoder's window is under audit
  through Row 6.50". Meta level: filing a label on rows.
- **B. QUARANTINED, travelling with Row 8.71(ii).** Towards the objective: nothing gained. Towards the principles: the
  disposition vocabulary gives QUARANTINED to a statement of "how the implementation currently works" (the reading
  file's §5, line 320, *checked*); these five are design rules, and the one audit question they could raise is
  already Row 8.71(ii)'s. Declined on the score-decomposition precedent. *A coherence note (§B item 9):* the same
  rule is filed two ways — the comparison proposes Row 8.71(ii), the engagement design's sentence, QUARANTINED, and
  this surface proposes the function design's five sentences HISTORICAL. *My reading:* the engagement design's
  channel table records what the built dormant layer uses (its next row, 8.73, says "already built"), so its row
  carries the audit question; the function design states the rules. Following the comparison's proposal for Row
  8.71(ii) is entry 314 §2's rule; filing all six HISTORICAL would leave the dormant layer's spelling reach with no
  audit question.
- **C. ADOPTED — proposed: L2 reads spelling only where a distinction is a spelling distinction.** This would change
  L2's algorithm, narrowing L2-S32 and L2-S10. Towards the objective: against — spelling "names a chord's root where
  pitch class cannot" (Row 6.44), and the comparison read (Micchi et al., §A.2) shows spelled input losing nothing
  significant while telling more apart. *(§B item 1; former wording, preserved (#12): "the one comparison found …
  losing nothing".)* Towards the principles: against #12 (information the record holds would go
  unread), against L2-S10 (Settled), and against the carried Rows 6.44 and 8.71(i). Its own reason is met by L0
  (above). Excluded.

**So the alternatives have collapsed to A.** I put it in the first confirmation, not as a separate choice.

## §A.5 The two travelling rows — Rows 10.18 claim (i) and 48.43 claim (i)

**Why they are here.** The reading-parts record of 2026-10-07 sent them to this family: "Rows 10.18(i) and 48.43(i) to
L2-S32's family (the emission categories against the content term)", and carried "whether the content term rates
in-collection and outside-collection elaborations differently (L2-S32's family)" (its lines 38–40 and 65–66,
*checked*).

**The rows, whole** (*checked*):
- **Row 10.18 claim (i)** (lines 22478–22488), `cowork_joint_estimator_factorization.md` §3: "each tone classified
  into categories: chord member (root / third / fifth / seventh-or-tension per the degree class's template),
  within-collection non-chord tone, outside-collection tone". L2-S1: **DIFFERS**. Proposed **UNPLACED** — "ratified
  tone categories with no elaboration relation, against L2-S1's assignment carrying one".
- **Row 48.43 claim (i)** (lines 63796–63806), `cowork_joint_estimator_architecture.md` §5a, *WITHHELD — D-527*: "each
  tone is emitted by category (chord member vs within-scale non-chord tone vs outside-scale tone — the
  Raphael-Stoddard structure)". **UNPLACED**, travelling with Row 10.18(i).

D-527 is LIVE, "decided 2026-07-19 · ratified by user" (`decisions/group_A.md`, lines 601–630, *checked*). The two
rows' claim (ii) — the covariates — was ruled ADOPTED — carried under L2-S25 and under L2-S24 in the
assignment-evidence record of 2026-10-05 (its lines 90–91 and 142–143, *checked*). *(§B item 10; former wording,
preserved (#12): "Its claim (ii) — the covariates — is already carried under L2-S24 and L2-S25 (both rows' claim
(ii), as proposed)." — "Its" read as D-527's, and the ruling was not cited.)*

**What is already settled, and what is left.** The reading-parts surface (its lines 182–190, *checked*) read these
categories as not a fifth part of a reading: whether a note lies inside the tonality's collection "is computable from
its spelled pitch and the span's spelled tonality, both already held, so nothing is lost by not publishing it as a part
(#12, the recomputable clause)." What is left is one question about the content term: **should an elaboration count
differently in the content term according to whether it belongs to the key's collection** — for example (*my
example*), in C major, a passing F against a passing F♯?

**An earlier ruling leans on the same distinction** (*checked*, §B item 11): the elaboration-relations record of
2026-10-05 declined a separate "chromatic neighbour" relation because "a chromatic neighbour is already distinguished
by D-527's outside-scale category" (its lines 83–88). *My reading:* that ground holds as long as the distinction stays
available — as a fact computable from spelled pitch and spelled tonality it is; whether the candidate score uses it
is this question.

**In plain words.** L2-S32 says chord tones, elaborations and missing chord members "each contribute". It does not say
whether a passing note that belongs to the key counts the same as one that does not. The ratified joint-estimator
design (D-527), following Raphael and Stoddard, did split them. Nothing I found measured whether the split helps.

**The alternatives, weighed.**

- **A. ADOPTED — proposed: OQ-L2-3's held-out comparisons gain one arm** — the content term with an elaboration's
  contribution split by whether its spelled pitch lies in the span's spelled tonality's collection, against the same
  term without the split; fitted weights only; nothing chosen now. Documentation only now; L2's algorithm changes only
  if the measurement shows the split earns its place beyond its uncertainty (#24). Towards the objective (#4): the
  better form is chosen on the music. Towards the principles: D-254 (measure, do not ask); #12 (a ratified, published
  form is not set aside unheard); #17(b) (no build without a prediction); the user's standing rule of 2026-10-07 that
  a design rule is tested by measurement as soon as there is reason to suspect another form might improve inference
  (as he stated it; its place in the repository record not checked this sitting — §B item 12); and the
  precedents of the tonality-evidence record's Ruling 4 of 2026-10-06 (its lines 99–122, *checked*: three UNPLACED
  rows carrying the joint estimator's spelling emission placed ADOPTED — proposed as one more arm of OQ-L2-3, "Each
  enters with fitted weights only. Nothing is chosen now.") and the structural-bass record's Ruling 3 of 2026-10-08
  (relayed from entry 322 §1: OQ-L2-3 gained the bass-degree prior as a held-out comparison). Cost: one more arm in a
  measurement already owed. Meta level: the analysis's own specification.
- **B. ADOPTED — proposed as a form of L2-S32 now.** Would change L2's algorithm today (one more fitted form). Towards
  the objective: possibly the same end state, but untested. Towards the principles: against D-254 and #17(b) — it
  builds before measuring, with no prediction recorded; it also spends capacity under L2-S38's declared budget before
  the gain is known. Declined.
- **C. HISTORICAL — the old emission's categories, superseded by L2-S1's assignment.** Towards the objective: a
  published, ratified distinction would be dropped without a measurement. Towards the principles: against #12 and the
  2026-10-07 rule; the tonality-evidence record declined HISTORICAL for the spelling emission because "a published,
  ratified form with a measured basis would be set aside unheard" — here the form is published and ratified but I
  found no measured basis, so the precedent applies with that difference; and it would leave the elaboration-relations
  ground above resting on a distinction L2 never tests. Excluded. *(§B item 13; former wording, preserved (#12): "the
  tonality-evidence record declined HISTORICAL on this ground for the spelling emission. Excluded." — the precedent's
  "measured basis" does not hold here.)*
- **D. ADOPTED — carried under L2-S32.** L2-S32's text does not name the split; carrying it would claim the derivation
  says what it does not. Excluded.

*My reading, recorded and not proposed:* a note outside the key's collection already bears on the tonality terms
(L2-S20 reads "which spelled scale degrees have sounded", *checked* at line 528–530), so the comparison would show
whether a split inside the content term adds anything beyond that.

**So the alternatives have collapsed to A** by D-254 and the precedents. I put it as the second confirmation, in its
own turn.

## §A.6 What stands, and what the questions would decide

**Confirmation 1 — the 31 row-parts.**
*Documentation (the only part decided):* the 26 row-parts of Groups 1–3 take the labels the comparison proposed (21
ADOPTED — carried under L2-S32; 5 QUARANTINED with their audit questions); Rows 5.19, 5.22, 5.194(ii), 5.229 and
5.230(ii) are placed HISTORICAL from UNPLACED. No outgoing text is edited; the labels are written beside each row by the
application dispatch. Rows 1.33, 1.35, 1.44 and 6.71 are on WITHHELD statements (D-449, D-534, D-329); those entries'
register status is settled at the ratification act, not here.
*Algorithm:* unchanged. L2-S32's wording does not change.

**Confirmation 2 — Rows 10.18(i) and 48.43(i).**
*Documentation:* both placed ADOPTED — proposed from UNPLACED; the proposal is one line beside OQ-L2-3 naming the
held-out comparison of §A.5 A. D-527's register status is settled at the ratification act, not here.
*Algorithm:* unchanged now; it would change later only if the measurement favours the split.

**The method that stands, as the ruled statements define it** (each *checked* at the derivation this sitting):
- Where the boundaries fall "is decided together with the tonality, the chord and the assignments, in the one
  decision" (L2-S11, lines 331–333).
- The candidate score is "a sum over its spans of span terms, plus a sum over adjacent span pairs of pair terms"; a
  span term "reads the span's position, its content (sounding set, assignments, attachments), the evidence at and
  inside it, and its four fields" (L2-S31, lines 776–780).
- The assignments "are made inside the candidate score, relative to each candidate reading's chord, and never by a
  detector that runs first" (L2-S23, lines 601–602).
- "An event is a chord tone of a span only if its spelled pitch class is a member of the span's chord, spelled", and a
  chord is admissible over a stretch lacking its root or its third (L2-S10, lines 308–311); the enharmonic allowance
  is open under OQ-L2-1.
- The content term: L2-S32 as quoted in §A.1 — purity and coverage, plain, duration-weighted and metric-weighted, read
  under the reading's assignments, against the spelled chord; a missing member a cost, never a disqualification.
- "Every weight of the candidate score is fitted from annotated music, not set by hand", on held-out folds, with the
  capacity budget declared in advance (L2-S38, lines 938–941).

**The questions to be put, each alone, in later turns:**
1. Whether to confirm the 26 row-parts as the comparison proposed them, and Rows 5.19, 5.22, 5.194(ii), 5.229 and
   5.230(ii) as HISTORICAL. Ground: towards the objective (#4), no reading changes and nothing the analysis uses is
   lost; towards the principles, D-599, the route ruling of 2026-10-04 ("Rows no family reaches stay proposals",
   *checked* at the route record's line 88 — §B item 14; former wording, preserved (#12): "relayed from the L2-S30
   surface, which checked it at the route record's line 88"), #12, #6, and the
   score-decomposition precedent. Meta level: filing labels on rows.
2. Whether to confirm Rows 10.18(i) and 48.43(i) as ADOPTED — proposed, the proposal being the held-out arm under
   OQ-L2-3 (§A.5 A). Ground as in §A.5 A. Meta level: the analysis's own specification.

## §A.7 Searches made so the confirmations do not repeat an earlier ruling, or miss a row

- **The L2 ruling records of 2026-10-04 to 2026-10-09** (the 35 at the rulings folder's listing of those dates; one
  search for "S32", "spelling distinction", "second spelling interpreter" and the numbers of Rows 5.19, 5.22, 5.194,
  5.229, 5.230, 8.71, 23.5, 39.9, 1.32, 6.94 and 6.95; a second for every Group 1 row number). None of this family's 31
  row-parts is named as placed by an earlier record. The hits were other claims of the same rows placed under other
  statements (for example Rows 6.18(ii), 6.74(i), 6.84(i), 6.112(iii), 10.14(i), (iii), (iv), (vii), (viii),
  10.17(ii) and (iv), 44.45(i), 44.50 claims (i)–(vii) and (x), 44.76 claims (ii)–(v), 48.7(i), 58.2(i)); Row 6.94
  (QUARANTINED, chord-tone-membership Ruling 5); the two travelling rows (reading-parts record); and the
  metric-strength record of 2026-10-07, which carried Rows 5.292, 42.51, 42.52, 42.54 and 48.13 under L2-S32 among
  other statements (its lines 26–36, *checked*) — rows not in §7's list for L2-S32 and not placed again here.
  *Bound:* a range written after other numbers is outside the number pattern, as the L2-S30 surface recorded.
- **The decisions groups** A, C, F, G and H for "spelling distinction", "second spelling interpreter" and "only for
  the labels": no hit. The other groups were not searched.
- **The L0/L1 reading** for "spelling distinction", "second spelling interpreter" and four category phrasings
  ("within-scale non-chord", "within-collection non-chord", "outside-collection tone", "outside-scale tone") *(§B
  item 15; former wording, preserved (#12): "and the three category phrasings")*:
  hits at Row 9.4 (§A.4) and Row 24.6, which the L0/L1 reading proposed RELOCATED to L2 and which the L2 reading
  tabulates at Row 8.71 (its Row 62.34, lines 70721–70727, *checked*).
- **The L2 surfaces** (`ratification_surfaces/cowork_l2_*.md`, the 34 at the boot listing of the folder, staged at the
  check)
  for the same phrases and Rows 5.19, 5.22, 5.229, 5.230: the reading-parts surface (§A.5); the elaboration-relations
  surface, lines 129 and 335 (D-527's categories; the chromatic-neighbour ground now in §A.5); and number-pattern
  hits on other rows (5.190, 5.196, 5.197, 5.199) that are not this family's. *(§B item 16; former wording, preserved
  (#12): "for the same phrases: only the reading-parts surface (§A.5)." — at the first writing only two L2 surfaces
  were staged, so the search reached two files, not the folder.)*
- **Rows proposed ADOPTED — proposed on this family's subject** (entry 322 §2): a search for that proposal within 400
  characters of "spell", "purity", "coverage", "missing", "absent", "non-chord", "chord tone", "figuration" or
  "collection", either side, returned one line (2297, Row 2.51(ii), the spelling of a tonality span — not the
  content term). I then listed the 64 lines carrying the proposal (one of them the vocabulary's own definition, line
  313) and read the heads of the groups whose subject
  could touch the content term (*checked*): **Row 10.23** (lines 22540–22548), proposed "that whether a pitch belongs
  to a tonality's collection be tested against the collection itself, never through the tonic", names no derived
  statement; **Row 1.55** (lines 1308–1319, with Rows 1.56 and 21.1(ii)), proposed "that the search over readings be
  independent of how the values of the candidate score's terms are produced", likewise. Neither is filed under
  L2-S32 and no family reaches them, so under the route ruling they stay proposals and are not placed here. *My
  reading:* Row 10.23 bears on how §A.5's "inside the key's collection" would be tested if the arm is built (D-323,
  LIVE, homed in `docs/scoring_model.md`, states the same rule — `DECISIONS.md` line 439, *checked*); I record it
  beside §A.5, not as part of the question. Rows 10.23, 1.55 and 21.1(ii) are named by no ruling record of 2026-10
  (one search, no hit). *(§B item 17; former wording, preserved (#12): "(D-323 states the same rule for the old
  scorer)" — D-323 is not marked LEGACY; and "None of the 64 was named by an earlier record of 2026-10 that I searched
  (no hit for 10.23, 1.55 or 21.1(ii))" — only three were searched.)* *Bound:* one
  pattern search and a reading of group heads; a proposal travelling with another head on this subject would be
  missed.

## §A.8 What was not read

The papers themselves (only the extracts, at the lines named); `cowork_layer5_function_design.md` and the other outgoing
documents at their own lines (the rows' quotations are the reading file's); the ledger; the reading file's §8 to §14
beyond the lines cited; the decisions groups other than A, C, F, G and H; the L0/L1 rulings, so whether L0/L1 Row 9.4's
proposal has been ruled is not established; the structural-bass record (its Ruling 3 is relayed from entry 322).

---

## §B The check, at the sources (2026-10-09, on the user's "continue")

The landed §A was re-read whole at the device's copy staged back (30,241 bytes), and its claims were checked at the
objects they cite — those reopened are named below — on four axes: completeness, coherence, correctness, and
absolutes. Every correction is made at its site with the former wording kept (#12). **None moves a placement, a
proposal, the count, or a recommendation.** Two items (11, 13) add ground to §A.5's exclusion of HISTORICAL; one (9)
records a coherence point the user may weigh.

1. §A.2, §A.4 C — Micchi et al. was called "the one" comparison found; no search of the other extracts was run, and
   the extract itself relays Temperley 2002's key finder. "Losing nothing" became "losing nothing significant".
2. §A.2 — Raphael and Stoddard have five categories, not three; that they are D-527's source is D-527's own
   statement; training is unsupervised (pp. 3–4).
3. §A.3 — Row 48.7(ii)'s "a pitch emission" was the comparison's summary quoted as the source's words.
4. §A.3 — Group 3's heading called all three rows descriptions of code; Row 8.71(ii) is a design document's sentence.
5. §A.4 — "worked as if G♯ and A♭ were the same note" was stronger than the source; now the source's words.
6. §A.4 — the "reason met by L0" reading now says it rests on S-3 and two unruled proposals.
7. §A.4 — Row 5.14's quotation was taken from the L2-S30 surface, not read at the row; marked relayed.
8. §A.4 A — the German sixth / dominant seventh separation is now cited as carried under L2-S1 (Row 5.194(i),
   reading-parts record line 26).
9. §A.4 B — a coherence note: the same spelling rule is filed QUARANTINED at Row 8.71(ii) (the comparison's proposal)
   and HISTORICAL at the five function-design rows (this surface's proposal); the difference is stated as my reading.
10. §A.5 — the covariate claims' placement is now cited at its ruling (assignment-evidence record, lines 90–91,
    142–143); "Its" no longer reads as D-527's.
11. §A.5 — added: the elaboration-relations record's Ruling 1 declined a "chromatic neighbour" relation because D-527's
    outside-scale category already distinguishes it (its lines 83–88); found by the widened surface search (item 16).
12. §A.5 A — the 2026-10-07 standing rule is now attributed to the user's statement; its place in the repository was
    not checked.
13. §A.5 C — the tonality-evidence precedent declined HISTORICAL for a form "with a measured basis"; this form has
    none found; the difference is stated.
14. §A.6 — the route ruling's "Rows no family reaches stay proposals" is now checked at its line 88.
15. §A.7 — four category phrasings were searched in the L0/L1 reading, not three.
16. §A.7 — the "L2 surfaces" search had reached only the two surfaces then staged; the check staged all 34 and reran
    it.
17. §A.7 — D-323 is LIVE, not a rule "for the old scorer"; and only Rows 10.23, 1.55 and 21.1(ii) were searched in the
    ruling records, not all 64.

**Confirmed at the objects without correction:** the derivation's L2-S32, L2-S10, L2-S11, L2-S20, L2-S23, L2-S31,
L2-S38 and OQ-L2-1 lines; §7's list and the arithmetic (21 + 2 + 3 + 5 = 31); every row quotation in §A.3 and §A.4
other than items 3 and 7; Masada & Bunescu's spelling sentence at p. 5 §5.1 (extract line 137) and the absence score at
p. 679 §3.5 (Yang extract line 146); D-527's status line; the tonality-evidence Ruling 4 and score-decomposition Ruling 3
quotations; Row 6.94's ruling.

**Swept for absolutes** ("all", "every", "none", "no", "nothing", "only", "never", "one", "whole") at each hit in §A:
those left stand on a named search or read and carry its bound, or quote a source.

**What this check did not do.** It did not open the papers, the outgoing documents at their own lines, the ledger, the
L0/L1 rulings, the structural-bass record, or the decisions groups other than A, C, F, G and H; it did not search the
other extracts for spelled-against-unspelled comparisons.

---

*Provenance: Cowork, 2026-10-09 (Stockholm), the sitting booted on entry 323. The user's words: the opening
instruction; "continue"; "continue" (the check).*

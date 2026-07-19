# The desk simulation of the ratified factorization (the #17c stage; discharging OI-181's declared forms)

**★ USER-RATIFIED 2026-07-19** — the §7 asks were granted in full: the verdict; the §4.1 granularity
amendment (now incorporated in `cowork_joint_estimator_factorization.md` §2/§3 with dated marks); the
§4.2 initial-state-only prior record (incorporated at §3.10); the findings dispositions (§4.3 rides
OI-177; §4.4 → OI-185; §4.5 → OI-184; §4.6 handled by THIS section as the tracked record, plus a dated
courtesy note on the report's on-disk copy — the report itself is untracked per the `/cc_*.md` ignore
policy and stays so, per the user's call at CC's 2026-07-19 stop); OI-181 closed.

**Author:** Cowork, 2026-07-19, at the user's direction. **Standing:** the desk-simulation stage of the
#17 funnel for the joint estimator — the next action named by `cowork_joint_estimator_factorization.md`
§6 (★ user-ratified 2026-07-19) and the 2026-07-19 handoff block. **This is paper only** — no code, no
build, no corpus run, no golden, no re-baseline; the estimator funnel stays shut. The traces run the ten
§6 cases (five synthetic, five corpus) against the ratified specification, answering FIRST "does the
mechanism fire on this case?" (control flow), THEN "which term moves, by how much?" (arithmetic), per
#17c and the OI-181 declared small-instance forms (truncated candidate sets; printed DP arithmetic).

**What ratification will be asked for at the end (§7):** the verdict (nine of ten traces pass as
specified; the tenth — the segmentation case — surfaced ONE specification under-determination, factor
granularity, recorded as a surprise per #13 with a proposed amendment: the stage doing its job), one
open §5a question settled by trace (the signature prior is INITIAL-STATE-ONLY, re-anchored at a
mid-piece signature change — the persistent-pull variant is rejected), and the findings register
(sensitive-cell records feeding OI-177, one measurement-side alignment question, one historical-report
erratum).

---

## 0. Ground rules (declared before any trace)

1. **All table values are PROVISIONAL** — declared here (§1) before use, each labeled with its
   provenance class: the FORM is from the ratified specification and the derived forms in
   `cowork_term_theory_grounding.md` §1 (F1–F10); the VALUES are hand-declared stand-ins whose only job
   is to let the mechanism be traced. No value here survives into any fit; fitting happens only under
   the OI-176/OI-177 gates. A verdict that would flip within the plausible range of a provisional value
   is reported as a NEAR-TIE with the sensitive cell named — never as a win.
2. **Identity weights.** Every trace runs the generative product (all `w = 1`) — exactly the ratified
   mandatory ablation baseline. The desk simulation therefore tests the structure and the tables, not
   the weight layer.
3. **Arithmetic** is in natural-log points, rounded to 2 decimals; sums were checked with a scratch
   calculator (arithmetic checking only — no model code was written; the figures are declared hand
   values, not measurements, so #17f's generated-artifact rule does not apply to them; every CORPUS
   fact, by contrast, is verified at a named source this session and cited at its trace).
4. **Truncated candidate sets** are declared per case (the OI-181 form). The truncation is part of the
   record: a candidate excluded from the set is excluded by the stated reason, and a reader can re-run
   the trace with a wider set.
5. **Shared-factor cancellation:** factors identical across all compared hypotheses of a case (e.g. the
   boundary probabilities when every hypothesis uses the same segmentation) are dropped from both sides
   and said so. Only differences decide.
6. **Corpus-fact verification:** every note, spelling, tick, ground-truth label, and prior-output figure
   used in §3–§4 was read this session from the committed data (`tools/corpus/<preset>/*.ours.json`,
   `tools/dcml/when_in_rome/.../analysis.txt`, `tools/robust_stop/corpus_transposition_offsets.json`)
   or from a named report; the source is cited at each case header. **bwv145.5 is one of the 12
   OI-142-transposed editions (offset +2)** — its WiR analysis text reads two semitones below our
   score, and every GT fact taken from it is transposed +2 here (the reports' `dcml_root=11` figures
   already are, via `dcml_parser.load_wir_regions`).

## 1. The provisional tables (T0–T9)

Notation: values in probability, with ln in brackets. Labels: **[spec]** = the ratified factorization
form; **[T]** = THEORY/FACT-anchored direction from the F1–F10 derivations; **[prov]** = hand-declared
provisional magnitude.

**T0 — signature/declared-mode prior `P_prior(k₁ | signature, declared mode)`** [spec §3.10; F2:
no published form — the form is OURS, ledgered]. For a signature of s fifths, with relative pair
(maj(s), min(s)):

| cell | p | ln |
|---|---|---|
| maj(s) | .38 | −0.97 |
| min(s) | .27 | −1.31 |
| each key one fifth away (4 keys: maj/min × sharpward/flatward) | .05 | −3.00 |
| each of the remaining 18 keys | .0083 | −4.79 |

Declared mode, where the score carries one [spec: second conditioning input, own fitted strength]:
multiply the declared mode's 12 keys by 1.8 **[prov]** and renormalize (≈ +0.59 ln before
renormalization; the traces use the unrenormalized shift and say so — renormalization moves all
candidates together and cancels in comparisons).

**T1 — pitch emission per sounding pitch class** [spec §3.1; Raphael-Stoddard categories +
Masada-Bunescu covariates [T]; magnitudes [prov], chord:NCT ratio anchored 3–8:1, out-of-collection
anchored to profile tails]. Presence/absence per pc, per segment (duration/repetition weighting
deliberately NOT used — Temperley measured it harmful, F1):

| per-tone category | rel. weight | ln |
|---|---|---|
| chord member (of the state's realized template) | 1.00 | 0 |
| within-collection non-chord tone, covariate-supported (stepwise-approached/left, metrically weak, or tied preparation) | .30 | −1.20 |
| within-collection non-chord tone, unsupported | .12 | −2.12 |
| outside-collection tone, covariate-supported (chromatic neighbor/passing) | .08 | −2.53 |
| outside-collection tone, unsupported | .03 | −3.51 |
| **missing** template tone (per tone) | .45 | −0.80 |
| **missing third** specifically | .35 | −1.05 |

Collection of a key = its signature's diatonic set; for minor, the composite-minor collection (natural
+ raised 6̂/7̂) per the ratified mode decision — the raised degrees are collection members, and they are
CHORD members where the template says so (V's leading tone; the raised-6th chords). An applied-degree
class's template is the applied chord's own tones — an applied chord **legalizes** its chromatic tones
as members [spec §1].

**T2 — spelling emission** [spec §3.2; Temperley TPC +3.6 pp measured [T]; magnitude [prov]]. The one
cell the traces need: a tone **spelled** as candidate minor key k's raised 7̂ (its leading tone —
e.g. A♯ under b minor, C♯ under d minor) contributes ×3.0 [ln +1.10] to k's segment relative to
competing keys where that spelling is a chromatic alteration. The collection question inside this
factor runs through the signature mask (the OI-168 form), no tonic in the membership test [spec].

**T3 — bass factor** [spec §3.3; figured-bass THEORY + Ni's p(bass|chord) [T]; values [prov]].
P(bass = root) .60 [−0.51], third .25 [−1.39], fifth .12 [−2.12], seventh .03 [−3.51]; a bass tone
that is not a chord factor of the state .02 [−3.91]. (Simplification, declared: inversion prevalence is
folded into this table rather than split between the c-state's inversion field and a match test; the
folding is identical across compared hypotheses.)

**T4 — same-key chord transition `P(c_j | c_{j−1}, mode)`** [spec §3.4; Ni key-conditioned form,
Rohrmeier asymmetries [T]; every cell [prov]]. Cells used by the traces (mode-conditioned; no
self-transition — semi-Markov):

| major | p (ln) | minor | p (ln) |
|---|---|---|---|
| V→I .42 (−0.87) | | V→i .40 (−0.92) | |
| ii→V .35 (−1.05) | | iv→V .28 (−1.27) | |
| IV→V .30 (−1.20) | | i→V .15 (−1.90) | |
| ii→I .25 (−1.39) | | i→iv .14 (−1.97) | |
| IV→I, vi→ii .18 (−1.71) | | i→VI .08 (−2.53) | |
| I→V .17 (−1.77) | | V→VI .09 (−2.41) | |
| I→IV .13 (−2.04) | | mid cells V→III .05 (−3.00), III→VII .06 (−2.81), i→x .05–.10 (−3.00…−2.30) | |
| vi→I .10 (−2.30) | | VII→i .15 (−1.90); VII→III .50 (−0.69) | |
| I→ii .09 (−2.41) | | i→iiø6/5 .06 (−2.81) | |
| I→vi .07 (−2.66) | | VI→iiø .20 (−1.61) | |
| viio→I .50 (−0.69) | | i→VII .06 (−2.81) | |
| V→vi .08 (−2.53); V→IV .02 (−3.91) | | V6→viø7 .01 (−4.61); viø7→IV .08 (−2.53); i→IV(raised-6) .02 (−3.91) | |
| x→V/y generic .03–.04 (−3.51…−3.22); V/x→x .65 (−0.43); V/x→(not x) .03 (−3.51); vi→V/vi (retrogression to the dominant of the chord just left) .015 (−4.20) | | rare/absent degree classes (major-key III♯ as a plain degree, minor VII7) .01–.02 (−4.61…−3.91) | |

**T5 — key transition per boundary** [spec §3.5; Noland/Rocher family, relative/parallel own cells
[T]; values [prov]]: stay .96 [−0.04]; change .04 split: relative .012 [−4.42], fifth-related .008
[−4.83], parallel .003 [−5.81], distant .001 [−6.91] per key.

**T6 — entry chord at a key change** [spec §3.6; replaces Raphael-Stoddard uniform [T]; values
[prov]]: I/i .40 [−0.92], V .25 [−1.39], IV/iv .08 [−2.53], viio .06 [−2.81], ii .07 [−2.66],
vi .05 [−3.00], III .04 [−3.22], others pooled.

**T7 — boundary probability per event** [spec §3.7; the Temperley 2009 71.5/22.3/2.4 shape [T]; our
values [prov]]: P(boundary | downbeat) .65 [−0.43; no-boundary −1.05], P(boundary | tactus beat) .25
[−1.39; no-boundary −0.29], P(boundary | sub-tactus) .03. Fermata: P(boundary at fermata end) .95.

**T8 — fermata/cadence location** [spec §3.8; de Clercq [T]]: cadence features at/one-strong-beat
before a fermata gain ×e^{+0.5}; not exercised decisively in these ten cases (no fermata sits at a
traced decision point) — noted, not dropped.

**T9 — cadence features toward key k at a site** [spec §3.9; Bigo feature forms, Feisthauer decay [T];
weights [prov]]: leading-tone resolution (7̂→1̂ of k across the boundary) +0.9; tritone pair (4̂ and 7̂
of k both sounding in the approach) +0.7; dominant-to-tonic bass motion (root of V → root of I, root
positions) +0.7. The features vote for the KEY of the segment at that site, whatever the chord path;
the parallel-major/minor false positive is declared (the features shared by k and its parallel fire
for both; the mode then rides the emission's 3̂) [spec: refinements carried as features].

---

## 2. The five synthetic traces (§6a — hand-computable DP, truncated candidate sets)

Common conventions: events are quarter-note slices; where every compared hypothesis uses the same
segmentation, the T7 terms cancel and are dropped (rule 0.5); bass terms common to all hypotheses are
shown once. Candidate keys are truncated to the declared set; all excluded keys fail on first-event
emission at least as badly as the worst included candidate.

### S1 — plain authentic cadence. VERDICT: fires, commits the obvious (margin 6.8)

Setup: 0-fifths signature, no declared mode, 4/4, four events (one per beat, m1): e1 {C,E,G} bass C ·
e2 {C,F,A} bass F · e3 {G,B,D,F} bass G · e4 {C,E,G} bass C. Candidates: C major, a minor, G major.
One segment per event for all hypotheses (T7 cancels).

**C major** (I → IV → V7 → I): prior −0.97; entry I −0.92; transitions I→IV −2.04, IV→V −1.20,
V→I −0.87; emissions all chord members 0; bass all roots 4 × −0.51 = −2.04; key stays ×3 −0.12;
cadence at e3→e4 toward C: leading-tone B→C +0.9, tritone pair F+B in e3 +0.7, bass G→C +0.7 = +2.3.
**Total −5.86.**

**a minor** (III → VI → VII7 → III — the same music re-labeled): prior −1.31; entry III −3.22;
transitions III→VI −2.30, VI→VII −3.00, VII→III −0.69; emissions 0 (all diatonic to a's collection);
bass −2.04; key stays −0.12; cadence toward a: none fires (no G♯ anywhere). **Total −12.68.**

**G major:** dies at e2 — {C,F,A} contains F♮, outside G's collection; the best G-reading of e2 (c = ii
with F as an unsupported out-of-collection tone and a missing chord tone) costs ≥ −4.3 at that one
event on top of a 1-fifth prior; no later credit recovers it. Excluded from the table by blowout.

Mechanism check ✓: the decode commits I–IV–V7–I in C with a 6.8-nat margin; the a-minor re-labeling
loses on entry + transition economics + the cadence factor's key vote, exactly as intended. Sensitivity:
none — the margin is multi-source and no single provisional cell within its plausible range flips it.

### S2 — relative-pair ambiguity. VERDICT: near-tie until the leading tone, decisive flip at it (0.07 → 6.2)

Setup: 0-fifths signature, seven events: e1 {A,C,E}/A · e2 {D,F,A}/D · e3 {C,E,G}/C · e4 {F,A,C}/F ·
e5 {D,F,A}/D · e6 {E,G♯,B}/E · e7 {A,C,E}/A. No leading tone (G♯) until e6 — diatonic to the signature
throughout before it. Candidates: a minor throughout; C major throughout; C-then-modulate-to-a at e6.

**Cumulative to e5** (prior + entry + transitions + bass ×5; emissions 0 on both — every tone is
diatonic to both readings):
- a minor (i → iv → III → VI → iv): −1.31 −0.92 −1.97 −2.81 −2.30 −2.53 −2.55 = **−14.39**
- C major (vi → ii → I → IV → ii): −0.97 −3.00 −1.71 −1.39 −2.04 −2.66 −2.55 = **−14.32**

**The posterior before the leading tone is a 0.07-nat near-tie — the published posterior split, which
is the designed behavior: the prior and cadence factors must resolve the pair exactly when the leading
tone appears, not before.** ✓

**e6–e7:**
- a minor (iv→V −1.27; V→i −0.92; bass −1.02; G♯ = chord member of V AND spelled leading tone of a:
  T2 +1.10; cadence toward a at e6→e7: +0.9 +0.7 +0.7 = +2.3): −14.39 −1.27 −0.92 −1.02 +1.10 +2.30 =
  **−14.20**
- C major (the only legal C-reading of {E,G♯,B} is the applied class V/vi — the applied template
  legalizes G♯ as a member; ii→V/vi −4.61; V/vi→vi −0.43; bass −1.02; no key vote for C): −14.32
  −4.61 −0.43 −1.02 = **−20.38**
- C-then-modulate (key change to a at e6: relative −4.42, entry V −1.39; then V→i −0.92, bass −1.02,
  +1.10 +2.30): −14.32 −4.42 −1.39 −0.92 −1.02 +1.10 +2.30 = **−18.67**

**a-minor-throughout wins by 6.2 nats, and the single-key reading beats the mid-phrase modulation** —
the Viterbi path revises the WHOLE prefix retroactively when the leading tone lands (the #12 payoff:
no early commitment ever happened). Mechanism ✓. Note for the record: the C-path's failure is carried
by the applied-class transition economics (ii→V/vi retrogression) plus the spelling and cadence votes —
membership alone could never separate the pair (all sets diatonic to both keys until e6).

### S3 — Dorian-notated opening. VERDICT: content overwhelms the weak prior (margin ≈ 8–12); prior variant question SETTLED: initial-state-only

Setup: 0-flat signature (the Dorian convention — the true key one flat short), four events:
e1 {D,F,A}/D · e2 {G,B♭,D}/G · e3 {A,C♯,E,G}/A · e4 {D,F,A}/D. Candidates: d minor (true), a minor
(the signature's minor), C major (the signature's major), F major (1 fifth flat, the other neighbor).

- **d minor** (i → iv → V7 → i; B♭ = iv's third, a collection member in composite minor; C♯ = raised
  7̂, member of V): prior (1-fifth minor) −3.00; entry i −0.92; transitions −1.97 −1.27 −0.92; bass
  −2.04; T2 spelling C♯-as-leading-tone +1.10; cadence toward d at e3→e4 (+0.9 +0.7 tritone G+C♯ +0.7
  bass A→D) +2.3. **Total −6.72.**
- **a minor:** prior −1.31, but e2's B♭ is outside a's collection (a's composite raises F/G, it does
  not flatten B) — best reading costs ≥ −4.3 at e2 alone (out-of-collection tone + missing member +
  non-factor bass), plus e3 needs V/iv; the path lands ≈ −18 to −19. Blowout; excluded from contention.
- **C major:** prior −0.97, same B♭ wreck at e2 plus C♯ wreck at e3 ≈ −19+. Excluded.
- **F major** (vi → ii → V/vi → vi — B♭ IS F's collection; C♯ legalized only as the applied V/vi):
  prior −3.00; entry vi −3.00; transitions vi→ii −1.71, ii→V/vi −4.61, V/vi→vi −0.43; bass −2.04; no
  spelling credit (C♯ votes d, not F); no cadence vote for F. **Total −14.79.**

**d minor wins by 8.1 nats over the nearest survivor.** The 1.7-nat prior tax (fifth-away minor vs the
signature's own minor) is overwhelmed by ONE B♭ and one C♯ — "the prior's fifth-away mass must behave"
✓. Declared-mode variant: with `<mode>minor</mode>`, T0's minor column gains ≈ +0.59 for d (and a) —
direction right, magnitude small, verdict unchanged.

**The §5a open question (initial-only vs persistent pull), settled by this trace:** a persistent
per-segment prior would tax every d-minor segment −3.00 against the signature keys' −0.97/−1.31 —
a linearly growing penalty (≈ 1.7–2.0 nats per segment) with no theory basis (F2: the literature has
no signature prior at all), which in accidental-free stretches actively re-introduces the
signature-pull bias the OI-174 measurement condemned, in soft form. The initial-state-only variant
pays the tax once and lets content govern thereafter; a mid-piece signature CHANGE re-anchors it
(the ratified OI-94(a) discharge) — re-anchoring is the one legitimate "persistent" moment because it
is new notated evidence. **Proposed for ratification: T0 conditions the initial key state only, and
re-enters only at a notated signature change.**

### S4 — tonicization (V/V → V). VERDICT: applied class wins on transition economics (margin 6.7)

Setup: C major established, four events: e1 {C,E,G}/C · e2 {D,F♯,A,C}/D · e3 {G,B,D}/G · e4 {C,E,G}/C.
Candidates: stay in C with the applied class (I → V/V → V → I) vs modulate (C: I | G: V7 → I | C: I).

- **Stay C:** prior −0.97; entry −0.92; I→V/V −3.22; V/V→V −0.43; V→I −0.87; bass −2.04; F♯ is a
  member of the applied template (0); cadence toward C at e3→e4: +0.9 (B→C) +0.7 (bass G→C) — the
  tritone-pair feature does NOT fire (4̂ = F♮ absent from the approach; e2 carries F♯) = +1.6.
  **Total −6.85.**
- **Modulate:** prior −0.97; entry −0.92; key change C→G (fifth) −4.83 + entry V −1.39; V→I −0.87;
  key change back G→C −4.83 + entry I −0.92; bass −2.04; cadence toward G at e2→e3 (+0.9 F♯→G, +0.7
  bass D→G) +1.6 and toward C at e3→e4 +1.6. **Total −13.57.**

**The applied-degree reading wins by 6.7 nats — by the two key-change costs, i.e. by transition
economics, not by fiat** ✓ (the ratified tonicization decision). Sensitivity: the verdict stands even
with free entry tables; it needs only P(key change) ≪ P(applied cell), which any fitted modulation
rate delivers.

### S5 — deceptive cadence (V7 → vi). VERDICT: stays in key (margin 4.9)

Setup: C major, two events: e1 {G,B,D,F}/G · e2 {A,C,E}/A. Candidates: C major (V7→vi); a minor
(VII7→i); modulate-to-a.

- **C major:** prior −0.97; entry V −1.39; V→vi −2.53; bass −1.02; cadence toward C: leading-tone
  B→C fires (C sounds in e2 as the third of vi) +0.9, tritone F+B +0.7; the bass-fifth feature does
  NOT fire (G→A) = +1.6. **Total −4.31.**
- **a minor:** prior −1.31; entry VII7 (a rare class) −3.91; VII7→i −3.00; bass −1.02; no cadence vote
  for a (no G♯). **Total −9.24.** Modulation variants add key-change cost on top; excluded.

**V7→vi in C wins by 4.9 nats.** Mechanism ✓: the deceptive resolution is carried by the asymmetric
transition table (V→vi .08 ≫ V→IV .02, the Rohrmeier asymmetry) — a symmetric or rule-based table
would have no cell for it and would push the decode toward a false reading. Sensitivity: the verdict
needs P(vi | V) to be a real cell of fitted mass, which the corpus statistics establish (F5); within
any plausible fitted range the verdict stands. Note: the cadence factor's +1.6 toward C at a deceptive
cadence is CORRECT behavior — the features vote for the key (the deception is in-key), illustrating why
they are key-evidence, not chord-evidence.

---

## 3. The five corpus traces (§6b — the #17c form on verified cases)

### C1 — `bwv145.5@12960` (Jazz; the OI-168 flip). VERDICT: comes out right WITHOUT the special form — twice over

**Verified facts (sources: `cc_oi168_fix_report.md` §2; `tools/corpus/jazz/bwv145.5.ours.json` regions
@12480/@12960/@13920; WiR `Chorales/017/analysis.txt` m9–m10 read through the OI-142 offset +2;
`tools/robust_stop/corpus_transposition_offsets.json`).** 3/4, no anacrusis; tick 12960 = m10 b1 ✓.
Our frame (= WiR +2): GT m9 ends `… A: V6 V6/5 I, E: IV`; GT m10 = `V6 · V6/5 · I` **in E major** — the
chord at 12960 is B major in first inversion, root pc 11, exactly the sounding, notated
D♯3(bass)·F♯3·B4 (tpc 23/20/19), joined at b2 by A♮ (the seventh: B7/D♯; region pcs {D♯,F♯,A,B} =
mask 2632 ✓). Our system emits local key `D#alt` (the OI-174 defect class) and, post-OI-168-fix, chord
`B/Eb`. The trace must produce (E major, V6) with no signature-mask special form in the chord factor.

**Events:** e0 = m9 b3 {A,C♯,E}/A (the A-major pivot chord) · e1 = m10 b1 {D♯,F♯,B}/D♯ ·
e2 = m10 b2 {D♯,F♯,A,B}/D♯ · e3 = m10 b3 {E,…}/E. **Candidates:** E major (GT); f♯ minor (our
key-layer's runner-up, conf .15); d♯ minor (the nearest two-mode state to the emitted `D#alt`); stay-A.
Common origin: the A-major context at e0 (shared prefix dropped). e1+e2 are one V-of-E segment
(V6 → V6/5 = same root; the same-root coalescing the fix report confirmed at this very spot).

| path | terms | total |
|---|---|---|
| **E major** (change at e1; A-chord stays A: I) | key change A→E (fifth) −4.83 · entry V −1.39 · bass D♯ = third −1.39 · spelling D♯-as-leading-tone-of-E +1.10 · V→I −0.87 · cadence toward E at e2→e3: +0.9 (D♯→E) +0.7 (tritone A+D♯ both sound in e2) = +1.6 | **−5.78** |
| E major (pivot variant: change at e0, A-chord = E: IV — the GT reading) | −4.83 · entry IV −2.53 · IV→V −1.20 · bass −1.39 · +1.10 · −0.87 · +1.6 | −8.12 |
| f♯ minor | key change A→f♯ (relative) −4.42 · entry IV(raised-6 class) −2.53 · bass −1.39 · IV→VII −2.81 · no spelling credit (D♯ is E's leading tone, not f♯'s) · no cadence (no E♯ anywhere) | **−11.15** |
| d♯ minor | key change A→d♯ (distant) −6.91 · entry VI −3.00 · bass −1.39 · e2: A♮ is OUTSIDE d♯'s collection (d♯ has A♯) −3.51 · VI→♭II −4.61 (e3's E-major chord is at best a Neapolitan in d♯) | **−19.42** |

**E major wins by 5.4 nats over the nearest rival.** The two E-variants differ only in where the pivot
boundary label sits (both commit (E, V) at e1 — the P5 pivot ambiguity, noted); the claim tested is the
e1 state, and every candidate agrees except the losers. **The OI-168 shadow, checked inside d♯
itself:** the old `Ebm` reading = (d♯, i): members D♯, F♯; missing fifth A♯ −0.80; B an unsupported
in-collection NCT −2.12; bass root −0.51 → **−3.43**; the (d♯, VI6) reading: all members, bass third
−1.39 → **−1.39**. The emission factor alone rejects the chord the notes do not contain by 2.0 nats
even under the wrong key — **the joint structure needs no collection-through-tonic special form to
reproduce the OI-168 correction, and the key economics never reach d♯ in the first place.** ✓
(The spelling factor's collection question still runs through the signature mask — that is a different
factor and unchanged, per §5a.)

### C2 — `bwv352@1440` (share-tone Am6 vs F♯ø7). VERDICT: honest near-tie, decided by the bass note — the correct epistemic output

**Verified facts (sources: `cc_uncertain_resolver_measurement_report.md` (the share-tone finding);
WiR `Chorales/037/analysis.txt` m1–m2; `tools/corpus/baroque/bwv352.ours.json` region @1440).**
A minor, 4/4, no anacrusis; tick 1440 = m1 b4. GT: m1 `i · i · V6 · vi/o7`, m2 `IV6 b1.5 viio b2 i …` —
the chord at b4 is **F♯ø7** (F♯-A-C-E; the raised-6th half-diminished class, root pc 6), resolving to
IV6 (D/F♯, raised-6th class). Ours commits Am6 (root 9); the committed alternatives carry exactly the
pair: `Am6/F♯ 2.7875` vs `F#m7b5 2.775` — margin 0.0125. The region (1440–2640, an over-grab into m2)
sounds {C,E,F♯,A}+G♯-tail; at b4 itself the pc set is {C,E,F♯,A}. The bass AT b4 is not settled by our
region data (the region's bass field is E with F♯ present at low weight; the kern source would settle
it; the BCMH `original_KernScores` copy named in OI-179 is not currently on disk — declared open,
traced both ways). Key: a minor throughout (both readings agree; the key axis is not in question).

**Candidates (chord axis, one segment, incoming = V6, outgoing = IV6):**
R1 = (a, viø7): all four tones chord members. R2 = (a, i) with F♯ as a covariate-supported
in-collection NCT (composite minor's raised 6̂). *(There is no "i(add6)" class — the ground-truth-derived
degree vocabulary contains no added-sixth degree for this repertoire, so the old committed reading is
not even expressible; its nearest legal form IS R2.)*

| | R1 (viø7) | R2 (i + NCT) |
|---|---|---|
| emission | 0 | −1.20 (F♯) |
| bass **if F♯** | root −0.51 | non-factor −3.91 |
| bass **if E** | seventh −3.51 | fifth −2.12 |
| incoming V6→c | V6→viø7 −4.61 | V→i −0.92 |
| outgoing c→IV6(raised) | viø7→IV −2.53 | i→IV −3.91 |
| **total if bass F♯** | **−7.65** | −9.94 |
| **total if bass E** | −10.65 | **−8.15** |

**The verdict flips on the bass note (±2.3/2.5 nats), and three of the deciding cells (V6→viø7,
viø7→IV, i→IV-raised) are rare-class transitions whose fitted values will sit at or below the OI-177
pooling threshold.** This is the honest and CORRECT output for the one case the whole architecture
history classifies as genuinely function-only pc-identical ambiguity: the joint model does not
manufacture certainty here — it publishes a posterior split (both readings within ~2.5 nats under
either bass), with the bass datum the decisive evidence. No structural defect; two records: (a) verify
the b4 bass at the kern source when the BCMH/kern copy is next on disk; (b) the rare-cell pooling
decision (OI-177) governs this case's fitted behavior — carried to the findings.

### C3 — `bwv10.7@36000` (segmentation over-grab). VERDICT: ★ SURPRISE — the spec under-specifies per-segment vs per-event factor granularity, and this case turns on it

**Verified facts (sources: WiR `Chorales/358/analysis.txt` m19–m20; `tools/corpus/baroque/
bwv10.7.ours.json` regions @35520/@36000/@36960; `cc_eg2_probe_report.md` §2.5).** G minor, 4/4, no
anacrusis; tick 36000 = m19 b4 ✓. GT: m19 `V2/iv · iv6 · V4/3/iv`, m20 `iv · iv6` — at 36000 the GT
chord is **V4/3/iv** (the applied G7 to C minor, bass D = the 4/3 figure's fifth, root pc 7), at 36480
(m20 b1) **iv** (C minor). The sounding pcs across 36000–36960 are {C,D,E♭,F,G} (mask 173 —
**E♭, settling the source discrepancy: CLAUDE.md block (D) is right; the "C-D-E-F-G" in
`cc_uncertain_resolver_measurement_report.md` is a transcription slip, see finding §4.6**). Notably NO
B♮ sounds — the applied dominant is an incomplete seventh (D-F-G, no third). Our current system commits
one merged region 36000–36960 as `Bb/C "VII"` under a `Charm` local key — a root (B♭) that does not
sound at all.

**Events:** e1 = 36000–36480 {D,F,G}/D (tactus beat 4) · e2 = 36480–36960 {C,E♭,G}/C (downbeat).
Incoming: the iv6 segment (GT m19 b3; ours agrees — `Cm/Eb i6` under its key). Key: g minor throughout
(shared). **Hypotheses:** H-split (GT): … iv6 | V4/3/iv | iv. H-merge: … iv6 | one merged segment, best
read as iv with D and F as covariate-supported passing tones.

Bookkeeping as the ratified score form literally reads (emission per tone; bass, missing-tone, and
transition per SEGMENT; boundary per event):

| | H-split | H-merge |
|---|---|---|
| transitions | iv→V/iv −3.51 · V/iv→iv −0.43 | iv6→iv is a SELF-transition — the merge-family's true best form is one long iv segment; it pays no transition |
| emission | missing third B♮ −1.05 | D −1.20 · F −1.20 |
| bass (per segment) | e1: D = fifth −2.12 · e2: C = root −0.51 (+ iv6's E♭ third −1.39 on the incoming segment, same in both) | ONE factor: C = root −0.51 |
| boundary terms (both events, both hypotheses) | bound@36000 (tactus) −1.39 · bound@36480 (downbeat) −0.43 | no-bound@36000 −0.29 · no-bound@36480 −1.05 |
| **total** | **−10.83** | **−4.25** |

*(The iv6 segment's bass term −1.39 appears only on the split side deliberately — under per-segment
bookkeeping the merge absorbs that span into ONE segment paying ONE bass factor; that asymmetry IS the
length bias being demonstrated.)*

**The merge WINS by ~6.6 nats under the per-segment reading — against the ground truth.** Diagnosis (the
stage doing its job): the advantage is mostly an artifact of per-SEGMENT factors — a longer segment pays
the bass factor and the missing-tone penalty ONCE where the split pays them per segment, so merging
harvests factor-instance discounts unrelated to musical content (the classic semi-Markov length-bias).
Re-computed with the bass factor evaluated PER EVENT (each event's sounding bass against the segment's
chord — which is exactly Ni's published per-frame form, F9): H-merge pays e1's D-against-iv as a
non-factor bass −3.91 and the totals become **H-split −10.83 vs H-merge −9.55** — still merge-leaning
by 1.3 nats, the remainder carried by the missing-B♮ penalty (−1.05) and the weak-beat boundary cost
(−1.39): an incomplete applied seventh entered on a weak beat is expensive under the provisional
values. Whether a FITTED missing-third penalty (Bach's passing-beat incomplete dominants are common)
and fitted boundary values flip it is a values question — but the granularity question is STRUCTURAL:
**the ratified §2 score form does not say which factors are per-segment and which per-event, and the
answer decides this case.** Carried to §4.1/§7 as the desk simulation's one structural finding, with
the proposed amendment (bass per event, per Ni's form; missing-tone penalty normalized per event of
segment length; emission already per tone). Note the floor: even at its worst, the new structure's
merge reading is (g, iv) root C — the current system's committed B♭ root is impossible (B♭ never
sounds; any B♭-rooted template pays a missing root plus non-member penalties ≥ 5 nats).

### C4 — `bwv110.7@2880` (relative major/minor, the key-LOCAL residual). VERDICT: flips to b minor by 5.1 — by exactly the three mechanisms the design predicts

**Verified facts (sources: `tools/reports/key_mode_inference_diagnosis.json` relative_key run
{bwv110.7, 2880, dur 2400, our Dmaj, GT b/b}; WiR `Chorales/055/analysis.txt` m0–m3;
`tools/corpus/baroque/bwv110.7.ours.json` regions @2400–@5280).** B minor, 4/4, one-quarter anacrusis
(WiR `m0 b4`; our tick 0 = that pickup ✓ first region m0). GT reads the passage after the D-major
cadence as `b: i · V · V | i …`; our system reads D major throughout (`vi · III · I · V · vi · V`),
confidence ~0.18–0.27, run enumerated in the committed diagnosis artifact. The A♯s are notated (tpc 24
in the region tones — verified). *(A one-beat GT-vs-tick alignment question in this piece is noted in
§4.5 — it does not affect this trace, which aligns by chord content: the six verified regions
Bm → F♯[+E] → D[+B,A] → A → Bm → F♯.)*

**Segments (verified tones):** s1 Bm{B,D,F♯}/B · s2 F♯{F♯,A♯,C♯}+E/F♯ · s3 D{D,F♯}+B,A/D ·
s4 A{A,C♯,E}/A · s5 Bm/B · s6 F♯[+A♯]/F♯. Common origin: the (D, I) cadence before s1. Candidates:
D-major-throughout (ours) vs change-to-b-at-s1 (GT). E in s2 is a chord MEMBER both ways (the seventh
of F♯7); B and A in s3 are covariate-supported NCTs both ways (−2.40 shared, shown for completeness);
bass factors are roots in both (−3.06 shared).

| path | terms | total |
|---|---|---|
| **D major** (vi → V/vi → I → V → vi → V/vi — the F♯-major chord has NO plain-degree reading in the major vocabulary; its only legal form is the applied V/vi) | I→vi −2.66 · vi→V/vi −4.20 · V/vi→I (an applied dominant abandoning its target) −3.51 · I→V −1.77 · V→vi −2.53 · vi→V/vi −4.20 · NCTs −2.40 · bass −3.06 · key stays −0.20 · no spelling credit, no cadence vote | **−24.53** |
| **b minor** (key change at s1; i → V7 → III → VII → i → V) | change D→b (relative) −4.42 · entry i −0.92 · i→V −1.90 · V→III −3.00 · III→VII −2.81 · VII→i −1.90 · i→V −1.90 · NCTs −2.40 · bass −3.06 · stays −0.20 · spelling: A♯-as-leading-tone-of-b ×2 +2.20 · cadence: A♯→B resolution at s2→s3 +0.90 | **−19.41** |

**b minor wins by 5.1 nats.** The three carrying mechanisms are exactly the designed ones: (1) the
degree-valued vocabulary makes the F♯-major chord STRUCTURALLY expensive in D (repeated
retrogression-to-applied cells, −4.20 each) while it is the plain V of b; (2) the spelling emission
reads the notated A♯ as b's leading tone (+1.10 per occurrence — the F3 clue our current key layer is
blind to); (3) the cadence factor votes b at the resolution. This is the key-LOCAL residual class the
architecture was decided FOR (the D-major over-pull + hysteresis mechanism named in
`cc_key_mode_inference_diagnosis_report.md` §1 case 4 has no analogue here — there is no hysteresis
term to be sticky). Sensitivity: the two retrogression cells are provisional, but the margin is
multi-source (economics + spelling + cadence each ≥ 1.5 nats); no single cell within plausible range
flips it.

### C5 — `bwv254` (genuinely modal: Dorian-notated, declared mode, d/F oscillation). VERDICT: reproduces the analyst's own dual reading; the declared-mode input does visible, correctly-sized work

**Verified facts (sources: WiR `Chorales/186/analysis.txt` (header "key signature blank"; opening
`m0 b4 d: i F: vi`; first phrase cadencing `F: … V7 I` at m3; d-minor cadences m6–m7, m10–11);
`tools/corpus/baroque/bwv254.ours.json` regions @0/@960/@1440; CLAUDE.md Stage-4a record: bwv254
carries `<fifths>0</fifths><mode>minor</mode>` — the declared-mode anchor is present in OUR score).**
0-flat signature; GT opens with the very double-reading this factor structure models: the pickup Dm is
`d: i` re-read `F: vi`. Verified events: e0 pickup {D,F,A}/D · e1 {F,A,C}/A (F/A) · e2 {G,B♭,D,F}/B♭
(the B♭ arrives in m1) · e3 the F-cadence dominant {C,E,G(,B♭)}/C · e4 {F,A,C}/F.

**Candidates:** F-throughout; d-then-F (the GT reading: pickup in d, F from e1); a minor; C major
(the signature pair).

- **a minor and C major die at e2** (B♭ outside both collections; a second wreck at e3's E♮ for a
  minor) — the signature's own pair is eliminated by the second measure, exactly the Dorian-notation
  phenomenon. ✓
- **F-throughout:** prior (1-fifth major) −3.00 · entry vi −3.00 · vi→I −2.30 · I→ii −2.41 · ii→V
  −1.05 · V→I −0.87 · cadence toward F at e3→e4 (+0.9 E→F, +0.7 tritone B♭+E, +0.7 bass C→F) +2.30 =
  **−10.33**
- **d-then-F:** prior d (1-fifth minor) −3.00 · entry i −0.92 · key change d→F (relative) at e1 −4.42 ·
  entry I −0.92 · I→ii −2.41 · ii→V −1.05 · V→I −0.87 · +2.30 = **−11.29**

**F-throughout leads by 0.96 nats — a near-tie that mirrors the ground truth's own double label.**
With the declared mode applied (T0 minor ×1.8: d gains +0.59), d-then-F closes to **0.37 nats** —
the declared-mode input moves the posterior visibly, in the right direction, and does NOT overwhelm
content (the ratified "weak prior" intent, quantified on a real case). Over the whole piece the d
reading additionally collects the m6/m7/m10–11 d-cadence evidence (leading-tone C♯ + cadence factors)
that this opening-window trace does not reach — consistent with GT's global d. The emission-variant
half (the composite-minor collection absorbing the B♭/B♮ traffic without a mode-state change) is
exercised structurally here (B♭ as a full member of d's iv while the piece is notated 0-flat);
persistent-vs-initial is settled at S3 and C5 concurs: a persistent 0-flat prior would tax every
d-segment of this genuinely modal piece forever, for nothing.

---

## 4. Findings register (surprises recorded, diagnosed, with proposed dispositions)

**4.1 ★ THE ONE STRUCTURAL FINDING (C3) — factor granularity is under-specified in the ratified
score form.** `cowork_joint_estimator_factorization.md` §2 writes each factor as a per-segment term
(`Σ_j …`) but does not state which factors are evaluated once per segment and which per event within
the segment. The choice is load-bearing: per-segment bass and missing-tone terms give longer segments a
factor-instance discount (the semi-Markov length bias), and on `bwv10.7@36000` that bookkeeping alone
decides merge-vs-split by ~6.6 nats against the ground truth. **Proposed specification amendment (a #17e
sharpening within the ratified structure, brought for ratification per #13/#22):** (a) the pitch
emission is per tone (already the ratified text); (b) the BASS factor is evaluated per event — each
event's sounding bass against the segment's chord — which is Ni's published per-frame form (F9), not a
new invention; (c) the missing-tone penalty is normalized per event of segment length (a segment
missing its third pays in proportion to how long it fails to sound it); (d) transition, entry, and
key-change factors remain per boundary (correct as written). A bookkeeping subtlety found while
tracing, recorded for the amendment text: T3's simplification here folded inversion into the bass
factor; under the ratified state (inversion a state field), successive same-degree different-inversion
labels (iv6→iv) are legal state transitions, which slightly reprices the merge family but does not
remove the length bias. With (b) applied the C3 gap closes to 1.3 nats (merge-leaning), the remainder
riding two fittable values (the incomplete-seventh penalty; the weak-beat boundary cost) — a values
question the fit settles, not a structure question.

**4.2 The §5a open question SETTLED by trace (S3, concurred by C5): the signature/declared-mode prior
conditions the INITIAL key state only,** re-entering only at a notated mid-piece signature change (the
OI-94(a) discharge moment). The persistent-pull variant imposes a linearly growing tax on
away-from-signature keys with no theory basis (F2: the literature has no signature prior at all) and
softly re-introduces the OI-174 signature-pull bias in exactly the accidental-free stretches where the
prior should be silent. Brought for ratification as the §7 record; the factorization doc §7 already
names this as settled-by-desk-sim.

**4.3 Sensitive-cell record (feeds OI-177, the capacity/pooling gate).** Cells the traces show
verdict-adjacent, where pooling/threshold decisions must be made deliberately: the rare-class
transitions V6→viø7 / viø7→IV / i→IV-raised (C2 — the whole case moves ±2.5 nats on them); the
applied-class retrogression cells vi→V/vi, V/x→(not x) (S2, C4 — they carry the discriminative load the
membership test cannot); V→vi (S5 — the deceptive cadence needs its real fitted mass); the
incomplete-seventh missing-third penalty and the tactus-beat boundary probability (C3 — the remaining
1.3-nat gap). The applied-class economics carrying discriminative load also means premise P2
(first-order transitions) is under real load at exactly these cells — its ledger row's false-negative
path (transition-table residual) should be watched at these cells first.

**4.4 `bwv352` m1 b4 bass verification item.** The C2 verdict flips on whether the b4 bass is F♯ or E;
our over-grabbed region does not settle it; the GT's root-position label implies F♯. Verify at the kern
source when the BCMH/kern copy (OI-179's `tools/BCMH_dataset/`, currently not on disk) is next
available — a one-note read.

**4.5 `bwv110.7` beat-alignment question (measurement layer, not model).** Hand-mapping WiR beats to
our ticks with the verified anacrusis (our m0 = WiR `m0 b4`) leaves the GT chord stream reading one
beat later than our verified region contents across m2–m3 (e.g. our Bm at m2 b1 vs GT's `b: i` at m2
b2), while the chord-content pairing is exact and unambiguous. Whether this is a WiR beat-numbering
convention around anacrusis, a local GT misalignment (the known `bwv245.40`/`bwv429` class), or an
error in my hand mapping is NOT settled here — the C4 trace aligns by chord content and is unaffected.
Flag for a register row at the next measurement-layer touch: the alignment convention for
anacrusis-bearing WiR pieces should be positively established (#19) before per-beat fitting counts are
drawn from them.

**4.6 Erratum found in a committed report (doc-sync, historical).**
`cc_uncertain_resolver_measurement_report.md` (2026-06-24) twice describes the `bwv10.7@36000`
over-grab as "a 5-note C-D-E-F-G scale"; the committed data (`bwv10.7.ours.json` @36000,
`pitchClassSet: 173` = {C,D,E♭,F,G}) and CLAUDE.md block (D) have **E♭**. No live surface carries the
wrong value (CLAUDE.md is correct); the report is a frozen historical record. Disposition proposed:
an erratum line in the report (or a register note), at the user's call — not silently edited here.
*[Disposition settled 2026-07-19 at CC's commit-time stop: the report turned out to be UNTRACKED
(`/cc_*.md` ignore policy, never committed) — user's call: it stays untracked; THIS section is the
tracked erratum record, and CC's dated note on the report's on-disk copy stays as an uncommitted
courtesy annotation.]*

**4.7 What did NOT surprise (the positive record).** C1: the degree-valued chord state + plain emission
reproduce the OI-168 correction with no signature-mask special form in the chord factor, and the wrong
key never enters the beam — the two defect classes (OI-168's δ, OI-174's exotic emission) are
structurally unreachable in the ratified state space. S2/C4: the relative-pair mechanism works
end-to-end (near-tie until evidence, then a retroactive whole-prefix flip — the #12 payoff made
concrete). S4: tonicization resolves by transition economics as ratified. C2: the genuinely ambiguous
share-tone case yields a published near-tie posterior instead of manufactured certainty — the correct
epistemic output. C5: the model reproduces the GT analyst's own dual reading within 1 nat, and the
declared-mode input is visible and correctly weak (+0.59, closing the gap to 0.37).

## 5. OI-181 discharge

The two declared forms were used as specified in the factorization doc §6: (a) five synthetic cases
with hand-computable DP arithmetic over truncated, declared candidate sets; (b) five single-piece
corpus traces in the #17c order (mechanism-fires-first, then magnitudes), every corpus fact verified
at a cited committed source this session. OI-181's condition — "declare the small-instance form before
the funnel's desk-sim stage runs" — was met by the ratified §6 itself; this document is that stage run.
Row disposition: OI-181 closes when this document is ratified and committed.

## 6. Self-check (the standing after-every-exercise rule, applied to this document)

Diff re-read in full before delivery. Checks: no `src/`, golden, corpus, or baseline file touched
(paper only — the funnel stays shut ✓ #8); every corpus fact carries a named committed source read this
session (✓ the verify-at-source rule; nothing from memory — the one memory-risk item found and
corrected during work: an early bash `ls`/`grep` on the live tree violated the never-bash rule, was
stopped, and all facts were re-taken through the file tools); provisional values are labeled [prov]
everywhere and no verdict within a provisional cell's plausible range is reported as a win (rule 0.1
✓ against DT-2's spirit — no value here becomes an instrument); the C3 surprise is surfaced as a STOP
item for ratification, not built around (✓ #13, DT-26's lesson of declaring scope); no self-invented
labels (table/case names are positional T0–T9/S1–S5/C1–C5 within this document only; every repository
concept uses its existing name); the two hypotheses-of-record (per-event bass, initial-only prior) are
proposed, not adopted (✓ #14 — nothing here changes behavior). Known-problem-types pass: DT-11
(hand-transcribed numbers) — the trace figures are declared hand values, not measurements, and are
labeled as such at rule 0.3; DT-9 (proxy substitution) — the folded-inversion bass simplification is
declared at T3 and its interaction with C3 recorded at §4.1; DT-10 (insulation claims) — C1's
"structurally unreachable" claims are grounded in the state-space definition, with the spelling-mask
exception explicitly carried.

## 7. What ratification is asked for

1. **The verdict:** the ratified factorization passes nine of ten traces as specified; no finding
   requires re-ratifying the STRUCTURE (variables, factors, decode).
2. **The §4.1 specification amendment** (factor granularity: bass per event per Ni's form;
   missing-tone penalty per event of segment length; emission per tone; boundary-family factors per
   boundary) — an amendment to the ratified `cowork_joint_estimator_factorization.md` §2/§3, so it
   needs your ratification before the spec is edited (#14/#22).
3. **The §4.2 record:** the signature/declared-mode prior is initial-state-only, re-anchored at a
   notated signature change — closing the question the factorization doc §7 left to this stage.
4. **The findings dispositions:** §4.3 rides OI-177 (no action now); §4.4 and §4.5 become register
   rows at the next commit (measurement-layer, low); §4.6 erratum handling at your call.
5. **Row closures on commit:** OI-181 (discharged, §5).

After ratification, the funnel's next stage per the handoff: the pre-fit gates — OI-176 (held-out
split), OI-177 (capacity budget), OI-178 (robust-stop adoption protocol), OI-180 (dual-path sanction +
retirement map) — Cowork-drafted for your ratification. No build before those.




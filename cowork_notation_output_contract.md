# The notation output-surface contract — the A-native record (★ USER-RATIFIED 2026-07-26)

**★ RATIFIED BY THE USER 2026-07-26, as asked in §8 — as specified, no amendments.** The build
dispatches open under the OI-180 sanction pattern; the first is the table codegen
(`cc_instruction_joint_table_codegen.md`, Decision D1 executed).

**Author:** Cowork, 2026-07-26, at the user's "go" after the P1 pedal ruling. **Status:
ratified.** This is the contract-drafting step of
the ratified `cowork_notation_adoption_increment.md` (§8 plan, after the §8.1 audit): it defines
WHAT the joint estimator publishes for the in-app notation path and how every audited consumed
fact maps onto it. It is a specification, not a build; the build dispatches follow under the
OI-180 sanction pattern.

**Governing inputs (all ratified):** Decisions A2 / B-full(OI-193) / C1 / D1 / E(OI-194) and the
§10 pedal ruling (`cowork_notation_adoption_increment.md`); the factorization's decode plan (§5)
and mode/emission decisions (§5a-1/4); the decision-neutrality corollary (CLAUDE.md). **The
exhaustiveness basis (#12/#15):** the consumption audit — 75 consumed-field rows at
`tools/audit/notation_surface/consumption_fields.csv` (commit `21422ee77d`); every row's
disposition appears in §4 below by cluster, none silently dropped.

**Terms, defined at first use.** *The record* — the data the joint module publishes per analyzed
score span; the one output surface the notation path reads (Decision A2). *Segment* — the joint
decode's unit: a contiguous span carrying one (key, chord-class) state. *Posterior* — the decode
lattice's probability mass over alternative readings (OI-193). *Content-score gap* — the
established local uncertainty quantity: the log-score difference from re-scoring a committed
span under an alternative reading (the Python probe's published slice). *Marginal mass* — the
full-lattice posterior probability of a reading (forward-backward; OI-193's completion). *Key
run* — a maximal run of consecutive segments sharing one key. *Modal reading* — the ratified
un-rounded publication of modal color (§3.4). *Ornament labels* — the ratified post-decode
non-chord-tone labels (OI-194), including the voice-independent pedal-point class (§10 ruling).

---

## 1. The two seams (both audited; both read THIS record)

1. **The span seam** (today `analyzeHarmonicRhythm` → `HarmonicRegion` vector): the caller names
   a score span; the record for that span is returned. Consumers: the section layer
   (`sectionanalyzer`/`sectioncadencedetection`), the composing bridge (annotations, status
   bar), the implode bridge (chord track), the tuning bridge.
2. **The note seam** (today `analyzeNoteHarmonicContext[Details]` → `NoteHarmonicContext`): the
   caller names a note/tick; the answer is a VIEW query over the same record — the containing
   segment, its key, its committed chord, its ranked alternatives, its uncertainty fields — plus
   the derived display facts. No second computation exists (#6): the note seam is a lookup into
   the span seam's record. Consumers: `notationinteraction` (writes Harmony elements),
   `notationcontextmenumodel` (right-click menu), the tuning bridge's single-note path, the
   status-bar/accessibility formatter chain.

`ChordAnalysisResult`, `NoteHarmonicContext`, and `HarmonicRegion` retire from the notation path
with the legacy analysis (Decision A2; the retirement executes at the map, the switch merely
stops producing them).

## 2. Provenance on the surface (#16/#19)

Every published record carries its instrument provenance: the embedded table set's source-artifact
hashes and the selected weight-vector identity (both compiled in per Decision D1), plus the
decoder's version. A consumer — and any future measurement — can always answer "which fitted
values produced this analysis" from the record itself; a provenance-less analysis cannot exist.

## 3. The record's fields

### 3.1 Per piece/span

- The analyzed span (ticks), the notated initial signature fifths and declared mode as READ
  (input echo — the prior's inputs, OI-94(a) re-anchor points included when a mid-piece notated
  signature change exists), and the §2 provenance block.

### 3.2 Per segment (the committed reading — all native decode facts)

- Span: `startTick`, `endTick`.
- Key: `tonicPc`, `isMajor`; DERIVED: the key's signature-fifths value (the deterministic
  (tonic, mode)→fifths mapping — the audit's `keySignatureFifths` consumers' source).
- Chord class: `degree` (scale-degree base), `quality` (the class's quality), `inversion`,
  applied `target` (empty when none), and the class key (the vocabulary identity).
- Derived chord facts (the ratified derived-published-fact family, computed once here,
  consumers read): `rootPc`; the chord-member pitch classes with factor roles (root/third/
  fifth/seventh); the chord symbol string; the Roman-numeral string (the batch render's form);
  the root and bass SPELLINGS (tonal pitch classes) derived from (key, degree/class) — an
  instrument with its own establishment condition (§5.2); `diatonicToKey` as the class's own
  diatonic-vs-chromatic/applied answer (replacing every legacy re-derivation, OI-173's lesson);
  the bass chord-factor role per event (from the published per-event bass facts vs the members).
- The augmented-sixth display sub-type (Italian/German/French), when the class is the
  augmented-sixth family: derived from the SOUNDING pitch classes over the segment (presence of
  the fifth/added degrees), NOT from the vocabulary class — **correcting the audit's DERIVABLE
  note:** the fitted vocabulary collapsed the family to Italian pitch content (2 corpus tokens —
  the algorithm-completion step-1 record), so the class cannot carry the distinction; the
  sounding-content derivation is a presentation-layer read of L1 facts and can (§5.3).

### 3.3 Per segment — the uncertainty surface (B-full, OI-193; two field groups, no redefinition)

Group (i), the ESTABLISHED slice — published from the first switch:

- Key axis: the committed chord class re-scored under every scoreable candidate key (the
  decoder's full candidate set), committed key flagged; the runner-up and gap are derived facts.
- Chord axis: every scoreable vocabulary class re-scored under the committed key, committed
  class flagged; each alternative resolvable to its derived chord facts (the legacy
  `alternatives` consumers' need).

**★ Amendment (user-ratified option 1, 2026-07-26, at the posterior-slice delivery):** both
axes publish the FULL scoreable candidate lists — the original "runner-up" / "top-N" wording is
superseded. No truncation constant exists anywhere in the publication (a breadth "N" or a
gap-window width would be a hand-set value with no basis, #1/#19); nothing computed is discarded
at the boundary (#12; the evidence-publication amendment — the near-miss class scores are the
evidence the OI-192-class refinements read); display subsetting is a downstream presentation
read. Constrained-optimum ledger: top-N and gap-window truncation were examined and excluded
(both invent an unestablished constant and lose ambiguity-dependent evidence for no principled
gain); re-test only if a measured cost of the full list ever appears. The delivered form
(commits `9849134f40`/`56439ebad7` — shared label tables + per-segment full score lists,
bit-identical C++ parity) is this amendment's form.

Group (ii), the MARGINAL completion — added by OI-193 when its oracle is established:

- Key axis: the committed key's marginal mass over the segment span, and the alternative keys'
  masses.
- Chord axis: the committed class's marginal mass; the alternatives' masses.
- Boundary axis: per event, the marginal probability of a segment boundary (the
  cross-segmentation mass the slice cannot see — #17e's named limit, closed here).

**The two groups are SEPARATE named fields with separate semantics — the gap is a log-score
difference, the mass is a probability; neither ever silently replaces the other (#19: two
different instruments, each trusted only under its own establishment). Both carry establishment
status on the surface; both are model-internal quantities, never calibrated confidences (no
consumer load-bears on calibration until a #20-gated calibration is ever measured).** The
ranked-alternatives LISTS are ordered by group (i) at first delivery and re-ordered by group (ii)
mass when it lands — the ordering source is itself a stamped field, so a consumer knows which
instrument ranked what it reads.

### 3.4 Per key run — the un-rounded modal reading (C1; ratified decision 1 delivered)

For each key run and each scale degree 1..7 of its key: the sounding duration and onset count of
EVERY chromatic inflection of that degree actually observed in the run (computed from the
published L1 note facts relative to (tonic, mode)). This is the whole publication — counted,
un-rounded, nothing hand-set: minor's variable 6̂/7̂ (Dorian color, subtonic-vs-leading-tone),
major's lowered 7̂ (Mixolydian color) or raised 4̂ (Lydian color), and every borrowing appear as
their actual counts. The presentation layer may FORMAT a reading from it ("Dorian-leaning"); the
published fact is the counts, with establishment status (§5.4). No 21-value mode label is
inferred or published anywhere (C1); the two-mode key plus this table informationally dominates
the retired labels (#12).

### 3.5 Per note — ornament labels (OI-194; fields reserved, not in the first switch)

The record reserves the per-note ornament-label fields (category per the fitted emission's
classes; the voice-independent pedal-point class with bass/internal/inverted sub-labels per the
§10 ruling). They are delivered by OI-194's own increment, status-marked; until then the fields
are absent, the OI-194 row's declared gap. The "X ped." annotation re-expresses from this class
at that delivery.

### 3.6 What the record deliberately does NOT carry

No emission-sigmoid confidence, no Class-M margin (both retire with their producers — different
instruments than §3.3's, never silently re-used); no 21-value mode; no `temporalExtensions`
snapshot, `hasAnalyzedChord`, `keyAlternatives`, `fanout` (audited: no live reader — the
information either has no consumer or is decode-internal); no pedal fields on the chord identity
(§10: an ornament class, not an identity bit).

## 4. The audited consumers, mapped (every CSV row dispositioned; row-level source: the artifact)

| audited cluster (rows) | legacy form | contract source |
|---|---|---|
| span ticks (8 rows) | `startTick`/`endTick` | §3.2 span, unchanged semantics |
| key context (13) | `keyModeResult.{keySignatureFifths, mode, tonicPc}` | §3.2 key + derived fifths; mode = `isMajor` (+ §3.4 for color) |
| chord identity (14) | `identity.{rootPc, quality, bassPc, extensions, rootTpc, bassTpc}` + symbol | §3.2 derived chord facts |
| degree / diatonic (6) | `function.{degree, diatonicToKey}` | §3.2 degree + class-native `diatonicToKey` |
| confidence cluster (6) | `normalizedConfidence` vs 0.5/0.8/0.35 + `hasAssertiveExposure` | §3.3 mass/gap; gate VALUES become the emitters' declared presentation constants (§4.1) |
| ranked alternatives (4) | `alternatives` / `chordResults[1..]` / score suffix | §3.3 lists + per-candidate display facts; the "(%.2f)" suffix shows the stamped §3.3 quantity |
| sounding tones (7) | `tones[].{pitch,tpc}` | the published L1 note surface over the span — RAW facts, read where needed (the fact-publication corollary's read-don't-re-derive applies to DERIVED facts; notes are the substrate A itself consumes) |
| key areas (5) | `AnalyzedSection.keyAreas`, `keyAreaId` | the SECTION layer derives areas by collapsing §3.2's key sequence — its own layer's published derived fact, one producer, as today (#7) |
| cadence/pivot inputs (7) | section reads of key/degree/quality/confidence | §3.2 + §3.3 (the cadence labels stay the section layer's derivation over the record) |
| single-note context (10) | `NoteHarmonicContext.*` | the §1 note-seam view |
| exotic-mode branches (12 sites) | 21-mode plumbing, suffixes, borrowed-key search | retire under C1; §3.4 carries the color; retirement-map item 2 takes the plumbing |
| pedal (2) | `isPedalPoint`/`pedalBassPc` | §3.5 / OI-194 (§10 ruling) |
| retire-candidates (4) + in-memory pair | `hasAnalyzedChord`, `temporalExtensions`, dead `score` out-param, `keyAlternatives`/`fanout` | §3.6 — audited no-reader, nothing consumed is lost |
| accessibility (1) | formatted annotation string | unchanged: downstream of the composing-bridge formatter, which reads this record |

### 4.1 The presentation gates (the OI-182 cluster's successor rule)

The legacy exposure/annotation gates keep their FUNCTION (whether to expose a key run, coalesce
a region, write a cadence label) but their INPUT becomes §3.3's published mass/gap, and their
numeric values are the emitting layer's DECLARED presentation constants — outside the inference
surface, registered (the OI-182 row's disposition executes at the emitter's build step), each
with a stated rationale, none pretending to be an inference value. `kSameChordReannotationGap`
(960 ticks) re-homes to the implode emitter as a declared presentation-timing constant,
unchanged in role.

## 5. Establishment conditions (#19 — each derived instrument, before it is trusted)

1. **The decode equality:** the in-app record's inference fields on the 326 covered corpus
   scores equal the adopted batch decode (`adoption_decode.json`) — the increment's §8.3(a/b)
   condition, unchanged.
2. **The spelling derivation** (root/bass tonal pitch classes from key + degree/class): a
   deterministic mapping table, established by (a) derivation review against the standard
   theory, and (b) reproduction of the notated spellings on a hand-checked corpus sample where
   the notation is unambiguous; divergences enumerated, none silently accepted.
3. **The augmented-sixth sub-type read:** established at its (few) corpus sites by direct
   comparison with the sounding content — trivial by construction, recorded anyway.
4. **The modal-reading counter:** established by byte-reproduction on a hand-verified sample
   (the desk-sim corpus cases include modal material — bwv254 is the natural check).
5. **The posterior slice:** parity with the Python probe's published slice (the existing
   oracle); **the marginal completion:** the OI-193 oracle (forward logZ == backward logZ,
   per-span mass normalization, synthetic-case agreement with the fit-arc lattice arithmetic)
   BEFORE publication.
6. **The formatter continuity:** the chord-symbol/Roman strings the record publishes reproduce
   the batch render's forms on the shared cases (the same derivation, one path, #6).

## 6. What this contract does NOT decide

The C++ naming/shape of the record (build detail under the sanction); the emitters' declared
presentation-constant values (each declared at its emitter's build step, §4.1); the ornament
labels' delivery (OI-194's increment); the marginal completion's delivery (OI-193's step); the
retirement map's execution order after the switch (OI-180 §4). Nothing here changes inference:
the decode, tables, and weights are the adopted ones; this contract only defines their published
form on the notation surface.

## 7. Self-check (the standing rule, applied)

Diff read in full before delivery. Every audited CSV row appears in §4 (75 rows across the
clusters; counts reconcile: 56 A-SOURCED + 13 DERIVABLE + 4 RETIRE + 2 pedal-UNRESOLVED→§3.5).
No hand-set value is introduced anywhere (the §4.1 presentation constants are declared-at-build,
registered, outside inference); no consumed decision-bearing fact lacks a §3 source or a §3.6
audited-no-reader retirement; the aug-sixth correction is grounded in the committed step-1
record, not memory of it (verified in the handoff's ratified 2026-07-19 entry, "exactly 2
augmented-sixth tokens, the family collapsed to Italian pitch content"); the slice-vs-marginal
separation avoids the silent-reinterpretation defect (#19); provenance-on-the-surface implements
#16 at the record level. Plain-language duty: terms defined at §0; no self-invented labels
(section numbers are positional within this document).

## 8. Ratification asked (in a later turn, after this is read)

The contract as specified: the two seams (§1), provenance-on-the-surface (§2), the record (§3 —
including the two-group uncertainty surface and the modal-reading form), the consumer mapping
with the presentation-gate rule (§4), and the establishment conditions (§5). After ratification:
the build dispatches under the OI-180 sanction pattern (§8.2–8.4 of the increment plan),
starting with the record + table codegen behind the default-OFF driver.

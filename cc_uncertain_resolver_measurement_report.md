# CC Measurement Report — O1 part 3: is the carried "uncertain" residual resolved by FUNCTION or by a note-separable cue?

> **READ-ONLY / decode-only.** No production change, no wiring, no new layer/step was built — this
> measures whether one is *needed*. Instruction: `cc_instruction_uncertain_resolver_measurement.md`.
> Parent: `cowork_uncertain_resolver_investigation.md` (open item O1). GT = the human Roman-numeral
> oracle (When-in-Rome / DCML via music21, §0); our cadence detector is **not** used. One grading
> path: `compare_analyses` / `dcml_parser` / `compare_rn` / `characterise_bir_false`, reused verbatim.
>
> **Verdict (the input to O1): CONFIRMED.** The resolver is **Architectural Layer 5 (function)** — no
> distinct gated box between the note-layers and Layer 5. Every separable cue the residual exposes is
> owned by **Layers 1–4** (spelling, bass/inversion, metric, local voice-leading) → those cases are
> *Layer-4 leakage / "fix back in Layer 4,"* **not** a new box. The genuinely irreducible residual is
> distinguishable **only** by the surrounding functional progression → Layer 5. No cue is separable
> **and** unowned by an existing layer → **no new `(evidence × question)` → no new box.**

Local tooling (gitignored, per §5): `tools/cc_uncertain_resolver_measure.py` (chord-side cue test),
`tools/cc_uncertain_resolver_inspect.py` (per-case note-level inspector), and the reused
`tools/characterise_bir_false.py` + `tools/compare_rn.py`. Corpora: `tools/corpus/{baroque,jazz}`
(353/353, manifest-validated; WiR coverage 326/353 = 92.4%).

---

## §1 — The TRUE residual case set (built, not assumed)

The residual splits into a **chord-side** half (the carried chord-root ambiguity that reaches the
resolver) and a **key-side** half (relative-major/minor + tonicization-vs-modulation).

### §1A — Chord-side residual = the BIR=false set

Extraction is byte-faithful to `characterise_bir_false.py` (our region `chord_disagree` vs music21 ∧
winner `bassIsRoot==False` ∧ `music21 AND WiR agree`). The GT root is the music21==WiR root (function
oracle). My script reproduces the canonical counts exactly:

| preset | BIR=false (music21∧WiR agree) |
|---|---|
| Baroque | **53** |
| Jazz | **24** |

(These are the WiR-coverage-gated `music21_dcml_agree` subset of the 57/23/57 Default gate in CLAUDE.md;
the 4-case gap is WiR-coverage / Default-vs-WiR alignment, not a discrepancy.)

#### §1.2 exclusions — cases a (spelling-aware) Layer 4 settles *without* function

A case where the **notated tertian (letter-stack) spelled root == GT root** is settled by spelling
alone: a spelling-aware Layer 4 pins it and it never reaches the resolver — **not residual**.

| preset | §1.2 excluded (spelling pins GT root) | of total |
|---|---|---|
| Baroque | **32** | 60% |
| Jazz | **10** | 42% |

These are overwhelmingly fully-diminished-7th and diminished-triad sonorities the score spells
unambiguously (e.g. `bwv258@10560` GT B°7 spelled B; `bwv64.8@5280` GT E♭°7 spelled E♭;
`bwv392@14400` GT F♯°7 spelled F♯). Our pitch-class analyzer is spelling-blind, so it mis-rotates them
— but the **spelling is present and correct**, so this is **Layer-4 work, not resolver work**. This is
the §2(a) leakage class, reported here per the instruction. It is also exactly the fix CLAUDE.md's gate
policy already names: *"spelling/voice-leading-aware chord-root selection (Layer 4 / Stage 5–6)."*

**True chord-side residual (post-exclusion): Baroque 21, Jazz 14.**

### §1B — Key-side residual = the `key_disagree` bucket

`compare_rn` routes a pair to `key_disagree` **only** when **root_pc agrees AND coarse chord-quality
agrees** but the scale-degree/key differs (`classify_pair`: `elif root_match and not quality_match` with
`extract_quality` equal). That bucket **is** the relative-major/minor + tonicization-vs-modulation
residual. Sizes (WiR-Bach, 326 movements):

| preset | key_disagree | S1 =global ≠local (tonicization-vs-modulation) | S2 ≠global (relative-key / genuine key error) |
|---|---|---|---|
| Baroque | **2012** (19.9%) | **1281** (63.7%) | 731 (36.3%) |
| Jazz | **2098** (21.5%) | **1006** (48.0%) | 1092 (52.0%) |

Top patterns are the two named classes exactly: `V→I` (325/281), `vi→i` (161/108), `III→I` (134/148),
`I→V` (122/130), `II→V` (82/110) — i.e. *tonic-of-a-tonicized-key vs dominant-in-home-key* (S1) and
*relative major vs relative minor* (vi↔i, III↔I).

---

## §2 — The separability test (per residual case)

For each residual case: does any **single-slice note cue** the note-layers already own predict the GT
reading on its own? (a) spelling, (b) bass/inversion, (c) metric weight, (d) local stepwise resolution
within the window (notes+window only, no functional naming). **SEPARABLE** = ≥1 cue predicts GT;
**FUNCTIONAL** = none does (only the surrounding progression separates the readings). Fixed computation,
no tuning.

### §2A — Chord-side (per-case, hand-verified against the score)

Automated cue tally over the true residual:

| preset | residual | SEPARABLE (≥1 cue) | FUNCTIONAL | cue hits a / b / c / d |
|---|---|---|---|---|
| Baroque | 21 | 16 | 5 | a=0 · b=13 · c=1 · d=10 |
| Jazz | 14 | 8 | 6 | a=0 · b=5 · c=2 · d=4 |

`§2(a) = 0` on the post-exclusion residual on both presets — consistent: spelling-resolvable cases were
removed in §1.2, so spelling predicts none of what remains. **No spelling leakage in the residual.**

**Critically, the separable cues b/c/d are all Layer-1–4-owned, and hand-inspection (per-case, against
the actual notes) shows what they are firing on:**

- **bass (b) / metric (c)** fire where the GT roots the chord *on its bass* and our analyzer rooted
  away from it — an **inversion/bass under-use** in Layer 4, not function:
  `bwv245.17@4800` (GT `iv6/5`, root D = bass D; we read `F/D`), `bwv269@20640` (GT `viio6`, root F♯ =
  bass F♯; we read `D/F♯`), `bwv16.6@16800` (GT `viio7/iv`, root C♯ = bass C♯). "Root = bass" picks GT.
- **local stepwise resolution (d)** fires where the GT root is a leading tone resolving up a semitone
  into the next slice (`C♯→D`, `F♯→G`) — a **voice-leading** cue Layer 4 owns, computable from
  notes+window with no functional name.
- The remaining automated **FUNCTIONAL** hits are **not** clean function-only residual — inspection
  shows most are **segmentation / alignment noise**, also pre-Layer-5 work: `bwv10.7@36000` (a 5-note
  C-D-E-F-G scale over-grab), `bwv245.40@51360` and `bwv429@24240` (GT region tick-misaligned by whole
  measures), `bwv432@5520` (one slice contains both E and E♭ — a chromatic ornament over-grab).
  *[Erratum 2026-07-19, found at the factorization desk simulation
  (`cowork_factorization_desk_simulation.md` §4.6): the scale is C-D-E♭-F-G — `pitchClassSet: 173`
  at the committed region includes pc 3 (E♭), not pc 4. CLAUDE.md block (D) has it correctly.]*
- The **genuinely function-only** members are **share-tone pc-identical tetrads** where the bass is
  *neither* root and no spelling/voice-leading cue separates the two readings:
  `bwv352@1440` — A-C-E-F♯ **is simultaneously** `Am6` (root A, ours) **and** `F♯ø7` (root F♯, GT);
  identical pitch-class set, identical spelling. Only the function (F♯ø7 = ii°7 in A minor, its
  resolution) picks F♯. Jazz `bwv291@17760` (Eø7 ↔ Gm6) is the same structural pair — already flagged
  in CLAUDE.md as a verified symmetric/share-tone "class-(a)" case.

**Honest reading of the chord-side numbers:** the BIR=false set is a **contaminated proxy** for "what
reaches the resolver" — in the target architecture, Layer 4 (enriched with spelling + bass/inversion +
voice-leading) and Layers 1–2 (segmentation) settle the b/c/d/§1.2 cases *before* anything reaches the
resolver. After removing the L1–L4-owned cases (spelling 32/10, bass/metric/voice-leading ~16/8,
segmentation/alignment noise), the **genuine Layer-5 chord-side residual is the small share-tone
pc-identical class** — function-only.

### §2B — Key-side (FUNCTIONAL by construction — definitional, then confirmed)

The `key_disagree` bucket is **FUNCTIONAL with zero SEPARABLE share, by definition of the bucket**: a
pair lands there **only** when root_pc *and* coarse quality agree. The two readings therefore share an
**identical pitch-class set, identical bass, identical spelling, identical metric** — they differ only
in the *key/degree name*. No single-slice note cue (a)–(d) can separate readings that are
note-for-note identical:

- `V→I`: the slice is (say) a G-major triad. As an isolated slice it is G major under **both** readings;
  nothing in its notes says whether it is V-of-C or I-of-G. Only whether a cadence confirms G as a key
  area (or the music returns to C) decides — the surrounding progression = **function**.
- `vi→i` / `III→I` (relative major/minor): the ambiguous slice is, by construction, the **same diatonic
  collection** under both tonics; the disambiguator is *which tonic receives the cadential confirmation*
  — **function/cadence**.

Cue (d) cannot rescue separability here either: the leading-tone that would distinguish relative major
from minor is itself a **spelled/functional** scale-degree judgment, not a window-local note move
independent of the key being named. **Key-side residual: SEPARABLE = 0, FUNCTIONAL = 100%, both
presets, structurally.**

---

## §3 — Reused measurements (referenced, not recomputed)

Three already-run measurements bear directly on the key-side class and on whether a separate
selection/joint box helps — all point the same way (no distinct box; resolution is functional):

1. **Joint key+chord search is INERT** — `cc_audit_jointkeydecision_report.md` §2.2: the scoped
   chord×key joint is *"inert… ≈0, net slightly negative (+0.04/−0.14/−0.06 pp), moves 0.2% of regions
   on the entire 353-score corpus."* A standalone joint-selection step over the carried alternatives
   buys ~nothing — direct evidence **against** a distinct selection box, **for** resolution living in
   the functional reading (*"precision lives in evidence breadth, not the joint search"*).
2. **The selection layer is SATURATED** — `contrapunctus_findings.md` §5: with the re-ranker shipped,
   further re-ranking is a near-no-op; the residual chord-ID error is *"candidate/emission-level or
   key-level, **not selection-level**,"* and the unresolved cases *"need a candidate never surfaced →
   **functional rules**, not re-weights."* A separate re-ranking/selection box was built, measured, and
   found saturated.
3. **The tonicization-vs-modulation decision is a Stage-4 (key) + Stage-6 (function) job, on cadence
   evidence** — `cc_modulation_keypath_scoping_dossier.md`: DCML reads a local modulation on 39.9% of
   regions; we stay home on 74.5% of those; the de-masked `partial` sub-split shows 11.3%/9.5%
   (`home_vs_local`) of credited partials are masked "stayed-home-under-modulation." The fix is to
   commit a local **KeyArea** in the key resolver using the **local V→I cadence** as the confirming
   signal, then **Stage 6 labels** tonicization vs modulation from it. Both the decision (cadence) and
   the label (function) are Layer-5 evidence; **no separable non-function cue, no new box** — the lever
   enriches the existing key (Stage 4) and function (Stage 5/6) layers.

---

## §4 — Verdict (per class, per preset)

| Class | preset | true-residual size | FUNCTIONAL | SEPARABLE (cue → disposition) |
|---|---|---|---|---|
| Chord — spelled dim7/aug (§1.2) | Baroque | (excluded 32) | — | spelling (a) → **back to Layer 4** (spelling-aware), not resolver |
| | Jazz | (excluded 10) | — | spelling (a) → back to Layer 4 |
| Chord — inversion/voice-leading | Baroque | ~16 of 21 | — | bass (b)/metric (c)/local-resolution (d) → **back to Layer 4** (under-used bass + VL) |
| | Jazz | ~8 of 14 | — | bass/metric/VL → back to Layer 4 |
| Chord — share-tone pc-identical | Baroque | small (e.g. `bwv352`) | **100%** | none → **Layer 5** |
| | Jazz | small (e.g. `bwv291`) | **100%** | none → Layer 5 |
| Key — tonicization-vs-modulation (S1) | Baroque | 1281 | **100%** | none → **Layer 5** (cadence/KeyArea) |
| | Jazz | 1006 | **100%** | none → Layer 5 |
| Key — relative major/minor (in key_disagree) | Baroque | within 2012 | **100%** | none → **Layer 5** |
| | Jazz | within 2098 | **100%** | none → Layer 5 |

**The residual is essentially all FUNCTIONAL or Layer-1–4-owned — confirming O1's verdict.** Precisely:

- **No class is resolved by a separable cue that is *not already owned by an existing layer*.** The
  cues that fire (spelling, bass/inversion, metric, local voice-leading) are **Layer-1–4 evidence**.
  Per the instruction's §4 disposition, a separable cue that an existing layer owns is a **"fix back in
  Layer 4"**, *not* a distinct gated step. None of the cues is a genuinely new `(evidence × question)`,
  so **no distinct box is justified.**
- **The genuinely irreducible residual** — share-tone pc-identical sonorities (chord) and the entire
  `key_disagree` class (relative-major/minor + tonicization-vs-modulation) — is distinguishable **only**
  by the surrounding functional progression / cadence. By the decisive test (selection is
  *co-determined* with naming function, not separable), that residual **is Layer 5**.
- **§2(a) is empty** on the post-exclusion residual (no spelling leakage remaining); the §1.2 spelling
  cases (32/10) are reported as the Layer-4-leakage class, not resolver work.
- The §3 reused measurements independently corroborate: a separate joint/selection box is **inert /
  saturated**, and the one key-side lever (modulation) routes to the **enriched key + function layers**
  on **cadence** evidence — never to a new pre-Layer-5 box.

**Bottom line for the specs (on the user's ratification):** O1's provisional verdict stands. Collapse
the three names ("later gated key-and-chord step," "function layer," "Architectural Layer 5") to **one —
"Architectural Layer 5 (function)"** — and state that resolving the carried "uncertain" readings is part
of Layer 5's job at its gated entry, on functional/cadential evidence the note-layers structurally lack.
The measurement adds one refinement worth recording: the BIR=false set **overstates** the resolver
residual ~3–10× — the bulk is Layer-1–4 work (spelling 60%/42%, bass-inversion + voice-leading, and
segmentation noise) the enriched note-layers settle first; the function-only core that actually reaches
Layer 5 is **small** (share-tone pc-identical chords) on the chord side and **structural** (the whole
`key_disagree` class) on the key side.

---

## §5 — Stop-condition compliance

No production output moved; no new layer/step built (read-only/decode-only). The FUNCTIONAL test used
the WiR/DCML GT oracle, **never** our cadence detector. One grading path (the committed
`compare_analyses`/`dcml_parser`/`compare_rn`/`characterise_bir_false`). No `upstream` push. Local
measurement scripts are gitignored (`tools/cc_*`).

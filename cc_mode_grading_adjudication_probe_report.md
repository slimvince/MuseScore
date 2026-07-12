# CC — Mode-grading adjudication probe (OI-132 / DISCOVERY D2, OI-145 wave 1) — report

**Dispatch:** `cc_instruction` (Cowork, 2026-07-12) — READ-ONLY probe producing the evidence the
user's ruling on OI-132 (the DT-6 key-parser divergence surfaced by the measurement-chain
hardening) needs. **No graded-pipeline code changed; no constant tuned; no golden refreshed.**
Both candidate rules are computed side by side in the probe only.

**Instrument:** `tools/mode_grading_adjudication_probe.py` (this commit). Machine-readable results:
`tools/reports/mode_grading_adjudication_probe.json` (regenerable; force-added this commit).
HEAD at run `26f53b5ba2`; corpus `c50002fee1`; ground truth through the OI-142-corrected
`dcml.load_wir_regions`.

**Bottom line (measurement, not a decision — the ruling is the user's):** the evidence supports
**Rule B (parent collection)** for all five dominant-family conflict modes. On the LOCAL key column
— the musically-correct comparison for a tonicized dominant span — Rule B matches what the DCML
annotators wrote on **67 % of the disagreeing duration (54–100 % per mode); Rule A matches on 0 %.**
Rule A edges out Rule B on exactly ONE narrow slice: the HOME column of Lydian-dominant spans (a
few cells whose piece home key is the emitted tonic as major). Adopting Rule B also *fixes* a
pre-existing parser artifact (Lyd+/Mixb6/Lydb7 currently KEYFAIL and count against agreement).

---

## 1. What the disagreement actually is (grounded at the code + data)

The two graded OURS-key parsers reduce a span's emitted key/mode to `(tonic_pc, is_major)` for
key-agreement grading. They disagree on the analyzer's **dominant-family exotic modes** — the modes
whose **tonic triad is major** but whose **parent collection is a minor scale**. Enumerated from the
committed corpus (`.ours.json` `key` field, all three presets, duration-weighted), the emitted mode
vocabulary and the two existing parsers' reductions are:

| emitted mode | tonic triad | parent collection | `_our_key_tonic` (SHARED, governs the committed columns) | `parse_our_key` (oracle tool) |
|---|---|---|---|---|
| maj / Mixolyd / Lyd | major | major | major | major |
| min / harm / mel / Dor / Phryg | minor | minor | minor | minor |
| **PhrygDom** | **major** | **harmonic minor** | **minor** (prefix `phr`) | **major** ← diverge |
| **alt** | **major** (altered dominant) | **melodic minor** | **minor** (prefix `alt`) | **major** ← diverge |
| **Lydb7** (Lyd♭7) | **major** | **melodic minor** | **KEYFAIL** (regex chokes on `♭`/digit) | tonic-only, mode None ← diverge |
| **Lyd+** | **major** (aug) | **melodic minor** | **KEYFAIL** | major ← diverge |
| **Mixb6** (Mix♭6) | **major** | **melodic minor** | **KEYFAIL** | major ← diverge |
| Dorb2 (Dor♭2) | minor | melodic minor | KEYFAIL | minor (not a conflict — both agree minor) |

**Two facts the enumeration exposes, both material to the ruling:**

1. **The current committed grading (`_our_key_tonic`) follows NEITHER candidate rule** — it grades
   PhrygDom/alt as *same-tonic minor* (a third reduction that is neither Rule A's major nor Rule B's
   parent-minor), and it grades Lydb7/Lyd+/Mixb6 as **KEYFAIL** because its `[A-Za-z]+` mode regex
   chokes on the unicode `♭` and the digit. So "consolidating to one shared rule" (the OI-132 fix)
   necessarily *moves* the graded figure away from this ad-hoc baseline whichever rule wins.
2. **The KEYFAIL for Lydb7/Lyd+/Mixb6 is a parser artifact, not a music-theory choice** — those
   regions currently abstain (and count against key-agreement in the committed `agree/scored_dur`
   formula). *Either* principled rule fixes this; it is orthogonal to the A-vs-B mode/tonic choice.

**The two candidate rules, as implemented in the probe** (both keep every non-conflict mode at the
committed reduction verbatim; they differ ONLY on the five conflict modes):

- **Rule A — tonic-triad quality:** `(emitted tonic, major)`. A key is named by its tonic chord;
  these five modes have a major(-third) tonic triad. (= what `parse_our_key` does for PhrygDom/alt.)
- **Rule B — parent collection:** `(parent-minor tonic, minor)`, the minor key the mode is a rotation
  of. Standard modes-of-the-scale derivation (cited in the probe):
  PhrygDom = 5th mode of harmonic minor → parent tonic = emitted − 7; Mixb6 = 5th mode of melodic
  minor → −7; Lydb7 = 4th mode → −5; Lyd+ = 3rd mode → −3; alt = 7th mode → +1. So "E PhrygDom"
  grades as `A minor` (the key it is the dominant of).

---

## 2. The disagreeing population (Task 1)

A region enters the population iff Rule A and Rule B yield different graded outcomes — which, by
construction, is exactly the five conflict-mode cells (Rule A: emitted-tonic + major; Rule B:
parent-tonic + minor — always different in both tonic and mode). Everywhere else the two rules are
identical (both = the committed reduction).

| preset | pop cells | pop duration | % of graded (scored) duration | composition by mode (cells) |
|---|---|---|---|---|
| baroque | 70 | 42 240 | **0.509 %** | PhrygDom 59, Mixb6 9, Lyd+ 2 |
| jazz | 101 | 58 560 | **0.706 %** | PhrygDom 65, alt 29, Mixb6 3, Lydb7 3, Lyd+ 1 |
| default | 65 | 39 840 | **0.480 %** | Mixb6 24, Lyd+ 20, PhrygDom 15, Lydb7 6 |

The population concentrates in a small number of stems (chorales with a tonicized-dominant passage
the annotator keeps in the local minor — e.g. `bwv123.6` recurs across all three presets). Full
per-stem, per-cell dump in the JSON (`population_cells`).

---

## 3. Both rules graded corpus-wide (Task 2)

Key-agreement % = `agree_dur / scored_dur` (the committed a8 formula; keyfail counts against, per the
OI-33 abstain convention). Δ is versus the current committed baseline (`_our_key_tonic`).

| preset | column | baseline % | Rule A % (Δ) | Rule B % (Δ) | \|A−B\| |
|---|---|---|---|---|---|
| baroque | home | 71.2909 | 71.2157 (−0.0752) | **71.4182 (+0.1273)** | 0.2025 |
| baroque | local | 65.7238 | 65.6891 (−0.0347) | **65.9900 (+0.2662)** | 0.3009 |
| jazz | home | 67.4887 | 67.5003 (+0.0116) | **67.8274 (+0.3387)** | 0.3271 |
| jazz | local | 62.4942 | 62.4942 (+0.0000) | **62.9805 (+0.4863)** | 0.4863 |
| default | home | 70.5183 | 70.5414 (+0.0231) | **70.6514 (+0.1331)** | 0.1100 |
| default | local | 65.3852 | 65.3621 (−0.0231) | **65.7093 (+0.3241)** | 0.3472 |

- **Rule B raises key-agreement on every column of every preset** (+0.13 to +0.49 pp); **Rule A is
  ≈flat** (−0.08 to +0.02 pp) — it moves almost nothing because, like the same-tonic-minor baseline,
  it rarely matches the ground truth on these cells.
- **Coverage (abstain) improves under both rules:** baseline key-abstain (KEYFAIL) duration
  7 680 / 10 800 / 33 120 (baroque/jazz/default, home) drops to 0 / 4 080 / 2 400 — both rules rescue
  the Lydb7/Lyd+/Mixb6 KEYFAILs; the small residual (Dorb2, a non-conflict mode) is left abstaining
  by design. Coverage rises to ~100 %.

**Establishment (both proven by the probe, self-asserting, ESTABLISHMENT PASS on all three presets):**
- **(a)** the baseline column reproduces the committed `tools/robust_stop/summary.json` a8 counters
  **exactly** — `b_key_agree`, `b_key_dis`, `b_key_fail` and their `_local` twins, and `scored_dur`,
  duration-for-duration on all three presets. This proves the probe's union-of-boundaries cell
  harness is identical to a8's `build_piece_grid` (it also self-validates each piece against
  `crn.grid_score_regions`).
- **(b)** with the disagreeing population EXCLUDED, Rule A and Rule B reproduce the baseline column
  **exactly** (every verdict-duration bucket identical). This proves the rules differ only where they
  differ — the five conflict modes — and nowhere else.

---

## 4. Desk-check against the annotators (Task 3)

For each case: our emitted mode, both reductions, and the DCML annotator's actual `analysis.txt`
line for the span. `bwv145.5` is an OI-142 transposed edition (+2); its corrected local key is quoted
(raw text + 2 semitones).

1. **`bwv123.6` @2400 (baroque; recurs @2880 jazz+default), our "C#PhrygDom".** Annotator:
   `m1 b: i b3 f#: viio6/5` then `m2 V6 … V7 b3 i` — a **dominant prolongation in F♯ minor** resolving
   to i. Rule B = **F♯ minor = the annotator's `f#`** → AGREE. Rule A = C♯ major, baseline = C♯ minor
   → both disagree. Our engine detected the Phrygian-dominant *scale on the dominant* (C♯); the
   annotator keeps it in the minor key. **Rule B matches.**
2. **`bwv26.6` @8160 (baroque), our "AMix♭6".** Annotator: `m4 … || d: V` then
   `m5 V b2 V6 b2.5 V b3 i` — a **dominant prolongation in D minor**. Rule B = **D minor = `d`** →
   AGREE; Rule A = A major → disagree; baseline = **KEYFAIL**. **Rule B matches and rescues a keyfail.**
3. **`bwv407` @31680 (jazz), our "DLyd♭7".** Annotator: `m17 a: IV b3 viio7 b4 V6` — the span is
   **`viio7` in A minor**. Rule B = **A minor = `a`** → AGREE; Rule A = D major → disagree; baseline =
   **KEYFAIL**. **Rule B matches and rescues a keyfail.** (Note: this piece's HOME key is D major, so on
   the *home* column Rule A's "D major" would match instead — the one place Rule A wins; see §5.)
4. **`bwv387` @13440 (default), our "GLyd♭7".** Annotator: `m5 … b4 d: VI` … `m7 IV6 b2 V6/5 b3 i b4 VI`
   — the span is **`VI` in D minor**. Rule B = **D minor = `d`** → AGREE; Rule A = G major → disagree;
   baseline = **KEYFAIL**. **Rule B matches and rescues a keyfail.**
5. **`bwv282` @7680 (baroque+jazz), our "CLyd+".** Annotator: `m6 viio7/ii` — an **applied
   leading-tone chord within G major** (the prevailing key; `local='G'`). Rule A = C major, Rule B =
   A minor, baseline = KEYFAIL — **NONE matches** the annotator's G major. Here the *engine's mode
   label itself is questionable* (it read a Lydian-augmented region over a plain applied diminished
   chord). **Neither rule; upstream issue (see §6).**
6. **`bwv382` @22560 (jazz), our "DMix♭6".** Annotator local = D minor (a tonic region). Rule A = D
   major (right tonic, wrong mode), Rule B = G minor (wrong tonic), baseline = KEYFAIL — **NONE
   matches** D minor exactly. Again the *engine emitted an exotic dominant scale on what the annotator
   reads as the tonic minor*. **Neither rule; upstream issue (see §6).**
7. **`bwv145.5` @11520 (jazz; transposed +2), our "D#alt".** Annotator (corrected): the span is
   **`V6` in A major** (raw `m9 … G: V6`, +2 → A major; the chord is E major = V of A). Rule A =
   E♭ major, Rule B = E minor, baseline = E♭ minor — **NONE matches** A major. The engine labelled a
   plain V6 as an altered-scale region (the altered scale has no unambiguous tonic triad at all —
   another reason Rule A is awkward here). **Neither rule; upstream issue (see §6).**

**Verdict tally over the WHOLE population (duration-weighted), which rule agrees with the annotator:**

| | LOCAL column | | HOME column | |
|---|---|---|---|---|
| mode | Rule A | Rule B | Rule A | Rule B |
| PhrygDom | 0 % | **72 %** | 0 % | 39 % |
| Mixb6 | 0 % | **60 %** | 0 % | 69 % |
| Lydb7 | 0 % | **100 %** | **67 %** | 22 % |
| Lyd+ | 0 % | **58 %** | 0 % | 0 % |
| alt | 0 % | **54 %** | 0 % | 55 % |
| **ALL** | **0 %** | **67 %** | **2 %** | **40 %** |

The residual (neither) is the §6 sub-population — engine mode-mislabels, not a grading-rule question.

---

## 5. The three written expectations, answered (Task 4)

1. **"The disagreeing population is SMALL — under 1 % on Baroque/Default, possibly more on Jazz."**
   **MET.** Baroque 0.509 %, Default 0.480 %, Jazz 0.706 % (Jazz is the largest, as predicted; all
   under 1 %).
2. **"For PhrygDom spans, PARENT-COLLECTION matches the annotators on ≥60 %; altered/Lydian-dominant
   may lean the other way."** **First clause MET, second clause largely FAILED.** PhrygDom → Rule B
   72 % (local), well over 60 %. But the "lean the other way [toward the tonic-triad rule]" prediction
   is *not* borne out: on the LOCAL column even Lydian-dominant is **100 %** Rule B and altered is
   **54 %** Rule B — **Rule A matches 0 % of the local duration for every mode.** Rule A wins in exactly
   one place: the **HOME** column of **Lydian dominant** (67 % vs 22 %, a 2 880-tick slice), where a
   piece's home key happens to be the emitted tonic as major. So the "other way" is real but confined
   to Lydb7-on-home, not a general altered/Lydian-dominant lean.
3. **"The two rules' whole-corpus key-agreement difference is under 0.5 pp per column per preset."**
   **MET.** Max \|A−B\| = **0.486 pp** (jazz local) < 0.5; all others smaller. (Note the more
   decision-relevant delta is Rule-B-vs-current-baseline, up to +0.486 pp — that is the move
   consolidation would make.)

---

## 6. A declared inference finding (OI-147 — Layer 3; NOT fixed here)

The desk-check surfaced a second, distinct sub-population inside the "neither" residual (~33 % of the
disagreeing duration on the local column): **cases where the engine emits an exotic dominant-family
scale label on a span the annotator reads as a plain diatonic chord** — a Lydian-augmented label over
an applied leading-tone chord (`bwv282`), an Aeolian-dominant label over a tonic minor (`bwv382`), an
altered-scale label over a plain V6 (`bwv145.5`). No grading rule can rescue these, because the
*mode emission itself* is the mismatch — a Layer-3 key/mode inference question. **Per the standing
instruction ("declare inference problems to Cowork, do not fix"), this is recorded as OI-147 and NOT
acted on.** It does not change the §4 conclusion (Rule B remains the best of the three for the genuine
dominant-tonicization cases); it bounds how much of the population any grading rule can reach.

---

## 7. Which rule the evidence supports (measurement; the ruling is the user's)

- **Rule B (parent collection) for all five conflict modes.** It is the only rule that matches the
  annotators (67 % of the disagreeing duration on the local column, 54–100 % per mode; Rule A: 0 %),
  it is the only rule that raises the governing key-agreement figure (+0.13…+0.49 pp; Rule A ≈ 0), and
  — with the KEYFAIL artifact it fixes — it *both* improves coverage and improves agreement. This
  holds *per mode label*; the rules do not split by mode in favour of Rule A on the local column.
- **The one honest caveat for the user:** on the **home/global** column, **Lydian dominant** favours
  Rule A (67 % vs 22 %) — a piece whose home key is the emitted tonic (as major) with a momentary
  Lydian-dominant colour. This is a small slice (2 880 ticks, a handful of cells). If the consolidated
  rule is applied uniformly, Rule B costs a little home-column agreement on Lydb7 while gaining on the
  local column and on every other mode. Since our engine's per-region key tracks a *local* key, and
  the LOCAL column is the musically-appropriate comparison for a tonicized dominant span, the local
  evidence is the weightier one — but this is the user's call.
- **Consolidation note (for whoever lands the OI-132 fix after the ruling):** the current committed
  `_our_key_tonic` matches *neither* rule (same-tonic-minor for PhrygDom/alt, KEYFAIL for the rest),
  so adopting *either* rule moves the graded columns and is a **re-baseline event** (the O-12 snapshot
  + user ratification + the `tools/robust_stop/` re-stamp ritual), not a byte-identical hygiene fold —
  exactly as OI-132 / D2 stated. This probe touched none of that.

---

## 8. Self-check (over every diff, before reporting done)

- **READ-ONLY honoured:** no `src/composing` change, no graded-pipeline code touched, no constant
  tuned, no golden refreshed. The probe writes ONLY to `tools/reports/` (gitignored/regenerable);
  `tools/robust_stop/` and `tools/corpus/` were written by nothing (git status confirms the only
  tracked-modified file is the known carry `cowork_joint_key_chord_design.md`).
- **Verified at the code and data, never at assertion:** the two rules are grounded in the actual
  emitted-mode vocabulary scanned from the committed corpus and the two real parser code paths; the
  baseline column reproduces the committed a8 counters exactly (establishment (a)); the desk-check
  quotes the annotators' actual `analysis.txt` lines.
- **No self-invented labels/jargon:** "Rule A / Rule B" and "conflict mode" are the dispatch's own
  terms; mode names and parent derivations are standard music theory.
- **Register discipline:** OI-132 updated with the probe's outcome (ruling pending); the new inference
  observation gets its own row OI-147 in the SAME commit. Plain language; American English.
- **Git:** only my own files staged by name; `cc_*.md` + this instruction force-added; `cowork_*`
  carries left unstaged; `git remote -v` confirmed `upstream` push disabled; pushed to `origin` only.

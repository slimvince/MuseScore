# J-key-iii — STEP 3: snapshot adjudication → **STOP FIRED** (do NOT flip ON, do NOT commit)

> **HELD — uncommitted. The §2/§6 STOP condition fired: ≥3 of the 11 moved snapshot goldens
> adjudicate as KEY REGRESSIONS vs DCML ground truth — ALL on OUT-of-WiR-Bach-scope
> (non-chorale) scores. Per the instruction, the goldens were NOT refreshed (restored
> byte-identically to the flag-OFF baseline), the production default was NOT flipped ON, and
> NO commit was made. Surfaced for a Cowork/user decision.**
>
> **Date:** 2026-06-16. **HEAD:** `2245aedf82` (unchanged). **Wiring source on disk:
> UNTOUCHED** (`jointKeyWiringEnabled()` still defaults OFF; no edits this step). Every Bach
> key is `[oracle]` via WiR rntxt; every non-Bach key is `[oracle]` via the committed DCML
> `harmonies.tsv` (`globalkey`/`localkey`), except chopin op30-1 (no DCML harmonies file →
> key signature + published-work key).

---

## 0. Headline

1. **The §2 load-bearing gate FAILED.** Of the 11 snapshot goldens that move under wiring-ON,
   **3 contain genuine KEY regressions** (the new key reading is *worse* than the old per
   DCML), **2 are improvements**, and **6 are neutral** (mode-collapse or region-key-unchanged).
2. **All 3 regressions are on OUT-of-WiR-Bach-scope scores** — `mozart_k279_1` (C major → F
   major, full window), `bach_bwv806_gigue` (A major → D major, full window), and
   `corelli_op01n08a` (tail regions C minor → G minor). None is a Bach chorale.
3. **The IN-scope Bach chorales (001, 003, 137) are all improvement-or-neutral** — consistent
   with, and corroborating, the measured J-key-i win. The regression is confined to the
   **non-chorale repertoire the J-key-i win was never measured on** — exactly the "flip-ON
   applies it to UNMEASURED non-Bach" scope caveat the Step-2 report flagged.
4. **Action taken (per instruction §2/§6 STOP):** goldens **restored byte-identically** to the
   flag-OFF baseline (0 diffs, git-clean); default **NOT flipped**; **NO commit**; §3 (refresh
   + flip) and §4 (gates ON) **correctly not executed** (they are gated behind a clean
   adjudication, which did not obtain).

**Recommendation: do NOT ship the global flip-ON as-is.** The constrained-joint key decision
(J-key-i strong-signature-backbone) is calibrated and measured on Bach chorales; applied
globally it **degrades non-chorale key reading**. Options for the user in §6.

---

## 1. Method

1. Built state confirmed current: binaries (`ninja_build_rel`, Jun-16 09:48) are newer than the
   on-disk wiring sources → no rebuild needed for adjudication. **Flag-OFF baseline re-confirmed
   byte-identical:** composing **545**, notation **57**, pipeline_snapshot **11/11**.
2. Backed up the 11 flag-OFF goldens, regenerated them with **`MUSE_JOINT_KEY_WIRING=1
   pipeline_snapshot_tests --update-goldens`** (wiring-ON, bridge/notation path), then did a
   **structural per-field diff** (old vs new) over every snapshot array
   (`implode`/`keyAreas`/`tickRegional`/`tickLocal`/`annotation`/`implodedChordTrack`).
3. Adjudicated each moved score's **region-level key** (the user-facing `implode`/`annotation`
   key — the primary axis) against ground truth:
   - **Bach chorales** → WiR rntxt (`when_in_rome/.../Bach.../Chorales/<NNN>/analysis.txt`).
   - **Non-Bach + Bach non-chorale** → committed DCML `harmonies.tsv` `globalkey`/`localkey`
     (authoritative ground truth, present for all of them except chopin op30-1). *(DCML is the
     project's gold standard per the ground-truth rule; it is strictly stronger than the
     music21 oracle the instruction named as the non-Bach fallback. The instruction proposed
     music21 on the assumption these were un-covered; the Step-2 report itself noted "they DO
     have When-in-Rome coverage." music21 cannot read the `.mscx` corpus files headless here,
     so DCML is both better and the only working oracle.)*
   - **chopin op30-1** (no DCML `harmonies.tsv` in the corpus — only `chords/notes/measures`):
     key signature (`-3` flats) + the published-work key (Mazurka Op. 30 No. 1, C minor).
4. **Ground-truth provenance trap caught:** the snapshot `bach_chorale_137` is the MS3 file
   *"137 Du, o schönes Weltgebäude"* = **BWV 301**, but the WiR folder `137` is a *different*
   chorale ("Wer Gott vertraut", G major — WiR numbering ≠ MS3/Riemenschneider numbering). The
   correct GT is **WiR folder `134`** (`remote.json` `"BWV":"301"`, analysis `m1 d: i …` → **D
   minor**). Using folder 137 would have mis-adjudicated this score.

---

## 2. Per-score adjudication (the 11 moved goldens)

Key = the region-level (user-facing `implode`/`annotation`) key over the first 16 measures
(the snapshot's `kMaxAnalysisMeasures` cap). "old→new" = flag-OFF golden → wiring-ON output.

| # | score | scope | GT (oracle) | old → new (region key) | verdict |
|---|---|---|---|---|---|
| 1 | bach_chorale_001 | **in (WiR)** | **G major** (rntxt `G: I`) | G → G (region unchanged; 4 late tickRegional vi/IV wobbles) | **NEUTRAL** |
| 2 | bach_chorale_003 | **in (WiR)** | **A minor** w/ **e: v tonicization @ m5** (rntxt) | A-mel→A-min (collapse); detects e-min @ m5; returns to a-min @ m7 | **IMPROVEMENT** |
| 3 | bach_chorale_137 (BWV 301) | **in (WiR)** | **D minor** (WiR 134, `d: i`) | **F maj → D min** (relative-major misread → home) | **IMPROVEMENT** |
| 4 | bach_bwv806_gigue | out | **A major** (DCML `globalkey=A`, localkey I/V/I; **D never appears**) | **A maj → D maj** (whole window) | **⛔ REGRESSION** |
| 5 | bach_bwv806_prelude | out | **A major** (DCML; I→V→I→vi) | A → A (region unchanged; tickRegional A→E partly matches the DCML V section) | NEUTRAL |
| 6 | mozart_k279_1 | out | **C major** (DCML `globalkey=C`, **localkey I throughout mm 1–16**) | **C maj → F maj** (whole window) | **⛔ REGRESSION** |
| 7 | mozart_k280_1 | out | **F major** (DCML, localkey I) | F → F (region unchanged; 6 tickRegional F→Bb=IV wobbles) | NEUTRAL |
| 8 | chopin_bi105_op30_1 | out | **C minor** (keysig −3; Op. 30/1, C minor) | **G-PhrygDom / Eb-maj → C min** | **IMPROVEMENT** |
| 9 | chopin_bi105_op30_2 | out | (G minor; DCML) | only `keyAreas.confidence` moved | NEUTRAL |
| 10 | corelli_op01n08a | out | **C minor** (DCML `globalkey=c`, **localkey i for ALL 16 mm**) | bulk C-Dor/C-mel/early-G-min → **C min** (good) **but tail C-min → G-min** @ t26880–28800 | **⛔ REGRESSION (mixed)** |
| 11 | schumann_kinderszenen_n01 | out | **G major** (DCML, localkey I) | G → G (region unchanged; 4 tickRegional wobbles) | NEUTRAL |

### The three regressions (detail)

- **#6 mozart_k279_1 — C major → F major (whole 16-measure window).** DCML: `globalkey=C`,
  `localkey=I` with **no modulation in mm 1–16**; the opening is the textbook
  `I – ii6 – V2 – I6 – ii6 – V – I(PAC)` in C. The flag-OFF golden reads the structural points
  correctly (C maj @ t0 and the whole t12840–25200 return) with an A-minor / F-Lydian excursion
  between; wiring-ON reads **F major everywhere** — wrong on every region, including the
  unambiguous C-major opening. F is the **subdominant**, not a home or local key. *Downstream
  chord-axis fallout (bridge stage-5 sparse-quality re-derivation under the wrong key):
  tickRegional t11520 `D minor → C major`, t12480 `D minor → C augmented`.*

- **#4 bach_bwv806_gigue — A major → D major (whole window).** DCML: `globalkey=A`, localkeys
  `I (mm 0–6) → V=E (mm 7–15) → I (m 16)`; **D never appears as a local key.** The flag-OFF
  golden reads A major throughout (correct on the I sections, misses the E tonicization);
  wiring-ON reads **D major everywhere** — the **subdominant**, wrong on every region. Signature
  is A major (3 ♯), so the joint decision committed a **non-home, non-local** key globally.
  *Downstream: tickRegional t8880/t9600 `E major → F# minor`; implodedChordTrack t7440 drops a
  pitch and writes `Dadd9/A`.*

- **#10 corelli_op01n08a — tail C minor → G minor.** The piece is 16 measures total, DCML
  `localkey=i` (**C minor**) for **all** of them. Wiring-ON corrects the bulk (the OLD
  C-Dorian / C-melodic / early-G-minor mis-spellings → C minor — a real improvement) **but
  introduces a new over-modulation at the tail** (t26880–28800: C minor → G minor=v, where DCML
  is i). Net-improving, but it **contains a regression**, which alone trips the STOP.

### The two improvements (detail)
- **#3 bach_chorale_137 / BWV 301** — flag-OFF read the body as **F major** (the relative
  major); DCML home is **D minor**; wiring-ON → D minor. Clean correction of a relative-pair
  error (exactly what the J-key-i win targets).
- **#8 chopin op30-1** — flag-OFF opened in **G-PhrygianDominant** and read **Eb major**
  (relative major); the work is **C minor** (keysig −3); wiring-ON → C minor. Correction.
- **#2 bach_chorale_003** — wiring-ON adds the **e-minor (v) tonicization at m5** that DCML
  annotates (`m5 … e: viio6 …`) and corrects the OLD over-extended e-minor back to a-minor at
  m7+ (DCML `m7 a: VI …`); the A-melodic→A-minor renames are tonic-preserving (DCML is binary
  a-minor). Net more DCML-aligned.

### Neutral (6)
Region-level key unchanged (or only `keyAreas.confidence` / a tonic-preserving mode rename
moved). Some carry **local `tickRegional` wobbles** at sampled status-bar ticks (e.g.
mozart_k280 F→Bb=IV, schumann 4 ticks, bwv806_prelude A→E which actually tracks the DCML V
section). These are momentary local-key samples, not the primary region key; they were **not**
individually adjudicated as improvement/regression because the user-facing region key is
unchanged and the STOP is already decisively fired by the region-level regressions above. They
are flagged here for completeness, not waved away.

---

## 3. Why the non-chorale scores regress (diagnostic, for the decision)

The wired decision is the **J-key-i strong-signature-backbone**, calibrated and measured on
**Bach chorales** (dense 4-voice homophony, frequent cadences, short regions). Applied to
non-chorale textures the joint Viterbi over-commits the **global** key — and the failures
cluster on the **subdominant** (K279: C→F; gigue: A→D) and the **dominant/relative** (corelli
tail: i→v). The common cause is that the note-evidence + cadence-anchor weighting that picks
the right home on chorales mis-weights on Alberti-bass / compound-meter / single-line
contrapuntal textures. This is the *measured* realization of the Step-2 scope caveat: the win
is **Bach-chorale-measured**, and flip-ON applies it to **unmeasured non-chorale repertoire**,
where it is **net-negative on key** (≥3/8 of the out-of-scope snapshot scores).

Note also: on the bridge/notation path the chord axis is **NOT byte-identical** under flip-ON
(unlike the batch/BIR path, which is) — stage-5 sparse-quality re-derivation reads the resolved
key, so a wrong joint key drags a few chord qualities with it (the tickRegional /
implodedChordTrack flips above). The batch-path BIR gate (57/23/57) remains byte-identical by
construction (chord = production R0), but a **global** flip-ON would still ship the wrong
bridge-path chord re-derivations on the regressing scores.

---

## 4. State after this step (no behavior change shipped)

| item | state |
|---|---|
| Snapshot goldens | **restored byte-identical** to flag-OFF baseline (0 diffs vs backup; `git status` clean for the snapshots dir) |
| Wiring source on disk | **UNCHANGED** — `jointKeyWiringEnabled()` still defaults OFF; **no edits made this step** |
| Production default flip-ON (§3) | **NOT done** (STOP) |
| Gates with wiring ON (§4) | **NOT run** (gated behind a clean adjudication) |
| Commit | **NONE** |
| HEAD | `2245aedf82` (unchanged) |
| Files touched | only HELD instruments: this report; `/tmp` scratch (golden backup + diff scripts). No tracked file modified. |

---

## 5. Stop-condition trace (instruction §6)

| condition | fired? |
|---|---|
| Any moved snapshot golden adjudicates as a regression → STOP, surface (do not refresh/flip) | **YES — 3 scores (mozart_k279, bwv806_gigue, corelli tail). Goldens not refreshed; default not flipped; surfaced.** |
| BIR moves on any preset (chord-axis) | n/a — not re-measured (blocked before flip; batch BIR is byte-identical by construction) |
| Suite fails un-adjudicated | No |
| Flip-ON doesn't reach the production/bridge path | n/a — the moves prove the bridge path DOES run the wiring (good), but it regresses |
| Any push / edit outside `src/composing` + `tools` + goldens | No — no source edits at all this step |
| Commit before Cowork verifies | No commit |

---

## 6. Surfaced for Cowork/user — the decision

The instruction's landing sequence assumed *"every moved golden is improvement-or-neutral."*
That assumption is **false**: the global flip-ON regresses non-chorale key reading. Live options
(the constrained-joint **key win on Bach chorales still stands** — it is realized and verified;
the issue is solely the **global** application to unmeasured repertoire):

- **(A) Do NOT flip globally — scope the wiring to where it is measured-positive.** Gate
  `applyJointKeyWiring` (or its commit) to the validated WiR-Bach-chorale scope (or a
  texture/repertoire signal), leaving non-chorale repertoire on the production resolver. Ships
  the measured win without the non-chorale regression. *(Needs a scoping signal designed +
  measured — a new step.)*
- **(B) Fix the non-chorale over-commitment first, then flip.** Re-measure / re-tune the joint
  decision on non-chorale repertoire (subdominant/relative over-commitment is the failure mode)
  before any global flip-ON. Defers the win; addresses the root cause.
- **(C) Commit the wiring flag-OFF (dormant, byte-identical) as a staging step**, defer the
  flip-ON to a later step conditioned on (A) or (B). Banks the integration code without shipping
  a behavior change.
- **(D) Accept the trade and flip anyway** — **not recommended**: it ships a net-negative key
  change on non-chorale repertoire (and the regression is on exactly the kind of scores the
  pipeline must also serve), contradicting "max correct inferring."

**CC recommendation: (A) or (C).** The win is real and in-scope-verified; the only defect is
applying it out-of-scope. Do not ship a global flip-ON until the out-of-scope key axis is at
least non-regressing. **Awaiting Cowork source-verification of this adjudication (the 11
verdicts + the 3 regressions at the GT files) and the user's choice of A/B/C.**

---

## 7. Reproduction
```
# flag-OFF baseline (byte-identical):
cd ninja_build_rel && ./pipeline_snapshot_tests.exe                       # 11/11
# wiring-ON regen (overwrites goldens — restore with: git checkout -- <snapshots dir>):
MUSE_JOINT_KEY_WIRING=1 ./pipeline_snapshot_tests.exe --update-goldens
# ground truth:
#   Bach chorales : tools/dcml/when_in_rome/Corpus/Early_Choral/Bach,_Johann_Sebastian/Chorales/{001,003,134}/analysis.txt
#   non-Bach      : tools/dcml/<corpus>/harmonies/<stem>.harmonies.tsv  (globalkey / localkey)
#   chopin op30-1 : keysig -3 in tools/dcml/chopin_mazurkas/MS3/BI105-1op30-1.mscx (no harmonies.tsv)
```

**HELD — no commit, no flip, goldens restored. Cowork verifies the adjudication at source; the
user chooses the path forward.**

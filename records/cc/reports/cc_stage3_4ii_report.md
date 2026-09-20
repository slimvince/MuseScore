# CC Stage 3.4-ii — C1 Gate Removal, Gated on a Non-Chorale Spot-Check

**Date:** 2026-06-13 · **Base:** `a652dc1ba7` (Stage 3.4-i complete) · **Owner:** CC
**Instruction:** retire the C1 "dead-in-practice" set (E / F / K / Iter 86) **only** where a
deliberately gate-favorable non-chorale spot-check confirms the chorale-corpus 0s — "dead on
chorales is not dead." Method A–H; held means held.

## Headline

**Zero gates were retired.** The spot-check + a byte-level (not winner-level) corpus proof gate
together falsified the C1 "dead" verdict for **all four** gates:

- **K** and **Iter 86** change real **winners** on classical/romantic repertoire (Chopin
  op24-4, Mozart K310-1, etc.) — alive, kept as C2 3.2-acceptance.
- **F** executes **winner-neutrally** (redundant with the bias correction) on Mozart K283-3 —
  not byte-identical to remove, kept as C2′ (alternatives-hygiene).
- **E**, the one gate that looked removable after the spot-check (0 winner changes anywhere),
  was caught by the **byte-level corpus proof gate**: removing it changes the `.ours.json`
  alternatives list on **2 Baroque chorales (bwv245.3, bwv336)** — winner-neutrally, but not
  byte-identically. Per the stop condition this is "the spot-check missed a chorale-corpus
  fire," so the removal was **reverted** and E reclassified C2′.

**A methodology finding for 3.4-i (load-bearing):** 3.4-i §3 measured each gate's footprint as
**per-region WINNER changes** and reported E/F/K/Iter 86 as 0 Baroque regions. That metric is
**blind to winner-neutral alternatives-list changes.** The stricter `.ours.json` **sha256**
comparison used here (the 3.4-i proof-gate standard) catches them: E and F both alter the
alternatives list without moving a winner. The two "C1 dead-in-practice" sub-claims that rested
on the winner-diff (**E, F**) do not survive the byte-level test. **K and Iter 86 were never
truly C1** — they change winners outright on non-chorale repertoire. Net: the C1 set is **empty**.

The tree is byte-identical to `a652dc1ba7`; **no commit was created**.

---

## §1 — The spot-check: selection, inertness, measurement, DCML sample

### 1a. Selection rationale (per gate — NOT random)

20 non-chorale movements chosen to stack each gate's target sonority. The DCML MS3 sets load in
`batch_analyze` exactly as the snapshot harness loads `.mscx` (no obstacle).

| Corpus | Movements | Chosen to exercise |
|---|---|---|
| **Mozart piano sonatas** (8) | K283-1, K283-3, K310-1, K331-1, K457-1, K545-1, K333-1, K570-1 | **E** (galant I6/IV6 first-inversion major triads over stepwise bass), **F** (cadential 6/4), **Iter 86** (Alberti V4/2, ♭7-in-bass dominants); minor-key K310-1/K457-1 add **K** (chromatic dim/aug). |
| **Chopin mazurkas** (5) | BI77-4op17-4, BI168op68-4, BI105-4op30-4, BI89-4op24-4, BI145-3op50-3 | **K** (the genre's most chromatic / augmented-rich members — literal augmented sonorities chorales never voice), with chromatic stepwise inner voices for **E/F**. |
| **Beethoven string quartets (ABC)** (3) | n01op18-1_02, n06op18-6_02, n04op18-4_02 | **K** + **E/F** — chromatic slow movements with augmented-sixth context; op18-4 fugato for **E/Iter 86**. Capped at 3 (≈15 s/movement). |
| **Corelli trio sonatas** (4) | op01n01a, op01n02a, op01n08d, op01n10a | **E** (7–6 suspension chains → first-inversions), **F** (church-sonata cadential 6/4), **Iter 86** (continuo ♭7-in-bass V4/2). |

E/F are preset-gated on `preferMinorOverMajorAdd6` (Baroque/Standard only); K and Iter 86 are
not preset-gated. Baseline + measurement captured for all three configs **{Baroque, Jazz,
Default}**.

### 1b. Harness and inertness

The 3.4-i env harness was re-added (`gateDisabled(id)` reading `MS_DRYRUN_DISABLE_GATE`, a
comma-separated token list; unset → `getenv()==nullptr` → `false`; `&& !gateDisabled("E"|"F"|"K"
|"Iter86")` conjuncts on the four entry conditions) and **fully reverted afterward**.

**Inertness (measured):** env-unset on the harness binary vs the `a652dc1ba7` (pre-harness)
binary over the full 60-file spot-check set = **0/60 byte diffs**. The conjuncts do not alter
the enabled path.

### 1c. Measurement — all-four-disabled vs baseline, then per-gate attribution

`MS_DRYRUN_DISABLE_GATE=E,F,K,Iter86` vs baseline over 60 files (3 configs × 20 movements):
**8/60 (score,preset) differ** at the byte level. Per-gate single-disable attribution:

| Gate | Fires on (spot-check, byte-level) | Nature of change |
|---|---|---|
| **E** | **NOWHERE** (0/60) | — (see §2 / the corpus finding — E is *not* dead, just dead on this non-chorale set). |
| **F** | K283-3 (Baroque) | **Winner-neutral** — only the displaced candidate's alternatives-list score (−0.70 = bias deduction) and the margin change. |
| **K** | BI89-4op24-4 (Baroque, Jazz, Default) + K333-1 (Jazz) | **Winner changes** (augmented-inversion swap, segmentation-cascade-mediated). |
| **Iter 86** | K310-1 (Baroque, Jazz, Default) | **Winner changes** (♭7 stamp → cascade). |

The dossier's C1 caveat was vindicated: "0 on chorales" reflected the chorale repertoire's
absence of literal augmented triads / ♭7-in-bass sevenths / first-inversion-major-over-stepwise
shapes, not a dead gate.

### 1d. The Gate F finding (fires, but winner-neutral)

On its sole spot-check region — **Mozart K283-3 m71 b2.25 (Baroque)** — the committed winner is
`Dadd9/A` (V(add9)6/4) **with F on or off**. With F enabled, F directly swaps the 6/4 reading to
`results[0]` and sets `didEnharmonicFlip`, skipping the bias deduction; with F disabled, the bias
correction deducts 0.70 from the bass-root `Aadd11` and re-sorts to the **same** winner. Net:
identical winner; only the displaced `Aadd11` alternatives score (2.5435 → 1.8435) and the margin
(−0.078 → +0.138) change. **F is redundant with the bias correction here** → its true retirement
is a *fold into the bias correction* / alternatives-ordering re-decide (dossier §4 F4/F6), not a
byte-identical delete. Kept.

### 1e. DCML verdict on a sample of fires

- **Iter 86 — K310-1 m61 b3 (A minor, local v→i):** DCML `#viio7` = D♯o7 (root pc 3, dim7,
  leading-tone seventh of the local dominant). Iter 86 **enabled → `Ebdim` (root pc 3)** — root
  + diminished agree with DCML; **disabled → `B7` (root pc 11)** — wrong root. **Iter 86's fire
  is DCML-correct** (disabling it regresses the root). (We emit a plain Diminished where DCML has
  the full o7; the BIR-relevant *root* axis is right.)
- **Gate K — Chopin op24-4 m5 (B♭ minor):** DCML `V7(6♯2)` = F7 (root pc 5). K-**disabled** →
  `F7♯5` (root pc 5 — correct root, augmented colouring consistent with the ♯-alteration);
  K-**enabled** → `Dbadd9/F` (root pc 1 — disagrees with DCML root). Here K-enabled is **worse**
  on the root axis, but the change is segmentation-cascade-mediated (matched-tick diff empty), so
  cascade-confounded.

The DCML sample is reported per instruction; it does not drive the fate (fate = fire/no-fire). It
is an honest 3.2 input: Iter 86's non-chorale fire is a *fix to reproduce*; K's is at best
root-neutral and possibly a *chromatic-romantic mis-fire to NOT import* — flagged in §4.

---

## §2 — Per-gate fate (and the corpus finding that decided E)

After the spot-check, only **E** had 0 winner changes anywhere and was carried into Task 2/3 as
the one removal candidate. The Task-3 **byte-level corpus A/B ×3** proof gate then ran:

| Preset | E-removed `.ours.json` sha256 vs `a652dc1ba7` baseline |
|---|---|
| Jazz | **0/353** (E is preset-gated off here — expected) |
| Default | **0/353** (E preset-gated off — expected) |
| **Baroque** | **2/353 — bwv245.3, bwv336** |

Determinism was confirmed (two E-removed Baroque regens byte-identical, 0/353), and the diff was
isolated to Gate E (rebuilt E-present binary; the 2 files differ E-present vs E-removed; the only
source delta is the Gate E block). **Region-winner diff on both = empty → Gate E is
winner-neutral on these 2 chorales** (alternatives-list / margin only — the same shape as Gate
F). Because Jazz and Default match the baseline perfectly (E does not run there), the baseline is
genuine and the 2-file Baroque diff is a **real, reproducible E effect**, not a stale baseline.

Per the stop condition — *"ANY diff = the gate was NOT dead = STOP, revert, reclassify"* — the
removal was **reverted**. Final fates:

| Gate | 3.4-i class | 3.4-ii result | **Fate** |
|---|---|---|---|
| **E** | C1 (would be C2) | Winner-neutral everywhere, but **alternatives-active on bwv245.3, bwv336 (Baroque)** → removal not byte-identical | **KEEP → C2′ (alternatives-hygiene).** Reclassify C1→C2′ in 3.4-i §5. |
| **F** | C1 (would be C2) | Winner-neutral on K283-3 (redundant w/ bias) | **KEEP → C2′ (alternatives-hygiene).** |
| **K** | C1 (would be C2) | **Winner changes** on Chopin op24-4 (×3) + K333-1 (Jazz) | **KEEP → C2 3.2-acceptance.** |
| **Iter 86** | C1 (would be C3) | **Winner changes** on Mozart K310-1 (×3); DCML-correct | **KEEP → C2 3.2-acceptance.** |

**The C1 "retire-now" set is empty.** No gate is byte-identical-dead.

---

## §3 — Proof-gate ledger (the Gate E removal attempt, then reverted)

The E removal was implemented (gate block → historical marker; 3 GateE pins deleted;
`scoring_model.md` §6 synced), built, and gated:

| Proof | Result |
|---|---|
| Build (composing + notation + snapshots + batch_analyze) | ✅ green (exit 0) |
| composing_tests (E removed) | ✅ 502/502 (505 − 3 deleted GateE pins) |
| notation_tests | ✅ 57/57 |
| pipeline_snapshot_tests | ✅ 11/11 zero-diff, 0 FAILED |
| **Corpus A/B Baroque sha256** | ❌ **2/353 (bwv245.3, bwv336)** → STOP |
| Corpus A/B Jazz / Default sha256 | 0/353 / 0/353 |

**Outcome:** STOP-condition hit on Baroque. Removal **reverted** (`git checkout` of
`chordanalyzer.cpp`, `postscoringgates_tests.cpp`, `scoring_model.md`); E-present binary rebuilt;
Baroque corpus regenerated and re-verified **0/353 vs baseline**; **composing 505/505** restored;
source tree clean. **No commit was created** (held means held; and there is nothing to commit —
the correct action was to keep the gate).

---

## §4 — Updated C2 set for 3.2

The C1 retire-now menu (3.4-i §5(A)) is **empty**. All four former-C1 gates join the C2/C2′
acceptance roster with measured firing cases:

| Gate | What the wider beam must reproduce | Measured firing case (3.4-ii) |
|---|---|---|
| **I** *(highest stakes)* | 5 Jazz 1st-inv-Major fixes + Δ=+7b first-inversion (coupled w/ Gate R) | (unchanged from 3.4-i) |
| **bias correction** | the 8-snapshot Baroque inversion structure via proper inversion edges | (unchanged from 3.4-i) |
| **K** *(C2)* | augmented-first-inversion swaps on chromatic repertoire | Chopin op24-4 (×3), K333-1 (Jazz). **Caution:** the sampled fire is root-neutral/worse vs DCML — reproduce K's Baroque-target behavior without importing its chromatic-romantic mis-fires. |
| **Iter 86** *(C2)* | ♭7-in-bass third-inversion seventh stamps | Mozart K310-1 (×3); DCML-correct (`#viio7` root reproduced). |
| **L** | the 18 Jazz tie-breaks | (unchanged; 0 spot-check fires) |
| **E** *(C2′ alternatives-hygiene)* | winner-neutral alternatives change on bwv245.3, bwv336 (Baroque) — reproduced once the decoder owns the per-node alternatives list | bwv245.3, bwv336 (Baroque) |
| **F** *(C2′ alternatives-hygiene)* | fold into the bias correction (alternatives ordering) | K283-3 m71 (Baroque) |
| **H**, **Iter 91** | near-dead forward edges | (unchanged; 0 spot-check fires) |

**Gates remaining for 3.2 after 3.4-ii:** I, bias, K, Iter 86, L, E (C2′), F (C2′), H, Iter 91 —
plus the C4 functional set (A, G-family) and C5 keeper (J) deferred to Stage 6. **No identity-
mutating gate was removed from the beam-widening path.** E and F are the two "alternatives-list
hygiene" re-decides the decoder's output-assembly subsumes for free (dossier §4 F6): they change
no winner, only the emitted alternatives ordering/scores.

---

## §5 — Process / caveats / corrections

1. **3.4-i §3 metric correction (the substantive finding).** The per-gate differential measured
   **winner-region** changes; it is blind to winner-neutral **alternatives-list** changes. E and
   F both have winner-neutral alternatives effects (E on bwv245.3/bwv336 Baroque; F on K283-3),
   so their "0 Baroque regions / C1 dead-in-practice" rows in 3.4-i are **incorrect at the
   byte-level standard the proof gate uses.** Recommend the 3.4-i dossier §3 table footnote and
   §5(A) be amended (see the dossier addendum). The byte-level `.ours.json` sha256 is the
   authoritative deadness test — not the winner-region diff.
2. **Held means held.** No commit was created. The working tree is `a652dc1ba7` byte-identical
   for all tracked source; the only new artifact is this report (untracked).
3. **Cascade caveat (dossier §6.1)** applies to K/Iter 86 attribution: their non-chorale fires
   manifest mostly as segmentation-boundary shifts, so changed-region counts are footprint upper
   bounds. The load-bearing facts are binary (winner changes: yes) and the matched-tick DCML
   samples.
4. **Spot-check scope.** 20 movements / 4 non-chorale corpora is a deliberate, not exhaustive,
   probe — sufficient to *falsify* "dead" (one fire suffices), not to prove deadness beyond the
   set. Combined with the byte-level corpus gate, it falsified all four C1 verdicts.
5. **Restoration verified:** Baroque/Jazz/Default corpora 0/353 vs baseline; source tree clean;
   composing 505/505, notation 57/57, snapshots 11/11 (a652dc1ba7 state).
</content>

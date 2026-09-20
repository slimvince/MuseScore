# CC Report — Stage 4 Design (key as a path)

*CC, 2026-06-13. Base `f8c6b3932a` (working tree otherwise clean). Deliverable:
`docs/key_path_design.md` (HELD — `git add` ok, **not** committed, awaiting ratification).
This report = the probe record + the load-bearing §3 derivation + section map + open questions
+ unknowns. Read-only investigation; the only repo writes are the design doc and this report.*

---

## §1 — Probes and the §3 S2 derivation (the load-bearing part)

**Probe:** `/c/tmp/s2_derive.py` (throwaway, untracked). Reuses VERBATIM `compare_analyses`
(`load_analysis`, `align_dcml_regions` time-overlap), `compare_rn.classify_pair` (the bucket
metric), and `dcml_parser` (`find_wir_file`, `parse_rntxt_file` — the Bach WiR reference). It
reads the per-region `key` / `keyConfidence` / `keyModeRunnerUp` straight from the committed
`.ours.json`. Margins are estimated by inverting the committed confidence sigmoid (midpoint 2.0,
steepness 1.5 [code `keymodeanalyzer.cpp:736`]) — reported as `gap~`, with the hysteresis caveat
that `promoteWinnerInPlace` does **not** recompute confidence (so `gap~` is reliable in steady
state, noisy where a hysteresis promotion fired; §1.3).

**Corpus:** `tools/corpus/default` (the live config), 326 WiR-covered Bach chorales, 10 108
matched regions. S2 = 1 032 (10.2%) — **reproduces the dossier's number exactly** [probe].

### 1.1 The headline split (corpus-wide, robust signals, no margin dependence)

```
S2 = 1032 regions (key_disagree, our key != DCML global)
  our key is RELATIVE major/minor of DCML global:        509  (49.3%)   [the rest are fifth/modal]
  in a stem whose key NEVER changes (consistent error):  153  (14.8%)   [no transition exists]
  DCML global key present as our region runner-up:        499  (48.4%)   [rank-2 reachable]

mechanism split (stem-correct-fraction x relative-pair):
  deviation     rel    :   77  (7.5%)
  deviation     nonrel :   29  (2.8%)
  mostly-wrong  rel    :  432  (41.9%)
  mostly-wrong  nonrel :  494  (47.9%)
  --> path-fixable (local deviation in a mostly-right stem):   106  (10.3%)
  --> NOT path-fixable by transitions alone (mostly-wrong):    926  (89.7%)
```

### 1.2 The derivation (the instruction's central question, answered with real margins)

The instruction's hypothesis: *a per-window scorer flips a↔C on local evidence; a path with a
modulation penalty resists the flip.* **It holds for ~10% of S2 and fails for the rest.** Three
sub-mechanisms, each grounded in a real per-region trace:

| Class | Case | Trace finding | Path verdict |
|---|---|---|---|
| **A — spurious flip** | `bwv16.6` (a minor) | Amin→**Cmaj** for ~18 mid regions then back; runner-up = **Amin every flipped region**; winner-over-runner-up margin **0.01–0.20** | **FIXES** — `λ_rel≈0.3 > 0.20` holds a minor |
| | `bwv420` (a minor) | correct `Aharm` ×17 then thin-margin flip to `Cmaj` (gap~ 0.01–0.12), runner-up Amin | **FIXES** |
| **B — consistent error** | `bwv244.54` (**F major**) | `Dmin` on **all 29 regions** (relative minor of F); correct key **F is NEVER rank-2**; margin favoring wrong Dmin = **2.0–3.3** | **does NOT fix** — no flip; correct key unreachable; a penalty *entrenches* Dmin |
| **C — hysteresis trap** | `bwv343` (g minor, read as **D** minor — *non-relative*) | `Dmin` ×25 then GDor; runner-up = GDor throughout; early gap~ 2.3–2.5 (Class-B), **late gap~ −0.7…−1.0** (GDor genuinely wins but greedy hysteresis holds Dmin) | **FIXES the late tail** (global decode isn't trapped); early half is Class-B, unfixable |

**Mechanistic conclusion:** the modulation penalty's only power is *stickiness*. Stickiness helps
when the path is mostly right and occasionally flips wrong (Class A, 10.3%). When the **emission**
is consistently wrong (Class B, the ~80–85% bulk), stickiness is neutral-to-**counterproductive** —
it adds cost to ever leaving the wrong key. This is the same shape as the shelved beam-widening
result: *path/search cannot move an error the emission consistently prefers.*

### 1.3 Caveats on the probe (stated, not buried)

- `gap~` (sigmoid-inverted `keyConfidence`) is the **winner-vs-runner-up** margin **only when no
  hysteresis promotion fired** that window. Where it did (Class C late tails), `keyConfidence`
  carries the promoted candidate's *old* local-gap confidence (the documented Stage-1c wart), so
  `gap~` there is indicative, not exact. The **structural** finding (§1.1) uses only the `key` /
  `runnerUp` / DCML `local`/`global` columns and is wart-independent.
- The "deviation vs mostly-wrong" cut (stem-correct-fraction ≥/< 0.5) is a **robust-signal proxy**,
  not a per-case causal classification. It can over-count "mostly-wrong" in heavily-modulating
  stems (DCML local ≠ global on 39.9% of regions [probe]). The **153 single-key stems (14.8%)** are
  the wart-free, proxy-free floor of the unfixable-by-transition class.
- True per-window 252-candidate emission margins (vs the inverted-sigmoid proxy) need a
  `batch_analyze` key-dump flag — a **Stage-4-build** probe, deliberately not built here. The §1.2
  verdict does not depend on it: the decisive Class-B fact (correct key **not even rank-2**,
  bwv244.54) comes from the reliably-serialized `keyModeRunnerUp`, not from margins.

---

## §2 — Section map + the three most load-bearing claims

**Design doc `docs/key_path_design.md` — section map:**

| § | Content |
|---|---|
| §0 | TL;DR table |
| §1 | Scope: S2 measured; fixes (Class A/C) vs enables (S1 via KeyArea) vs must-not-regress (81978321e3, piece-start, BIR) |
| §2 | The HMM concretely — states/emission/transition/decode; window unit; top-N emission; weights deferred to Stage 5 |
| §3 | **The S2 derivation** (the §1 above, in the doc) |
| §4 | KeyArea struct + the tonicization-vs-modulation interface stub for Stage 6 |
| §5 | Reuse map (analyzeKeyMode REUSE; hysteresis/promoteWinnerInPlace/normalizedConfidence REPLACED) |
| §6 | Step-3 shelving reconciliation |
| §7 | Measurement on the L1 rung (`--key-breakdown`, DCML-only, granularity-robust, both corpora) |
| §8 | Single-path / config / decode-once / cost |
| §9 | Sub-steps 4.0–4.x, risks, rollback |
| §10 | Open questions (forks) |

**Three most load-bearing claims, with evidence:**

1. **"The path fixes ~10%, not ~100%, of S2."** *Evidence:* §1.2/§1.1 [probe] — 10.3% deviation-in-
   mostly-right-stem; 89.7% mostly-wrong; 14.8% single-key floor; bwv244.54 correct key never rank-2
   with 2.0–3.3 margins. *Consequence:* Stage 4 reframed from "the S2 fix" to "Class A/C fix +
   KeyArea + hysteresis supersession," with the Class-B bulk routed to an emission fix
   (partial-signature broadening / Stage-5 profile). This is the stop-condition finding, reported.

2. **"analyzeKeyMode is a clean emission model; the resolver's per-region argmax+hysteresis is the
   replaceable part — no falsification on read."** *Evidence:* [code] `keymodeanalyzer.cpp:564`
   computes all 252 `eval.score`; `keyresolver.cpp:311–321` is the hysteresis + `promoteWinnerInPlace`
   the decode replaces; `regionanalyzer.cpp:418–421` is the per-window `.front()` consumption.
   *One refinement (not a falsification):* the resolver surfaces only **top-3 family-selected**, so
   the HMM needs top-N **raw** scores exposed (§2.3 of the doc) — additive change.

3. **"A key change is also a chord-axis change, so Stage 4 ends the byte-identity era."** *Evidence:*
   [code] `regionanalyzer.cpp:453` — the resolved `localKeyFifths/Mode` feed `analyzeChord`
   directly; key freezes into `cell.basisIndep` via `snapshot.keyTonicPc/scale` [doc, Step-3].
   *Consequence:* Stage 4's behavior-change A/B (sub-step 4.1-measure) must gate Baroque BIR +
   pipeline snapshots and DCML-adjudicate any movement, exactly as a 3.2-class change.

---

## §3 — Open questions (inline; full forms in design §10)

- **OQ-1 — co-ratify Stage 4 `λ` with the Stage-6 label contract.** `λ` sets KeyArea granularity,
  which *is* the tonicization-vs-modulation boundary Stage 6 reads. *Rec: yes, one decision surface.*
- **OQ-2 — Class B routing (the §3 fork).** Path-only (route Class B to Stage 5) vs bundle the
  partial-signature/key-profile emission work into Stage 4. *Rec: bundle the partial-signature
  detector (Baroque-structural, not a fitted weight); leave the relative-pair profile to Stage 5.*
- **OQ-3 — KeyArea confidence:** best-path-minus-best-alternative-key-path (cheap, decode-native) vs
  forward-backward posterior (textbook, costlier). *Rec: the former unless Stage 6 needs calibrated p.*
- **OQ-4 — emission top-N:** top-3 / top-8 / full-252. 51.6% of S2 has the correct key outside rank-2,
  so top-3 caps reachable S2 — but widening N only helps Class A. *Rec: top-8; full-252 only on a
  measured need (beam-revisit discipline).*

---

## §4 — Unknowns / what I could not measure cheaply

1. **True 252-candidate per-window emission margins.** Used the inverted-sigmoid `gap~` proxy
   (hysteresis-contaminated where promotion fired). A clean read needs a `batch_analyze` key-dump
   flag (Stage-4 build). The §3 verdict stands without it (rests on runner-up identity + the 153
   single-key floor, both wart-free).
2. **Non-Bach S2 structure.** §3 is measured on Bach (the only WiR-covered, homophonic gate set).
   Cross-corpus key error is ~2× harder (root_err 50.7% vs 26.8% [doc]); whether its S2 is similarly
   ~90% consistent-emission is **unknown** — a Stage-4-measure task once the path A/B runs there.
3. **Exact Class-A vs Class-C sizing.** Class C (hysteresis traps) is mechanism-confirmed (bwv343
   tail) but not separately counted — it overlaps the "deviation" bin and the late-tail of some
   "mostly-wrong" stems. Bounded above by the 10.3% deviation class plus the late-switch tails;
   not pinned to an integer (would need a per-stem switch-point detector).
4. **The provisional `λ` direction.** Whether a plausible `λ` actually nets S2 ↓ on Class A without
   netting S2 ↑ on Class B (over-entrenchment) is the **decision-point A/B** (design sub-step
   4.1-measure) — not run here (it requires the flagged decode, i.e. production code, which this
   design-only task does not build).
5. **`is_relative` / stem-fraction proxy precision.** Robust-signal proxies, not per-case causal
   reads; the 153-single-key floor and the bwv244.54/343 traces are the proxy-free anchors.

---

## Stop-condition disclosures (per the instruction)

- **The §3 derivation shows the path does NOT fix the S2 bulk** — reported as the primary finding
  (§1.2). It reshapes Stage 4's value (path = ~10% Class A/C + KeyArea + hysteresis fix; the ~85%
  Class-B bulk needs an emission fix), the way the beam finding reshaped 3.2. Stage 4 is **not**
  cancelled — KeyArea (the S1/Stage-6 enabler) and the hysteresis supersession are independent of
  S2 shrink — but its headline is corrected from "the S2 fix" to "the scaffold + the flip fix."
- **No reuse assumption about `KeyModeAnalyzer`/`resolveKeyAndModeRanked` proved false on read.**
  One refinement surfaced (top-N raw emission exposure vs today's top-3 family-selected, §2.3); it is
  additive, not a rebuild. Reported because it changes the 4.0 sub-step, not the build/reuse split.
- **No scope creep:** Stage 6 functional labeling is left at the KeyArea **interface stub** (§4.2);
  Stage 5 weight numbers are left at the transition **structure** (§2.1/§2.4, numbers deferred).

*Design doc `docs/key_path_design.md` is HELD (uncommitted) pending the ratification addendum.*

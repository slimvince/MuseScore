# cc_e0prime_report.md — E0′: the capped/affected-measure re-run after the L4→L5 carry-fix + D-L5a squash

> **HELD for Cowork** (gitignored). Read-only measurement, byte-identical to production.
> Executes `cc_instruction_carryfix_dl5a_e0prime.md` Task 3 + the Cowork Task-2 ruling addendum (2026-07-02).
> Re-runs ONLY the measures the two dormant commits could move; everything else is E0-frozen.

## 0. Provenance

- **Commits under test (local, unpushed):**
  - `4b3d054d89` — `feat(chord): L4->L5 carry-fix — carry ChordIdentity extensions + naturalFifthPresent` (Task 1).
  - `0a88747e7f` — `feat(function): D-L5a — publish FunctionConfidence.combinedBoundary [0,1) squash` (Task 2).
- **Gate (flag OFF):** BIR case-identity **53 / 24 / 53** — re-measured EXACT (count exact on all three; the enumerated
  delta-subgroups are a clean subset of the CLAUDE.md sets with **zero additions**; the sole production change is the
  byte-identical `extensionBits` refactor, so the flag-OFF `.ours.json` corpus is byte-identical by construction).
- **Suites:** composing **995** (990 + 5 new carry/boundary tests) / notation **53** / pipeline_snapshot **11/11 — NO
  golden refresh** (P1–P4 byte-identical) / `test_batch_analyze_regressions.py` passed.
- **Grep-proof (zero production reach):** `deriveChordExtensions` is called only by the dormant decoder + tests;
  `ChordSliceDecoder` has no production caller; the carry fields touch only chordanalyzer/chordslicedecoder (dormant),
  the tests, and the `--dump-fullspine` harness. functionoutput/resolver/modulation are dormant (no production consumer).
- **Corpora:** fullspine regenerated 352/352 per preset with the two-commit binary; legacy = the flag-OFF 53/24/53
  corpus. 326 stems carry a When-in-Rome analysis (the RN/root/key denominator).

---

## 1. §1 — the HEADLINE: #1 RAW full-RN + EXACT levels (the cap did NOT close) + triad/root controls

| Preset | stream | root_agree | robust(dur) | TRIAD-exact | RAW-exact | cap (triad−raw, EXACT) | E0 cap |
|---|---|---|---|---|---|---|---|
| Baroque | **chain** | 54.1% | 36.2% | 28.9% | 20.7% | **+8.2 pts** | +7.9 |
| Jazz | **chain** | 54.2% | 35.6% | 28.7% | 20.5% | **+8.2 pts** | +7.8 |
| Default | **chain** | 54.2% | 36.2% | 28.9% | 20.7% | **+8.2 pts** | +7.9 |

**The controls are UNCHANGED vs E0 → no scope leak (no STOP):** root_agree 54.1% (E0 54.1%), TRIAD-exact 28.9%
(E0 28.9%). The Task-1 change did NOT move root or triad on any preset. ✅ (STOP condition "any control-level movement
in #1" is NOT triggered.)

**But the cap did NOT close — the predicted +7.8/+7.9 EXACT recovery did NOT materialize.** RAW-exact is **20.7%**
(E0 21.0%) — essentially unchanged; the cap is **+8.2 pts** (E0 +7.9), i.e. the EXACT RN did **not** absorb the carried
seventh. **This is the report's principal finding, and its cause is a SECOND, L5-internal carry gap** (see §6). It is a
*negative result*, not a regression or a control movement.

## 2. §7 — relational labels: V7/x now FIRES (was structurally impossible), Ger+6 = 0

| Preset | chain-EMITTED V7/x | DCML V7/x occ. (ceiling) | Ger+6 emitted | DCML Ger+6 | AppliedSecondary role total | ModalMixture |
|---|---|---|---|---|---|---|
| Baroque | **36** | 316 | 0 | 0 | 684 | 1318 |
| Jazz | **34** | 316 | 0 | 0 | 622 | 1184 |
| Default | **35** | 316 | 0 | 0 | ~666 | 1262 |

- **The carry-fix makes `V7/x` firable at all** — E0 measured it **structurally NON-firable (0)** because the seventh was
  dropped at the projection; now the chain emits **36 / 34 / 35** figured applied-dominant labels (e.g. `V7/V`
  `bwv140.7@8400`, `V7/ii` `bwv159.5@16560`, `V7/iv` `bwv229.2@26160`, `V7/VII` `bwv144.6@23280`). This is the direct,
  visible effect of Task 1 — the seventh reaches `formatRomanNumeral` on the readings that carry it.
- **But only ~36 of the 316 addressable DCML V7/x fire** (~11%) — the same L5-internal gap as §1 caps the rest: the
  resolver reconstructs most readings *bare* (§6), so their applied labels stay triad-level (`V/x`).
- **Ger+6 = 0 emitted, DCML Ger+6 = 0** — correct: there are no German sixths in the Bach chorale corpus, so nothing to
  fire (the aug6 nationality read is now *wired* through `naturalFifthPresent`, but the corpus never exercises it). The
  1 `AugmentedSixth` that fires is the It/Fr+6 notated-spelling path, unchanged from E0.

## 3. §9 — the L5 boundary form (D-L5a) + the D-FS frame-scale rider

| Preset | l5CombinedBoundary min / med / max | l5Combined (internal, x-check) max | §5.5 contradiction (fired) min/med/max (n) | §5.4 cadentialWeight min/med/max (n) |
|---|---|---|---|---|
| Baroque | 0.0000 / 0.5000 / **0.9619** | 25.25 | 2.0 / 2.0 / 3.0 (n=1051) | 3.35 / 5.85 / 9.35 (n=60) |
| Jazz | 0.0000 / 0.5000 / **0.9619** | 25.25 | 2.0 / 2.0 / 3.0 (n=1041) | 3.35 / 5.85 / 9.35 (n=59) |
| Default | 0.0000 / 0.5000 / **0.9619** | 25.25 | 2.0 / 2.0 / 3.0 (n=1051) | 3.35 / 5.85 / 9.35 (n=60) |

- **combinedBoundary ∈ [0, 0.9619] ⊂ [0,1)** on the full E0-observed range — the D-L5a squash behaves exactly as
  specified: it maps the internal additive `combined` (unchanged, max 25.25, confirming the D-L5a premise) monotonically
  into [0,1), with the max 25.25 → 25.25/26.25 = **0.9619**. U2 satisfied. ✅
- **D-FS rider (Stage-5 frame-scale evidence).** The two §8 contradiction quantities, measured *as they fire*, are on
  **very different scales** from each other AND from the [0,1) boundary form — the exact incommensurability the contract
  §4/§6 flags for θ-calibration: the §5.5 fine-grain contradiction (plausibility-diff) sits at **2–3**, while the §5.4
  cadential weight sits at **3.35–9.35**. Neither is [0,1]; both are compared against bounded incumbents (L4 composite /
  L3 key) today. This is banked evidence, not acted on (no θ this run).

## 4. Honest-carry telemetry (Task 1.2 — "REPORT which case occurred")

| Preset | decoder alt ExtKnown | decoder alt ExtUnknown (honest-carry) | finalReading ExtKnown | finalReading ExtUnknown |
|---|---|---|---|---|
| Baroque | 26,521 (14.1%) | 161,515 (85.9%) | 7,103 | 16,284 |
| Jazz | 26,511 | 161,599 | 7,047 | 16,196 |
| Default | 26,521 | 161,515 | 7,079 | 16,288 |

- **The chosen committed chord is ALWAYS a full extraction** (`extensionsKnown` = true) — guaranteed by
  `completeChosenExtensions` and locked by the end-to-end test `CarryFix_Dom7ChosenCarriesMinorSeventh`.
- **Carried ALTERNATIVES: ~14% obtainable, ~86% honest-carry.** As designed — `analyzeChord` returns only ≤4 ranked
  results (winning bass), so a cube-cell alternative matches one only ~1-in-7 of the time; the rest are honest-carry
  (`extensions=0`, `extensionsKnown=false` — unknown, never a guess). This is the "which case occurred" answer: the
  honest-carry path is the *common* case for alternatives, exactly as anticipated.
- **The `finalReading` split (7,103 known / 16,284 unknown) is the §6 finding surfacing** — it is NOT the decoder's
  chosen (which is 100% known); it is what `finalReadingOf` returns, i.e. the L5 resolver's *reconstructed* reading,
  which is bare for ~70% of chorded slices.

## 5. §6-6 rider — keyparse_fail spot-check (naming artifact vs genuine key error)

`keyparse_fail` = **855 chain vs 110 legacy** (unchanged from E0 — the key path is untouched by both commits, expected).
**Verdict: a key-NAMING artifact, NOT a genuine key error.** The chain's local-key path emits **mode-qualified** names —
**4,439 chain regions** carry a non-`maj`/`min` suffix: `Gharm`/`Aharm`/`Charm`/`Dharm`/`F#harm`/`Bharm`/`Bbharm`
(harmonic minor), `Dmel`/`Gmel` (melodic minor), `DDor`/`EDor`/`GDor` (Dorian), `EPhrygDom` (Phrygian-dominant). The
**tonic in every one is correct** (`Gharm` = G, `DDor` = D, `EPhrygDom` = E, …); it is the *string* the DCML key parser
(which expects `Xmaj`/`Xmin`) rejects → the parse fails and the region is counted `keyparse_fail`. Legacy emits only
`maj`/`min` names → 110. So the 745-case gap is **local-mode label parseability**, not key-inference quality. (A
grader-side name normalisation `harm/mel/Dor/… → min|maj` would dissolve most of it; out of scope here.)

## 6. ★ THE PRINCIPAL FINDING (declared to Cowork) — a SECOND, L5-INTERNAL carry gap re-drops the seventh

The Task-1 fix closes the **L4→L5 projection** gap: `decoded[i].chosen` now carries `extensions` +
`naturalFifthPresent` (verified: the chosen is 100% `extensionsKnown`; 36 `V7/x` now fire). **But the EXACT-RN cap did
not close, because a second gap, entirely INSIDE Layer 5, re-drops the extensions before the consumer reads them:**

- The L5 resolver operates on **`Progression` / `ProgressionChord`**, whose fields are **`{rootPc, quality}` ONLY**
  (`functionprogression.h:79-82`) — extensions (and bass) are dropped when the committed chain is projected into the
  resolver substrate.
- For a committed **pass-through** slice the resolver emits `r.reading = candidateFromProg(s.chord)`
  (`functionresolver.cpp:369`), and `candidateFromProg` (`:50-57`) reconstructs a **bare** `ChordSliceCandidate`
  (root + quality + bass=root; **no extensions, `extensionsKnown` defaults false**).
- The harness consumer builds the base-RN / relational identity from **`finalReadingOf(i)`**, which returns the
  resolver's `rr.reading` (bare) whenever it is set — so ~**70% of chorded readings (16,284 / 23,387)** reach
  `formatRomanNumeral` triad-level. The seventh survives only on the ~**7,103** slices where `finalReadingOf` falls
  through to `decoded[i].chosen` — which is exactly where the 36 `V7/x` come from.

**This is an architecture/carry problem, not an inference-tuning one, and not fixable inside E0′ (read-only).** It is
**declared, not coded** (per the standing rule). The fix belongs to Cowork's L5 design: the resolver substrate must
carry the committed chord's full identity forward (either `ProgressionChord`/`ProgressionSlice` gain the extension
identity, or `carryThrough`/`candidateFromProg` reference the decoder's `chosen` instead of reconstructing bare), after
which E0″ would re-measure whether the +8.2 EXACT cap finally closes. Task 1 is a **necessary prerequisite** for that
(the extensions now exist at the L4→L5 boundary); it is **not sufficient alone**.

*(Caveat: the E0-instruction's prediction that Task 1 would recover +7.8/+7.9 EXACT points assumed the base RN read the
carried chosen directly; it reads the resolver's reconstructed reading instead. The prediction is deferred to E0″, not
refuted — the mechanism is verified correct on the pass-through path.)*

## 7. §5 — updated better/worse rows (re-measured respects ONLY)

| Respect | E0 | E0′ (this run) | verdict |
|---|---|---|---|
| **RN** triad-normalized EXACT (control) | 28.9% | **28.9%** | unchanged (no leak) |
| Chord **root** (control) | 54.1% | **54.1%** | unchanged (no leak) |
| **RN** RAW-exact / cap | 21.0% / +7.9 | **20.7% / +8.2** | cap **NOT closed** (§6 second gap) |
| **#7 `V7/x` firable** | 0 (structural) | **36 / 34 / 35 emitted** | **BETTER** — now fires; capped by §6 |
| **#7 Ger+6** | 0 (structural) | 0 (corpus has none) | wired; unexercised in Bach |
| **#9 L5 boundary** (D-L5a) | combined unbounded (25.25) | **combinedBoundary ∈ [0, 0.9619] ⊂ [0,1)** | **CLOSED** — U2 satisfied |
| Honest-carry (alternatives) | — | ~14% known / ~86% honest-carry | as designed |

**Pre-read (NOT a G2 pass/fail claim):** Task 2 (D-L5a) is **fully realized and correct** — the boundary form is bounded
and monotone. Task 1 is **correct and necessary but its end-to-end EXACT-RN payoff is gated on a second L5-internal
carry gap (§6)** that must be closed before the cap moves; its *visible* win is the 36 `V7/x` labels that were
structurally impossible before. No control level moved (no scope leak). Byte-identity holds on production.

## 8. Byte-identity argument (Task-3 close)

No additional flag-OFF regen was required beyond the Task-1 gate run: the only production-reachable change is the
byte-identical `extensionBits` refactor of `buildChordResult` (confirmed by 995 composing tests + 11/11 snapshot goldens
with no refresh + BIR 53/24/53 exact); Task 2's functionoutput/resolver/modulation are dormant (no production caller,
grep-proof) and the snapshot goldens are unchanged after the Task-2 build. Therefore the flag-OFF `.ours.json` corpus is
byte-identical with both commits in, and the 53/24/53 gate stands.

---

*Report line count (this file): **161 lines**.*

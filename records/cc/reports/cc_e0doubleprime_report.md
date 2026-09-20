# cc_e0doubleprime_report.md — E0″: the re-measure after carry-fix 2 (resolver identity carry) + grader key-name fairness

> **HELD for Cowork** (gitignored). Read-only measurement, byte-identical to production.
> Executes `cc_instruction_carryfix2_resolver_identity.md` Task 3. Re-runs the capped/affected measures after the two
> dormant/tool-only changes; everything structural is E0/E0′-frozen (and re-measured identical, confirming
> decision-invariance).

## 0. Provenance

- **Changes under test (local, working tree — commits 1–2 of this dispatch):**
  - **Commit 1 (Task 1) — resolver identity carry.** `FunctionSlice` gains `chosen` (the committed full identity);
    `carryThrough` emits `s.chosen` VERBATIM (was `candidateFromProg(s.chord)` = bare root-position, no seventh);
    the override neighbour pool is built from `region[idx].chosen` (verbatim) not a reconstruction; `candidateFromProg`
    retired. Harness `batch_analyze.cpp` populates `fs.chosen = decoded[i].chosen`. Doc-sync L5 §5.5/§7.
  - **Commit 2 (Task 2) — grader key-name normalization (measurement fairness only).** `compare_rn._our_key_tonic`
    now normalizes mode-qualified local-key names (`Xharm`/`Xmel`/`XPhrygDom` → X-minor; `XDor` → its parent-signature
    minor at the same tonic — declared) to a (tonic, major/minor) identity so the key comparison scores key IDENTITY, not
    string parseability. **Production emits unchanged.**
- **Controls / STOP checks (all clear):**
  - **`root_agree` STRUCTURALLY INVARIANT (proven, not just measured).** Every `finalReadingOf` branch preserves
    `rootPc`: pass-through `s.chosen.rootPc == s.chord.rootPc == decoded[i].chosen.rootPc`; the abstain path is untouched;
    the override selects by `toPC` (root+quality), which is identical for `region[idx].chosen` vs the old
    `candidateFromProg(neighbourChord)`, so the SAME candidate is picked and its `rootPc` is the same either way. Measured
    root_agree 54.1 / 54.2 / 54.1 (Baroque/Jazz/Default) — unchanged. **No STOP.**
  - **Suites green:** composing **998** (995 + 3 new verbatim-carry tests) / notation **53** / pipeline_snapshot **11/11 —
    NO golden refresh** / grader unit tests **88** (+1 new mode-normalization test).
  - **Gate byte-identical — EMPIRICALLY CONFIRMED.** The flag-OFF standard corpus uses a SEPARATE emission block
    (`batch_analyze.cpp:2454`, `sc.chosen`); only the `--dump-fullspine` block (`:2985+`) reads `finalReadingOf`/`fs.chosen`.
    A full Baroque flag-OFF regen with the new binary diffs **0 / 352** `.ours.json` against the E0′ baseline → BIR
    **53 / 24 / 53** byte-identical by construction. No θ anywhere.
- **Corpora:** fullspine regenerated **352/352 per preset** with the new binary; legacy = the byte-identical flag-OFF
  corpus; 326 stems carry When-in-Rome GT (the RN/root/key denominator).

---

## 1. ★ THE HEADLINE — #1 RAW/EXACT + the cap: the cap did NOT close; it WIDENED (+8.2 → +9.8)

| Preset | stream | root_agree | robust(dur) | TRIAD-exact | RAW-exact | cap (triad−raw, EXACT) | E0′ cap |
|---|---|---|---|---|---|---|---|
| Baroque | chain | **54.1%** | **36.2%** | **28.9%** | 19.1% | **+9.8 pts** | +8.2 |
| Jazz | chain | **54.2%** | **35.6%** | 28.5% | 18.8% | **+9.7 pts** | +8.2 |
| Default | chain | **54.1%** | **36.2%** | **28.9%** | 19.1% | **+9.8 pts** | +8.2 |

**Controls (STOP checks):** `root_agree` 54.1/54.2/54.1 — unchanged (E0′ 54.1/54.2/54.2; the Default 0.1 is display
rounding — root is structurally invariant, §0). `robust` unchanged. `TRIAD-exact` unchanged on Baroque/Default (28.9);
Jazz moved **28.7 → 28.5** (−0.2) — attributed below, not a root/decision move. **No control STOP fired.**

**The deferred E0 prediction is REFUTED, not deferred again.** E0 predicted Task 1 would recover ≈+7.8/+7.9 EXACT points
(raw-exact rising toward triad-exact). Instead **RAW-exact FELL** (Baroque 20.7 → **19.1**), so the cap **widened** to
**+9.8**. The carry itself now demonstrably WORKS (§3: committed ExtKnown 30% → 72.5%; §2: V7/x 36 → 125). The EXACT cap
did not close because **it was never primarily a carry artifact** — it is a genuine Layer-4 chord-identity accuracy gap
vs DCML (seventh/extension over-detection + bass/inversion), and the prior bare-root-position flattening was **masking
part of it** (a bare `V` accidentally matches DCML's frequent root-position `V`). Carrying the committed identity verbatim
removes that accidental inflation — E0′'s raw-exact 20.7 was an **overcount**; 19.1 is the honest number.

## 2. #7 relational — V7/x MORE than tripled (36 → 125); over-trigger unchanged

| Preset | chain-EMITTED V7/x (RN string) | E0′ | DCML V7/x occ. (ceiling) | Ger+6 emitted | AppliedSecondary role | ModalMixture |
|---|---|---|---|---|---|---|
| Baroque | **125** | 36 | 316 | 0 | 691 | 1318 |
| Jazz | **117** | 34 | 316 | 2 | 622* | 1184 |
| Default | **122** | 35 | 316 | 0 | ~666 | 1262 |

- The verbatim carry pushes the seventh onto **all** committed/inherit pass-throughs (not just the ~7k that fell through
  to `decoded[i].chosen` in E0′), so `V7/x` now fires **125 / 117 / 122** (e.g. `V7/v` `bwv101.7@14400`, `V7/ii`
  `bwv104.6@9600`, `V7/V` `bwv140.7@8400`). This is the direct, visible win of Task 1 — well above the E0′ 36 and the
  original E0 structural-0. Still ~40% of the 316 DCML occurrences (the rest sit where the L4 root/key itself disagrees,
  not the carry).
- **Ger+6 = 0** (Baroque/Default; 2 on Jazz) — the nationality read is wired through `naturalFifthPresent`; the Bach
  corpus barely exercises it. Over-trigger (chain applied where DCML diatonic) 545 stems-worth — **unchanged from E0**
  (the override/applied *decisions* are identical; only the emitted figure is richer).

## 3. Carry telemetry — finalReading ExtKnown share jumped 30% → 72.5% (≈100% on committed/inherit)

| Preset | finalReading ExtKnown | finalReading ExtUnknown | ExtKnown share | E0′ share |
|---|---|---|---|---|
| Baroque | **16,955** | 6,432 | **72.5%** | 30.4% |
| Jazz | 16,831 | 6,412 | 72.4% | 30.2% |
| Default | 16,931 | 6,436 | 72.5% | 30.3% |

- **The residual ~27.5% unknown is NOT a pass-through leak — it is the resolved-ABSTAIN readings.** On the committed and
  inherit pass-throughs the share is **≈100%** (they emit `s.chosen`, always a full extraction). The 6,432 unknown are
  L4-abstains the resolver RESOLVED to a carried alternative that was **honest-carry** (`extensionsKnown=false` — the
  ~86% of alternatives that `analyzeChord`'s ≤4 ranked cells could not match, per the carry-fix-1 design). Those are
  honestly triad-level, never guessed. So the "≈100% on committed/inherit, report the residual" expectation is met, and
  the residual is exactly the honest-carry abstain resolutions.

## 4. ★ THE CAP DECOMPOSITION (why raw-exact fell) — seventh over-detection + bass/inversion, both L4

Over the matched pairs where the TRIAD RN agrees but the RAW RN differs (== exactly the EXACT-cap set), the disagreement
splits (Baroque; Jazz/Default near-identical):

| cap component | Baroque | share | representative cases (chain \| GT) |
|---|---|---|---|
| **seventh-presence** differs | 1,051 | 45% | `i7 \| i`, `iM9 \| i`, `V7 \| V`, `V(add11) \| V7`, `VIM7 \| VI`, `V \| V7` |
| **inversion-figure** differs | 984 | 42% | `iv \| iv6`, `i \| i6`, `V/iv \| V6/iv`, `I64 \| I` |
| both differ | 250 | 11% | — |
| other/unparsed figure | 46 | 2% | — |
| **total cap pairs** | **2,331** | | |

- **The seventh half is dominated by OVER-emission** — chain reads a seventh/upper extension where DCML reads a plain
  triad (`i7`, `iM9`, `V(add11)`, `VIM7`). The `iM9`/`(add11)`/`(add9)` cases are textbook **non-chord-tone
  over-detection** (a suspension 4–3 read as an 11th, a passing/neighbour tone read as a 9th/7th). This is L4's
  `deriveChordExtensions` extending onto NCTs — the exact gap the architecture review flagged as **F-9 (the NCT-filter
  L4 lever)**, now measured.
- **The inversion half is the committed bass disagreeing with DCML's figure** (`iv` vs `iv6`, `I64` vs `I`) — the
  Layer-2 segmentation / Layer-4 bass residual the **O1 caveat** (CLAUDE.md) already names as most of the non-functional
  remainder.
- **Both halves are Layer-4 chord-identity accuracy, faithfully surfaced by the correct carry — not a carry or a
  render bug** (spot-checked: `V7`/`iv6`/`I64` are correct figured-bass renders of the committed identity; the identity
  itself disagrees with DCML). **Declared to Cowork as an inference problem (L4 seventh/NCT + bass/inversion); not fixed
  here.**
- The Jazz TRIAD-exact −0.2 (§1) is the same phenomenon leaking one step further: `triad_norm` strips figured digits and
  `maj/M/Δ` but NOT the parenthetical `(add9)/(add11)`, so a spurious `V(add11)` misses even at triad level. A grader
  `triad_norm` refinement (strip `(add…)`) would remove it; out of scope here (it does not touch root/decision).

## 5. #2 KEY — re-run under Task 2's normalization (keyparse_fail 855 → 144), key measures now comparable

**keyparse_fail before/after (same corpus, old vs new parser — isolates Task 2):**

| Preset | matched pairs | keyparse_fail BEFORE (old maj/min-only) | AFTER (Task 2) | Δ |
|---|---|---|---|---|
| Baroque | 21,303 | **855** | **144** | −711 |
| Jazz | 21,182 | **2,524** | **186** | −2,338 |
| Default | 21,285 | **1,568** | **238** | −1,330 |

- Baroque BEFORE = **855**, matching the E0′ report exactly — confirming the key path is untouched by carry-fix 2 (the
  local-key strings are identical; only the grader's parser changed). The normalization dissolves the mode-label
  parse-failures (`Gharm`/`Dmel`/`DDor`/`EPhrygDom` → correct tonic + minor); the residual (144/186/238) is genuine
  (empty / non-`<letter><acc?><mode>` strings), the honest floor.
- **With parseability removed as a confound, `key_disagree` and its S1/S2 split are now comparable.** Post-normalization
  (from the grader): Baroque chain key_disagree **4,216** (S1 eq-global **3,190** / S2 ne-global **1,026**; keyfail 47) vs
  legacy 2,243 (S1 1,447 / S2 796). The chain's larger key_disagree is now legible as a **real** S1 tonicization-label
  gap (the local-key path reads local tonics DCML labels against the global key — the expected §5.3 behavior), not a
  string artifact. This is measurement fairness only; production key output is unchanged.

## 6. §9 — the D-L5a boundary form (unchanged, still correct)

`l5CombinedBoundary ∈ [0, 0.9619] ⊂ [0,1)` on all three presets (internal `combined` max 25.25 → 25.25/26.25 = 0.9619),
identical to E0′ — Task-2's commit is grader-only and Task-1 does not touch `functionoutput`. The §5.5 fine-grain
contradiction still fires at 2–3 (n≈1049) and §5.4 cadentialWeight at 3.35–9.35 (n≈60) — the Stage-5 frame-scale evidence,
banked, not acted on.

## 7. §5 — updated better/worse rows (re-measured respects only)

| Respect | E0′ | E0″ (this run) | verdict |
|---|---|---|---|
| Chord **root** (control) | 54.1% | **54.1%** | unchanged (structurally invariant) — no STOP |
| **RN** triad-normalized EXACT (control) | 28.9% | **28.9%** (Jazz 28.7→28.5) | unchanged (Jazz −0.2 = `(addN)` triad_norm leak, §4) |
| **RN** RAW-exact / cap | 20.7% / +8.2 | **19.1% / +9.8** | cap **WIDENED** — the E0 recovery prediction **REFUTED** (§1/§4) |
| **#7 `V7/x` emitted** | 36 | **125 / 117 / 122** | **BETTER** — 3.4× (the carry's visible win) |
| finalReading ExtKnown share | 30% | **72.5%** (≈100% committed/inherit) | **BETTER** — the carry now reaches the consumer (§3) |
| **#2 keyparse_fail** | 855 | **144** (Task 2) | **BETTER (fairness)** — key measures now comparable (§5) |
| **#9 L5 boundary** (D-L5a) | [0, 0.9619] | [0, 0.9619] | unchanged — still CLOSED |

**Pre-read (NOT a G2 pass/fail claim):** Task 1 is **correct, necessary, and now demonstrably wired end-to-end** (the
seventh + bass/inversion reach the formatter; V7/x tripled; ExtKnown ≈100% on the committed paths). But the EXACT-RN
payoff the E0 instruction predicted **does not exist to recover** — the cap is a **Layer-4 chord-identity accuracy** gap
(seventh/NCT over-detection ≈45% + bass/inversion ≈42%), not a carry drop, and the prior flattening was inflating
raw-exact by accident. **Declared to Cowork (inference problem, L4; ties to review F-9 NCT-filter + the O1 bass/inversion
caveat).** No control level moved (root structurally invariant), suites green, gate byte-identical, no θ. Byte-identity
holds on production.

---

*Report line count (this file): 166 lines.*

# CC Instruction — Phase 5 backfill round 2, cluster 4 of 4: L3 keymode (~72 upper-bound, oracle-asserted)

> **Why.** The **last** cluster of the stable-half branch backfill. Same rules as clusters 1–3 (`3f2e4bebe2`,
> `1218ad1003`, `45a89f49df`): **coverage is the gap-finder, NOT the goal**; each test asserts the **theory/contract-
> correct value (oracle), re-derived at source** — never an echo. A correct oracle that **fails** current code →
> `DISABLED_`/xfail + flag (surfaced defect). **Tests-only — no production change.** The `~72` is an **upper bound**
> (re-confirm class at source; skip provably-unreachable defensive).
> *(Reminder: the never-bash rule is Cowork's; it does not constrain your build/test/tool runs.)*

## §1 — The worklist (L3 keymode ADD-TEST branches)
Files + triage ADD-TEST counts (upper bounds): `key/keymodeformatting.cpp` (30), `key/keymodeanalyzer.cpp` (26),
`key/keymodesequence.cpp` (16).
- **Exact unhit locations:** grep `cc_union_branch_coverage_report.md` (§5) for each file.
- **Re-confirm class at source:** ADD-TEST vs EXCLUDE-DEFENSIVE (size/bounds clamps, exhaustive-enum `default:`,
  the documented broken-chain fallback, upstream-invariant guards → **skip**, Phase-6 seal).
- **★ The brittle leading-tone presence-gate (`keymodeanalyzer.cpp` ~347 / ~354) — pin as a LABELLED regression-guard,
  do NOT assert correct.** This is the known spec-flagged fragility (L3 §11; the non-Bach C→F regression). Assert
  current behaviour only, labelled as documenting a known issue — its fix is **Phase B (B2)**, not now.
- Oracle themes (derive the exact value at source):
  - **`keymodeformatting.cpp` (the exact display contract — assert each string):** the **tonic name** per mode at a key
    sig (e.g. Dorian@0-fifths → `D`, Lydian@0 → `F`, Mixolydian@0 → `G`; harmonic/melodic-minor reuse Aeolian/Dorian
    names) and the **suffix** per mode (`maj`/`Dor`/`Phryg`/`Lyd`/`Mixolyd`/`min`/`Loc`/`mel`/`harm`/`PhrygDom`/…).
    These are the user-visible label contract — one assert per mode case.
  - **`keymodeanalyzer.cpp`:** scale-membership `inC&&!inKS` / `!inC&&inKS` arms; **pairwise relative maj/min
    disambiguation** (complete-triad-vs-tonic-only bonus/cost); declared-"minor" accepts minor-class modes;
    `keySignatureFifthsForKey` table (C-major→0, A-minor→0…); out-of-range key-sig → global-argmax fallback;
    tonal-center override **suppression** when the raw winner is materially stronger; runner-up emission;
    single-result confidence (gap-vs-0).
  - **`keymodesequence.cpp`:** empty-context slice → neutral row skipped; `stateIndexForResult` not-found → skip;
    single-state lattice → confidence-vs-0; empty emissions/states → `{}`; **`maxAlternatives<=0` → ALL alternatives
    emitted**; pinned/redecode margin exclusions; single-viable-state → `kSingleStateConfidence` (certain, not uncertain).

## §2 — Write the tests + §3 gate + §4 scope — IDENTICAL to clusters 1–3
- New `keymode_branch_tests.cpp` (or extend `keymodeanalyzer_tests.cpp` / `decode_keymode_tests.cpp`), registered in
  `tests/CMakeLists.txt`. Oracle from theory/contract, never echoed (except the labelled leading-tone guard).
- A failing correct-oracle → `DISABLED_`/xfail + expected-vs-actual (rule 2). Do not weaken.
- **Gate:** new tests pass (bar xfails); `composing_tests` grows; `notation_tests` + snapshots **unchanged**; corpus
  53/24/53 by construction; build green. **Any corpus/snapshot movement → STOP.**
- **Re-measure:** clang branch-coverage scoped to the three key files → branch% before→after (note any
  covered-but-uncredited inline-header arms, per cluster 2).
- **Tests-only.** A gap closable only by changing production → STOP, flag. Skip defensive. Do not annotate exclusions
  (Phase-6). `upstream` never; local commit.

## §5 — Deliver
Commit **locally (unpushed)**: the new test file + CMake. Write `cc_backfill_l3_keymode_report.md` (gitignored): tests
added, branches re-classified defensive at source (+ over-count count), any surfaced defects (xfails — esp. anything
beyond the known leading-tone guard), per-file branch% before→after, and the commit sha — so Cowork verifies by sha that
only test files + CMake changed.

## §6 — Wrap (this closes the stable-half backfill)
This is cluster 4 of 4. In the report, give the **cumulative** stable-half picture: total tests added across clusters
1–4, the union branch% over the four stable file-groups before→after, and the consolidated **surfaced-defects list**
(the `DISABLED_` tests across all four clusters — German-bass slash, the leading-tone guard, any new ones) so Cowork can
fold them into the Phase-5 sign-off ledger.

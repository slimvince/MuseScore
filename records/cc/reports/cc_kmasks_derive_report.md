# CC Report — Phase 5 refactor (1 of 2): derive `kMasks` from one canonical interval source

**Date:** 2026-06-26
**Refactor commit (local, unpushed):** `a0b983839a`
**§0 docs commit (local, unpushed):** `c2612b7541`
**Prior HEAD:** `b2de0771fc`

Build-it-right refactor closing audit Q1.3: the 17 hand-typed Gate R `kMasks` bitmasks
(`harmonicfunctionlayer.cpp`) were a hand-maintained duplicate of the template intervals;
a wrong/zero mask silently disables Gate R for that template. The intervals are now defined
once (`analysis::kTemplateIntervals`, `chordanalyzer.h`) and `kMasks` is **derived** from
them at compile time. **Byte-identical — no scoring/template/gate/weight/matrix logic
changed.**

---

## §0 — Cowork doc sweep-protection (done first)

Commit `c2612b7541` — `docs(cowork): Phase-5 branch-backfill spec + plan re-sequence
(L1-L4 seal) + audit/handoff corrections`. `git show --stat` lists **only doc files**:

- `cowork_l1l3_stabilization_plan.md` (modified, the Phase-5b/6 re-sequence)
- `cowork_phase5_branch_backfill_spec.md` (new)

(The other docs named in the instruction — `cowork_l1l4_architecture_audit.md`,
`cowork_tpc_capability_design.md` — had **no uncommitted edits** in the tree at session
start, so were not part of this commit. `scratch_artifacts/` is untracked scratch, not a
Cowork doc — deliberately left out.)

---

## §1 — Equality gate (read-only, BEFORE changing): PASS — all 17 masks match

Computed each template's mask (bit *i* = OR over the intervals, `1u << i`) from the
`templates` interval column (`chordanalyzer.cpp:1199-1215`) and compared to the 17
hand-typed `kMasks` literals (`harmonicfunctionlayer.cpp:192-208`). **All 17 are exactly
equal** — no mismatch, so **no latent live bug to escalate** (the §1/§4 STOP condition did
not trigger). Cross-checked programmatically:

| idx | quality        | intervals      | derived = kMasks |
|-----|----------------|----------------|------------------|
| 0   | Major triad    | {0,4,7}        | 0x0091 |
| 1   | Maj7           | {0,4,7,11}     | 0x0891 |
| 2   | Dom7           | {0,4,7,10}     | 0x0491 |
| 3   | Dom7b5         | {0,4,6,10}     | 0x0451 |
| 4   | Minor triad    | {0,3,7}        | 0x0089 |
| 5   | Minor 7th      | {0,3,7,10}     | 0x0489 |
| 6   | Diminished     | {0,3,6}        | 0x0049 |
| 7   | Sus4b5         | {0,5,6,10}     | 0x0461 |
| 8   | HalfDim        | {0,3,6,10}     | 0x0449 |
| 9   | Augmented      | {0,4,8}        | 0x0111 |
| 10  | Aug dom7       | {0,4,8,10}     | 0x0511 |
| 11  | Sus2           | {0,2,7}        | 0x0085 |
| 12  | Sus4+m7        | {0,5,7,10}     | 0x04A1 |
| 13  | Sus4+Maj7      | {0,5,7,11}     | 0x08A1 |
| 14  | Sus4#5         | {0,5,8,10}     | 0x0521 |
| 15  | Sus#4          | {0,6,7}        | 0x00C1 |
| 16  | Power          | {0,7}          | 0x0081 |

These 17 hex values are the **frozen snapshot** the compile-time static_assert pins (below).

---

## §2 — The refactor, and which path I took

### What was added (canonical interval source) — `chordanalyzer.h`, purely additive

Between `kTemplateCount` and `enum class ChordQuality` (analysis namespace):

- `kMaxTemplateTones = 4` (the widest template — the 7th chords).
- `inline constexpr std::array<std::array<int, kMaxTemplateTones>, kTemplateCount>
  kTemplateIntervals` — the **single canonical interval source**, one row per template,
  trailing `-1` padding, row index == template index == `tiePriority`.
- `constexpr std::uint16_t templateIntervalMask(std::size_t t)` — OR of `1u << interval`
  over the non-`-1` tones of row `t`.
- `constexpr std::array<std::uint16_t, kTemplateCount> makeTemplateMasks()` — the full
  derived mask table.

### What changed (derive + delete the literals) — `harmonicfunctionlayer.cpp`

`bassIsTemplateChordTone`'s local `kMasks` is now
`static constexpr … = analysis::makeTemplateMasks();` — **the 17 hand-typed literals are
deleted.** The lookup (`(kMasks[tiePriority] & (1u << interval)) != 0`) and the existing
size static_assert are **unchanged**. Added a compile-time **byte-identity static_assert**
pinning the 17 derived masks to the frozen hex snapshot from §1. Comment block rewritten
(hand-sync → derived). `harmonicfunctionlayer.h`'s Gate R header comment updated ("kMasks is
the 5th atomic-update site" → "now DERIVED … no longer a hand-sync site").

### Path taken: **keep `templates[]` literals (the §2 fallback), NOT consume-the-table**

The instruction offered two paths for the templates array:
**(A)** single-source `templates[]` by having it consume the canonical table; or
**(B)** keep `templates[]`'s interval literals and add a compile-time check.

**I took path B (keep the literals).** Two decisive reasons:

1. **§5's file constraint forbids path A.** §5 says Cowork verifies by sha that **only
   `harmonicfunctionlayer.*` / `chordanalyzer.h` / `scoring_model.md` changed**. Path A
   requires editing `chordanalyzer.cpp` (the `templates` array), which is **excluded** from
   that list. Path B leaves `chordanalyzer.cpp` untouched — honoring the constraint and the
   "no scoring-array restructure this step" intent.

2. **The literal §2-path-B static_assert is infeasible as written**, and I substituted the
   §3-endorsed one. The instruction's path B suggests
   `static_assert(maskFromIntervals(templates[i].intervals) == kMasks[i])`. That **cannot
   compile**: `TemplateDef::intervals` is a runtime `std::vector<int>` (verified at
   `chordanalyzer.cpp:342`; it is used pervasively as a vector — `.size()`, `.begin()/.end()`,
   indexing, and `tpcDeltas[i]` indexed in parallel at `:510`), so `templates` is **not** a
   constant expression and cannot appear in a `static_assert`. Changing the representation to
   make it constexpr would be invasive and out of scope (touches `chordanalyzer.cpp` + the
   ~30 helper call-sites). Instead I deliver compile-time single-truth the way §3 endorses:
   the **frozen-snapshot static_assert on the derived masks** proves byte-identity at compile
   time, and the **independent `gater_tests.cpp` table oracle** (which encodes the 17 interval
   sets a third time and checks `bassIsTemplateChordTone` against them) continuously guards
   `kMasks` ↔ template-interval agreement at runtime.

**What this closes and what remains.** The audit-Q1.3 hazard — *a wrong/zero `kMasks` entry
silently disabling Gate R* — is **closed**: `kMasks` is derived from `kTemplateIntervals` and
frozen-asserted, so it can no longer be hand-typed wrong, and a zero mask is impossible
(every row has interval 0). The one residual hand-sync is `templates[]`'s own interval
literals vs `kTemplateIntervals` — same human-readable interval form, agreement proven now
(§1) and guarded ongoing by the independent gater oracle + the §9 checklist. **Fully
single-sourcing `templates[]` (path A) is a clean follow-up that touches `chordanalyzer.cpp`;
it was deliberately deferred to honor §5.**

---

## §3 — Byte-identity gate

### Compile-time proof (strongest — the STOP condition is a compile error)

The build **succeeded**, so the byte-identity `static_assert` in `bassIsTemplateChordTone`
holds: the 17 derived `kMasks` equal the exact original hand-typed hex values. Because
`kMasks` is the **only** behavioral surface this refactor changes (templates untouched, all
scoring logic untouched) and Gate R is its only consumer, **all scoring output is
byte-identical by construction.** The instruction's stop condition ("the derivation altered a
mask") is made a **compile error** — it cannot produce a binary.

### In-binary empirical confirmation (all green)

| suite | result |
|---|---|
| `composing_tests.exe` | **695 passed, 0 failed** (incl. gater F1 `BassIsTemplateChordTone_TableMatchesEveryTemplate` — the independent runtime oracle checking the derived masks vs an independently-encoded interval table) |
| `notation_tests.exe` | **53 passed, 0 failed** |
| `pipeline_snapshot_tests.exe` | **11/11 passed, ZERO diffs** (byte-identical P1–P4 output; **no golden refresh**) |

### Corpus BIR 53/24/53 — proven unchanged by construction; empirical regen BLOCKED by environment

I attempted the Baroque corpus regen (`run_bach_preset.py --preset Baroque`) for an A/B
byte-diff. It failed — **`batch_analyze.exe` cannot load any score in this session**:
`ERROR: failed to load score` for **both** `tools/corpus/bwv10.7.xml` (MusicXML) **and** a
native `tools/dcml/.../*.mscx`. Tried: Git Bash launch (the documented requirement), correct
preset case (`Baroque`), `QT_QPA_PLATFORM=offscreen`, Qt 6.10.1 `bin` on PATH +
`QT_PLUGIN_PATH` — all fail identically. No `platforms/` plugin dir sits beside the binary.

This is a **pre-existing session/infrastructure condition, independent of the refactor**:
score-loading happens **before** any chord scoring, so a score that never loads exercises
**zero** of the changed code; the failure reproduces identically regardless of code state.
(Prior sessions' `scratch_artifacts/set_baroque.txt` etc. confirm the corpus *did* run in a
properly provisioned environment.) **The corpus result is therefore certain by construction
(byte-identical `kMasks` ⇒ byte-identical scoring ⇒ BIR 53/24/53 unchanged), but was not
empirically re-run here.** Reported faithfully, not claimed as executed. A regen in a
Qt-provisioned environment will reproduce 53/24/53; the `kMasks` change is preset-independent,
so all three presets follow.

---

## §4 — Doc sync (`docs/scoring_model.md`, in the same commit)

- **§3 "Atomic update requirement"** — relabeled the kMasks bullet as a *size*-sync site and
  added a paragraph: the per-template interval data now lives once in
  `analysis::kTemplateIntervals`; `kMasks` is derived via `makeTemplateMasks()` and pinned by
  the byte-identity static_assert; noted the one residual `templates[]`↔table hand-sync
  guarded by the gater oracle.
- **§3 Gate R condition (3)** — "a static `kMasks[17]` … mirroring the 17 TemplateDef
  interval sets" → "a static `kMasks` … **derived** from `analysis::kTemplateIntervals`".
- **§4 Gate R "Forward-compatible"** — "`kMasks` is a sync site …" → "`kMasks` is **derived**
  … a 0 mask is impossible by construction".
- **§9 add-a-template checklist (step 5)** — replaced "add the new template's interval
  bitmask to `kMasks`" with "add the interval row to `kTemplateIntervals` (the single source;
  masks derive automatically); extend the byte-identity static_assert; the gater oracle
  cross-checks templates ↔ derived masks".

(The dated changelog footer was left untouched — its ordering is a historical record, and the
§4 sync rule scopes to §3/§9, both fully updated. `gater_tests.cpp`'s header comment slightly
over-describes kMasks as hand-typed but is **left untouched per §5's file constraint**; its
assertions remain valid and now serve as the independent runtime oracle.)

---

## §5 — Deliverables / how Cowork verifies

- **Refactor commit `a0b983839a`** (local, unpushed) — `git show --stat` lists **exactly**
  four files, no `chordanalyzer.cpp`, no tests, no scoring logic:
  - `src/composing/analysis/chord/chordanalyzer.h` (+60, purely additive)
  - `src/composing/analysis/function/harmonicfunctionlayer.cpp` (literals → derived + frozen
    static_assert; lookup unchanged)
  - `src/composing/analysis/function/harmonicfunctionlayer.h` (comment only)
  - `docs/scoring_model.md` (§3/§4/§9 sync)
- **§0 docs commit `c2612b7541`** (local, unpushed) — doc files only.
- Neither pushed; `upstream` untouched.

**Verification summary:** §1 equality PASS (17/17) · compile-time frozen byte-identity
static_assert holds (build green) · composing 695/0 · notation 53/0 · snapshots 11/11
zero-diff · corpus 53/24/53 unchanged by construction (empirical regen blocked by a
change-independent Qt environment issue — flagged for Cowork; not claimed as run).

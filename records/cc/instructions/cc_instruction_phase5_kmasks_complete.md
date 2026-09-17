# CC Instruction — Phase 5 refactor (1 of 2, COMPLETION): single-source `templates[]` from `kTemplateIntervals`

> **Why.** The kMasks-derive step (`a0b983839a`) added the canonical `kTemplateIntervals` in `chordanalyzer.h` and
> derived `kMasks` from it — but `templates[]` in `chordanalyzer.cpp` still holds **its own** interval literals, so the
> duplication **moved** (`kTemplateIntervals ↔ templates[].intervals`) rather than being eliminated. The first pass's
> §5 file constraint (no `chordanalyzer.cpp`) blocked the clean fix; **this completion lifts that constraint** to reach
> **one** interval source feeding both `templates` and `kMasks`. **Byte-identical — NO scoring/weight/template-membership
> change.** This finishes audit Q1.3 to its real intent (the compiler-enforced single source).
>
> **Grounded (verified at source, file tools):** `templates` = `static const std::array<TemplateDef, kTemplateCount>` at
> `chordanalyzer.cpp:1198-1216`, each `{ ChordQuality, intervals{…}, weights{…} }`; `TemplateDef::intervals` is a
> runtime `std::vector<int>`. `kTemplateIntervals` is the canonical constexpr table added in `chordanalyzer.h` (same
> header `templates` already includes).

## §1 — The change (`chordanalyzer.cpp` `templates[]` initializer ONLY)
- Make each `templates[i]`'s **`intervals` field derive from `kTemplateIntervals[i]`** (the canonical table) instead of
  the inline literal — same 17 interval lists, same values. The `quality` and `weights` fields stay inline (those are
  template-scoring-specific, not the shared interval data). Pick the minimal conversion to build the `std::vector<int>`
  from `kTemplateIntervals[i]`.
- After this, `kTemplateIntervals` is the **sole** interval definition; both `templates[]` and `kMasks` consume it.
- **If `TemplateDef::intervals` cannot cleanly take `kTemplateIntervals[i]` without a representation change that touches
  `TemplateDef` or the scoring path → STOP and report.** Do not restructure `TemplateDef`, the score matrices, or any
  scoring logic to force it.

## §2 — Gate (byte-identical is the hard gate)
- The 17 `templates[i].intervals` values are **unchanged** (same lists) — prove by a one-time equality check and the
  existing `gater_tests.cpp` + catalog tests (which exercise template matching).
- **`composing_tests` + `notation_tests` + `pipeline_snapshot_tests` green and byte-identical** (no golden refresh).
  Corpus BIR 53/24/53 is **unchanged by construction** (kMasks already snapshot-pinned; the template intervals are
  value-identical). *(If `batch_analyze` has been restored, regen to confirm; otherwise by-construction + the suites,
  and note `batch_analyze` is still down — the plan's Phase-5b prerequisite.)*
- **No scoring / weight / matrix / template-membership / `kMasks` change** — only the `intervals` data is single-sourced.

## §3 — Scope & stops
- **Only `chordanalyzer.cpp`'s `templates[]` initializer changes** (no weights, no `kMasks` — already derived, no logic).
- A post-change `intervals` value differs from the original 17 → **STOP** (a transcription error — a bug).
- `TemplateDef`/scoring would need restructuring → STOP, report (we keep the partial-but-improved state rather than
  risk the scoring path).
- `upstream` never; local commit only.

## §4 — Deliver
Commit **locally (unpushed)**: the `templates[]` single-sourcing. Write `cc_kmasks_complete_report.md` (gitignored): the
conversion used, the intervals-unchanged proof (17 lists equal), the byte-identity proof (suites + snapshots), and the
commit sha — so Cowork verifies by sha that **only `chordanalyzer.cpp` changed** (no other file, no scoring logic).

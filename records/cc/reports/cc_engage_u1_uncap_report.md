# CC Engage arc #5 — U1 UNCAP (Option A): **STOP** — cap #1 removal is NOT byte-identical

**Verdict: STOP (surfaced to Cowork, not built around).** Removing cap #1 alone
(`harmonicfunctionlayer.cpp:521`, the `if (results.size() >= 3) break;` loop-bound) is **not**
byte-identical on the default path. It changes the serialized `.ours.json` alternatives on most
regions **and** breaks a winner-relevant post-pass (pedal detection). This directly trips the
dispatch's own hard STOP: *"Any diff on the DEFAULT `.ours.json` path ⟹ STOP."* Per principles #3
(an unexpected finding = we failed #1) and #13 (surface a surprise as a STOP before building around
it), I stopped, **reverted the edit, rebuilt to restore byte-identical HEAD**, and did **not** add
the fan-out dump, refresh goldens, write the corpus, commit, or push.

Provenance: Cowork dispatch "Engage arc #5 (Option A)", 2026-07-06. HEAD `5fa16b77e0`, branch
`master`, fork-only. Instrument artifacts under `scratch_artifacts/u1_byteid/` and
`scratch_artifacts/u1_pipeline_snap.txt`, `scratch_artifacts/u1_composing_tests.txt`.

---

## Task 1 — the three caps (characterized at source) ✓

"How many chord readings we keep" is governed by **three independent `<3` caps**, confirmed at
source:

| Cap | Site | Surface governed | Bound |
|---|---|---|---|
| **#1 production carry** | `src/composing/analysis/function/harmonicfunctionlayer.cpp:521` — `if (results.size() >= 3) break;` in the results-fill loop | the in-memory `results` returned by `analyzeChord` → flows to `HarmonicRegion.alternatives` via `alternativesSnapshot = results[1..end]` (`regionanalyzer.cpp:990-992`) | **≤ 3 TOTAL** (winner + 2 alternatives)* |
| **#2 measurement serialization** | `tools/batch_analyze.cpp:660` (section path) and `:712` (main batch path) — `altIdx < 3` | the `.ours.json` `"alternatives"` array (serialized at `batch_analyze.cpp:1490-1494`) | **≤ 3 ALTERNATIVES** (winner + 3) |
| **#3 user display** | `src/notation/internal/notationcomposingbridge.cpp:794` — `maxShown = prefs->analysisAlternatives()` | the status-bar chord-alternatives display | user preference |

\* *plus the "Guaranteed inversion alternative (diff-root append)"* at
`harmonicfunctionlayer.cpp:530-549`, which can add **one** extra diff-root entry as `results[3]` in
the narrow "winner is bass-root AND top-3 all share the winner's root" case (see M2 below).

**★ The load-bearing local fact the dispatch's premise missed:** cap #1 and cap #2 are **off by
one**. Cap #1 bounds the **total** result count at 3 (⇒ winner + **2** alternatives). Cap #2 bounds
the **alternative** count at 3 (⇒ winner + **3**). So cap #2 does **not** re-truncate to HEAD's
serialized surface — HEAD's default `.ours.json` carries mostly **2** alternatives, and removing
cap #1 lets a **3rd** alternative through cap #2. The dispatch's model ("removing #1 leaves every
serialized surface capped at 3, byte-identical, because #2 re-truncates") is therefore incorrect at
the code level.

---

## What I did (exactly the scoped change) then measured

1. Removed cap #1 (only the `results.size() >= 3` break; kept the `rc.score < threshold` gate),
   as instructed. **Did not** add the dump yet (correct sequencing: prove the default path is
   byte-identical before layering the dump on top — it is not).
2. Built (`setup_and_build.bat`, exit 0, all 7 targets).
3. Measured the default path (dump-off — the dump was never added) on the three surfaces the
   dispatch names in Task 3.

### Evidence — the default path is NOT byte-identical

| Surface | HEAD (dispatch's stated baseline) | cap #1 removed | Verdict |
|---|---|---|---|
| `pipeline_snapshot_tests` (P1–P4, 10 scores) | 11/11 | **0/11** (all fail) | **CHANGED** |
| `composing_tests` | 1101 pass | **1097 pass, 4 FAIL** (all pedal) | **CHANGED** |
| batch_analyze `.ours.json` (the stops' input) | frozen `tools/corpus/baroque` | **diverges** (bwv10.7 **37 hunks**, bwv259 **13**, bwv281 **11**) | **CHANGED** |

**Determinism / attribution control (rules out nondeterminism):** after reverting the edit and
rebuilding, regenerating `bwv259.ours.json` with the restored binary is **byte-identical to
`tools/corpus/baroque/bwv259.ours.json`** (`diff` exit 0). So the divergence above is **100%
attributable to cap #1 removal**, and the revert fully restored HEAD.

---

## The three local coupling mechanisms (the local knowledge Cowork could not see)

### M1 — the cap#1/cap#2 off-by-one (the dominant, systematic channel)
HEAD serializes mostly **winner + 2 alternatives** because cap #1 (≤3 total) is the binding
constraint, not cap #2 (≤3 alternatives). Removing cap #1 lets the previously-blocked **3rd**
alternative through cap #2. Measured on **bwv259** (24 regions):

```
HEAD    (cap #1 live): #alternatives-per-region → {2: 16, 3: 8}
cap#1-removed        : #alternatives-per-region → {2:  7, 3: 17}   (9 regions gained a 3rd alt)
```
Example added 3rd alternatives (batch surface): `D @3.1` **+** `D5 Power @1.89`; `B7/A @2.41` **+**
`G+/A Aug @2.24`; `D/F# @3.43` **+** `Bm7/F# @2.68`; `FMaj7/A @2.57` **+** `F#m7b5/A @2.52`. Every
added entry is a legitimately-admitted (≥ threshold) tail candidate that cap #1 was hiding.

### M2 — the diff-root-append coupling (the `results[3]` content channel)
The "Guaranteed inversion alternative" append (`harmonicfunctionlayer.cpp:530-549`) was added
**specifically to compensate for cap #1** (`docs/prompts/fix_results_cap_exhaustion.md`: when the
cap-of-3 is exhausted by same-root variants, append the highest-scoring diff-root so the
post-ranking correction has a target). With cap #1 removed the main loop already carries every
above-threshold diff-root, so the append goes **dead** — and the candidate it used to promote into
the serialized `results[3]` slot is **displaced** by the natural higher-scoring same-root candidate.
Observed on bwv259: HEAD's `Dsus/G Vsus46 @2.05` (an appended guaranteed-inversion alt) is replaced
by `G5 Power @2.13`, and `Dsus/G` drops out of the serialized window. This changes *which*
alternatives are serialized even where the count stays at 3.

### M3 — the pedal-detection coupling (a WINNER-IDENTITY change)
`applyIter8691Pedal(results, …)` (run in the region pipeline, `regionanalyzer.cpp:980`) reads
`results` and annotates the **winner** (`results.front().identity.isPedalPoint / pedalBassPc`). With
the longer/reshaped `results` vector, pedal detection breaks: **4 unit tests fail with
`results.front().identity.isPedalPoint` = `false`, expected `true`** (`chordanalyzer_tests.cpp:2144`
et al.; `postscoringgates_tests.cpp:1458`). This is a change to the **winner's identity**, not just
the alternatives. (Note: `isPedalPoint` is **not** serialized in `.ours.json`, so it is invisible on
the batch stop surface — but it is real, affects the notation pipeline / display / any
`identity.isPedalPoint` consumer, and shows that cap #1 is coupled to a winner-relevant post-pass.)

**On winner-root stability:** on the 3 sampled Baroque scores the region-level winner root/quality
is unchanged (all batch diffs are inside the alternatives arrays). But I did **not** run the full
robust sandwich (the edit was reverted once the byte-identity STOP fired), and M3 shows the winner's
identity *is* affected in pedal cases — so corpus-wide winner-root stability is **not established**,
and the dispatch's "winners unchanged / both stops trivially green" premise is **not supported** by
what I can measure locally.

---

## Conflict with the dispatch's greater-context premise (why this is a STOP, not a proceed)

The dispatch (from context I cannot see) stated: *"Under Option A the default `.ours.json` is
byte-identical anyway, so both stops stay trivially green and no re-baseline is needed."* My local,
code-level measurement contradicts this on every surface. The premise assumed cap #2 re-truncates
cap #1's output to the same bytes; in reality cap #1 (≤3 total) is a **tighter** and **differently-
shaped** bound than cap #2 (≤3 alternatives), and cap #1 is **coupled** to two `results`-reading
post-passes (M2 the diff-root append, M3 pedal detection). This is precisely the local/detailed
knowledge the engagement note says CC holds and Cowork does not. Building the fan-out dump on top of
this would be building around the surprise (violates #13) and would ship a non-byte-identical default
(violates the dispatch's own STOP condition and #16).

---

## What I did NOT do (STOP hygiene)

- Did **not** add the fan-out dump (Task 2 half-2), **not** refresh goldens, **not** write/regen the
  corpus, **not** re-baseline, **not** commit, **not** push. (`tools/corpus/` and
  `tools/robust_stop/` untouched; the pending Cowork CLAUDE.md #12 edit left as-is.)
- **Reverted** the cap #1 edit and **rebuilt** → working tree clean (only the pre-existing
  `M CLAUDE.md` + untracked scratch remain); binary byte-identical to HEAD (control above).

---

## Options for Cowork (surfaced, not decided — this is an architecture call)

The goal — full ranked carry in memory for dormant Layer 5 + an observable fan-out — is achievable,
but **not** via "remove cap #1, leave caps #2/#3, expect byte-identical." Three ways to reconcile:

- **(A) Decouple the carry from the winner/serialization path (cleanest re: Option A's spirit).**
  Leave `results` and the whole existing path (diff-root append, pedal pass, cap #2 serialization,
  cap #3 display) **exactly as-is**, and add a **separate** full-carry field the dormant Layer 5 /
  the default-off dump read (e.g. `HarmonicRegion.fullCarry`, populated from the untruncated
  `chosenPerBass` alongside the capped `results`). Default `.ours.json` stays byte-identical; Layer 5
  still gets the complete fan-out. This changes *where the full carry lives* — an architecture
  decision for Cowork.
- **(B) Do U1 together with the cap-#2 lift + a deliberate re-baseline** (the very thing the dispatch
  deferred to the Layer 5 engagement design). If the full carry is meant to become the default
  serialized surface, that is a ratified re-baseline of `tools/corpus/` + `tools/robust_stop/` with an
  explained per-run diff — not a byte-identical no-op. Option A-as-scoped cannot be byte-identical.
- **(C) If the intent really is "byte-identical default, cap #1 gone":** cap #2 would have to be
  tightened `< 3` → `< 2` to match cap #1's effective 2-alternative surface, **and** the diff-root
  append (M2) and pedal pass (M3) would need explicit decoupling from `results.size()`. This is
  several coupled edits touching the deferred cap #2 — out of the stated scope.

My read (local, for Cowork to weigh): **(A)** best matches "uncap the in-memory carry, byte-identical
default, observable dump" without disturbing the winner/serialization substrate — but the three-cap
**#6 unification** and the cap-#2 lift the dispatch already deferred to the Layer 5 engagement design
are where the "should the full carry be the default measured surface" decision belongs (that's **(B)**).

---

## Reproduce

```
# cap #1 removal = delete the `if (results.size() >= 3) { break; }` at
#   src/composing/analysis/function/harmonicfunctionlayer.cpp:521  (keep the threshold break)
# build, then:
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe          # → 0/11 (added alternatives)
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe                  # → 1097/1101, 4 pedal fails
cd C:\s\MS && ./ninja_build_rel/batch_analyze.exe tools/corpus/bwv259.xml /tmp/x.ours.json --preset Baroque
diff tools/corpus/baroque/bwv259.ours.json /tmp/x.ours.json          # → non-empty (13 hunks)
```

*CC, 2026-07-06 (arc #5). STOP surfaced for Cowork adjudication. The fan-out the dispatch wants to
"see in reality" is real and large — bwv259 alone: 9/24 regions carry a 3rd above-threshold reading
that cap #1 currently hides — but exposing it on the default serialized path is a behavior change,
not a byte-identical no-op.*

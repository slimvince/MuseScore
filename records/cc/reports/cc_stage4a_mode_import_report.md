# CC Report — Stage 4a: declared-mode MusicXML import fix

*CC, 2026-06-14. Base `a96f179f40`. Discrete first Stage-4 step (NOT full Stage 4):
the local engraving patch that restores the declared `<mode>` for empty (0-fifths) key
signatures on MusicXML import, proven in isolation before any graded-prior / KeyArea work
is built on top. **HELD — `git add` done, no commit (user commits).** Every number tagged
`[probe]` (Python over `.ours.json`/DCML), `[dump]` (key-candidate instrument), `[rt]`
(MuseScore round-trip), or `[code]`.*

> **Headline.** A one-condition fix to `addKey()` (add a `mode()` term to the fifths-only
> dedup) restores the dropped declared mode on **exactly 79 zero-signature stems** and
> nothing else. **BIR gate byte-identical on all three presets** (Baroque 57 / Jazz 23 /
> Default 57 — identity sets unchanged, 0 added / 0 removed → ratification gate PASSED).
> **Key inference improves materially and the projected reach materialized:** Default S2
> (genuine key error) **1063 → 685 = −378** (the dossier projected ~349; the win slightly
> exceeds it). 47 of the 73 WiR-covered affected stems improve, 19 neutral, **7 regress on
> S2 only** (all "notation-disagrees-DCML" over-locks of the existing −7 wall — the precise
> motivation for Stage-4 step 2's graded prior; **not a BIR stop**). Round-trip of a
> 0-fifths `<mode>` file now preserves `<mode>` (#9444 fixed, before/after verified on our
> base).

---

## §1 — The patch

**File:** `src/importexport/musicxml/internal/import/importmusicxmlpass2.cpp`,
function `addKey()` (only file touched; the authorized off-limits exception). Diff:

```diff
-    Key oldkey = score->staff(staffIdx)->key(tick);
+    const KeySigEvent oldKeySig = score->staff(staffIdx)->keySigEvent(tick);
+    const Key oldkey = oldKeySig.key();
     // TODO only if different custom key ?
-    if (oldkey != key.key() || key.custom() || key.isAtonal()) {
+    // Also retain the key signature when only the <mode> differs at matching fifths.
+    // [comment — see source]
+    if (oldkey != key.key() || oldKeySig.mode() != key.mode() || key.custom() || key.isAtonal()) {
```

**Mechanism (verified at source) [code].** `KeyList::key()` returns the prevailing
`KeySigEvent` defaulting to `{key=C(0), mode=KeyMode::UNKNOWN}` (`keylist.cpp:36` →
`setConcertKey(Key::C)`). For a 0-fifths key bearing an explicit `<mode>`, the old guard's
`oldkey != key.key()` was false (C==C) and `custom`/`isAtonal` false → the whole `KeySig`
was dropped, taking the declared mode → `KeyMode::UNKNOWN` downstream. Adding
`oldKeySig.mode() != key.mode()` retains it. A key matching the prevailing one in **both**
fifths **and** mode (and not custom/atonal) still produces **no** `KeySig` (the
no-spurious-keysig guard), so plain mode-less C-major scores are unaffected.

The companion CLAUDE.md "Local patches — do not revert" entry is added (mirrors the
Windows-Snap-fix entry: file/function, fifths-only-dedup rationale, round-trip evidence,
upstream #9444, "do not let dependency updates overwrite without approval").

**No other engraving file was needed** — the `KeySigEvent`/`mode()` accessors
(`key.h:77`, `staff.h:125`) already exist; the stop-condition "fix needs another engraving
file" did not trigger.

---

## §2 — #9444 repro (before/after, verified on our base) [rt]

Input `tools/corpus/bwv254.xml` carries `<fifths>0</fifths><mode>minor</mode>`.
MuseScore CLI round-trip (`MuseScore5.exe in.xml -o out.musicxml`), exported first `<key>`:

| build | exported `<key>` | mode |
|---|---|---|
| **pre-fix** (stash-reverted, full rebuild) | `<fifths>0</fifths>` | **LOST** |
| **post-fix** (patched) | `<fifths>0</fifths><mode>minor</mode>` | **preserved** |
| control: `testKeysig1.xml` (0-fifths, **no** mode), post-fix | `<fifths>0</fifths>` | none (no spurious keysig) |

Export already writes `<mode>` (`exportmusicxml.cpp:2473`), so the fault was purely the
import-side dedup. **Confirmed on our base.** The buggy fifths-only dedup is
upstream-unchanged code (the maintainers' own `// TODO only if different custom key ?` at
the same line), so the repro applies to upstream `master` by inspection — I did **not**
separately check out and rebuild upstream `master`. The pre-fix `<mode>`-drop was also
independently corroborated by the emission dossier (`declaredModeOrdinal=-1` on every
0-sig region) and by the corpus before/after (§4: exactly the 79 mode-bearing 0-sig stems'
resolved keys changed — which can only happen if the mode was absent before and present
after).

This table is the tight repro Cowork can use to draft the #9444 comment.

---

## §3 — Build + test verification

- Build green (full `setup_and_build.bat`); `ninja … : no work to do` confirms the patched
  tree is current.
- **composing_tests 505/505**, **notation_tests 57/57**, **pipeline_snapshot_tests 11/11**
  (zero golden diffs — see §5).
- MusicXML round-trip: the engraving `iex_musicxml_tests` target is **not configured in
  this build tree** (`unknown target`), so the round-trip was verified via the rebuilt
  `MuseScore5.exe` CLI (§2) rather than the gtest harness. The existing keysig IO fixtures
  are unaffected by inspection: `testKeysig1` (0-fifths, no mode → both UNKNOWN → no keysig,
  unchanged), `testKeysig2` (`<mode>none</mode>` → already retained via `isAtonal`),
  `staffTwoKeySigs` / `nonStandardKeySig*` (non-empty or custom). The CLI control on
  `testKeysig1.xml` confirms it still round-trips identically.

---

## §4 — Isolation + gate re-measure (the ratification gate)

Corpora regenerated at the patched build (353/353, manifest-stamped) for all three presets;
pre-fix corpora (`a96f179f40` baseline) backed up for the byte-diff.

### 4.1 Isolation — confined to empty signatures [probe]

```
.ours.json changed (Default, pre-fix vs patched):  79 / 353
  of which zero-signature (<fifths>0</fifths>):    79
  of which non-empty-signature:                     0
```

**Exactly the 79 mode-bearing 0-sig stems changed; 0 non-empty-signature stems moved.** The
~127 anchored-relative bucket (all non-empty-sig) did **not** move. The 79 = every corpus
input whose first `<key>` is `0-fifths + <mode>` (25 major / 54 minor); 73 of them are
WiR-covered (= the dossier's "73 zero-sig stems"), 6 uncovered. Isolation requirement
satisfied; the "change not isolated to empty-signature scores" stop-condition did not
trigger.

### 4.2 BIR gate — byte-identical on all three presets [probe]

`characterise_bir_false.py --corpus-dir …`, gating on **case identity** (stem@tick):

| preset | baseline | patched | added | removed |
|---|---|---|---|---|
| Baroque | 57 | **57** | 0 | 0 |
| Jazz | 23 | **23** | 0 | 0 |
| Default | 57 | **57** | 0 | 0 |

**Zero BIR=false movement; identity sets identical.** The "BIR=false increase = hard stop"
condition did not trigger. (Expected: ~95% of gate cases are symmetric-dim7 / viio↔V7
share-tone sonorities whose root/bass identity is independent of the global key mode, so a
key-mode change cannot move them.)

### 4.3 Real key-inference improvement (the user's bar) [probe]

`compare_rn.py --wir-bach <dir> --key-breakdown`, 326 WiR-covered stems, 10 108/10 109
matched regions. **Default (the user-run config):**

| metric | pre-fix | patched | Δ |
|---|---|---|---|
| rn_agree (full RN match) | 43.9% (4438) | **45.4% (4589)** | +151 |
| key_disagree total | 2948 | 2812 | −136 |
| **S2 (genuine key error, Stage-4 axis)** | **1063** | **685** | **−378 (−35.6%)** |
| S1 (=global, tonicization label-gap, Stage-6) | 1885 | 2127 | +242 |

Baroque mirrors: S2 1052 → 683 (−369). The S2 −378 **entirely attributable to the 79
stems** (subset measure: S2 640 → 262 = −378; nothing else moved). Decomposition of the
378 S2 fixes: **~151 became full agreement** (rn_agree gain); **~242 moved S2→S1** — i.e.
our **global key is now correct** and only the **local tonicization label** differs (an
explicit Stage-6 axis, not a key error). The dossier projected ~349 reachable; the measured
win is **378 ≥ 349** — it **materialized** (the "projected win fails to materialize"
stop-condition did not trigger).

The fix re-enables, for the 73 zero-sig stems, the three machinery the dropped mode gated
off [dump]: piece-start **anchor** (`path:"anchor"`), the declared-mode penalty, and
`partialSignatureCorrection`. Confirmed on bwv153.9 (0/major): pre-fix `declaredModeOrdinal
=-1`, productionKey Amin (wrong relative); patched `declaredModeOrdinal=0`, `path:"anchor"`,
productionKey **Cmaj** (= DCML global). bwv254 (the dossier's partial-signature poster
child, d-minor notated 0-fifths): S2 **17 → 0**.

### 4.4 DCML adjudication of the 7 S2 regressions

Per-stem S2 (73 WiR-covered affected stems): **47 improved, 19 neutral, 7 regressed**, net
**−378**. The 7 regressions (S2 up), all adjudicated against DCML global:

| stem | notated | DCML global | S2 bef→aft | class |
|---|---|---|---|---|
| bwv64.2 | 0/minor (=Amin) | G major | 1→20 (+19) | notation≠DCML; patched reads Emin (G-major's **relative**) — strict-tonic metric artifact |
| bwv365 | 0/major (=Cmaj) | a minor | 4→7 (+3) | C↔a **relative pair** |
| bwv33.6 | 0/major | a minor | 14→16 (+2) | C↔a relative pair |
| bwv83.5 | 0/minor | d minor | 10→13 (+3) | partial-sig (d-min, 1 flat) |
| bwv276 | 0/major | d minor | 19→21 (+2) | partial-sig |
| bwv371 | 0/major | G major | 13→15 (+2) | partial-sig (G, 1 sharp) |
| bwv437 | 0/minor | d minor | 15→17 (+2) | partial-sig |

**Single mechanism:** every regression stem's 0-fifths notation **disagrees with the DCML
analytical global tonic**. The fix faithfully imports the notated mode; the resolver's
**existing −7 declared-mode wall** then over-commits to the notated (analytically "wrong")
key. This is the dossier's predicted bucket-A risk ("the zero-sig relative stems whose
notation disagrees with DCML entrench wrong") plus the §4.2-point-2 over-lock ("a hard −7
lock over-constrains genuinely-modulating 0-sig pieces — which is why the lock must become a
graded prior"). It is a property of the **pre-existing −7 wall, not of this import fix**,
and bounded: six of seven are +2/+3 (several pure C↔a / G↔e relative-pair metric artifacts);
bwv64.2's +19 is the lone outlier (reads E minor, the relative of DCML's G major). **Net
+378, and BIR untouched** → not a ratification stop. These 7 are the concrete case for
Stage-4 step 2 (graded declared prior replacing the −7 wall), which recovers them without
forfeiting the +378.

---

## §5 — Pipeline-snapshot goldens: unchanged (no refresh)

`pipeline_snapshot_tests` 11/11 with **zero golden diffs** — no refresh performed. The
snapshot corpus loads `.mscx` directly via `ScoreRW::readScore` (`pipeline_snapshot_tests
.cpp:154+`), which bypasses the MusicXML importer entirely, so this fix cannot reach it (an
independent confirmation of §4.1's isolation — the change touches only the `*.xml`
MusicXML-import path). Same reason `composing_tests`/`notation_tests` did not even relink
against the changed `iex_musicxml.lib` (`ninja … no work to do`).

---

## §6 — Verdict + what is NOT in this run

**Stage-4a verifies in isolation — proceed to the next Stage-4 step.** All five
verification items pass: (1) suites + round-trip green; (2) change isolated to
empty-signature scores; (3) key-inference win real and ≥ projected (S2 −378); (4) gate
byte-identical on all presets, every key change DCML-adjudicated; (5) snapshots unchanged.
No stop-condition triggered.

**Held for the next steps (NOT built here, per instruction):** the **graded declared prior**
(replace the resolver's −7 wall with a graded HMM-style prior — recovers the 7 over-lock
regressions and the bwv64.2 class), **KeyArea spans**, and **P3 mode-drop**. The 7
regressions and the 242 S2→S1 cases are their concrete targets.

**Process:** HELD — `git add` of the patch + CLAUDE.md entry done; **no commit** (user
commits). The corrected-metric commit remains the flagged Stage-5 prerequisite (unchanged
by this run).

### Files staged
- `src/importexport/musicxml/internal/import/importmusicxmlpass2.cpp` (the patch)
- `CLAUDE.md` (local-patch entry)
- `cc_stage4a_mode_import_report.md` (this report)
- regenerated corpora under `tools/corpus/{baroque,jazz,default}` (patched-build `.ours.json`
  + manifests) — stage if corpus regen is normally committed; otherwise leave to the user.

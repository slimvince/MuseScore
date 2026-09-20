# CC — BUILD report: the standing per-event TIERED oracle-root metric + Baroque corpus regen

> **MEASUREMENT-ONLY. HEAD `dd418ecfed`.** No production / analyzer / scoring / gate-threshold /
> `chordanalyzer` change. The new tool only *reads* validated corpora and *emits* case-identity sets —
> exactly like `characterise_bir_false.py`. It reuses `characterise_bir_false.validate_corpus_dir`,
> `compare_analyses`, and `dcml_parser` **verbatim** (imported, not forked). First committed tooling in
> the metric arc. North star: best = CORRECT vs the DCML/music21 oracle, not the BIR gate.
>
> **Deliverables (local, unpushed):** `tools/oracle_root_metric.py` (the tool) +
> `tools/tests/test_oracle_root_metric.py` (15 tests). This report is HELD (`/cc_*.md` is gitignored).
> The Baroque corpus regen is reported (corpora are gitignored — `git ls-files tools/corpus` = 0).
>
> **★ One STOP surfaced + user-ratified (see §3):** the round-3/decomp "Baroque HEAD" baseline was
> measured on `tools/corpus/baroque_kma_abs`, which is **not** plain HEAD Baroque but a non-default
> KEY-MODULATION corpus. The user ratified **plain-for-all** as the standing baseline (Baroque
> re-stated 54.9 → 46.8 % KEY). Details below; nothing papered over.

---

## §1 — The tool (design)

`tools/oracle_root_metric.py` consolidates the two **throwaway** diagnostics that produced the ratified
read-only numbers — `cc_round3_measure.py` (per-event charged/floor separation) and
`cc_decomp_measure.py` (KEY / OVER-GRAB / CHORD-ID / AMBIGUOUS decomposition) — into one standing,
manifest-validated, tested tool, **with the KEY band split into KEY-HARD vs KEY-TONICIZATION** (the
mandated separation the throwaways did not surface as first-class tiers).

**Granularity (round-3 semantics).** One scored *event* per DCML annotation; event tick = the DCML
onset reconstructed from our region anchors via `compare_analyses._dcml_time_spans` (rntxt has no
absolute-tick column); our root and music21's root at the event = the root of the region whose
`[start,end)` **contains** the tick (tick-containment — no onset-vs-overlap choice).

**Predicate (reused verbatim).** `compare_analyses.three_way_classify(our_pc, m21_pc, dcml_pc)`,
bass-decoupled, pc-typed. Our absent-root (-1) and music21 absent-root → `None` → `three_way_classify`
returns `no_dcml`, so an absent-our-root event is **never charged** (it is the flagged residual).

**The two top-level buckets — clean by construction, NEVER summed.**
- **CHARGED** = `three_way_classify == 'music21_dcml_agree'` (m21 == dcml ≠ ours) — genuine oracle-root
  error. A charge **requires** m21 == dcml.
- **FLOOR** = events where m21 and dcml are both present and **m21 ≠ dcml** (the genuine same-event
  oracle dispute / symmetric-dim7). A floor **requires** m21 ≠ dcml.
- Because charge ⇒ (m21==dcml) and floor ⇒ (m21≠dcml), **no event is ever both** (pinned by a test that
  sweeps every root combination).

**The 5 charged sub-tiers** (each charged event lands in exactly one; priority order):
1. **KEY-HARD** — our key ≠ DCML-local key **and** music21 corroborates DCML (m21 key == DCML key):
   our key differs from **both** oracles → genuine key-detection error.
2. **KEY-TONICIZATION** — our key ≠ DCML-local key but music21 **disputes** DCML's local key (m21 ≠ DCML):
   the local-vs-global tonicization-labeling grain — reported **separately**, never folded into KEY-HARD.
3. **OVER-GRAB** — our key matches the oracle key, our single region spans **≥2** distinct oracle roots
   (segmentation under-grab).
4. **CHORD-ID** — our key matches, region aligns ~1:1 (exactly 1 oracle root in span), root still wrong
   (vertical / competition miss).
5. **AMBIGUOUS** — our key matches DCML but music21 disputes the oracle key, or a key string is
   unparseable — cannot be cleanly bucketed; size reported, never forced.

`KEY-HARD + KEY-TONICIZATION == the aggregate KEY band`; the 5 tiers sum to the per-record charged total.

**Case-identity = `stem@tick`** (reconstructed DCML onset tick; preset-stable). Two DCML annotations can
reconstruct to the same tick (co-tick) → distinct *records*, one identity string → the deduped
identity-set size is slightly below the per-record count. The tool reports BOTH (no conflation).

**Manifest validation.** Every corpus dir is run through `characterise_bir_false.validate_corpus_dir`
(the anti-contamination guard) before measuring — identical to `characterise_bir_false`.

**CLI.** `python tools/oracle_root_metric.py --corpus-dir DIR [--corpus-dir DIR ...] [--emit-json PATH]`.
Prints a per-preset summary table; `--emit-json` writes the full per-tier case-identity sets.

---

## §2 — Acceptance: the tool reproduces the read-only findings EXACTLY

Run against the exact corpora the round-3 / decomposition reports used (Baroque HEAD =
`baroque_kma_abs`, Jazz = `jazz`, Default = `default`). **Every number matches.**

### Round-3 charged / floor (deduped case-identity sets)

| preset (report corpus) | charged (set) | floor (set) | per-record charged | co-tick | target (reports) |
|---|---:|---:|---:|---:|---|
| Baroque HEAD (`baroque_kma_abs`) | **3862** | **4287** | 3882 | +20 | 3862 / 4287 ✓ |
| Jazz (`jazz`) | **4065** | **4276** | 4083 | +18 | 4065 / 4276 ✓ |
| Default (`default`) | **3894** | **4285** | 3914 | +20 | 3894 / 4285 ✓ |

### Decomposition tiers (% of per-record charged) — incl. the KEY-HARD / KEY-TONICIZATION split

| preset | KEY | …HARD | …TONIC | OVER-GRAB | CHORD-ID | AMBIGUOUS |
|---|---:|---:|---:|---:|---:|---:|
| Baroque HEAD (`baroque_kma_abs`) | **54.9 %** | 24.5 % | 30.4 % | **31.6 %** | **2.2 %** | **11.3 %** |
| Jazz (`jazz`) | **52.9 %** | 18.4 % | 34.5 % | **37.9 %** | **2.0 %** | **7.2 %** |
| Default (`default`) | **46.4 %** | 9.8 % | 36.6 % | **45.1 %** | **3.3 %** | **5.1 %** |

All match the decomposition report's PRIMARY table (54.9 / 31.6 / 2.2 / 11.3 etc.) **and** the
KEY-HARD numbers exactly match the report's strict-AMBIGUOUS sensitivity "hard, m21-corroborated" band
(24.5 / 18.4 / 9.8 % = 951 / 752 / 384). The ~10–25 % hard vs ~30 % tonicization grain is reproduced.

### The 2 robust fixes + chord-ID near-ceiling

Confirmed at the event tick (HEAD = `baroque_kma_abs`, ANCHOR = the old `baroque` ANCHOR corpus):
- **bwv14.5@8160** (m5.1 `I`, Bb): HEAD `Gm/Bb`→G **charged** → ANCHOR `Bbadd9`→Bb **ok** = FIX
  (in HEAD charged set, **not** in ANCHOR charged set).
- **bwv416@10080** (m6.1 `viio7`, Ab): HEAD `E7b9/G#`→E **charged** → ANCHOR `G#dim7`→Ab **ok** = FIX.
- **CHORD-ID near-ceiling 2.0–3.3 %** holds — the chord/vertical axis is near-ceiling, as concluded.

### One clarification (the standing tool is MORE correct than the throwaway)

Round-3 §2.4 attributed a **91-event "absent-our-root" residual** for Baroque HEAD. The tool's direct
count of absent-our-root scoreable events (oracle pair concurs, our root absent) is **0**. The full
per-event partition closes exactly: `scoreable 18348 = all_agree 10108 + music21_dcml_agree 3882 +
dcml_ours_agree 456 + all_differ 3902`. The "91" was a **bookkeeping remainder** from mixing the
per-event scoreable count with the *deduped* charged/floor set sizes (charged co-tick 20 + floor
co-tick 71 = 91), **not** absent roots. The tool keeps per-record and set-identity counts separate, so
its accounting is internally consistent and reports the true residual (0). The actual acceptance
numbers (charged/floor sets, all tiers) are unaffected → **no STOP**; recorded as a refinement.

---

## §3 — Corpus hygiene: the stale Baroque dir + a provenance STOP (user-ratified)

**Stale dir confirmed.** `tools/corpus/baroque/` held **ANCHOR** output: BIR **54**,
`bwv40.8@20160 = Bbsus/G` (despite the manifest stamping HEAD `dd418ecfed` — a dirty-tree generation).

**Regen (the standing path).** Built the current source (incremental; binary already current — no C++
changed this session, only Python added) and ran
`python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus/baroque`.
Result: **BIR 57**, `bwv40.8@20160 = Gm7` (the HEAD reading), manifest stamped `dd418ecfed`, 353/353.
The stale ANCHOR dir is fixed; the canonical Baroque dir now matches the documented BIR gate. ✓

**★ STOP surfaced — `baroque_kma_abs` ≠ plain HEAD Baroque.** §3's premise (a clean regen would match
`baroque_kma_abs`'s oracle tiers) is **false**, and I did not paper over it:
- The fresh plain regen returns the correct **chord** readings (BIR 57, Gm7) — chord roots are
  byte-identical to `baroque_kma_abs` in pitch-class terms (20/11040 region diffs, all enharmonic bass
  spelling like Db/C# = same pc, + 2 segmentation diffs on bwv297/bwv354).
- But the **key field** diverges in **4035/11040 regions across 250 stems**. `baroque_kma_abs` emits a
  **modulating** key (e.g. bwv10.7 `Gmin → Bbmaj`, the relative major over a g-minor span), whereas
  plain HEAD emits a **stable** key (`Gmin`). Plain HEAD reads keys *better* here; the kma mode
  over-modulates to the relative major, which the decomposition counts as KEY-HARD errors.
- This is a non-default **key-modulation ("kma") mode**, not reproducible by the documented standing
  path: it is **neither** plain `--preset Baroque` (all `Gmin`) **nor** `--joint-key-wiring` (all
  `Bbmaj`). It exists as a deliberate variant set for all three presets
  (`baroque_kma_abs` / `jazz_kma_abs` / `default_kma_abs`, all generated at `a03c2493bb`).
- **The reports were internally inconsistent:** Baroque used `baroque_kma_abs` (kma), but Jazz/Default
  used the **plain** dirs (their report numbers — Jazz 52.9/37.9, Default 46.4/45.1 — match plain, not
  `*_kma_abs`, which give Jazz 59.1/28.7, Default 54.5/31.2). Plain Baroque (46.8/45.5) ≈ plain Default
  (46.4/45.1), as expected since key emission is near preset-independent.

**User decision (ratified): plain-for-all (canonical).** The standing oracle-root baseline is anchored
on the flag-OFF plain HEAD corpora `tools/corpus/{baroque,jazz,default}` — internally consistent,
reproducible via `run_bach_preset.py`, matching the BIR gate and the just-regenerated canonical dir.
**Baroque is RE-STATED 54.9 → 46.8 % KEY** (the report's kma figure was a non-canonical key-mode
artifact). Jazz/Default are unchanged (their report numbers were already plain).

---

## §4 — The STANDING tiered baseline (plain-for-all; user-ratified)

Per-event, HEAD, plain corpora. **CHARGED and FLOOR are separate standing sets — never summed.**

| preset | charged (set) | per-rec | KEY | …HARD | …TONIC | OVER-GRAB | CHORD-ID | AMBIG | FLOOR (set) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Baroque** (`tools/corpus/baroque`, `dd418ecfed`) | **3861** | 3881 | **46.8 %** | 9.7 % | 37.1 % | **45.5 %** | **3.1 %** | **4.6 %** | **4285** |
| **Jazz** (`tools/corpus/jazz`, `41f7c65f63`) | **4065** | 4083 | **52.9 %** | 18.4 % | 34.5 % | **37.9 %** | **2.0 %** | **7.2 %** | **4276** |
| **Default** (`tools/corpus/default`, `41f7c65f63`) | **3894** | 3914 | **46.4 %** | 9.8 % | 36.6 % | **45.1 %** | **3.3 %** | **5.1 %** | **4285** |

Notes:
- Jazz/Default are at `41f7c65f63` (a byte-identical refactor ancestor of HEAD `dd418ecfed`); they
  "already match CLAUDE.md" (instruction §3) and reproduce the report numbers exactly — not regenerated.
- Plain Baroque charged-set is **3861** (vs 3862 on `baroque_kma_abs`): the −1 is a segmentation/spelling
  shift between the two corpora (chord roots are pc-identical; only the key mode + 2 segmentations differ).
- The flagged absent-our-root residual is **0** on all three (the true value; see §2 clarification).
- Full per-tier `stem@tick` case-identity sets emitted via `--emit-json` (the standing object Cowork
  verifies against).

**Reading the tiers (the whole point of the separation):** under the canonical plain corpus the per-event
charged error is **co-dominant KEY ≈ OVER-GRAB** (Baroque/Default a near dead-heat ~46–47 % each; Jazz
KEY 52.9 % > OVER-GRAB 37.9 %), with CHORD-ID near-ceiling (2–3 %). Within KEY, the **tonicization grain
(~35–37 %) dominates the hard key-detection band (~10–18 %)** in every preset — i.e. most of the KEY mass
is the local-vs-global *labeling* sub-problem, not raw mis-keying. (The kma corpus inflated Baroque's KEY
to 54.9 % by over-committing the relative major — exactly why the canonical plain corpus is the right
anchor.)

---

## §5 — Stop-condition compliance

- **MEASUREMENT-ONLY** — HEAD `dd418ecfed`; no production/analyzer/scoring/gate-threshold/`chordanalyzer`
  change. The tool reads corpora and emits case-identity sets. The only build was an incremental no-op
  (binary already current; no C++ edited). ✅
- **Reuse, not fork** — `validate_corpus_dir`, `compare_analyses`, `dcml_parser` imported verbatim. The
  key-mode parsers are tool-local glue (ported from the ratified throwaway, test-pinned). ✅
- **Tiers reproduce the read-only reports** — exactly, on the corpora the reports used (§2). The tool does
  **not** disagree with the throwaway on the same corpus. ✅
- **KEY-TONICIZATION never folded into KEY-HARD; charged never summed into floor** — structurally
  separated and tested. ✅
- **STOP honored, not papered over** — the `baroque_kma_abs` ≠ plain-HEAD provenance discrepancy was
  surfaced (not silently accepted, not forced by copying kma into the canonical dir, not reproduced by a
  guessed flag), characterized to root cause (a non-default key-modulation mode), and the standing
  baseline corpus was put to the user, who ratified plain-for-all. ✅
- **Baroque regen returned 57 / `bwv40.8=Gm7`** — ✅ (the §5 chord-reading stop is satisfied; the
  divergence was key-mode-only and is the surfaced finding).
- **Tests** — 15 new (`test_oracle_root_metric.py`) pin the 5-tier decision tree (incl. the
  KEY-HARD/KEY-TONICIZATION partition), the three key parsers, the charge/floor separation invariant, and
  `region_at`. Full metric suite **106/106** green (`python -m unittest discover -s tools/tests`). No C++
  suite run needed (no C++ change); the HEAD binary is healthy (regen 353/353, BIR 57). ✅

## §6 — For Cowork / user

- **Cowork** verifies at the committed object: the tool imports the three modules unchanged; the tiers
  reproduce §2 exactly on `baroque_kma_abs`/`jazz`/`default`; no production/scoring file touched; the
  standing plain baseline (§4) reproduces from the on-disk plain corpora.
- **User** has ratified the standing baseline (plain-for-all, §4). The Baroque re-statement
  (54.9 → 46.8 % KEY) is the one substantive change vs the read-only reports, and it is a *corpus
  correction* (canonical plain vs non-canonical kma), not a tool disagreement.
- **Deferred (separate steps, NOT started here):** the CLAUDE.md gate-policy rewrite (oracle-root primary
  / BIR secondary), the off-chorale genre-balanced builds, and any K1/K3/segmentation inference work.
  No push.

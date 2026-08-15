# CC Dossier — does `compare_rn` over-penalize the tonicization↔modulation equivalence?

> **READ-ONLY metric-design investigation. No production change, no metric change, no commit.** Reuses
> `compare_rn` / `compare_analyses` / `dcml_parser` + the 6-tonic-i `--dump-tonicization` diagnostic as
> analysis inputs. Base HEAD `2245aedf82`. Every claim tagged `[code]` (read source) / `[probe]` (ran it) /
> `[oracle]` (DCML When-in-Rome ground truth). Probe scripts: `tools/cc_tonicization_modulation_probe.py`
> (new, read-only) + inline aggregates over `tools/corpus/default` & `tools/corpus/default_6tonic`.

---

## §0 — TL;DR (the hypothesis is FALSIFIED, in an important way)

The user's hypothesis — *the metric over-penalizes a defensible equivalent notation* — is **wrong on both
halves**:

1. **The comparator does NOT over-penalize.** `compare_rn.classify_pair` already returns **`partial`
   (rn_agree, credited)** when we emit `V/d` and DCML writes the local-key `V`/`V6`/`V7` at the same
   sounding root `[code][probe]`. The only reason these cases score as `key_disagree` today is that
   **production emits the bare home-key numeral** (e.g. `II`) for the plain-triad ones — an **emission**
   gap, not a comparator penalty. Emitting the label moves 242 of the 409 from `key_disagree`→`partial`
   with **no crediting-rule change** (this population's rn_agree 31.8 % → 91.0 % `[probe]`).
2. **But the cases are NOT brief/either-valid equivalences — they are established modulations.** **92.7 %**
   (379/409) of the labeler's correct-key `/d` emissions on DCML-modulated regions sit in a local key DCML
   **confirms with a local V→I cadence**; **79.2 %** span ≥5 chords `[probe][oracle]`. Only **2.7 %**
   (11/409) are genuinely brief. So DCML's modulation is the **musically correct** analysis for ~97 %, and
   our `V/d`-everywhere notation is the **wrong** reading there.

**Therefore the gap is a REAL OUTPUT problem (≈97 %), not a metric artifact (≈3 %)** — and the metric is
if anything **lenient** (it gives `partial` credit to a notation that is musically wrong for a sustained
modulation), so a "credit-the-equivalence" rule is the **wrong** move (it would further *mask* the real
error). The genuine fix is a **local-modulation / KeyArea detector (Stage 4)** that lets the pipeline read
the established local key, which Stage 6 then expresses as a modulation rather than `V/d`.

**★ This generalizes to the whole S1 slice:** across the full corpus, **95.6 %** of the S1
"tonicization label-gap" (2001 / 2093 `key_disagree, =global`) is a **local-modulation** case (DCML local
key ≠ global), 83.2 % of those sustained ≥5 chords `[probe][oracle]`. The metric-design dossier's "S1 ≈
17.7 % tonicization label-gap" is **predominantly a local-modulation (Stage-4) gap, not a Stage-6
tonicization-label emission gap.**

---

## §1 — Task 1: how `compare_rn` scores these now `[code][probe]`

### 1.1 The comparator path (read at source)
`classify_pair` `[code` `compare_rn.py:296-360]` compares our `roman_numeral` to DCML's `chord_symbol`
(the **raw local-key token**, e.g. `V`, `V6`, `V7`), and both `root_pc`s. DCML's `root_pc` is the **actual
sounding root** resolved in the effective (relativeroot/localkey-folded) key `[code` `dcml_parser
_compute_root_pc / _resolve_effective_dcml_key]`. The buckets, probed directly on the four notational
configurations `[probe]`:

| ours RN (home key) | DCML chord (local key d) | roots | `classify_pair` → |
|---|---|---|---|
| `V/V` | `V` (loc G) | 2 = 2 | **partial** (rn_agree) |
| `V/V` | `V6` (loc G) | 2 = 2 | **partial** |
| `V7/V` | `V7` (loc G) | 2 = 2 | **partial** |
| `V/vi` | `V` (loc a) | 4 = 4 | **partial** |
| `II` (bare home numeral) | `V` (loc G) | 2 = 2 | **key_disagree** |
| `V/V` | `I` (loc G) | 2 ≠ 7 | **root_err** |

The mechanism: `V/d` normalizes to degree-base `V`; DCML local `V` also degree-base `V`; root matches →
`root_match ∧ quality_match` true; strings differ (`"V/V"` vs `"V"`) → **`partial`** `[code`
`classify_pair:337-342]`. So **the comparator already credits the tonicization↔modulation equivalence as
partial** — it does NOT miss it. It is only NOT credited when (a) we emit the *bare home numeral*
(`key_disagree`) or (b) DCML writes the local **tonic** `I` at a different root (`root_err`).

### 1.2 Score impact of the 409 (now vs if the labeler's `/d` were emitted) `[probe][oracle]`
Population = the 409 correct-key regions where the 6-tonic-i labeler emits `/d` AND DCML reads a local
modulation whose local tonic == our target degree.

| `compare_rn` bucket | NOW (production RN) | IF the label is emitted |
|---|---:|---:|
| partial | 130 | **372** |
| key_disagree | 237 | 0 |
| quality_disagree | 5 | 0 |
| root_err | 37 | 37 |
| **rn_agree (exact+partial)** | **130/409 (31.8 %)** | **372/409 (91.0 %)** |

Transitions: **237 `key_disagree`→`partial`**, 5 `quality_disagree`→`partial`, 130 `partial`→`partial`
(the dom7 cases the existing `formatRomanNumeral` labeler already emits), 37 `root_err`→`root_err` (the
DCML-local-tonic-`I` / alignment cases — never recovered by emission). **No crediting-rule change is
involved** — the existing comparator does this. So emitting the label is a real rn_agree *gain* on this
population, NOT a metric workaround. (Caveat in §3: that gain is partly the metric crediting a musically
wrong notation.)

---

## §2 — Task 2: brief vs sustained — is DCML's modulation correct? `[probe][oracle]`

Objective key-establishment signal = the DCML **local-key span** containing the aligned row: the maximal
run of consecutive DCML rows sharing that `local_key` (chord count + tick duration), and whether the run
contains a local `V→I` cadence. (When-in-Rome `Cad.` tokens are dropped by `parse_rntxt_file`'s
`_SKIP_TOKENS` `[code]`, so the local `V→I` within the span is the in-zone cadence proxy; the committed
cadence instrument is key-agnostic over *our* regions and not needed — the DCML span itself is the oracle
signal.)

**Labeler-fired population (the 409):**

| class | count | share | local V→I cadence in span |
|---|---:|---:|---:|
| **brief** (≤2 chords in local key) | 11 | **2.7 %** | 6 |
| moderate (3–4) | 74 | 18.1 % | 58 |
| **sustained** (≥5 chords) | 324 | **79.2 %** | 315 |

Span chord-count histogram `[probe]`: heavily right-tailed — modes at 4/8 chords, a long tail to 36.
**379/409 = 92.7 % of these "tonicization" cases sit in a local key DCML confirms with a V→I cadence.**
Examples `[probe][oracle]`: `bwv11.6 V/ii` in a **14-chord** E-minor span (cad ✓); `bwv133.6 V/V` in a
14-chord A span (cad ✓); `bwv108.6 V/VII` in a 14-chord A span (cad ✓). These are unambiguous
modulations; our `V/d` is the wrong reading.

This is structurally expected and confirms DCML's notation is **principled**: DCML assigns a `localkey`
(modulation notation) precisely when the tonicization is *established* (sustained + cadenced), and uses
applied `/d` notation (no key change) only for brief ones. The brief/either-valid bucket is therefore tiny
**by construction** — a truly momentary tonicization DCML writes as `V/d` and it would NOT be in this
"DCML modulated" population at all (it would be in the genuine S1-applied set the 6-tonic-i recall
measured).

---

## §3 — Task 3: metric-artifact vs real-output-gap sizing `[probe]`

**Two questions, two answers:**

**(a) Is the COMPARATOR over-penalizing?** No. It gives `partial` (rn_agree). The "penalty" is an emission
gap (bare home numeral → `key_disagree`), removable by emitting the label. So the **metric-artifact
bucket — cases the comparator wrongly scores as a miss — is ≈0.** A `partial` for `V/d` vs local `V` is a
defensible score (root + function agree; only the reference-key framing differs).

**(b) Is OUR OUTPUT wrong?** Yes, for the vast majority. Sizing:

| bucket | labeler-fired (409) | full S1-modulation (2001) |
|---|---:|---:|
| **brief / either-valid** (metric-creditable equivalence) | 11 (2.7 %) | 28 (1.4 %) |
| moderate (ambiguous middle) | 74 (18.1 %) | 309 (15.4 %) |
| **sustained / modulation-correct** (real output gap) | 324 (79.2 %) | 1664 (83.2 %) |

**Corrected S1 headroom (the generalization).** Full corpus, default preset, WiR-Bach `[probe][oracle]`:
matched 10109; rn_agree 45.7 %; `key_disagree` 27.5 % (2780); **S1 (`=global ≠local`) = 2093** (the
"tonicization label-gap", 20.7 % of matched). Splitting S1 by DCML local-vs-global:

- **S1-modulation (DCML local ≠ global): 2001 = 95.6 % of S1** — of which 83.2 % sustained ≥5 chords,
  15.4 % moderate, **1.4 % brief**.
- **S1-home-key (DCML local == global): 92 = 4.4 % of S1** — the genuine in-home-key
  tonicization/functional-label residue.

So the **single biggest precision slice (S1 ≈ 17.7–20.7 %) is ≈95 % a LOCAL-MODULATION detection gap**, not
a tonicization-label emission gap. The metric-design framing ("we emit `II` not `V/V`") was **incomplete**:
emitting `V/d` only band-aids the *dominant* chords of those spans to `partial`; the **bulk** of S1 is the
*non-dominant* local-key chords (I, IV, ii of d) that need the **modulation reading** (local-key degrees),
obtainable only from a Stage-4 KeyArea / local-key capability.

**Combining with the rest of the 6-tonic-i picture:**
- genuine plain-diatonic false labels (6-tonic-i): 6.4 % of correct-key `/d` — real but small, mostly
  segmentation/alignment.
- inversion recall gap (6-tonic-i misses `V6/5/V`, `V2/IV`, …): a recall ceiling of root-position-only
  figures + the strict next-region resolution requirement.
- **this finding:** ≈95 % of S1 is local modulation (Stage-4), ≈4 % home-key tonicization (Stage-6),
  ≈1–3 % brief/either-valid (already partial-credited).

---

## §4 — Task 4: the crediting rule — NOT warranted (and would be harmful)

A `compare_rn` crediting rule (e.g. *credit `V/d` in home key ≡ local-key-`V` when targets match*) is
**not recommended**:

1. **It buys almost nothing on the honest axis.** The comparator already gives `partial`; the only thing a
   rule could add is upgrading `partial`→`exact` for these. But the genuinely-equivalent (brief) bucket is
   **1.4–2.7 %**, so the upgrade is tiny.
2. **It would MASK the real error.** Upgrading `V/d`-for-a-sustained-modulation to `exact` would give
   **full credit to a musically wrong analysis** (95.6 % of S1). The metric is already lenient here
   (`partial` masks the modulation error); crediting harder makes the metric *blind* to the largest real
   output gap. **False-equivalence risk is the dominant consideration**, not the upside.
3. **Direction is backwards.** If anything, the metric should be made **stricter** so a *correct modulation
   reading* (our pipeline emitting local-key degrees once Stage-4 detects the key) scores **better** than a
   `V/d` band-aid — i.e. the metric should be able to *distinguish* the two, which today it cannot
   (`partial` for both). That is a separate metric-design step (a `localkey`-aware sub-tag of `partial`,
   analogous to the existing `--key-breakdown` S1/S2 split), not a crediting rule.

If a minimal metric refinement is wanted now, it is **diagnostic, not crediting**: split the `partial`
bucket by whether our reference-key matches DCML's `localkey`, so "credited-but-via-a-different-key-framing"
is *visible* rather than silently folded into rn_agree. This *exposes* the masking; it does not reward it.

---

## §5 — Recommendation

**The discriminator is warranted — but it is primarily a Stage-4 (local-modulation / KeyArea) capability,
sized to ≈95 % of S1, and its payoff is OUTPUT CORRECTNESS, not rn_agree.**

1. **Do NOT add a tonicization↔modulation crediting rule to `compare_rn`** (§4): the comparator already
   credits the equivalence as `partial`, the brief/either-valid bucket is ≈1–3 %, and crediting would mask
   the real error.
2. **Do NOT naively wire 6-tonic-i `V/d` everywhere.** It *would* lift rn_agree (242 `key_disagree`→
   `partial` in the fired set; more across S1) — but ≈95 % of that lift is the metric crediting a musically
   wrong reading (`V/d`-everywhere over an established modulation). That is **gaming the metric**, the
   opposite of the project's DCML-correctness goal.
3. **Build the local-modulation detector (Stage-4 KeyArea / local-key spans), feeding the Stage-6
   tonicization-vs-modulation decision.** Its job: detect the established local key (the objective signal
   is exactly what this dossier used — sustained span + local V→I cadence, **83 % sustained / 92.7 %
   cadence-confirmed**), so the pipeline emits a **modulation** (local-key degrees) for the sustained cases
   and reserves `V/d` for the genuinely brief ones. This addresses the real ≈95 % of S1; the 6-tonic-i
   predicate (sound, 6.4 % genuine FP) becomes the *brief-only* branch under that discriminator.
4. **Stage-6 tonicization labeling (6-tonic-ii) is the SMALL lever** here: the genuine in-home-key
   tonicization residue is ≈4 % of S1 (92 regions) plus the brief modulation cases (≈1–3 %). Worthwhile and
   low-risk, but it is **not** where the S1 headroom lives — the headroom is the local-modulation gap.

**One-line answer to the user's question:** the gap is **≈95 % a real output-quality problem** (established
modulations our notation gets wrong), **≈3–5 % a benign equivalence the comparator already credits as
partial** — so the metric is not over-penalizing (it is mildly *under*-penalizing), and the lever to build
is the **local-modulation/KeyArea detector**, not a metric crediting rule.

---

## §6 — Stop-condition disclosures
- **Did NOT build the discriminator or change `compare_rn`** — quantify + recommend only, per scope.
- **The brief-vs-sustained signal exists in-zone** (DCML `localkey` spans via `_dcml_time_spans` + the
  local `V→I` cadence proxy). The only absent signal — When-in-Rome `Cad.` tokens (dropped by
  `parse_rntxt_file`) — is **reported as a finding**, not guessed around; the span + local-V→I proxy is
  sufficient (92.7 % of cases carry a local cadence under it). No signal was fabricated.
- Numbers are `[probe]` over the committed `tools/corpus/default` (BIR-gate corpus) + the byte-identical
  `default_6tonic` (6-tonic-i diagnostic corpus); roots/keys are `[oracle]` (When-in-Rome rntxt via the
  pinned `dcml_parser`). READ-ONLY — no commit.

*Drafted by CC, 2026-06-15, base `2245aedf82`. Probe: `tools/cc_tonicization_modulation_probe.py`
(read-only). No production, metric, or commit change.*

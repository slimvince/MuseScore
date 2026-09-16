# CC Instruction — LAYER 3 / Increment B: the held-out ground-truth key/mode harness (READ-ONLY)

> Second increment of the L3 key/mode build (`cowork_layer3_keymode_impl_design.md` §2). Build the **direct
> key/mode-vs-RN-ground-truth** measurement — the metric the Increment-C rebuild will be graded against (design §6
> done-criterion) — with a proper **held-out split**, and fix the audit's caveats. **READ-ONLY: no production code,
> no behavior change, production byte-identical.** It is a measurement tool (extend the existing
> `tools/cc_layer3_keymode_baseline.py`), not a production change.
>
> **★ Context you do NOT have:** L3 = **key/mode** only (`C-major`, `F-mixolydian`). Ground truth comes from the
> Roman-numeral corpora, which encode the local key/mode (a RN is stated relative to a key). This increment does NOT
> change the resolver — it MEASURES it. The rebuild is Increment C.
>
> **★ No-assume:** confirm at source how the existing tooling (`compare_rn`, `dcml_parser`, the `.ours.json` / WiR
> `rntxt` / on-disk music21) actually surface key/mode; report what is and isn't available rather than assuming.

## §1 — Extract ground-truth key/mode per location
- From the RN corpora, derive the **local key/mode per tick/region**: DCML `localkey` (relative to `globalkey`) →
  absolute key/mode; and/or music21 `RomanNumeral.key`. Reuse `compare_rn` / `dcml_parser`; confirm at source which
  fields exist on disk (the audit noted on-disk music21 is **global-only** — establish whether local key/mode is
  recoverable, e.g. re-derived from the RN, or document the limitation).
- Align to **our** key/mode output (the `.ours.json` the baseline already reads) per location, per preset.

## §2 — The unambiguous / ambiguous split (the done-criterion's spine)
- **Unambiguous** = the ground-truth sources **concur** on the local key/mode (the DCML ∧ music21 policy-A
  analogue). **Ambiguous** = they differ (relative major/minor, modulation boundaries, passing-vs-structural).
- The audit used a **single-source proxy** (WiR `local==global`). **Replace it with a genuine two-source
  concurrence where the on-disk data allows**; where it does not, state precisely what proxy is used and its
  limitation (do not silently keep a weaker proxy). **Report the corpus split** (what fraction is unambiguous) per
  preset — this sizes the done-bar.

## §3 — The held-out split (out-of-sample — the audit's open item)
- Define a **fixed, documented train/test partition** by stem (deterministic + reproducible; if WiR/DCML publishes
  a canonical split, use it and cite it). Future tuning happens on **train**; the reported metric is on **test**.
- This addresses the audit's "no held-out split yet." All headline numbers are **test-split** numbers.

## §4 — The metric + the Jazz fix
- **The metric**, per slice/event, per preset: **full (tonic+mode) match on unambiguous**; on **ambiguous**,
  count correct iff the ground truth is **among our ranked alternatives** OR we **flagged** it ∧ the sources
  disagreed. (Today's resolver emits a ranked list — use it; the flagged-residual machinery is Increment C, so for
  now report the ambiguous bucket as "top-1 / in-top-k / neither" so the bar is measurable pre-C.)
- **Fix the Jazz 39% key-parse-fail** (audit caveat): enumerate WHY Jazz `.ours` keys fail to parse (the key-string
  forms — modes, enharmonics), repair the **parser/extractor** (read-only tooling, not production), and re-report
  Jazz on the now-parseable set. Until fixed, Jazz numbers are not trustworthy — say so.

## §5 — Gate
- **READ-ONLY:** no production `.cpp`/`.h`; `composing`/`notation`/snapshots/BIR/oracle **byte-identical**. Only the
  `tools/` measurement harness changes. If any production metric moves → STOP.
- **Reproduces the audit baseline** (~85.5% Baroque / ~91.5% Jazz unambiguous full-match) as a sanity check — now on
  the **held-out test split** and with **Jazz parse fixed** (expect the numbers to shift; explain the delta).
- **Documents** precisely: the GT extraction, the unambiguous definition + its data limitation, the held-out split,
  the metric, and the Jazz fix. Re-runnable.
- No corpus regen (read existing `.ours.json` + annotations).

## §6 — Workflow + deliver
Commit **locally (unpushed)**: the `tools/` harness only (read-only diagnostic). Leave held WIP unstaged. Write
`cc_layer3_incrementB_report.md`: the held-out direct key/mode numbers (per preset, unambiguous full-match + the
ambiguous bucket breakdown), the corpus + split sizes, the unambiguous-definition + its limitation, the Jazz fix +
its effect, and the byte-identity confirmation. Cowork verifies read-only + the split/metric methodology (esp. that
headline numbers are held-out and not in-sample); user ratifies; then push; then Increment C (the rebuild).

## §7 — Stop conditions
- Any production / behavior change, or a harness that alters analysis output → STOP (read-only).
- The on-disk data cannot support a genuine two-source unambiguous split → do NOT fake it; document the best
  available proxy + its limitation and surface it.
- The held-out split or the Jazz fix needs a corpus regen / production change → STOP and surface.
- Headline numbers turn out to be in-sample (no real held-out) → STOP (the done-criterion requires out-of-sample).

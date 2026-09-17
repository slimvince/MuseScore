# CC Instruction — Layer 3 key/mode: PUSH the unification increment, then build the CHARACTERIZATION SCAFFOLD

> The L3 decoder is built, the unification debt is closed, and Cowork verified `c453315faa` at source
> (byte-identical, nothing wired, the `pitchContextOverSpan` extraction is a pure relocation). **Do NOT start
> the wiring increment, and do NOT tune the decoder yet.** The next step is *measurement*: a scaffold that
> tells us which of the remaining errors are genuinely fixable before any sweep. This is a gate, not a fix.
>
> **★ No-assume / no-context guard:** this increment changes NO production code and wires NOTHING. It only
> adds read-only diagnostics + grading tooling on top of the existing `--decode-keymode` output and the
> held-out harness. If any production analysis output would move, STOP and surface it.

## §0 — Push the ratified unification increment to the fork (FIRST)
`c453315faa` is verified and ratified. Push it:
- Push **`origin` only** (`slimvince/MuseScore`). **NEVER `upstream`** (`musescore/MuseScore`) — that remote is
  disabled and must stay so. If any push would target `upstream`, STOP (hard stop).
- Confirm the held WIP stays unpushed because it is unstaged (the B2 trio, `STATUS.md`, WIP docs); only the 16
  committed files go. Report the resulting `origin/master` SHA.

## §1 — The characterization scaffold (four read-only measurements)
All four grade the **existing** `--decode-keymode` decoder output against the held-out RN ground truth, per preset.
You may make ONE additive change to the diagnostic: have `--decode-keymode` emit, per slice, the **confidence**,
the **`uncertain`** flag, and the ranked **alternatives** (tonic+mode) alongside the chosen key/mode — these are
already produced by the decoder (`SliceKeyMode`); the diagnostic just needs to serialize them. That emission is
diagnostic-only (the path already returns before `analyzeScore`), so production stays byte-identical.

### §1a — Calibration (the core one; it gates our "honest about ambiguity" claim)
Answer: *do confidence and the `uncertain` flag actually track correctness?* Compute, per preset, on the held-out split:
1. **Reliability curve** — bin slices by confidence (the sequence margin); report per-bin agreement-with-GT.
   Well-calibrated ⇒ low-confidence bins have low accuracy, high-confidence bins high accuracy (monotone).
2. **Uncertainty precision / recall on the error set** — of the slices the decoder got *wrong* vs GT, what
   fraction were flagged `uncertain` (recall); of the slices flagged `uncertain`, what fraction were actually
   wrong-or-structurally-ambiguous (precision).
3. **Alternative-recall** — on the wrong slices, how often the *true* key/mode is in the carried `alternatives`
   (the "we carried the right answer even when we didn't pick it" rate).
Output: the three numbers + the reliability table, per preset. (This is measurement only — do NOT move the
`uncertainThreshold` to improve the numbers; that tuning is the later, separately-ratified sweep.)

### §1b — Jazz-residual breakdown (we only ever characterized Baroque)
Bucket the Jazz misses (the ~21.5% gap at 78.5%) into: relative-pair, tonicization-boundary, modal-GT-
representational, structurally-undecidable (symmetric dim7 / whole-tone / augmented), genuinely-wrong-resolvable,
other. Same categorization already applied to Baroque. Output: the histogram, so we know how much of the Jazz gap
is fixable vs non-resolvable.

### §1c — Modal-bucket audit (guard against excusing real errors as "modal")
For the misses we attribute to "defensible modal reading the major/minor GT can't represent" (both presets),
inspect a sample and classify each as **confirmed-defensible** (the notes genuinely support the decoder's mode) vs
**actually-wrong** (the decoder is plainly wrong and "modal" is an excuse). Output: confirmed-defensible vs
actually-wrong counts within the modal bucket. This is the check that we are not hiding regressions behind the
modal-GT caveat.

### §1d — Granularity-robust metric (does the region-level win survive?)
Re-grade the decoder's key/mode at **per-beat (or measure-aligned) granularity**, not just region/slice
granularity, per preset — the existing gate metric is ~7× harsher at finer granularity, and we need to know if the
modulation-region gains hold up when scored where a consumer would actually read the key. Output: per-beat
agreement per preset, alongside the region-level numbers, with the delta.

## §2 — Constraints
- **No production change, nothing wired.** The decoder is not put on any live path. `composing` / `notation` /
  snapshot tests and `.ours.json` stay byte-identical. The only code change is the additive diagnostic
  serialization in §1 (confidence / uncertain / alternatives), which runs only in the diagnostic.
- **No decoder tuning.** Do not change cost magnitudes, `topK`, the window, or `uncertainThreshold`. This
  increment *measures*; the sweep that *acts on* these measurements is the next, separately-ratified step.
- **Reuse the existing harness.** Extend `tools/cc_layer3_keymode_baseline.py` / the decode driver; do not fork a
  second grading path (the unification rule — one grading path).

## §3 — Deliverables
- The grading/metric tooling (committed): the harness extensions + the additive diagnostic serialization.
- A characterization report `cc_layer3_characterization_report.md` (local, gitignored like the other `cc_*`
  reports — stays unpushed) carrying: the four sections' numbers per preset, and an explicit **attribution of the
  residual** (how much of each preset's gap is resolvable vs modal-GT-representational vs structurally-undecidable
  vs needs-a-later-layer). That attribution is what lets Cowork + user decide which improvements to actually make.

## §4 — Commit + push
- Commit the scaffold tooling **locally** as its own increment (separate from `c453315faa`). Leave held WIP
  (B2 trio, `STATUS.md`, WIP docs) unstaged; the `cc_*` report stays gitignored/local.
- **Push to `origin` only. NEVER `upstream`.** Report the new `origin/master` SHA and the committed file list.

## §5 — Stop conditions
- Any production analysis output moves, or the decoder ends up on a live path → STOP (this is measurement-only).
- You find yourself changing a decoder setting to improve a metric → STOP (that is the later sweep, not this).
- A push would target `upstream` → STOP (fork-only; hard rule).
- A metric needs chord/function evidence to compute → STOP and surface (out of L3 scope; note it for a later layer).

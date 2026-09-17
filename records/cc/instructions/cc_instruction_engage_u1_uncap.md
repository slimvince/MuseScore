# CC Instruction — Engage arc #5: U1 — UNCAP the production carry (Option A, scope-adjudicated)

> **ACTIVE DISPATCH (Cowork, 2026-07-06).** CC surfaced a STOP (excellent #6/#13 catch): "how many chord
> readings we keep" is governed by **three** independent `<3` caps, not one — the production in-memory carry
> (#1, `harmonicfunctionlayer.cpp:521`), the **measurement serialization** (#2, `batch_analyze.cpp:712/660`
> → `.ours.json`), and the **user display** (#3, `notationcomposingbridge.cpp:794`, a preference). Removing
> #1 alone grows the in-memory set but leaves every serialized/displayed surface capped at 3, because the
> measurement tool re-truncates what it writes.
>
> **★ USER-RATIFIED SCOPE = OPTION A:** remove **cap #1** (production carry) so the full ranked set is
> carried in memory; add a **default-off measurement dump** that serializes the full carry so we can SEE the
> real fan-out — with the **default `.ours.json` byte-identical**. **Leave cap #2** (measurement
> serialization) **and cap #3** (display). The cap-#2 lift + the one-governed-limit **#6 unification** are
> **DEFERRED to the Layer 5 engagement design** (recorded there — that is where the "should the full carry be
> the default serialized/measured surface" decision belongs, with a single deliberate re-baseline).
>
> **Greater-context note (CC could not see this):** the governing hard stop is now the **robust-unit stop**
> (post-R10-b), which is **winner-root-based** — carrying more alternatives cannot move it (winners
> unchanged). Under Option A the default `.ours.json` is byte-identical anyway, so both stops stay
> **trivially green** and **no re-baseline is needed.**
>
> **Why (principles):** cap #1 removal gives the dormant Layer 5 the full carry in memory
> (forward-provisioning — audit-OK); the dump makes the fan-out observable NOW, **byte-identically** (#16/#13
> — do not disturb the measurement substrate; minimize surprises); the three-cap #6 unification is recorded
> and deferred as one governed decision, not done piecemeal; moratorium-clear (forward-provisioning +
> measurement, no inference/winner change).
>
> **Read first:** CC's own Task-1 finding (the three caps, at source) · `cowork_information_loss_audit.md` U1
> · CLAUDE.md principle #12 (the exclusion elaboration).
>
> **Current state:** HEAD `5fa16b77e0`, branch `master`, fork-only, ahead 0. Both stops green (batch
> 52/24/52; robust sandwich identity-PASS). **Pending uncommitted Cowork edit in the tree:** the CLAUDE.md
> principle-#12 exclusion elaboration — fold it here.
>
> **VS Code bash rules:** append `; echo "exit:$?"`; large output → file + `head`. **Do NOT bash to read
> files** — use the file tools. **Build via** `powershell.exe -Command "Start-Process
> 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"`.

---

## Task 1 — DONE (record) ✓
The three-cap characterization is complete (cap #1 = the loop-bound `break` at `harmonicfunctionlayer.cpp:521`;
the full ranked `chosenPerBass` prefix flows to `HarmonicRegion.alternatives` at `regionanalyzer.cpp:992`;
caps #2/#3 the sibling truncations). Carry it into the report.

## Task 2 — remove cap #1 + add the default-off fan-out dump (carry-machinery only, #7)
- **Remove cap #1** — the `if (results.size() >= 3) { break; }` loop-bound at `harmonicfunctionlayer.cpp:521`.
  **Keep the `rc.score < threshold` gate.** The in-memory carry now holds the full ranked set (kept entries
  unchanged, same order, the previously-dropped tail added).
- **Leave cap #2 and cap #3 UNTOUCHED** (deferred / display preference).
- **Add a default-OFF measurement surface** that serializes the **full** carried set (reuse the existing
  fullspine/dump machinery if it can carry it; else a minimal additive default-off field). The **default
  `.ours.json` path must be byte-identical** — the dump is observable only under its flag.
- No new function-layer inference; confirm no further sibling cap on the in-memory carry.

## Task 3 — verify (byte-identical default; NO re-baseline)
1. **Build.**
2. **Default-path byte-identity:** the standard `.ours.json` (dump OFF) **byte-identical to HEAD across all
   352 × 3** (cap #2 unchanged). Prove the dump is default-off. ⟹ **both stops trivially green:**
   `characterise_bir_false` = **52/24/52** set-diff empty; robust sandwich **identity-PASS**.
3. **The fan-out (the user's "see what we have in reality"):** with the dump ON (scratch only), report the
   **full carried-set-size distribution** per slice ×3 presets — min / median / max / long-tail — the real
   fan-out cap #1 exposes. (Winner unchanged; the growth is the tail.)
4. **Suites:** composing 1101, notation 53 + 4 skip, pipeline_snapshot 11/11 — **no golden refresh** (default
   path unchanged).
5. **NO corpus write / NO re-baseline** (the frozen `tools/corpus/` + `tools/robust_stop/` are untouched — the
   default substrate did not change).

## Task 4 — commit + report + fold + push
1. **One revertible, provenance-stamped `feat(composing):` commit** (#14): cap #1 removal + the default-off
   fan-out dump + doc-sync.
2. **Report** `cc_engage_u1_uncap_report.md` (force-add): the three-cap finding, cap #1 removal, the
   default-path byte-identity proof, the fan-out distribution, the dump-default-off proof, all SHAs.
3. **Fold** (`docs(cowork):`): `STATUS.md` · `COWORK_HANDOFF.md` · `cowork_stage5_fitter_design.md`
   (engage-arc observation — **RECORD the three-cap #6 finding + that cap-#2 lift + the one-governed-limit
   unification are DEFERRED to the Layer 5 engagement design**, so it is not lost) · this instruction
   (force-add) · **the pending CLAUDE.md #12 exclusion elaboration edit** · update the U1 row in
   `cowork_information_loss_audit.md` to **RESOLVED — cap #1 removed; caps #2/#3 + the unification deferred to
   L5 engagement** (commit SHA).
4. **Push fork-only** (`git push origin master`) — never toward `upstream`/`musescore/MuseScore` (the
   `cfc7eb5e39` distribution HARD STOP).

## STOP conditions
- **Any diff on the DEFAULT `.ours.json` path** (dump must be default-off; the default surface must be
  byte-identical) ⟹ STOP.
- Any winner/root move (robust sandwich not identity-PASS, or batch ≠ 52/24/52) ⟹ STOP.
- Any change to cap #2 or cap #3, or any corpus write / re-baseline (all out of scope — deferred) ⟹ STOP.
- Any cross-layer change; any push toward `upstream`/`musescore/MuseScore`.

## Acceptance
Cap #1 removed (in-memory full carry), caps #2/#3 untouched ✓ · default-off fan-out dump added, default
`.ours.json` byte-identical (both stops green, no golden refresh, no re-baseline) ✓ · the fan-out
distribution measured + reported (the "see reality" data) ✓ · the three-cap #6 finding + the deferred
cap-#2/unification recorded for the Layer 5 design ✓ · one revertible provenance-stamped commit + report +
fold (incl. the CLAUDE.md #12 edit + the U1-resolved catalogue update) with SHAs ✓ · pushed fork-only,
upstream untouched ✓.

*Cowork, 2026-07-06. Engage arc #5 (Option A) — the production carry uncapped + the fan-out made observable,
byte-identically; the serialization + three-cap unification deferred to the Layer 5 engagement design. On
CC's report: Cowork verifies the default-path byte-identity at objects → the fan-out distribution feeds the
Layer 5 design (next).*

# CC instruction — carry-fix 2: the resolver emits SELECTED identities, never reconstructions (+ key-name grader fairness + E0″)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only), `C:\s\MS\BUILD_AND_TEST.md`.
> Also: `cc_e0prime_report.md` §4/§6 (your finding — the design basis), `cowork_layer5_function_design.md` §5.5/§7.
>
> **Dispatch state: ACTIVE (2026-07-02, on the ratified E0′ verdict).** Three tasks, commits 1–2 separate
> (one change-class each), Task 3 read-only. All dormant/byte-identical-on-production; local, unpushed. No θ, no
> constant tuning. Bash rules as always.
>
> **The ruling this executes (Cowork-verified at `0a88747e7f` objects):** your §6 finding is ratified and WIDENED —
> `candidateFromProg` also sets `bassPc = rootPc`, so the resolver's reconstruction flattens the committed
> **bass/inversion** on the pass-through path, not only the extensions. The legal basis is L5's own spec: §5.5
> "selection among carried readings, **never re-derivation**" applies to the *emitted struct* too, and §7 requires
> the committed identity carried **verbatim**. Reconstruction is a code-gap against both.

## Task 1 — resolver identity carry (commit 1)

The resolver's emitted `reading` must always BE an existing identity, selected — never rebuilt field-by-field:
1. **Pass-through** (a committed slice, `functionresolver.cpp:369` today): `r.reading` = the slice's own committed
   `decoded[i].chosen` **verbatim** (root, quality, committed bass/inversion, `extensions`, `naturalFifthPresent`,
   `extensionsKnown=true`).
2. **Carry/inherit/neighbour-based selections** (`carryThrough` and the §5.5 kind-rules where the selected reading is
   the prevailing/neighbouring harmony): carry THAT source's committed identity verbatim. Where the slice's own
   sounding bass is a decided fact of the slice (already carried on its candidates), you may pair the selected
   identity with the slice's own bass **only if** that pairing is itself a carried candidate; otherwise carry the
   source identity as-is. Declare which you implemented and why — do NOT invent a hybrid identity.
3. **Selections among carried alternatives** (the abstain-resolution and case-4 override paths): the selected
   alternative goes out verbatim, including its `extensionsKnown` honest-carry state (an unknown stays unknown).
4. `candidateFromProg` is retired or reduced to a pure reference helper — no call site may construct a reading whose
   fields did not come from one committed/carried identity. `ProgressionChord` itself stays `{rootPc, quality}`
   (the licensing test needs no more — minimality; the widening happens at the READING, not the grammar substrate).
5. Tests: pass-through preserves extensions+bass (a committed V65 emits `V65`, not `V`); an inherit slice carries the
   prevailing chord's seventh; an honest-carry alternative selection stays triad-level. Doc-sync: L5 design §5.5/§7
   note ("the emitted reading is the selected source's committed identity verbatim") in the same commit.
6. Gate: dormant-only (grep-proof, no production caller), suites green, NO golden refresh, flag-OFF corpus argument
   as in E0′ §8.

## Task 2 — grader-side key-name normalization (commit 2; measurement fairness only)

Per the E0′ §5 verdict (keyparse_fail = mode-label parseability, tonics correct): in the GRADER only, normalize the
chain's mode-qualified local-key names (`Xharm`/`Xmel` → `Xmin`; `XDor` → its parent-signature classification —
declare the mapping choice; `XPhrygDom` → `Xmin`) before the DCML key comparison, so key measures compare key
identity, not string parseability. Production emits unchanged. Document the full mapping in the script; report
before/after `keyparse_fail`.

## Task 3 — E0″ (read-only re-measure; report `cc_e0doubleprime_report.md`, HELD)

All 3 presets, fullspine regen with commits 1–2:
1. **#1 RAW/EXACT + the cap** — does the +8.2 close now (the deferred E0 prediction)? **Control expectations
   (changed from E0′):** `root_agree` must stay unchanged (roots never move — any movement = STOP); **triad-exact and
   robust MAY legitimately move UP** (the committed bass/inversion now survives the pass-through — an inversion-figure
   effect, not a leak) — report the delta and attribute it.
2. **#7 `V7/x`** — expected well above 36 (ceiling 316, gated now only by root/key correctness, not the carry).
3. **finalReading extensionsKnown share** — expected ≈100% on committed/inherit paths; report the residual.
4. **Key measures re-run under Task 2's normalization** — key_disagree/S1/S2 now comparable; report before/after.
5. Updated §5 better/worse rows for the re-measured respects only. End with the line count.

## Stop conditions

Any case in Task 1 that cannot be expressed as selection-of-an-existing-identity (would require synthesis) → STOP +
name it. `root_agree` movement in E0″ → STOP. Suites/gate movement → STOP. No θ anywhere.

**On your report: Cowork re-reads this instruction, reads the report in full, and verifies commit 1's emission sites
+ the E0″ headline at committed objects before ratifying.**

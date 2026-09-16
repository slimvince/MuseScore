# CC Instruction — J-key-ii: note-based home-key inference (demote the signature pin), DIAGNOSTIC + re-measure (HELD)

> **Ratification-gated, DIAGNOSTIC-ONLY, production byte-identical.** Second step of
> `docs/scoped_joint_design.md` §6 (key-axis), implementing the user-ratified J-key-ii direction
> (2026-06-15): **replace the home-fifths HARD backbone with note-based home-key inference (signature →
> soft prior), then re-measure — BEFORE any wiring.** This is the **safety fix** the J-key-i §7 stop
> requires (a hard constraint that pins wrong ~17% cannot ship). **No production resolve-path edit. No
> commit. Wiring is a SEPARATE later gate (J-key-iii), explicitly NOT in this step.**

---

## §1 — What this is (and is NOT)

J-key-i proved the **soft** constrained-joint key decision beats production (+3.5/+3.8/+12.2 pp) but fired
a §7 stop: the home pair is pinned from the signature **fifths**, which is a HARD lattice backbone and is
**unsafe at ~17 %** (56 stems — partial/modal "Dorian" signatures whose fifths ≠ the DCML key, e.g. bwv254/
265 = D minor notated 0 flats, structurally unrepresentable). J-key-ii **removes that hard pin**: the home
key becomes **note-inferred**, the notated signature a **soft prior**. Then re-measure, diagnostically.

**The load-bearing risk to measure (Cowork strategic flag):** the J-key-i win was achieved *with* the hard
signature backbone — it supplies the preset-stability (notably the +12 pp Jazz win). Demoting it could
**break the 17 % ceiling (good) OR loosen the anchor and shrink the win.** J-key-ii must therefore
**re-measure the win, not bank J-key-i's numbers.** The two outcomes that matter: (1) does the home-fifths
safety failure drop to ~0, and (2) is the soft win preserved-or-improved.

**NOT in scope:** wiring into production (`keyresolver`/`basisIndep`/rendered RNs) — that is **J-key-iii**,
its own ratified gate; the chord axis; the joint-coupling (J-key-i measured it inert on the key axis — keep
the toggle for continuity, do not invest in it); the learned dim7 emission. Any of these → STOP and surface.

## §2 — Scope (autonomous zone only)

All work in `src/composing/` + `tools/`. **Zero** `src/notation`/`src/engraving` edits. The producer stays
**diagnostic, parallel to production** (`--dump-joint-key` path only) — production must remain byte-identical.
If a clean implementation needs a production-path edit, STOP and surface.

## §3 — Build: note-based home-key inference (the demotion)

In `jointkeydecision.cpp`, replace the **forced signature home-pair** (currently `jointkeydecision.cpp:
187-205`: `homeMajorTonic`/`homeMinorTonic` from `keySignatureFifths` are the only non-span lattice states)
with a **note-inferred home-candidate set**:

1. **Home-key candidates from note evidence (aggregated over the whole piece, key-agnostic):** the
   collection-fit prior, the committed **cadence anchor** (`aggregateGlobalAnchor` — already a piece-global
   tonic+mode call), and the existing `analyzeKeyMode` local candidates. Propose a **small scoped set** of
   candidate home keys (keep the lattice small — e.g. the top note-ranked candidates ∪ the signature pair ∪
   the cadence-anchor key; do NOT enumerate all 24). The lattice is then **home-candidates ∪ modulation
   spans**, exactly as before but with note-inferred (not signature-forced) home states.
2. **The notated signature becomes a SOFT prior**, not a hard restriction: a bonus toward signature-
   compatible keys, magnitude **provisional `[empirical — Stage-5 fits]`**, small enough that strong note
   evidence overrides it (so a Dorian D-minor chorale can win D minor over the 0-flat C/Am pair). It is an
   additive term in the emission, never a lattice gate.
3. **Everything else unchanged:** cadence anchor / modulation / bass-is-root / declared-mode all stay SOFT
   and additive (no veto); the global key-path Viterbi + transition penalty unchanged; keep the soft-only
   vs soft+joint attribution toggle.

This **subsumes the deferred 4b note-triggered partial-signature detector (OQ3)** — the note-based home key
recovers partial-signature tonics without a declared-mode trigger. Note that after this demotion the key
axis may have **no hard constraints at all** (the signature is now soft; the candidate "pinned-chord ⊆ key"
was already measured unsafe → soft) — that is consistent with J-key-i (the key decision is soft; the hard
constraints live on the chord axis). Confirm and state it.

## §4 — Measure (all three presets), reusing the J-key-i instruments + two new checks

Re-run `cc_j_key_i_measure.py` (committed L1 `--key-breakdown`) on the regenerated dumps, and report vs
BOTH production AND the J-key-i soft baseline:

1. **Hard-constraint safety (the fix).** The home-fifths safety rate **must now drop toward ~0** (the home
   key is no longer signature-pinned). Report the new rate; if it is not ~0, the demotion did not take —
   STOP (§6). Confirm the **partial-signature stems recover**: of the 56 J-key-i stems (bwv254/265 the
   stress cases), how many now read the correct DCML key.
2. **The win — preserved or shifted?** key-acc / S2 / relative-pair / modulation-de-masking, **delta vs
   J-key-i soft AND vs production**, all three presets. This is the load-bearing measurement: the win must
   be **preserved-or-improved**. A material **shrink** (the signature anchor was load-bearing) is a finding
   to surface, not to wire past (§6/§7).
3. Keep the J-key-i tables (scope cross-check, per-case adjudication of changed regions vs production,
   soft→joint increment) for continuity.

## §5 — Byte-identity + suite gates (still diagnostic — must not perturb production)

Identical to J-key-i: capture production output before/after → **byte-identical** (`.ours.json` chord + key
axes); **BIR 57/23/57**; **snapshots pass, goldens unchanged** (no `--update-goldens` — no intended
production change; confirm the current count from STATUS.md); suites green (composing / notation / snapshots
— confirm current counts at source). Any production-output / gate / golden move = **STOP** (the diagnostic
leaked into production).

## §6 — Deliver: HELD + dossier, and the J-key-iii gate

Write `cc_j_key_ii_report.md` (gitignored, HELD, no commit) with: the safety-rate drop + partial-signature
recovery, the win delta vs J-key-i-soft and production, the byte-identity/suite confirmations, and a clear
**verdict on the J-key-iii (wiring) gate**: *proceed to wire* only if **safety ~0 AND the win is
preserved-or-improved**; otherwise surface the trade-off (e.g. safety fixed but win shrank) for a Cowork/
user decision on how to rebalance the signature prior before wiring. Cowork verifies at source; user
ratifies J-key-iii separately. Note any sandbox-bash noise (host-side Read/Grep authoritative).

## §7 — Stop conditions
- Production resolve-path / `src/notation` / `src/engraving` edit needed → STOP, surface.
- The home-fifths safety rate does **not** drop to ~0 after the demotion → STOP (the demotion didn't work).
- The soft **win collapses / materially shrinks** under the demotion (the anchor was load-bearing) → STOP,
  surface the trade-off — do NOT proceed toward wiring on a degraded win.
- Production output, the BIR gate, or a snapshot golden moves (diagnostic leaked into production) → STOP.
- The home-candidate set balloons (it must stay a small scoped lattice) → STOP, surface.
- Any attempt to wire into production in this step (wiring is J-key-iii) → STOP.
- Uncertain whether a key decision is correct → adjudicate vs DCML; if still unclear, bucket as
  convention-boundary and surface — never guess.

# CC Instruction: Stage 4a — declared-mode import fix (local engraving patch, discrete + measured)

## Authorization + decision

**User authorized (2026-06-14) a LOCAL engraving patch** to fix the MusicXML mode-drop. This is
a DISCRETE first Stage-4 step — *not* the full Stage 4 — so we verify it works in isolation
before building the graded prior / KeyArea on top (step-by-step: each layer correct before the
next). The upstream #9444 comment is drafted by Cowork **only after this fix is proven to work**.

**Off-limits exception granted for THIS change: `src/importexport/musicxml/internal/import/importmusicxmlpass2.cpp` ONLY.**
If the fix turns out to need ANY other engraving file (e.g. a `KeySigEvent` comparison helper in
`libmscore`/`engraving`), **STOP and surface that file for separate authorization** — do not
touch it unannounced. The resolver/consumer side (`src/composing/analysis/key/*`) is the normal
autonomous zone.

## The bug (verified at source — for your context)

`addKey` (`importmusicxmlpass2.cpp:5978`) dedups on **fifths only**:
`if (oldkey != key.key() || key.custom() || key.isAtonal())`. The `<mode>` is parsed correctly
(`key.setMode(...)`, :6074–6099) but when a 0-fifths key matches the prevailing fifths the whole
`KeySig` is dropped, taking the mode with it → `KeyMode::UNKNOWN` downstream. Export *does* write
`<mode>` (`exportmusicxml.cpp:2473–2497`), so this breaks round-trip fidelity. ~73 zero-sig Bach
stems lose their mode anchor (`cc_key_emission_headroom_dossier.md`). The maintainers' own
`// TODO only if different custom key ?` (:5977) flags the dedup as known-incomplete.

## The fix

Make the dedup also fire when the **mode** differs, so a mode-bearing key at matching fifths is
retained. Approach (verify the exact `KeySigEvent`/mode accessor at the call site — do NOT guess
the API; read it):
- fetch the prevailing `KeySigEvent` (not just the `Key` fifths) at `(staffIdx, tick)`, and add a
  `oldMode != key.mode()` term to the `if` condition;
- guard against spurious keysigs: a key that matches the prevailing one in BOTH fifths AND mode
  (and is not custom/atonal) must still produce NO keysig (no change for plain C-major scores).
- Keep the change minimal and localized to `addKey`.

**Document it as a never-pushed local patch** in CLAUDE.md's "Local patches — do not revert"
section, mirroring the Windows-Snap-fix entry: file/function, the fifths-only-dedup-drops-mode
rationale, the round-trip evidence, the upstream ref (#9444), and "do not let dependency updates
overwrite without approval."

## This is a DELIBERATE, MEASURED behavior change (it ends byte-identity for affected scores)

The just-ratified gate (Baroque 57 / Jazz 23 / Default 57) was measured on the **mode-dropped**
Score; restoring mode changes key resolution → `.ours.json` → possibly the gate. That is expected
and is the point — but it must be measured and ratified, not shipped as a side effect.

Verification (report all):
1. Build; **composing + notation suites green**; **MusicXML import round-trip tests** pass (or
   update with per-case justification — round-trip of a 0-fifths-mode file should now PRESERVE
   `<mode>`; add/point to a test that proves it).
2. **Confirm the change is isolated to empty-signature scores** — non-empty-signature scores'
   key resolution must be unchanged (the ~127 anchored-relative bucket must NOT move; this fix
   targets only the zero-sig bucket). Show a byte-diff scoped check.
3. **Does it actually work** (the user's bar): confirm the ~73 zero-sig stems now carry
   `declaredMode` (`declaredModeOrdinal != -1` via the key-candidate dump) and report the REAL
   key-inference improvement vs the projected ~349 reach — measured, not projected.
4. **Gate re-measure** Baroque/Jazz/Default (regenerate corpora at the patched build): report the
   full delta vs 57/23/57 with identity sets. A **BIR=false INCREASE is a hard stop for
   ratification** (surface it; expected direction is improvement/neutral on the zero-sig cases).
   DCML-adjudicate every key change.
5. **Pipeline-snapshot goldens**: refresh ONLY verified-correct changes (DCML-adjudicate each
   diff); report which snapshots moved and why.

## Held / report

HELD — `git add` ok, **no commit** (user commits). Report `cc_stage4a_mode_import_report.md`:
the patch (+ the CLAUDE.md local-patch entry), the round-trip test, the isolation proof, the
real key-inference improvement (3), the gate delta (4) with adjudication, the snapshot diffs (5),
and a tight **#9444 repro** (the round-trip: 0-fifths+`<mode>minor</mode>` → import → mode lost;
verified on our base — note whether you confirmed it against current upstream `master`) that
Cowork will use to draft the comment. Every number [probe], every root [oracle].

Stop conditions: the fix needing any engraving file beyond `importmusicxmlpass2.cpp` (surface for
authorization); a BIR=false **increase** on any preset (ratification stop); the change NOT
isolated to empty-signature scores (it's over-broad — report); the projected key-inference win
**failing to materialize** (report honestly — it would mean the import fix needs the graded prior
to be useful, reshaping the Stage-4 order). Do NOT build the graded prior / KeyArea in this run —
those are the next Stage-4 steps, gated on this one verifying.

# OI-7 — EG-6: Jazz validation status

> STATUS IS AUTHORITATIVE IN THE INDEX (OPEN_ITEMS.md) — this file carries narrative and provenance only and is NEVER the status of record

**Section A — STAGE-3 ENTRY GATE — blocks E4/L5 engagement (from `cowork_engage_arc_plan.md`)**

| OI-7 | EG-6: Jazz validation status — establish jazz GT corpus or de-scope Jazz correctness claims (T3-2) | arc plan; premise-debt T3-2 | OPEN |


---

**Dated note — 2026-08-02 (Cowork, user-initiated): A CANDIDATE ANSWER TO THIS ROW EXISTS — the
jazz realization loop.** Design at `cowork_jazz_realization_qa_instrument.md` (untracked until its
phase-2 adoption commit): realize lead-sheet chord symbols with MuseScore's own `RealizedHarmony`
(voicing × literal grid, THREE_NOTE ≈ the shell voicing; the realizer established per symbol class
against `chords_std.xml` before anything is graded, #19), infer from the realized notes, compare to
the symbols through a convention-equivalence layer — a scaled jazz vocabulary/segmentation QA tier
at zero annotation cost. Two-stage pipeline (user architecture): stage A realizes once per corpus
revision into per-tune per-variant file sets, manifest-stamped; stage B tests against the prepared
sets behind a validate-guard. Corpus: OpenEWLD (public domain) + the iRealPro corpus (CC BY 4.0);
**Effendi admitted by the user's explicit risk ruling 2026-08-02, hash-pin-only** (unclear-licence
class, the census mechanism). It tests the vocabulary axis, NOT real performance texture — human
annotation (D-205, OI-38/OI-56) remains the texture path. Slots into phase 2's exhaustion program.

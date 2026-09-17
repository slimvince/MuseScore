# CC Instruction — diagnose WHY the L3 decoder picks F over C (Mozart K279 + harmony fixture) — READ-ONLY, no fix

> **Context.** Verified symptom: production reads Mozart K279's opening as **F major** (golden `mozart_k279_1.json` =
> `"key":"F"`); correct is **C major** (the opening's B♮ is foreign to F; DCML = I). The same error shows in the
> harmony-pin fixture (#4/#5: a C triad read as `V` of F instead of `I` of C). **The CAUSE is not diagnosed.** The
> earlier "the deferred Step-2 scaleMembership reweight is to blame, the scale-membership lever fixes it" is a
> **hypothesis** — the lever was only ever measured on Bach, never on Mozart. This stage **diagnoses the actual
> mechanism** so we can name the correct amendment in the correct layer. **Knowledge, not assumption.** It proposes
> and applies **no fix**, and is **read-only** (any diagnostic dump must be production-byte-identical and stay
> local/uncommitted).

## §1 — The question
For the Mozart opening (and the harmony fixture), establish **precisely why F outscores C** in the L3 decoder, and
**localize the responsible mechanism** to a specific term / component / layer. The decoder chooses the best sequence
by **local-fit minus change-cost**, with a per-window scorer whose terms include **scale-membership**,
**key-signature-proximity**, **leading-tone**, and **preset bias**. The diagnosis must say which of these (or the
change-cost, or the emission weighting) is responsible — with numbers.

## §2 — What to dump (use existing diagnostics; add a minimal read-only dump only if needed)
Run the decoder on the Mozart fixture and dump, at the opening slice(s):
1. **The weighted pitch content the scorer actually saw** — the emission / per-pc weights over the window. **Does the
   B♮ appear, and with what weight** relative to F/A/C? (Is it metrically weak / brief?)
2. **Per-candidate local-fit scores** — **F major vs C major** (and the next few), at each opening slice.
3. **The local-fit term decomposition for F vs C** — scale-membership, key-signature-proximity, leading-tone, bias —
   **which term makes F ≥ C, and by how much.** In particular: **what is the scale-membership penalty F receives for
   the foreign B♮** — is it zero, small, or sizeable?
4. **The change-cost / sequence contribution** — is F the winner on **local-fit alone**, or does the **sequence /
   change-cost** tip it (e.g. F is entered and "cheap-to-stay" holds it)? Compare the per-slice argmax (no change
   cost) against the sequence pick: do **both** choose F, or only the sequence?

## §3 — The decisive contrast (why the unit test passes but Mozart fails)
The unit test `Composing_KeyModeAnalyzerTests.PrefersCMajorForCMajorPitchSet` **passes** — the bare scorer prefers C
for a clean C-major pitch set. Mozart (real, weighted content) → F. **Dump both side by side** and show exactly what
about Mozart's weighted content flips it: is it (a) the **weighting** (F/A/C dominate the metric/bass profile and the
B♮ is too weak to matter), or (b) a **missing/too-small penalty** (the B♮ *is* present with weight but F is not
penalized enough for it), or (c) the **change-cost**? This contrast is the crux — it separates "the scorer term is
wrong" from "the weighting starves the right term" from "the sequence overrides a correct local pick."

## §4 — The harmony-pin fixture (#4/#5)
Repeat the §2 dump for the synthetic C-triad fixture — why `V`-of-F over `I`-of-C. (It is a controlled case: a bare C
triad with no surrounding context, so it isolates the scorer/bias from the sequence.)

## §5 — Verdict (the mechanism — NO fix)
State plainly, with the numbers:
- **F wins on:** local-fit or change-cost (which);
- **the responsible term/mechanism:** e.g. "scale-membership penalizes F's B♮ by only X, far below F's local-fit lead
  of Y" — or "the B♮ carries weight ~0 in the emission, so no term can penalize it" — or "the change-cost holds F"
  — whatever the dump shows;
- **hypothesis check:** is CC's "missing scale-membership reweight" the cause? **Confirmed** (with the numbers) or
  **refuted** (and the real mechanism named);
- **candidate proper-layer amendment** — name it as a *candidate* (which term/component/layer), and whether it is the
  measured scale-membership lever or something else. **Do not apply it.** If the diagnosis points to more than one
  interacting cause, or a broader non-Bach weakness, say so.

## §6 — Constraints & stops
- **READ-ONLY / diagnosis only.** No fix, no golden refresh, no production change. Any dump you add is
  production-byte-identical (diagnostic path only) and **local/uncommitted**.
- The foundation HEAD (`1fb168f56e`), the working tree, and the stash `bc4fa79c4a…` stay untouched.
- `upstream` never; `origin` held.
- You start applying a fix (scorer term, reweight, golden) → STOP (that is a separate, gated step decided after this
  verdict).

## §7 — Deliverable
`cc_keyregression_diagnosis_report.md` (gitignored): the §2 dumps (weighted content, F-vs-C scores + term
decomposition, change-cost contribution) for Mozart and the fixture; the §3 unit-test contrast; and the §5 verdict —
the mechanism, the numbers, hypothesis confirmed/refuted, and the candidate proper-layer amendment.

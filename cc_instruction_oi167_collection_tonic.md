# CC instruction — OI-167: does the collection/tonic split hold for the engaged L4? (READ-ONLY disposition analysis)

**Dispatch author:** Cowork, 2026-07-13. **Type:** READ-ONLY premise verification + a disposition proposal
— the first design-pass step, and the foundational one. **No build, no `src/` edit, no golden refresh, no
retirement applied, no register re-scope.** The single deliverable is a report characterizing the two live
tonic-dependent L4 sites and proposing each one's disposition, for the design pass and the user to ratify.

**Why this is first (the premise under test).** The whole L3/L4 separation and the key-layer design rest on
one load-bearing causal claim: **the engaged chord layer (L4) needs the diatonic COLLECTION, not the
TONIC** — so it can be decided before the key is, strictly forward. The fact-dependency audit upgraded this
THEORY→FACT for the rebuilt `ChordSliceDecoder` (it takes no key; its key-consuming terms are pure
collection-membership tests), **but flagged two live TONIC-dependent sites that are not in the decoder**
(OI-167): Gate G-E and the `sparsechordrefinement` Aeolian lone-tonic guard. If either genuinely fires in
the engaged path and needs the tonic, the split does not hold and every design resting on it loses its
premise (#18). Under #18 (no design carries load on an unverified causal claim about our own system) and
#19 (a premise is trusted only after positive establishment), this must be settled before anything is built
on the split.

**Frame (the user's standing point, 2026-07-13):** the existing layer/method partition is an artifact of
how the code grew, not necessarily right for what the inference needs. So for each tonic-dependent site the
question is not only "does it fire" but **"is its tonic-dependence a genuine musical NEED, or a legacy
artifact that should be retired or re-homed so L4 is cleanly tonic-independent?"** — #7's layer-redesign
clause, applied narrowly to these sites.

Read first: `CLAUDE.md`, `OPEN_ITEMS.md` (OI-167, OI-102, OI-90, the R1 retirement text), the audit report
`cc_fact_dependency_audit_report.md` §3.6/§5.3, and the code.

---

## 1. Governing constraints

Read-only throughout. Apply the Premise Gate (#17): write the §5 predictions BEFORE checking; verify every
claim **at the code** (the actual firing conditions and call paths, not the register summary or memory);
label each finding **FACT** (code citation), **THEORY**, or **ASSUMPTION**. No self-invented labels. Be
adversarial (#15/#19): the point is to find out if the split genuinely breaks, not to confirm it — a
tonic-dependence you cannot prove dispensable is a STOP, not an assumption.

---

## 2. Task 1 — Gate G-E (`postscoringgates.cpp:379-385`)

Characterize it exactly: what it tests (the ii/iii/vii degree test), its tonic-dependence, when it fires
(preset-gated `preferMinorOverMajorAdd6`, Baroque ON), and what it changes (swaps the winner to a
HalfDiminished root — i.e. it changes the committed chord). **The decisive question: is it reachable in the
ENGAGED decoder?** The audit found `ChordSliceDecoder::decideSlice` runs `analyzeChord` with
`gateCtxOut=nullptr`, so the post-scoring gates never run in the engaged path — confirm this at the code.
If Gate G-E fires only in the LEGACY `analyzeChord`/`regionanalyzer` path, it is dormant for the engaged L4
and retires with that path (it rides R1 — but R1's text names Gate *letters*, not sub-rules, so confirm the
sub-rule is covered, per OI-167). State plainly whether Gate G-E threatens the split for the engaged decoder
(expected: no, it is legacy-only) or not.

## 3. Task 2 — the `sparsechordrefinement` Aeolian guard (`sparsechordrefinement.cpp:154-159`)

This is the genuinely open one (its retirement is undecided — OI-102; OI-90 re-tagged the file L4).
Characterize the guard: a single sounding tonic (an A) under A-Aeolian stays `Unknown`, while the same A
under C-Ionian — the identical collection — hardens to A-minor, so the verdict depends on the TONIC, not
just the collection. Establish:
- **Is `sparsechordrefinement` in the engaged decoder path, or the legacy path?** Trace the call sites.
- **Does the guard's tonic-dependence encode a genuine musical need** — a sonority that truly cannot be
  decided from the collection alone and legitimately needs the tonic — **or is it a legacy artifact** that
  the rebuilt decode path either already handles collection-agnostically or does not need?
- **What breaks if it is retired / re-homed?** If retiring it changes committed chords, name the cases
  (from the code and any existing test); if it is inert on the engaged path, say so.

## 4. Task 3 — the verdict and the disposition proposal

State, for the engaged L4, whether the collection/tonic split **holds unconditionally**, holds only if a
named site is retired/re-homed, or **genuinely breaks** (a site's tonic-dependence is a real need in the
engaged path). For each site, propose one disposition with evidence — **retire** (a legacy artifact that
dies with its path), **re-home** (the tonic-dependent decision belongs at a layer where the tonic is
legitimately available — name it), or **keep** (a genuine need — which means the split is conditional and
the design must account for it). Present these as proposals for the design pass, not decisions; the actual
retirement rides E4/OI-102, and the disposition call is the user's.

**STOP-and-report** if a tonic-dependent site is a genuine need in the engaged decoder — that is a real
partial break of the collection/tonic premise, exactly the finding this pass exists to surface, and it
changes the key-layer design; do not rationalize it away.

## 5. Premise Gate — predictions before checking (#17b)

Record first: whether you expect Gate G-E to be engaged-reachable or legacy-only; whether you expect the
Aeolian guard to be a genuine need or a legacy artifact; and whether you expect the split to hold, hold
conditionally, or break. A gap between prediction and finding is diagnostic (#3).

## 6. Deliverable

- **A report `cc_oi167_collection_tonic_report.md`**: the two site characterizations (code-cited, each
  FACT/THEORY/ASSUMPTION), the engaged-vs-legacy reachability of each, the need-vs-artifact judgment, the
  split verdict, and the per-site disposition proposals with their consequences.
- **Everything is a proposal.** Do not edit `ARCHITECTURE.md`, the design opening, or any register row's
  scope; do not retire or move any code; do not build. Record any register annotation the code contradicts
  as a proposed correction with evidence.
- **Commit:** the report as a `docs(cc)` fold + a `STATUS.md`/`cowork_handoff.md` note. Force-add this
  instruction file. Nothing else is written.

**On completion:** the foundational premise of the L3/L4 separation is either established (the split holds,
the tonic-dependent sites are legacy/retirable) or a real conditional/break is surfaced — and the design
pass can proceed to the OI-166 cadence-vote precision probe on a verified footing, with the key-layer funnel
still shut until the corrected layer assignment is ratified as a whole.

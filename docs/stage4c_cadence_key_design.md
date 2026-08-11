# Stage 4c Design — cadence→key: a key-agnostic global tonic anchor for the relative-pair decision

> **★ HISTORICAL RECORD — a design whose approach was FALSIFIED. Banner added 2026-08-11 under the
> FILING CONVENTION (`cowork_design_doc_template.md`, the user's Ruling 62 of
> `cowork_rulings_2026_08_11_fourteenth_stop.md`); `OPEN_ITEMS.md` OI-332 item (3). THE BODY BELOW
> IS UNTOUCHED (#12).**
>
> **What this document is a record OF:** a design, written 2026-06-14, for deciding the
> relative-major/minor pair from cadences detected without knowing the key.
>
> **The fate of its subject:** the approach is **FALSIFIED at its precision ceiling**, recorded one
> day later — register entry **D-290**, homed in `ARCHITECTURE.md`'s key layer, whose own words are
> that deciding the key from cadences found without knowing the key, one cadence at a time, was
> tested to its limit and cannot be made accurate enough to use; the remaining errors need either a
> long-range key decision or a different kind of model, not a better local cadence rule. **What
> survives the falsification is entered separately as D-616 and D-617 and is NOT falsified.**
>
> **So the design below is not a plan.** The banner is here because the document carried an inline
> supersession note elsewhere and none for this — so its omission read as an oversight rather than
> as a state, and a reader meeting the DRAFT banner first was told a design was awaiting
> ratification when its central approach had already been ruled out.
>
> **DRAFT — ratification-gated.** Cowork design, 2026-06-14. Follows the ratified Stage-4 redirect
> (`back_half_design.md` §4) and two measured results: **4b-ii** (`cc_stage4b_ii_report.md` — local
> reweighting CANNOT carry the relative-major/minor decision; the floor is the sub-1.0-hint near-ties and
> any local term strong enough to win them mode-absent overrides the correct hint mode-present — the §4
> structural coupling) and the **cadence→key investigation** (`cc_cadence_key_investigation_dossier.md` —
> the floor is 91% relative-pair; a cadence signal is *structurally decoupled* because it is a
> piece/section-scoped, note-derived proxy for the same global-key signal the declared mode supplied; the
> existing `detectCadences` is unusable — circular on `function.degree`, confidence-gated, key-blind — so
> NEW key-agnostic detection is required). Composing autonomous-zone. No code until ratified.

---

## §1 — The idea, and the one risk that must be measured first

**The signal.** Replace the lost declared-mode crutch with a **note-derived global tonic anchor**: detect
cadential resolutions *key-agnostically* (from absolute root motion + chord quality + leading-tone
presence — NOT from the key-relative `function.degree`, which is what made the existing detector circular),
aggregate them over the section/piece, and use the resulting tonic+mode anchor to break the relative-pair
tie — at **section/piece scope**, exactly the scope the declared mode used. Because it agrees with the
correct note evidence (a real cadence resolves to the true tonic), it **reinforces** the mode-present hint
rather than fighting it, and **supplies** the answer mode-absent. That is the decoupling 4b-ii's local
terms lacked.

**The risk.** The investigation's "≈91% / ~1259 regions addressable" is a **perfect-detection CEILING**
(hint-parity). A real note-derived cadence detector is imperfect; the **realized** fraction is bounded by
detection reliability, which is **unmeasured**. So this design's first obligation is to **measure realized
detection BEFORE wiring it into production scoring** — never bank the 91%. If a buildable detector cannot
correctly anchor a worthwhile fraction of the floor, that is a finding (richer detection, or the key axis
is a learned-emission / Stage-6 problem — the A-vs-B decision on the key axis lands here).

---

## §2 — The key-agnostic cadence detector (proposal — validated by 4c-i, not assumed)

Operates on the existing per-region `chordResult.identity` (absolute root pc + quality) and region pitch
content — **never `function.degree`** (key-relative → circular) and **never the resolved key**. For
consecutive regions (a → b):

- **Authentic cadence (the primary, strongest tonic anchor):** `root(a)` is a descending perfect fifth to
  `root(b)` (`root_b ≡ root_a − 7 mod 12` — a is the dominant of b), `a` is major/dominant quality (so it
  carries the leading tone = major third of a, a semitone below `root(b)`), and `b` is a stable triad.
  Then **`root(b)` is a cadential tonic** and `b`'s quality (major/minor) gives the **mode** — both derived
  with no key knowledge.
- **(Later/optional) plagal, half, deceptive** — weaker anchors; defer to a refinement step (4c-iii) unless
  4c-i shows authentic alone under-covers.

**Aggregation → the global anchor.** Collect cadences over the section (and the piece). The
**final/strongest cadence** is the dominant anchor for the global key (a piece resolves to its tonic);
multiple cadences vote, weighted by finality/strength. Output: a candidate **(tonicPc, mode, confidence)**
per section + a piece-level anchor. This is the note-derived replacement for the declared mode's global
signal.

**Key-agnosticism is the whole point** — it must run **before/independent of** key resolution and use only
absolute roots/qualities/intervals, so it can *feed* the relative-pair decision rather than depend on it.

---

## §3 — Feeding key scoring WITHOUT re-entering the §4 coupling (the load-bearing constraint)

The anchor must act like the declared mode did — a **section/piece-scoped global prior** on tonic+mode that
breaks the relative-pair tie — **NOT** a per-candidate local-salience term inside `analyzeKeyMode`'s
252-candidate window scoring. If it is added as just another local term, it re-enters the coupling and
fails like 4b-ii's levers. Concretely: apply a cadence-anchor bonus at the **resolver / section level**
(the scope the removed declared anchor occupied), gating the relative-pair choice; keep `analyzeKeyMode`'s
per-window scoring unchanged. The design's **decoupling proof obligation** (4c-ii ratification gate): show
empirically that the anchor **reinforces** mode-present (does NOT regress the cases the 1.0 hint already
gets right) while lifting the mode-absent floor — the measured confirmation of the investigation's
`[theory]` decoupling claim.

---

## §4 — Staged plan (the detection-reliability risk is staged FIRST)

- **4c-i — build a deliberately-simple key-agnostic detector + MEASURE realized detection (read-only on the
  scoring side).** Implement the §2 authentic-cadence detector as a standalone composing function +
  a read-only diagnostic that, per floor case, reports the detector's anchored (tonicPc, mode) vs the DCML
  global key. **Deliverable: the realized fraction** — of the ~1259 relative-pair floor regions, how many
  does this detector correctly anchor (precision/recall vs oracle/DCML)? Mode-present scoring is UNCHANGED
  (the detector is measured, not yet wired into the winner) → byte-identical gate/snapshots (a no-behavior-
  change measurement step). **This is the reality check on the 91% ceiling.** Stop/branch: realized fraction
  far below the ceiling ⇒ richer detection (4c-iii) or escalate the A-vs-B key-axis question — report, don't
  force the wiring.
- **4c-ii — wire the anchor into key scoring at section/piece scope (§3) + measure the floor improvement.**
  The behavior change: mode-absent S2 should drop toward the mode-present level on the relative-pair class;
  **mode-present must NOT regress** (gate 57/57/23 byte-identical *(superseded 2026-06-26: live gate now 53/24/53 — L3-wiring delta; CLAUDE.md authoritative)*, the §3 decoupling proof). DCML-adjudicate
  every moved gate case + snapshot. HELD, ratified. The OQ6 pass-bar is set here against the **4c-i realized
  fraction**, not the ceiling.
- **4c-iii — refine detection** (plagal/half/deceptive, modulation/section handling, voting) only against the
  4c-ii residual.

All composing autonomous-zone + `tools/` measurement. The only off-limits-zone artifact would be a
snapshot-golden refresh (standard ratified-change path). 4c-ii is the 3rd intentional behavior change (key
→ `basisIndep` → chord axis), gated/adjudicated/ratified like 4b.

---

## §5 — Measurement, targets, residual

- L1 `--key-breakdown`, **mode-present AND mode-absent**, all three presets (Baroque/Default load-bearing;
  Jazz key S2 unreliable per 4b-i/ii). The anchor is note-derived so it should lift the **mode-absent floor**
  toward the mode-present level on the relative-pair class — that lift is the headline.
- **Targets (relative-pair, addressable ~1259):** bwv365/bwv33.6 (already recovered in 4b-i — must stay
  recovered), **bwv64.2** (reclassified relative-pair, C-major global — should now recover; resolve the
  G-vs-C GT discrepancy in 4c-i).
- **Residual (NOT 4c's job → Stage 6 / B):** the ~454 "other"/different-key (mode-invariant; bwv83.5 the
  exemplar) + 164 keyfail. A large 4c residual is the key-axis A-vs-B evidence.

---

## §6 — Open design questions (decide before / during 4c-i)

1. **First-version cadence scope:** authentic-only (recommended — the strongest, cleanest tonic anchor) vs
   include plagal/half/deceptive now. Recommendation: authentic-only in 4c-i; add others in 4c-iii only if
   coverage demands.
2. **Anchor scope:** piece-level final-cadence anchor, section-level (modulation-aware), or both. The
   relative-pair decision is mostly global → start piece/section anchor; KeyArea (already in composing) is
   the natural carrier.
3. **Confidence/trust gating:** when is the cadence anchor strong enough to break the tie (and never to
   override clear note evidence)? Provisional; Stage 5 fits.
4. **Multiple-cadence voting:** finality-weighted vote vs last-cadence-wins.
5. **bwv64.2 GT discrepancy** (G vs C major) — resolve in 4c-i so the target set is correct.

---

## §7 — For user ratification
1. Approve the staged plan (4c-i measure realized detection FIRST → 4c-ii wire+measure → 4c-iii refine) and
   the §3 decoupling-preserving scope constraint.
2. Confirm §6.1 (authentic-cadence-only first version) and §6.2 (piece/section anchor).
3. On ratification, Cowork writes the 4c-i instruction (build the key-agnostic authentic-cadence detector +
   the read-only realized-detection measurement; mode-present scoring untouched → byte-identical; HELD).

## §8 — Stop conditions (carried into the 4c instructions)
- The detector needing `function.degree` or the resolved key (circular) — it must be key-agnostic; if it
  can't be, that is a finding.
- 4c-i realized fraction far below the 91% ceiling — report as the detection-reliability / A-vs-B finding;
  do NOT wire a weak detector into production.
- 4c-ii regressing mode-present (gate or mode-present S2) — the decoupling failed empirically; report, do
  not push through (this is where a non-decoupled anchor would surface, exactly as 4b-ii's coupling did).
- Any off-limits production edit beyond a DCML-verified snapshot-golden refresh — surface.

# Layer-5 (FUNCTION) spec review — the three-standards audit + sweep (record)

> Independent read-only audit of `cowork_layer5_function_design.md` against the three design-doc standards the L4 spec was
> held to — **specify by rule (no preference-shaped holes); code-free architecture body (§1–§12); standard vocabulary** —
> plus internal consistency, before the spec becomes the build contract. Verdict: *ready for sign-off after 7 fixes.* All
> 7 + a tie-direction rule were applied. This records what was found and fixed.

## Findings & fixes applied

**Standard 1 — specify by rule (the load-bearing one):**
1. **§5.2 plagal/evaded admit gate** — both cadence types had a *confidence* but no *feature trigger* (a preference-shaped
   hole). Fixed: plagal = subdominant-family→tonic at a phrase boundary with no intervening dominant; evaded = a set-up
   dominant whose expected tonic arrival is replaced by a non-tonic continuation / re-launched phrase.
2. **§5.2 imperfect-authentic totality** — "imperfect" was a non-exhaustive example list. Fixed: recast as the **complement**
   of "perfect" within authentic motion, with an explicit "branch is total" statement.
3. **§5.5 "insufficient" decider** — "where one is clearly favoured" left the criterion to preference. Fixed: same
   functional/cadential-plausibility + bass-prior decider as "close"; only the margin is the precision-phase constant.
4. *(polish)* **§5.3 tie-direction** — added the break-even rule: default to tonicization (direction fixed, magnitude deferred).

**Standard 2 — code-free body:**
5. **§15 code-token carve-out** — the banner claimed code-free prose but §15 names as-built identifiers for the build
   hand-off. Fixed: widened the banner to state §1–§12 is code-free while §13–§15 may name as-built identifiers + doc
   cross-references (the honest, consistent resolution).
6. **"O1" ledger token in the body** — removed from §1, §2, §9-D4 (kept the concept: "resolution by selection, not
   re-derivation"); the doc cross-reference to the L4 spec's §15-O1 remains only in the status banner.

**Standard 3 — standard vocabulary:**
7. **Gloss the carried project vocabulary** — added §12 entries for **class-(b) error** (the gate hard-stop term §10 leans
   on) and **ambiguity kind**, and confirmed in §5.5 that the kind names (transition / share-tone / relative pair / close /
   insufficient) are exactly Layer 4's carried kinds, not new coinages.

**Internal consistency:**
- **Fine-grain-override pointer** (the one real coherence wrinkle) — §8/§9-D7 cited §5.5 for the fine-grain chord override,
  but §5.5 was abstention-resolution (case 2) while the override is case 4. Fixed by adding a §5.5 clause making it the home
  of selection-among-carried-readings for **both** the abstained slices (case 2) and the confident-commit override (case 4),
  so the pointers are now accurate.
- Cross-references, the §8 four-case model ↔ §5.4/§5.5/§9-D7 "two instances", the §15 numbering (1–9), and the scope
  decision (Roman-numeral output; three-role derived-only) were all verified **consistent** — no change needed.

## Standing residue (not gating; tracked elsewhere)
The build-facing open items remain in the spec's §15 (the forward-recompute contract + the reduction/J-key-iii pins, the
cadence sub-unit, the two-path unification + predecessor rename, the section-grouping interaction, the backlog-notes pull).
These are *deferred work*, not spec defects.

**Result: the spec meets the three standards and is internally consistent.**

## Second pass — language-mechanical audit (every predicate subjected; every statement why/how-resolved; every concept defined)
An independent pass applied three mechanical tests to every sentence of the body §1–§12: (A) does each predicate have an
explicit subject; (B) does each statement survive a recursive "why/how?" until fully resolved in the text; (C) is each
concept defined. It found **12 genuine resolution gaps** — mechanisms the body *asserted* but never defined (several of
which §15 quietly admitted were deferred). All 12 were closed:

1. **A shared-definitions block (§5.0)** now defines, once, the five concepts the rules stood on without defining:
   **region** (the phrase-bounded span; exact recompute bound deferred to §15-3 only), **prevailing harmony**, **the
   progression** + **licensed (real) progression** (an *enumerable* list of functional root motions — the resolver's core
   evidence, previously invoked but never built) + **established next function**, and **resolution** (a concrete
   voice-motion event, not mere tone-presence).
2. **§5.2** — half-cadence admissibility (admit-at-lower-weight, not "preferentially"); the salience *combination* rule
   (weighted sum, direction fixed); "set up to cadence", "subdominant-family", and the leading-tone-chord substitute all
   given criteria.
3. **§5.3** — the no-cadence case reconciled (cadence = necessary **gate**; persistence = **hysteresis** among confirmed,
   measured in duration + cadential weight); the spelling-key-change test defined.
4. **§5.5** — "functional plausibility" made a fixed-feature score; "same-collection tonal-centre cues" enumerated; the
   undefined "voice-leading context" **dropped** (with a §11 note — the layer builds no voice-leading test).
5. **§5.6** — a fixed **precedence** for the four relational labels (aug6 → Neapolitan → applied → mixture; mixture the residual).
6. **§6/§3** — the section-grouping contradiction resolved (grouping is downstream, no feedback).
7. **§7** — function confidence given its components; **§8** — the recursion-closure operation named (a one-pass
   final-marking flag); **§12** — glossary entries added for every load-bearing term.

An independent **re-audit** confirmed all 12 closed, the new definitions **bottom out** (no fresh undefined term or
preference-hole introduced), and every glossary pointer resolves — verdict **fully resolved**. The lone soft edge
("section end" granularity) was then crisped to a structural-score-boundary predicate.

**Result: the spec is fully resolved under both passes — ready for the user's sign-off.**

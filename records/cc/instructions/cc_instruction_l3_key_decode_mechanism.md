# CC INSTRUCTION — Pin the key-decode mechanism at the code (the beam-drop question) — OI-141

> **Issued by Cowork, 2026-07-12.** The drift research grounding
> (`cowork_key_drift_research_grounding.md` — READ IT FIRST) ends on one deliberately
> open premise, and the user directed it be pinned before the key-layer design
> conversation opens: **where, mechanically, can the true key be lost?** The
> literature's decoders run the full key lattice — a key can only be outranked, never
> dropped from search. Our hand-traced failure (`bwv369@10080`, the diagnosis report)
> looked like a key falling off a short carried list mid-run. Which stage of OUR
> layer-3 pipeline actually loses it decides the shape of every fix. This session
> answers that at the code, read-only, with file-and-line evidence for every claim.
>
> **Read in this order:** `cowork_key_drift_research_grounding.md`, `OPEN_ITEMS.md`
> (session-start rule — OI-141 carries the question; OI-91/OI-97/OI-75/OI-81/OI-94/
> OI-78 are the related facts), `CLAUDE.md` in full,
> `cc_key_mode_inference_diagnosis_report.md` (the desk traces),
> `cc_l3_audit_pass1_report.md` (the certified map of this layer), `BUILD_AND_TEST.md`.
> Open-book, explorational: surprises are findings — except in your own tooling.
>
> **Cowork's written predictions (#17 — recorded here, before you look; each is
> checked and answered met/failed in your report):**
> 1. The per-slice EMISSION scoring evaluates ALL candidate key/mode states (the full
>    grid the mode-prior tables imply), not a pruned subset.
> 2. The SEQUENCE decode (`KeyModeSequenceDecoder`) is also full-lattice over its
>    states with transition/change costs — no search pruning inside it.
> 3. The loss therefore happens DOWNSTREAM of the search: at a greedy or
>    hysteresis-gated REGION-COMMIT stage (the audit named a greedy expansion step),
>    and/or at the CARRY truncation (`keyAlternatives`, a short top-list formed after
>    commit). If so, the drift is a commit/penalty problem, and widening or ranking
>    the carried list alone cannot fix it — it only serves downstream consumers.
> If any prediction fails — for example a genuine search-level beam exists — that is
> the finding, and it changes the design conversation more than a confirmation would.
>
> **REMINDERS:** READ-ONLY — no `src/` change, no constant tuned, no golden refresh,
> `tools/robust_stop/` and `tools/corpus/` written by NOTHING (scratch dumps
> allowed); you fix nothing and design nothing — findings become register rows and
> report sections (guiding principles 7 and 8); verify at the code and data, never at
> assertion — including the audit reports' own assertions: cite file and line fresh
> (principles 15 and 19); no self-invented labels or jargon — use the names the code
> and register already have; run the self-check over every diff before reporting
> done; shell rules (`; echo "exit:$?"`, redirect large output); git rules (stage
> only your own files by name, never `git add -A`, `git status` after every commit;
> the known carry `cowork_joint_key_chord_design.md` stays unstaged; `cc_*.md` is
> gitignored — force-add this instruction in your final commit); push to `origin`
> (the user's fork) ONLY, never `upstream` — the standing hard stop,
> `git remote -v` first.

## Task 0 — Preconditions and the register commit

0. **Commit Cowork's waiting edits** (the drift research grounding document and the
   OI-141 register update recording its delivery):
   ```
   git add OPEN_ITEMS.md
   git add cowork_key_drift_research_grounding.md
   git add -f cc_instruction_l3_key_decode_mechanism.md
   git commit -m "docs(cowork): the key-drift research grounding delivered (Temperley in-paper + the Contrapunctus dossier mined + field survey) + OI-141 updated + the key-decode mechanism instruction"
   ```
   (Force-add the grounding document too if a gitignore rule catches it.)
   Then `git status --short; echo "exit:$?"` — remaining: the known carry plus
   untracked scratch only; anything else, stop and report.
1. `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor f586a422d7 HEAD; echo "exit:$?"` — the second must
   print `exit:0`.

## Task 1 — The mechanism map (the core deliverable)

Answer each question AT THE CODE, with file and line for every claim and one
plain-language sentence per answer a reader who does not know the code can follow.
Where a constant is involved: its name, value, and fit status (in
`tools/param_manifest.json` or not).

1. **Emission:** per slice or segment, which key/mode states get SCORED? All of them
   (how many — enumerate the state space the mode-prior tables imply), or a pruned
   subset? Where is that candidate set formed?
2. **Sequence decode:** inside `KeyModeSequenceDecoder::decode` — is every scored
   state a lattice node at every step, or is the lattice restricted (to a per-slice
   top group, a windowed set, anything)? Where do the transition/change costs apply,
   which constants are they, and is the decode's optimum global (whole span) or
   windowed/greedy?
3. **Region commit:** where do key REGIONS get committed from the decode's output —
   the greedy expansion step the layer-3 audit named, the hysteresis margins, any
   stage that is irrevocable once taken? Name every point where a decision, once
   made, cannot be revisited by later evidence.
4. **The carry:** where is `keyAlternatives` formed, from what, capped at how many;
   at the point of its formation, does a per-alternative score or margin exist that
   is then discarded (the OI-75/OI-81 facts, re-verified at the current code)?
5. **Anchoring:** where do the notated key signature, a mid-piece signature change
   (OI-94), and the declared mode (OI-78) enter or fail to enter the decode?

## Task 2 — Re-trace the failures against the found mechanism

Take `bwv369@10080` plus at least two more absent-key or wrong-area cases from the
diagnosis artifacts (different scores, different shapes). For each, using scratch
dumps and the mechanism map: name WHICH stage loses or outranks the true key — the
emission rank at the relevant slices, the sequence decode's choice, a greedy commit
that locked before the evidence arrived, or the carry truncation — with the actual
numbers (scores, margins, costs) at the decisive point. If the stage you find
contradicts the diagnosis report's earlier phrasing ("drops off the beam"), say so
plainly and correct the record.

## Task 3 — Report, register, push

1. `cc_l3_key_decode_mechanism_report.md`: the mechanism map (every claim cited);
   each of Cowork's three predictions answered met/failed with the evidence; the
   re-traces with numbers; a closing plain-language statement of WHERE drift and
   stickiness mechanically live in our pipeline — mechanism only, no fix, no design.
2. Register discipline: update OI-141 with the pinned mechanism (the design
   conversation's first premise, now checked); correct any register row the findings
   contradict (say which, annotate rather than rewrite); any new discovery gets its
   own row in the SAME commit. Update `STATUS.md` (prepend) and the entry block of
   `cowork_handoff.md`. Plain language everywhere.
3. Commits: the Task-0 register commit; one `feat(tools):` ONLY if a scratch probe
   script is worth committing (else the fold carries the report alone); one
   `docs(cc):` fold. Run the self-check over every diff. **Push — user-authorized
   2026-07-12:** all local commits to `origin` only, after `git remote -v` confirms
   `upstream` push is still disabled; anything that would touch `upstream` is the
   standing hard stop. Confirm in the report: the pushed hash, `upstream` untouched.

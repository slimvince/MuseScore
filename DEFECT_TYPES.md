# DEFECT-TYPE CATALOG — the Living Signature List for Certification Audits

> **Created 2026-07-10 (session 36), user-directed.** The second half of the audit protocol
> (`cowork_audit_protocol.md` P7/P8): every problem TYPE ever discovered in this project, each
> with its detection signature — mechanical where possible. **Standing rule (mirrors the
> OPEN_ITEMS rule): every newly discovered problem TYPE gets a catalog entry in the same
> commit that records its discovery.** Types are never removed; a type made impossible by a
> structural fix is marked NEUTRALIZED with the mechanism that kills it (the kTemplateCount
> precedent). IDs are stable.

| ID | type (plain) | founding instance | detection signature | mechanical? |
|---|---|---|---|---|
| DT-1 | Unverified causal premise carrying load (Class A, #18) | F-B "θ accounts for it" | #17 ledger review + P4 behavioral contradiction | partly (P4) |
| DT-2 | Unestablished instrument / constant (Class B, #19), incl. tuned-against-a-broken-instrument | the pre-2026-06-13 constant mass; batch-gate era | per-constant provenance vs manifest license stamps; per-instrument establishment record | partly (stamp check scriptable) |
| DT-3 | Value-copied constants — one decision stored as two named literals that agree by history, not by reference | S8 key-decoder costs | script: equal literals across files + semantic pairing review | YES (candidate generation) |
| DT-4 | Silent overwrite of a committed field — revision without carrying the original (#12) | S14/S16 quality-from-key; the pedal clobber | enumerate all post-commit mutation sites of committed structs; each must carry-or-justify | YES (site enumeration) |
| DT-5 | Siloed / trapped derived fact — computed, then unavailable to other consumers | spelling (OI-15); the 17-item sweep | per derived value: consumer count by grep; 0–1 consumers → flag | YES |
| DT-6 | Duplicated derivation — the same verdict recomputed per consumer | FQ-1 four scans; bass-verdict ~60 sites | repeated predicate shapes; P3 contract direction | partly |
| DT-7 | Never-fires / always-fires mechanism — code whose designed population is empty or total | Gate K (0 firings, retired); the dim7 pin (4/214) | P4 fire-rate counters on the pinned corpus | YES |
| DT-8 | Scale-incommensurable comparison — quantities on different scales compared as if same | T1-3 / S19 (bounded vs unbounded) | type every confidence-like quantity; review every cross-type comparison | partly (inventory scriptable) |
| DT-9 | Unvalidated proxy→target substitution — a structural proxy read as a behavioral quantity | the 13.5 % coupled proxy vs 1.4 % fire-rate | #17(d) ledger review of every proxy | no (review) |
| DT-10 | One-sided insulation claim — "X cannot affect Y" without the false-negative path enumerated | the gate-insulation hypothesis (13→57) | #17(e) review of every insulation claim | no (review) |
| DT-11 | Hand-transcribed measurement number — a figure in a doc with no generated-artifact provenance | the R10-b 68.19/64.52/67.77 entry error | script: numbers in normative docs vs manifest sources (#17(f)) | partly |
| DT-12 | Stale anchor / dangling reference — file:line anchors or doc references that no longer resolve | scoring_model §4/§6 anchors; `backlog_chord_track_flag.md` | script: resolve every anchor and referenced path | YES |
| DT-13 | Interim exception without a wired retirement condition — a "bridge" nothing forces closed | the class-(a) two-tier exception (pre-register) | register review: every INTERIM row names its retiring gate | YES (register lint) |
| DT-14 | Gate/precondition mismatch — a mechanism guarded by a precondition its real population almost never satisfies (the generalized PC-1 shape) | the spelling-pin's chosen-quality gate | P4 per-branch counters: precondition pass-rate vs design intent | YES |
| DT-15 | Abstention/coverage-movable metric — a quality metric reducible by opting out rather than by being right | the EG-2 −16 % abstention artifact | per metric: does declining to answer move it? decomposition required | no (design review) |
| DT-16 | Raw-source interpretation outside the fact layer — a consumer re-reading the raw score/DOM with private eligibility rules (#7) | S2/S3/S4 walks | script: raw-DOM API calls outside L1 | YES |
| DT-17 | Silently-truncating capability — a specified trigger/handler that was never coded, failing quiet instead of loud | the L4 temporal-extension trigger (roadmap §2.15) | P3 spec→code: every specified behavior located or flagged | no (P3 review) |

*Usage: protocol P8 pass 2 sweeps the audited layer against every catalog row — mechanical
signatures run as scripts over the whole layer; review signatures applied row-by-row to the
P1 inventory. New types found in pass 1 are PROMOTED into this catalog before pass 2 runs.
Cross-refs: `cowork_audit_protocol.md` P7/P8; CLAUDE.md #17–#19; `OPEN_ITEMS.md`.*

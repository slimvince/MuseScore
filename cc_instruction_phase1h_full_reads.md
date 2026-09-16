# CC instruction — Phase 1h: continue the full reads of the LIVE-SPEC class (self-contained; may be handed over WITHOUT Cowork verification of phase 1g in between)

> **HANDOVER NOTE:** the user may hand you this immediately after the phase-1g triage report,
> unattended. Cowork's verification of phase 1g AND of this dispatch happens afterwards, at the
> objects, in one pass. You therefore SELF-ESTABLISH at start: working tree clean; all four
> guards PASS at HEAD (`gen_decisions_register.py --check` · `gen_cluster_dispositions.py
> --verify` · `gen_cluster_dispositions.py --check` · `python tools/open_items_split_check.py`);
> the triage artifact `tools/audit/decisions/phase1g_triage.md` exists and is committed. Any
> failure = STOP and report; do not repair another session's state.
>
> **Read first (every session):** `C:\s\MS\CLAUDE.md` IN FULL; `C:\s\MS\DECISIONS.md` (the
> INDEX); `C:\s\MS\STATUS.md`; `C:\s\MS\OPEN_ITEMS.md` (INDEX) with **OI-207**, **OI-268/OI-272**
> (rulings pending — collect evidence, never act), **OI-270** (the D-282…D-285 flag duty);
> `C:\s\MS\cowork_design_doc_template.md`; the phase-1g triage table.
>
> **Hard stops:** unchanged — origin only; no `src/` change; no golden/`tools/corpus/`/
> `tools/robust_stop/` movement; no fix, no design, no inference change; no `ARCHITECTURE.md`
> edits; new decisions NEVER self-ratified (RATIFICATION QUEUE); resolving an open question is a
> STOP on that item; a surprise is a STOP (#13); VS Code bash rules; measured feasibility stops
> accepted. **DO NOT touch these untracked Cowork files:** `cowork_candidate_findings_*.md`,
> `cc_instruction_*.md`, `tools/joint_estimator/invariance_probes_2026_08_02/`,
> `tools/joint_estimator/applied_chord_stake_2026_08_02/` — they are Cowork's pending work,
> commit nothing of them.

**Dispatch author:** Cowork, 2026-08-02, prepared in advance for the user's unattended window.

## The one governing constraint

**The exclusion list is NOT accepted.** The user has not ruled on phase 1g's proposed exclusions,
so NOTHING is excluded: this dispatch only READS MORE — full reads of documents the triage
classified LIVE-SPEC, in descending unresolved-cluster order. Reading a document that later turns
out excludable costs nothing (over-capture is free); excluding unread is the forbidden move.
Clusters in documents you do not read stay untouched.

## Task 1 — full reads, LIVE-SPEC class, descending cluster count

Work down the triage table's LIVE-SPEC rows (skipping any the phase-1g session already read in
full — its report names them). Per document: read IN FULL; decisions extracted verbatim by line
range; status/date/ratifier from the record only; register entries (data + regenerated files,
guards passing); homes judged as documentation-gap ROWS where owed; every new decision into the
RATIFICATION QUEUE; supersession chains entered, never skipped. Standing flag duties: anything
refining D-282…D-285; OI-268/OI-272 conduct evidence (collected only); measurement-tools
findings fenced in their own report section. Bulk rules only where licensed by a full read, each
numbered with its count. Continue document by document until capacity ends; commit per
change-class as you go (each commit leaves all guards green — the anchor-remap discipline, drift
report per citation, never a single assumed threshold).

## Task 2 — close

Final dispositions for every fully-read document's clusters; the manifest regenerated; all four
guards at the final tree; rows for gaps/conflicts; dated note on OI-207 with the updated
documents-read-in-full count (the honest coverage metric); `STATUS.md` pointer at the TOP;
push origin.

## Report

Documents read in full this session (names, cluster counts, yields); the cumulative
read-in-full figure against 143; the RATIFICATION QUEUE; the flag sections; the disposition
arithmetic; guard results; anomalies each diagnosed; the measured remainder. Standing self-check
before reporting.

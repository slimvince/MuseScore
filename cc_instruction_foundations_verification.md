# CC Instruction: Foundations verification — recheck the facts the back-half re-grounding rests on

## Context

The back-half re-grounding (`docs/back_half_design.md`, DRAFT) and its A-vs-B resolution
rest on a chain of findings, **some links of which are explicitly unverified or known
stale**. Per the standing mandate (be well-informed; never assume; double-check; old
truths may be inaccurate; data sources REALLY correct, not stale/misunderstood; docs
current so future sessions aren't misled; stick to the decided layers) — **verify the
foundations BEFORE the re-grounding is ratified.** This run does not build the Stage-4
fix; it confirms or CORRECTS the facts that fix is premised on.

Base `a4ae4a9203`. Method A–H; never-guess in full force (this task IS the double-check).
Read-only except the tiny music21-version record (Task 3) and the doc-currency edits
(Task 6), each called out. Every claim [code]/[probe]; a CORRECTION to any prior finding
is the most valuable output — say so loudly.

## Task 0 — RE-CONFIRM the instrument commit's byte-identity (not "as reported")

`a4ae4a9203` (the key-candidate dump) touched production files
(`keymodeanalyzer.{h,cpp}`, `keyresolver.{h,cpp}`) and its byte-identity is **why the
dump's §3 numbers are trusted to reflect production**. It was reported green but NOT
re-confirmed this turn (CC's own honesty note). Per the mandate (don't assume,
double-check), re-run the gate at HEAD: build; composing 505/505; notation 57/57;
pipeline snapshots 11/11 zero-diff; Baroque corpus sha256 0/353 vs the pre-instrument
baseline (`548adb7b2e`/`f8c6b3932a` outputs). If ANY diff: the instrument perturbed
production → the dump's term-attribution (§3) is suspect → STOP and report (it would
undermine the keystone evidence itself). Expected: all green, as recorded — but
confirmed, not assumed.

## Task 1 — THE KEYSTONE: verify the declared-mode-drop root cause (key-emission §5.1 gap)

The 349-region structural lever and the "hand-built emission has headroom" (A-confirmed)
conclusion both rest on: *MuseScore drops the notated `<mode>` for empty (0-fifths) key
signatures, so the resolver gets `KeyMode::UNKNOWN`.* This was proven only at the resolver
boundary. Verify it at the SOURCE:
1. **Read the actual import path** [code]: from MusicXML `<key><mode>` → engraving
   `KeySigEvent` → the bridge's `KeySigEvent::mode()` the resolver reads
   (`keyresolver.cpp:225`). Find WHERE a 0-fifths signature yields `KeyMode::UNKNOWN` /
   drops the mode. Is the mode (a) dropped at MusicXML import, (b) read but discarded for
   0 fifths, or (c) never carried by `KeySigEvent` at 0 fifths? Name the exact site.
2. **Confirm `<mode>` presence across ALL 73 zero-sig stems** [probe], not the 2 sampled.
   How many of the 73 actually carry `<mode>` in their MusicXML? The 349-reach assumed
   the mode is recoverable; if N of 73 lack `<mode>`, the reach shrinks — report the real
   number and which stems lack it.
3. **Explain bwv62.6** (the lone non-zero-sig non-anchored anomaly, §1.2) — is it a
   second, different mode-handling path? If so it may indicate the §1.2 correlation is
   not the whole story.
4. **Verdict:** is the keystone fact CONFIRMED (mode genuinely recoverable for ~349), or
   CORRECTED (smaller/different)? This determines whether the re-grounding's central claim
   stands. If corrected, quantify the new reach.

## Task 2 — Quarantine or refresh the STALE cross-corpus numbers

The "non-Bach root_err 50.7% / rn_agree 27.6% / ~2× harder than Bach" figures
(headroom dossier §1.4, metric-design §1.1, cited in the re-grounding §4) are **June-3,
pre-F1-metric, preset-uncertain** [doc]. We have been quoting a stale measurement as a
current fact. Resolve [probe]:
1. Re-run `compare_rn --cross-corpus` at HEAD `a4ae4a9203` with the committed (F-1/F-2-
   fixed) metric on the cross-corpus dirs that exist. Report the CURRENT numbers vs the
   stale ones; flag any material drift.
2. If the cross-corpus `.ours.json` dirs are themselves stale (old binary outputs),
   say so — and either regen-cost-box it or mark the cross-corpus picture explicitly
   "unverified at HEAD, do not quote as current" so the re-grounding's "~2× harder" claim
   is either confirmed or quarantined.
3. State plainly which of the re-grounding's quantitative claims are Bach-gate-set (solid,
   reproduced at HEAD) vs non-Bach (stale until this task).

## Task 3 — Pin the music21 provenance (OQ-V1, the unrecorded version)

The `.music21.json` generator version is recorded nowhere committed (corpus audit C2).
The DCML-only metric doesn't depend on it, but the three-way (the "4.8% vertically
fixable" / music21-filter sizing) does. [probe] establish the version (the corpus-hygiene
pass found `<software>music21 v.9.9.1</software>` in the `.xml`; confirm it stamps the
`.music21.json` provenance too) and record it in a committed location
(`tools/corpus/README.md` is gitignored — put it in `REPRODUCIBILITY.md` or the manifest
schema). Freeze-by-fiat if unrecoverable. Tiny committed change OR a documented freeze.

## Task 4 — Verify "key feeds chord emission" is CURRENT post-3.3 (not a stale truth)

The re-grounding says Stage 4 ends the byte-identity era because the resolved key flows
into `analyzeChord`'s `basisIndep` (via `snapshot.keyTonicPc/scale`). Stage 3.3 migrated
signals between oracle and pipeline. [code] Confirm the key→emission path is still as
described at HEAD: does the resolved `localKeyFifths/Mode` still feed `analyzeChord`, and
does the key still enter `basisIndep` (diatonicRootBonus / scale-dependent terms)?
Confirm or correct — if 3.3 changed how key enters scoring, the "Stage 4 is a behavior
change on the chord axis" framing must be updated.

## Task 5 — Layer-separation check for the proposed Stage-4 fix

The mode-drop is an ENGRAVING-IMPORT fact surfacing in COMPOSING analysis. The fix is a
Dependency-Rule (§3.3) decision: (a) read the MusicXML `<mode>` in the notation BRIDGE
and pass it into the composing resolver (respects the layer — composing stays
notation-agnostic), vs (b) fix the engraving keysig import (deeper, touches engraving).
[code] State which respects the decided layers, and flag if either would force composing
to depend on notation/engraving import internals. (Design input for the Stage-4 build;
do not implement.)

## Task 6 — Doc currency (so future sessions aren't misled) — committed

The mandate "documents up to date so cc will not be misled" — clear the known-stale items
that could mislead the next session. [code] verify-then-fix:
1. `decoder_design.md` §11 Δ=+7a row erratum (the "low-scoring transient" line falsified
   in the 3.2 design — the standing queued erratum).
2. Sweep `implementation_roadmap.md` / `STATUS.md` / `COWORK_HANDOFF.md` for any claim
   now contradicted by this session's findings (beam, key-path, the meta-principle) that
   a fresh reader would take as current — list them; fix the clear-cut ones, flag the
   judgment calls.
3. Confirm the rider queue (Baroque-13 set pinned, freeze-anchor, the 2.1 ARCHITECTURE
   file-map) actually landed in `4f1754c26c` or are still open — close the ledger.
One docs commit; explicit staging; never `muse`.

## Deliverable — `cc_foundations_verification_report.md`

Per task: CONFIRMED / CORRECTED / QUARANTINED, with [code]/[probe] evidence. Lead with
Task 1's verdict (the keystone). A consolidated "facts the re-grounding can stand on"
list vs "facts corrected/quarantined — re-grounding must be revised" list — that list is
what gates ratification.

Stop conditions: Task 1 CORRECTING the keystone (the 349 lever is materially smaller/
different) — report immediately, it reshapes the A-vs-B resolution; any "current" doc fact
found contradicted that a build would have relied on; any layer-violation the proposed fix
would force. Do not implement any fix — this run verifies and corrects the record only.

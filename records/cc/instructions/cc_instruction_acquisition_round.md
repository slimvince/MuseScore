# CC INSTRUCTION — the acquisition round: union-search-approved pickups + the PDMX symbol count (2026-07-04)

**Status: ACTIVE DISPATCH (the only open instruction). Executes the user-approved disposition of the union
search round (`cowork_union_search_record.md`, status banner = the rulings). Clone + hash-pin + inventory +
bookkeeping, the Wave-3 mechanism verbatim — plus ONE read-only counting measurement (Task 3). NOTHING under
`src/`; no production/tool code changes; the frozen gate corpus stays byte-untouched.**

## Mandatory reads BEFORE any work

1. `CLAUDE.md` (bash rules; the gate = the 53/24/53 case-identity sets) + `STATUS.md` header + 22k (end).
2. `cowork_union_search_record.md` — the record this dispatch executes (§1–§5 per-need findings + the
   disposed §6). Every URL/size below re-verifies against the actual data at clone time.
3. `tools/REPRODUCIBILITY.md` (`corpora/gt|plain/` sections) + `cowork_score_census.md` §3/§4/§8c (intake
   rule: full N1–N20 needs note per row) + `cc_corpus_wave3_report.md` §0 (the row conventions).

## Standing rules (as Wave 3 / the addendum)

Full-vector N1–N20 `needs_coverage` per row · every GT layer inventoried · claim verification at the cloned
data (mismatches reported, not accepted) · license recorded, NC/unclear/no-license → hash-pin-only ·
dedupe-by-work overlaps recorded · all beds held-out · per-source failure = a report line, not a wave STOP.

## Task 1 — N9 voice-separation beds (three clones)

1. **piano_svsep** — `github.com/CPJKU/piano_svsep` (ISMIR 2024). Clone + pin. Verify at the data: the GT
   graph dataset over DCML-corpus piano scores (record §1 says 393 pieces / 77 test; per-note voice + staff
   + chord labels as graph edges) — report what the repo ACTUALLY ships (the dataset may live in a release
   artifact or a loader; if the data is fetched at runtime, pin what is pinnable and record the fetch path).
   Code MIT; the underlying DCML scores are per-repo licensed (we hold them — record the overlap by work:
   which of the 393 map to our `tools/dcml/` clones). The companion "jpop" set is explicitly NOT public —
   record that as an access-path line, do not chase it.
2. **MCMA** — `gitlab.com/skalo/mcma` (CC BY 4.0). Clone + pin. Verify: ~475 files (239 3-track / 153
   2-track / 83 4+); voice = one-per-track, hand-exploded Baroque counterpoint. Record the overlap by work
   with our held WTC/Bach material.
3. **vocsep_ijcai2023** — `github.com/manoskary/vocsep_ijcai2023`. Clone + pin. Verify: the 1,054-graph
   collection (chorales/WTC/Inventions/Haydn quartets); license = whatever the repo actually states (record
   §1 says unstated → hash-pin-only). Note in its needs_coverage: notation-derived voice labels — weaker as
   inference GT except the WTC fugues (the record's caveat, carried verbatim).

## Task 2 — the other approved pickups

1. **Mikrokosmos-difficulty** — `github.com/PRamoneda/Mikrokosmos-difficulty`. Clone + pin. Verify: 147
   pieces / 3 classes / MusicXML present. NO license file (record §3) → hash-pin-only. Needs: N14 primary.
2. **GuitarSet (annotations only)** — Zenodo record 3371780, CC-BY 4.0. Pinnable-source rule: download +
   sha256-pin the ANNOTATION artifact (the JAMS zip — instructed+performed chords, per-string midi notes,
   beats, keys). The audio artifacts are NOT our material — record their existence + URL, do not download.
   Verify: 360 excerpts. Needs: N12 (instructed-chart vs performed-comping pairs).
3. **Batik-plays-Mozart** — `github.com/huispaty/batik_plays_mozart`. Clone + pin. Multi-need intake (the
   record's §2 star): verify the harmony + cadence annotation layers (N1/N4 — 12 Mozart sonatas), the
   score-to-performance match files, and the `trill-mark`-anchored insertion structure the record names as
   the recoverable-trill-realization path (N13-partial — VERIFY the structure exists on one example file,
   e.g. a kv279 match file; do NOT build any extraction). License = whatever the repo states (record §2
   says none visible → hash-pin-only).
4. **Recorded rows (no clone):** CIPI (Zenodo 8037327 — status=gated, research-only, USER access request
   pending; needs N14 primary, MusicXML included per record) and PSyllabus (Zenodo 14794592 —
   status=recorded; 7,901 exam-board-labeled recordings, NO symbolic scores; N14-adj). Both get full
   needs_coverage rows so intake scoring exists when either lands.

## Task 3 — the PDMX `<harmony>` counting pass (read-only measurement; the N12 lever)

Against the ALREADY-HELD PDMX copy (registry row `pdmx`; locate via the registry/REPRODUCIBILITY — do not
re-download): count, over the PD MusicXML files,
1. scores containing ≥1 chord-symbol element (`<harmony>` in MusicXML; PDMX's MusicRender `ChordSymbol` if
   the JSON is the held form — say which form you measured);
2. of those, how many have a realized multi-voice texture (report the proxy you use — e.g. >1 staff/part,
   or a notes-per-onset threshold — and its value; pick the simplest defensible proxy, state it, do not
   tune it);
3. the joint table: total scores · with-symbols · with-symbols-AND-multi-voice, plus a small breakdown by
   PDMX's own metadata if cheap (e.g. its rating/complexity buckets).

**Rules:** the counting script is scratch (`scratch_artifacts/`, untracked); READ-ONLY over the held copy
(no re-packaging, no extraction of a subset, no new corpus dir — the subset acquisition, if any, is a
future user decision on these numbers); if the held PDMX form turns out not to contain the raw
MusicXML/mxl needed to answer (1), STOP the task (not the wave), report what the held form contains and
what answering would require. The result lands in the report + the `pdmx` registry row's needs_coverage
note (N12: measured symbol-bearing subset).

## Task 4 — bookkeeping + report + fold

- Registry: additive `wave3_sources` rows via the generator (deterministic, two-run byte-identical);
  pins/sha256 read live; full needs notes.
- `cowork_union_search_record.md` §1–§4: append an "ACQUIRED @ <pin>" (or gated/recorded) annotation per
  item — the record doc is the natural provenance home (the audit-§7.1 precedent).
- Census §8c: N9/N12/N14 state columns updated to acquired/measured states.
- REPRODUCIBILITY.md + score_inventory.md: clone/pin commands + bed notes.
- Report `cc_acquisition_round_report.md` (force-added): per-source verification, the Task-3 table, the
  piano_svsep↔DCML and MCMA↔held-material overlap notes, reuse-vs-new + what retires (expected: nothing),
  **commit SHAs mandatory** (report cites prior SHAs per precedent).
- **The `docs(cowork):` fold — exactly this list, surfacing anything else dirty:** `STATUS.md`,
  `cowork_handoff.md`, `cowork_score_census.md`, `cowork_union_search_record.md`,
  `cowork_product_tool_register.md`, `cowork_voiceleading_axis_design.md`, force-added
  `cc_instruction_acquisition_round.md` + the report. (The register and VL-design files carry the
  union-search disposition edits — T-32 license caveat; §15-4 update + §15-10.)
- Suggested commits: (1) clones/pins + registry · (2) the Task-3 measurement report material (if any
  tracked artifact beyond the report, keep it in the report itself) · (3) the fold + report. Local,
  unpushed, fork-only.

## Acceptance (ALL required)

Every Task 1–2 source cloned+pinned+verified OR precisely recorded (gated/unavailable); Task-3 table
delivered with the stated proxy (or its STOP correctly reported); registry deterministic; **gate sandwich:
53/24/53 case-identity set-diff empty both directions ×3, before AND after**; nothing under `src/`, no
tool-code changes (the scratch script is untracked and read-only); held-out discipline stated per row.

## STOP conditions (global)

Anything would touch `src/` or tracked tool code; the frozen gate corpus or the held PDMX copy would be
modified; a license genuinely ambiguous about LOCAL mirroring; the Task-3 script wants to become an
extraction/subset-builder (measure only); the registry regen stops being deterministic.

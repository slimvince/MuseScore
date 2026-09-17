# CC Instruction — Refactor #1 (DESIGN): chordanalyzer.cpp layer-split — READ-ONLY map + plan

> **The PIVOT to (b) — architecture first (user, 2026-06-16).** We have been improving inference on the
> un-refactored pipeline; we now establish the target architecture's **single-responsibility layers**, which
> unlock the layer-by-layer audit AND give later inference work a correct foundation. The first refactor is
> the **`chordanalyzer.cpp` file-split** — a **byte-identical** structural refactor (pure code movement, no
> logic change). This step is the **READ-ONLY design**: map the file, define the target decomposition, and
> plan the split as a verifiable byte-identical sequence. **No code moves in this step.** The non-chorale /
> bridge-anchor inference work is **on HOLD** — it resumes on the refactored architecture.

---

## §1 — What this is

`chordanalyzer.cpp` conflates several chord-side layers in one large translation unit (the vertical oracle,
the competition/function scoring pipeline, the post-scoring gate layer A–L, the diagnose/replay, helpers).
The target architecture wants each as a **single-responsibility** unit so a layer can be audited in
isolation. This design step **maps the current file onto the architecture's layers and plans the split**;
the byte-identical split build is the follow-on. It also **locates the gate layer (A–L)** precisely so the
*separate* refactor #2 (gate dissolution — a behavior change) has its target, but does **not** dissolve
anything here.

## §2 — Scope

**Read-only**, `src/composing/` (read). No edits, no build needed (source reading; cite `file:line`). The
producer and all behavior stay untouched; HEAD unchanged.

## §3 — The design tasks

1. **Map the current file at source.** Enumerate `chordanalyzer.cpp`'s major sections with line ranges and
   their single responsibility: the template vocabulary + the `kTemplateCount`/score-matrix size model
   (`chordanalyzer.h`); the vertical oracle (per-cell scoring snapshot, the inversion-eligibility
   predicates); the competition/function pipeline (`basisIndep`/`basisDep`, `diatonicRootContribution`,
   `applyHarmonicFunction`, the three score matrices); the **post-scoring gate layer A–L**
   (`applyPostScoringGates` + each gate); the diagnose/replay (`diagnoseChord`); file-local helpers. Note
   the total size and which responsibilities are conflated.
2. **Map onto the architecture's layers.** Assign each section to a target layer (vertical oracle /
   competition+function scoring / post-scoring gates / diagnose / shared helpers). Flag any section whose
   responsibility is **split across** the current code or **tangled** with another layer (a genuine seam
   problem — surface it; it may be a refactor-#2 or deeper-untangle item, not a clean move).
3. **Define the target file decomposition.** A set of single-responsibility TUs (name each, define its
   boundary + the public interface it exposes to its consumers). Each new file = one layer's responsibility.
   Keep the gate layer as its **own** unit (the refactor-#2 dissolution target).
4. **Plan the split as a byte-identical SEQUENCE.** Order the moves to minimize risk (leaf helpers + the
   template/oracle first; the gate layer isolated last). Each step: move one responsibility to its new TU,
   **no logic change**, independently verifiable byte-identical (BIR 57/23/57, suites green, snapshots
   unchanged, `.ours.json` 0-diff). State how many steps and what each moves.
5. **Account for the constraints (cite/plan each):**
   - **`kTemplateCount` size model** — the compiler-enforced array extents (the three score matrices,
     `kMasks`) must stay derived from `kTemplateCount` ACROSS the split (no silent stack-buffer regression).
   - **Unity/jumbo build ODR risk** — anonymous-namespace names shared across the concatenated
     `composing/analysis` TUs must not clash (the `jkd*`/`lmd*`-prefix precedent); plan the prefixing/naming.
   - **`docs/scoring_model.md` sync** — the split changes no scoring logic, so the doc's *content* is
     unchanged, but its §/file references update; note the sync (CLAUDE.md sync rule).
   - **Byte-identity** is the acceptance gate for every move (this is a refactor, not a behavior change).

## §4 — Output: the split plan (dossier, no code)

Write `cc_refactor1_split_design_dossier.md` (gitignored, HELD): the current-file map (§3.1, line-ranged),
the target layer decomposition (§3.3, files + interfaces), the byte-identical split sequence (§3.4), the
constraint-handling plan (§3.5), and the precisely-located gate layer (for refactor #2). Frame it as the
**spec for the byte-identical split build** — concrete enough that the build instruction follows directly.
Note any tangles found (§3.2) as findings for refactor #2 / the layer audit.

## §5 — Stop conditions
- Any code change / file move in this step (read-only) → STOP.
- A responsibility that cannot be cleanly assigned to one layer (a genuine tangle) → **surface it as a
  finding** (do not force a split that would change behavior; it may belong to refactor #2).
- The split could not be made byte-identical for some section (e.g. a real ODR / size-model obstruction) →
  surface it in the plan with the obstruction, do not hand-wave it.
- Uncertain about a section's responsibility or a constraint → read the source, cite `file:line`, surface —
  never guess.

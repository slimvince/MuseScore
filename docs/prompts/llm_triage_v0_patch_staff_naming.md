# LLM-Triage v0 Patch — Staff Disambiguation

**Scope:** Fix one specific issue in `tools/llm_triage/llm_triage.cpp`.
The current emitter labels every staff by `Part::partName()`, which
collides for piano (one Part, two Staves both named "Piano") and any
multi-staff part. Output looks like:

```
m9 b1 (h):  staff "Piano": D4 F#4 ; staff "Piano": D3
```

Both staves emit as `staff "Piano"`, leaving an LLM to guess treble
vs bass from pitch range. Fix: when two or more staves share a part
name, append ` #N` (1-based, in score order within that part) to
disambiguate. When a part name appears only once, render unchanged.

After the patch, the same line should read:

```
m9 b1 (h):  staff "Piano #1": D4 F#4 ; staff "Piano #2": D3
```

(`#1` for the upper staff, `#2` for the lower, by staff index in
score order.)

---

## Branch and worktree context

You are working in the `llm-triage` worktree at `C:\s\MS-llm-triage`.
The `llm-triage` branch's last commit is the v0 format-emitter that
introduced this issue. The `master` branch is owned by a different
session; **do not touch any file outside `tools/llm_triage/`**.

`CLAUDE.md` will auto-load with stale `src/composing/`
pre-authorizations — ignore those for this session. The full pact is
in `docs/prompts/llm_triage_v0_format_emitter.md` (committed on this
branch) and applies here.

---

## Pre-flight

1. Confirm branch and clean tree:
   ```bash
   cd /c/s/MS-llm-triage
   git rev-parse --show-toplevel  # must be /c/s/MS-llm-triage
   git status -sb                 # must show: ## llm-triage  (no diff)
   git log --oneline -1           # the v0 format-emitter commit
   ```
   If anything is dirty or you're not in the worktree, **halt and
   surface**.

2. Skim the v0 emitter source to find the one or two places where
   the staff label string is built. `grep -n 'staff "' tools/llm_triage/llm_triage.cpp`
   (or your preferred search) will locate the format string.

---

## The fix

Algorithm:

1. Before emitting any region, walk the score's staves once and
   build a count: for each `partName()` string, how many staves carry
   that name? Cache a per-staff-index `displayName` derived from
   that count:
   - If `count[partName] == 1` → `displayName = partName`
   - If `count[partName] >  1` → `displayName = partName + " #" + indexWithinPart`
     where `indexWithinPart` is the 1-based ordinal of this staff
     among all staves sharing this `partName`, in score order.

   This means a score with one piano (2 staves) and one organ (3
   staves) produces:
   - Piano upper → `Piano #1`
   - Piano lower → `Piano #2`
   - Organ upper → `Organ #1`
   - Organ middle → `Organ #2`
   - Organ pedal → `Organ #3`

   And a score with one guitar (1 staff) keeps it as `Guitar` (no
   suffix).

2. Replace the inline `partName()` call in the emitter with a lookup
   into this cached `displayName` map keyed by staff index.

3. Apply the same change in **all three emitters** — `notes_only`,
   `with_symbols`, and `analyzer_output` — wherever the staff label
   appears. (The chord-tone listings in `analyzer_output.txt` use
   `(D2 F#2 ...)` form without staff labels, so likely unaffected;
   confirm by reading the code rather than assuming.)

4. Document the choice in a comment near the cache: "Disambiguates
   staves that share `partName()` (e.g. piano with two staves) so
   LLM input can distinguish upper from lower without pitch-range
   inference."

Skip the eligibility-filtered staves (those excluded from analysis
via `staffIsEligible`) when building the count — they don't appear
in output, so they shouldn't influence the numbering. If you include
them in the count, an eligible second piano staff might get labelled
`#3` because an excluded-but-counted percussion staff took `#2`.
That'd be confusing.

---

## Verification

1. Rebuild:
   ```bash
   /c/Qt/Tools/Ninja/ninja.exe -C /c/s/MS-llm-triage/ninja_build_llm_triage llm_triage
   ```

2. Re-run on the default score:
   ```bash
   cd /c/s/MS-llm-triage
   ./ninja_build_llm_triage/llm_triage.exe \
     "tools/extra scores/hiromi/pachelbel-canon-in-d-arr-hiromi-uehara.mscz" \
     ./outputs
   ```

3. Diff against the previous run (the previous output is committed
   nowhere — it was in `outputs/` which is gitignored — so do the
   diff inline by reading the new output):
   ```bash
   head -25 outputs/pachelbel-canon-in-d-arr-hiromi-uehara.notes_only.txt
   ```
   Expected: lines that previously read `staff "Piano": ... ; staff
   "Piano": ...` now read `staff "Piano #1": ... ; staff "Piano #2":
   ...`. The exact pitches and durations must be unchanged from the
   v0 run.

4. Confirm no other lines changed beyond the staff-label
   substitution. If you see any other diff (different pitches,
   different durations, different region count), **halt and
   surface** — the patch should be label-only.

---

## Halt-and-surface protocol

Halt and surface to Vincent immediately if:

- Pre-flight finds the working tree dirty or you're not in the
  worktree.
- The patch would require editing any file outside
  `tools/llm_triage/`.
- The build fails for any reason. Include the full build error.
- The post-patch run produces a different region count, different
  pitches, or any change beyond the staff-label substitution.
- You discover that staff-label rendering happens in more than two
  or three places and the change becomes scattered. Surface for a
  refactor decision rather than spreading the fix across many
  call sites.

---

## Commit and push

```bash
cd /c/s/MS-llm-triage
git add tools/llm_triage/llm_triage.cpp
git status   # confirm: only llm_triage.cpp changed
git commit -m "LLM-Triage v0 patch: disambiguate staves sharing partName

Multi-staff parts (e.g. piano: one Part, two Staves both named
'Piano') previously emitted both staves as 'staff \"Piano\":' in
all three artifacts, leaving LLM input ambiguous. Append ' #N'
(1-based index within the shared part name, score order) when
the count is greater than 1; leave singletons unchanged.

Notes_only and with_symbols sample line, before:
  staff \"Piano\": D4 F#4 ; staff \"Piano\": D3
After:
  staff \"Piano #1\": D4 F#4 ; staff \"Piano #2\": D3"
git push origin llm-triage
```

---

## Report-back format

```
## LLM-Triage v0 staff-naming patch — session report

Branch: llm-triage @ <commit_sha>
Pushed to: origin/llm-triage  (yes/no)

### Diff summary
- Files changed: 1 (tools/llm_triage/llm_triage.cpp, +<X>/-<Y>)
- Build: pass/fail
- Re-run on Pachelbel: 77 regions (must match prior; flag if not)

### Before / after sample lines
Before (m9 b1):
  <paste actual line>
After (m9 b1):
  <paste actual line>

### Pact compliance
Files touched outside tools/llm_triage/: <list — should be empty>

### Surprises / open questions
- <list, brief>
```

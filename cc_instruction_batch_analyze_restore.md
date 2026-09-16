# CC Instruction — restore `batch_analyze` (F16, the unblock for the gated finish)

> **Why.** `batch_analyze` cannot load any score this session (missing Qt `platforms/` plugins beside the binary; Qt
> PATH/plugin-path didn't fix it). It is the **corpus two-tier BIR gate** — the safety net for ALL the behaviour-
> changing L1–L4 finishing work (the L4 build, legacy retirement, defect fixes). Until it runs, none of that can
> proceed. F17 already confirmed `batch_analyze`'s corpus path **reuses the production analyzer** (not a duplicate), so
> restoring it is purely an **environment/deployment** fix — **NOT a production `src/composing/` change.**
> *(Reminder: the never-bash rule is Cowork's; it does not constrain your build/test/tool runs.)*

## §1 — Diagnose (capture the exact failure)
Run `batch_analyze` on one score and **capture the exact error** (redirect to a file, then read). It is most likely the
Qt platform-plugin load ("could not load the Qt platform plugin 'windows'…") because the tool spins up a
`QGuiApplication`-class init that needs `platforms/qwindows.dll`. Report:
- the verbatim error,
- **why** the production app / `notation_tests` find the Qt plugins but `batch_analyze.exe` doesn't (where each looks —
  working dir, `platforms/` beside the exe, `QT_PLUGIN_PATH`/`QT_QPA_PLATFORM_PLUGIN_PATH`),
- whether `batch_analyze` actually needs a *windowing* platform at all (it's a headless CLI score-analyzer).

## §2 — Restore, least-invasive first
Try in this order; stop at the first that works and report which:
1. **Headless platform (preferred — no deploy):** set `QT_QPA_PLATFORM=offscreen` (or `minimal`) for the
   `batch_analyze` run, so it never needs `qwindows`. If it then loads scores, bake it into the **runner**
   (`run_bach_preset.py` / `tools/coverage` runner) or the tool's own startup — a tools-only change.
2. **Deploy the plugins:** copy the Qt `platforms/` plugins beside `batch_analyze.exe` (or `windeployqt`, or set
   `QT_QPA_PLATFORM_PLUGIN_PATH` to the Qt install's `plugins/platforms`).
3. **Tool startup (tools-only):** if the tool must select the platform itself, set it in `tools/batch_analyze.cpp`
   startup (e.g. force `offscreen` when headless) — `tools/` only.
- **STOP if a fix would require editing `src/composing/` production code** — it should not; this is Qt deployment.

## §3 — Verify the gate is genuinely back (the real test)
- `batch_analyze` loads a score and writes a valid `.ours.json`.
- **Re-run the corpus characterisation** (`run_bach_preset.py` + `characterise_bir_false.py`) for **Baroque + Jazz +
  Default** and confirm the **BIR identity sets reproduce 53 / 24 / 53** (the CLAUDE.md ratified sets) on the CURRENT
  config — i.e. the restore changed *nothing* about the analysis, only made the tool runnable. **Any deviation from
  53/24/53 → STOP and report** (the restore must be analysis-neutral; a shifted set means something other than the Qt
  env changed).
- Report the manifest sha256s.

## §4 — Scope & stops
- **Environment / runner / `tools/` only.** NO `src/composing/` production change. If one seems needed → STOP, report.
- **The corpus must reproduce 53/24/53** — the restore is analysis-neutral. A shift → STOP.
- *(Do NOT touch the F17 dense-start config gap here — aligning `excludeLookAheadOnDenseStart` to the live value is a
  separate, deliberate gate-re-baseline decision, AFTER the gate is confirmed reproducing.)*
- `upstream` never; local commit of any runner/tool change only.

## §5 — Deliver
Commit **locally (unpushed)** any runner/tool/env change. Write `cc_batch_analyze_restore_report.md` (gitignored): the
§1 diagnosis, the §2 fix that worked (which of the three), the §3 verified corpus regen (53/24/53 + manifest sha256s),
and the commit sha — so Cowork verifies by sha that only `tools/`/runner changed, no `src/composing/`.

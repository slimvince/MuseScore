# CC Report — F16: restore `batch_analyze` (corpus two-tier BIR gate)

**Date:** 2026-06-27   **HEAD at restore:** `c9633aebc4`   **Fix commit (local, unpushed):** `5357f5a7ed`
**Scope:** `tools/` only — `tools/run_bach_preset.py` (the corpus runner). **No `src/composing/` change.**

---

## TL;DR

`batch_analyze.exe` itself was never broken this session — the **runner** was. The reported "cannot load
any score" was **not** a Qt platform-plugin failure (the instruction's hypothesis). The real cause is a
**path-form / MSYS argument-conversion** issue in `run_bach_preset.py`: it passed unix-form path arguments
(`/c/s/MS/...`) to the native `batch_analyze.exe` and relied on MSYS2's automatic POSIX→Windows argument
conversion, which is **disabled by `MSYS_NO_PATHCONV=1`** (the default in the Claude Code / VS Code Git Bash
integration). With conversion off, the unix path reached the exe verbatim → `failed to load score`.

Fix (tools-only): pass **drive-letter forward-slash** paths (`C:/s/MS/...`) — valid Windows paths the exe
opens directly regardless of conversion state — and additionally select `QT_QPA_PLATFORM=offscreen` for the
subprocess as the instruction-requested headless hardening. The restore is **analysis-neutral**: the corpus
reproduces the ratified **53 / 24 / 53** BIR=false identity sets **exactly**, and a fresh Baroque regen is
**byte-identical** (0/353 differing sha256) to the prior corpus.

---

## §1 — Diagnosis (the exact failure)

### The verbatim error
Reproduced by invoking the exe the way the runner does (unix-form path argument), in this session's shell:
```
$ ./ninja_build_rel/batch_analyze.exe "/c/s/MS/tools/corpus/bwv101.7.xml" "C:/tmp/x.json" --preset Baroque
ERROR: failed to load score: /c/s/MS/tools/corpus/bwv101.7.xml      (exit 1)
```
Run through the runner, **all 353 scores** failed identically (`0/353 OK`, corpus marked INCOMPLETE).

### The Qt hypothesis was a red herring — and here is the proof
The error is **not** a Qt platform-plugin message ("could not load the Qt platform plugin 'windows'").
`batch_analyze` constructs its `QGuiApplication` **successfully** — it gets far enough to enter score
loading and emit `failed to load score`. So:

- **batch_analyze DOES find its Qt plugins.** There are **no** Qt6 DLLs and **no** `platforms/` dir beside
  `ninja_build_rel/batch_analyze.exe`. The Qt install bin `C:\Qt\6.10.1\msvc2022_64\bin` is on `PATH`, so the
  exe loads `Qt6Core/Gui.dll` from the install, and Qt finds `…/plugins/platforms/qwindows.dll` via the
  prefix baked into those install DLLs. No env var, no beside-the-binary deployment needed. The instruction's
  question "why does the production app find plugins but batch_analyze doesn't" is **moot** — batch_analyze
  finds them too.
- **The real determinant is the path-form of the score ARGUMENT, decided by MSYS conversion:**

  | input arg form | result |
  |---|---|
  | `C:/s/MS/tools/corpus/bwv101.7.xml` (Windows fwd-slash) | **loads, exit 0, 57860-byte JSON** |
  | `/c/s/MS/tools/corpus/bwv101.7.xml` (unix) | **`failed to load score`, exit 1** |

  Session shell state: **`MSYS_NO_PATHCONV=1`**, `MSYS2_ARG_CONV_EXCL=` (empty), `MSYS=winsymlinks:nativestrict`.
  `MSYS_NO_PATHCONV=1` turns OFF MSYS2's automatic POSIX→Windows conversion of arguments handed to native
  programs. The runner builds its command with `_to_unix_path()` (→ `/c/s/MS/...`) and depends on that
  conversion to rewrite the arg to `C:\s\MS\...` for the native exe. In a shell where conversion is on (a
  normal desktop Git Bash / PowerShell-launched run — how the *prior* corpus was generated), it works; in this
  session's shell it does not, so every score fails. (`MSYS_NO_PATHCONV` affects only *argument* conversion,
  not how bash itself resolves the `/c/...` **program** path to exec — that is why the exe still launches.)

- **Does batch_analyze need a windowing platform at all?** No. It is a headless CLI score-analyzer; it reads
  the score model and writes JSON. `QT_QPA_PLATFORM=offscreen` produces **byte-identical** output (verified),
  confirming no display/window is required.

---

## §2 — Restore (least-invasive; the fix that worked)

The instruction's ordered menu (§2.1 offscreen → §2.2 deploy plugins → §2.3 tool startup) was framed around a
Qt-plugin failure. Since the actual failure is the runner's **path form**, the fix lives in the runner. Two
changes, both in `tools/run_bach_preset.py`, both `tools/`-only:

1. **Path-form fix (the actual restore).** New `_to_win_path()` returns the resolved Windows path with forward
   slashes (`C:/s/MS/…`); `_run_batch_analyze` now passes it for the **input and output arguments** to the exe
   (the exe *program* path is left in unix form — bash execs it fine). A `C:/…` path is a valid Windows path
   the exe opens directly, is left untouched by MSYS whether or not conversion is on, and needs no backslash
   escaping inside the `bash -c` string. → loads regardless of `MSYS_NO_PATHCONV`.

2. **Headless Qt hardening (instruction §2.1, preferred).** New `_qt_subprocess_env()` sets
   `QT_QPA_PLATFORM=offscreen` (via `setdefault`, so an explicit caller override is respected) on the
   batch_analyze subprocess, so the gate never depends on a windowing platform plugin being loadable — the
   failure mode the instruction anticipated, which would bite in a true headless/CI/cron context even though
   it was not this session's bug. Proven byte-identical, so it is a strict no-op-or-improvement.

**No deploy (§2.2) and no `batch_analyze.cpp`/startup (§2.3) change was needed.** **No `src/composing/`
change.** STOP-condition (§4: "stop if a fix would require editing `src/composing/`") was never triggered.

---

## §3 — Verification (the gate is genuinely back)

Fresh full-corpus regen with the **fixed runner** at HEAD `c9633aebc4`, all three configs, each 353/353 OK
(`complete=True`, exit 0), then `characterise_bir_false.py`:

| preset | regen | BIR=false count | identity set vs CLAUDE.md ratified |
|---|---|---|---|
| Baroque | 353/353 OK | **53** | **EXACT match (53)** |
| Jazz | 353/353 OK | **24** | **EXACT match (24)** |
| Default | 353/353 OK | **53** | **EXACT match (53)** |

Identity sets compared at `stem@tick` granularity against the CLAUDE.md sets (Default taken as Baroque-53 with
`{bwv352@1440, bwv60.5@30960}` → `{bwv227.7@18000, bwv387@10560}`, per the CLAUDE.md note — confirmed exactly).
**Zero deviation from 53/24/53** → the §3 STOP-on-deviation condition did not fire.

**Analysis-neutrality proof (byte-level).** Before overwriting the canonical dirs, Baroque was regenerated
into a temp dir with the fixed runner and its per-score sha256 compared against the prior canonical Baroque
manifest (generated at `d7dae4573f`, *without* the offscreen/winpath changes, in a conversion-on environment):

```
OK-both differing sha256: 0      RESULT: BYTE-IDENTICAL (all 353 OK stems match)
```

So the winpath + offscreen changes are jointly **byte-identical** to the historical invocation — the restore
changed only the tool's runnability, nothing about the analysis. (It also shows the binary's output has not
drifted between `d7dae4573f` and `c9633aebc4`, both doc-only commits.)

### Manifest sha256s (this regen, HEAD `c9633aebc4`)
```
baroque  : 75cfbf01f5cf0a3270d36fc56762f5e61cfec19c0ed1acfcddf8bad8405a77f0
jazz     : 5437f79ccde7cf6e5da0f92d7e24b39453783e586e071660729d1008f75b14c4
default  : 08623d20322774569ba33789e4fbf71ae55416b72a57f498ffb8f8ea13695d40
```
(sha256 of each `tools/corpus/<preset>/corpus_manifest.json`. These embed a fresh timestamp + exe mtime, so
they fingerprint *this* regen; the per-score `.ours.json` content inside is byte-identical to the prior corpus
as shown above.)

---

## §4 — Scope & stops

- **`tools/` / runner only.** Commit `5357f5a7ed` = `tools/run_bach_preset.py`, 1 file, +46/−4. No
  `src/composing/`, no `notationaccessibility.cpp`, no `batch_analyze.cpp`. Verified:
  `git show --name-only 5357f5a7ed` → grep for `src/composing|notationaccessibility` = none.
- **Corpus reproduces 53/24/53 exactly** (identity sets, not just integers) → analysis-neutral.
- **Did NOT touch the F17 dense-start config gap** (`excludeLookAheadOnDenseStart`) — left for the separate
  deliberate gate-re-baseline decision, per §4.
- **`upstream` never.** Local commit only; not pushed (master ahead of origin by 32, all prior local commits).

---

## §5 — Deliverables

- **Fix commit (local, unpushed):** `5357f5a7ed` — `fix(tools): batch_analyze runner — Windows-form path args
  + headless Qt platform (F16 restore)`. Cowork can verify by sha that only `tools/run_bach_preset.py` changed.
- **This report:** `cc_batch_analyze_restore_report.md` (gitignored).
- **Corpus state:** `tools/corpus/{baroque,jazz,default}` regenerated at `c9633aebc4`, manifests
  `complete=True`, BIR=false 53/24/53 (sha256s above). `tools/corpus/` is gitignored (no tracked churn).

### One correction for the record
The F16 instruction's central hypothesis (missing Qt `platforms/` plugins / a Qt platform-plugin load
failure) did **not** reproduce: batch_analyze's Qt init succeeds and it finds its plugins via the Qt-install
bin on `PATH`. The genuine blocker was the runner's unix-form path arguments under `MSYS_NO_PATHCONV=1`. The
offscreen hardening was still applied (instruction §2.1, byte-identical) as forward protection against the
anticipated headless Qt failure mode in CI/cron contexts.

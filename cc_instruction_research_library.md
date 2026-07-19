# CC instruction — research-paper library: link-rot mitigation into a PRIVATE repo

**Dispatch author:** Cowork, 2026-07-19, at the user's direction. **Type:** file/repo chore — no code,
no build, no test, no inference, no register change beyond what is stated. **Policy set by the user:
NOTHING is redistributed.** The public fork (`origin` = `slimvince/MuseScore`) carries only the text
register; every PDF and dataset copy lives in a separate PRIVATE GitHub repo.

**Read first:** `docs/research_papers/BIBLIOGRAPHY.md` (the register — the "wanted" rows with URLs are
the download list), `docs/research_papers/README.md` (the index of the 7 already-local PDFs).

## 1. The privacy rule (why a second repo)

GitHub has no per-directory visibility, and a fork of a public repo cannot be made private — so any
PDF committed to the fork is published. Therefore: **no PDF, and no `tools/BCMH_dataset/` content, is
ever committed to the fork.** The private repo is the only git home for binaries.

## 2. Task 1 — guard the fork FIRST

Before anything else, add `.gitignore` entries in the fork:
```
docs/research_papers/*.pdf
tools/BCMH_dataset/
```
Verify with `git status` that the 7 existing PDFs and `tools/BCMH_dataset/` are untracked and stay so.
**If any of these files is already tracked or was ever committed to the fork: STOP and report** (a
history rewrite is a user decision, not yours).

## 3. Task 2 — the private repo

- Ask the user for (or confirm) the private repo: suggested `slimvince/MS-research-papers` (their
  naming choice governs). If `gh` is not authenticated or the repo cannot be created/pushed, **STOP
  and ask the user to create it** — do not improvise hosting.
- Layout in the private repo: `papers/` (all PDFs), `datasets/BCMH_dataset/` (a copy — the working
  copy stays at `C:\s\MS\tools\BCMH_dataset\` for the future OI-179 instrument, gitignored in the
  fork), and a copy of `BIBLIOGRAPHY.md` + `README.md` for self-containedness (the fork's copies
  remain the canonical ones, per #6 one-home: state in the private repo's README that it mirrors the
  fork's register).
- Move the 7 existing PDFs' git home there; the on-disk copies under `docs/research_papers/` may stay
  for local reading (they are gitignored).

## 4. Task 3 — batch-download the "wanted" rows

- For each BIBLIOGRAPHY row marked **wanted**, download the URL into `papers/` with the row's
  descriptive-style filename (author_year_venue_topic.pdf).
- Verify each file: non-trivial size and a `%PDF` header (an HTML error page saved as .pdf is a
  silent failure — check, don't assume). For arXiv abs-links, fetch the /pdf/ form.
- **On failure** (paywall, anti-bot, dead link): record `FAILED (reason)` in the row's Local column.
  Do NOT circumvent paywalls or bot walls, do NOT use archive/mirror workarounds — a failed row is
  simply reported to the user.
- Flip each succeeded row's Local column to ✓ (private repo). Keep the Redistribution column
  untouched — the user's standing policy is "redistribute nothing" regardless of tier.

## 5. Deliverable

- **Fork commit** (one, `docs(cc)`): the `.gitignore` guard + the BIBLIOGRAPHY Local-column updates +
  a one-line note in `docs/research_papers/README.md` naming the private repo as the binary home.
  Force-add this instruction file. Push to `origin` only (`upstream` stays disabled).
- **Private-repo commit(s):** the papers, the BCMH dataset copy, its README. Private visibility
  verified (`gh repo view --json visibility` or the web UI) BEFORE pushing any PDF — if visibility
  cannot be confirmed private, STOP.
- **Report:** counts (downloaded / failed with reasons), the verification method, and confirmation
  that `git status` on the fork shows no binary tracked. Self-check the diff (standing rule).

# Draft comment for musescore/MuseScore#9444

*Cowork draft, 2026-06-14. For Vincent to post (after the pre-post checklist at the bottom).
Framing per the user mandate: advocacy to get the key-signature **mode** property properly
supported, NOT to hide it — because a maintained mode property is a reliable signal that
downstream features and tools can depend on. Complementary to #9444 (a specific import-side
facet), not a duplicate. All file/line refs verified in our current tree; re-confirm against
upstream `master` before posting.*

---

## Comment body (paste this)

I'd like to add a concrete **import-side** facet to this issue, and make the case for *fixing* the key-signature mode rather than hiding it.

### An import-side mechanism that silently drops `<mode>`

In `addKey()` (`src/importexport/musicxml/internal/import/importmusicxmlpass2.cpp`), the guard that decides whether to create a `KeySig` compares **fifths only**:

```cpp
// TODO only if different custom key ?
if (oldkey != key.key() || key.custom() || key.isAtonal()) {
```

`<mode>` is parsed correctly just above (`key.setMode(...)`), but when a key's fifths match the prevailing key, the whole `KeySig` is deduped away — taking the parsed mode with it (→ `KeyMode::UNKNOWN` downstream). The common trigger is a **0-fifths key carrying an explicit mode**: at score start the prevailing key defaults to `{C, UNKNOWN}`, so `<fifths>0</fifths><mode>minor</mode>` (A minor, or any 0-signature modal key) matches on fifths and is dropped. (The maintainers' own `// TODO only if different custom key ?` on the line above already flags this dedup as incomplete.)

### It breaks export/import round-trip

Export **does** write `<mode>` (`exportmusicxml.cpp`, for every `KeyMode` value). So:

1. A score with an A-minor key signature exports as `<fifths>0</fifths><mode>minor</mode>`.
2. Re-importing that file **drops** the mode (the Inspector then shows "Unknown").
3. Re-exporting can no longer recover it.

Information present in the file is lost on a plain round-trip.

### A minimal fix — and it's the same correctness class MuseScore already applies

The dedup **already** preserves one mode value: the `|| key.isAtonal()` term, and `isAtonal()` is defined as `m_mode == KeyMode::NONE` (`key.h`). So *atonal* mode already survives the dedup — only the tonal/modal values are dropped. Extending the guard to also compare mode closes the gap:

```cpp
if (oldkey != key.key() || oldKeySig.mode() != key.mode() || key.custom() || key.isAtonal()) {
```

A key matching the prevailing one in **both** fifths and mode still produces no `KeySig`, so plain mode-less C-major scores are unaffected. In our build this restores `<mode>` on round-trip and adds no spurious key signatures.

### Why fix rather than hide: mode is already load-bearing

The key-signature mode isn't XML-only or cosmetic:

- It's persisted in the native `.mscz` format (read/write) and round-trips through MusicXML.
- It's exposed in the Inspector (`Pid::KEYSIG_MODE`) and the plugin API.
- `isAtonal()` (== mode `NONE`) already gates real behavior — e.g. transposition skips atonal keys (`transpose.cpp`, `edit.cpp`).
- The tonal modes are the only thing that distinguishes **relative pairs that share a signature** (C major vs A minor — both 0 fifths). Anything that names a key or reasons about tonality (harmonic analysis, plugins, import/export fidelity) needs that distinction.

Hiding the UI removes the only way to *set* a property that the data model, the native format, the MusicXML round-trip, and the plugin API all already carry. Making mode functional — a working editor plus this import fix — looks like the better direction: it's small and well-scoped, and it lets mode become a dependable signal rather than a silently-dropped one.

I'm happy to open a PR for the import-side fix if that's welcome.

---

## Pre-post checklist (NOT part of the comment)

- [ ] **Re-verify against current upstream `master`.** Our fork's importer may lag; confirm the fifths-only dedup in `addKey()` is still present upstream (it was upstream-unchanged code as of our base — the `// TODO only if different custom key ?` line). Update the file/line references to match upstream.
- [ ] **Optionally rebuild upstream `master`** to reproduce the round-trip drop there directly (we confirmed it on our fork; the dedup is upstream-unchanged by inspection, so it applies by reading, but a fresh upstream repro is stronger if you want it).
- [ ] **Optionally attach a minimal repro file** — a 2-bar score in A minor, exported to `.musicxml`, plus the re-imported/re-exported version showing `<mode>` gone.
- [ ] **Decide on the PR offer** — leave the last line in only if you're willing to open the PR.

## Source references (verified in our tree this session)

- `importmusicxmlpass2.cpp` `addKey()` — fifths-only dedup at the `if` guard; `<mode>` parsed via `key.setMode(...)` just above.
- `exportmusicxml.cpp:2473–2497` — writes `<mode>` for all `KeyMode` values. *(verified)*
- `key.h:81` — `isAtonal() const { return m_mode == KeyMode::NONE; }`. *(verified)*
- `transpose.cpp` / `edit.cpp` — `isAtonal()` gates transposition; `keysig.cpp` — `Pid::KEYSIG_MODE` Inspector property. *(carried from prior-session source verification; re-confirm line numbers before citing exact lines publicly)*

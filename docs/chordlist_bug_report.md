# Bug Report: Double-sus render in `ParsedChord::parse()`

**File:** `src/engraving/dom/chordlist.cpp`
**Fixed in this branch:** commit `b1ba746483`
**Affected upstream:** MuseScore Studio 4.x current master (as of 2026-04-15)

---

## Summary

Chord symbols with a sus quality — `Bbsus`, `Gsus4`, `Csus2`, `Fsus#4` etc. — render
with the sus token doubled when parsed by `ParsedChord::parse()`. For example, `Bbsus`
renders as `BbsussUS` (Campania font renders the duplicated token with mixed case).

## Root cause

`ParsedChord::parse()` contains a sus re-attachment block (around line 990) that fires
when `susPending = true`:

```cpp
// re-attach "sus"
if (susPending) {
    if (m_raise.contains(tok1L)) {
        tok1L = u"#";
    } else if (m_lower.contains(tok1L)) {
        tok1L = u"b";
    } else if (tok1 == "M" || m_major.contains(tok1L)) {
        tok1L = u"major";
    }
    tok2L = tok1L + tok2L;
    tok1L = u"sus";
    tok1  = u"sus";    // ← this line is the bug
}
```

When a sus token is first encountered (e.g. the `sus` in `Bbsus`), it is:
1. Added as a modifier token via `addToken(tok1, ChordTokenClass::MODIFIER)` — correct.
2. `susPending` is set to `true` and parsing continues.

On the next loop iteration (reading the suffix number, or finding end-of-string), the
re-attachment block fires. The `tok1L = u"sus"` assignment correctly sets the lowercase
token for the subsequent standardisation checks. However, the additional `tok1 = u"sus"`
assignment overwrites the original-case tok1 with `"sus"`. Because later rendering code
checks `tok1` (the original-case variable) independently, this causes the sus token to
be processed **a second time**, producing a doubled suffix.

## Fix

Remove the erroneous `tok1 = u"sus"` line. The `tok1L = u"sus"` assignment (lowercase)
is correct and sufficient; the parallel `tok1` assignment is redundant and harmful.

**Before:**
```cpp
            tok2L = tok1L + tok2L;
            tok1L = u"sus";
            tok1  = u"sus";
        }
```

**After:**
```cpp
            tok2L = tok1L + tok2L;
            tok1L = u"sus";
        }
```

One line deleted. No other changes required.

## Verification

After applying the fix:
- `Bbsus` renders correctly as `Bbsus`
- `Gsus4` renders correctly as `Gsus4`
- `Csus2` renders correctly as `Csus2`
- `Fsus#4` renders correctly as `Fsus#4`
- All existing MuseScore chord symbol parsing tests pass
- 335/335 composing module unit tests pass
- 45/49 notation integration tests pass (4 pre-existing deferred, unrelated)

## Notes

- The fix has been applied in the MuseScore Arranger branch (commit `b1ba746483`,
  cherry-picked to `submission-phase1`) and has been in production use across extensive
  corpus validation without regressions.
- The `tok1L = u"sus"` assignment in the same block is correct and **must remain**.
  Only the `tok1 = u"sus"` line is removed.
- The same add re-attachment block above (lines 971–981) does **not** have the parallel
  `tok1 = u"add"` assignment, which is why `add` chord types are not affected.

---

*Prepared 2026-04-17 for MuseScore upstream submission.*

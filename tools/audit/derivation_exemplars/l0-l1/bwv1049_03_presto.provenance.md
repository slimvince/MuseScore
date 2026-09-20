# `bwv1049_03_presto.mscx` — where this file came from, and what was established about it

> **What this file is.** The `.mscx` score that the archive
> `"tools/extra scores/large/bach-brandenburg-concerto-no-4-bwv-1049-mvt-iii-presto.mscz"` holds,
> extracted from that container without alteration and written here under a name that says which
> music it is. **Nothing was edited, stripped, re-encoded or re-saved.**
>
> Every fact below was established at the object on 2026-09-01 by the batch that wrote the file.

---

## 1. The source archive

| | |
|---|---|
| Path | `tools/extra scores/large/bach-brandenburg-concerto-no-4-bwv-1049-mvt-iii-presto.mscz` |
| Byte size | 75,260 |
| `sha256` | `56e2241707caea88e24ec9ab9ae0e5ff9f26dffabfd7638badda8df6acf89cfb` |

The path contains a space and is quoted in every command that names it
(`docs/score_inventory.md`, Hard rule 3).

## 2. The member inside it

The archive holds three members. The one score member is:

| | |
|---|---|
| Member name | `temp_10111.mscx` |
| Uncompressed length the archive records | 1,701,770 bytes |
| Stored CRC-32 | `6c222647` |

The other two members are `META-INF/container.xml` (158 bytes) and
`Thumbnails/thumbnail.png` (19,995 bytes). Neither was extracted here.

## 3. How the file arrived, and the proof that no byte was altered

The file arrived by **container extraction** — the ZIP member was inflated and copied. **No byte
was altered.** The proof is stated as what it is, and it is two independent facts:

- **The extracted length equals the length the archive records for that member**: 1,701,770 bytes
  extracted against 1,701,770 bytes recorded.
- **The member's stored CRC-32 verifies against its decompressed bytes.** `unzip -t` reported
  *"No errors detected in compressed data"* over all three members of the archive, which is that
  check for each of them.

| | `sha256` |
|---|---|
| The file as extracted, in a scratch directory outside the repository | `a4d9d89798469f654e120e08884c4c6e3c47c2842e2b2fccc53ec9db87fbac80` |
| The file as it now stands on disk at this path | `a4d9d89798469f654e120e08884c4c6e3c47c2842e2b2fccc53ec9db87fbac80` |

The two digests are equal, so nothing normalized the file on its way into the repository. Its size
on disk is 1,701,770 bytes; it carries 64,500 line feeds and **no carriage returns at all**.

## 4. What build declares itself the writer of this file

Read at the head of the file:

```
<museScore version="3.01">
  <programVersion>3.0.0</programVersion>
  <programRevision>c1a5e4c</programRevision>
```

**`programVersion` 3.0.0 predates this repository's own `5.0.0`** — `version.cmake` sets
`MUSE_APP_VERSION_MAJOR "5"`, `MUSE_APP_VERSION_MINOR "0"` and `MUSE_APP_VERSION_PATCH "0"` — **by
two major versions, so this file cannot be this build's output.** The declared revision is
`c1a5e4c`, which has the shape of a revision hash rather than of a placeholder.

## 5. The license, quoted from the file's own metadata

```
<metaTag name="copyright">OpenScore (CC0)</metaTag>
```

That is the file's own copyright metaTag, quoted in full. It says CC0, which is the condition on
which this file may stand inside the repository at all.

## 6. Annotation elements — the file carries none of the three kinds

| Element | Count over the whole file |
|---|---:|
| `<Harmony>` | **0** |
| `<FiguredBass>` | **0** |
| `<StaffText>` | **0** |

The file carries no Roman-numeral analysis, no figured bass and no staff text. It is a plain
notational record in that sense.

## 7. The whole-staff duplication check, in full

**The question.** A score file can carry one line written twice on two staves — a shape the record
establishes elsewhere in this repository's corpora, at
`cowork_rulings_2026_08_31_decision_surface_sitting.md` §3u — and such a pair looks exactly like two
real parts, because in the file it IS two staves. The
check is therefore mechanical: for **every** body staff, the ordered sequence of `<pitch>` values
over the **whole** staff — every `<Chord>` in document order, every `<pitch>` child in file order —
and then **all 36 pairs** compared.

**The result: NO PAIR is identical over the whole staff.** All 36 diverge.

The file has 9 part-list `<Staff id="N">` entries and 9 body `<Staff id="N">` sections, ids 1–9.
Every chord in the file holds exactly one pitch, so a staff's chord count and its pitch count are
the same number.

| Staff | Part name (part-list order) | Chords | Pitches |
|---:|---|---:|---:|
| 1 | Violino principale | 1,345 | 1,345 |
| 2 | Flauto 1 (Recorder) | 604 | 604 |
| 3 | Flauto 2 (Recorder) | 596 | 596 |
| 4 | Violino 1 | 564 | 564 |
| 5 | Violino 2 | 775 | 775 |
| 6 | Viola | 636 | 636 |
| 7 | Violoncello | 671 | 671 |
| 8 | Violone | 480 | 480 |
| 9 | Continuo (Harpsichord) | 690 | 690 |

**The three pairs that had matched over an earlier 24-chord window — and each of them separates.**
The index below is a position in the staff's own pitch sequence, counted from zero.

| Pair | Parts | Identical over the whole staff | First divergence, index | The two values there | Positions agreeing, over the shorter staff |
|---|---|---|---:|---|---|
| **1 ↔ 4** | Violino principale / Violino 1 | **No** | 126 | 74 against 76 | 161 of 564 — 28.5 % |
| **2 ↔ 3** | Flauto 1 / Flauto 2 | **No** | 95 | 74 against 78 | 164 of 596 — 27.5 % |
| **7 ↔ 9** | Violoncello / Continuo | **No** | 401 | 50 against 52 | 421 of 671 — 62.7 % |

**And the same verdict for the other 33 pairs: none matches over the whole staff.** Every one of
them diverges at index 0 — that is, at the very first pitch — except the three above.

| Pair | First divergence, index | The two values there | Positions agreeing, over the shorter staff |
|---|---:|---|---|
| 1 ↔ 2 | 0 | 74 against 79 | 38 of 604 |
| 1 ↔ 3 | 0 | 74 against 79 | 38 of 596 |
| 1 ↔ 5 | 0 | 74 against 67 | 59 of 775 |
| 1 ↔ 6 | 0 | 74 against 62 | 25 of 636 |
| 1 ↔ 7 | 0 | 74 against 55 | 0 of 671 |
| 1 ↔ 8 | 0 | 74 against 43 | 0 of 480 |
| 1 ↔ 9 | 0 | 74 against 55 | 4 of 690 |
| 2 ↔ 4 | 0 | 79 against 74 | 33 of 564 |
| 2 ↔ 5 | 0 | 79 against 67 | 19 of 604 |
| 2 ↔ 6 | 0 | 79 against 62 | 1 of 604 |
| 2 ↔ 7 | 0 | 79 against 55 | 0 of 604 |
| 2 ↔ 8 | 0 | 79 against 43 | 0 of 480 |
| 2 ↔ 9 | 0 | 79 against 55 | 0 of 604 |
| 3 ↔ 4 | 0 | 79 against 74 | 32 of 564 |
| 3 ↔ 5 | 0 | 79 against 67 | 23 of 596 |
| 3 ↔ 6 | 0 | 79 against 62 | 5 of 596 |
| 3 ↔ 7 | 0 | 79 against 55 | 0 of 596 |
| 3 ↔ 8 | 0 | 79 against 43 | 0 of 480 |
| 3 ↔ 9 | 0 | 79 against 55 | 0 of 596 |
| 4 ↔ 5 | 0 | 74 against 67 | 46 of 564 |
| 4 ↔ 6 | 0 | 74 against 62 | 18 of 564 |
| 4 ↔ 7 | 0 | 74 against 55 | 0 of 564 |
| 4 ↔ 8 | 0 | 74 against 43 | 0 of 480 |
| 4 ↔ 9 | 0 | 74 against 55 | 0 of 564 |
| 5 ↔ 6 | 0 | 67 against 62 | 49 of 636 |
| 5 ↔ 7 | 0 | 67 against 55 | 2 of 671 |
| 5 ↔ 8 | 0 | 67 against 43 | 0 of 480 |
| 5 ↔ 9 | 0 | 67 against 55 | 2 of 690 |
| 6 ↔ 7 | 0 | 62 against 55 | 13 of 636 |
| 6 ↔ 8 | 0 | 62 against 43 | 0 of 480 |
| 6 ↔ 9 | 0 | 62 against 55 | 11 of 636 |
| 7 ↔ 8 | 0 | 55 against 43 | 11 of 480 |
| 8 ↔ 9 | 0 | 43 against 55 | 7 of 480 |

**What this check does and does not reach, stated exactly.** It establishes that **no staff's
ordered pitch sequence is identical to any other staff's** — which is the test Ruling 19's condition
(i) names. It says nothing about rhythm, and it does not say what the passages where two staves DO
agree are — whether a doubling, an imitation at the unison, or a coincidence. No such reading is
asserted here.

## 8. What in this file's placement is a choice rather than a fact

**The directory `tools/audit/derivation_exemplars/l0-l1/` and the file name `bwv1049_03_presto` are
the Cowork writing side's choices**, made under Ruling 19's condition (ii), which requires the
extracted file to carry *a name that does* say what the music is — the container's own member name,
`temp_10111.mscx`, names nothing about it. The directory sits beside `tools/audit/derivation_boot_pack/`;
the name follows the convention `tools/dcml/bach_en_fr_suites/MS3/` uses (`BWV806_10_Gigue.mscx`).
**Neither choice is a finding, and both are the user's to overturn.**

**A line-ending caveat, stated because this file is now inside the repository.** `.gitattributes`
carries the rule `text=auto` for every path (`*`) and marks only `*.mscz` as `binary`; it carries no
rule for `*.mscx` at all, and its own comment says in terms that
*"(.mscx is uncompressed XML and is left under text=auto by design — only the committed .mscz set
needs this.)"* **So a committed `.mscx` is subject to line-ending normalization** — the
`OPEN_ITEMS.md` OI-195 / OI-34 class that the same comment names — and a later checkout on a
platform that writes CRLF may give this file different line endings from the ones recorded in §3.
**The batch that wrote this file did not edit `.gitattributes` and added no ignore rule.** Whether
a committed `.mscx` exemplar should be held byte-stable is left open and is the user's.

## 9. The authority

**Ruling 19 (§3w) of `cowork_rulings_2026_08_31_decision_surface_sitting.md`** — *the
staggered-entries slot is filled by decoding this container by dispatch and staging the `.mscx` it
holds*, with the whole-staff check of §7 above and the naming of §8 as its two conditions.
Executed by `cc_instruction_exemplar_decode_2026_09_01.md`.

**The score file beside this one is written into the repository. It is not staged in front of any
session, and this record stages nothing.**

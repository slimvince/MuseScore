# CC report — L3's PACK BUILD, SECOND HALF: TASK 1 STOPPED — the L2 freeze moves L2's record beyond the frozen shape; nothing of Task 1 committed, Tasks 2 to 4 not performed; no pack rendered, no list assembled, no algorithm changed

> **This report decides nothing and recommends nothing.** It records what was done, what was measured, and where
> the act departed from what the dispatch predicted. **No ruling was taken, no question or recommendation was put
> to the user, nothing was withheld, no pack was rendered, no pack directory was written, no session was booted, no
> brief was written, no score was staged, and no decisions-register entry was written.** Where this report would name
> a hash it cannot contain — its own commit, and the end-state commit that follows — it points at the git log. Guard
> counts are this batch's own runs; the end-state run's values are carried by `tools/audit/guard_state.json` →
> `summary` in the end-state commit.

**Dispatch:** `records/cc/instructions/cc_instruction_l3_pack_build_second_half_2026_10_16.md`, pinned at Task 0 to
blob `d17ee82b68fc84148e1130150d6e57b554bb11f3`, proven unmoved immediately before staging; the committed blob at
Task 0's commit equals the pin.
**Full close:** `records/cowork/handoff/cowork_away_returns.md`, the section **THE L3 PACK BUILD, SECOND HALF: TASK 1
STOPPED — …**, which carries the plan line and points here.

---

## TASK 1 STOPPED — THE L2 FREEZE MOVES L2's RECORD BEYOND THE FROZEN SHAPE

Task 1(g)'s D-657 comparison, run with the five repair edits and the `FROZEN["l2"]` entry in the generator, against the
committed manifest taken at `a01e9402fbaf034fe0d357214b67c06a8294309c` (`C.json`), the repaired build before the
freeze (`B1.json`) and the repaired build with the freeze (`B2.json`). **Item 1's `l2` comparison is NOT empty; every
other listed diff is empty.** The script's whole output, every differing path with both values (A is `T(C.subjects["l2"])`,
B is `B2.subjects["l2"]`; values truncated at 300 characters by `diff_paths.py`, as the dispatch orders):

```
FROZEN['l2']['finding'] equals the dispatch's text: PASS
FROZEN['l2']['reason'] equals the dispatch's text: PASS
FROZEN['l2']['date'] equals the dispatch's text: PASS
l2 not in RENDERED_BEFORE_THE_SCOPING_RULINGS: PASS
=== 1. against the committed manifest (the governing comparison)
diff(C.subjects['harmony-boundary'], B2.subjects['harmony-boundary']): EMPTY
diff(C.subjects['scoring-model'], B2.subjects['scoring-model']): EMPTY
diff(C.subjects['l0-l1'], B2.subjects['l0-l1']): EMPTY
diff(T(C.subjects['l2']), B2.subjects['l2']): 187 DIFFERENCE(S)
    /counted/extras_lines_with_a_leak_hit
        A: 61
        B: 63
    /LEAKS_IN_THE_EXTRAS/entries#len
        A: 61
        B: 63
    /LEAKS_IN_THE_EXTRAS/entries[0]/member
        A: 8
        B: 7
    /LEAKS_IN_THE_EXTRAS/entries[0]/file
        A: "08_the_fifty_six_research_extracts.md"
        B: "07_the_charter_the_layers_and_the_decisions.md"
    /LEAKS_IN_THE_EXTRAS/entries[0]/line
        A: 12
        B: 150
    /LEAKS_IN_THE_EXTRAS/entries[0]/matched[0]
        A: "docs/research_papers/rocher_robine_hanna_oudre_2010_ismir_concurrent_chords_keys.pdf"
        B: "D-527"
    /LEAKS_IN_THE_EXTRAS/entries[0]/kinds[0]
        A: "a-docs-or-src-path"
        B: "withheld-identity"
    /LEAKS_IN_THE_EXTRAS/entries[0]/the_line
        A: "**File:** `docs/research_papers/rocher_robine_hanna_oudre_2010_ismir_concurrent_chords_keys.pdf`."
        B: "class carries a note's foreignness rather than dropping it (#12); the charter's list, D-527's label list and"
    /LEAKS_IN_THE_EXTRAS/entries[1]/member
        A: 8
        B: 7
    /LEAKS_IN_THE_EXTRAS/entries[1]/file
        A: "08_the_fifty_six_research_extracts.md"
        B: "07_the_charter_the_layers_and_the_decisions.md"
    /LEAKS_IN_THE_EXTRAS/entries[1]/line
        A: 217
        B: 151
    /LEAKS_IN_THE_EXTRAS/entries[1]/matched[0]
        A: "docs/research_papers/catteau_martens_leman_2006_gfkl_key_chord_recognition.pdf"
        B: "D-207"
    /LEAKS_IN_THE_EXTRAS/entries[1]/kinds[0]
        A: "a-docs-or-src-path"
        B: "withheld-identity"
    /LEAKS_IN_THE_EXTRAS/entries[1]/the_line
        A: "**File:** `docs/research_papers/catteau_martens_leman_2006_gfkl_key_chord_recognition.pdf` (944,281"
        B: "D-207's class become one vocabulary (#6); standard names, each defined by approach and departure, or by a tone"
    /LEAKS_IN_THE_EXTRAS/entries[2]/line
        A: 399
        B: 12
    /LEAKS_IN_THE_EXTRAS/entries[2]/matched[0]
        A: "docs/research_papers/BIBLIOGRAPHY.md"
        B: "docs/research_papers/rocher_robine_hanna_oudre_2010_ismir_concurrent_chords_keys.pdf"
    /LEAKS_IN_THE_EXTRAS/entries[2]/the_line
        A: "`cowork_reading_pass_findings_2026_08_31.md` and `docs/research_papers/BIBLIOGRAPHY.md` are untouched;"
        B: "**File:** `docs/research_papers/rocher_robine_hanna_oudre_2010_ismir_concurrent_chords_keys.pdf`."
    /LEAKS_IN_THE_EXTRAS/entries[3]/line
        A: 420
        B: 217
    /LEAKS_IN_THE_EXTRAS/entries[3]/matched[0]
        A: "docs/research_papers/raphael_stoddard_2003_ismir_harmonic_analysis_pgm.pdf"
        B: "docs/research_papers/catteau_martens_leman_2006_gfkl_key_chord_recognition.pdf"
    /LEAKS_IN_THE_EXTRAS/entries[3]/the_line
        A: "**File:** `docs/research_papers/raphael_stoddard_2003_ismir_harmonic_analysis_pgm.pdf` (93,277 bytes"
        B: "**File:** `docs/research_papers/catteau_martens_leman_2006_gfkl_key_chord_recognition.pdf` (944,281"
    /LEAKS_IN_THE_EXTRAS/entries[4]/line
        A: 596
        B: 399
    /LEAKS_IN_THE_EXTRAS/entries[4]/matched[0]
        A: "docs/research_papers/temperley_2009_jnmr_unified_probabilistic_polyphonic_analysis.pdf"
        B: "docs/research_papers/BIBLIOGRAPHY.md"
    /LEAKS_IN_THE_EXTRAS/entries[4]/the_line
        A: "**File:** `docs/research_papers/temperley_2009_jnmr_unified_probabilistic_polyphonic_analysis.pdf`"
        B: "`cowork_reading_pass_findings_2026_08_31.md` and `docs/research_papers/BIBLIOGRAPHY.md` are untouched;"
    /LEAKS_IN_THE_EXTRAS/entries[5]/line
        A: 598
        B: 420
    /LEAKS_IN_THE_EXTRAS/entries[5]/matched[0]
        A: "docs/research_papers/BIBLIOGRAPHY.md"
        B: "docs/research_papers/raphael_stoddard_2003_ismir_harmonic_analysis_pgm.pdf"
    /LEAKS_IN_THE_EXTRAS/entries[5]/the_line
        A: "(`docs/research_papers/BIBLIOGRAPHY.md` line 22)."
        B: "**File:** `docs/research_papers/raphael_stoddard_2003_ismir_harmonic_analysis_pgm.pdf` (93,277 bytes"
    /LEAKS_IN_THE_EXTRAS/entries[6]/line
        A: 1004
        B: 596
    /LEAKS_IN_THE_EXTRAS/entries[6]/matched[0]
        A: "docs/research_papers/BIBLIOGRAPHY.md"
        B: "docs/research_papers/temperley_2009_jnmr_unified_probabilistic_polyphonic_analysis.pdf"
    /LEAKS_IN_THE_EXTRAS/entries[6]/the_line
        A: "`reading_pass/candidacy_upgrades.md`, `docs/research_papers/BIBLIOGRAPHY.md` and"
        B: "**File:** `docs/research_papers/temperley_2009_jnmr_unified_probabilistic_polyphonic_analysis.pdf`"
    /LEAKS_IN_THE_EXTRAS/entries[7]/line
        A: 1022
        B: 598
    /LEAKS_IN_THE_EXTRAS/entries[7]/the_line
        A: "row** (`docs/research_papers/BIBLIOGRAPHY.md` line 40: *\"Key Estimation Using a Hidden Markov Model,\""
        B: "(`docs/research_papers/BIBLIOGRAPHY.md` line 22)."
    /LEAKS_IN_THE_EXTRAS/entries[8]/line
        A: 1027
        B: 1004
    /LEAKS_IN_THE_EXTRAS/entries[8]/matched[0]
        A: "docs/research_papers/noland_sandler_2006_ismir_key_estimation_hmm.pdf"
        B: "docs/research_papers/BIBLIOGRAPHY.md"
    /LEAKS_IN_THE_EXTRAS/entries[8]/the_line
        A: "**File:** `docs/research_papers/noland_sandler_2006_ismir_key_estimation_hmm.pdf` (417,537 bytes at"
        B: "`reading_pass/candidacy_upgrades.md`, `docs/research_papers/BIBLIOGRAPHY.md` and"
    /LEAKS_IN_THE_EXTRAS/entries[9]/line
        A: 1211
        B: 1022
    /LEAKS_IN_THE_EXTRAS/entries[9]/the_line
        A: "`reading_pass/candidacy_upgrades.md`, `docs/research_papers/BIBLIOGRAPHY.md` and"
        B: "row** (`docs/research_papers/BIBLIOGRAPHY.md` line 40: *\"Key Estimation Using a Hidden Markov Model,\""
    /LEAKS_IN_THE_EXTRAS/entries[10]/line
        A: 1228
        B: 1027
    /LEAKS_IN_THE_EXTRAS/entries[10]/matched[0]
        A: "docs/research_papers/"
        B: "docs/research_papers/noland_sandler_2006_ismir_key_estimation_hmm.pdf"
    /LEAKS_IN_THE_EXTRAS/entries[10]/the_line
        A: "Boundaries\". **The printed title and author match the bibliography's row** (`docs/research_papers/"
        B: "**File:** `docs/research_papers/noland_sandler_2006_ismir_key_estimation_hmm.pdf` (417,537 bytes at"
    /LEAKS_IN_THE_EXTRAS/entries[11]/line
        A: 1393
        B: 1211
    /LEAKS_IN_THE_EXTRAS/entries[12]/line
        A: 1414
        B: 1228
    /LEAKS_IN_THE_EXTRAS/entries[12]/the_line
        A: "Italy\"*. **Title, authors, venue and year all match the bibliography's row** (`docs/research_papers/"
        B: "Boundaries\". **The printed title and author match the bibliography's row** (`docs/research_papers/"
    /LEAKS_IN_THE_EXTRAS/entries[13]/line
        A: 1630
        B: 1393
    /LEAKS_IN_THE_EXTRAS/entries[13]/the_line
        A: "`reading_pass/candidacy_upgrades.md`, `docs/research_papers/BIBLIOGRAPHY.md`,"
        B: "`reading_pass/candidacy_upgrades.md`, `docs/research_papers/BIBLIOGRAPHY.md` and"
    /LEAKS_IN_THE_EXTRAS/entries[14]/line
        A: 1648
        B: 1414
    /LEAKS_IN_THE_EXTRAS/entries[14]/matched[0]
        A: "docs/research_papers/BIBLIOGRAPHY.md"
        B: "docs/research_papers/"
    /LEAKS_IN_THE_EXTRAS/entries[14]/the_line
        A: "match the bibliography's row** (`docs/research_papers/BIBLIOGRAPHY.md` line 19: *Temperley, \"A Bayesian"
        B: "Italy\"*. **Title, authors, venue and year all match the bibliography's row** (`docs/research_papers/"
    /LEAKS_IN_THE_EXTRAS/entries[15]/line
        A: 1655
        B: 1630
    /LEAKS_IN_THE_EXTRAS/entries[15]/matched[0]
        A: "docs/research_papers/temperley_2002_icmai_bayesian_key_finding.pdf"
        B: "docs/research_papers/BIBLIOGRAPHY.md"
    /LEAKS_IN_THE_EXTRAS/entries[15]/the_line
        A: "**File:** `docs/research_papers/temperley_2002_icmai_bayesian_key_finding.pdf` (85,400 bytes at the"
        B: "`reading_pass/candidacy_upgrades.md`, `docs/research_papers/BIBLIOGRAPHY.md`,"
    /LEAKS_IN_THE_EXTRAS/entries[16]/line
        A: 1859
        B: 1648
    /LEAKS_IN_THE_EXTRAS/entries[16]/the_line
        A: "`reading_pass/candidacy_upgrades.md`, `docs/research_papers/BIBLIOGRAPHY.md` and"
        B: "match the bibliography's row** (`docs/research_papers/BIBLIOGRAPHY.md` line 19: *Temperley, \"A Bayesian"
    /LEAKS_IN_THE_EXTRAS/entries[17]/line
        A: 1888
        B: 1655
    /LEAKS_IN_THE_EXTRAS/entries[17]/matched[0]
        A: "docs/research_papers/masada_bunescu_2019_tismir_segmental_crf_chord_recognition.pdf"
        B: "docs/research_papers/temperley_2002_icmai_bayesian_key_finding.pdf"
    /LEAKS_IN_THE_EXTRAS/entries[17]/the_line
        A: "**File:** `docs/research_papers/masada_bunescu_2019_tismir_segmental_crf_chord_recognition.pdf`"
        B: "**File:** `docs/research_papers/temperley_2002_icmai_bayesian_key_finding.pdf` (85,400 bytes at the"
    /LEAKS_IN_THE_EXTRAS/entries[18]/line
        A: 2248
        B: 1859
    /LEAKS_IN_THE_EXTRAS/entries[18]/the_line
        A: "`reading_pass/candidacy_upgrades.md`, `reading_pass/population.md`, `docs/research_papers/BIBLIOGRAPHY.md`"
        B: "`reading_pass/candidacy_upgrades.md`, `docs/research_papers/BIBLIOGRAPHY.md` and"
    /LEAKS_IN_THE_EXTRAS/entries[19]/line
        A: 2273
        B: 1888
    /LEAKS_IN_THE_EXTRAS/entries[19]/matched[0]
        A: "docs/research_papers/sarawagi_cohen_2004_nips_semi_markov_crf.pdf"
        B: "docs/research_papers/masada_bunescu_2019_tismir_segmental_crf_chord_recognition.pdf"
    /LEAKS_IN_THE_EXTRAS/entries[19]/the_line
        A: "**File:** `docs/research_papers/sarawagi_cohen_2004_nips_semi_markov_crf.pdf` (87,343 bytes at the"
        B: "**File:** `docs/research_papers/masada_bunescu_2019_tismir_segmental_crf_chord_recognition.pdf`"
    /LEAKS_IN_THE_EXTRAS/entries[20]/line
        A: 2514
        B: 2248
    /LEAKS_IN_THE_EXTRAS/entries[21]/line
        A: 2536
        B: 2273
    /LEAKS_IN_THE_EXTRAS/entries[21]/matched[0]
        A: "docs/research_papers/BIBLIOGRAPHY.md"
        B: "docs/research_papers/sarawagi_cohen_2004_nips_semi_markov_crf.pdf"
    /LEAKS_IN_THE_EXTRAS/entries[21]/the_line
        A: "(`docs/research_papers/BIBLIOGRAPHY.md` line 33) names *Yang, Cwitkowitz & Duan, \"Harmonic Analysis"
        B: "**File:** `docs/research_papers/sarawagi_cohen_2004_nips_semi_markov_crf.pdf` (87,343 bytes at the"
    /LEAKS_IN_THE_EXTRAS/entries[22]/line
        A: 2548
        B: 2514
    /LEAKS_IN_THE_EXTRAS/entries[22]/matched[0]
        A: "docs/research_papers/yang_cwitkowitz_duan_2023_ismir_harana_neural_semi_crf.pdf"
        B: "docs/research_papers/BIBLIOGRAPHY.md"
    /LEAKS_IN_THE_EXTRAS/entries[22]/the_line
        A: "**File:** `docs/research_papers/yang_cwitkowitz_duan_2023_ismir_harana_neural_semi_crf.pdf` (318,293"
        B: "`reading_pass/candidacy_upgrades.md`, `reading_pass/population.md`, `docs/research_papers/BIBLIOGRAPHY.md`"
    /LEAKS_IN_THE_EXTRAS/entries[23]/line
        A: 2855
        B: 2536
    /LEAKS_IN_THE_EXTRAS/entries[23]/the_line
        A: "`reading_pass/candidacy_upgrades.md`, `reading_pass/population.md`, `docs/research_papers/BIBLIOGRAPHY.md`"
        B: "(`docs/research_papers/BIBLIOGRAPHY.md` line 33) names *Yang, Cwitkowitz & Duan, \"Harmonic Analysis"
    /LEAKS_IN_THE_EXTRAS/entries[24]/line
        A: 3168
        B: 2548
    /LEAKS_IN_THE_EXTRAS/entries[24]/matched[0]
        A: "docs/research_papers/BIBLIOGRAPHY.md"
        B: "docs/research_papers/yang_cwitkowitz_duan_2023_ismir_harana_neural_semi_crf.pdf"
    /LEAKS_IN_THE_EXTRAS/entries[24]/the_line
        A: "`reading_pass/candidacy_upgrades.md`, `reading_pass/population.md`, `docs/research_papers/BIBLIOGRAPHY.md`"
        B: "**File:** `docs/research_papers/yang_cwitkowitz_duan_2023_ismir_harana_neural_semi_crf.pdf` (318,293"
    /LEAKS_IN_THE_EXTRAS/entries[25]/line
        A: 4531
        B: 2855
    /LEAKS_IN_THE_EXTRAS/entries[25]/the_line
        A: "`docs/research_papers/BIBLIOGRAPHY.md` all stand exactly as they stand. Row 18's finding (3), row"
        B: "`reading_pass/candidacy_upgrades.md`, `reading_pass/population.md`, `docs/research_papers/BIBLIOGRAPHY.md`"
    /LEAKS_IN_THE_EXTRAS/entries[26]/line
        A: 4755
        B: 3168
    /LEAKS_IN_THE_EXTRAS/entries[26]/the_line
        A: "`cowork_reading_pass_findings_2026_08_31.md` and `docs/research_papers/BIBLIOGRAPHY.md` all stand"
        B: "`reading_pass/candidacy_upgrades.md`, `reading_pass/population.md`, `docs/research_papers/BIBLIOGRAPHY.md`"
    /LEAKS_IN_THE_EXTRAS/entries[27]/line
        A: 5014
        B: 4531
    /LEAKS_IN_THE_EXTRAS/entries[27]/matched[0]
        A: "D-525"
        B: "docs/research_papers/BIBLIOGRAPHY.md"
    /LEAKS_IN_THE_EXTRAS/entries[27]/kinds[0]
        A: "withheld-identity"
        B: "a-docs-or-src-path"
    /LEAKS_IN_THE_EXTRAS/entries[27]/the_line
        A: "  specification beside D-525 and DP-P."
        B: "`docs/research_papers/BIBLIOGRAPHY.md` all stand exactly as they stand. Row 18's finding (3), row"
    /LEAKS_IN_THE_EXTRAS/entries[28]/line
        A: 5071
        B: 4755
    /LEAKS_IN_THE_EXTRAS/entries[28]/the_line
        A: "`docs/research_papers/BIBLIOGRAPHY.md` all stand exactly as they stand. **Row 18's finding (3), row"
        B: "`cowork_reading_pass_findings_2026_08_31.md` and `docs/research_papers/BIBLIOGRAPHY.md` all stand"
    /LEAKS_IN_THE_EXTRAS/entries[29]/line
        A: 5341
        B: 5014
    /LEAKS_IN_THE_EXTRAS/entries[29]/matched[0]
        A: "docs/research_papers/BIBLIOGRAPHY.md"
        B: "D-525"
    /LEAKS_IN_THE_EXTRAS/entries[29]/kinds[0]
        A: "a-docs-or-src-path"
        B: "withheld-identity"
    /LEAKS_IN_THE_EXTRAS/entries[29]/the_line
        A: "`docs/research_papers/BIBLIOGRAPHY.md` all stand exactly as they stand. **Row 18's finding (3), row"
        B: "  specification beside D-525 and DP-P."
    /LEAKS_IN_THE_EXTRAS/entries[30]/line
        A: 6405
        B: 5071
    /LEAKS_IN_THE_EXTRAS/entries[30]/the_line
        A: "`reading_pass/population.md`, `docs/research_papers/BIBLIOGRAPHY.md` and"
        B: "`docs/research_papers/BIBLIOGRAPHY.md` all stand exactly as they stand. **Row 18's finding (3), row"
    /LEAKS_IN_THE_EXTRAS/entries[31]/line
        A: 6660
        B: 5341
    /LEAKS_IN_THE_EXTRAS/entries[31]/the_line
        A: "`docs/research_papers/BIBLIOGRAPHY.md` and `cowork_reading_pass_findings_2026_08_31.md` all stand"
        B: "`docs/research_papers/BIBLIOGRAPHY.md` all stand exactly as they stand. **Row 18's finding (3), row"
    /LEAKS_IN_THE_EXTRAS/entries[32]/line
        A: 6688
        B: 6405
    /LEAKS_IN_THE_EXTRAS/entries[32]/matched[0]
        A: "docs/research_papers/sha_pereira_2003_naacl_shallow_parsing_crf.pdf"
        B: "docs/research_papers/BIBLIOGRAPHY.md"
    /LEAKS_IN_THE_EXTRAS/entries[32]/the_line
        A: "The held file `docs/research_papers/sha_pereira_2003_naacl_shallow_parsing_crf.pdf`, **198,866 bytes**,"
        B: "`reading_pass/population.md`, `docs/research_papers/BIBLIOGRAPHY.md` and"
    /LEAKS_IN_THE_EXTRAS/entries[33]/line
        A: 6702
        B: 6660
    /LEAKS_IN_THE_EXTRAS/entries[33]/the_line
        A: "- **`docs/research_papers/BIBLIOGRAPHY.md` at row 14's own row, line 28.**"
        B: "`docs/research_papers/BIBLIOGRAPHY.md` and `cowork_reading_pass_findings_2026_08_31.md` all stand"
    /LEAKS_IN_THE_EXTRAS/entries[34]/line
        A: 6828
        B: 6688
    /LEAKS_IN_THE_EXTRAS/entries[34]/matched[0]
        A: "docs/research_papers/BIBLIOGRAPHY.md"
        B: "docs/research_papers/sha_pereira_2003_naacl_shallow_parsing_crf.pdf"
    /LEAKS_IN_THE_EXTRAS/entries[34]/the_line
        A: "`docs/research_papers/BIBLIOGRAPHY.md` or to `cowork_reading_pass_findings_2026_08_31.md`. **All stand"
        B: "The held file `docs/research_papers/sha_pereira_2003_naacl_shallow_parsing_crf.pdf`, **198,866 bytes**,"
    /LEAKS_IN_THE_EXTRAS/entries[35]/line
        A: 7145
        B: 6702
    /LEAKS_IN_THE_EXTRAS/entries[35]/the_line
        A: "`docs/research_papers/BIBLIOGRAPHY.md` and `cowork_reading_pass_findings_2026_08_31.md` all stand exactly"
        B: "- **`docs/research_papers/BIBLIOGRAPHY.md` at row 14's own row, line 28.**"
    /LEAKS_IN_THE_EXTRAS/entries[36]/line
        A: 7369
        B: 6828
    /LEAKS_IN_THE_EXTRAS/entries[36]/the_line
        A: "the extracts directory**, both checked at their own listings this sitting (`docs/research_papers/BIBLIOGRAPHY.md`"
        B: "`docs/research_papers/BIBLIOGRAPHY.md` or to `cowork_reading_pass_findings_2026_08_31.md`. **All stand"
    /LEAKS_IN_THE_EXTRAS/entries[37]/line
        A: 7648
        B: 7145
    /LEAKS_IN_THE_EXTRAS/entries[37]/the_line
        A: "`docs/research_papers/BIBLIOGRAPHY.md` — the two bibliography notes of finding (1) are routed, not made."
        B: "`docs/research_papers/BIBLIOGRAPHY.md` and `cowork_reading_pass_findings_2026_08_31.md` all stand exactly"
    /LEAKS_IN_THE_EXTRAS/entries[38]/line
        A: 7895
        B: 7369
    /LEAKS_IN_THE_EXTRAS/entries[38]/the_line
        A: "`DECISIONS.md` and no row of `docs/research_papers/BIBLIOGRAPHY.md` — finding (3) is routed, not made. It"
        B: "the extracts directory**, both checked at their own listings this sitting (`docs/research_papers/BIBLIOGRAPHY.md`"
    /LEAKS_IN_THE_EXTRAS/entries[39]/line
        A: 7916
        B: 7648
    /LEAKS_IN_THE_EXTRAS/entries[39]/the_line
        A: "derivation whole, `docs/research_papers/BIBLIOGRAPHY.md` whole, row 35's extract whole, `FRAMEWORK.md` at"
        B: "`docs/research_papers/BIBLIOGRAPHY.md` — the two bibliography notes of finding (1) are routed, not made."
    /LEAKS_IN_THE_EXTRAS/entries[40]/line
        A: 8291
        B: 7895
    /LEAKS_IN_THE_EXTRAS/entries[40]/the_line
        A: "  `cowork_reading_pass_findings_2026_08_31.md`, `docs/research_papers/BIBLIOGRAPHY.md`,"
        B: "`DECISIONS.md` and no row of `docs/research_papers/BIBLIOGRAPHY.md` — finding (3) is routed, not made. It"
    /LEAKS_IN_THE_EXTRAS/entries[41]/line
        A: 8954
        B: 7916
    /LEAKS_IN_THE_EXTRAS/entries[41]/matched[0]
        A: "D-526"
        B: "docs/research_papers/BIBLIOGRAPHY.md"
    /LEAKS_IN_THE_EXTRAS/entries[41]/kinds[0]
        A: "withheld-identity"
        B: "a-docs-or-src-path"
    /LEAKS_IN_THE_EXTRAS/entries[41]/the_line
        A: "raises **no** STOP, on the commission's §5 read at the object. It takes **no** verdict on D-526,"
        B: "derivation whole, `docs/research_papers/BIBLIOGRAPHY.md` whole, row 35's extract whole, `FRAMEWORK.md` at"
    /LEAKS_IN_THE_EXTRAS/entries[42]/line
        A: 8955
        B: 8291
    /LEAKS_IN_THE_EXTRAS/entries[42]/matched#len
        A: 2
        B: 1
    /LEAKS_IN_THE_EXTRAS/entries[42]/matched[0]
        A: "D-532"
        B: "docs/research_papers/BIBLIOGRAPHY.md"
    /LEAKS_IN_THE_EXTRAS/entries[42]/kinds[0]
        A: "withheld-identity"
        B: "a-docs-or-src-path"
    /LEAKS_IN_THE_EXTRAS/entries[42]/the_line
        A: "D-532, D-533, DP-E, R-5 or the L2 candidate-admission clause — each finding is an addition candidate or"
        B: "  `cowork_reading_pass_findings_2026_08_31.md`, `docs/research_papers/BIBLIOGRAPHY.md`,"
    /LEAKS_IN_THE_EXTRAS/entries[43]/line
        A: 8980
        B: 8954
    /LEAKS_IN_THE_EXTRAS/entries[43]/matched[0]
        A: "docs/research_papers/BIBLIOGRAPHY.md"
        B: "D-526"
    /LEAKS_IN_THE_EXTRAS/entries[43]/kinds[0]
        A: "a-docs-or-src-path"
        B: "withheld-identity"
    /LEAKS_IN_THE_EXTRAS/entries[43]/the_line
        A: "**`docs/research_papers/BIBLIOGRAPHY.md` line 37**, read at the file this day:"
        B: "raises **no** STOP, on the commission's §5 read at the object. It takes **no** verdict on D-526,"
    /LEAKS_IN_THE_EXTRAS/entries[44]/line
        A: 9141
        B: 8955
    /LEAKS_IN_THE_EXTRAS/entries[44]/matched#len
        A: 1
        B: 2
    /LEAKS_IN_THE_EXTRAS/entries[44]/matched[0]
        A: "docs/research_papers/BIBLIOGRAPHY.md"
        B: "D-532"
    /LEAKS_IN_THE_EXTRAS/entries[44]/kinds[0]
        A: "a-docs-or-src-path"
        B: "withheld-identity"
    /LEAKS_IN_THE_EXTRAS/entries[44]/the_line
        A: "**`docs/research_papers/BIBLIOGRAPHY.md` line 39**, read at the file this sitting:"
        B: "D-532, D-533, DP-E, R-5 or the L2 candidate-admission clause — each finding is an addition candidate or"
    /LEAKS_IN_THE_EXTRAS/entries[45]/line
        A: 9258
        B: 8980
    /LEAKS_IN_THE_EXTRAS/entries[45]/matched[0]
        A: "docs/research_papers/Rohrmeier2011.pdf"
        B: "docs/research_papers/BIBLIOGRAPHY.md"
    /LEAKS_IN_THE_EXTRAS/entries[45]/the_line
        A: "> `| 22 | Rohrmeier, JMM 5(1) 2011, towards a generative syntax of tonal harmony | ✓ | **ADMITTED** | The grammar DP-O's *for* side rests on. **Paywalled, and HELD since 2026-09-12** — the user placed `docs/research_papers/Rohrmeier2011.pdf`, established at its page 1 as this work on title, author,…
        B: "**`docs/research_papers/BIBLIOGRAPHY.md` line 37**, read at the file this day:"
    /LEAKS_IN_THE_EXTRAS/entries[46]/line
        A: 9268
        B: 9141
    /LEAKS_IN_THE_EXTRAS/entries[46]/the_line
        A: "**`docs/research_papers/BIBLIOGRAPHY.md` line 36**, read at the file this sitting:"
        B: "**`docs/research_papers/BIBLIOGRAPHY.md` line 39**, read at the file this sitting:"
    /LEAKS_IN_THE_EXTRAS/entries[47]/line
        A: 9477
        B: 9258
    /LEAKS_IN_THE_EXTRAS/entries[47]/matched[0]
        A: "docs/research_papers/BIBLIOGRAPHY.md"
        B: "docs/research_papers/Rohrmeier2011.pdf"
    /LEAKS_IN_THE_EXTRAS/entries[47]/the_line
        A: "**`docs/research_papers/BIBLIOGRAPHY.md` line 98**, read at the file this sitting:"
        B: "> `| 22 | Rohrmeier, JMM 5(1) 2011, towards a generative syntax of tonal harmony | ✓ | **ADMITTED** | The grammar DP-O's *for* side rests on. **Paywalled, and HELD since 2026-09-12** — the user placed `docs/research_papers/Rohrmeier2011.pdf`, established at its page 1 as this work on title, author,…
    /LEAKS_IN_THE_EXTRAS/entries[48]/line
        A: 9630
        B: 9268
    /LEAKS_IN_THE_EXTRAS/entries[48]/the_line
        A: "**`docs/research_papers/BIBLIOGRAPHY.md` line 100**, read at the file this sitting:"
        B: "**`docs/research_papers/BIBLIOGRAPHY.md` line 36**, read at the file this sitting:"
    /LEAKS_IN_THE_EXTRAS/entries[49]/line
        A: 9837
        B: 9477
    /LEAKS_IN_THE_EXTRAS/entries[49]/the_line
        A: "**`docs/research_papers/BIBLIOGRAPHY.md`, line 48 (the register row), read at the file:**"
        B: "**`docs/research_papers/BIBLIOGRAPHY.md` line 98**, read at the file this sitting:"
    /LEAKS_IN_THE_EXTRAS/entries[50]/line
        A: 10014
        B: 9630
    /LEAKS_IN_THE_EXTRAS/entries[50]/the_line
        A: "**`docs/research_papers/BIBLIOGRAPHY.md`, line 99** — the register row, in the section *\"The grammar"
        B: "**`docs/research_papers/BIBLIOGRAPHY.md` line 100**, read at the file this sitting:"
    /LEAKS_IN_THE_EXTRAS/entries[51]/line
        A: 10032
        B: 9837
    /LEAKS_IN_THE_EXTRAS/entries[51]/the_line
        A: "and stands; the second half is false at the object.** `docs/research_papers/BIBLIOGRAPHY.md` line 137,"
        B: "**`docs/research_papers/BIBLIOGRAPHY.md`, line 48 (the register row), read at the file:**"
    /LEAKS_IN_THE_EXTRAS/entries[52]/member
        A: 9
        B: 8
    /LEAKS_IN_THE_EXTRAS/entries[52]/file
        A: "09_the_empirical_findings_ledger.md"
        B: "08_the_fifty_six_research_extracts.md"
    /LEAKS_IN_THE_EXTRAS/entries[52]/line
        A: 94
        B: 10014
    /LEAKS_IN_THE_EXTRAS/entries[52]/matched[0]
        A: "docs/scoring_model.md"
        B: "docs/research_papers/BIBLIOGRAPHY.md"
    /LEAKS_IN_THE_EXTRAS/entries[52]/kinds#len
        A: 2
        B: 1
    /LEAKS_IN_THE_EXTRAS/entries[52]/the_line
        A: ">    constraints and stop rules. Existing seeds: `DEFECT_TYPES.md`, `docs/scoring_model.md` §8, the"
        B: "**`docs/research_papers/BIBLIOGRAPHY.md`, line 99** — the register row, in the section *\"The grammar"
    /LEAKS_IN_THE_EXTRAS/entries[53]/member
        A: 9
        B: 8
    /LEAKS_IN_THE_EXTRAS/entries[53]/file
        A: "09_the_empirical_findings_ledger.md"
        B: "08_the_fifty_six_research_extracts.md"
    /LEAKS_IN_THE_EXTRAS/entries[53]/line
        A: 145
        B: 10032
    /LEAKS_IN_THE_EXTRAS/entries[53]/matched[0]
        A: "docs/scoring_model.md"
        B: "docs/research_papers/BIBLIOGRAPHY.md"
    /LEAKS_IN_THE_EXTRAS/entries[53]/kinds#len
        A: 2
        B: 1
    /LEAKS_IN_THE_EXTRAS/entries[53]/the_line
        A: "| **`docs/scoring_model.md` §8** | **YES** | Read WHOLE at the object, `:1129–1457`, by the first harvest. **Eight** entries in the body come from it — C1, C2, C4, C5, C6, C7, the restatement C8, and, since the extension of 2026-08-26, the ruled restatement C9, whose EARLIER wording stands refused …
        B: "and stands; the second half is false at the object.** `docs/research_papers/BIBLIOGRAPHY.md` line 137,"
    /LEAKS_IN_THE_EXTRAS/entries[54]/line
        A: 156
        B: 94
    /LEAKS_IN_THE_EXTRAS/entries[54]/the_line
        A: "2026-08-07 routed the chord- and function-layer refuted-repair family into `docs/scoring_model.md` §8"
        B: ">    constraints and stop rules. Existing seeds: `DEFECT_TYPES.md`, `docs/scoring_model.md` §8, the"
    /LEAKS_IN_THE_EXTRAS/entries[55]/line
        A: 166
        B: 145
    /LEAKS_IN_THE_EXTRAS/entries[55]/matched#len
        A: 2
        B: 1
    /LEAKS_IN_THE_EXTRAS/entries[55]/matched[0]
        A: "D-490"
        B: "docs/scoring_model.md"
    /LEAKS_IN_THE_EXTRAS/entries[55]/kinds#len
        A: 1
        B: 2
    /LEAKS_IN_THE_EXTRAS/entries[55]/kinds[0]
        A: "withheld-identity"
        B: "a-docs-or-src-path"
    /LEAKS_IN_THE_EXTRAS/entries[55]/the_line
        A: "OI-2, which uses the phrase in this project's sense — *\"**D-490** and **D-491** are the falsification"
        B: "| **`docs/scoring_model.md` §8** | **YES** | Read WHOLE at the object, `:1129–1457`, by the first harvest. **Eight** entries in the body come from it — C1, C2, C4, C5, C6, C7, the restatement C8, and, since the extension of 2026-08-26, the ruled restatement C9, whose EARLIER wording stands refused …
    /LEAKS_IN_THE_EXTRAS/entries[56]/line
        A: 167
        B: 156
    /LEAKS_IN_THE_EXTRAS/entries[56]/matched[0]
        A: "D-491"
        B: "docs/scoring_model.md"
    /LEAKS_IN_THE_EXTRAS/entries[56]/kinds#len
        A: 1
        B: 2
    /LEAKS_IN_THE_EXTRAS/entries[56]/kinds[0]
        A: "withheld-identity"
        B: "a-docs-or-src-path"
    /LEAKS_IN_THE_EXTRAS/entries[56]/the_line
        A: "and the refuted repair behind that recommendation\"* — and D-491 is a decisions-register entry whose"
        B: "2026-08-07 routed the chord- and function-layer refuted-repair family into `docs/scoring_model.md` §8"
    /LEAKS_IN_THE_EXTRAS/entries[57]/line
        A: 217
        B: 166
    /LEAKS_IN_THE_EXTRAS/entries[57]/matched#len
        A: 1
        B: 2
    /LEAKS_IN_THE_EXTRAS/entries[57]/matched[0]
        A: "docs/scoring_model.md"
        B: "D-490"
    /LEAKS_IN_THE_EXTRAS/entries[57]/kinds#len
        A: 2
        B: 1
    /LEAKS_IN_THE_EXTRAS/entries[57]/kinds[0]
        A: "a-docs-or-src-path"
        B: "withheld-identity"
    /LEAKS_IN_THE_EXTRAS/entries[57]/the_line
        A: "| **C9** — admitted as the restatement *\"The presence of a leading tone does not distinguish the genuine cases.\"* (`cowork_fact_gate_admissions_2026_08_26.md:120`) | `cowork_empirical_findings_candidates.md` §C9, `:301–321` | **The admitted sentence's SUBJECT is a population defined by a mechanis…
        B: "OI-2, which uses the phrase in this project's sense — *\"**D-490** and **D-491** are the falsification"
    /LEAKS_IN_THE_EXTRAS/entries[58]/line
        A: 318
        B: 167
    /LEAKS_IN_THE_EXTRAS/entries[58]/matched[0]
        A: "docs/scoring_model.md"
        B: "D-491"
    /LEAKS_IN_THE_EXTRAS/entries[58]/kinds#len
        A: 2
        B: 1
    /LEAKS_IN_THE_EXTRAS/entries[58]/kinds[0]
        A: "a-docs-or-src-path"
        B: "withheld-identity"
    /LEAKS_IN_THE_EXTRAS/entries[58]/the_line
        A: "  same entry (`docs/scoring_model.md:1418–1424`, register entry **D-300**). The sentence was neither"
        B: "and the refuted repair behind that recommendation\"* — and D-491 is a decisions-register entry whose"
    /LEAKS_IN_THE_EXTRAS/entries[59]/line
        A: 351
        B: 217
    /LEAKS_IN_THE_EXTRAS/entries[59]/matched[0]
        A: "D-575"
        B: "docs/scoring_model.md"
    /LEAKS_IN_THE_EXTRAS/entries[59]/kinds#len
        A: 1
        B: 2
    /LEAKS_IN_THE_EXTRAS/entries[59]/kinds[0]
        A: "withheld-identity"
        B: "a-docs-or-src-path"
    /LEAKS_IN_THE_EXTRAS/entries[59]/the_line
        A: "  DESIGN decision (**D-575**)."
        B: "| **C9** — admitted as the restatement *\"The presence of a leading tone does not distinguish the genuine cases.\"* (`cowork_fact_gate_admissions_2026_08_26.md:120`) | `cowork_empirical_findings_candidates.md` §C9, `:301–321` | **The admitted sentence's SUBJECT is a population defined by a mechanis…
    /LEAKS_IN_THE_EXTRAS/entries[60]/line
        A: 644
        B: 318
    /LEAKS_IN_THE_EXTRAS/entries[60]/the_line
        A: "eight `docs/scoring_model.md` §8 entries.** Ruling 1 of"
        B: "  same entry (`docs/scoring_model.md:1418–1424`, register entry **D-300**). The sentence was neither"
=== 2. against the repaired build before the freeze
diff(B1.subjects['harmony-boundary'], B2.subjects['harmony-boundary']): EMPTY
diff(B1.subjects['scoring-model'], B2.subjects['scoring-model']): EMPTY
diff(B1.subjects['l0-l1'], B2.subjects['l0-l1']): EMPTY
diff(T(B1.subjects['l2']), B2.subjects['l2']): EMPTY
top-level keys the same set (B1, B2): PASS
top-level 'generator' equal (B1, B2): PASS
top-level 'the_STOPS' equal (B1, B2): PASS
top-level 'the_pack_files_in_order' equal (B1, B2): PASS
top-level 'the_rulings_it_executes' equal (B1, B2): PASS
top-level 'what_is_AUTHORED' equal (B1, B2): PASS
top-level 'what_is_DERIVED' equal (B1, B2): PASS
top-level 'what_this_is' equal (B1, B2): PASS
top-level '★_it_boots_no_session' equal (B1, B2): PASS
top-level '★_the_verdicts_clear_nothing' equal (B1, B2): PASS
RESULT: STOP
```

**What the 187 paths are, measured rather than read off the list.** The paths are all under
`LEAKS_IN_THE_EXTRAS` and `counted/extras_lines_with_a_leak_hit`; most are index shifts. A diagnosis script — NOT
ordered by the dispatch, run after the STOP and before the restore, writing nothing into the repository (D-669: a
cause is established before anything is touched; text in §6) — compared the two leak lists as whole entries:

```
entries: committed 61, today 63
in today's list and not the committed one: 2
    {"member": 7, "file": "07_the_charter_the_layers_and_the_decisions.md", "line": 150, "matched": ["D-527"], "kinds": ["withheld-identity"], "the_line": "class carries a note's foreignness rather than dropping it (#12); the charter's list, D-527's label list and"}
    {"member": 7, "file": "07_the_charter_the_layers_and_the_decisions.md", "line": 151, "matched": ["D-207"], "kinds": ["withheld-identity"], "the_line": "D-207's class become one vocabulary (#6); standard names, each defined by approach and departure, or by a tone"}
in the committed list and not today's: 0
the committed entries stand in today's list, in the same order: True
diff(T(C.l2), B2.l2 with exactly those entries removed and its count reset): EMPTY
```

So the movement is **exactly two entries inserted** into `l2`'s extras leak list and its count moved with them —
nothing removed, the committed entries standing in the same order, and with those two taken out the record equals the
frozen shape. Both new lines are in member (7), the charter member (`FRAMEWORK.md` §5 and §9, the shared
`CHARTER_MEMBER_7`), and each names an identity of L2's withheld family. **This is the risk the freeze derivation named
in advance** (`records/cowork/rulings/cowork_rulings_2026_10_15_l2_freeze_derivation_sitting.md` §2): a frozen subject is
still built from today's sources, `frozen_from_disk` re-points member sizes at the directory but not the extras' leak
list, and L2's charter source has changed since L2's pack was rendered. **Established at the objects after the close commit:** both lines stand in L2's block of `FRAMEWORK.md` §5
(`FRAMEWORK.md:450–451`, inside the heading *"L2 — The tonal reading. The one entangled decision."*), as part of the
stated ground of the elaboration-list amendment that
`records/cc/instructions/cc_instruction_l2_ratification_application_2026_10_14.md` (Task 2) carried — the amendment the
`FROZEN["l2"]` finding names — and neither occurs in `tools/audit/derivation_boot_pack/l2/07_the_charter_the_layers_and_the_decisions.md`
(a search of that file for both lines' phrases and for *appoggiatura* matches nothing). *(★ CORRECTED in the end-state
commit; FORMER WORDING, PRESERVED (#12): "*Read at the rendered line text and not otherwise established:* the two lines'
wording is consistent with the 2026-10-14 amendment to L2's block of `FRAMEWORK.md` §5 that the `FROZEN["l2"]` finding
names; `FRAMEWORK.md` was not opened by this batch." — true when the close was written, and made false by the check run
after it.)*

**The acts the dispatch orders on this STOP, done.** The generator was restored with `git checkout
a01e9402fbaf034fe0d357214b67c06a8294309c -- tools/audit/gen_derivation_boot_pack.py` (exit 0); the tracked file's
`git hash-object` is `b1e142da972bd2c0b1ed67df02e5a3ab66320fab`, equal to the blob at that commit; the manifest was
never written (no write run of the generator was made in this batch) and hashes
`db340baf15f7fa3ad1ab29d067f12a47b4354ace`, equal to its blob there; `git diff --stat
a01e9402fbaf034fe0d357214b67c06a8294309c --` over the generator, the manifest and `tools/audit/derivation_boot_pack/` is
empty. **Nothing of Task 1 was committed, and the batch went from the STOP to Task 5.** The derivation's own bound
applies: what the repair is now is the user's (D-436, D-657), and no fix was taken.

---

## 1. The commits, by explicit hash

| Act | Commit | What it carries |
|---|---|---|
| the tree met | `a01e9402fbaf034fe0d357214b67c06a8294309c` | `master` and `origin/master`, both read at the ref files |
| Task 0 | `c60fb31d50ad371942ae8276cf05055b89cb2c4b` | this dispatch, handoff entries 410 to 413, the two 2026-10-15 ruling records, the L3 extracts cut list, `tools/audit/evidence_pin_membership.json` |
| Task 1 | **none** | STOPPED at (g); the generator restored (above) |
| Tasks 2, 3, 4 | **none** | not performed — the dispatch sends the batch from Task 1's STOP to its close |
| the close | see the git log | `STATUS.md`, `STATUS_ARCHIVE.md`, the re-aimed `tools/audit/gen_status_batch_bound.py`, `tools/audit/status_batch_bound.json`, `tools/audit/session_start_read_size.json`, this report, the close section |
| the end state | see the git log | the full guard run at the close's tree, with the artifacts A2 orders regenerated |

After every push, `.git/refs/remotes/origin/master` was read with the file tools and named the commit just made. Every
commit was verified at the object by explicit hash (`git show --stat <hash>`).

## 2. The guard states

**THE START STATE, a `--check` run before the first edit:** 81 run, **15 failing**, 4 not run, 20 historical — the
committed guard state's fourteen failing (read at the tip's `tools/audit/guard_state.json`), plus
`gen_evidence_pin_membership.py --check`, which A2 predicts for exactly this cause (the two untracked 2026-10-15 ruling
records) and Task 0 act (2) cleared. The runner's own *"STALE vs the run"* line. `gen_guard_classification.py --check`
(exit 2) gave the standing STOP: *"STOP: tool(s) in the guard-state population with no authored verdict:
['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py',
'tools/audit/gen_withheld_family_reading.py']"*. The start run's whole output:

```
STALE vs the run: guard_state.json does not re-derive
  [PASS] tools/audit/register_lint.py 
  [PASS] tools/audit/index_status_lint.py --check
  [PASS] tools/audit/gen_arm_comment_sweep.py --check
  [PASS] tools/audit/local_patches_check.py 
  [PASS] tools/audit/local_patches_check.py --establish --check
  [PASS] tools/audit/guard_armed_check.py 
  [PASS] tools/audit/process_check.py --establish --check
  [PASS] tools/audit/shell_read_guard.py --establish --check
  [PASS] tools/audit/output_encoding.py --establish --check
  [PASS] tools/audit/changed_paths.py --establish
  [PASS] tools/audit/claude_md_rule_triage.py --check
  [PASS] tools/audit/corpus_arm_stamp.py --check
  [PASS] tools/audit/corpus_arm_stamp.py --establish --check
  [PASS] tools/audit/instrument_arm_declaration_effect.py --check
  [FAIL] tools/audit/gen_phase3_gate_partition.py --check
  [PASS] tools/audit/gen_nongating_apparatus_rows.py --check
  [PASS] tools/audit/gen_discard_records.py --check
  [PASS] tools/audit/decisions/gen_true_half_reach.py --check
  [PASS] tools/audit/decisions/gen_true_half_reach_rows.py --check
  [PASS] tools/audit/gen_gating_row_sizing.py --check
  [FAIL] tools/audit/gen_filing_convention_application.py --check
  [PASS] tools/audit/decisions/gen_phase1q_snapshot_establishment.py --check
  [PASS] tools/audit/gen_period_stratum_split.py --check
  [PASS] tools/audit/gen_july_screen.py --check
  [PASS] tools/audit/gen_specification_document_set.py --check
  [PASS] tools/audit/gen_l0_l1_outgoing_population.py --check
  [PASS] tools/audit/gen_withheld_family_reading.py --subject l2 --check
  [PASS] tools/audit/gen_withheld_family_reading.py --subject l3 --check
  [FAIL] tools/audit/gen_artifact_inventory.py --check
  [FAIL] tools/audit/gen_artifact_inventory_surface.py --check
  [PASS] tools/audit/gen_status_archive_pass.py --check
  [PASS] tools/audit/gen_doc_change_candidates.py --check
  [FAIL] tools/audit/gen_test_construction_evidence.py --check
  [PASS] tools/audit/gen_decisions_filter.py --check
  [FAIL] tools/audit/gen_retirement_caller_check.py --check
  [PASS] tools/audit/gen_deciding_act_recovery.py --check
  [PASS] tools/audit/gen_rulings_sort.py --check
  [PASS] tools/audit/gen_sole_carrier_subclass.py --check
  [PASS] tools/audit/gen_ratified_document_check.py --check
  [FAIL] tools/audit/decisions/apply_soft_discard.py --check
  [FAIL] tools/audit/decisions/apply_residue_discard.py --check
  [PASS] tools/audit/gen_framework_untrusted_candidates.py --check
  [PASS] tools/audit/gen_phase1_gate_readers.py --check
  [PASS] tools/audit/gen_discard_reach_split.py --check
  [PASS] tools/audit/decisions/gen_retired_subject_moves.py --check
  [PASS] tools/audit/gen_census_movement_classification.py --check
  [PASS] tools/audit/gen_governing_surface_spans.py --check
  [PASS] tools/audit/gen_governing_surface_readers.py --check
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair CLAUDE.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair OPEN_ITEMS.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair DECISIONS.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair STATUS.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair BUILD_AND_TEST.md
  [PASS] tools/audit/gen_status_batch_bound.py --check
  [PASS] tools/audit/gen_status_residue_move.py --check
  [PASS] tools/audit/gen_retirement_census_movement.py --check
  [PASS] tools/audit/gen_claude_md_finer_spans.py --check
  [PASS] tools/audit/gen_claude_md_finer_surface.py --check
  [FAIL] tools/audit/gen_evidence_pin_membership.py --check
  [PASS] tools/audit/gen_session_start_read_size.py --check
  [PASS] tools/audit/gen_defense_share.py --check
  [FAIL] tools/audit/gen_epoch_write_path.py --check
  [FAIL] tools/audit/gen_derivation_boot_pack.py --check
  [FAIL] tools/audit/gen_recognizer_establishment_sort.py --check
  [PASS] tools/audit/gen_l2_withheld_documents.py --check
  [PASS] tools/audit/gen_l2_withheld_documents.py --subject l3 --check
  [PASS] tools/audit/decisions/gen_decisions_register.py --check
  [FAIL] tools/audit/decisions/gen_cluster_dispositions.py --verify
  [PASS] tools/audit/decisions/gen_cluster_dispositions.py --check
  [PASS] tools/audit/decisions/gen_cluster_dispositions.py --producible
  [FAIL] tools/audit/decisions/gen_home_classification.py --check
  [FAIL] tools/audit/decisions/gen_phase1p_delegation_bar.py --check
  [PASS] tools/audit/decisions/gen_reads5_repack.py --check
  [PASS] tools/audit/decisions/gen_decision_clusters.py --check
  [PASS] tools/audit/decisions/gen_phase1w_legacy_verification.py --check
  [PASS] tools/audit/decisions/reaim_home_anchors.py --check
  [PASS] tools/audit/decisions/gen_live_prohibition_pointers.py --check
  [PASS] tools/audit/gen_claude_md_growth.py --check
  [PASS] tools/audit/prune_at_amendment_lint.py --check
  [PASS] tools/open_items_split_check.py 
  [PASS] tools/notation_seams/gen_callpath_facts.py --check
  [NOT RUN] tools/audit/gen_ratification_surface_set.py
  [NOT RUN] tools/audit/reaim_ratification_surface_paths.py
  [NOT RUN] tools/audit/decisions/gen_verbatim_subject_consistency.py
  [NOT RUN] tools/audit/gen_reserved_word_scanner.py
  [HISTORICAL] tools/audit/gen_phase1_completion_inventory.py
  [HISTORICAL] tools/audit/gen_phase1_finish_line.py
  [HISTORICAL] tools/audit/decisions/gen_outstanding_delegations.py
  [HISTORICAL] tools/audit/gen_claude_md_finer_archive.py
  [HISTORICAL] tools/audit/gen_post_split_archive.py
  [HISTORICAL] tools/audit/gen_l2_outgoing_population.py
  [HISTORICAL] tools/audit/decisions/gen_phase1n_reading_regime.py
  [HISTORICAL] tools/audit/decisions/gen_reads5_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads6_yield.py
  [HISTORICAL] tools/audit/decisions/gen_phase1m_measurements.py
  [HISTORICAL] tools/audit/decisions/gen_phase1g_triage.py
  [HISTORICAL] tools/audit/decisions/gen_reads1_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads2_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads3_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads4_yield.py
  [HISTORICAL] tools/audit/decisions/gen_finish_line_item1_routes.py
  [HISTORICAL] tools/audit/decisions/gen_item1_rehome_blocker.py
  [HISTORICAL] tools/audit/decisions/gen_r1_superseded_reach.py
  [HISTORICAL] tools/audit/decisions/gen_reads4_oi326_application.py
  [HISTORICAL] tools/audit/gen_claude_md_prune_backlog.py
81 guard(s) run, 15 failing, 4 not run, 20 historical record(s)
```

**`gen_derivation_boot_pack.py --check` stays red**, `l2` not having been frozen. A2's end prediction (the fourteen
less this tool, after Task 4's render) does not apply as written, Task 4 not having run.

**THE END STATE IS NOT ASSERTED HERE.** The one further commit carries it.

## 3. A1 to A3, and E0 to E5, graded

- **A1 — HELD, BY CONTENT.** The five tracked inputs each diffed empty against `a01e9402…`. The tracked population
  through `tools/audit/changed_paths.py` showed exactly one tracked modification, `tools/audit/claude_md_finer_archive.json`,
  whose hash through git's filters equals the tip's blob (`1df4f20771b6782cbb965c293db4d445bc7ec892`) — re-established,
  left untouched, never staged. Every path of Task 0's list was untracked; **entry 413 was present** and is landed, so the
  subject reads `entries 410-413`. **Untracked paths outside Task 0's list, NOT landed:** none under `records/`,
  `reading_pass/` or `ratification_surfaces/`; elsewhere `Claude outputs/`, `Codex research inventory/`,
  `docs/research_papers/polyph9-release/`, two files under `external resarch summary/`, the `scratch_artifacts/`
  population and `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`. No further handoff entry or ruling
  record appeared during the run. After the restore, the tracked population again showed that one modification only.
- **A2 — HELD AT THE START** (§2). The end prediction does not apply as written (§2).
- **A3 — verified at the objects after the last commit**, stated in the close section's end-state part.
- **E0 — MET.** The nine paths in one commit; `origin/master` at it; every path accounted for.
- **E1 — NOT MET: TASK 1 STOPPED AT (g).** Its other limbs hold: the ten files proved equal to their committed blobs, the
  ten digests taken twice, agreeing and equal to the premise ledger's (§4); (e) wholly empty (§5). (g) non-empty for `l2`;
  no manifest regenerated, nothing committed, every pack directory byte-unchanged.
- **E2, E3/E4 — NOT MET: TASKS 2, 3 AND 4 NOT PERFORMED.**
- **E5** — carried by the end-state commit, not asserted here.

## 4. Task 1(a) and (b) — the ten files and their digests

The directory listing (by the file tools) and the tip's tree (`git ls-tree --name-only a01e9402… tools/audit/derivation_boot_pack/l2/`)
name the same ten files. For each, `git hash-object` (through git's filters), `git hash-object --no-filters` and
`git rev-parse a01e9402…:<path>` agree, and each equals the premise ledger's value:

| File | Digest (all three forms agree; equal to the premise ledger) |
|---|---|
| `00_READ_THIS_FIRST.md` | `fd27dee7a4b6bca3454d12c659aa34a96cd1abc1` |
| `01_the_phase_definitions.md` | `518b1e50d60af2b4e2ddcd8978623832eb071899` |
| `02_the_guiding_principles_and_the_conventions.md` | `41288e7375faca980c566ca0367fca1c7de760e8` |
| `03_the_writing_standards.md` | `a41983018cb27ed4a47d24ff8bb9e95181ed0572` |
| `04_the_dispatch_protocol.md` | `72b8a1fb58ed50a2fbdc65a08ff4ec68e863e9da` |
| `05_the_ratified_design_intent.md` | `6ae0b1d8c9a830cfc3f2021f37460f05fad23547` |
| `06_the_defect_type_catalog.md` | `1dec7621dc48d89242cacaf79b3048cd965d6a19` |
| `07_the_charter_the_layers_and_the_decisions.md` | `5796c2d1bda0520b067ccde300e25336b9606884` |
| `08_the_fifty_six_research_extracts.md` | `69404bace220b25589e78edc7c89c513ae5a0e2e` |
| `09_the_empirical_findings_ledger.md` | `925c458e6a77b728bc9815ac75fb8c8a6c1bc0f6` |

## 5. Task 1(c) to (g) — the edits made, the two comparisons, and the restore

**(c)** `B0.json` dumped with the generator untouched; `C.json` taken by `git show a01e9402…:tools/audit/derivation_boot_pack.json`.

**(d)** The five edits made in the dispatch's order, each old text found exactly once. After them, `subject in FROZEN`
occurred **nowhere in `build_subject`**; the three remaining hits in the file are `if subject in FROZEN:` in `build()`,
`write_all` and `check_all`, untouched.

**(e) — WHOLLY EMPTY: the repair is inert before the freeze.** `B1.json` dumped; the comparison's output:

```
diff(B0.subjects, B1.subjects): EMPTY
top-level keys the same set: PASS
top-level 'generator' equal: PASS
top-level 'the_pack_files_in_order' equal: PASS
top-level 'what_is_AUTHORED' equal: PASS
top-level 'what_is_DERIVED' equal: PASS
top-level 'what_this_is' equal: PASS
top-level '★_it_boots_no_session' equal: PASS
top-level '★_the_verdicts_clear_nothing' equal: PASS
B1.the_STOPS == B0.the_STOPS + [the added string]: PASS
B1.the_rulings_it_executes == B0.the_rulings_it_executes + [the added string]: PASS
RESULT: ALL PASS
```

*(The first run of this script ended on a console encoding error at its first line containing `★`, after printing the
diff and five PASS lines; it was re-run with `PYTHONIOENCODING=utf-8` and the output above is that run's. §7 item 3.)*

**(f)** The `FROZEN["l2"]` entry inserted between the table's last comment line and its `}`, its `digests` the ten
values of §4 in the premise ledger's order, its `finding`, `date` and `reason` the dispatch's texts — proven equal to
them by the (g) script's first three lines — and the ordered comment after it. `l2` was not added to
`RENDERED_BEFORE_THE_SCOPING_RULINGS` (proven by the (g) script's fourth line).

**(g)** `B2.json` dumped; the comparison is at the head of this report. **Item 2 — the repaired build before the freeze —
is wholly empty**, including `diff(T(B1.subjects["l2"]), B2.subjects["l2"])`: the freeze moves today's build of `l2` by
exactly the frozen shape. It is the committed record, rendered on 2026-09-27, that today's sources no longer reproduce.

**(h)** not reached.

## 6. The scripts, whole

All kept in this session's scratch folder, outside the repository.

`dump_build.py` — as the dispatch gives it:

```python
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location(
    "dbp", r"C:\s\MS\tools\audit\gen_derivation_boot_pack.py")
dbp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dbp)
manifest, packs, displaced = dbp.build()
with open(sys.argv[1], "w", encoding="utf-8", newline="") as fh:
    fh.write(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
print("dumped", sys.argv[1], "subjects:", sorted(manifest["subjects"]))
```

`diff_paths.py` — the helper the dispatch orders written:

```python
"""diff(a, b, path="") -> every JSON path at which two parsed values differ.

Recurses into dicts by key and lists by index; a missing key or a different list length is
itself a difference at that path.  Each difference carries both values, printed truncated to
300 characters.  Kept outside the repository working tree; imported by the comparison scripts.
"""
import json

MISSING = "<MISSING>"


def _show(v) -> str:
    if v is MISSING:
        return MISSING
    s = json.dumps(v, ensure_ascii=False)
    return s if len(s) <= 300 else s[:300] + "…"


def diff(a, b, path=""):
    out = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in list(a.keys()) + [k for k in b.keys() if k not in a]:
            p = f"{path}/{k}"
            if k not in a:
                out.append((p, MISSING, _show(b[k])))
            elif k not in b:
                out.append((p, _show(a[k]), MISSING))
            else:
                out.extend(diff(a[k], b[k], p))
        return out
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            out.append((f"{path}#len", str(len(a)), str(len(b))))
        for i in range(min(len(a), len(b))):
            out.extend(diff(a[i], b[i], f"{path}[{i}]"))
        return out
    if type(a) is not type(b) or a != b:
        out.append((path, _show(a), _show(b)))
    return out


def report(name, d):
    print(f"{name}: {'EMPTY' if not d else f'{len(d)} DIFFERENCE(S)'}")
    for p, x, y in d:
        print(f"    {p}\n        A: {x}\n        B: {y}")
    return not d
```

`cmp_t1e.py` — Task 1(e):

```python
"""Task 1(e): the repair is inert before the freeze.  B0 (generator untouched) against B1 (the five
edits made, no freeze).  Kept outside the repository working tree."""
import json
import sys
import os

S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, S)
from diff_paths import diff, report  # noqa: E402

B0 = json.load(open(os.path.join(S, "B0.json"), encoding="utf-8"))
B1 = json.load(open(os.path.join(S, "B1.json"), encoding="utf-8"))

STOP_ADDED = ("an entry of `RENDERED_BEFORE_THE_SCOPING_RULINGS` naming a subject that is not FROZEN, "
              "or lacking its finding, its date or its reason")
RULING_ADDED = (
    "The derivation recorded at "
    "`records/cowork/rulings/cowork_rulings_2026_10_15_l2_freeze_derivation_sitting.md`, "
    "applying Ruling 1 of `cowork_rulings_2026_09_27_l2_leak_list_sitting.md` as ruled — the "
    "field choice, limb B and the additions' wording keyed on the authored list "
    "`RENDERED_BEFORE_THE_SCOPING_RULINGS` rather than on FROZEN membership — and the freeze "
    "of the spent `l2` pack (Ruling 1 of `cowork_rulings_2026_10_15_l3_boot_list_sitting.md`, "
    "noted).")

ok = True
ok &= report("diff(B0.subjects, B1.subjects)", diff(B0["subjects"], B1["subjects"]))
same_keys = set(B0) == set(B1)
print("top-level keys the same set:", "PASS" if same_keys else "FAIL")
ok &= same_keys
for k in sorted(set(B0) & set(B1)):
    if k in ("subjects", "the_STOPS", "the_rulings_it_executes"):
        continue
    eq = B0[k] == B1[k]
    print(f"top-level {k!r} equal:", "PASS" if eq else "FAIL")
    ok &= eq
a = B1["the_STOPS"] == B0["the_STOPS"] + [STOP_ADDED]
b = B1["the_rulings_it_executes"] == B0["the_rulings_it_executes"] + [RULING_ADDED]
print("B1.the_STOPS == B0.the_STOPS + [the added string]:", "PASS" if a else "FAIL")
print("B1.the_rulings_it_executes == B0.the_rulings_it_executes + [the added string]:",
      "PASS" if b else "FAIL")
ok &= a and b
print("RESULT:", "ALL PASS" if ok else "STOP")
sys.exit(0 if ok else 3)
```

`cmp_t1g.py` — Task 1(g):

```python
"""Task 1(g): the D-657 comparison.  C = the committed manifest at a01e9402…, B1 = the repaired
build before the freeze, B2 = the repaired build with FROZEN["l2"].  T(rec) applies to a record
exactly what build() does to a frozen subject's record, in the same order.  Also checks the
authored freeze fields against the dispatch's verbatim texts.  Kept outside the working tree."""
import copy
import importlib.util
import json
import os
import sys

S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, S)
from diff_paths import diff, report  # noqa: E402

spec = importlib.util.spec_from_file_location(
    "dbp", r"C:\s\MS\tools\audit\gen_derivation_boot_pack.py")
dbp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dbp)

C = json.load(open(os.path.join(S, "C.json"), encoding="utf-8"))
B1 = json.load(open(os.path.join(S, "B1.json"), encoding="utf-8"))
B2 = json.load(open(os.path.join(S, "B2.json"), encoding="utf-8"))


def T(rec):
    r = copy.deepcopy(rec)
    r["★_FROZEN"] = dbp.frozen_block("l2")
    dbp.frozen_from_disk("l2", r)
    return r


ok = True
FINDING = ("Its deriving session has RUN (Ruling 1 of "
           "`records/cowork/rulings/cowork_rulings_2026_10_15_l3_boot_list_sitting.md`, noted), and "
           "the specification it produced, `cowork_derived_specification_l2_2026_10_10.md`, was "
           "ratified face by face on 2026-10-13 and 2026-10-14. The pack is STALE against today's "
           "sources — its rendered charter member lacks the 2026-10-14 amendment to L2's block of "
           "`FRAMEWORK.md` §5 — so the digests recorded here are those of the files on disk, proved "
           "equal to their committed blobs: what the session was given, and not a re-render.")
REASON = ("A spent subject's pack is the record of what its session was given rather than an input "
          "to be kept current (Ruling 17(a); D-646). Left live it would re-render the charter member "
          "with an amendment ruled after the session ran, and so back-date into a completed "
          "derivation's record a text its session never read (#12); and L3's pack shares the charter "
          "member with it (`CHARTER_MEMBER_7`), so it must be frozen before L3's is built (the "
          "boot-list record's Ruling 1, noted). Frozen at the blobs it carries, with the hash STOP.")
f = dbp.FROZEN["l2"]
for name, got, want in (("finding", f["finding"], FINDING), ("reason", f["reason"], REASON),
                        ("date", f["date"], "2026-10-15")):
    print(f"FROZEN['l2'][{name!r}] equals the dispatch's text:", "PASS" if got == want else "FAIL")
    ok &= got == want
print("l2 not in RENDERED_BEFORE_THE_SCOPING_RULINGS:",
      "PASS" if "l2" not in dbp.RENDERED_BEFORE_THE_SCOPING_RULINGS else "FAIL")
ok &= "l2" not in dbp.RENDERED_BEFORE_THE_SCOPING_RULINGS

print("=== 1. against the committed manifest (the governing comparison)")
for s in ("harmony-boundary", "scoring-model", "l0-l1"):
    ok &= report(f"diff(C.subjects[{s!r}], B2.subjects[{s!r}])",
                 diff(C["subjects"][s], B2["subjects"][s]))
ok &= report("diff(T(C.subjects['l2']), B2.subjects['l2'])",
             diff(T(C["subjects"]["l2"]), B2["subjects"]["l2"]))

print("=== 2. against the repaired build before the freeze")
for s in ("harmony-boundary", "scoring-model", "l0-l1"):
    ok &= report(f"diff(B1.subjects[{s!r}], B2.subjects[{s!r}])",
                 diff(B1["subjects"][s], B2["subjects"][s]))
ok &= report("diff(T(B1.subjects['l2']), B2.subjects['l2'])",
             diff(T(B1["subjects"]["l2"]), B2["subjects"]["l2"]))
keys = set(B1) == set(B2)
print("top-level keys the same set (B1, B2):", "PASS" if keys else "FAIL")
ok &= keys
for k in sorted(set(B1) & set(B2)):
    if k == "subjects":
        continue
    eq = B1[k] == B2[k]
    print(f"top-level {k!r} equal (B1, B2):", "PASS" if eq else "FAIL")
    ok &= eq
print("RESULT:", "ALL EMPTY / PASS" if ok else "STOP")
sys.exit(0 if ok else 3)
```

`diag_t1g.py` — the diagnosis after the STOP, NOT ordered by the dispatch (§7 item 2):

```python
"""Diagnosis of Task 1(g)'s non-empty `l2` diff — NOT ordered by the dispatch; writes nothing.

Takes the entries of B2's `l2` LEAKS_IN_THE_EXTRAS list that are NOT in the committed manifest's
list (compared as whole entries), prints them, and then checks whether T(C.l2) equals B2.l2 once
exactly those entries are removed from B2 and its count reset — i.e. whether the movement is
precisely those insertions and nothing else.  Kept outside the repository working tree."""
import copy
import importlib.util
import json
import os
import sys

S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, S)
from diff_paths import diff, report  # noqa: E402

spec = importlib.util.spec_from_file_location(
    "dbp", r"C:\s\MS\tools\audit\gen_derivation_boot_pack.py")
dbp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dbp)

C = json.load(open(os.path.join(S, "C.json"), encoding="utf-8"))
B2 = json.load(open(os.path.join(S, "B2.json"), encoding="utf-8"))

tc = copy.deepcopy(C["subjects"]["l2"])
tc["★_FROZEN"] = dbp.frozen_block("l2")
dbp.frozen_from_disk("l2", tc)
b2 = copy.deepcopy(B2["subjects"]["l2"])

old = tc["LEAKS_IN_THE_EXTRAS"]["entries"]
new = b2["LEAKS_IN_THE_EXTRAS"]["entries"]
key = lambda e: json.dumps(e, sort_keys=True, ensure_ascii=False)  # noqa: E731
old_keys = [key(e) for e in old]
new_keys = [key(e) for e in new]
added = [e for e in new if key(e) not in old_keys]
removed = [e for e in old if key(e) not in new_keys]
print(f"entries: committed {len(old)}, today {len(new)}")
print(f"in today's list and not the committed one: {len(added)}")
for e in added:
    print("   ", json.dumps(e, ensure_ascii=False))
print(f"in the committed list and not today's: {len(removed)}")
for e in removed:
    print("   ", json.dumps(e, ensure_ascii=False))
rest_same_order = [k for k in new_keys if k in old_keys] == old_keys
print("the committed entries stand in today's list, in the same order:", rest_same_order)

b2["LEAKS_IN_THE_EXTRAS"]["entries"] = [e for e in new if key(e) in old_keys]
b2["counted"]["extras_lines_with_a_leak_hit"] = len(b2["LEAKS_IN_THE_EXTRAS"]["entries"])
report("diff(T(C.l2), B2.l2 with exactly those entries removed and its count reset)",
       diff(tc, b2))
```

`extract_member8_json.py` — NOT ordered in this form (§7 item 4): it wrote Task 3(d)'s JSON authority to the scratch
folder from the PINNED dispatch blob read through `git cat-file -p d17ee82b…`, before Task 1 ran; the file it wrote
(25,121 bytes; 17 in `order`, 5 `new`, 12 `carried`) was never used, Task 3 not being reached:

```python
"""Write Task 3(d)'s JSON object, byte for byte, from the PINNED dispatch blob read on stdin
(`git cat-file -p <blob> | python extract_member8_json.py <out>`).  The object is the one fenced
```json block of the dispatch, which opens directly under the words "The authority is this JSON
object" — located by that text, and required to be found exactly once.  Kept outside the
repository working tree."""
import json
import sys

raw = sys.stdin.buffer.read().decode("utf-8")
text = raw.replace("\r\n", "\n")
marker = "**The authority is this JSON object.**"
assert text.count(marker) == 1, "marker not found exactly once"
after = text[text.index(marker):]
assert after.count("```json\n") >= 1
start = after.index("```json\n") + len("```json\n")
end = after.index("\n```\n", start)
body = after[start:end] + "\n"
assert text.count("```json\n") == 1, f"```json fences in the dispatch: {text.count('```json')}"
obj = json.loads(body)
with open(sys.argv[1], "w", encoding="utf-8", newline="") as fh:
    fh.write(body)
print("written", sys.argv[1], len(body.encode("utf-8")), "bytes;",
      "order", len(obj["order"]), "new", len(obj["new"]), "carried", len(obj["carried"]))
```

`assemble_report.py` — fills this report's marked places with the run outputs and script texts above, verbatim
(§7 item 5):

```python
"""Fill the report skeleton's insertion places with the named scratch files, verbatim (trailing
newline stripped), in ONE pass over the skeleton — so text inserted is never itself re-scanned —
and write the report.  Every named file must exist, or nothing is written.  Kept outside the
repository working tree."""
import os
import re
import sys

S = os.path.dirname(os.path.abspath(__file__))
skel = open(os.path.join(S, "report_skeleton.md"), encoding="utf-8").read()
MARK = re.compile(r"<<INSERT:([^>]+)>>")
names = MARK.findall(skel)
bodies = {n: open(os.path.join(S, n), encoding="utf-8").read().rstrip("\n") for n in names}
out = MARK.sub(lambda m: bodies[m.group(1)], skel)
with open(sys.argv[1], "w", encoding="utf-8", newline="\n") as fh:
    fh.write(out)
print("filled", len(names), "places; wrote", sys.argv[1], len(out.encode("utf-8")), "bytes")
```

## 7. Declared departures

1. **The dispatch was read from the working tree before it was pinned** — standing clause P-2's fallback route, the
   user's opening line naming only the file. Pinned at Task 0 (`git hash-object -w`); the blob proven unmoved before
   staging.
2. **One unordered diagnosis script was run after the STOP** (`diag_t1g.py`, §6) to establish the shape of the
   movement before restoring — it imports the edited generator, writes nothing into the repository, and its result is
   the measurement in the head section. D-669: a cause is established before the mechanism is touched; no fix followed.
3. **The comparison scripts were run with `PYTHONIOENCODING=utf-8`** after the first run of `cmp_t1e.py` stopped on the
   console's code page at a `★`. Nothing was written by the failed run except its own scratch output.
4. **Task 3(d)'s JSON authority was written to the scratch folder before Task 1 ran**, extracted from the pinned blob by
   script rather than retyped (byte for byte, as Task 3(d) orders). It was never used.
5. **This report was assembled by a scratch script** that replaced marked places with the run outputs and script texts
   verbatim, so that no output was hand-transcribed (#17f).
6. **`STATUS.md` carries no entry for Task 1**: its work committed nothing and is stated in the close entry, on the first
   half's precedent for its own stopped Task 1.
7. **Each commit message carries one trailer line after the ordered subject** — the co-author attribution this session's
   instructions require — as a second paragraph; the subject lines are exactly the ordered ones.
8. **`git hash-object` was run on working-tree files** — the dispatch, for P-2; `claude_md_finer_archive.json`, for A1;
   and the ten `l2` pack files, as Task 1(a)–(b) orders.
9. **Task 5's ordered `STATUS.md` wording and away-returns heading are written for the stopped case**, which the dispatch
   provides for (*"or, if a task stopped, which task stopped and that nothing after it was done"*).

## 8. Observations, recorded and not acted on

1. **The two new leak lines sit in the SHARED charter member.** `EXTRAS["l3"]` is ordered to carry the same
   `CHARTER_MEMBER_7`, so whatever L3's leak scan finds in member (7) is computed against L3's own withheld strings, not
   L2's; whether those two lines are hits for L3 was not measured, Task 4 not being reached.
2. **The derivation's own sentence predicted this exact path**, and the dispatch's STOP caught it before anything was
   committed; the committed manifest's `l2` record therefore still describes L2's live pack as rendered on 2026-09-27.
3. **`VERDICTS["l3"]`'s opening comment** says `WITHHELD` carries no `l3` entry and nothing reads that table today; that
   is still true at this batch's end.

## 9. What this batch did not do

No `FROZEN` entry for `l2`, no `RENDERED_BEFORE_THE_SCOPING_RULINGS` table, no `VERDICT_DATE["l3"]`, no criterion-bullet
edit, no `WITHHELD["l3"]`, `EXTRAS["l3"]` or `L3_WITHHELD_DOCUMENTS` — the generator is byte-unchanged at the end; no
manifest regenerated; no pack rendered and no pack directory written; no list for the user assembled; no session booted;
no brief written; no score copied, staged or written; no edit to any ruling record, the cut list, any extract or either
input-contract copy; no ruling taken and no question or recommendation put to the user; no open-items row created,
flipped or discarded; no decisions-register entry and no `D-NNN`; nothing in the suspension file; no `src/` file, build,
test, golden, corpus of scores, or anything under `tools/corpus/` or `tools/robust_stop/`; no measurement of the
analysis; no governing document edited except `STATUS.md` and `STATUS_ARCHIVE.md`.

## 10. The plan's tell, in one sentence

**Did this batch produce anything other than the landed paths, the repair, the freeze, the three Task 2 edits, the `l3`
entries of `WITHHELD` and `EXTRAS` with `L3_WITHHELD_DOCUMENTS` and the four ruling strings, the rendered `l3` directory,
the manifest, the Task 5 files and the report?** **Yes, by absence and by addition:** the repair and the freeze were made
and then restored, so neither is produced; nothing of Tasks 2 to 4 is produced; Task 0 carries the regenerated
`tools/audit/evidence_pin_membership.json`, as its act (2) orders; the end-state commit carries the artifacts A2's
classing regenerates beside `tools/audit/guard_state.json`; and three scripts the dispatch does not order in that form
were run outside the repository (§7 items 2, 4 and 5). Nothing else.

## 11. The standing self-check (D-434) over this batch's own work

1. *Principles touched.* **#13/#3** — the named risk was measured by the ordered comparison, and its firing was a STOP
   before anything was committed; the cause was established at the objects first (D-669), with no fix taken. **#12** —
   the record of what L2's session was given is untouched, the act that would have moved it having been stopped and
   reversed. **#15/#19** — every comparison is at the objects, both directions, against an explicit hash. **#17(f)/D-431**
   — no count restated outside the run outputs reproduced verbatim. Conforms.
2. *Conventions.* American English in this side's prose; no self-invented label; reserved words in their musical senses
   or qualified (*decisions-register*, *open-items*, *corpus of scores*; a pack *part* only as the generator's field).
3. *Figures and premises.* Every commit read from its own object and the ref files.
4. *File-tools rule.* Repository content read with the file tools, save the git object queries, the sanctioned scripts and
   the declared items of §7.
5. *Uncertainty.* No check rests on a sample; each is a whole-object comparison or a full run.

*Provenance: CC, 2026-10-16, at boot tip `a01e9402fbaf034fe0d357214b67c06a8294309c`, under
`cc_instruction_l3_pack_build_second_half_2026_10_16.md`, after its ordered first reads — the freeze-derivation and
confirmation records and the cut list whole; `CLAUDE.md` at its session-start spans; `STATUS.md` and `DECISIONS.md` whole;
the gating answer located; handoff entries 410 to 413 whole; the dispatch-protocol section of `cowork_audit_protocol.md`
at its standing clauses and P-2; the first half's dispatch at its Tasks 0 to 2, its report whole and its close section
whole (read before this report was written, not at boot); the boot-list and
first-pass extracts records whole; the generator at its docstring, `VERDICT_DATE`, `FROZEN`, `CHARTER_MEMBER_7`,
`LEDGER_MEMBER_9`, `EXTRAS` at its head and its `l2` tail, `WITHHELD`, `filter_part`, `_removal_spans`, `_cut_spans`,
`render_extra`, `criterion_block`, `cross_reference_additions`, `build_subject`, `build()`, `frozen_block`,
`frozen_from_disk`, `write_all`, `check_all` and `main`; `tools/audit/l3_withheld_documents.json` whole; and
`gen_status_batch_bound.py` at the tip's object, at its docstring, its last aimings and its five authored inputs. **Not
read:** the twelve carried `l2` parts' filter entries, Task 3 not being reached; the first half's dispatch at its Tasks 3
to 5.*

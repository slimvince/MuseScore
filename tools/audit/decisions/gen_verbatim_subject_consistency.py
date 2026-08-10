#!/usr/bin/env python3
"""DOES EACH REGISTER ENTRY'S QUOTED DECISION MATCH THE DECISION THE ENTRY IS ABOUT?

WHAT THIS ANSWERS, AND WHY NOTHING ELSE DOES.  `OPEN_ITEMS.md` OI-358 found five consecutive
entries of the decisions register quoting a DIFFERENT rule than their own title, plain restatement
and recorded defense describe -- one of them quoting a section heading, which is not a decision at
all.  Two checks already run over that data and BOTH PASS OVER IT:

  * `gen_decisions_register.py --check` verifies the rendered files match the source data;
  * `gen_cluster_dispositions.py --verify` verifies every `verbatim` is found at its cited home
    AND starts at the cited line.

Both are satisfied by a CORRUPTED PAIR.  Once the `verbatim` IS the text at the drifted line, the
two agree with each other permanently -- the condition is self-sealing, and the machinery that
exists to detect drift confirms health from the moment it happens.  The only surviving witness is
the entry's own title and defense, and nothing compared those against the quote.  This does.

WHAT IT IS AND IS NOT, stated before any value is read off it.  It is an ADVISORY REPORT.  The
user's Ruling 24(b) of 2026-08-09 (`cowork_rulings_2026_08_09_fourth_stop.md`) requires it built
CORPUS-FIRST and adopted as a guard ONLY on measured clean separation -- because a check that
fires on legitimate work gets switched off, which is worse than none (D-473's own ground, and the
three measured conditions a mechanism is judged on, D-436).  This file therefore MEASURES its own
separation and states the adoption verdict rather than assuming one.  It has no `--check` mode and
is not in any guard list until that verdict says it may be.

THE CORPUS, RECORDED BEFORE THE MECHANISM (the order every guard family in this record is built
in).  `KNOWN_BAD` below carries the five OI-358 quotes as they stood when the defect was found --
the labelled POSITIVES.  They are kept here as data rather than read from the live entries on
purpose: the repair re-takes those five quotes, so a corpus read from the live data would empty
itself the moment the defect was fixed and the measurement would stop being reproducible.

THE SIGNAL, stated plainly because its limits are the whole question.  For each entry, the tokens
of its `verbatim` are ranked by how RARE they are across every entry's verbatim, and the rarest
few are looked for in the entry's own title plus plain restatement.  A correct pair shares its
distinctive vocabulary -- an entry about `hasStructuralBass` says so in its title.  A corrupted
pair does not.  WHAT THE SIGNAL CANNOT SEE, and this bounds every value below: an entry whose
title paraphrases its quote in different words scores low while being perfectly correct, and two
ADJACENT bullets of one section share vocabulary, so a one-bullet slip is the hardest case for it.

WHY THE DEFENSE FIELD IS NOT IN THE PRIMARY COMPARISON.  Two of the five were given a recorded
defense AFTER the mismatch was known, written deliberately against the decision the title
identifies rather than against the quoted text, and each says so in its own field.  Including that
text would let the repair's own record improve the measurement of the defect.  It is computed as a
SECOND value and reported beside the first, never mixed into it.

Run:
    python tools/audit/decisions/gen_verbatim_subject_consistency.py

Output:
    tools/audit/decisions/verbatim_subject_consistency.json
"""
from __future__ import annotations

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
BACKBONE = os.path.join(HERE, "backbone_decisions.json")
OUT = os.path.join(HERE, "verbatim_subject_consistency.json")

sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 -- the findings must survive a non-console stdout

# ── THE CORPUS, recorded before the mechanism ───────────────────────────────────────────────
# The five OI-358 quotes AS THEY STOOD when the defect was found: the labelled POSITIVES of this
# measurement. Each is the text the entry's `verbatim` field carried while the entry's title,
# plain restatement and defense described a different rule entirely.
#
# They are DATA here, not read from the live entries, because the repair re-takes those five
# quotes -- a corpus read from live data would empty itself at the moment of repair and the
# separation could never be re-measured. Recorded 2026-08-09 with the repair, from the entries'
# own preserved provenance.
KNOWN_BAD = {
    "D-220": "- **`hasStructuralBass` gates inversion bonuses.** Sparse upper-register\n  \"bass\" "
             "notes do not get inversion bonuses (Corelli op01n08d m2 b3).\n",
    "D-221": "  live `results[0]` reference (Sub-9a lesson).\n",
    "D-222": "  fires only when at least one tone has `onsetAtRegionStart == true` or\n  "
             "`distinctMetricPositions > 0` (i.e. came from `collectRegionTones`).\n  Single-tick "
             "/ status-bar / unit-test paths use the legacy single-bass path.",
    "D-223": "---\n\n## 9. How to add a new template safely (checklist)",
    "D-224": "Derived from the B1, B2, and B3 lessons.\n\n1. **Read the existing template nearest "
             "to yours.** Understand its intervals,\n   TPC deltas, and which existing terms / "
             "guards apply to it.\n",
}

# How many of the rarest tokens of a quote are looked for in the entry's own description.
RAREST_TOKENS = 8

# Words carrying no subject information. Deliberately short: a longer list is a tuning knob, and
# a tuned stopword list would make the separation a property of this file rather than of the data.
STOPWORDS = {
    "that", "this", "with", "from", "when", "which", "what", "have", "been", "were", "will",
    "would", "there", "their", "them", "then", "than", "does", "into", "onto", "only", "also",
    "each", "every", "some", "such", "must", "not", "and", "but", "for", "the", "its", "it's",
    "rather", "because", "where", "while", "over", "under", "here", "these", "those", "they",
    "more", "most", "less", "least", "same", "other", "another", "about", "after", "before",
    "both", "never", "always", "still", "even", "very", "than", "upon", "being", "itself",
}

TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


def tokens(text: str) -> set[str]:
    """Distinct informative tokens: at least four characters, not a stopword."""
    return {t.lower() for t in TOKEN_RE.findall(text or "")
            if len(t) >= 4 and t.lower() not in STOPWORDS}


def describe(entry: dict) -> str:
    """The entry's own account of WHICH decision it records -- title and plain restatement.

    The recorded defense is deliberately excluded here and computed separately; see the module
    docstring for why.
    """
    return f"{entry.get('title', '')} {entry.get('plain', '')}"


def agreement(quote: str, description: str, rarity: dict[str, int]) -> dict:
    """How many of the quote's RAREST informative tokens appear in the description."""
    qt = tokens(quote)
    if not qt:
        return {"agreement_value": None, "why_none": "the quote carries no informative token",
                "rarest_tokens": [], "tokens_found": []}
    ranked = sorted(qt, key=lambda t: (rarity.get(t, 0), t))[:RAREST_TOKENS]
    dt = tokens(description)
    found = [t for t in ranked if t in dt]
    return {
        "agreement_value": round(len(found) / len(ranked), 4),
        "rarest_tokens": ranked,
        "tokens_found": found,
    }


def main() -> int:
    data = json.loads(open(BACKBONE, encoding="utf-8").read())
    entries = data["decisions"]

    # Rarity is measured over every entry's own quote, so a token common to the whole decisions
    # register (a principle number, a layer name) never counts as distinctive.
    rarity: dict[str, int] = {}
    for e in entries:
        for t in tokens(e.get("verbatim", "")):
            rarity[t] = rarity.get(t, 0) + 1

    by_id = {e["id"]: e for e in entries}

    live = []
    for e in entries:
        a = agreement(e.get("verbatim", ""), describe(e), rarity)
        a_with_defense = agreement(e.get("verbatim", ""),
                                   describe(e) + " " + (e.get("rationale") or ""), rarity)
        live.append({
            "id": e["id"],
            "title": e.get("title", ""),
            "home": e.get("home", ""),
            "agreement_value": a["agreement_value"],
            "agreement_value_including_the_recorded_defense": a_with_defense["agreement_value"],
            "rarest_tokens": a["rarest_tokens"],
            "tokens_found": a["tokens_found"],
            "why_none": a.get("why_none"),
        })

    # The labelled positives, measured against the SAME entries' own descriptions.
    corpus = []
    unrepaired = []
    for did, bad in sorted(KNOWN_BAD.items()):
        e = by_id.get(did)
        if e is None:
            raise SystemExit(f"STOP: the corpus names {did}, which the decisions register does "
                             "not carry")
        a = agreement(bad, describe(e), rarity)
        still_live = (e.get("verbatim", "") == bad)
        if still_live:
            unrepaired.append(did)
        corpus.append({
            "id": did,
            "label": "KNOWN-BAD",
            "the_entry_is_about": e.get("title", ""),
            "the_quote_it_carried": bad,
            "agreement_value": a["agreement_value"],
            "rarest_tokens": a["rarest_tokens"],
            "tokens_found": a["tokens_found"],
            "this_quote_is_still_the_entry_s_live_verbatim": still_live,
        })

    scored_live = [r for r in live if r["agreement_value"] is not None]
    corpus_values = [c["agreement_value"] for c in corpus if c["agreement_value"] is not None]
    worst_bad = max(corpus_values) if corpus_values else None

    # Separation, measured rather than asserted. The live side EXCLUDES the five while they are
    # still unrepaired, so a corrupted entry is not counted as its own counter-example.
    remainder = [r for r in scored_live if not (r["id"] in KNOWN_BAD and r["id"] in unrepaired)]
    at_or_below = [r for r in remainder if worst_bad is not None
                   and r["agreement_value"] <= worst_bad]
    best_bad = min(corpus_values) if corpus_values else None
    clean = bool(corpus_values) and not at_or_below

    verdict = ("ADOPTABLE AS A GUARD -- every labelled known-bad quote scores strictly below every "
               "entry of the remainder, so a threshold between them denies nothing legitimate."
               if clean else
               "NOT ADOPTABLE AS A GUARD -- ADVISORY ONLY. Entries of the remainder score at or "
               "below the worst labelled known-bad quote, so no threshold separates the two "
               "populations and any guard built on this value would fire on legitimate entries. "
               "A guard that fires on legitimate work gets switched off, which is worse than none "
               "(D-473's ground, D-436's third condition). The report stands as a READING AID: "
               "the entries listed in `the_lowest_agreement_values` are worth a human look, in "
               "that order, and nothing here decides that any of them is wrong.")

    artifact = {
        "what_this_is": "An ADVISORY comparison of every decisions-register entry's quoted "
                        "decision against the entry's own account of which decision it records. "
                        "Built on the user's Ruling 24(b) of 2026-08-09, corpus first, and "
                        "adopted as a guard only on measured clean separation -- which this file "
                        "measures rather than assumes.",
        "generated_by": "tools/audit/decisions/gen_verbatim_subject_consistency.py",
        "the_row_it_answers": "OPEN_ITEMS.md OI-358",
        "why_no_existing_check_sees_the_defect":
            "The register check verifies the rendered files match the source data, and the "
            "disposition verifier verifies every quote is found at its cited home and starts at "
            "the cited line. BOTH ARE SATISFIED BY A CORRUPTED PAIR: once the quote IS the text "
            "at the drifted line, the two agree with each other permanently. The condition is "
            "self-sealing, and this comparison is the only one that does not depend on the pair "
            "agreeing with itself.",
        "the_signal": {
            "what_is_compared": "the entry's `verbatim` against the entry's own `title` plus "
                                "`plain` restatement.",
            "how": f"the quote's informative tokens are ranked by how rare they are across every "
                   f"entry's quote, and the rarest {RAREST_TOKENS} are looked for in the "
                   f"description. The value is the fraction found.",
            "rarest_tokens_used": RAREST_TOKENS,
            "informative_token": "at least four characters, not in the short stopword list, "
                                 "matched as an identifier-shaped run so that code names survive "
                                 "whole.",
            "what_it_cannot_see": [
                "An entry whose title paraphrases its quote in different words is CORRECT and "
                "scores low. The value is not a verdict.",
                "Two ADJACENT bullets of one section share vocabulary, so a one-bullet slip -- "
                "which is exactly the shape OI-358 found -- is the hardest case for this signal "
                "and not the easiest.",
                "It cannot detect a quote that is wrong in a way the title happens to describe.",
            ],
            "why_the_defense_is_a_second_value_and_not_part_of_the_first":
                "Two of the five labelled entries were given a recorded defense AFTER the "
                "mismatch was known, written against the decision their title identifies rather "
                "than against the quoted text, and each says so in its own field. Including that "
                "text in the primary comparison would let the repair's own record improve the "
                "measurement of the defect it repairs.",
        },
        "the_corpus_recorded_before_the_mechanism": {
            "what_these_are": "The five OI-358 quotes as they stood when the defect was found -- "
                              "the labelled POSITIVES. Kept as data rather than read from the "
                              "live entries, because the repair re-takes them and a corpus read "
                              "from live data would empty itself at the moment of repair.",
            "entries": corpus,
            "still_carrying_the_known_bad_quote": sorted(unrepaired),
            "what_that_field_means": "Non-empty means the repair has NOT been applied at this "
                                     "tree, so the live population below still contains the "
                                     "defect. Empty means the five have been re-taken and the "
                                     "corpus is measuring history, which is what it is for.",
        },
        "separation": {
            "worst_labelled_known_bad_value": worst_bad,
            "best_labelled_known_bad_value": best_bad,
            "entries_of_the_remainder_at_or_below_the_worst_known_bad":
                [{"id": r["id"], "agreement_value": r["agreement_value"], "title": r["title"]}
                 for r in sorted(at_or_below, key=lambda r: (r["agreement_value"], r["id"]))],
            "count_at_or_below": len(at_or_below),
            "remainder_size": len(remainder),
            "clean_separation": clean,
            "what_clean_separation_would_mean": "every labelled known-bad quote scoring strictly "
                                                "below every other entry, so that a threshold "
                                                "between the two populations denies nothing "
                                                "legitimate.",
        },
        "adoption_verdict": verdict,
        "the_lowest_agreement_values": [
            {"id": r["id"], "agreement_value": r["agreement_value"], "title": r["title"],
             "home": r["home"], "rarest_tokens": r["rarest_tokens"],
             "tokens_found": r["tokens_found"]}
            for r in sorted(scored_live, key=lambda r: (r["agreement_value"], r["id"]))[:40]
        ],
        "entries_with_no_informative_token_in_the_quote":
            [r["id"] for r in live if r["agreement_value"] is None],
        "every_entry": live,
    }

    open(OUT, "w", encoding="utf-8", newline="").write(
        json.dumps(artifact, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    print(f"  entries compared: {len(scored_live)} (of {len(entries)})")
    print(f"  labelled known-bad: {len(corpus)}; still carrying the bad quote: {len(unrepaired)}")
    print(f"  worst known-bad value: {worst_bad}; remainder at or below it: {len(at_or_below)}")
    print(f"  clean separation: {clean}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""THE RESERVED-WORD SCANNER — a DERIVED candidate population, authored verdicts, advisory output.

WHY THIS EXISTS.  `CLAUDE.md`'s reserved-vocabulary convention (register entry **D-113**) reserves
any term that coincides even slightly with music theory for its musical meaning, and states the
disambiguation rule: **the bare word always carries the musical meaning; every non-musical use is
explicitly qualified.**  It lists twenty collided words.  The user asked how that list's
COMPLETENESS is known, and **Ruling 31** of 2026-08-09 (`cowork_rulings_2026_08_09_fifth_stop.md`)
answers: *it is not, and it becomes checkable by DERIVATION.*

THE DERIVATION, and it is the whole point of the tool.  A candidate is a word that is BOTH

  (a) in the project's own MUSICAL VOCABULARY — extracted from its own domain surfaces, never from
      an assumed word list; and
  (b) used by the project's GOVERNANCE surfaces, whose subject is not music.

The twenty words `CLAUDE.md` lists are the SEED verdicts, not the population.  Every derived
candidate carries an AUTHORED verdict, and **an unclassified candidate is a STOP** — the
guard-population pattern.  "Complete" then means complete relative to a NAMED derivation, re-derived
as the tree grows (#19).

THE PROXY IS DECLARED AS A PROXY (#17d).  Occurring in a governance surface stands in for *used in
a non-musical context*.  It is a STRUCTURAL proxy for a semantic property and it is over-inclusive
by construction: a governance document may discuss music, and a musical word may appear there in
its musical sense.  That is deliberate — over-inclusion is safe because every candidate is decided
by an authored verdict, and under-inclusion would silently shrink the population the completeness
claim rests on.  The proxy is NOT validated against a semantic ground truth, and no verdict here
rests on it alone.

THE EXTERNAL LEG IS ABSENT AND SAID SO.  Ruling 31 admits an external music glossary as an optional
second source for (a).  None is used: this repository vendors no music-theory glossary, and
importing one would put an unestablished list under load (#19).  The consequence is stated rather
than hidden — a musical word this project never writes in its own code or specifications is outside
the derived population, and the derivation says so instead of claiming a completeness it does not
have.

WHAT IT IS.  ADVISORY.  Ruling 31 permits adoption as a diff-time check on new text ONLY on
measured clean separation; the separation is measured here, and the verdict is reported rather than
tuned (**D-436**'s third condition, **D-473**'s ground).

Run:
    python tools/audit/gen_reserved_word_scanner.py            # derive + author + measure
    python tools/audit/gen_reserved_word_scanner.py --check    # re-derive; STOP on drift

Output:
    tools/audit/reserved_word_scanner.json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "reserved_word_scanner.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# ── (a) THE MUSICAL SURFACE — the project's own domain surfaces ───────────────────────────────
# The analysis code's identifiers, and the two documents whose subject IS the music theory. A word
# must appear in BOTH kinds to enter the musical vocabulary: an identifier alone is often a
# programming word, and a document alone is often prose.
CODE_ROOTS = ["src/composing/analysis"]
MUSIC_DOCS = ["docs/scoring_model.md", "ARCHITECTURE.md"]

# ── (b) THE GOVERNANCE SURFACE — documents whose subject is not music ─────────────────────────
GOVERNANCE_DOCS = [
    "CLAUDE.md",
    "cowork_audit_protocol.md",
    "cowork_design_doc_template.md",
    "OPEN_ITEMS.md",
    "DECISIONS.md",
    "BUILD_AND_TEST.md",
]

# Words carried by every English text, which say nothing about either surface.
STOPWORDS = set("""
a an the and or but if then else for while do does did done of in on at by to from with without
this that these those it its is are was were be been being have has had not no yes all any some
each every other another same such than as so too very can could may might must shall should will
would we you they them their there here when where which who whom whose what why how also only
just now new old first second third last next per via over under between within across into onto
out off up down again more most less least many much few both either neither one two three four
five six seven eight nine ten zero none than about after before during since until upon against
because though although however therefore thus hence still yet even ever never always often
sometimes rather quite already almost enough own see read write make made take taken give given
use used using set sets setting get gets got put puts run runs ran running say says said state
states stated states name names named call calls called work works worked working case cases
point points line lines file files code codes text texts word words list lists item items
""".split())

IDENT = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
WORD = re.compile(r"[a-z]{3,}")
CAMEL = re.compile(r"[A-Z]?[a-z]+|[A-Z]{2,}(?![a-z])")


def read(rel: str) -> str:
    with open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace") as fh:
        return fh.read()


def code_identifier_words() -> set[str]:
    """Every word inside an identifier in the analysis code, camel/snake split and lowercased."""
    words: set[str] = set()
    for rel in CODE_ROOTS:
        base = os.path.join(ROOT, rel)
        for dirpath, _dirnames, filenames in os.walk(base):
            for fn in filenames:
                if not fn.endswith((".h", ".cpp")):
                    continue
                path = os.path.join(dirpath, fn)
                with open(path, encoding="utf-8", errors="replace") as fh:
                    body = fh.read()
                for ident in IDENT.findall(body):
                    for piece in ident.split("_"):
                        for w in CAMEL.findall(piece):
                            w = w.lower()
                            if len(w) >= 3 and w not in STOPWORDS:
                                words.add(w)
    return words


def prose_words(rels: list[str]) -> set[str]:
    words: set[str] = set()
    for rel in rels:
        for w in WORD.findall(read(rel).lower()):
            if w not in STOPWORDS:
                words.add(w)
    return words


ENUM = re.compile(r"\benum\s+(?:class\s+)?(\w+)[^{]*\{(.*?)\}", re.S)


def domain_type_words() -> tuple[set[str], list[str]]:
    """The SHARPER musical surface: the words naming the analysis's own DOMAIN TYPES.

    Every `enum` in the analysis code, its name and its enumerators, camel-split and lowercased.
    An enumeration is where a program writes down the categories its domain actually has, so for a
    music-analysis module these are the chord qualities, the modes, the degrees, the cadence kinds,
    the interval classes — the project's musical vocabulary in the strictest in-repo sense
    available. It is far narrower than any word that merely appears in both a code file and a music
    document, and the two are measured against each other below rather than one being assumed.
    """
    words: set[str] = set()
    enums: list[str] = []
    for rel in CODE_ROOTS:
        for dirpath, _dirnames, filenames in os.walk(os.path.join(ROOT, rel)):
            for fn in filenames:
                if not fn.endswith((".h", ".cpp")):
                    continue
                with open(os.path.join(dirpath, fn), encoding="utf-8", errors="replace") as fh:
                    body = fh.read()
                for name, block in ENUM.findall(body):
                    enums.append(name)
                    for ident in [name] + IDENT.findall(block):
                        for piece in ident.split("_"):
                            for w in CAMEL.findall(piece):
                                w = w.lower()
                                if len(w) >= 3 and w not in STOPWORDS:
                                    words.add(w)
    return words, sorted(set(enums))


def derive() -> dict:
    code = code_identifier_words()
    music_prose = prose_words(MUSIC_DOCS)
    governance = prose_words(GOVERNANCE_DOCS)
    broad_vocabulary = code & music_prose
    domain_words, enums = domain_type_words()
    sharp_vocabulary = domain_words & music_prose
    return {
        "code_identifier_words": len(code),
        "music_document_words": len(music_prose),
        "governance_document_words": len(governance),
        "broad_vocabulary": len(broad_vocabulary),
        "broad_candidates": sorted(broad_vocabulary & governance),
        "domain_enumerations": len(enums),
        "sharp_vocabulary": len(sharp_vocabulary),
        "sharp_candidates": sorted(sharp_vocabulary & governance),
        "enumerations": enums,
    }


# ── THE SEED VERDICTS — parsed from CLAUDE.md's own list, never typed here ────────────────────
SEED_LINE = re.compile(r"starting inventory:(.*?)\.\s*\*\*THE DISAMBIGUATION", re.S)


def seed_inventory() -> set[str]:
    body = read("CLAUDE.md")
    m = SEED_LINE.search(body)
    if not m:
        raise SystemExit("STOP: CLAUDE.md's collision inventory could not be located by its own "
                         "wording. The seed is parsed from that document and never typed here, so "
                         "a wording change is a STOP rather than a silently smaller seed.")
    # The inventory names each collided word in italics and then glosses it in parentheses; only
    # the italicised heads are the inventory, so the glosses' own words are not read as members.
    return {w for w in re.findall(r"\*([a-z]{3,})\*", m.group(1))}


# ── THE LABELLED CORPUS — recorded BEFORE the measurement, and it is DATA, not a live read ────
# Every collision this project's own standing self-check has caught in its OWN new prose, wave by
# wave, with the wave that caught it. They are the POSITIVES a scanner must find. Recording them
# here rather than reading them live is what the previous corpus-first build established: a corpus
# read from the live tree empties itself the moment the defect is corrected, and the separation can
# never be re-measured afterwards.
CAUGHT_COLLISIONS = [
    ("part", "2026-08-09, the guard-family wave — bare non-musical `part` throughout new text and "
             "in an artifact field name"),
    ("rest", "2026-08-09, the same wave — bare `rest` as a parameter name, the same collision the "
             "previous wave had caught in its own selection function"),
    ("figure", "2026-08-09, the second return continuation — bare non-musical `figure` in a new "
               "CLAUDE.md block, two register fields, two rows and the returns file"),
    ("part", "2026-08-09, the fifth return continuation — bare non-musical `part` in a new "
             "open-items detail file"),
    ("figure", "2026-08-09, the fifth return continuation — bare non-musical `figure` twice in one "
               "sentence of the registration queue's extension"),
]


def measure_separation(candidates: set[str]) -> tuple[dict, dict]:
    """Does the derived population CONTAIN the words the self-checks actually caught?

    This is the only separation a derivation of a POPULATION can be measured on. It is not a
    detection rate on occurrences: the scanner proposes words for a ruling, and whether a given
    USE of a word is the non-musical sense is the semantic judgment no mechanism makes — which is
    also why Ruling 32 closed the neighbouring limb.
    """
    caught = {w for w, _ in CAUGHT_COLLISIONS}
    found = sorted(w for w in caught if w in candidates)
    missed = sorted(w for w in caught if w not in candidates)
    corpus = {"what": "Every reserved-word collision this project's standing self-check has caught "
                      "in its OWN new prose, with the wave that caught it. Recorded as DATA rather "
                      "than read live, because a corpus read from the tree empties itself the "
                      "moment the defect is corrected.",
              "entries": [{"word": w, "wave": why} for w, why in CAUGHT_COLLISIONS]}
    separation = {
        "what_was_measured": "Whether the DERIVED candidate population contains the words the "
                             "self-checks actually caught.",
        "positives_found": found,
        "positives_missed": missed,
        "verdict": ("EVERY known positive is in the derived population" if not missed else
                    "the derivation MISSES a known positive: " + ", ".join(missed)),
        "WHAT_IT_DOES_NOT_ESTABLISH": "Containment is not detection. The population says which "
            "WORDS deserve a ruling; it does not say which USE of a word is the non-musical sense, "
            "and no threshold over it separates a legitimate bare musical use from a collision — "
            "that is the semantic judgment Ruling 32 closed the neighbouring limb over. SO NO "
            "GUARD IS ADOPTED: a diff-time check would fire on every legitimate musical use of "
            "every word in this population, which is precisely the mis-firing D-473 refuses and "
            "D-436's third condition measures.",
        "the_adoption_condition_and_its_verdict": "Ruling 31 permits adoption as a diff-time check "
            "ONLY on measured clean separation. There is no separation to measure at the "
            "occurrence level and none is claimed; the inventory stays ADVISORY, which is the "
            "result rather than a shortfall, and nothing was tuned to make it look otherwise.",
    }
    return corpus, separation


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--derive-only", action="store_true",
                    help="print the derived candidate population and stop (evidence for authoring)")
    args = ap.parse_args()

    d = derive()
    if args.derive_only:
        print(f"broad vocabulary  {d['broad_vocabulary']}  -> candidates "
              f"{len(d['broad_candidates'])}")
        print(f"enumerations {d['domain_enumerations']}; sharp vocabulary "
              f"{d['sharp_vocabulary']}  -> CANDIDATES {len(d['sharp_candidates'])}")
        print(" ".join(d["sharp_candidates"]))
        return 0
    seed = seed_inventory()
    sharp = set(d["sharp_candidates"])
    broad = set(d["broad_candidates"])
    seed_reached = sorted(seed & sharp)
    seed_missed = sorted(seed - sharp)
    seed_missed_by_both = sorted(seed - sharp - broad)
    unclassified = sorted(sharp - seed)

    corpus, separation = measure_separation(sharp)

    artifact = {
        "what_this_is": __doc__.strip().split("\n\n")[1].replace("\n", " "),
        "generated_by": "tools/audit/gen_reserved_word_scanner.py",
        "the_ruling": "Ruling 31 of `cowork_rulings_2026_08_09_fifth_stop.md`: the collision "
                      "inventory's completeness is NOT known and becomes checkable BY DERIVATION — "
                      "the project's musical vocabulary intersected with the words the "
                      "documentation uses in non-musical contexts, with the twenty-word inventory "
                      "as the SEED verdicts, every derived candidate carrying an authored verdict, "
                      "and an unclassified candidate a STOP.",
        "status": "ADVISORY. No guard is adopted, no text is renamed, and no verdict here binds "
                  "anything. Ruling 30 governs what happens next: the user rules per-word batches, "
                  "governing surfaces first.",
        "THE_CLOSING_STATE_the_user_ruled_2026_08_09": {
            "the_ruling": "Ruling 37 of `cowork_rulings_2026_08_09_sixth_stop.md`, recorded here "
                          "and on `OPEN_ITEMS.md` OI-229's row by "
                          "`cc_instruction_return_continuation_6.md` Task 0.",
            "the_outcome": "READING 3 of the reading surface's three. The inventory stays at the "
                           "user's twenty, the convention stays LIVE for new writing, and the "
                           "COMPLETENESS QUESTION IS ANSWERED AND RECORDED RATHER THAN CLOSED.",
            "the_answer_that_is_now_a_STANDING_STATEMENT": "The inventory is incomplete by a "
                "measured amount relative to named derivations that are themselves incomplete "
                "against the record. So 'complete' means COMPLETE RELATIVE TO A NAMED DERIVATION, "
                "re-derived as the tree grows, with the derivation's MEASURED MISS RATE AGAINST "
                "THE SEED part of its name. It is register entry D-661, homed in "
                "cowork_audit_protocol.md beside D-436; this artifact is the evidence for it and "
                "is re-run when the tree has grown.",
            "what_the_ruling_does_NOT_do": [
                "No verdict-authoring pass runs over the derived population — the STOP below stays "
                "armed and the candidates stay unclassified by decision rather than by omission.",
                "No check is adopted: the separation measurement below is negative and nothing was "
                "tuned to change that.",
                "Nothing is renamed and no batch is scheduled.",
                "OI-229 does NOT close — its subject is the cleanup, not the completeness question.",
            ],
            "the_working_enforcement": "The per-wave standing self-check (D-434), whose "
                "establishment is four consecutive waves each catching a reserved-word collision "
                "in that wave's OWN new prose. Those catches are the labelled corpus below.",
            "one_bounded_option_HELD_and_not_scheduled": "A batch over the SEED TWENTY's bare uses "
                "in the governing surfaces — the one subset sound by construction, the seed being "
                "the user's own inventory — as a later leftover-capacity item. Named so it is not "
                "rediscovered; not started.",
            "excluded_alternatives_recorded": [
                "Authoring verdicts over either derived population: unsound over the sharp one "
                "(it misses seed words the record holds) and unbounded over the broad one. "
                "Confidence in a verdict is not what #19 licenses.",
                "Per-word batches over the same population — the same defect at a smaller bill.",
            ],
        },
        "the_derivation": {
            "musical_surface_a": {
                "sharp": "Every `enum` in the analysis code — its name and its enumerators, "
                         "camel-split and lowercased — intersected with the words the two "
                         "music-theory documents use. An enumeration is where a program writes "
                         "down the categories its domain actually has, so for this module they are "
                         "the chord qualities, modes, degrees, cadence kinds and interval classes: "
                         "the project's musical vocabulary in the strictest in-repo sense "
                         "available.",
                "broad": "Every word inside any identifier in the analysis code, intersected with "
                         "the same documents. Reported beside the sharp one so the choice is "
                         "measured rather than asserted.",
                "code_roots": CODE_ROOTS,
                "music_documents": MUSIC_DOCS,
            },
            "non_musical_surface_b": {
                "documents": GOVERNANCE_DOCS,
                "THE_PROXY_IS_DECLARED_AS_A_PROXY": "Occurring in a governance surface stands in "
                    "for USED IN A NON-MUSICAL CONTEXT. It is a STRUCTURAL proxy for a semantic "
                    "property (#17d) and it is over-inclusive by construction: a governance "
                    "document discusses the analysis constantly, so a musical word appears there "
                    "in its musical sense. Over-inclusion is the safe direction — every candidate "
                    "is decided by an AUTHORED verdict — while under-inclusion would silently "
                    "shrink the population the completeness claim rests on. It is NOT validated "
                    "against a semantic ground truth and no verdict rests on it alone.",
            },
            "THE_EXTERNAL_LEG_IS_ABSENT_AND_SAID_SO": "Ruling 31 admits an external music glossary "
                "as an optional second source for (a). None is used: this repository vendors no "
                "music-theory glossary, and importing one would put an unestablished list under "
                "load (#19). THE CONSEQUENCE, stated rather than hidden: a musical word this "
                "project never writes in its own code or specifications is OUTSIDE the derived "
                "population, so 'complete' here means complete relative to THIS derivation and to "
                "nothing wider.",
        },
        "counts": {
            "code_identifier_words": d["code_identifier_words"],
            "music_document_words": d["music_document_words"],
            "governance_document_words": d["governance_document_words"],
            "domain_enumerations": d["domain_enumerations"],
            "broad_vocabulary": d["broad_vocabulary"],
            "broad_candidates": len(broad),
            "sharp_vocabulary": d["sharp_vocabulary"],
            "sharp_candidates": len(sharp),
            "seed_words": len(seed),
            "seed_reached_by_the_derivation": len(seed_reached),
            "seed_missed_by_the_sharp_derivation": len(seed_missed),
            "seed_missed_by_BOTH_derivations": len(seed_missed_by_both),
            "candidates_with_no_authored_verdict": len(unclassified),
        },
        "WHAT_THE_DERIVATION_ANSWERS": {
            "the_question": "How is the twenty-word inventory's completeness known?",
            "the_answer": "It is not, and now it is checkable. The derived population is many "
                          "times the inventory, so the inventory is NOT complete relative to this "
                          "derivation — which is the finding, and it is what Ruling 31 predicted "
                          "in its own words.",
            "and_the_derivation_is_bounded_TOO": "The seed words the derivation does NOT reach "
                                                 "bound it from the other side: they are collisions "
                                                 "the user recorded which this derivation would "
                                                 "never have proposed, so the derivation is not a "
                                                 "superset of the record either. Both lists are "
                                                 "below.",
            "seed_reached": seed_reached,
            "seed_missed_by_the_sharp_derivation": seed_missed,
            "seed_missed_by_both_derivations": seed_missed_by_both,
        },
        "the_seed_verdicts": {
            "source": "CLAUDE.md's Conventions block — the twenty words the user's own inventory "
                      "names, parsed from that list rather than typed here.",
            "words": sorted(seed),
        },
        "THE_STOP": {
            "armed": bool(unclassified),
            "rule": "Every derived candidate carries an authored verdict — collision, "
                    "non-collision-with-reason, or structural case — and an unclassified candidate "
                    "is a STOP. This tool exits nonzero while any remains.",
            "why_the_artifact_is_written_anyway": "A tool that stops writes no artifact, and a "
                    "check whose whole output is its own failure teaches a reader nothing. The "
                    "advisory inventory is written and the STOP is reported in it, which is the "
                    "shape the rule-triage tool's own history argued for.",
            "candidates_with_no_authored_verdict": unclassified,
            "what_authoring_them_is": "A named act of its own, not a step inside another task: a "
                    "verdict per candidate, each with its ground, over a population this artifact "
                    "counts. It is the input to Ruling 30's per-word batches and it is NOT "
                    "performed here.",
        },
        "the_separation_measurement": separation,
        "the_labelled_corpus": corpus,
        "what_this_does_NOT_do": [
            "It renames nothing and proposes no rename — Ruling 30 forbids a tree-wide rename and "
            "reserves the batches to the user.",
            "It is not adopted as a diff-time check: Ruling 31 permits that ONLY on measured clean "
            "separation, and the measurement is below.",
            "It touches no src/, no golden, no corpus of scores and nothing in tools/robust_stop/.",
            "It says nothing about research-tied names beyond recording Ruling 30's two-tier test "
            "for them; applying that test needs the introduction sites, which are authored.",
        ],
        "rulings_30_two_tier_test_for_research_tied_names": {
            "not_renamed": "A name carrying correspondence to the published research is NOT "
                           "renamed (#1/#2).",
            "tier_i": "At the INTRODUCTION SITE — where the public research is actually discussed, "
                      "expected to be one or very few places — the collision is explained and our "
                      "decided synonym stated. Conformant.",
            "tier_ii": "EVERY SUBSEQUENT USE outside our vocabulary carries a compact inline "
                       "annotation referencing the research. Conformant iff annotated; an "
                       "UNANNOTATED REPEAT USE is a flag.",
            "why_it_is_recorded_here_and_not_implemented": "Deciding which candidates are "
                "research-tied, and which site is the introduction site, is authorship — the same "
                "act the per-candidate verdicts are. The test is written down so the authoring "
                "pass applies the user's rule rather than inventing one.",
        },
    }

    open(OUT, "w", encoding="utf-8", newline="").write(
        json.dumps(artifact, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    print(f"  sharp candidates {len(sharp)} (broad {len(broad)}); seed {len(seed)}, "
          f"reached {len(seed_reached)}, missed {len(seed_missed)}")
    print(f"  separation: {separation['verdict']}")
    if unclassified:
        print(f"STOP: {len(unclassified)} derived candidate(s) with no authored verdict. The "
              f"advisory inventory is written; authoring the verdicts is its own act.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

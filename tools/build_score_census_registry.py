#!/usr/bin/env python3
"""
build_score_census_registry.py — deterministic generator for
tools/score_census_registry.json (the census schema-v2 source registry).

WHY a new file (declared per CC corpus-wave-1 Task A): the existing
tools/corpus_registry.json is an append-only *validation-run* log and
tools/extra_scores_registry.json is a per-*score* list; neither carries the
census's per-*source* schema (gt_type / license_class / distribution / tier /
split / pinned_commit). Introducing tools/score_census_registry.json is cleaner
than overloading either.

Per-source schema (census §3 + CC dispatch):
  name, container, content, pieces, annotated_pieces, gt_type, gt_layers,
  annotation_standard, score_format, alignment, license_class, distribution,
  tier, status, split, provenance_url, pinned_commit, notes

DLC rows are generated live from the tools/dcml/ clones (sha via git rev-parse,
counts via glob, harmony_version + cadence/phrase layer counts from the TSVs) so
the registry never drifts from disk. Non-DLC rows are hand-encoded from the
census appendices (cowork_score_census_gt_draft.md) with shas read live where the
source is a local git clone.

Run:  python tools/build_score_census_registry.py  (writes the JSON next to it)
"""
from __future__ import annotations

import csv
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DCML = ROOT / "tools" / "dcml"
OUT = ROOT / "tools" / "score_census_registry.json"

NOT_DLC = {"bach_chorales", "when_in_rome"}

# Pre-wave1 DLC members (already in project use) — split=dev by history.
PREWAVE1 = {"ABC", "bach_en_fr_suites", "chopin_mazurkas", "corelli",
            "cpe_bach_keyboard", "dvorak_silhouettes", "grieg_lyric_pieces",
            "mozart_piano_sonatas", "schumann_kinderszenen", "tchaikovsky_seasons"}
# Newly onboarded DLC members designated dev (CC dispatch, 2026-07-02); all other
# newly onboarded members default to held-out.
NEW_DEV = {"beethoven_piano_sonatas", "wagner_overtures", "liszt_pelerinage",
           "rachmaninoff_piano", "schulhoff_suite_dansante_en_jazz",
           "monteverdi_madrigals"}
# DLC repos carrying an explicit CC BY-NC-SA 4.0 LICENSE file (verified per-repo);
# the rest have NO in-repo LICENSE -> license_class=unclear (org statement is
# CC BY-NC-SA [reported]).  All DLC are hash-pin-only regardless.
CC_LICENSED = {"ABC", "beethoven_piano_sonatas", "chopin_mazurkas", "corelli",
               "debussy_suite_bergamasque", "dvorak_silhouettes",
               "grieg_lyric_pieces", "liszt_pelerinage", "medtner_tales",
               "mozart_piano_sonatas", "schumann_kinderszenen", "tchaikovsky_seasons"}

DLC_CONTENT = {
    "ABC": "Beethoven, all 16 string quartets",
    "bach_en_fr_suites": "J.S. Bach English & French Suites",
    "bach_solo": "J.S. Bach solo works (cello/violin/flute)",
    "bartok_bagatelles": "Bartok, 14 Bagatelles op. 6",
    "beethoven_piano_sonatas": "Beethoven, piano sonatas",
    "c_schumann_lieder": "Clara Schumann, Lieder",
    "chopin_mazurkas": "Chopin, mazurkas",
    "corelli": "Corelli, trio sonatas",
    "couperin_clavecin": "Couperin, L'art de toucher le clavecin",
    "couperin_concerts": "Couperin, Concerts Royaux",
    "cpe_bach_keyboard": "C.P.E. Bach, keyboard works",
    "debussy_suite_bergamasque": "Debussy, Suite bergamasque",
    "dvorak_silhouettes": "Dvorak, Silhouettes op. 8",
    "frescobaldi_fiori_musicali": "Frescobaldi, Fiori Musicali (1635) — modal",
    "grieg_lyric_pieces": "Grieg, Lyric Pieces",
    "handel_keyboard": "Handel, Grobschmied Variations HWV 430",
    "jc_bach_sonatas": "J.C. Bach, keyboard sonatas",
    "kleine_geistliche_konzerte": "Schuetz, Kleine Geistliche Konzerte (17th-c. sacred)",
    "kozeluh_sonatas": "Kozeluch, piano sonatas",
    "liszt_pelerinage": "Liszt, Annees de Pelerinage",
    "mahler_kindertotenlieder": "Mahler, Kindertotenlieder (orchestral song)",
    "medtner_tales": "Medtner, Tales (Skazki)",
    "mendelssohn_quartets": "Mendelssohn, string quartets",
    "monteverdi_madrigals": "Monteverdi, madrigals",
    "mozart_piano_sonatas": "Mozart, complete piano sonatas",
    "pergolesi_stabat_mater": "Pergolesi, Stabat Mater",
    "peri_euridice": "Peri, Euridice (1600) — earliest surviving opera, modal",
    "pleyel_quartets": "Pleyel, string quartets",
    "poulenc_mouvements_perpetuels": "Poulenc, Mouvements perpetuels",
    "rachmaninoff_piano": "Rachmaninoff, piano pieces",
    "ravel_piano": "Ravel, piano pieces",
    "scarlatti_sonatas": "D. Scarlatti, keyboard sonatas",
    "schubert_winterreise": "Schubert, Winterreise",
    "schulhoff_suite_dansante_en_jazz": "Schulhoff, Suite dansante en jazz (jazz-idiom art music)",
    "schumann_kinderszenen": "R. Schumann, Kinderszenen",
    "schumann_liederkreis": "R. Schumann, Liederkreis op. 39",
    "sweelinck_keyboard": "Sweelinck, organ/keyboard (Renaissance/early Baroque)",
    "tchaikovsky_seasons": "Tchaikovsky, The Seasons",
    "wagner_overtures": "Wagner, Tristan + Meistersinger preludes (orchestral, chromatic)",
    "wf_bach_sonatas": "W.F. Bach, keyboard sonatas",
}

# DCML harmony-TSV GT layers beyond the RN itself. NOTE: the 'form' column is
# chord-FORM (o/%/M/+), a harmony sub-field, NOT a phrase/structure layer — it is
# deliberately excluded here. 'cadence' = PAC/HC/IAC/EC/DC/PC(+HC subtypes);
# 'phraseend' = phrase-boundary brackets.
LAYER_COLS = ("cadence", "phraseend")


def _sha(p: Path) -> str | None:
    try:
        return subprocess.check_output(["git", "-C", str(p), "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return None


def _url(p: Path) -> str | None:
    try:
        return subprocess.check_output(["git", "-C", str(p), "remote", "get-url", "origin"], text=True).strip()
    except Exception:
        return None


def _harmony_versions(repo: Path) -> str:
    md = repo / "metadata.tsv"
    seen: dict[str, int] = {}
    if md.exists():
        with open(md, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                v = (r.get("harmony_version") or "").strip()
                if v:
                    seen[v] = seen.get(v, 0) + 1
    if not seen:
        return "DCML harmony (version unstamped in metadata)"
    parts = ", ".join(f"{k}({n})" for k, n in sorted(seen.items()))
    return f"DCML harmony {parts}"


def _layer_counts(repo: Path) -> dict:
    hdir = repo / "harmonies"
    counts = {c: 0 for c in LAYER_COLS}
    if not hdir.is_dir():
        return counts
    for t in hdir.glob("*.harmonies.tsv"):
        try:
            with open(t, newline="", encoding="utf-8") as f:
                rows = list(csv.DictReader(f, delimiter="\t"))
        except Exception:
            continue
        for col in counts:
            if rows and col in rows[0]:
                counts[col] += sum(1 for r in rows if (r.get(col) or "").strip() not in ("", ".", "@none", "~"))
    return counts


def dlc_rows() -> list[dict]:
    rows = []
    for d in sorted(DCML.iterdir()):
        if not d.is_dir() or d.name in NOT_DLC or not (d / "MS3").is_dir():
            continue
        repo = d.name
        mscx = len(list((d / "MS3").glob("*.mscx")))
        tsv = len(list((d / "harmonies").glob("*.harmonies.tsv"))) if (d / "harmonies").is_dir() else 0
        lc = _layer_counts(d)
        layers = ["rn"]
        if lc["cadence"]:
            layers.append("cadence")
        if lc["phraseend"]:
            layers.append("phrase")
        split = "dev" if (repo in PREWAVE1 or repo in NEW_DEV) else "held-out"
        rows.append({
            "name": repo,
            "container": "distant_listening_corpus",
            "content": DLC_CONTENT.get(repo, "?"),
            "pieces": mscx,
            "annotated_pieces": tsv,
            "gt_type": "rn",
            "gt_layers": layers,
            "layer_label_counts": lc,
            "annotation_standard": _harmony_versions(d),
            "score_format": "MuseScore .mscx (ms3 TSV extracts)",
            "alignment": "score-aligned",
            "license_class": "CC-BY-NC" if repo in CC_LICENSED else "unclear",
            "distribution": "hash-pin-only",
            "tier": "G",
            "status": "onboarded",
            "split": split,
            "provenance_url": _url(d),
            "pinned_commit": _sha(d),
            "notes": ("explicit CC BY-NC-SA 4.0 LICENSE in repo" if repo in CC_LICENSED
                      else "no in-repo LICENSE; org states CC BY-NC-SA [reported]") +
                     ("; onboarded pre-wave1" if repo in PREWAVE1 else "; onboarded corpus-wave1 2026-07-02"),
        })
    return rows


def _local_sha(rel: str) -> str | None:
    p = ROOT / rel
    return _sha(p) if (p / ".git").exists() else None


# Non-DLC sources the project uses / has cloned. Hand-encoded from the census
# appendices (cowork_score_census_gt_draft.md) + REPRODUCIBILITY.md; shas read
# live where the source is a local git clone.
def nondlc_rows() -> list[dict]:
    r = []
    r.append({
        "name": "when_in_rome", "container": "MarkGotham/When-in-Rome",
        "content": "RN meta-corpus (~1,500 works incl. TAVERN, HaydnSun, KMT, BPS-FH, Tymoczko TAOM Bach-371, WTC-I preludes, OpenScore Lieder RN)",
        "pieces": 762, "annotated_pieces": 762, "gt_type": "rn", "gt_layers": ["rn", "key"],
        "annotation_standard": "RomanText (analysis.txt) / remote.json",
        "score_format": "score.mxl / remote.json (music21-parsable)", "alignment": "score-aligned",
        "license_class": "CC-BY", "distribution": "hash-pin-only", "tier": "G", "status": "onboarded",
        "split": "dev", "provenance_url": "https://github.com/MarkGotham/When-in-Rome",
        "pinned_commit": _local_sha("tools/dcml/when_in_rome"),
        "notes": "Bach-chorale slice is the BIR gate human-annotation GT (dcml_parser.find_wir_file). CC BY-SA analyses, mixed/CC0 scores [verified].",
    })
    r.append({
        "name": "bach_chorales_dcml", "container": "DCMLab/bach_chorales",
        "content": "J.S. Bach chorales (Kaiser edition) — SCORES ONLY, no harmony labels",
        "pieces": 361, "annotated_pieces": 0, "gt_type": "none", "gt_layers": [],
        "annotation_standard": "n/a (labels column empty for every file [verified])",
        "score_format": "MuseScore .mscx", "alignment": "none",
        "license_class": "CC0", "distribution": "hash-pin-only", "tier": "S", "status": "onboarded",
        "split": "dev", "provenance_url": "https://github.com/DCMLab/bach_chorales",
        "pinned_commit": _local_sha("tools/dcml/bach_chorales"),
        "notes": "Source of 11-score pipeline-snapshot suite (MS3). NOT a DLC submodule. Bach-chorale RN GT is music21/WiR, not this repo.",
    })
    r.append({
        "name": "music21_bach_chorales", "container": "music21 built-in corpus",
        "content": "Bach chorales exported via music21 -> the BIR gate input + GT (tools/corpus)",
        "pieces": 353, "annotated_pieces": 326, "gt_type": "rn", "gt_layers": ["rn"],
        "annotation_standard": "music21 v.9.9.1 (RN via WiR overlay)",
        "score_format": "MusicXML (music21 export)", "alignment": "score-aligned",
        "license_class": "PD", "distribution": "hash-pin-only", "tier": "G", "status": "onboarded",
        "split": "dev", "provenance_url": "https://github.com/cuthbertLab/music21",
        "pinned_commit": None,
        "notes": "THE gate corpus. Version-pinned (music21 v9.9.1), not commit-pinned; gitignored/regenerable. Frozen — do not touch (CLAUDE.md gate policy).",
    })
    # Jazz/pop + research corpora (research-tier; some in corpora/ship [ship-licensed], some corpora/expl [NC/exploration]).
    r.append({
        "name": "choco", "container": "smashub/choco",
        "content": "ChoCo 18-partition chord-corpus aggregator (20,080 JAMS)",
        "pieces": 20080, "annotated_pieces": 20080, "gt_type": "chords", "gt_layers": ["chords", "key"],
        "annotation_standard": "JAMS / Harte-normalized", "score_format": "JAMS (mostly audio-aligned; symbolic subset)",
        "alignment": "chords-only", "license_class": "CC-BY", "distribution": "hash-pin-only", "tier": "J",
        "status": "onboarded", "split": "held-out", "provenance_url": "https://github.com/smashub/choco",
        "pinned_commit": _local_sha("corpora/ship/choco"),
        "notes": "Research-tier (idiom study). Chordify/Mozart/JAAH partitions CC BY-NC-SA.",
    })
    r.append({
        "name": "nottingham", "container": "jukedeck/nottingham-dataset",
        "content": "British/Irish folk tunes, ABC + chord symbols", "pieces": 1000, "annotated_pieces": 1000,
        "gt_type": "chords", "gt_layers": ["chords"], "annotation_standard": "ABC chord symbols",
        "score_format": "ABC (symbolic)", "alignment": "score-aligned", "license_class": "unclear",
        "distribution": "hash-pin-only", "tier": "J", "status": "onboarded", "split": "held-out",
        "provenance_url": "https://github.com/jukedeck/nottingham-dataset",
        "pinned_commit": _local_sha("corpora/ship/nottingham"), "notes": "Research-tier.",
    })
    r.append({
        "name": "mcgill_billboard", "container": "McGill Billboard (DDMAL)",
        "content": "US pop charts 1958-91, expert Harte chords", "pieces": 890, "annotated_pieces": 890,
        "gt_type": "chords", "gt_layers": ["chords"], "annotation_standard": "Harte / SALAMI",
        "score_format": "salami_chords text", "alignment": "chords-only", "license_class": "CC0",
        "distribution": "hash-pin-only", "tier": "J", "status": "onboarded", "split": "held-out",
        "provenance_url": "https://ddmal.music.mcgill.ca/research/The_McGill_Billboard_Project_(Chord_Analysis_Dataset)/",
        "pinned_commit": None, "notes": "Research-tier; local dir not a git repo (downloaded archive).",
    })
    r.append({
        "name": "irb", "container": "iRb (Shanahan/Broze, DCMLab lda_tpcs reference)",
        "content": "iRealPro jazz standards in Humdrum", "pieces": 1200, "annotated_pieces": 1200,
        "gt_type": "chords", "gt_layers": ["chords"], "annotation_standard": "Humdrum **harm/jazz",
        "score_format": "Humdrum (chart, no notation)", "alignment": "chords-only", "license_class": "unclear",
        "distribution": "hash-pin-only", "tier": "J", "status": "onboarded", "split": "held-out",
        "provenance_url": "https://github.com/DCMLab/lda_tpcs", "pinned_commit": None,
        "notes": "Research-tier; local dir not a git repo.",
    })
    r.append({
        "name": "jazz_harmony_treebank", "container": "DCMLab/JazzHarmonyTreebank",
        "content": "150 jazz standards, hierarchical harmonic syntax trees", "pieces": 150, "annotated_pieces": 150,
        "gt_type": "chords", "gt_layers": ["chords", "syntax-tree"], "annotation_standard": "JHT JSON",
        "score_format": "chords-only JSON", "alignment": "chords-only", "license_class": "CC-BY",
        "distribution": "hash-pin-only", "tier": "J", "status": "onboarded", "split": "held-out",
        "provenance_url": "https://github.com/DCMLab/JazzHarmonyTreebank",
        "pinned_commit": _local_sha("corpora/expl/jazz_harmony_treebank"), "notes": "Research-tier.",
    })
    r.append({
        "name": "hooktheory_hlsd", "container": "wayne391/lead-sheet-dataset (HLSD sample)",
        "content": "Hooktheory/TheoryTab crowd lead sheets (melody+chords+key, RN-convertible)",
        "pieces": None, "annotated_pieces": None, "gt_type": "chords", "gt_layers": ["chords", "key", "melody"],
        "annotation_standard": "TheoryTab XML/JSON", "score_format": "symbolic (proprietary)",
        "alignment": "score-aligned", "license_class": "unclear", "distribution": "hash-pin-only", "tier": "J",
        "status": "recorded", "split": "held-out", "provenance_url": "https://github.com/wayne391/lead-sheet-dataset",
        "pinned_commit": _local_sha("corpora/expl/hooktheory_hlsd"),
        "notes": "Research-tier sample; full HLSD pending HF m-a-p/HookTheory access.",
    })
    r.append({
        "name": "pop909", "container": "music-x-lab/POP909-Dataset",
        "content": "Chinese pop piano arrangements; chords/keys/beats/phrases", "pieces": 909, "annotated_pieces": 909,
        "gt_type": "chords", "gt_layers": ["chords", "key", "phrase"], "annotation_standard": "MIR-algorithm + human-corrected",
        "score_format": "MIDI (aligned)", "alignment": "score-aligned", "license_class": "unclear",
        "distribution": "hash-pin-only", "tier": "J", "status": "onboarded", "split": "held-out",
        "provenance_url": "https://github.com/music-x-lab/POP909-Dataset",
        "pinned_commit": _local_sha("corpora/expl/pop909"), "notes": "Research-tier; chord labels semi-automatic.",
    })
    r.append({
        "name": "chordonomicon", "container": "ailsntua/Chordonomicon (HF)",
        "content": "Ultimate-Guitar scrape, 666k chord progressions + section structure",
        "pieces": 666000, "annotated_pieces": 666000, "gt_type": "chords", "gt_layers": ["chords", "structure"],
        "annotation_standard": "chord symbols", "score_format": "chords-only (no scores)", "alignment": "none",
        "license_class": "CC-BY-NC", "distribution": "hash-pin-only", "tier": "X", "status": "recorded",
        "split": "held-out", "provenance_url": "https://huggingface.co/datasets/ailsntua/Chordonomicon",
        "pinned_commit": None, "notes": "Research-tier; no score alignment. Local dir not a git repo (HF download).",
    })
    r.append({
        "name": "lda_tpcs", "container": "DCMLab/lda_tpcs",
        "content": "Moss et al. tonal pitch-class LDA method reference data", "pieces": None, "annotated_pieces": None,
        "gt_type": "none", "gt_layers": [], "annotation_standard": "n/a (method reference)",
        "score_format": "derived data", "alignment": "none", "license_class": "unclear",
        "distribution": "hash-pin-only", "tier": "X", "status": "recorded", "split": "held-out",
        "provenance_url": "https://github.com/DCMLab/lda_tpcs", "pinned_commit": _local_sha("corpora/ship/lda_tpcs"),
        "notes": "Research-tier reference, not GT.",
    })
    # Jazz validation corpora (NO ground truth) — from REPRODUCIBILITY.md.
    for nm, cont, url, pieces in [
        ("omnibook", "Charlie Parker Omnibook (loria)", "https://homepages.loria.fr/evincent/omnibook/", 50),
        ("effendi", "Effendi jazz Real Book leadsheets", "https://effendi.me/jazz/repo/", 292),
        ("rampageswing", "Rampage Swing big-band charts", "https://www.rampageswing.com/", 36),
        ("pdmx", "PDMX public-domain MusicXML (scale/soak)", "https://zenodo.org/records/15571083", 250000),
    ]:
        r.append({
            "name": nm, "container": cont, "content": cont, "pieces": pieces, "annotated_pieces": 0,
            "gt_type": "none", "gt_layers": [], "annotation_standard": "n/a (no RN/harmony GT)",
            "score_format": "MusicXML/MXL", "alignment": "none", "license_class": "unclear" if nm != "pdmx" else "PD",
            "distribution": "hash-pin-only", "tier": "S", "status": "onboarded", "split": "held-out",
            "provenance_url": url, "pinned_commit": None,
            "notes": "Jazz/plain-score validation only, no GT (score_inventory.md).",
        })
    return r


def _annot_sha(name: str) -> str | None:
    p = ROOT / "corpora" / "annot" / name
    return _sha(p) if (p / ".git").exists() else None


# Wave-2 annotation/validation beds (axis 2). These are NOT analysis/score corpora:
# they are expert label layers laid over scores (schema / texture) or a standalone
# phrase-marked melody bed, used to VALIDATE the just-built axis-2 (voice leading)
# components. Distinguished by kind="annotation-bed". All are held-out validation
# material (never tuned against) and hash-pin-only under gitignored corpora/annot/.
# Per-bed extra fields beyond the base schema: kind, axis2_role, target_corpus,
# label_count. gt_type carries the bed-native layer (phrase | schema | texture).
def annotation_bed_rows() -> list[dict]:
    return [
        {
            "name": "schema_annotation_data",
            "container": "DCMLab/schema_annotation_data",
            "kind": "annotation-bed",
            "axis2_role": "VL-F footing (voice-leading schema recognition)",
            "content": "Expert galant voice-leading-schema annotations over 18 Mozart "
                       "piano sonatas / 54 mvts (Finkensiep, Deguernel, Neuwirth, "
                       "Rohrmeier, ISMIR 2020)",
            "target_corpus": "Mozart piano sonatas — self-contained repo bundle "
                             "(mscore/musicxml/notelist); same K-id/movement set as "
                             "DCML mozart_piano_sonatas",
            "pieces": 54,
            "annotated_pieces": 45,
            "label_count": 273,
            "gt_type": "schema",
            "gt_layers": ["voice-leading-schema"],
            "annotation_standard": "note-ID instance lists (repo-local IDs -> notelist/*.json); "
                                   "lexicon.json interval templates",
            "score_format": "MusicXML + JSON notelist (repo-bundled); MuseScore .mscx sources",
            "alignment": "score-aligned (repo-local note IDs; movement-keyed to DCML mozart by K-id)",
            "license_class": "unclear",
            "distribution": "hash-pin-only",
            "tier": "C",
            "status": "onboarded",
            "split": "held-out",
            "provenance_url": "https://github.com/DCMLab/schema_annotation_data",
            "pinned_commit": _annot_sha("schema_annotation_data"),
            "notes": "Wave-2 annotation bed (cc_corpus_wave2_report.md). No in-repo LICENSE -> "
                     "unclear (DCMLab org CC-BY-NC [reported]). Measured 273 true instances at pin "
                     "(10 base types w/ >=1 instance / 20 non-empty subtype dirs / 45 of 54 mvts); "
                     "paper reported 244 (living repo grown since 2020) — structure matches. Held-out.",
        },
        {
            "name": "symbolic_texture_dataset",
            "container": "algomus.fr/symbolic-texture-dataset (GitLab)",
            "kind": "annotation-bed",
            "axis2_role": "VL-C validation + spec 15-1 per-bar granularity reference",
            "content": "Per-bar symbolic-texture annotations for 9 Mozart sonata movements "
                       "(K279/K280/K283, all 3 mvts each) — Couturier, Bigo, Leve, ISMIR 2022 (v1.1)",
            "target_corpus": "DCML mozart_piano_sonatas (bar-keyed by mn per Hentschel 2021; "
                             "descriptors computed against DCML mozart v1.0 release)",
            "pieces": 9,
            "annotated_pieces": 9,
            "label_count": 1164,
            "gt_type": "texture",
            "gt_layers": ["symbolic-texture"],
            "annotation_standard": "texture syntax (M/H/S functions, density, diversity, 14 "
                                   "elements h/p/o/...); txt/tsv/dez formats; 62 bundled descriptors",
            "score_format": "TSV/TXT/Dezrann labels over DCML mozart_piano_sonatas .mscx",
            "alignment": "score-aligned (bar mn per DCML Annotated Mozart Sonatas convention)",
            "license_class": "ODbL-1.0 (data) + GPLv3 (code)",
            "distribution": "hash-pin-only",
            "tier": "C",
            "status": "onboarded",
            "split": "held-out",
            "provenance_url": "https://gitlab.com/algomus.fr/symbolic-texture-dataset",
            "pinned_commit": _annot_sha("symbolic-texture-dataset"),
            "notes": "Wave-2 annotation bed (cc_corpus_wave2_report.md). 1,164 bar labels verified "
                     "(= paper); 1,357 configurations via ',' sequential-separation. 62 descriptors "
                     "+ generator bundled in-repo (no separate descriptor clone needed); related "
                     "repos algomus.fr/texture, comparing-texture, pythouille/smc22-... recorded as "
                     "tooling-reference, NOT cloned. Held-out.",
        },
        {
            "name": "essen_folksong_collection",
            "container": "ccarh/essen-folksong-collection (CCARH kern edition, D. Huron)",
            "kind": "annotation-bed",
            "axis2_role": "VL-E footing (melodic per-line phrase segmentation)",
            "content": "Essen Folksong Collection in Humdrum **kern; expert phrase-boundary marks "
                       "({ open / } close) on monophonic folk melodies",
            "target_corpus": "self-contained (monophonic **kern melodies; no external score dependency)",
            "pieces": 8473,
            "annotated_pieces": 8473,
            "label_count": 36094,
            "gt_type": "phrase",
            "gt_layers": ["phrase-boundary"],
            "annotation_standard": "Humdrum kern phrase tokens { (open) / } (close)",
            "score_format": "Humdrum **kern (monophonic, single spine)",
            "alignment": "self-aligned (phrase marks inline in the melody line)",
            "license_class": "CCARH-MuseData-NC",
            "distribution": "hash-pin-only",
            "tier": "C",
            "status": "onboarded",
            "split": "held-out",
            "provenance_url": "https://github.com/ccarh/essen-folksong-collection",
            "pinned_commit": _annot_sha("essen-folksong-collection"),
            "notes": "Wave-2 annotation bed (cc_corpus_wave2_report.md). 8473 .krn total (europa "
                     "6213 ~ lit. 6236; asia 2246, america 13, africa 1). label_count=36094 = europa "
                     "phrase-open '{' tokens (europa 100% phrase-marked). CCARH MuseData license: "
                     "non-commercial, no commercial/derivative distribution -> hash-pin-only, never "
                     "redistributed. COVERAGE CAVEAT: monophonic folk melodies — a single-line vocal "
                     "bed for the per-voice phrase task, not usable for motion profiles (no voice "
                     "pairs) nor for the harmonic idiom pipeline (no chord symbols). Held-out.",
        },
    ]


def main() -> None:
    dlc = dlc_rows()
    other = nondlc_rows()
    beds = annotation_bed_rows()
    doc = {
        "_schema": "score_census_registry v2 (census §3 + CC corpus-wave1 dispatch 2026-07-02)",
        "_generated_by": "tools/build_score_census_registry.py (deterministic; re-run after any clone/pin change)",
        "_fields": ["name", "container", "content", "pieces", "annotated_pieces", "gt_type",
                    "gt_layers", "annotation_standard", "score_format", "alignment",
                    "license_class", "distribution", "tier", "status", "split",
                    "provenance_url", "pinned_commit", "notes"],
        "_notes": [
            "gt_type enum: rn|chords|key|cadence|phrase|none (+ schema|texture for annotation_beds). "
            "tier: G|J|C|S|X. distribution: committable|hash-pin-only. "
            "license_class: PD|CC0|CC-BY|CC-BY-NC|unclear (annotation_beds may carry a precise license "
            "token, e.g. ODbL/GPLv3 or CCARH-MuseData-NC). "
            "split: dev|held-out (held-out never tuned against; demotion to dev only by explicit recorded decision).",
            "All DLC members are distribution=hash-pin-only (gitignored under tools/dcml/; C1-audit mechanism) "
            "regardless of license_class. 28 of 40 DLC repos have NO in-repo LICENSE (license_class=unclear).",
            "DLC 'pieces'=MS3 .mscx movement count; 'annotated_pieces'=harmonies TSV count. "
            "Every DLC harmonies TSV also carries cadence/form/phraseend columns (layer_label_counts) that "
            "dcml_parser.py currently DROPS (reads only numeral/chord/keys) — see cc_corpus_wave1_report.md §4.",
            "Container = distant_listening_corpus has 40 submodules (census '41' was an overcount; verified from "
            ".gitmodules 2026-07-02).",
            "annotation_beds (Wave-2, cc_corpus_wave2_report.md): expert LABEL layers over scores (schema/texture) "
            "or a standalone phrase-marked melody bed, for validating axis-2 (voice leading). kind='annotation-bed'; "
            "extra fields kind/axis2_role/target_corpus/label_count. All held-out (never tuned against), hash-pin-only "
            "under gitignored corpora/annot/. They add labels over already-held scores (schema/texture over Mozart) or "
            "material outside the discovery views (Essen monophonic, no chords) — NOT analysis/gate corpora.",
        ],
        "distant_listening_corpus": {
            "submodule_count": len(dlc),
            "onboarded": len(dlc),
            "members": dlc,
        },
        "other_sources": other,
        "annotation_beds": beds,
    }
    OUT.write_text(json.dumps(doc, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT}  DLC={len(dlc)} other={len(other)} beds={len(beds)} "
          f"total={len(dlc)+len(other)+len(beds)}")


if __name__ == "__main__":
    main()

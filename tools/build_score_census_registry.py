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
        row = {
            "name": nm, "container": cont, "content": cont, "pieces": pieces, "annotated_pieces": 0,
            "gt_type": "none", "gt_layers": [], "annotation_standard": "n/a (no RN/harmony GT)",
            "score_format": "MusicXML/MXL", "alignment": "none", "license_class": "unclear" if nm != "pdmx" else "PD",
            "distribution": "hash-pin-only", "tier": "S", "status": "onboarded", "split": "held-out",
            "provenance_url": url, "pinned_commit": None,
            "notes": "Jazz/plain-score validation only, no GT (score_inventory.md).",
        }
        if nm == "pdmx":
            # Acquisition round (2026-07-04, cc_acquisition_round_report.md Task 3): the N12 <harmony>
            # counting pass was ATTEMPTED + STOPPED — the held form cannot answer it. Recorded here per
            # the dispatch ("the pdmx registry row's needs_coverage note").
            row["needs_coverage"] = (
                "N12 (realized-texture chord-symbol subset) — COUNTING PASS ATTEMPTED + STOPPED "
                "(cc_acquisition_round_report.md §Task-3). The HELD form is METADATA-ONLY: tools/pdmx/PDMX.csv "
                "(a 250k-row, 225 MB index) + derived jazz_candidates.csv + 5 spot-check .mxl. It carries NO "
                "chord-symbol field — `n_annotations`/`has_annotations` conflate ALL annotation types (chord "
                "symbols + dynamics + tempo + text; per analyze_pdmx.py's own note), `tracks` = instrument-program "
                "codes ('0-0'), and there is no n_chords/n_harmony column. The raw MXL (the `mxl` column paths, in "
                "mxl.tar.gz) and the per-score MusicRender JSON (the `metadata` column paths) live ONLY in the Zenodo "
                "archive (record 15571083), NOT on disk. Counting <harmony>/ChordSymbol would require fetching "
                "mxl.tar.gz + parsing per file, or the MusicRender JSON form — a re-download/acquisition (a FUTURE "
                "user decision), which the read-only, do-not-re-download dispatch forbids. No proxy was invented "
                "(has_annotations would over-count). The symbol-bearing multi-voice subset stays UNMEASURED."
            )
        r.append(row)
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


def _corpora_sha(rel: str) -> str | None:
    """SHA of a git clone under corpora/ (gitignored, hash-pin-only). None if absent."""
    p = ROOT / rel
    return _sha(p) if (p / ".git").exists() else None


def _file_sha256(rel: str) -> str | None:
    """sha256 of a pinned downloaded artifact (non-git, e.g. the WJD SQLite). None if absent."""
    import hashlib
    p = ROOT / rel
    if not p.is_file():
        return None
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()


# Wave-3 sources (corpus wave 3, 2026-07-04; cc_corpus_wave3_report.md). Per the census
# §8c FULL-NEEDS AUDIT disposition (user, 2026-07-04): jazz/pop GT + cadence/form/dual-annotator
# beds + figured bass + trees/reduction + plain-score stress. All held-out (never tuned against),
# all hash-pin-only under gitignored corpora/gt|plain/. Per the census §8c INTAKE RULE each row
# carries a `needs_coverage` note scored against the FULL vector N1-N20 (not single-purpose tagged).
# `status`: onboarded (cloned+pinned+inventoried) | walked (inspected, finding recorded) |
# inventory (already-held material re-inventoried, no new clone) | gated (access-restricted, path
# recorded) | unavailable (no public deposit found, access path recorded) | enumerated (manifest
# recorded, nothing cloned). Shas read live from the clones; None when the clone/artifact is absent.
def wave3_rows() -> list[dict]:
    r = []
    r.append({
        "name": "cocopops", "container": "Computational-Cognitive-Musicology-Lab/CoCoPops",
        "content": "Coordinated Corpus of Popular Music: melodic+harmonic transcriptions of "
                   "Billboard (McGill Billboard in Humdrum + 214 new melody transcriptions) + "
                   "RollingStone (RS200) — README: 414 complete transcriptions of 398 unique tracks",
        "pieces": 398, "annotated_pieces": 414, "gt_type": "rn", "gt_layers": ["harm", "kern-melody", "harte", "phrase", "form"],
        "annotation_standard": "Humdrum (**harm RN + **kern melody + **harte + **phrase + **form + metadata spines)",
        "score_format": "Humdrum .hum (fully symbolic)", "alignment": "score-aligned",
        "license_class": "CC-BY", "distribution": "hash-pin-only", "tier": "J", "status": "onboarded",
        "split": "held-out", "provenance_url": "https://github.com/Computational-Cognitive-Musicology-Lab/CoCoPops",
        "pinned_commit": _corpora_sha("corpora/gt/CoCoPops"),
        "needs_coverage": "N3 (jazz/pop analysis GT, score-aligned — the top Tier-J acquisition; **harm RN "
                          "+ **kern melody, fully symbolic); N12-adj (chord symbols aligned with a symbolic "
                          "melody line, not a full realized score); N16-adj (**form/phrase spines); N17 (rich "
                          "metadata). Verified 628 .hum (Billboard 428 + RollingStone 200); 414 complete "
                          "transcriptions per README. DEDUPE: absorbs McGill-Billboard + RS200 (both held as "
                          "ChoCo partitions + registry rows) — the symbolic superset of those chord-only slices.",
        "notes": "Wave-3 (cc_corpus_wave3_report.md). 628 .hum at pin; **harm+**kern+**harte spines verified. Held-out.",
    })
    r.append({
        "name": "openewld", "container": "00sapo/OpenEWLD",
        "content": "Public-domain subset of EWLD (Enhanced Wikifonia Leadsheet Dataset): MusicXML "
                   "lead sheets (melody + chord symbols) with metadata",
        "pieces": 486, "annotated_pieces": 486, "gt_type": "chords", "gt_layers": ["chords", "melody"],
        "annotation_standard": "MusicXML harmony + melody; per-piece feature CSV", "score_format": "compressed MusicXML (.mxl)",
        "alignment": "score-aligned", "license_class": "PD", "distribution": "hash-pin-only", "tier": "J",
        "status": "onboarded", "split": "held-out", "provenance_url": "https://github.com/00sapo/OpenEWLD",
        "pinned_commit": _corpora_sha("corpora/gt/OpenEWLD"),
        "needs_coverage": "N12 (chord symbols + melody leadsheet — the symbol+melody half; the symbol+REALIZED-score "
                          "half stays thin); N3-adj (lead-sheet chords, no functional RN); N17. MEASURED 486 .mxl at pin "
                          "vs the ~502 census/paper claim (living-repo/PD-filter variance — reported, not silently "
                          "accepted). Zenodo DOI 10.5281/zenodo.4332855. DEDUPE: PD subset of EWLD (⊃ OpenEWLD; EWLD "
                          "gated, separate row). WINDOWS caveat: git checkout fails on one '?' filename (NTFS-illegal); "
                          "pin + inventory taken from git objects (ls-tree) — bed is hash-pin-only, so unaffected.",
        "notes": "Wave-3 (cc_corpus_wave3_report.md). 486 .mxl (git ls-tree; Windows working-tree checkout partial). Held-out.",
    })
    r.append({
        "name": "bcfb", "container": "juyaolongpaul/Bach_chorale_FB",
        "content": "Bach Chorales Figured Bass (BCFB) v2.0: 139 J.S. Bach chorales with figured-bass "
                   "encodings in MusicXML / **kern / MEI, based on the Neue Bach Ausgabe (Ju et al., ISMIR 2020)",
        "pieces": 139, "annotated_pieces": 143, "gt_type": "figured-bass", "gt_layers": ["figured-bass"],
        "annotation_standard": "figured-bass symbols in MusicXML/kern/MEI (143 files: BWV 10.07/161.06/38.06/177.05 have two NBA versions)",
        "score_format": "MusicXML + Humdrum **kern + MEI", "alignment": "score-aligned",
        "license_class": "CC-BY", "distribution": "hash-pin-only", "tier": "C", "status": "onboarded",
        "split": "held-out", "provenance_url": "https://github.com/juyaolongpaul/Bach_chorale_FB",
        "pinned_commit": _corpora_sha("corpora/gt/Bach_chorale_FB"),
        "needs_coverage": "N10 (figured-bass GT — the gate repertoire's OWN composer-stated harmony evidence, "
                          "L4 evidence channel R-4); N1-adj (Bach chorales, but FB not RN); N17. VERIFIED at data: "
                          "kern 143 / mei 146 / musicXML_master 248 (in-progress additions); reference_table.csv. "
                          "The third N10 source beside DCMLab/figured-bass (a realization TOOL, not GT — see that row) "
                          "and the DLC figbass column (parser-dropped). Also Zenodo 5084914.",
        "notes": "Wave-3 (cc_corpus_wave3_report.md). 139 chorales / 143 canonical files (kern count). Held-out.",
    })
    r.append({
        "name": "algomus_data", "container": "algomus.fr/algomus-data (GitLab)",
        "content": "Algomus datasets monorepo (backs algomus.fr/data): quartets/mozart (32 Mozart string-quartet "
                   "movements, Dezrann sonata-form + cadence GT), fugues/bach-wtc-i (Bach WTC-I fugue subjects/"
                   "countersubjects/cadences/pedals), jazz-arbres (jazz harmony treebank)",
        "pieces": 32, "annotated_pieces": 55, "gt_type": "form", "gt_layers": ["structure", "cadence", "harmony", "fugue-subject", "pedal", "jazz-tree"],
        "annotation_standard": "Dezrann .dez (labels: type Structure/Cadence/Harmony, onset+duration in seconds, line)",
        "score_format": "Dezrann .dez labels over external Mozart-quartet / WTC scores (onset-in-seconds keyed)",
        "alignment": "score-aligned (onset/duration in seconds; external scores)", "license_class": "ODbL-1.0",
        "distribution": "hash-pin-only", "tier": "C", "status": "onboarded", "split": "held-out",
        "provenance_url": "https://gitlab.com/algomus.fr/algomus-data",
        "needs_coverage": "★ MULTI-NEED. N16 (Mozart SQ sonata-form — the RATIFIED best form/section-GT candidate, "
                          "quartets/mozart = 32 -ref.dez, matches paper); N4 (cadence labels, quartets + fugues); "
                          "N18 (fugue subjects/countersubjects — the adopted-2026-07-04 contrapuntal/imitative GT); "
                          "N20 (fugue pedal-point labels — the adopted own-row need); N11-adj + N3-adj (jazz-arbres "
                          "treebank.json, 1170 entries — jazz harmony trees). GAP REPORTED: fugues/ holds bach-wtc-i "
                          "(23 -ref.dez of 24) only; the 12 Shostakovich fugues are NOT in the repo (website-only). "
                          "ALIGNMENT caveat: .dez onsets are in SECONDS keyed to a specific score/recording, not "
                          "ticks — a mapping step is owed before load-bearing use.",
        "notes": "Wave-3 (cc_corpus_wave3_report.md). quartets/mozart 32 ref.dez; fugues/bach-wtc-i 23 ref.dez (no Shostakovich); jazz-arbres treebank 1170. Held-out.",
        "pinned_commit": _corpora_sha("corpora/gt/algomus-data"),
    })
    r.append({
        "name": "protovoice_annotations", "container": "DCMLab/protovoice-annotations",
        "content": "Pieces/excerpts annotated with protovoice analyses (Finkensiep dissertation ch. 7): "
                   "note-to-note reduction derivations (regular + passing edges, reduction slices)",
        "pieces": 63, "annotated_pieces": 38, "gt_type": "reduction", "gt_layers": ["protovoice-derivation"],
        "annotation_standard": "protovoice .analysis.json (topSegments -> trans.edges {regular,passing} + rslice.notes; loadable in the protovoice viewer)",
        "score_format": "MusicXML + .analysis.json (+ .piece.json)", "alignment": "score-aligned (paired MusicXML)",
        "license_class": "unclear", "distribution": "hash-pin-only", "tier": "C", "status": "onboarded",
        "split": "held-out", "provenance_url": "https://github.com/DCMLab/protovoice-annotations",
        "pinned_commit": _corpora_sha("corpora/gt/protovoice-annotations"),
        "needs_coverage": "N9 (stream/implied-polyphony GT — this INSPECTION GATES the Cowork-side N9 union search; "
                          "verdict below); N11 (hierarchical harmony/voice reduction trees, the JHT/Schenker family); "
                          "N1-adj (score-aligned). INSPECTED: 38 .analysis.json derivations + 63 MusicXML + 5 .piece.json "
                          "(bach 3 / examples 2 / theory-article 33), WIP. N9 VERDICT = PARTIALLY usable: the regular+"
                          "passing edges ARE note-level voice-connection GT (the raw material for stream/voice-separation), "
                          "but encoded as HIERARCHICAL reduction derivations (surface->background), not flat surface-stream "
                          "labels, and small (38); usable for N9 only via a derivation->surface-stream extraction step. "
                          "Nearest thing to stream GT in the whole enumeration; does not by itself close N9.",
        "notes": "Wave-3 (cc_corpus_wave3_report.md). N9 gating inspection — see needs_coverage. Held-out.",
    })
    r.append({
        "name": "schenker41", "container": "pkirlin/schenker41",
        "content": "41 common-practice excerpts with machine-readable Schenkerian analyses (Kirlin PhD dissertation, "
                   "UMass Amherst 2014 / ISMIR 2014) — 18 Mozart, 7 Haydn, 5 Beethoven, 4 Schubert, 3 Bach, 2 Chopin, "
                   "1 each Handel/Clementi",
        "pieces": 41, "annotated_pieces": 41, "gt_type": "reduction", "gt_layers": ["schenkerian-prolongation"],
        "annotation_standard": "MusicXML + text prolongation files (X (Y) Z, notes by measure/pitch/octave/occurrence)",
        "score_format": "MusicXML + analysis text (per README)", "alignment": "score-aligned",
        "license_class": "unclear", "distribution": "hash-pin-only", "tier": "C", "status": "recorded",
        "split": "held-out", "provenance_url": "https://github.com/pkirlin/schenker41",
        "pinned_commit": _corpora_sha("corpora/gt/schenker41"),
        "needs_coverage": "N11 (hierarchical trees / reduction — the COMMON-PRACTICE counterpart to the JHT jazz trees; "
                          "N11's classical half); N1-adj. ACCESS FINDING: the pinned GitHub repo contains ONLY README.md "
                          "at HEAD (and in its entire history — verified git log --all); the 41 MusicXML + analysis files "
                          "are NOT committed. The data is referenced to the dissertation page "
                          "http://www.cs.rhodes.edu/~kirlinp/diss.html — access path recorded, data not obtained this wave. "
                          "(A newer 2024 dataset exists: arXiv 2408.07184.)",
        "notes": "Wave-3 (cc_corpus_wave3_report.md). Repo pinned = README only; data at the dissertation page. Held-out.",
    })
    r.append({
        "name": "weimar_jazz_database", "container": "jazzomat.hfm-weimar.de (WJazzD, native)",
        "content": "Weimar Jazz Database: 456 monophonic jazz-solo transcriptions with beats/sections/metadata "
                   "(the native SQLite, beyond the ChoCo chord slice)",
        "pieces": 456, "annotated_pieces": 456, "gt_type": "chords", "gt_layers": ["melody", "beats", "sections", "chords", "metadata"],
        "annotation_standard": "SQLite (solo_info/melody/beats/sections/... ; db_info v2.1 DB 2.2, 2018)",
        "score_format": "SQLite3 database (wjazzd.db)", "alignment": "score-aligned (onset-timed within each solo)",
        "license_class": "ODbL-1.0", "distribution": "hash-pin-only", "tier": "J", "status": "onboarded",
        "split": "held-out", "provenance_url": "https://jazzomat.hfm-weimar.de/download/downloads/wjazzd.db",
        "pinned_commit": _file_sha256("corpora/gt/weimar-jazz-database/wjazzd.db"),
        "needs_coverage": "N3 (jazz analysis material); N4 (the native phrase/sections layer — WJD `sections` table, "
                          "beyond the ChoCo chord slice); N16 (form via sections); N17 (per-solo style/genre/tonality "
                          "metadata). VERIFIED: 456 solos (solo_info + transcription_info), 200,809 melody rows, ODbL "
                          "license embedded in db_info. Pinned by sha256 (non-git artifact, pinnable-source rule). DEDUPE: "
                          "the ChoCo `weimar` partition (916 jams, held) is the chord-slice re-encoding of THIS DB; the "
                          "native DB adds the phrase/form/beat layers ChoCo drops.",
        "notes": "Wave-3 (cc_corpus_wave3_report.md). 42.5 MB SQLite pinned by sha256. Held-out.",
    })
    r.append({
        "name": "openscore_lieder", "container": "OpenScore/Lieder",
        "content": "OpenScore Lieder Corpus: late-romantic art songs, CC0, proofread (MuseScore .mscx + MusicXML)",
        "pieces": 1352, "annotated_pieces": 0, "gt_type": "none", "gt_layers": [],
        "annotation_standard": "n/a (plain scores; the RN subset lives in When-in-Rome)", "score_format": "MuseScore .mscx / MusicXML .mxl",
        "alignment": "none", "license_class": "CC0", "distribution": "hash-pin-only", "tier": "S", "status": "onboarded",
        "split": "held-out", "provenance_url": "https://github.com/OpenScore/Lieder",
        "pinned_commit": _corpora_sha("corpora/plain/Lieder"),
        "needs_coverage": "Tier S (plain-score chromatic-stress bed — the best chromatic soak material). N1-carrier: "
                          "the CC0 SCORE half of the When-in-Rome OpenScore-Lieder RN subset (179 analyzed, WiR row); "
                          "N17 (era). No GT of its own. VERIFIED 1462 .mxl / 1352 .mscx at pin (>1,300 claim). "
                          "NOT gate/analysis material (dormant-build discipline) — held-out stress/soak only.",
        "notes": "Wave-3 (cc_corpus_wave3_report.md). depth-1 clone; 1462 mxl / 1352 mscx. Held-out.",
    })
    r.append({
        "name": "openscore_string_quartets", "container": "OpenScore/StringQuartets",
        "content": "OpenScore String Quartet Corpus: historic string quartets, CC0 (MuseScore .mscx)",
        "pieces": 122, "annotated_pieces": 0, "gt_type": "none", "gt_layers": [],
        "annotation_standard": "n/a (plain scores)", "score_format": "MuseScore .mscx",
        "alignment": "none", "license_class": "CC0", "distribution": "hash-pin-only", "tier": "S", "status": "onboarded",
        "split": "held-out", "provenance_url": "https://github.com/OpenScore/StringQuartets",
        "pinned_commit": _corpora_sha("corpora/plain/StringQuartets"),
        "needs_coverage": "Tier S (plain-score; the texture gap between chorales and piano). N7-material (texture — "
                          "raw scores, no texture GT; the algomus texture bed is the GT); N17. VERIFIED 122 .mscx at pin "
                          "(>100 claim). NOT gate material — held-out.",
        "notes": "Wave-3 (cc_corpus_wave3_report.md). depth-1 clone; 122 mscx. Held-out.",
    })
    r.append({
        "name": "asap", "container": "fosfrancesco/asap-dataset",
        "content": "ASAP: 222 romantic/classical piano MusicXML scores aligned to performance MIDIs "
                   "(the MIDIs ride along; our material is the scores)",
        "pieces": 222, "annotated_pieces": 0, "gt_type": "none", "gt_layers": [],
        "annotation_standard": "n/a (score + performance-MIDI alignment; no harmonic GT)", "score_format": "MusicXML (.xml) + performance MIDI",
        "alignment": "none", "license_class": "CC-BY-NC", "distribution": "hash-pin-only", "tier": "S", "status": "onboarded",
        "split": "held-out", "provenance_url": "https://github.com/fosfrancesco/asap-dataset",
        "pinned_commit": _corpora_sha("corpora/plain/asap-dataset"),
        "needs_coverage": "Tier S (real romantic-piano MusicXML scores for stress/soak). Explicitly NOT N15 "
                          "(performed-intonation) — piano is fixed intonation and the alignment is TIMING, not intonation "
                          "(N15 ruled audio-domain / out of corpus scope, 2026-07-04). The performance MIDIs (1302) are "
                          "NOT our material. N17. VERIFIED 235 .xml / 1302 .mid at pin (~222 distinct scores). Held-out.",
        "notes": "Wave-3 (cc_corpus_wave3_report.md). depth-1 clone; 235 xml / 1302 midi. Held-out.",
    })
    # --- Wave-3 ADDENDUM (2026-07-04, cc_wave3_addendum_report.md): two DDMAL direct pickups.
    #     KMT = the N5 upstream the Wave-3 correction named; Flexible = surfaced by the humdrum-data
    #     closure (§7 of the Wave-3 report). Both cloned+pinned+walked under gitignored corpora/gt/. ---
    r.append({
        "name": "key_modulation_dataset", "container": "DDMAL/key_modulation_dataset",
        "content": "Key/modulation annotations over music-theory-textbook examples (Aldwell-Schachter-"
                   "Cadwallader, Kostka-Payne, Reger, Rimsky-Korsakov, Tchaikovsky) in Humdrum — the "
                   "upstream KMT the Wave-3 audit wrongly located inside When-in-Rome (DLfM-2020 lineage)",
        "pieces": 201, "annotated_pieces": 201, "gt_type": "key", "gt_layers": ["key", "modulation", "rn"],
        "annotation_standard": "Humdrum **kern (4 voices) + **text annotation spines; key/modulation as "
                               "Humdrum key-designation tokens (*C:, *G:) + inline NEWKEY=>:RN modulation "
                               "markers in the **text spine (e.g. 'c=>:viio6'); spine-association scripts embed each annotation to its note",
        "score_format": "Humdrum **kern + **text (.krn)", "alignment": "score-aligned",
        "license_class": "CC-BY-SA (scores) + MIT (code)", "distribution": "hash-pin-only", "tier": "C",
        "status": "onboarded", "split": "held-out", "provenance_url": "https://github.com/DDMAL/key_modulation_dataset",
        "pinned_commit": _corpora_sha("corpora/gt/key_modulation_dataset"),
        "needs_coverage": "★ N5 PRIMARY (key/modulation/tonicization GT — the S1/S2 residual's exact shape; the "
                          "direct-acquisition candidate the Wave-3 N5 correction named after KMT was found ABSENT as "
                          "analyses at the WiR pin). N1-adj (the **text spines ALSO carry Roman-numeral harmonic "
                          "analysis, textbook-relative not corpus-canonical); N17 (textbook provenance). VERIFIED at data: "
                          "201 .krn at pin, ALL bearing **text annotation spines — aldwell 7 / kostka-payne 15 / reger 117 / "
                          "rimsky-korsakov 37 / tchaikovsky 25. MISMATCH reported-not-accepted: the README 'Dataset' "
                          "checkbox list enumerates ~135 annotated examples (aldwell 7 / KP 14 / reger 'Examples 1-100' / "
                          "RK 7 / tchaik 7); the pinned repo has grown past it (KP 15 = ex18-3 split a/b per NOTES.md; "
                          "reger 117 / RK 37 / tchaik 25). Encoders: Feisthauer + Napoles Lopez (ENC record). DEDUPE: the "
                          "actual KMT upstream, DISJOINT from the held DLC/WiR common-practice RN GT (textbook examples, "
                          "not repertoire); closes the N5 acquisition the Wave-3 correction queued.",
        "notes": "Wave-3 addendum (cc_wave3_addendum_report.md). 201 annotated .krn across 5 textbooks. CC-BY-SA scores / MIT code. Held-out.",
    })
    r.append({
        "name": "flexible_harmonic_chorale_annotations", "container": "DDMAL/Flexible_harmonic_chorale_annotations",
        "content": "Permutational ('flexible') harmonic analyses of 571 chorales (371 J.S. Bach + 200 Praetorius), "
                   "companion to the ISMIR 2018 paper; the analysis GT ships as an R package (data.table binary), the "
                   "kernData/ folder holds the raw Humdrum **kern scores",
        "pieces": 572, "annotated_pieces": 571, "gt_type": "rn", "gt_layers": ["permutational-harmony"],
        "annotation_standard": "R package FlexibleChoraleHarmonicAnalysis 0.8.0 (permutational analysis data.tables "
                               "+ filtering functions; README-stated coverage, binary not extracted); scores in Humdrum "
                               "**kern with NO analysis spine in the .krn",
        "score_format": "Humdrum **kern (.krn) scores; analysis in an R-package .tar.gz binary (6.8 MB)", "alignment": "score-aligned",
        "license_class": "GPL-3.0", "distribution": "hash-pin-only", "tier": "C", "status": "onboarded",
        "split": "held-out", "provenance_url": "https://github.com/DDMAL/Flexible_harmonic_chorale_annotations",
        "pinned_commit": _corpora_sha("corpora/gt/Flexible_harmonic_chorale_annotations"),
        "needs_coverage": "N2 candidate (a SECOND, MULTI-READING annotation layer over gate-class Bach chorales — the "
                          "'flexible'/permutational method admits MULTIPLE valid harmonic readings per slice with "
                          "filtering functions, unlike a single canonical RN) + N1-residual (harmony GT over Bach chorales). "
                          "⚠ OVERLAPS THE GATE REPERTOIRE: the 371 Bach chorales are the Breitkopf/Doerffel 371 "
                          "Four-Part Chorales (KernScores lineage — the same works as the music21 gate corpus). RECORD-ONLY "
                          "this dispatch: NOT wired to / compared against / bulk-diffed with the gate corpus; any use over "
                          "gate pieces is a FUTURE USER ruling (census §4 dedupe / M3 contamination lesson). WALK finding: "
                          "the annotation GT is bundled in the R-package BINARY (6.8 MB data.table), NOT a directly-readable "
                          "text/Humdrum spine — the kernData/ .krn are **kern-ONLY scores (verified: 572/572 files carry "
                          "only **kern). Coverage: 572 .krn = 371 Bach + 201 Praetorius files (200 logical; 130a/130b "
                          "split); README says 571 — reported-not-accepted. The 200 Praetorius chorales are NEW (not "
                          "available elsewhere per README) and lie OUTSIDE the gate repertoire.",
        "notes": "Wave-3 addendum (cc_wave3_addendum_report.md). 572 .krn (371 Bach / 201 Praetorius files); analysis in R-package binary. GPLv3. RECORD-ONLY re gate. Held-out.",
    })
    # --- ACQUISITION ROUND (2026-07-04, cc_acquisition_round_report.md): the union-search-approved pickups
    #     (cowork_union_search_record.md §6, user-disposed). N9 voice-separation beds (piano_svsep + MCMA +
    #     vocsep) + N14 Mikrokosmos + N12 GuitarSet + multi-need Batik-plays-Mozart, all cloned/pinned;
    #     CIPI (gated) + PSyllabus (recorded), no clone. All held-out, hash-pin-only under gitignored
    #     corpora/gt/. TWO record license mismatches CORRECTED at the data: MCMA = CC-BY-NC-SA-4.0 (record
    #     said CC-BY-4.0); vocsep = MIT (record said license-unstated). ---
    r.append({
        "name": "piano_svsep", "container": "CPJKU/piano_svsep",
        "content": "Piano Staff and Voice Separation (Foscarin/Karystinaios/Nakamura/Widmer, ISMIR 2024): a GNN "
                   "that clusters notes into chords and links them into voices+staves. The repo ships CODE + "
                   "pretrained models; the GT graph dataset (the `dcml` set — per-note voice+staff+chord-cluster "
                   "labels over DCML-corpus piano scores, cross-staff voices included) is FETCHED AT RUNTIME, not committed",
        "pieces": 393, "annotated_pieces": 393, "gt_type": "voice", "gt_layers": ["voice", "staff", "chord-cluster"],
        "annotation_standard": "graph GT (DGL heterograph): per-note voice-link + staff + chord-cluster edges, built "
                               "by the loader from engraved MusicXML voice/staff assignments",
        "score_format": "code (Python) + fetched MusicXML (DCML piano corpora)", "alignment": "score-derived (engraving voices)",
        "license_class": "MIT (code)", "distribution": "hash-pin-only", "tier": "C", "status": "onboarded",
        "split": "held-out", "provenance_url": "https://github.com/CPJKU/piano_svsep",
        "pinned_commit": _corpora_sha("corpora/gt/piano_svsep"),
        "needs_coverage": "★ N9 PRIMARY (stream/voice-separation GT, notated-polyphony half — per-note voice+staff+"
                          "chord-cluster labels incl. homophonic (chord) voices and CROSS-STAFF voices; the SOTA piano "
                          "voice/staff task set). N1-adj. VERIFIED at data: the repo ships CODE (piano_svsep/ package + "
                          "pretrained_models + one test_score artifact) — NOT the GT graphs. `DCMLPianoCorporaDataset` "
                          "FETCHES the raw data at runtime from github.com/fosfrancesco/piano_corpora_dcml.git "
                          "(scores/<collection>/*.musicxml; per-note voice/staff GT derived from the engraving). PIN = the "
                          "code repo; the ACTUAL GT lives at the fetch path (a follow-on pin candidate, NOT fetched this "
                          "round). The companion `jpop` set is CONFIRMED non-public (README + MusescoreJPopDataset docstring "
                          "'not publicly available … only for reference') — access-path line, not chased. OVERLAP by work: "
                          "the 393 are DCML piano corpora = the same family as our held DLC piano members (mozart/beethoven/"
                          "chopin/scarlatti/kozeluh/…); the exact 393↔DLC map needs the piano_corpora_dcml manifest (not "
                          "fetched). CAVEAT (record §1): labels originate from engraved notation — for piano, engraving-voice "
                          "≈ the inference target (the SOTA field accepts this); stated at intake.",
        "notes": "Acquisition round (cc_acquisition_round_report.md). Code repo pinned; GT fetched at runtime from fosfrancesco/piano_corpora_dcml. MIT (code). Held-out.",
    })
    r.append({
        "name": "mcma", "container": "skalo/mcma (GitLab)",
        "content": "Multitrack Contrapuntal Music Archive (Aljanaki/Kalonaris/Micchi/Nichols 2021): symbolic "
                   "Baroque/contrapuntal works hand-edited so every polyphonic work has one INDEPENDENT PART PER TRACK "
                   "(incl. keyboard fugues, inventions, WTC I/II) — flat per-note voice GT by construction",
        "pieces": 475, "annotated_pieces": 475, "gt_type": "voice", "gt_layers": ["voice"],
        "annotation_standard": "one-voice-per-track MusicXML (voice = the track assignment; per-piece metadata.csv "
                               "carries 'Number of Tracks', instruments, provenance)",
        "score_format": "compressed MusicXML (.mxl)", "alignment": "score-aligned",
        "license_class": "CC-BY-NC-SA-4.0", "distribution": "hash-pin-only", "tier": "C", "status": "onboarded",
        "split": "held-out", "provenance_url": "https://gitlab.com/skalo/mcma",
        "pinned_commit": _corpora_sha("corpora/gt/mcma"),
        "needs_coverage": "★ N9 (stream/voice-separation GT — flat per-note voice = the one-voice-per-track assignment, the "
                          "cleanest-form voice GT; hand-exploded Baroque counterpoint). N18-adj (fugues/canons). VERIFIED at "
                          "data: 475 .mxl (matches the record's ~475) + 12 metadata.csv + 11 json. Track-count split "
                          "RE-COUNTED at the data from metadata.csv 'Number of Tracks' = 153 two-track / 239 three-track / 83 "
                          "four-plus (73×4 + 8×5 + 2×6) = 475 — EXACTLY the record's 239/153/83. Composers: albinoni, "
                          "bach_js (goldberg, inventions, kunst_der_fuge, sinfonias, WTC I, WTC II), becker, buxtehude, lully, "
                          "… ★ LICENSE MISMATCH reported-not-accepted: the LICENSE file is CC-BY-NC-SA-4.0, NOT the record's "
                          "'CC BY 4.0' — the NC clause matters for any commercial use (T-32); research mirroring unaffected. "
                          "OVERLAP by work: MCMA's bach_js WTC I/II + inventions overlap the WiR WTC-I interior slice (24) + "
                          "the algomus bach-wtc-i fugue labels; recorded, NOT wired.",
        "notes": "Acquisition round (cc_acquisition_round_report.md). 475 .mxl; split 153/239/83 verified. CC-BY-NC-SA-4.0 (record said CC-BY — corrected). Held-out.",
    })
    r.append({
        "name": "vocsep_ijcai2023", "container": "manoskary/vocsep_ijcai2023",
        "content": "Voice Separation as Link Prediction (Karystinaios et al., IJCAI 2023): a heterogeneous-GNN "
                   "voice-separation model. The repo ships CODE; its ~1,054-graph note-collection is BUILT AT RUNTIME "
                   "from external score sources (Bach 370 Chorales, Haydn + Mozart string quartets, MCMA)",
        "pieces": 1054, "annotated_pieces": 1054, "gt_type": "voice", "gt_layers": ["voice"],
        "annotation_standard": "note-graph GT: one node per note, voice-link edges (consecutive-in-same-voice); built by "
                               "the loaders from engraved-notation voices",
        "score_format": "code (Python); graphs built from fetched .krn/MusicXML", "alignment": "score-derived (engraving voices)",
        "license_class": "MIT", "distribution": "hash-pin-only", "tier": "C", "status": "onboarded",
        "split": "held-out", "provenance_url": "https://github.com/manoskary/vocsep_ijcai2023",
        "pinned_commit": _corpora_sha("corpora/gt/vocsep_ijcai2023"),
        "needs_coverage": "N9 (stream/voice-separation GT — the largest of the three N9 beds by graph count). VERIFIED at "
                          "data: the repo ships CODE (vocsep/ package), NOT committed graphs — vocsep/data/datasets/ has the "
                          "loaders bach_chorales.py (url=github.com/craigsapp/bach-370-chorales), haydn_string_quartets.py, "
                          "mozart_string_quartets.py, mcma.py; the ~1,054-graph collection is BUILT AT RUNTIME from those. PIN "
                          "= the code repo; the source scores are fetched/held separately. ★ LICENSE MISMATCH reported-not-"
                          "accepted: the LICENSE file is MIT (Copyright 2023 Emmanouil Karystinaios), NOT the record's "
                          "'unstated' — vocsep IS MIT-licensed. CAVEAT (record §1): labels are notation-derived (engraving "
                          "voices) — weaker as an inference GT than de-novo stream annotation, except the WTC fugues (which "
                          "arrive via the MCMA dependency). CONTENT NOTE: the committed loaders are chorales/Haydn-SQ/Mozart-SQ/"
                          "MCMA — the record's 'Inventions/WTC' arrive through MCMA (the README results table reports Inventions/"
                          "WTC I/WTC II). DEDUPE: shares source material with our MCMA clone + the held Bach chorales.",
        "notes": "Acquisition round (cc_acquisition_round_report.md). Code repo pinned; 1054 graphs built at runtime from bach-370-chorales + Haydn/Mozart SQ + MCMA. MIT (record said unstated — corrected). Held-out.",
    })
    r.append({
        "name": "mikrokosmos_difficulty", "container": "PRamoneda/Mikrokosmos-difficulty",
        "content": "Bartok Mikrokosmos with expert difficulty labels (Ramoneda et al.): the 147 Mikrokosmos pieces "
                   "in MusicXML, each carrying a Henle-derived difficulty label (the difficulty-classification benchmark)",
        "pieces": 147, "annotated_pieces": 147, "gt_type": "difficulty", "gt_layers": ["difficulty"],
        "annotation_standard": "per-piece difficulty label (henle_difficulty in metadata; 3-class classification target) + "
                               "cross-validation splits.json; metadata JSONs (bartok/books/henle) + mikrokosmos_metadata.csv",
        "score_format": "MusicXML (.xml)", "alignment": "n/a (whole-piece label)",
        "license_class": "unclear (no LICENSE file)", "distribution": "hash-pin-only", "tier": "C", "status": "onboarded",
        "split": "held-out", "provenance_url": "https://github.com/PRamoneda/Mikrokosmos-difficulty",
        "pinned_commit": _corpora_sha("corpora/gt/Mikrokosmos-difficulty"),
        "needs_coverage": "★ N14 PRIMARY (difficulty/grade labels — the OPEN, symbolic-score half; consumer T-32). VERIFIED at "
                          "data: 147 .xml MusicXML (matches the record's 147); metadata/mikrokosmos_metadata.csv carries "
                          "henle_difficulty (e.g. 'Piano 1 easy') as the label source; splits.json = CV folds; metadata JSONs "
                          "bartok/books/henle. NO LICENSE FILE (matches record §3) → hash-pin-only. T-32 CAVEAT (rides the "
                          "product-tool register): a research-validation label source, research-only at origin like every real "
                          "N14 source; a COMMERCIAL grading feature needs a license path. DEDUPE: disjoint from all held "
                          "repertoire GT (Bartok Mikrokosmos, not in the DLC/WiR/chorale sets).",
        "notes": "Acquisition round (cc_acquisition_round_report.md). 147 MusicXML; henle-difficulty 3-class labels. No license file. Held-out.",
    })
    r.append({
        "name": "guitarset", "container": "Zenodo 10.5281/zenodo.3371780 (GuitarSet annotation artifact)",
        "content": "GuitarSet (Xi et al., ISMIR 2018): 360 guitar excerpts with rich JAMS annotations — instructed-chart "
                   "chord symbols vs performed comping, per-string MIDI notes, beats, keys. The ANNOTATION artifact only "
                   "(the audio artifacts are NOT our material)",
        "pieces": 360, "annotated_pieces": 360, "gt_type": "chords", "gt_layers": ["chords-instructed", "chords-performed", "notes", "beats", "key"],
        "annotation_standard": "JAMS (per excerpt: chord (instructed) + chord (performed), note_midi per string, beat_position, key_mode)",
        "score_format": "JAMS (.jams; symbolic annotation over audio)", "alignment": "onset-timed (over the audio recordings)",
        "license_class": "CC-BY-4.0", "distribution": "hash-pin-only", "tier": "J", "status": "onboarded",
        "split": "held-out", "provenance_url": "https://zenodo.org/records/3371780",
        "pinned_commit": _file_sha256("corpora/gt/guitarset/annotation.zip"),
        "needs_coverage": "N12 (realized-texture chord symbols — the small CLEAN pair set: instructed CHART chord vs "
                          "performed polyphonic COMPING, the exact symbol-vs-realization contrast). N5-adj (key_mode). VERIFIED "
                          "at data: annotation.zip = 39,132,574 bytes (matches Zenodo), sha256-pinned (pinnable-source rule; "
                          "non-git artifact); 360 .jams (matches the record's 360). Excerpt names encode style/tempo/key + "
                          "comp|solo (e.g. 03_SS1-100-C#_comp.jams, 04_Jazz2-110-Bb_solo.jams). ANNOTATION-ONLY: the 4 audio "
                          "zips (mono-mic 657 MB, mono-pickup-mix 683 MB, hex-pickup original 3.21 GB / debleeded 3.61 GB) are "
                          "NOT our material — their URLs are recorded, none downloaded. CAVEAT: audio-domain (JAMS over "
                          "recordings), so the chord/comping contrast is the value, not an engraved-score bed.",
        "notes": "Acquisition round (cc_acquisition_round_report.md). annotation.zip sha256-pinned; 360 jams. CC-BY-4.0. Audio not downloaded. Held-out.",
    })
    r.append({
        "name": "batik_plays_mozart", "container": "huispaty/batik_plays_mozart",
        "content": "Batik-plays-Mozart (Hu & Widmer 2023): 12 complete Mozart piano sonatas (36 movements) performed on "
                   "a computer-monitored Bösendorfer, note-aligned to the New Mozart Edition scores, with the DCML "
                   "'Annotated Mozart Sonatas' harmony/cadence/phrase annotations aligned to the score parts",
        "pieces": 36, "annotated_pieces": 36, "gt_type": "rn", "gt_layers": ["harmony", "cadence", "phrase", "match", "trill-mark"],
        "annotation_standard": "per-movement score-part CSVs (_spart_harmony.csv globalkey/localkey/numeral/chord_type, "
                               "_spart_cadence.csv, _spart_phrases.csv) + partitura .match performance-score alignment (snote↔note, "
                               "trill-mark attribute on score notes, insertion lines for performed notes)",
        "score_format": "MusicXML scores + MIDI performances + .match alignments + annotation CSVs", "alignment": "score-aligned + performance-aligned",
        "license_class": "unclear (no LICENSE file)", "distribution": "hash-pin-only", "tier": "C", "status": "onboarded",
        "split": "held-out", "provenance_url": "https://github.com/huispaty/batik_plays_mozart",
        "pinned_commit": _corpora_sha("corpora/gt/batik_plays_mozart"),
        "needs_coverage": "★ MULTI-NEED (the record §2 star). N1 (harmony RN — _spart_harmony.csv carries full DCML columns "
                          "globalkey/localkey/chord/numeral/chord_type/chord_label) + N4 (cadence — _spart_cadence.csv) over 12 "
                          "Mozart sonatas / 36 movements. N13-partial (ornament realization): the .match files anchor score "
                          "notes bearing the `trill-mark` attribute (VERIFIED: kv279_1.match has 49 trill-mark snotes + 163 "
                          "insertion lines) to performed insertion notes → trill realizations are RECOVERABLE by a grouping "
                          "heuristic, NOT shipped as labeled pairs (structure VERIFIED on one file; NO extraction built, per "
                          "the dispatch). N15-adj (performance timing, out of corpus scope). VERIFIED at data: 36 scores (12 "
                          "sonatas × 3 mvts), score_parts_annotated/ CSVs present; the annotations/ dir is an UNPOPULATED git "
                          "SUBMODULE (the upstream DCML Annotated Mozart Sonatas — not fetched by a plain clone; the "
                          "materialized annotations live in score_parts_annotated/). NO LICENSE FILE (matches record §2) → "
                          "hash-pin-only. ⚠ OVERLAP: the harmony/cadence GT = the DCML Annotated Mozart Sonatas = our held "
                          "mozart_piano_sonatas (DLC) + the WiR Mozart RN — recorded, NOT wired/diffed against the gate.",
        "notes": "Acquisition round (cc_acquisition_round_report.md). 36 movements; harmony/cadence/phrase CSVs + .match; trill-mark structure verified (kv279_1). annotations/ = empty submodule. No license file. Held-out.",
    })
    r.append({
        "name": "cipi", "container": "Zenodo 10.5281/zenodo.8037327 (Ramoneda et al., CIPI)",
        "content": "'Can I Play It?' (CIPI): 652 classical-piano pieces with expert-verified Henle 1–9 difficulty "
                   "levels; MusicXML included — the largest expert-verified symbolic difficulty set",
        "pieces": 652, "annotated_pieces": 652, "gt_type": "difficulty", "gt_layers": ["difficulty"],
        "annotation_standard": "per-piece Henle 1–9 difficulty level (expert-verified); MusicXML scores",
        "score_format": "MusicXML", "alignment": "n/a (whole-piece label)",
        "license_class": "unclear (research-only, gated)", "distribution": "hash-pin-only", "tier": "C", "status": "gated",
        "split": "held-out", "provenance_url": "https://zenodo.org/records/8037327", "pinned_commit": None,
        "needs_coverage": "★ N14 PRIMARY (difficulty/grade GT — the LARGEST expert-verified symbolic set, Henle 1–9, MusicXML "
                          "included; consumer T-32). GATED: Zenodo restricted-access, research-only — requires a request-access "
                          "form (USER ACTION pending, per the disposition). Not obtainable in a non-interactive session; access "
                          "path recorded. Mikrokosmos (onboarded) is the open committable N14 slice; CIPI lands on access grant. "
                          "T-32 CAVEAT (product-tool register): research-only at origin — commercial grading needs a license path.",
        "notes": "Acquisition round (cc_acquisition_round_report.md). Gated (Zenodo request-access; user form pending). Held-out.",
    })
    r.append({
        "name": "psyllabus", "container": "Zenodo 10.5281/zenodo.14794592 (PSyllabus)",
        "content": "PSyllabus: 7,901 piano recordings labeled on a unified 11-level difficulty scale distilled from real "
                   "exam-board syllabi (ABRSM/RCM/Trinity…). NO symbolic scores (audio + MIDI only)",
        "pieces": 7901, "annotated_pieces": 7901, "gt_type": "difficulty", "gt_layers": ["difficulty"],
        "annotation_standard": "per-recording 11-level difficulty label (exam-board-syllabus-derived)",
        "score_format": "audio + MIDI (NO symbolic score)", "alignment": "n/a (whole-recording label)",
        "license_class": "unclear (CC-BY badge but 'research use only' text)", "distribution": "hash-pin-only", "tier": "C",
        "status": "recorded", "split": "held-out", "provenance_url": "https://zenodo.org/records/14794592", "pinned_commit": None,
        "needs_coverage": "N14-adj (difficulty labels at the largest scale + the richest exam-board provenance, but NO SYMBOLIC "
                          "SCORES — audio/MIDI only, so not directly usable as a score-difficulty GT; consumer T-32). RECORDED "
                          "(no clone): the label taxonomy + provenance are the value; the missing scores make it adjacent, not "
                          "primary. T-32 CAVEAT: research-only text at origin. Full needs row so intake scoring exists if a "
                          "score-bearing derivative appears.",
        "notes": "Acquisition round (cc_acquisition_round_report.md). Recorded (7,901 recordings, no symbolic scores). Held-out.",
    })
    # --- inventory of already-held material (no new clone) ---
    r.append({
        "name": "choco_jazz_corpus_slice", "container": "smashub/choco :: partitions/jazz-corpus",
        "content": "Granroth-Wilding & Steedman Jazz Corpus (harmonic-FUNCTION analyses of jazz standards) — "
                   "the ChoCo partition (already held under corpora/ship/choco)",
        "pieces": 76, "annotated_pieces": 160, "gt_type": "chords", "gt_layers": ["chords", "function"],
        "annotation_standard": "JAMS (ChoCo-normalized)", "score_format": "JAMS (chords-only)", "alignment": "chords-only",
        "license_class": "CC-BY", "distribution": "hash-pin-only", "tier": "J", "status": "inventory",
        "split": "held-out", "provenance_url": "https://github.com/smashub/choco",
        "pinned_commit": _corpora_sha("corpora/ship/choco"),
        "needs_coverage": "N3 (rare harmonic-FUNCTION GT for jazz — the census's 76-piece function set). INVENTORIED "
                          "in the pinned ChoCo clone: partitions/jazz-corpus = 160 .jams (choco/jams + jams-converted). "
                          "Chords-only (no engraved score) — research-tier. DEDUPE: a ChoCo partition, not a new "
                          "acquisition; the native MCR/Steedman source is the upstream.",
        "notes": "Wave-3 inventory of already-held ChoCo (cc_corpus_wave3_report.md). 160 jams in the slice. Held-out.",
    })
    r.append({
        "name": "choco_weimar_slice", "container": "smashub/choco :: partitions/weimar",
        "content": "Weimar Jazz Database chord slice — the ChoCo partition (already held under corpora/ship/choco)",
        "pieces": 456, "annotated_pieces": 916, "gt_type": "chords", "gt_layers": ["chords"],
        "annotation_standard": "JAMS (ChoCo-normalized)", "score_format": "JAMS (chords-only)", "alignment": "chords-only",
        "license_class": "ODbL-1.0", "distribution": "hash-pin-only", "tier": "J", "status": "inventory",
        "split": "held-out", "provenance_url": "https://github.com/smashub/choco",
        "pinned_commit": _corpora_sha("corpora/ship/choco"),
        "needs_coverage": "N3-adj (jazz chord slice). INVENTORIED: partitions/weimar = 916 .jams. DEDUPE: the "
                          "chord-only re-encoding of the native WJD (weimar_jazz_database row) — the native SQLite adds "
                          "the phrase/sections/beat layers this slice drops; use the native for N4/N16.",
        "notes": "Wave-3 inventory of already-held ChoCo (cc_corpus_wave3_report.md). 916 jams in the slice. Held-out.",
    })
    r.append({
        "name": "wir_interior_inventory", "container": "MarkGotham/When-in-Rome (interior, already pinned)",
        "content": "Per-slice inventory of the pinned When-in-Rome clone (tools/dcml/when_in_rome @ aa7539f1) — "
                   "exposure, NOT a new acquisition",
        "pieces": None, "annotated_pieces": None, "gt_type": "rn", "gt_layers": ["rn", "key"],
        "annotation_standard": "RomanText analysis.txt (+ analysis_B.txt second annotator); Analyst-line provenance",
        "score_format": "score.mxl + analysis.txt", "alignment": "score-aligned",
        "license_class": "CC-BY", "distribution": "hash-pin-only", "tier": "G", "status": "inventory",
        "split": "dev", "provenance_url": "https://github.com/MarkGotham/When-in-Rome",
        "pinned_commit": _corpora_sha("tools/dcml/when_in_rome"),
        "needs_coverage": "N1 N2 N4 N5 N16 — EXPOSURE (on-disk), not acquisition. VERIFIED per-slice at the pin "
                          "(genre-reorganized layout, NOT named TAVERN/KMT/... dirs): TAVERN = Variations_and_Grounds/"
                          "{Beethoven 17, Mozart 10} = 27 works, ALL with a second-annotator analysis_B.txt (the N2 "
                          "flagship dual set — 27 A/B pairs); HaydnSun = Quartets/Haydn = 32 analyses; BPS-FH = "
                          "Piano_Sonatas/Beethoven = 86 analyses; WTC-I = Keyboard_Other/Bach = 24 scores/31 analyses; "
                          "OpenScore-Lieder RN = 179 analyses; Piano_Sonatas/Mozart = 54. Analyst buckets across 1259 "
                          "analysis.txt: DCML 988 / Tymoczko 419 / Gotham 161 / TAVERN-Devaney 54 / BPS 32. "
                          "TYMOCZKO-vs-DCML dual-annotation OVERLAP (by composer/collection/movement key) = 0 (Tymoczko-only "
                          "420, DCML-only 494, BOTH 0): within WiR the two analyst sets are DISJOINT piece-sets — the only "
                          "co-located dual annotation is the 27 TAVERN A/B pairs. CORRECTION to the audit: KMT is NOT a "
                          "confirmed analyzed slice at this pin (Textbooks = 201 scores / 0 analysis.txt: Kostka/Reger/"
                          "Aldwell present as SCORES only, no RN) — flag for Cowork.",
        "notes": "Wave-3 read-only inventory (cc_corpus_wave3_report.md). No new clone; no re-pin; no reorganization. dev (WiR is the gate GT container).",
    })
    # --- gated / unavailable / walked / enumerated (access paths recorded) ---
    r.append({
        "name": "ewld", "container": "Zenodo 10.5281/zenodo.1476555 (Simonetta et al. 2018)",
        "content": "Enhanced Wikifonia Leadsheet Dataset: ~5,000+ MusicXML lead sheets (melody+chords+metadata) — "
                   "the full superset of OpenEWLD",
        "pieces": 5000, "annotated_pieces": 5000, "gt_type": "chords", "gt_layers": ["chords", "melody"],
        "annotation_standard": "MusicXML harmony+melody + metadata", "score_format": "MusicXML", "alignment": "score-aligned",
        "license_class": "unclear", "distribution": "hash-pin-only", "tier": "J", "status": "gated",
        "split": "held-out", "provenance_url": "https://zenodo.org/records/1476555", "pinned_commit": None,
        "needs_coverage": "N12 / N3-adj (symbol+melody leadsheets, the ~5,000 superset). GATED: Zenodo restricted-access "
                          "— requires a request-access form (name, institution, role, non-commercial statement, research "
                          "explanation). Not obtainable in a non-interactive session; access path recorded. The PD subset "
                          "OpenEWLD (486, onboarded) is the committable slice.",
        "notes": "Wave-3 (cc_corpus_wave3_report.md). Gated (Zenodo request-access); OpenEWLD is the PD subset. Held-out.",
    })
    r.append({
        "name": "hooktheory_full", "container": "m-a-p/HookTheory (Hugging Face)",
        "content": "Full HookTheory/TheoryTab research release: crowd lead sheets (melody+chords+key, RN-convertible) — "
                   "the full set behind the pinned wayne391/lead-sheet-dataset sample",
        "pieces": None, "annotated_pieces": None, "gt_type": "chords", "gt_layers": ["chords", "key", "melody"],
        "annotation_standard": "TheoryTab (key-relative)", "score_format": "symbolic (HF dataset)", "alignment": "score-aligned",
        "license_class": "CC-BY-NC", "distribution": "hash-pin-only", "tier": "J", "status": "gated",
        "split": "held-out", "provenance_url": "https://huggingface.co/datasets/m-a-p/HookTheory", "pinned_commit": None,
        "needs_coverage": "N3 (largest key-relative pop analysis GT); N5-adj (key); N12-adj (symbol+melody). GATED: HF "
                          "gated dataset — academic-affiliation gate + accept-conditions, CC-BY-NC-4.0, 112 GB; not "
                          "obtainable in a non-interactive session (matches the standing 'pending HF m-a-p/HookTheory "
                          "access' note). The sample entry (hooktheory_hlsd, wayne391/lead-sheet-dataset) stays as-is.",
        "notes": "Wave-3 (cc_corpus_wave3_report.md). Gated (HF academic access); sample kept in other_sources. Held-out.",
    })
    r.append({
        "name": "sears_haydn_cadences", "container": "Sears et al. 2018 (Haydn string-quartet cadences)",
        "content": "270 cadence tokens in 50 Haydn string-quartet expositions (1771-1803), TWO annotators, plus "
                   "key/mode/modulation/pivot annotations",
        "pieces": 50, "annotated_pieces": 50, "gt_type": "cadence", "gt_layers": ["cadence", "key", "modulation", "pivot"],
        "annotation_standard": "manual cadence + key/modulation/pivot annotations (two annotators)", "score_format": "symbolic + text (per literature)",
        "alignment": "score-aligned", "license_class": "unclear", "distribution": "hash-pin-only", "tier": "C",
        "status": "unavailable", "split": "held-out",
        "provenance_url": "https://doi.org/10.1177/1029864918763769", "pinned_commit": None,
        "needs_coverage": "N2 (dual-annotator disagreement) + N4 (cadence) + N5 (key/modulation/PIVOT) — a top multi-need "
                          "node. UNAVAILABLE: no public GitHub/Zenodo/OSF deposit found across targeted searches; widely "
                          "cited (Sears et al. 2018) but not openly deposited. Access = contact the authors (David Sears) "
                          "or check the paper's supplementary. Per-source failure = report line, not a wave STOP.",
        "notes": "Wave-3 (cc_corpus_wave3_report.md). No public deposit located; access path recorded. Held-out.",
    })
    r.append({
        "name": "gttm_database", "container": "gttm.jp (Hamanaka/Hirata/Tojo GTTM Database)",
        "content": "GTTM Database: ~300 melodies with grouping / metrical / time-span / prolongational trees "
                   "(MusicXML + XML tree encodings)",
        "pieces": 300, "annotated_pieces": 300, "gt_type": "tree", "gt_layers": ["grouping", "metrical", "time-span", "prolongational", "harmonic"],
        "annotation_standard": "MusicXML (MSC) + GTTM XML (GPR/MPR/TS/PR/HM)", "score_format": "MusicXML + XML trees",
        "alignment": "score-aligned", "license_class": "unclear", "distribution": "hash-pin-only", "tier": "C",
        "status": "recorded", "split": "held-out", "provenance_url": "https://gttm.jp/gttm/database/", "pinned_commit": None,
        "needs_coverage": "N6 (melodic-phrase — grouping trees over monophonic melodies) + N4 (metrical/grouping "
                          "boundaries) + N11-melodic (time-span trees — melodic-side hierarchy GT). LOCATED, NOT PINNED: "
                          "distributed as ~157+ per-piece ZIP archives at gttm.jp/gttm/wp-content/uploads/2015/12/ (numbered), "
                          "NO single bulk artifact, NO explicit license shown — per the pinnable-source rule (no stable "
                          "artifact) the access path is recorded and mass-download deferred (license unclear about mirroring).",
        "notes": "Wave-3 (cc_corpus_wave3_report.md). No single stable artifact + license unclear -> options recorded, not downloaded. Held-out.",
    })
    r.append({
        "name": "dcmlab_figured_bass", "container": "DCMLab/figured-bass",
        "content": "WALKED (census §7 residual promotion): a single Python script that GENERATES chords from a "
                   "figured-bass specification — a realization TOOL, not a figured-bass GT corpus",
        "pieces": 0, "annotated_pieces": 0, "gt_type": "none", "gt_layers": [],
        "annotation_standard": "n/a (figured-bass.py realization algorithm; no dataset)", "score_format": "n/a (code)",
        "alignment": "none", "license_class": "unclear", "distribution": "hash-pin-only", "tier": "X", "status": "walked",
        "split": "held-out", "provenance_url": "https://github.com/DCMLab/figured-bass",
        "pinned_commit": _corpora_sha("corpora/gt/figured-bass"),
        "needs_coverage": "N10 — NEGATIVE (corrects the census §7 assumption). WALKED at data: the repo is ONE file "
                          "(figured-bass.py) + README — a bass-figure -> chord REALIZATION script (e.g. `-k 80 -n 5 9` -> "
                          "a realized triad), NOT a figured-bass ground-truth corpus. Does NOT serve N10 as a GT source; "
                          "the N10 sources are BCFB + the DLC figbass column. Recorded so it is never re-mistaken for GT.",
        "notes": "Wave-3 WALK (cc_corpus_wave3_report.md). Realization tool, not a corpus — §7->§1 promote with this finding. Held-out (n/a).",
    })
    r.append({
        "name": "humdrum_data_closure", "container": "humdrum-tools/humdrum-data (.lists manifest)",
        "content": "Enumeration record (CLONE NOTHING): the complete humdrum-data download manifest — the mechanical "
                   "closure of the census's craigsapp/KernScores partial",
        "pieces": None, "annotated_pieces": None, "gt_type": "none", "gt_layers": [],
        "annotation_standard": "n/a (repo manifest: .lists/LIST.txt, **ghname/**ghrepo columns)", "score_format": "n/a (enumeration)",
        "alignment": "none", "license_class": "mixed", "distribution": "enumeration-only", "tier": "S", "status": "enumerated",
        "split": "held-out", "provenance_url": "https://github.com/humdrum-tools/humdrum-data", "pinned_commit": None,
        "needs_coverage": "Tier S/X breadth (Humdrum **kern score collections). ENUMERATED from .lists/LIST.txt (nothing "
                          "cloned): 71 distinct repos across 16 GitHub orgs (821 file entries) — incl. craigsapp/* "
                          "(bach-370-chorales, beethoven/haydn/mozart/scarlatti sonatas, chopin-mazurkas), "
                          "josquin-research-project (22 composer repos), TassoInMusicProject, SEILSdataset, ccarh/essen "
                          "(already held as the Wave-2 phrase bed), Computational-Cognitive-Musicology-Lab/CoCoPops "
                          "(onboarded this wave), and DDMAL/Flexible_harmonic_chorale_annotations (a harmonic-chorale "
                          "annotation set = N1-residual). Closes the census's named craigsapp mechanical partial; "
                          "acquisition of individual sets is NOT this wave. Full list: cc_corpus_wave3_report.md.",
        "notes": "Wave-3 enumeration (cc_corpus_wave3_report.md). 71 repos / 16 orgs recorded; nothing cloned. Held-out (n/a).",
    })
    return r


def main() -> None:
    dlc = dlc_rows()
    other = nondlc_rows()
    beds = annotation_bed_rows()
    wave3 = wave3_rows()
    doc = {
        "_schema": "score_census_registry v2 (census §3 + CC corpus-wave1 dispatch 2026-07-02)",
        "_generated_by": "tools/build_score_census_registry.py (deterministic; re-run after any clone/pin change)",
        "_fields": ["name", "container", "content", "pieces", "annotated_pieces", "gt_type",
                    "gt_layers", "annotation_standard", "score_format", "alignment",
                    "license_class", "distribution", "tier", "status", "split",
                    "provenance_url", "pinned_commit", "notes",
                    "(wave3_sources add: needs_coverage — full-vector N1-N20 intake note per census §8c intake rule)"],
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
            "dcml_parser.py currently DROPS (reads only numeral/chord/keys) — see cc_corpus_wave1_report.md §4. "
            "CLARIFYING CLAUSE (audit-verified 2026-07-04, cowork_census_full_needs_audit.md §4): the `form` column "
            "is DCML chord-MORPHOLOGY (o/+/%/M — the label-grammar quality suffix), NOT form/section GT; N16 (form) is "
            "NOT covered by the DLC. The same TSVs also carry a `figbass` column (inversion figured-bass, N10) and a "
            "`pedal` column (pedal-point GT, N20); both were historically parser-dropped and are now EXPOSED as additive "
            "dcml_parser.DcmlRegion.figbass/pedal fields at the Wave-3 addendum (cc_wave3_addendum_report.md) — no "
            "consumer reads them yet (byte-identity proven), so the closure is exposure-only.",
            "Container = distant_listening_corpus has 40 submodules (census '41' was an overcount; verified from "
            ".gitmodules 2026-07-02).",
            "annotation_beds (Wave-2, cc_corpus_wave2_report.md): expert LABEL layers over scores (schema/texture) "
            "or a standalone phrase-marked melody bed, for validating axis-2 (voice leading). kind='annotation-bed'; "
            "extra fields kind/axis2_role/target_corpus/label_count. All held-out (never tuned against), hash-pin-only "
            "under gitignored corpora/annot/. They add labels over already-held scores (schema/texture over Mozart) or "
            "material outside the discovery views (Essen monophonic, no chords) — NOT analysis/gate corpora.",
            "wave3_sources (Wave-3, cc_corpus_wave3_report.md): jazz/pop GT (CoCoPops, OpenEWLD, WJD native, ChoCo "
            "jazz-corpus/weimar slices) + cadence/form/dual-annotator beds (algomus-data quartets+fugues, WiR interior "
            "inventory) + figured bass (BCFB; DCMLab/figured-bass WALKED = a realization TOOL not GT) + trees/reduction "
            "(schenker41, protovoice-annotations [the N9 gating inspection], GTTM) + plain-score stress (OpenScore "
            "Lieder/StringQuartets, ASAP) + gated/unavailable records (EWLD, HookTheory full, Sears Haydn) + the "
            "humdrum-data enumeration closure (71 repos, cloned nothing). Each row carries a `needs_coverage` note scored "
            "against the FULL vector N1-N20 (census §8c intake rule). All held-out (never tuned against); cloned beds are "
            "hash-pin-only under gitignored corpora/gt| corpora/plain/ (WJD pinned by sha256; non-git). status: onboarded|"
            "walked|inventory|gated|unavailable|recorded|enumerated.",
            "wave3 ADDENDUM (cc_wave3_addendum_report.md, 2026-07-04): two DDMAL direct pickups added to wave3_sources — "
            "key_modulation_dataset (KMT, the N5 upstream the Wave-3 correction named; 201 annotated Humdrum .krn across 5 "
            "textbooks; CC-BY-SA scores/MIT code) and flexible_harmonic_chorale_annotations (571 chorales, permutational "
            "multi-reading harmony in an R-package binary; GPLv3; RECORD-ONLY re the gate — 371 Bach chorales overlap the "
            "gate repertoire). Same addendum exposes the parser-dropped figbass/pedal columns (see the clarifying clause).",
            "ACQUISITION ROUND (cc_acquisition_round_report.md, 2026-07-04): the union-search-approved pickups "
            "(cowork_union_search_record.md §6, user-disposed) added to wave3_sources — N9 voice-separation beds "
            "piano_svsep (MIT code; GT graphs fetched at runtime from fosfrancesco/piano_corpora_dcml), mcma (475 .mxl, "
            "one-voice-per-track; CC-BY-NC-SA-4.0), vocsep_ijcai2023 (MIT; ~1,054 graphs built at runtime from "
            "bach-370-chorales + Haydn/Mozart SQ + MCMA); N14 mikrokosmos_difficulty (147 MusicXML, henle labels, no "
            "license); N12 guitarset (annotation.zip sha256-pinned, 360 .jams, CC-BY-4.0; audio not downloaded); "
            "multi-need batik_plays_mozart (36 Mozart-sonata movements — harmony/cadence/phrase CSVs N1/N4 + .match "
            "trill-mark structure N13-partial; no license); CIPI (gated, Zenodo request-access, user form pending) + "
            "PSyllabus (recorded, 7,901 recordings, no symbolic scores). TWO record license mismatches CORRECTED at the "
            "data (MCMA = CC-BY-NC-SA-4.0 not CC-BY; vocsep = MIT not unstated). The PDMX N12 <harmony> counting pass was "
            "ATTEMPTED + STOPPED (held form = metadata-only CSV; see the pdmx row's needs_coverage). New gt_type values "
            "this round: 'voice' (N9 voice-separation) and 'difficulty' (N14). All held-out; hash-pin-only.",
        ],
        "distant_listening_corpus": {
            "submodule_count": len(dlc),
            "onboarded": len(dlc),
            "members": dlc,
        },
        "other_sources": other,
        "annotation_beds": beds,
        "wave3_sources": wave3,
    }
    OUT.write_text(json.dumps(doc, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT}  DLC={len(dlc)} other={len(other)} beds={len(beds)} wave3={len(wave3)} "
          f"total={len(dlc)+len(other)+len(beds)+len(wave3)}")


if __name__ == "__main__":
    main()

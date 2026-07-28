#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# gen_decision_clusters.py — THE MECHANICAL CLUSTERING LAYER over the decision
# harvest (dispatch cc_instruction_decision_clustering.md).
#
# ONE TOOL PER CONCERN (#6): the harvest (gen_decision_harvest.py) FINDS candidate
# statements; this tool GROUPS them. It is a strict LAYER — it reads
# decision_candidates.json and never writes it, never merges two candidates into
# one record, never rewrites a candidate's text, never deletes a candidate, and
# never drops an occurrence because a similar one exists. Every cluster names
# every one of its members by candidate id, and every one of the harvest's
# candidates belongs to exactly one cluster (singletons included). --check proves
# that round-trip.
#
# NON-ADJUDICATIVE. It does not decide whether a candidate is really a decision,
# does not fill status, does not judge conformance, and does not name a
# supersession. The per-cluster representative it proposes is labelled "proposed
# representative", chosen by SOURCE AUTHORITY alone (never by length) — the
# adjudication pass decides.
#
# THE THREE GROUPING SIGNALS (the dispatch's, with their declared strengths):
#   (1) near-identical text  — the PRIMARY signal; it alone forms the clusters.
#   (2) shared evidence pointer — WEAKER; emitted as links BETWEEN clusters,
#       never merged into them.
#   (3) same date + same ratifier — WEAKEST; corroborating links only.
# Each grouping records the signal that produced it.
#
# Determinism: no wall-clock, no randomness. The MinHash permutations are derived
# from a fixed salt by SHA-256, so a re-run over the same pinned candidate list
# reproduces byte-identical output.

import argparse
import csv
import hashlib
import json
import os
import re
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CANDIDATES = os.path.join(HERE, "decision_candidates.json")

# ── Declared parameters (every one is reported in the manifest) ───────────────
#
# SIM_THRESHOLD — the Jaccard similarity (on word 3-gram shingles) at or above
# which two statements are proposed as the same decision.
#
# Justification for 0.80, and the risk asymmetry the dispatch sets:
#   * a WRONG MERGE is invisible afterwards and would corrupt the register;
#     an over-large cluster is merely untidy and the adjudication can split it.
#     The dispatch's operative instruction is therefore "when in doubt, do not
#     group", so the threshold is set on the CONSERVATIVE (high) side of the
#     near-duplicate range rather than the permissive side.
#   * 0.80 Jaccard over 3-gram shingles is the standard near-duplicate operating
#     point for shingled-document resemblance (Broder resemblance; web
#     near-duplicate detection conventionally runs 0.8-0.9). At 0.80 two texts
#     share four fifths of their word triples — restatement in near-identical
#     words, which is what the dispatch describes, not merely the same subject.
#   * The sweep at 0.70/0.75/0.85/0.90/0.95 is reported beside it so the effect
#     of moving the threshold is visible rather than asserted.
SIM_THRESHOLD = 0.80
SWEEP = [0.70, 0.75, 0.80, 0.85, 0.90, 0.95]

# Short statements are matched by EXACT normalized text only, never by
# similarity: a five-word heading shares 3-gram shingles with unrelated five-word
# headings, and grouping those would be exactly the doubt the dispatch says to
# resolve by not grouping.
MIN_TOKENS_FOR_SIMILARITY = 8
SHINGLE_W = 3

# MinHash + banded LSH: 256 permutations in 32 bands of 8 rows. The band
# configuration's 50%-probability point is (1/32)^(1/8) = 0.648, so a pair at the
# 0.80 operating threshold is generated as a candidate with probability
# 1-(1-0.80^8)^32 = 0.997, and at 0.70 with 0.87 — the sweep's two lowest rungs
# are therefore reported as LOWER BOUNDS, which is stated in the manifest.
N_HASH = 256
N_BANDS = 32
ROWS_PER_BAND = 8
# Arithmetic bound: shingle hashes are reduced to 31 bits and the multiplier to
# 32 bits, so (a*h + b) < 2^63 + 2^33 and the unsigned 64-bit product never
# wraps — the permutation is exact, not approximate.
HASH_PRIME = 4294967311          # the first prime above 2^32
PERM_SALT = b"decision-clusters/v1"

# Signal (2): an evidence pointer shared by more than this many clusters is too
# common to be a grouping signal (OI-207, CLAUDE.md and the like appear
# everywhere). Such pointers are still REPORTED, with their cluster counts, so
# nothing is hidden — they are simply not proposed as links.
EVIDENCE_LINK_MAX_CLUSTERS = 25
# Signal (3): same rule for a (date, ratifier) pair.
DATE_LINK_MAX_CLUSTERS = 25

# ── Source authority for the PROPOSED representative ──────────────────────────
# By source authority, never by length. The governing documents rank above the
# handoff and status files, and those above the Claude Code session reports,
# which are restatements by construction.
def authority_rank(rel):
    r = rel.replace("\\", "/")
    if r in ("CLAUDE.md", "ARCHITECTURE.md"):
        return 1                      # the governing documents
    if r.startswith("docs/"):
        return 2                      # the design/reference documents
    if r.startswith("cowork_") and not r.startswith("cowork_handoff"):
        return 2                      # the ratified cowork_* decision documents
    if r == "OPEN_ITEMS.md" or r.startswith("open_items/"):
        return 3                      # the open-items register
    if r.startswith("src/") or r.startswith("tools/"):
        return 4                      # a decision recorded at the site it governs
    if r in ("STATUS.md", "cowork_handoff.md", "DEFECT_TYPES.md"):
        return 5                      # the status and handoff files
    if r in ("STATUS_ARCHIVE.md", "cowork_handoff_archive.md"):
        return 6                      # their archives
    if r.startswith("cc_"):
        return 7                      # Claude Code session reports and dispatches
    return 8


AUTHORITY_REASON = {
    1: "governing document (CLAUDE.md / ARCHITECTURE.md)",
    2: "design or decision document (docs/ or cowork_*)",
    3: "the open-items register",
    4: "a comment at the code site the decision governs",
    5: "status or handoff file",
    6: "archived status or handoff file",
    7: "Claude Code session report or dispatch (a restatement by construction)",
    8: "other",
}

# ── The boilerplate bucket ────────────────────────────────────────────────────
# Phrases that recur across documents as SCAFFOLDING or as DISPATCH INSTRUCTIONS
# rather than as statements about the project. They are KEPT, never deleted —
# bucketed and labelled so the adjudication can confirm the judgment cheaply,
# class by class, instead of one occurrence at a time.
#
# Every class requires RECURRENCE, so a one-off statement is never bucketed on
# wording alone.
#
# Every pattern below is written against the NORMALIZED text (lower case, no
# punctuation, no Markdown), because that is what it is matched against.
BOILERPLATE_INSTRUCTION = [
    ("push_target", r"push\w*\s.{0,60}\bupstream\b|\bupstream\b.{0,40}\b(?:never|disabled|untouched)|\bpush to origin only\b|\borigin only\b|\bfork only\b"),
    ("stop_condition_line", r"→\s*stop\b|\bstop immediately\b|\bstop conditions?\b|\bstop surface\b"),
    ("do_not_push", r"^do not push\b"),
    ("read_only_scope", r"\bno src change\b|\bno behaviou?r change\b|\bthis instruction is read only\b"),
    ("self_check_line", r"\bself check before reporting\b|\bstanding self check\b"),
    ("withheld_files", r"\bdo not read the withheld files\b"),
    ("no_mid_flight", r"\bno mid flight steering\b"),
    ("commits_per_class", r"\bcommits? per change class\b"),
    ("prepush_hook", r"\bpre push hook should pass\b"),
]
BOILERPLATE_MIN_OCCURRENCES = 2
BOILERPLATE_SCAFFOLD_MIN_OCCURRENCES = 3
BOILERPLATE_MEMBER_FRACTION = 0.60
#
# WHAT IS DELIBERATELY *NOT* BUCKETED, and why. Bucketing is itself a form of
# grouping, so the dispatch's "when in doubt, do not group" applies to it:
#   * a bold run-in line (a whole paragraph in bold) is NOT treated as
#     scaffolding, even when it recurs, because in this repository such a line
#     often carries a rule — the open-items register's
#     "Section C — Owned by Stage-5 (precision phase — do NOT fix earlier, #8)"
#     is a live ownership rule, not a navigation label;
#   * the open-items detail-file banner ("STATUS IS AUTHORITATIVE IN THE
#     INDEX …") is NOT bucketed either: it states a rule about the register
#     rather than instructing a session, which is the line the dispatch draws.
# Both therefore appear as ordinary clusters, where they are visible.

# ── Internal-divergence triggers (flag only — never resolved here) ────────────
STATUS_CHANGE_WORDS = [
    "superseded", "supersedes", "overturned", "withdrawn", "withdrew", "reverted",
    "shelved", "falsified", "refuted", "retired", "no longer", "rescinded",
]
# Opposed wording, matched with word boundaries so the flag stays precise. The
# ON/OFF pair is matched CASE-SENSITIVELY in capitals, which is how this
# repository writes a flag's default.
POLARITY_PAIRS = [
    (r"\bdefault(?:s|ed)?[- ]?(?:to )?ON\b", r"\bdefault(?:s|ed)?[- ]?(?:to )?OFF\b", True),
    (r"\bON\b", r"\bOFF\b", True),
    (r"\btrue\b", r"\bfalse\b", False),
    (r"\benabled\b", r"\bdisabled\b", False),
    (r"\bincreas(?:e|es|ed|ing)\b", r"\bdecreas(?:e|es|ed|ing)\b", False),
]
_NUM = re.compile(r"(?<![\w.])\d[\d,]*(?:\.\d+)?\s?%?")
_DATEISH = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
# A leading list marker ("3. ", "5) ") or numbered heading ("## 6. ") is layout,
# not content: the same statement appearing as item 3 in one dispatch and item 5
# in another, or as section 6 of one report and section 5 of another, is not a
# disagreement about anything.
_LISTNUM = re.compile(r"^\s*(?:#{1,6}\s+)?\d+[.)]\s", re.MULTILINE)


# ── Normalization for clustering ──────────────────────────────────────────────
_STRIP_CHARS = re.compile(r"[`*_#>|~\[\]()<>{}\"'!?;:,.\\/—–\-]+")


def cluster_norm(text):
    """Whitespace, case, punctuation and Markdown formatting removed. Words and
    digits are kept — a number is content, and a cluster whose members quote
    different numbers is exactly what the divergence flag must catch."""
    t = text.lower()
    t = _STRIP_CHARS.sub(" ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def shingles(tokens, w=SHINGLE_W):
    if len(tokens) < w:
        return {" ".join(tokens)} if tokens else set()
    return {" ".join(tokens[i:i + w]) for i in range(len(tokens) - w + 1)}


def h32(s):
    """31-bit shingle hash (see the arithmetic bound at HASH_PRIME)."""
    return int.from_bytes(
        hashlib.blake2b(s.encode("utf-8"), digest_size=4).digest(), "big") & 0x7FFFFFFF


def permutations(n):
    a = np.empty(n, dtype=np.uint64)
    b = np.empty(n, dtype=np.uint64)
    for i in range(n):
        d = hashlib.sha256(PERM_SALT + b":%d" % i).digest()
        a[i] = int.from_bytes(d[:8], "big") % ((1 << 32) - 1) + 1
        b[i] = int.from_bytes(d[8:16], "big") % HASH_PRIME
    return a, b


# ── Union-find ────────────────────────────────────────────────────────────────
class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if rx < ry:
                self.p[ry] = rx
            else:
                self.p[rx] = ry


# ── The clustering ────────────────────────────────────────────────────────────
def candidates_sha256():
    h = hashlib.sha256()
    with open(CANDIDATES, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_candidates():
    with open(CANDIDATES, encoding="utf-8") as fh:
        blob = json.load(fh)
    return blob["header"], blob["candidates"]


def primary_location(c):
    o = c["source_occurrences"][0]
    return o["file"], o["line"]


def build_units(cands):
    """Collapse candidates onto DISTINCT normalized texts. Nothing is dropped:
    each unit carries the full id list of the candidates that share its text."""
    units = {}
    order = []
    for c in cands:
        n = cluster_norm(c["decision_text"])
        if n not in units:
            units[n] = {"norm": n, "ids": [], "toks": n.split()}
            order.append(n)
        units[n]["ids"].append(c["id"])
    return [units[n] for n in order]


def lsh_candidate_pairs(units, report):
    """Return the verified pair list [(i, j, similarity)] for units long enough
    to be matched by similarity. Short units are matched by exact text only, so
    they simply produce no pairs here."""
    idx_long = [i for i, u in enumerate(units)
                if len(u["toks"]) >= MIN_TOKENS_FOR_SIMILARITY]
    report["units_total"] = len(units)
    report["units_similarity_eligible"] = len(idx_long)
    report["units_exact_only"] = len(units) - len(idx_long)
    if not idx_long:
        return []

    shingle_sets = {}
    for i in idx_long:
        sh = shingles(units[i]["toks"])
        shingle_sets[i] = frozenset(h32(s) for s in sh)

    a, b = permutations(N_HASH)
    sig = np.empty((len(idx_long), N_HASH), dtype=np.uint64)
    for row, i in enumerate(idx_long):
        h = np.fromiter(shingle_sets[i], dtype=np.uint64,
                        count=len(shingle_sets[i]))
        # (a*h + b) mod HASH_PRIME, minimum over the shingles, per permutation
        prod = (np.multiply.outer(a, h) + b[:, None]) % HASH_PRIME
        sig[row] = prod.min(axis=1)

    pairs = set()
    for band in range(N_BANDS):
        lo = band * ROWS_PER_BAND
        hi = lo + ROWS_PER_BAND
        buckets = {}
        for row in range(len(idx_long)):
            key = sig[row, lo:hi].tobytes()
            buckets.setdefault(key, []).append(row)
        for members in buckets.values():
            if len(members) < 2:
                continue
            for x in range(len(members)):
                for y in range(x + 1, len(members)):
                    pairs.add((members[x], members[y]))
    report["lsh_candidate_pairs"] = len(pairs)

    verified = []
    lowest = min(SWEEP)
    for (rx, ry) in sorted(pairs):
        i, j = idx_long[rx], idx_long[ry]
        A, B = shingle_sets[i], shingle_sets[j]
        inter = len(A & B)
        if inter == 0:
            continue
        sim = inter / float(len(A | B))
        if sim >= lowest:
            verified.append((i, j, sim))
    verified.sort(key=lambda t: (-t[2], t[0], t[1]))
    report["verified_pairs_at_sweep_floor"] = len(verified)
    return verified


def exact_pairs_bruteforce(units, floor):
    """The ESTABLISHMENT reference (#19): the EXACT similarity of every pair of
    similarity-eligible units that shares at least one shingle. A pair sharing
    none has similarity 0, so this enumeration is complete — it is a brute-force
    ground truth for the MinHash+LSH path, not an approximation of it.

    Computed by sparse boolean matrix multiplication: rows are units, columns are
    shingles, so (X @ X.T)[i][j] is |A ∩ B| exactly."""
    from scipy import sparse

    idx_long = [i for i, u in enumerate(units)
                if len(u["toks"]) >= MIN_TOKENS_FOR_SIMILARITY]
    vocab = {}
    rows, cols = [], []
    sizes = np.zeros(len(idx_long), dtype=np.int64)
    for r, i in enumerate(idx_long):
        sh = {h32(s) for s in shingles(units[i]["toks"])}
        sizes[r] = len(sh)
        for s in sh:
            c = vocab.get(s)
            if c is None:
                c = len(vocab)
                vocab[s] = c
            rows.append(r)
            cols.append(c)
    X = sparse.csr_matrix((np.ones(len(rows), dtype=np.int32), (rows, cols)),
                          shape=(len(idx_long), len(vocab)))
    Xt = X.T.tocsr()
    out = []
    CH = 400
    for start in range(0, len(idx_long), CH):
        end = min(start + CH, len(idx_long))
        P = (X[start:end] @ Xt).tocoo()
        for a, b, inter in zip(P.row, P.col, P.data):
            r = start + a
            if b <= r:
                continue
            sim = inter / float(sizes[r] + sizes[b] - inter)
            if sim >= floor:
                out.append((idx_long[r], idx_long[b], float(sim)))
    out.sort(key=lambda t: (-t[2], t[0], t[1]))
    return out, len(idx_long), len(vocab)


def cluster_at(units, verified, threshold):
    uf = UF(len(units))
    for (i, j, sim) in verified:
        if sim >= threshold:
            uf.union(i, j)
    groups = {}
    for i in range(len(units)):
        groups.setdefault(uf.find(i), []).append(i)
    return groups


# ── Cluster annotation ────────────────────────────────────────────────────────
def numbers_in(text):
    t = _LISTNUM.sub(" ", text)
    t = _DATEISH.sub(" ", t)
    return frozenset(m.group(0).replace(",", "").strip() for m in _NUM.finditer(t))


def divergence(members_texts):
    """MECHANICAL flags only — the cluster is marked, never resolved. Each
    trigger is named so the adjudication can weigh it; the differing-numbers
    trigger is the softest of the three and is counted separately."""
    triggers = []
    if len(members_texts) < 2:
        return triggers
    lows = [t.lower() for t in members_texts]

    numsets = {numbers_in(t) for t in members_texts}
    if len(numsets) > 1:
        triggers.append("numbers differ between members")

    with_status = sum(1 for t in lows if any(w in t for w in STATUS_CHANGE_WORDS))
    if 0 < with_status < len(lows):
        triggers.append("some members carry a status-changing word, others do not")

    for (p, q, case_sensitive) in POLARITY_PAIRS:
        flags = 0 if case_sensitive else re.IGNORECASE
        rp, rq = re.compile(p, flags), re.compile(q, flags)
        src = members_texts if case_sensitive else lows
        # The members must SPLIT on the opposed words. A single member that
        # contains both (a sentence describing a divergence — "batch passes
        # true, the bridge defaults false") is not a disagreement between
        # members, and must not be flagged as one.
        only_p = any(rp.search(t) and not rq.search(t) for t in src)
        only_q = any(rq.search(t) and not rp.search(t) for t in src)
        if only_p and only_q:
            triggers.append("members split on opposed wording (%s vs %s)" % (p, q))
            break
    return triggers


def boilerplate_class(cluster_members, total_occurrences):
    """Returns (class_name, matched_rule) or (None, None). Every class requires
    recurrence, so a one-off statement is never bucketed on wording alone."""
    kinds = [m["unit_kind"] for m in cluster_members]
    texts = [cluster_norm(m["decision_text"]) for m in cluster_members]
    n = len(cluster_members)

    scaffold = sum(1 for k in kinds if k in ("heading", "table_row"))
    if (total_occurrences >= BOILERPLATE_SCAFFOLD_MIN_OCCURRENCES
            and scaffold >= BOILERPLATE_MEMBER_FRACTION * n):
        return "document_scaffolding", "heading or table header row, recurring"

    for (name, rx) in BOILERPLATE_INSTRUCTION:
        rxc = re.compile(rx, re.IGNORECASE)
        hit = sum(1 for t in texts if rxc.search(t))
        if (total_occurrences >= BOILERPLATE_MIN_OCCURRENCES
                and hit >= BOILERPLATE_MEMBER_FRACTION * n):
            return "dispatch_instruction", name

    return None, None


def choose_representative(members):
    """PROPOSED representative — by source authority, never by length."""
    def key(m):
        f, ln = primary_location(m)
        return (
            authority_rank(f),
            0 if m["tier"] == "high" else 1,
            0 if m["ratified_by"] else 1,
            m["date"] or "9999-99-99",
            m["id"],
        )
    return sorted(members, key=key)[0]


def build_clusters(units, groups, by_id, verified_lookup):
    clusters = []
    for root, unit_idxs in groups.items():
        ids = []
        for ui in unit_idxs:
            ids.extend(units[ui]["ids"])
        ids.sort()
        members = [by_id[i] for i in ids]
        texts = [m["decision_text"] for m in members]
        files = sorted({primary_location(m)[0] for m in members})
        rep = choose_representative(members)
        rep_file, rep_line = primary_location(rep)

        # Within-cluster cohesion: the lowest similarity among the pairs of this
        # cluster's distinct texts that were actually computed (1.0 when the
        # cluster is one text repeated verbatim; below the threshold only when
        # transitive chaining linked the extremes). It is an UPPER BOUND on the
        # true minimum: a pair below the sweep floor is not in the pair list at
        # all, so a chained cluster's extremes may be further apart than this
        # says. Enough to FLAG chaining, which is all it is used for.
        cohesion = 1.0
        chained = False
        if len(unit_idxs) > 1:
            sims = []
            s = set(unit_idxs)
            for (i, j, sim) in verified_lookup:
                if i in s and j in s:
                    sims.append(sim)
            if sims:
                cohesion = min(sims)
                chained = cohesion < SIM_THRESHOLD

        occ = len(ids)
        bcls, brule = boilerplate_class(members, occ)
        trig = divergence(texts)
        dates = sorted({m["date"] for m in members if m["date"]})
        ratifiers = sorted({r for m in members for r in m["ratified_by"]})
        ev = []
        seen = set()
        for m in members:
            for e in m["evidence_pointer"]:
                if e not in seen:
                    seen.add(e)
                    ev.append(e)

        # A CLUSTER OF ONE groups nothing, so every field that would merely
        # restate its single member is left null and read from
        # decision_candidates.json instead — this layer must never become a
        # second copy of the candidate list (#6). The schema stays regular:
        # the fields are always present, they are simply empty where they would
        # duplicate. The same reasoning removes the three constant strings
        # (the signal, the authority reason, the text note) to the header.
        grouped = occ > 1
        clusters.append({
            "size": occ,
            "distinct_texts": len(unit_idxs),
            "n_files": len(files),
            "files": files if grouped else None,
            "member_ids": ids,
            "proposed_representative": {
                "id": rep["id"],
                "file": rep_file,
                "line": rep_line,
                "authority_rank": authority_rank(rep_file),
                "text": rep["decision_text"] if grouped else None,
            },
            "min_pairwise_similarity": round(cohesion, 4) if grouped else None,
            "formed_by_chaining": chained,
            "boilerplate_class": bcls,
            "boilerplate_rule": brule,
            "internally_divergent": bool(trig),
            "divergence_triggers": trig,
            "dates": dates if grouped else None,
            "ratified_by": ratifiers if grouped else None,
            "evidence_pointer": ev[:24] if grouped else None,
            "_sortkey": (-occ, rep["id"]),
        })

    clusters.sort(key=lambda c: c["_sortkey"])
    for n, c in enumerate(clusters, 1):
        c["cluster_id"] = "DC-%05d" % n
        del c["_sortkey"]
    # cluster_id first in the record
    return [dict([("cluster_id", c.pop("cluster_id"))] + list(c.items())) for c in clusters]


# ── Signals (2) and (3): links BETWEEN clusters, never merged into them ───────
#
# Both are computed from the MEMBERS, not from the cluster record, because the
# cluster record deliberately leaves those fields empty for a cluster of one
# (they would only restate the member). A cluster of one is exactly where these
# links matter most — "these five separately-worded statements all cite the same
# commit" is the whole point — so the link layer reads the members directly.
def cluster_pointers(c, by_id):
    ev, seen = [], set()
    for mid in c["member_ids"]:
        for e in by_id[mid]["evidence_pointer"]:
            if e not in seen:
                seen.add(e)
                ev.append(e)
    return ev[:24]


def cluster_dates_ratifiers(c, by_id):
    dates = sorted({by_id[m]["date"] for m in c["member_ids"] if by_id[m]["date"]})
    who = sorted({r for m in c["member_ids"] for r in by_id[m]["ratified_by"]})
    return dates, who


def evidence_links(clusters, by_id):
    idx = {}
    for c in clusters:
        for e in cluster_pointers(c, by_id):
            idx.setdefault(e, set()).add(c["cluster_id"])
    groups, too_common = [], []
    for e, cids in sorted(idx.items()):
        if len(cids) < 2:
            continue
        if len(cids) > EVIDENCE_LINK_MAX_CLUSTERS:
            too_common.append({"pointer": e, "n_clusters": len(cids)})
            continue
        groups.append({
            "signal": "2 — shared evidence pointer (WEAKER than signal 1; a link, not a merge)",
            "pointer": e,
            "n_clusters": len(cids),
            "cluster_ids": sorted(cids),
        })
    groups.sort(key=lambda g: (-g["n_clusters"], g["pointer"]))
    too_common.sort(key=lambda g: (-g["n_clusters"], g["pointer"]))
    return groups, too_common


def date_ratifier_links(clusters, by_id):
    idx = {}
    for c in clusters:
        dates, who = cluster_dates_ratifiers(c, by_id)
        if not dates or not who:
            continue
        for d in dates:
            for r in who:
                idx.setdefault((d, r), set()).add(c["cluster_id"])
    groups, too_common = [], []
    for (d, r), cids in sorted(idx.items()):
        if len(cids) < 2:
            continue
        rec = {"date": d, "ratified_by": r, "n_clusters": len(cids)}
        if len(cids) > DATE_LINK_MAX_CLUSTERS:
            too_common.append(rec)
            continue
        rec["signal"] = ("3 — same date and same ratifier (WEAKEST; corroborating only, "
                         "never a grouping on its own)")
        rec["cluster_ids"] = sorted(cids)
        groups.append(rec)
    groups.sort(key=lambda g: (-g["n_clusters"], g["date"], g["ratified_by"]))
    too_common.sort(key=lambda g: (-g["n_clusters"], g["date"], g["ratified_by"]))
    return groups, too_common


# ── Reporting helpers ─────────────────────────────────────────────────────────
def size_distribution(clusters):
    buckets = {"1": 0, "2-5": 0, "6-20": 0, "21+": 0}
    for c in clusters:
        s = c["size"]
        if s == 1:
            buckets["1"] += 1
        elif s <= 5:
            buckets["2-5"] += 1
        elif s <= 20:
            buckets["6-20"] += 1
        else:
            buckets["21+"] += 1
    return buckets


def git_head():
    r = subprocess.run(["git", "-C", REPO, "rev-parse", "HEAD"],
                       capture_output=True, text=True)
    return r.stdout.strip()


# ── The declared worked counter-example ───────────────────────────────────────
# One decision this repository is KNOWN to restate many times — the Stage-3.1b
# shelving of whole-score interactive analysis, named as the leading example in
# the dispatch that commissioned this layer. Counting how many candidate
# statements mention it, and how many separate clusters they land in, measures
# what near-identical-text grouping can and cannot reach on this corpus. It is a
# text search reported as a count — nothing about the decision is judged here.
COUNTER_EXAMPLE = {
    "name": "the Stage-3.1b shelving of whole-score interactive analysis",
    "must_match": r"3\.1b",
    "and_match": r"shelv|whole[- ]score|whole[- ]piece|overturn",
}
# The three occurrences quoted in the preview: one from a design document, one
# from the measured evidence artifact, one from the code comment at the site the
# decision governs — three homes stating the same decision in different words.
# Named explicitly so the choice of quotation is visible rather than implicit;
# the quoted text itself is verbatim.
COUNTER_EXAMPLE_QUOTES = ["DH-03685", "DH-03941", "DH-14548"]


def counter_example(clusters, by_id):
    must = re.compile(COUNTER_EXAMPLE["must_match"], re.IGNORECASE)
    also = re.compile(COUNTER_EXAMPLE["and_match"], re.IGNORECASE)
    cluster_of, size_of = {}, {}
    for c in clusters:
        size_of[c["cluster_id"]] = c["size"]
        for m in c["member_ids"]:
            cluster_of[m] = c["cluster_id"]
    hits = []
    for cid in sorted(by_id):
        t = by_id[cid]["decision_text"]
        if must.search(t) and also.search(t):
            f, ln = primary_location(by_id[cid])
            hits.append({"id": cid, "file": f, "line": ln,
                         "cluster_id": cluster_of[cid],
                         "cluster_size": size_of[cluster_of[cid]]})
    return {
        "name": COUNTER_EXAMPLE["name"],
        "query": {k: v for k, v in COUNTER_EXAMPLE.items() if k != "name"},
        "matching_candidates": len(hits),
        "distinct_clusters_they_fall_into": len({h["cluster_id"] for h in hits}),
        "all_in_singleton_clusters": all(h["cluster_size"] == 1 for h in hits),
        "occurrences": hits,
    }


# ── The worked preview (Task 2) ───────────────────────────────────────────────
# The plain-words restatement of each previewed decision is written by hand and
# lives HERE, keyed by the proposed representative's candidate id, so the preview
# document is GENERATED and every number in it is derived (#17f) — no number is
# ever hand-typed into the document.
#
# These restatements say what the quoted text says, in ordinary words. They do
# NOT say whether the decision still stands, whether the code obeys it, or which
# statement is authoritative — those are the adjudication's.
PREVIEW_PROSE = {
    # DC-00001 — the open-items detail-file banner
    "DH-04764": {
        "title": "Where an open item's status of record lives",
        "what": "An open item's status is held in one place only — the index file "
                "`OPEN_ITEMS.md`. The per-item detail file carries the story and the "
                "provenance, and is never allowed to state a status of its own. The "
                "point is that a reader who wants to know whether something is still "
                "open has exactly one place to look, and two places can never "
                "disagree.",
        "row": "An open item's status of record lives in the index `OPEN_ITEMS.md` "
               "only; the per-item detail file carries narrative and provenance and "
               "never a status.",
        "home_note": "*A caution about this proposal.* Every one of the statements in "
                     "this group is the same banner line, reproduced at the top of each "
                     "detail file, so the highest-authority statement among them is "
                     "still just one of those banners. The rule's governing statement "
                     "is in `CLAUDE.md`, in the open-items-register section — but it is "
                     "worded differently there, so this grouping did not reach it. That "
                     "gap is the subject of the finding at the end of this document.",
    },
    # DC-00002 — register section B
    "DH-04475": {
        "title": "Which open items are owned by the build-and-design stage",
        "what": "Open items filed under section B are owned by the stage where building "
                "and design decisions are made, and are dealt with there rather than "
                "wherever they happen to be noticed. Filing an item into a section is "
                "how the project fixes *when* it will be worked on.",
        "row": "Open items in section B are owned by the build-and-design stage "
               "(Stage-3 / E4) and are fixed there.",
    },
    # DC-00008 — register section C
    "DH-04771": {
        "title": "Open items that must not be fixed early",
        "what": "Open items filed under section C belong to the precision stage, and "
                "are explicitly not to be fixed before it. This is the sequencing rule "
                "that says accuracy work does not start until the methods it depends on "
                "are in place — fixing such an item early would mean tuning against a "
                "moving foundation.",
        "row": "Open items in section C are owned by the precision stage (Stage-5) and "
               "must NOT be fixed earlier (principle #8).",
    },
    # DC-00010 — register section H
    "DH-04906": {
        "title": "Long-horizon items are held on purpose, not forgotten",
        "what": "Open items filed under section H are held back deliberately, and they "
                "are written down precisely so that holding them back never turns into "
                "losing them. Being listed is what distinguishes a deferral from an "
                "omission.",
        "row": "Open items in section H are long-horizon and held deliberately; they "
               "are listed so they are never forgotten.",
    },
    # DC-00015 — register section E
    "DH-04860": {
        "title": "Open items that are waiting on the user's ruling",
        "what": "Open items filed under section E are ones where the next move is not "
                "anyone's to make except the user's: they are waiting on a ruling or a "
                "ratification, not on work.",
        "row": "Open items in section E are waiting on the user's adjudication or "
               "ratification.",
    },
}
PREVIEW_N = 5


def _q(text, limit=700):
    t = text.strip()
    if len(t) > limit:
        t = t[:limit].rstrip() + " […]"
    return "\n".join("> " + ln for ln in t.split("\n"))


def write_preview(clusters, manifest, by_id, counter, path):
    shown = [c for c in clusters if not c["boilerplate_class"]][:PREVIEW_N]
    n_in = manifest["input_candidates"]
    L = []
    A = L.append
    A("# The decision groups — a worked preview")
    A("")
    A("> **What this document is for.** The decision harvest collected every statement in")
    A("> the repository that reads like a ruling — %s of them. This step proposes which of"
      % f"{n_in:,}")
    A("> those statements are restatements of **one** decision, so that the session that")
    A("> writes the decisions register reads groups rather than %s separate lines."
      % f"{n_in:,}")
    A(">")
    A("> Below are the %d largest groups, each written up in the shape a decisions-register"
      % len(shown))
    A("> entry would take. **Please read them and say whether that shape is readable** —")
    A("> before the expensive session commits to it. There is also a finding at the end")
    A("> that changes what this grouping is worth; it is short and it matters more than the")
    A("> examples do.")
    A(">")
    A("> **Nothing was decided here, and nothing was thrown away.** This step does not judge")
    A("> whether a statement really is a decision, whether a decision still stands, or")
    A("> whether the code obeys it. And all %s statements are still present and still"
      % f"{n_in:,}")
    A("> individually readable in `decision_candidates.json` — this is a grouping laid on")
    A("> top, in which every group names every statement it contains.")
    A("")
    A("*Generated by `tools/audit/decisions/gen_decision_clusters.py`. Every number below is")
    A("derived from the artifacts; none is typed by hand.*")
    A("")
    A("---")
    A("")
    A("## How two statements were judged to be the same decision")
    A("")
    A("Only by **wording**. Each statement is cut into overlapping runs of three")
    A("consecutive words, and two statements are proposed as the same decision when they")
    A("share at least **%d%%** of those runs — four fifths of the three-word runs in common,"
      % int(round(manifest["similarity_threshold"] * 100)))
    A("which is restatement in near-identical words rather than merely writing about the")
    A("same subject. Capitalisation, punctuation and Markdown formatting are ignored;")
    A("numbers are not, because a number is content. Statements shorter than %d words are"
      % manifest["min_tokens_for_similarity"])
    A("grouped only when their wording is *exactly* the same, since a short heading shares")
    A("three-word runs with unrelated short headings.")
    A("")
    A("Two further signals were computed but deliberately **not** allowed to group anything:")
    A("statements citing the same commit or document, and statements carrying the same date")
    A("and the same person ratifying. Both are recorded as links *between* groups, because")
    A("either one on its own would join statements that merely share a context. The rule")
    A("throughout was: when in doubt, do not group — a wrong join disappears from view")
    A("afterwards, whereas a group that is too coarse is merely untidy and can be split.")
    A("")
    A("Where the wording was strong enough to group but the members do not appear to say")
    A("the same thing — different numbers in otherwise identical sentences, or one member")
    A("carrying a word like *superseded* that the others lack — the group is **flagged and")
    A("left alone**. Those flags are where a change of mind is most likely hiding.")
    A("")

    for n, c in enumerate(shown, 1):
        rep = c["proposed_representative"]
        prose = PREVIEW_PROSE.get(rep["id"], {})
        A("---")
        A("")
        A("## %d. %s" % (n, prose.get("title", "(group %s)" % c["cluster_id"])))
        A("")
        A("**What was decided.** %s" % prose.get("what", "*(not yet restated)*"))
        A("")
        A("**When, and who ratified it.** %s" % (
            prose.get("when")
            or ("The statements themselves carry %s%s. Where a group's own words do not "
                "say, this stays blank rather than being guessed." % (
                    ("the date(s) " + ", ".join(c["dates"])) if c["dates"] else "no date",
                    (" and name " + ", ".join(c["ratified_by"]) + " as ratifying")
                    if c["ratified_by"] else " and name no ratifier"))))
        A("")
        A("**Where its authoritative statement appears to live — a proposal, not a "
          "finding.** `%s`, line %d. It was picked because that file ranks highest in "
          "source authority among the group's members (%s); it was *not* picked for being "
          "the longest or the clearest."
          % (rep["file"], rep["line"], AUTHORITY_REASON[rep["authority_rank"]]))
        if prose.get("home_note"):
            A("")
            A(prose["home_note"])
        A("")
        flist = ", ".join("`%s`" % f for f in (c["files"] or [])[:5])
        A("**How often it is restated.** %d times, across %d documents%s. Repetition is "
          "evidence that the decision stands — each time someone worked in its "
          "neighbourhood, they wrote it out again." % (
              c["size"], c["n_files"],
              " (%s)" % flist if c["n_files"] <= 5 else " (%s, and %d more)"
              % (flist, c["n_files"] - 5)))
        A("")
        if c["internally_divergent"]:
            A("**Do the restatements agree?** **No — this group is flagged as divergent, "
              "and deliberately left unresolved.** What differs, mechanically: %s."
              % "; ".join(c["divergence_triggers"]))
        else:
            A("**Do the restatements agree?** Yes. No disagreement was detectable "
              "mechanically: no differing numbers, no member carrying a word that would "
              "change a decision's standing while the others do not, no opposed wording.")
        A("")
        A("**Some of the statements themselves, quoted exactly.**")
        A("")
        seen_txt, quoted = set(), 0
        for mid in c["member_ids"]:
            m = by_id[mid]
            k = cluster_norm(m["decision_text"])
            if k in seen_txt:
                continue
            seen_txt.add(k)
            f, ln = primary_location(m)
            A("*From `%s`, line %d (statement `%s`):*" % (f, ln, m["id"]))
            A("")
            A(_q(m["decision_text"]))
            A("")
            quoted += 1
            if quoted >= 3:
                break
        if c["distinct_texts"] == 1:
            A("*(All %d occurrences are word-for-word the same; one is quoted.)*" % c["size"])
            A("")
        A("**A mock decisions-register entry.**")
        A("")
        A("| Field | Value |")
        A("|---|---|")
        A("| Decision, in plain words | %s |" % prose.get("row", "").replace("\n", " "))
        A("| Date | %s |" % (", ".join(c["dates"]) if c["dates"]
                             else "*(not stated in the text)*"))
        A("| Ratified by | %s |" % (", ".join(c["ratified_by"]) if c["ratified_by"]
                                    else "*(not stated in the text)*"))
        A("| Status | *(left empty — this is the adjudication's to fill: live / "
          "superseded-by / shelved-with-evidence / falsified)* |")
        A("| Evidence pointer | %s |" % (", ".join("`%s`" % e for e in c["evidence_pointer"][:6])
                                         if c["evidence_pointer"] else "*(none extracted)*"))
        A("| Home — the authoritative statement | `%s`:%d — **proposed** |"
          % (rep["file"], rep["line"]))
        A("| Detail file | *(only if the pointer above does not suffice)* |")
        A("| Restated | %d times across %d documents — group `%s` |"
          % (c["size"], c["n_files"], c["cluster_id"]))
        A("")
        A("*(The date and ratifier above are whatever the statements themselves carry,")
        A("unfiltered. Where several appear, picking the one that is the ratification date")
        A("is the adjudication's job, not this step's. There is no conformance field:")
        A("whether the code obeys a decision changes every time the code moves, whereas a")
        A("decision's standing changes only when someone rules again, and keeping both in")
        A("one row is what makes a decisions register go stale — non-conformance is tracked")
        A("in `OPEN_ITEMS.md` as ordinary rows.)*")
        A("")

    # ---- the finding ----
    A("---")
    A("")
    A("## The finding — please read this")
    A("")
    A("**Grouping by wording barely reduces the work, and the reason is that this")
    A("repository does not restate decisions by copying them. It restates them in fresh")
    A("words every time.**")
    A("")
    A("Across all %s collected statements there are only **%d pairs** anywhere in the"
      % (f"{n_in:,}", manifest["diagnostics"]["verified_pairs_at_sweep_floor"]))
    A("repository that are near-identical in wording at all — and that count is exact, not")
    A("an estimate: it was checked by comparing every possible pair by brute force. Almost")
    A("all of those pairs are repeated layout or repeated dispatch instructions. So the")
    A("%s statements fall into %s groups: the grouping merges %s statements and leaves"
      % (f"{n_in:,}", f"{manifest['cluster_count']:,}",
         f"{n_in - manifest['cluster_count']:,}"))
    A("%s standing alone." % f"{manifest['size_distribution']['1']:,}")
    A("")
    A("### A worked example of what it misses")
    A("")
    A("Take %s — the very decision that prompted this whole exercise." % counter["name"])
    A("**%d** of the collected statements are about it. They fall into **%d** separate"
      % (counter["matching_candidates"], counter["distinct_clusters_they_fall_into"]))
    A("groups — that is, %s. Three of them, quoted exactly:"
      % ("every single one stands alone" if counter["all_in_singleton_clusters"]
         else "almost none of them were joined"))
    A("")
    by_hit = {h["id"]: h for h in counter["occurrences"]}
    chosen = [by_hit[i] for i in COUNTER_EXAMPLE_QUOTES if i in by_hit]
    for h in chosen:
        A("*From `%s`, line %d (statement `%s`):*" % (h["file"], h["line"], h["id"]))
        A("")
        A(_q(by_id[h["id"]]["decision_text"], 520))
        A("")
    A("Those say the same thing and share almost no wording, so no measurement of wording")
    A("can join them. The consequence is worth stating plainly: **the number of groups is")
    A("not the number of decisions.** It is the number of *distinctly-worded statements*,")
    A("which is very nearly the number of statements.")
    A("")
    A("### What this does and does not settle")
    A("")
    A("What the grouping does deliver: the repeated layout and repeated instruction text is")
    A("now identified and set aside as a labelled bucket (%d groups, %d occurrences), and"
      % (manifest["boilerplate"]["clusters"], manifest["boilerplate"]["occurrences"]))
    A("the handful of genuine copy-and-paste restatements is found with certainty. What it")
    A("does not deliver is the consolidation the exercise was aiming at, and no adjustment")
    A("of the wording cut-off would change that. Loosening it from %s all the way to %s"
      % (("%.2f" % manifest["similarity_threshold"]),
         min(manifest["diagnostics"]["threshold_sweep"], key=float)))
    sweep = manifest["diagnostics"]["threshold_sweep"]
    loosest = min(sweep, key=float)
    A("merges only %s further statements; tightening it to %s un-merges %s. The whole"
      % (f"{sweep['%.2f' % manifest['similarity_threshold']]['clusters'] - sweep[loosest]['clusters']:,}",
         max(sweep, key=float),
         f"{sweep[max(sweep, key=float)]['clusters'] - sweep['%.2f' % manifest['similarity_threshold']]['clusters']:,}"))
    A("range from %s to %s spans %s groups out of %s."
      % (loosest, max(sweep, key=float),
         f"{max(v['clusters'] for v in sweep.values()) - min(v['clusters'] for v in sweep.values()):,}",
         f"{manifest['cluster_count']:,}"))
    A("")
    A("This is flagged rather than worked around, because working around it would mean")
    A("changing what a \"statement\" is — cutting the collected blocks into single sentences,")
    A("or matching by meaning rather than by wording. Either is a real change of method with")
    A("its own risks, and neither is what this step was asked to do.")
    A("")
    A("---")
    A("")
    A("## The size of the work this leaves")
    A("")
    A("| | Count |")
    A("|---|---|")
    A("| Statements collected by the harvest | %s |" % f"{n_in:,}")
    A("| Groups they fall into | %s |" % f"{manifest['cluster_count']:,}")
    A("| … standing alone (no restatement found) | %s |"
      % f"{manifest['size_distribution']['1']:,}")
    A("| … 2 to 5 statements | %s |" % f"{manifest['size_distribution']['2-5']:,}")
    A("| … 6 to 20 statements | %s |" % f"{manifest['size_distribution']['6-20']:,}")
    A("| … 21 or more statements | %s |" % f"{manifest['size_distribution']['21+']:,}")
    A("| Groups set aside as repeated layout or instruction text (kept, not deleted) | %s |"
      % f"{manifest['boilerplate']['clusters']:,}")
    A("| Groups flagged as not saying the same thing | %s |"
      % f"{manifest['internally_divergent_clusters']:,}")
    A("")
    A("The set-aside groups are of two kinds, and each can be confirmed a kind at a time")
    A("rather than one statement at a time:")
    A("")
    for cls, rec in sorted(manifest["boilerplate"]["by_class"].items()):
        pretty = {"document_scaffolding": "repeated layout — section titles and table "
                                          "header rows",
                  "dispatch_instruction": "repeated standing instructions — the "
                                          "\"push to our own copy only\", \"stop if "
                                          "surprised\" and \"read-only\" lines every "
                                          "dispatch repeats"}.get(cls, cls)
        A("- **%s**: %d groups, %d occurrences." % (pretty, rec["clusters"], rec["occurrences"]))
    A("")
    A("Two things were deliberately **not** set aside, because setting something aside is")
    A("itself a form of grouping and the same when-in-doubt rule applies: a whole line in")
    A("bold is not treated as a mere heading (in this repository such a line often carries a")
    A("rule — the open-items sections above are the case in point), and the open-items")
    A("banner is not treated as an instruction, because it states a rule rather than")
    A("directing a session. Both therefore appear above as ordinary groups, where they are")
    A("visible.")
    A("")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(L))


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(
        description="Mechanical clustering LAYER over the decision harvest (OI-207/OI-208).")
    ap.add_argument("--check", action="store_true",
                    help="prove the layer is non-destructive and exit nonzero if it is not")
    ap.add_argument("--establish", action="store_true",
                    help="establish the grouping against an exact brute-force reference "
                         "over the WHOLE corpus (#19); writes cluster_establishment.json "
                         "and exits nonzero on any missed or spurious pair")
    ap.add_argument("--no-preview", action="store_true",
                    help="skip cluster_preview.md (used on the first pass, before the "
                         "plain-words restatements are written)")
    args = ap.parse_args()

    sha_before = candidates_sha256()
    header, cands = load_candidates()
    by_id = {c["id"]: c for c in cands}
    report = {}

    units = build_units(cands)
    verified = lsh_candidate_pairs(units, report)

    if args.establish:
        floor = min(SWEEP)
        exact, n_elig, n_shingles = exact_pairs_bruteforce(units, floor)
        es = {(i, j) for (i, j, _s) in exact}
        fs = {(i, j) for (i, j, _s) in verified}
        missed, spurious = es - fs, fs - es
        rec = {
            "establishes": "tools/audit/decisions/gen_decision_clusters.py — the "
                           "MinHash+LSH near-identical-text grouping",
            "method": "brute-force EXACT Jaccard over every pair of "
                      "similarity-eligible units sharing at least one shingle "
                      "(a pair sharing none has similarity 0, so the enumeration "
                      "is complete), by sparse boolean matrix multiplication",
            "input_sha256": sha_before,
            "head_commit": git_head(),
            "floor": floor,
            "similarity_eligible_units": n_elig,
            "distinct_shingles": n_shingles,
            "exact_pairs_at_or_above_floor": len(es),
            "pairs_found_by_the_tool": len(fs),
            "missed_by_the_tool": len(missed),
            "spurious_from_the_tool": len(spurious),
            "recall": 1.0 if not es else round(len(es & fs) / float(len(es)), 6),
            "precision": 1.0 if not fs else round(len(es & fs) / float(len(fs)), 6),
            "verdict": "ESTABLISHED" if not missed and not spurious else "FAILED",
            "exact_pairs": [
                {"a": units[i]["ids"][0], "b": units[j]["ids"][0],
                 "similarity": round(s, 4)} for (i, j, s) in exact],
        }
        with open(os.path.join(HERE, "cluster_establishment.json"), "w",
                  encoding="utf-8", newline="\n") as fh:
            json.dump(rec, fh, indent=1, sort_keys=False)
        print("establishment: %s" % rec["verdict"])
        for k in ("similarity_eligible_units", "distinct_shingles",
                  "exact_pairs_at_or_above_floor", "pairs_found_by_the_tool",
                  "missed_by_the_tool", "spurious_from_the_tool",
                  "recall", "precision"):
            print("  %-32s %s" % (k, rec[k]))
        sys.exit(0 if rec["verdict"] == "ESTABLISHED" else 2)

    groups = cluster_at(units, verified, SIM_THRESHOLD)
    clusters = build_clusters(units, groups, by_id, verified)

    # ---- the non-destructiveness proof (#12, and the dispatch's first rule) ----
    seen = []
    for c in clusters:
        seen.extend(c["member_ids"])
    ok_count = len(seen) == len(cands)
    ok_unique = len(set(seen)) == len(seen)
    ok_same = set(seen) == set(by_id)
    # the input file is untouched: its content hash is taken again here and once
    # more after every output has been written (the final re-check at the end of
    # main), and both must equal the hash taken before the read.
    ok_input_untouched = candidates_sha256() == sha_before
    nondestructive = ok_count and ok_unique and ok_same and ok_input_untouched
    report["non_destructive"] = {
        "input_candidates": len(cands),
        "candidates_placed_in_a_cluster": len(seen),
        "every_candidate_exactly_once": ok_unique and ok_count,
        "id_set_identical_to_input": ok_same,
        "input_sha256": sha_before,
        "input_unchanged_by_this_tool": ok_input_untouched,
        "verdict": "PASS" if nondestructive else "FAIL",
    }

    # ---- threshold sensitivity ----
    sweep = {}
    for t in SWEEP:
        g = cluster_at(units, verified, t)
        n_clusters = 0
        expanded = {}
        for root, uidx in g.items():
            n_clusters += 1
            expanded[root] = sum(len(units[u]["ids"]) for u in uidx)
        sweep["%.2f" % t] = {
            "clusters": n_clusters,
            "largest_cluster_occurrences": max(expanded.values()) if expanded else 0,
        }
    report["threshold_sweep"] = sweep

    ev_groups, ev_common = evidence_links(clusters, by_id)
    dr_groups, dr_common = date_ratifier_links(clusters, by_id)

    bp_clusters = [c for c in clusters if c["boilerplate_class"]]
    bp_by_class = {}
    for c in bp_clusters:
        k = c["boilerplate_class"]
        bp_by_class.setdefault(k, {"clusters": 0, "occurrences": 0, "rules": {}})
        bp_by_class[k]["clusters"] += 1
        bp_by_class[k]["occurrences"] += c["size"]
        bp_by_class[k]["rules"][c["boilerplate_rule"]] = \
            bp_by_class[k]["rules"].get(c["boilerplate_rule"], 0) + 1
    div = [c for c in clusters if c["internally_divergent"]]
    chained = [c for c in clusters if c["formed_by_chaining"]]
    div_by_trigger = {}
    for c in div:
        for t in c["divergence_triggers"]:
            head = t.split("(")[0].strip()
            div_by_trigger[head] = div_by_trigger.get(head, 0) + 1
    div_largest = [{"cluster_id": c["cluster_id"], "occurrences": c["size"],
                    "triggers": c["divergence_triggers"],
                    "boilerplate_class": c["boilerplate_class"],
                    "representative": "%s:%d" % (c["proposed_representative"]["file"],
                                                 c["proposed_representative"]["line"])}
                   for c in sorted(div, key=lambda x: (-x["size"], x["cluster_id"]))[:10]]

    counter = counter_example(clusters, by_id)

    manifest = {
        "instrument": "tools/audit/decisions/gen_decision_clusters.py",
        "instrument_blob_sha": hashlib.sha1(
            open(os.path.abspath(__file__), "rb").read()).hexdigest(),
        "purpose": "OI-207/OI-208 — the mechanical clustering LAYER over the decision "
                   "harvest. Proposes which candidate statements are the same decision. "
                   "NO adjudication: no status, no conformance, no supersession named.",
        "input": {
            "file": "tools/audit/decisions/decision_candidates.json",
            "harvest_head_commit": header["head_commit"],
            "total_candidates": header["total_candidates"],
            "distinct_statements": header["distinct_statements"],
        },
        "head_commit": git_head(),
        "input_candidates": len(cands),
        "signals": [
            {"signal": 1, "name": "near-identical text", "strength": "primary",
             "definition": "Jaccard similarity of word %d-gram shingles on the normalized "
                           "text, >= %.2f; statements shorter than %d tokens are matched by "
                           "EXACT normalized text only."
                           % (SHINGLE_W, SIM_THRESHOLD, MIN_TOKENS_FOR_SIMILARITY),
             "role": "forms the clusters"},
            {"signal": 2, "name": "shared evidence pointer", "strength": "weaker",
             "definition": "two clusters cite the same commit hash, document, open-item id "
                           "or artifact path; a pointer shared by more than %d clusters is "
                           "reported as too common to be a signal."
                           % EVIDENCE_LINK_MAX_CLUSTERS,
             "role": "links clusters; NEVER merges them"},
            {"signal": 3, "name": "same date and same ratifier", "strength": "weakest",
             "definition": "two clusters carry the same date and the same ratifier; a pair "
                           "shared by more than %d clusters is reported as too common."
                           % DATE_LINK_MAX_CLUSTERS,
             "role": "corroborating only"},
        ],
        "similarity_threshold": SIM_THRESHOLD,
        "shingle_width_words": SHINGLE_W,
        "min_tokens_for_similarity": MIN_TOKENS_FOR_SIMILARITY,
        "minhash": {"permutations": N_HASH, "bands": N_BANDS,
                    "rows_per_band": ROWS_PER_BAND,
                    "band_50pct_similarity": round((1.0 / N_BANDS) ** (1.0 / ROWS_PER_BAND), 4),
                    "generation_probability_at_threshold":
                        round(1 - (1 - SIM_THRESHOLD ** ROWS_PER_BAND) ** N_BANDS, 4),
                    "caveat": "the two lowest sweep rungs (0.70, 0.75) are LOWER BOUNDS: the "
                            "band configuration is tuned for the 0.80 operating point, so a "
                            "small fraction of pairs below it is not generated."},
        "cluster_count": len(clusters),
        "size_distribution": size_distribution(clusters),
        "largest_cluster_occurrences": max(c["size"] for c in clusters) if clusters else 0,
        "clusters_formed_by_chaining": len(chained),
        "internally_divergent_clusters": len(div),
        "internally_divergent_by_trigger": div_by_trigger,
        "internally_divergent_outside_the_boilerplate_bucket":
            sum(1 for c in div if not c["boilerplate_class"]),
        "internally_divergent_largest": div_largest,
        "worked_counter_example": {k: v for k, v in counter.items() if k != "occurrences"},
        "boilerplate": {
            "clusters": len(bp_clusters),
            "occurrences": sum(c["size"] for c in bp_clusters),
            "by_class": bp_by_class,
            "policy": "KEPT, never deleted — bucketed and labelled by class so the "
                      "adjudication can confirm the judgment a class at a time.",
        },
        "evidence_links": {"groups": len(ev_groups),
                           "pointers_too_common_to_be_a_signal": len(ev_common)},
        "date_ratifier_links": {"groups": len(dr_groups),
                                "pairs_too_common_to_be_a_signal": len(dr_common)},
        "diagnostics": report,
        "outputs": ["decision_clusters.json", "decision_clusters.csv",
                    "cluster_manifest.json", "cluster_preview.md"],
        "NOTE": "status, conformance and supersession are NOT decided here. The "
                "per-cluster representative is a PROPOSAL chosen by source authority "
                "alone. Every input candidate is present in exactly one cluster and "
                "remains individually readable in decision_candidates.json.",
    }

    if args.check:
        print("non-destructiveness check: %s" % report["non_destructive"]["verdict"])
        for k, v in report["non_destructive"].items():
            print("  %-34s %s" % (k, v))
        sys.exit(0 if nondestructive else 2)

    with open(os.path.join(HERE, "decision_clusters.json"), "w",
              encoding="utf-8", newline="\n") as fh:
        header_out = {k: manifest[k] for k in
                      ("instrument", "purpose", "input", "similarity_threshold",
                       "cluster_count", "size_distribution",
                       "internally_divergent_clusters")}
        header_out["clusters_formed_by"] = (
            "signal 1 — near-identical text. Signals 2 and 3 appear separately "
            "below as links BETWEEN clusters and never merged any cluster.")
        header_out["authority_rank_meaning"] = AUTHORITY_REASON
        header_out["empty_field_rule"] = (
            "For a cluster of ONE, the fields that would merely restate its single "
            "member — files, dates, ratified_by, evidence_pointer, the "
            "representative's text, min_pairwise_similarity — are null by design; "
            "read them from that member in decision_candidates.json. This layer "
            "must not become a second copy of the candidate list (#6). The "
            "evidence-pointer and date+ratifier link groups below are computed "
            "from the MEMBERS, so clusters of one participate in them fully.")
        json.dump({"header": header_out,
                   "clusters": clusters,
                   "evidence_links": ev_groups,
                   "evidence_pointers_too_common": ev_common,
                   "date_ratifier_links": dr_groups,
                   "date_ratifier_pairs_too_common": dr_common,
                   "worked_counter_example": counter},
                  fh, indent=1, sort_keys=False)

    with open(os.path.join(HERE, "decision_clusters.csv"), "w",
              encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["cluster_id", "signal", "occurrences", "distinct_texts", "files",
                    "boilerplate_class", "internally_divergent", "divergence_triggers",
                    "min_pairwise_similarity", "formed_by_chaining",
                    "proposed_representative_id", "proposed_representative_file",
                    "proposed_representative_line", "authority_reason",
                    "dates", "ratified_by", "member_ids",
                    "representative_text_excerpt_grouped_clusters_only_"
                    "full_text_in_decision_candidates_json"])
        for c in clusters:
            rep = c["proposed_representative"]
            w.writerow([
                c["cluster_id"], "1-text", c["size"], c["distinct_texts"], c["n_files"],
                c["boilerplate_class"] or "", "yes" if c["internally_divergent"] else "",
                "; ".join(c["divergence_triggers"]), c["min_pairwise_similarity"],
                "yes" if c["formed_by_chaining"] else "",
                rep["id"], rep["file"], rep["line"],
                AUTHORITY_REASON[rep["authority_rank"]],
                ";".join(c["dates"] or []), ";".join(c["ratified_by"] or []),
                ";".join(c["member_ids"]),
                ((rep["text"] or "").replace("\r", " ").replace("\n", " ")[:300]),
            ])

    with open(os.path.join(HERE, "cluster_manifest.json"), "w",
              encoding="utf-8", newline="\n") as fh:
        json.dump(manifest, fh, indent=1, sort_keys=False)

    if not args.no_preview:
        write_preview(clusters, manifest, by_id, counter,
                      os.path.join(HERE, "cluster_preview.md"))

    print("decision clustering complete.")
    print("  input candidates       : %d" % len(cands))
    print("  distinct texts         : %d (similarity-eligible %d / exact-only %d)"
          % (report["units_total"], report["units_similarity_eligible"],
             report["units_exact_only"]))
    print("  clusters               : %d" % len(clusters))
    print("  size distribution      : %s" % json.dumps(manifest["size_distribution"]))
    print("  largest cluster        : %d occurrences" % manifest["largest_cluster_occurrences"])
    print("  boilerplate bucket     : %d clusters / %d occurrences"
          % (len(bp_clusters), sum(c["size"] for c in bp_clusters)))
    print("  internally divergent   : %d clusters" % len(div))
    print("  formed by chaining     : %d clusters" % len(chained))
    print("  evidence links         : %d groups (%d pointers too common)"
          % (len(ev_groups), len(ev_common)))
    print("  date+ratifier links    : %d groups (%d pairs too common)"
          % (len(dr_groups), len(dr_common)))
    final_untouched = candidates_sha256() == sha_before
    print("  non-destructive        : %s (input unchanged after all writes: %s)"
          % (report["non_destructive"]["verdict"], final_untouched))
    print("  threshold sweep        : %s"
          % json.dumps({k: v["clusters"] for k, v in sweep.items()}))
    if not (nondestructive and final_untouched):
        sys.stderr.write("FATAL: the clustering layer is NOT non-destructive.\n")
        sys.exit(2)


if __name__ == "__main__":
    main()

"""Voice-leading idiom discovery — the axis-2 study (CC, 2026-07-03).

Read-only research/measurement.  No src/ change, no build, no gate-corpus touch: the BIR
gate is untouched BY CONSTRUCTION (this pipeline reads note TSVs / scores and clusters
feature vectors; it never runs the analyzer or writes any corpus).

Coverage (Task 1): every DCML/DLC corpus on disk with notes/*.tsv (canonical tools/dcml/;
corpora/expl/dcml_* excluded as dedup-verified clones) + the full music21 4-part Bach chorale
set + the curated arrangements (steely_dan / piazzolla / hiromi) at note level.

Two feature views (Task 2): A = the pilot's |interval| histogram + repeat/step/leap rates
(UNCHANGED); B = voice-pair motion-type rates (parallel/similar/contrary/oblique).

Discovery + confound gate (Task 3): K-sweep x seeds x per-source caps; ARI/AMI of the VL
clusters against source / era / texture / voice-count / piece-length (the §5 leakage gate).
Ablation A vs B vs A+B says which features carry the structure.

Usage:  python run_vl_discovery.py [REPO_ROOT]     (default C:\\s\\MS)
        env VL_RELOAD=1 forces a re-parse (otherwise the record cache is reused)."""
import os, sys, time, pickle, itertools, collections
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parsers import voiceleading2 as vl2
from discover import leakage_report                       # reuse the ARI/AMI reporter
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score as ARI

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("VL_CORPUS_ROOT", vl2.REPO_DEFAULT)
CACHE = os.path.join(os.environ.get("TEMP", "/tmp"), "vl_records.pkl")
OUT = os.path.join(ROOT, "idiom_discovery", "vl_discovery_out.txt")
_lines = []
def emit(s=""):
    print(s); _lines.append(s)


# --------------------------------------------------------------------------- load
def load_all():
    if os.path.exists(CACHE) and os.environ.get("VL_RELOAD") != "1":
        recs = pickle.load(open(CACHE, "rb"))
        emit("loaded %d records from cache %s" % (len(recs), CACHE))
        return recs
    t0 = time.time()
    recs = []
    # (a) every DCML/DLC notes corpus
    for name, nd, texture, era in vl2.dcml_corpora(ROOT):
        r = vl2.load_dcml_notes(nd, name, texture, era)
        recs += r
        emit("  +dcml %-30s %-10s %-10s %4d  (%.0fs)" % (name, era, texture, len(r), time.time() - t0))
    # (b) full music21 4-part Bach chorale set
    r = vl2.load_m21_chorales()
    recs += r
    emit("  +m21_chorale (full)                              %4d  (%.0fs)" % (len(r), time.time() - t0))
    # (c) curated arrangements at note level (NOT chordify)
    cur = os.path.join(ROOT, "corpora", "expl", "curated_mxl")
    for sub, trad in [("steely_dan", "pop"), ("piazzolla", "tango"), ("hiromi", "jazz")]:
        d = os.path.join(cur, sub)
        if os.path.isdir(d):
            r = vl2.load_curated_notes(d, sub, "arrangement", "modern")
            recs += r
            emit("  +curated %-26s %-10s %4d  (%.0fs)" % (sub, trad, len(r), time.time() - t0))
    pickle.dump(recs, open(CACHE, "wb"))
    emit("TOTAL %d records in %.0fs (cached -> %s)" % (len(recs), time.time() - t0, CACHE))
    return recs


# --------------------------------------------------------------------------- helpers
def matrix(recs, view):
    """(X, kept_records) for view in {'A','B','AB','ABz'}."""
    keep = [r for r in recs if r['A'] is not None and (view == 'A' or r['B'] is not None)]
    if view == 'A':
        X = np.array([r['A'] for r in keep])
    elif view == 'B':
        X = np.array([r['B'] for r in keep])
    else:
        X = np.array([np.concatenate([r['A'], r['B']]) for r in keep])
        if view == 'ABz':
            X = (X - X.mean(0)) / (X.std(0) + 1e-9)
    return X, keep


def cap(recs, n):
    """Per-source cap: first n records (sorted by id) from each source."""
    bysrc = collections.defaultdict(list)
    for r in recs:
        bysrc[r['source']].append(r)
    out = []
    for s in sorted(bysrc):
        out += sorted(bysrc[s], key=lambda r: r['id'])[:n]
    return out


def stability_table(recs, view, Ks=(2, 3, 4, 5, 6, 7, 8), seeds=range(5), caps=(40, 80, 150)):
    emit("\n=== stability — view %s  (ARI vs texture ; self-stability across %d seeds) ===" % (view, len(list(seeds))))
    emit("  cap    K   texture-ARI mean±sd    source-ARI    self-stab")
    for c in caps:
        capped = cap(recs, c)
        X, keep = matrix(capped, view)
        tex = np.array([r['texture'] for r in keep])
        src = np.array([r['source'] for r in keep])
        emit("  --- cap=%d  (n=%d pieces) ---" % (c, len(keep)))
        for K in Ks:
            labs = [KMeans(K, random_state=s, n_init=10).fit_predict(X) for s in seeds]
            tA = [ARI(tex, l) for l in labs]
            sA = [ARI(l1, l2) for l1, l2 in itertools.combinations(labs, 2)]
            srcA = np.mean([ARI(src, l) for l in labs])
            emit("        %d   %.3f ± %.3f         %.3f        %.3f"
                 % (K, np.mean(tA), np.std(tA), srcA, np.mean(sA)))


def confound_gate(recs, view, K, cap_n=80, seed=0):
    capped = cap(recs, cap_n)
    X, keep = matrix(capped, view)
    labs = KMeans(K, random_state=seed, n_init=10).fit_predict(X)
    emit("\n=== confound gate — view %s, K=%d, cap=%d (n=%d) : ARI/AMI of clusters vs each covariate ===" % (view, K, cap_n, len(keep)))
    src = np.array([r['source'] for r in keep])
    tex = np.array([r['texture'] for r in keep])
    era = np.array([r['era'] for r in keep])
    vc = np.array([r['nvoices'] for r in keep])
    ln = np.array([r['nnotes'] for r in keep])
    vcb = np.array(["1-2" if v <= 2 else "3" if v == 3 else "4" if v == 4 else "5+" for v in vc])
    q = np.quantile(ln, [.25, .5, .75])
    lnb = np.array(["Q1" if x <= q[0] else "Q2" if x <= q[1] else "Q3" if x <= q[2] else "Q4" for x in ln])
    for nm, arr in [("source", src), ("texture", tex), ("era", era),
                    ("voice-count", vcb), ("piece-length", lnb)]:
        emit("  " + leakage_report(labs, arr, nm))
    return labs, keep


def idiom_table(recs, view, K, cap_n=80, seed=0):
    capped = cap(recs, cap_n)
    X, keep = matrix(capped, view)
    labs = KMeans(K, random_state=seed, n_init=10).fit_predict(X)
    tex = np.array([r['texture'] for r in keep])
    src = np.array([r['source'] for r in keep])
    overall = X.mean(0)
    HN = (["P|iv|=%d" % k for k in range(12)] + ["P|iv|>=12", "repeat", "step", "leap"]
          if view == 'A' else ["parallel", "similar", "contrary", "oblique"] if view == 'B'
          else ["P|iv|=%d" % k for k in range(12)] + ["P|iv|>=12", "repeat", "step", "leap",
                "parallel", "similar", "contrary", "oblique"])
    emit("\n=== idiom table — view %s, K=%d, cap=%d ===" % (view, K, cap_n))
    for cl in sorted(set(labs)):
        m = labs == cl
        n = int(m.sum())
        tmix = collections.Counter(tex[m]).most_common(4)
        smix = collections.Counter(src[m]).most_common(4)
        mean = X[m].mean(0)
        lift = mean - overall
        top = np.argsort(lift)[::-1][:4]
        bot = np.argsort(lift)[:2]
        emit("  c%d n=%3d  texture{%s}" % (cl, n, " ".join("%s:%d" % (k, v) for k, v in tmix)))
        emit("       sources{%s}" % " ".join("%s:%d" % (k, v) for k, v in smix))
        emit("       elevated: %s | low: %s" % (
            " ".join("%s(+%.2f)" % (HN[i], lift[i]) for i in top),
            " ".join("%s(%.2f)" % (HN[i], lift[i]) for i in bot)))
    return labs, keep


def pilot_replication(recs):
    """The pilot's chorale-vs-'piano' subset, from the fuller data, View A."""
    emit("\n=== pilot replication (chorale vs keyboard-quartet subset, View A) ===")
    sub = [r for r in recs if r['A'] is not None and
           (r['source'] == 'm21_chorale' or r['source'] in ('mozart_piano_sonatas', 'ABC', 'scarlatti_sonatas'))]
    # keep the m21-chorale count comparable to the pilot's 60 for the headline line
    ch = [r for r in sub if r['source'] == 'm21_chorale']
    pi = [r for r in sub if r['source'] != 'm21_chorale']
    lab = np.array([0 if r['source'] == 'm21_chorale' else 1 for r in (ch + pi)])
    X = np.array([r['A'] for r in (ch + pi)])
    km = KMeans(2, random_state=0, n_init=10).fit_predict(X)
    emit("  full chorale(%d) vs keyboard/quartet(%d): VL-cluster ARI = %.3f" % (len(ch), len(pi), ARI(lab, km)))
    for nm, mask in [("chorale", lab == 0), ("keyboard", lab == 1)]:
        mp = X[mask].mean(0)
        emit("    %-9s step(1-2)=%.0f%% leap(>2)=%.0f%% repeat=%.0f%%" % (nm, 100 * mp[14], 100 * mp[15], 100 * mp[13]))


def main():
    recs = load_all()
    # per-source coverage (Task 1 deliverable)
    emit("\n=== per-source coverage (view-usable counts) ===")
    bysrc = collections.defaultdict(lambda: [0, 0, 0])
    for r in recs:
        bysrc[r['source']][0] += 1
        bysrc[r['source']][1] += r['A'] is not None
        bysrc[r['source']][2] += r['B'] is not None
    for s in sorted(bysrc):
        n, a, b = bysrc[s]
        emit("  %-30s pieces=%4d  A=%4d  B=%4d" % (s, n, a, b))
    emit("  TOTAL sources=%d pieces=%d" % (len(bysrc), len(recs)))

    pilot_replication(recs)
    for view in ('A', 'B', 'AB', 'ABz'):
        stability_table(recs, view)
    # confound gate + idiom table at a defensible K (read from the stability tables; default 4)
    K = int(os.environ.get("VL_K", "4"))
    for view in ('A', 'B', 'AB'):
        confound_gate(recs, view, K)
    idiom_table(recs, 'AB', K)
    idiom_table(recs, 'A', K)
    idiom_table(recs, 'B', K)

    open(OUT, "w", encoding="utf-8").write("\n".join(_lines))
    emit("\nwrote %s" % OUT)


if __name__ == "__main__":
    main()

"""Voice-leading vs harmonic — the formal orthogonality test (axis-2 study, Task 4).

On the intersection pieces (a DCML score that carries BOTH notes/ -> a VL vector AND
harmonies/ -> a harmonic-view vector from the existing pipeline):
  * cross-ARI(VL clusters, harmonic clusters) + the 2-D contingency table;
  * the curated probe — Steely Dan / Piazzolla / Hiromi are ONE harmonic idiom (v1.6);
    do they SPLIT by voice-leading?
  * the chorale projection — the pilot predicts VL-tight / harmonically-scattered.

Read-only.  Reuses the harmonic pipeline (parsers/dcml, extract, discover) verbatim; the
VL side reads the record cache written by run_vl_discovery.py.

Usage:  python run_vl_orthogonality.py [REPO_ROOT]"""
import os, sys, pickle, collections
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parsers import voiceleading2 as vl2
from parsers.dcml import load_dcml_repo
from extract import build_corpus
from discover import fit_lda
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score as ARI, adjusted_mutual_info_score as AMI

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("VL_CORPUS_ROOT", vl2.REPO_DEFAULT)
CACHE = os.path.join(os.environ.get("TEMP", "/tmp"), "vl_records.pkl")
OUT = os.path.join(ROOT, "idiom_discovery", "vl_orthogonality_out.txt")
K = int(os.environ.get("VL_K", "5"))
_lines = []
def emit(s=""):
    print(s); _lines.append(s)


def vl_AB(r):
    return np.concatenate([r['A'], r['B']])


def main():
    recs = pickle.load(open(CACHE, "rb"))
    vl_by = {(r['source'], r['id']): r for r in recs if r['A'] is not None and r['B'] is not None}
    emit("VL records (A&B usable): %d" % len(vl_by))

    # --- harmonic-view Pieces from every DCML corpus that has harmonies/ ---
    hpieces = []
    for name, nd, tex, era in vl2.dcml_corpora(ROOT):
        repo = os.path.dirname(nd)
        ps = load_dcml_repo(repo, source=name, composer=name)
        for p in ps:
            p.meta['texture'] = tex
            p.meta['era'] = era
        hpieces += ps
    emit("harmonic-view Pieces (DCML harmonies): %d" % len(hpieces))

    X, vocab, meta = build_corpus(hpieces, view='transition', min_df=5, max_df=0.95)
    lda, dt = fit_lda(X, n_topics=12, seed=0)
    hlab_all = KMeans(K, random_state=0, n_init=10).fit_predict(dt)
    hkey = [(p.source, p.pid.replace('.harmonies', '')) for p in hpieces]
    hlab_by = {k: hlab_all[i] for i, k in enumerate(hkey)}

    # --- intersection ---
    inter = [k for k in hkey if k in vl_by]
    emit("\n=== INTERSECTION (both a VL vector and a harmonic vector): %d pieces ===" % len(inter))
    Xvl = np.array([vl_AB(vl_by[k]) for k in inter])
    vl_lab = KMeans(K, random_state=0, n_init=10).fit_predict(Xvl)
    h_lab = np.array([hlab_by[k] for k in inter])
    tex = np.array([vl_by[k]['texture'] for k in inter])
    era = np.array([vl_by[k]['era'] for k in inter])
    src = np.array([vl_by[k]['source'] for k in inter])

    emit("\n=== the orthogonality number ===")
    emit("  cross-ARI(VL clusters, harmonic clusters) = %.3f" % ARI(vl_lab, h_lab))
    emit("  cross-AMI(VL clusters, harmonic clusters) = %.3f" % AMI(vl_lab, h_lab))
    emit("  (for reference, on the SAME intersection pieces:)")
    emit("  VL clusters vs texture   ARI=%.3f  vs era ARI=%.3f  vs source ARI=%.3f"
         % (ARI(tex, vl_lab), ARI(era, vl_lab), ARI(src, vl_lab)))
    emit("  Harm clusters vs texture ARI=%.3f  vs era ARI=%.3f  vs source ARI=%.3f"
         % (ARI(tex, h_lab), ARI(era, h_lab), ARI(src, h_lab)))

    emit("\n=== contingency: VL cluster (rows) x harmonic cluster (cols) ===")
    ct = collections.Counter(zip(vl_lab, h_lab))
    hcs = sorted(set(h_lab)); vcs = sorted(set(vl_lab))
    emit("        " + "".join("  H%d " % c for c in hcs) + "   | row")
    for v in vcs:
        row = [ct.get((v, h), 0) for h in hcs]
        emit("   VL%d  " % v + "".join("%4d " % x for x in row) + "  | %4d" % sum(row))
    emit("   col   " + "".join("%4d " % sum(ct.get((v, h), 0) for v in vcs) for h in hcs))

    # --- curated probe: one harmonic idiom (v1.6), do they split by VL? ---
    emit("\n=== curated probe — one harmonic idiom (v1.6); split by VL? ===")
    curated = [r for r in recs if r['source'] in ('steely_dan', 'piazzolla', 'hiromi')
               and r['A'] is not None and r['B'] is not None]
    if curated:
        Xc = np.array([vl_AB(r) for r in curated])
        csrc = np.array([r['source'] for r in curated])
        cl = KMeans(min(3, K), random_state=0, n_init=10).fit_predict(Xc)
        emit("  curated pieces: %d  (VL-clustered into %d)" % (len(curated), len(set(cl))))
        for s in ('steely_dan', 'piazzolla', 'hiromi'):
            m = csrc == s
            if m.sum():
                spread = collections.Counter(cl[m])
                mp = Xc[m].mean(0)
                emit("    %-11s n=%2d VL-cluster spread=%s  step=%.0f%% leap=%.0f%% contrary=%.0f%% oblique=%.0f%%"
                     % (s, int(m.sum()), dict(spread), 100 * mp[14], 100 * mp[15], 100 * mp[18], 100 * mp[19]))

    # --- chorale projection: VL-tight? (harmonic scatter established in v1/v1.1) ---
    emit("\n=== chorale projection — VL-tight? (fuller coverage) ===")
    allkeep = [r for r in recs if r['A'] is not None and r['B'] is not None]
    Xall = np.array([vl_AB(r) for r in allkeep])
    lab_all = KMeans(K, random_state=0, n_init=10).fit_predict(Xall)
    src_all = np.array([r['source'] for r in allkeep])
    for chsrc in ('m21_chorale', 'bach_chorales'):
        m = src_all == chsrc
        if m.sum():
            spread = collections.Counter(lab_all[m]).most_common()
            top = spread[0]
            emit("  %-14s n=%3d  dominant VL cluster c%d holds %.0f%%  (spread %s)"
                 % (chsrc, int(m.sum()), top[0], 100 * top[1] / m.sum(),
                    " ".join("c%d:%d" % (c, n) for c, n in spread)))

    open(OUT, "w", encoding="utf-8").write("\n".join(_lines))
    emit("\nwrote %s" % OUT)


if __name__ == "__main__":
    main()

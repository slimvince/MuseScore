"""Full balanced-coverage idiom discovery + cap-robustness sweep + curated probe.

Portable: all paths derived from this file's location (works in the sandbox AND on the
user's machine). Run with no args for the full thing (~10 min, chordify-bound).
Env knobs (for quick validation): IDIOM_CAPS="120"  SKIP_CHORDIFY=1
Writes idiom_discovery/discovery_report.md.
"""
import os, sys, time, random, collections
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # the MS repo root
sys.path.insert(0, HERE)
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score as ARI
from parsers.dcml import load_dcml_repo
from parsers.jht import load_jht
from parsers.mcgill import load_mcgill
from parsers.choco import load_choco_harte, load_choco_m21, load_choco_weimar, load_choco_jparser
from parsers.bach_chordify import load_bach, load_xml_scores
from parsers.improvisor import load_improvisor
from parsers.chordonomicon import load_chordonomicon

C = os.path.join(ROOT, "corpora"); T = os.path.join(ROOT, "tools")
P = os.path.join(C, "ship", "choco", "partitions")
CUR = os.path.join(C, "expl", "curated_mxl")
CAPS = [int(x) for x in os.environ.get("IDIOM_CAPS", "400,700,1200").split(",")]
SKIP_CHORDIFY = os.environ.get("SKIP_CHORDIFY") == "1"


def load_all(cap, seed=0, do_chordify=True):
    """Every source, each capped at `cap` (balance + dedup ceiling); ireal-pro raw excluded."""
    random.seed(seed); pieces = []

    def add(ps, trad, sub):
        if cap and len(ps) > cap:
            ps = random.sample(ps, cap)
        for p in ps:
            p.meta["tradition"] = trad; p.meta["sub"] = sub
        pieces.extend(ps)

    # classical — DCML harmonies
    for nm in ["corelli", "cpe_bach_keyboard", "bach_en_fr_suites"]:
        add(load_dcml_repo(os.path.join(T, "dcml", nm), source=nm, composer=nm), "classical", nm)
    for rel, nm in [("expl/dcml_scarlatti", "scarlatti"), ("expl/dcml_mozart", "mozart"),
                    ("expl/dcml_beethoven", "beethoven")]:
        add(load_dcml_repo(os.path.join(C, rel.replace("/", os.sep)), source=nm, composer=nm), "classical", nm)
    romdir = os.path.join(C, "expl", "dcml_romantic")
    if os.path.isdir(romdir):
        for s in os.listdir(romdir):
            d = os.path.join(romdir, s)
            if os.path.isdir(os.path.join(d, "harmonies")):
                add(load_dcml_repo(d, source=s, composer=s), "classical", s)
    # jazz / pop / folk — symbolic
    add(load_jht(os.path.join(C, "expl", "jazz_harmony_treebank", "treebank.json")), "jazz", "jht")
    add(load_choco_harte(os.path.join(P, "real-book"), "real-book", "jazz", limit=cap), "jazz", "real-book")
    add(load_choco_weimar(os.path.join(P, "weimar"), "weimar", "jazz", limit=cap), "jazz", "weimar")
    add(load_choco_harte(os.path.join(P, "jaah"), "jaah", "jazz", limit=cap), "jazz", "jaah")
    add(load_choco_jparser(os.path.join(P, "jazz-corpus"), "jazz-corpus", "jazz", limit=cap), "jazz", "jazz-corpus")
    ipath = os.path.join(C, "expl", "improvisor", "leadsheets2", "imaginary-book")
    if os.path.isdir(ipath):
        add(load_improvisor(ipath, "improvisor", "jazz", limit=cap), "jazz", "improvisor")
    add(load_mcgill(os.path.join(C, "ship", "McGill-Billboard")), "pop", "mcgill")
    add(load_choco_harte(os.path.join(P, "isophonics"), "isophonics", "pop"), "pop", "isophonics")
    add(load_choco_m21(os.path.join(P, "wikifonia"), "wikifonia", "pop", limit=cap), "pop", "wikifonia")
    cpath = os.path.join(C, "expl", "chordonomicon", "chordonomicon_v2.csv")
    if os.path.isfile(cpath):
        add(load_chordonomicon(cpath, "chordonomicon", "pop", limit=cap), "pop", "chordonomicon")
    add(load_choco_m21(os.path.join(P, "nottingham"), "nottingham", "folk", limit=cap), "folk", "nottingham")
    # note-level chordify (slow) — only on the main run
    if do_chordify and not SKIP_CHORDIFY:
        add(load_bach(limit=min(cap, 300)), "classical", "bach_chorale")
        for fld, sub in [("corpus_rampageswing_full", "rampageswing"), ("corpus_effendi_src", "effendi")]:
            d = os.path.join(T, fld)
            if os.path.isdir(d):
                add(load_xml_scores(d, sub, "jazz", limit=80), "jazz", sub)
    random.shuffle(pieces)
    return pieces


def discover(pieces, K=6):
    trad = np.array([p.meta["tradition"] for p in pieces])
    docs = [p.transition_tokens() for p in pieces]
    vec = CountVectorizer(analyzer=lambda d: d, min_df=5, max_df=0.9)
    X = vec.fit_transform(docs)
    lda = LatentDirichletAllocation(12, random_state=0, max_iter=25, learning_method="batch")
    dt = lda.fit_transform(X)
    lab = KMeans(K, random_state=0, n_init=10).fit_predict(dt)
    return dict(trad=trad, X=X, feat=vec.get_feature_names_out(), vec=vec, lda=lda, dt=dt, lab=lab)


def report(r, out):
    Xd = np.asarray(r["X"].todense()); overall = Xd.mean(0) + 1e-9
    feat, lab, trad = r["feat"], r["lab"], r["trad"]
    out("  clusters<->tradition ARI = %.3f" % ARI(trad, lab))
    for c in sorted(set(lab)):
        m = lab == c; n = int(m.sum()); tr = collections.Counter(trad[m])
        mk = "  ".join("%s:%.0f%%" % (k, 100 * v / n) for k, v in tr.most_common(3))
        incl = Xd[m].mean(0); cand = [i for i in range(len(feat)) if incl[i] >= 0.30]
        cand.sort(key=lambda i: -incl[i] / overall[i])
        out("   c%d [%s]  %s" % (c, mk, " ".join(feat[i] for i in cand[:6])))


def main():
    lines = []; out = lambda s: (print(s), lines.append(s))
    t0 = time.time()
    out("# Idiom discovery — full balanced run + cap-robustness sweep (%s)" % time.strftime("%Y-%m-%d"))
    main_r = None
    for cap in CAPS:
        is_main = (cap == CAPS[len(CAPS) // 2])           # chordify only the middle cap
        ps = load_all(cap, do_chordify=is_main)
        out("\n## cap=%d  (%d pieces, %.0fs)  by-tradition=%s"
            % (cap, len(ps), time.time() - t0, dict(collections.Counter(p.meta["tradition"] for p in ps))))
        r = discover(ps); report(r, out)
        if is_main:
            main_r = r
    # curated probe — project the sophisticated scores into the main idiom space
    out("\n## curated probe (where Steely Dan / Piazzolla / Hiromi land)")
    cur = []
    for s, trad in [("steely_dan", "pop"), ("piazzolla", "classical"), ("hiromi", "jazz")]:
        d = os.path.join(CUR, s)
        if os.path.isdir(d) and not SKIP_CHORDIFY:
            cur += load_xml_scores(d, s, trad)
    if cur and main_r is not None:
        csets = np.array([p.source for p in cur])
        dtc = main_r["lda"].transform(main_r["vec"].transform([p.transition_tokens() for p in cur]))
        km = KMeans(6, random_state=0, n_init=10).fit(main_r["dt"]); lc = km.predict(dtc)
        for s in ["steely_dan", "piazzolla", "hiromi"]:
            d = collections.Counter(lc[csets == s]); tot = sum(d.values())
            if tot:
                out("   %-11s (n=%d) -> %s" % (s, tot, "  ".join("c%d:%.0f%%" % (c, 100 * v / tot) for c, v in d.most_common())))
    out("\n# done in %.0fs" % (time.time() - t0))
    open(os.path.join(HERE, "discovery_report.md"), "w").write("\n".join(lines) + "\n")
    print("\n-> wrote idiom_discovery/discovery_report.md")


if __name__ == "__main__":
    main()

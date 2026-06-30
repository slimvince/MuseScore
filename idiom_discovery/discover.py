"""Unsupervised discovery (LDA topics + clustering) and the confound checks.

Discover-then-name (spec §2): we learn topics/clusters with NO theory or genre
labels, then read them post-hoc.  The source-leakage test (spec §5) is first-class:
if clusters are explained by which corpus/source a piece came from, we found
bookkeeping, not idiom.
"""
from __future__ import annotations
import numpy as np
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score


def fit_lda(X, n_topics: int = 10, seed: int = 0):
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=seed,
                                    learning_method="batch", max_iter=30)
    doc_topic = lda.fit_transform(X)
    return lda, doc_topic


def top_tokens_per_topic(lda, vocab, n: int = 12):
    out = []
    for k, comp in enumerate(lda.components_):
        idx = np.argsort(comp)[::-1][:n]
        out.append([(vocab[i], float(comp[i])) for i in idx])
    return out


def cluster(doc_topic, n_clusters: int = 6, seed: int = 0):
    km = KMeans(n_clusters=n_clusters, random_state=seed, n_init=10)
    return km.fit_predict(doc_topic)


def leakage_report(labels, meta_array, name: str):
    """How strongly do the discovered labels track an external label (source/
    composer/mode)?  ARI/AMI near 0 = independent (good — not a confound); near 1
    = the clustering essentially recovered that label."""
    ari = adjusted_rand_score(meta_array, labels)
    ami = adjusted_mutual_info_score(meta_array, labels)
    return f"{name:10s}  ARI={ari:+.3f}  AMI={ami:+.3f}"


def summarise(lda, doc_topic, vocab, meta, n_clusters=6, seed=0, label_view="external"):
    print(f"\n=== {lda.n_components} LDA topics (top transition-tokens) ===")
    for k, toks in enumerate(top_tokens_per_topic(lda, vocab, n=10)):
        toks_s = " ".join(t for t, _ in toks)
        print(f"  T{k:02d}: {toks_s}")

    labels = cluster(doc_topic, n_clusters=n_clusters, seed=seed)

    print(f"\n=== {n_clusters} clusters vs external labels (the source-leakage test) ===")
    for key in ("tradition", "source", "composer", "era", "mode"):
        if key in meta and len(set(meta[key])) > 1:
            print("  " + leakage_report(labels, meta[key], key))

    # also: does the DOMINANT topic per piece track source? (topic-level leakage)
    dom = doc_topic.argmax(axis=1)
    if "source" in meta and len(set(meta["source"])) > 1:
        print("  " + leakage_report(dom, meta["source"], "dom-topic↔source"))

    return labels

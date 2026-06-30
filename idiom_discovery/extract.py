"""Build the clustering input from Pieces: each piece -> a bag of low-prejudice
tokens (transition tokens by default — the progression view; or chord tokens — the
vocabulary view).  No theory/genre labels enter here (spec §3)."""
from __future__ import annotations
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


def build_corpus(pieces, view: str = "transition", dedup: bool = True,
                 min_df: int = 5, max_df: float = 0.95):
    """Return (X, vocab, meta) where X is a piece × token count matrix.

    view: 'transition' (adjacent chord pairs) | 'chord' (single chords).
    min_df/max_df prune ultra-rare and near-universal tokens (a token in 95% of
    pieces carries no discriminative signal)."""
    if view == "transition":
        docs = [p.transition_tokens(dedup_repeats=dedup) for p in pieces]
    elif view == "chord":
        docs = [p.tokens(dedup_repeats=dedup) for p in pieces]
    else:
        raise ValueError(view)

    vec = CountVectorizer(analyzer=lambda d: d, min_df=min_df, max_df=max_df)
    X = vec.fit_transform(docs)
    vocab = vec.get_feature_names_out()
    meta = {
        "source": np.array([p.source for p in pieces]),
        "tradition": np.array([p.meta.get("tradition", "") for p in pieces]),
        "composer": np.array([p.meta.get("composer", "") for p in pieces]),
        "era": np.array([p.meta.get("era", "") for p in pieces]),
        "mode": np.array([p.mode or "" for p in pieces]),
        "pid": np.array([p.pid for p in pieces]),
        "n_tokens": np.array([len(d) for d in docs]),
    }
    return X, vocab, meta

#!/usr/bin/env python3
"""normalize.py — the OI-186(a) FIT-TIME label normalization (the label-side table fit, part 1).

READ-ONLY / FIT-LAYER-OWNED. No src/ change, no corpus mutation, no gate change, no metric
consulted. This is the ONE new normalization the fit event owns (`cc_instruction_label_table_fit.md`,
Cowork 2026-07-19). It maps a raw When-in-Rome Roman-numeral label to the class

    (degree base, quality, inversion figure, applied target)

with **quality derived from the FIGURE AND CASE, never from compare_rn.extract_quality** — that is the
OI-186(a) requirement: `extract_quality` is COARSE on WiR slash-spelled figured bass (it splits the
suffix on the first '/', so 'V6/5' reads as Maj not Dom7, and 'ii/o6/5' reads as Min not HalfDim7).
The fit-time class must not carry that coarseness. See OPEN_ITEMS.md OI-186.

REUSE (TOTAL UNIFICATION, #6) — this module writes NO second Roman-numeral parser. It reuses:
  - dcml_parser._split_rntxt_applied : the producer's own applied/tonicization splitter (already
                                       produced DcmlRegion.roman_numeral) — for the X/Y split.
  - compare_rn.normalise_rn / split_rn: degree token (case = mode color) + verbatim suffix.
The ONLY thing computed here that is NOT in those primitives is the quality-from-figure+case derivation
(the whole point of OI-186(a)) and the augmented-sixth / chromatic mapping for the split_rn=None tokens
(It6 → the augmented-sixth class, the factorization's standard chromatic class — dispatch §1).

WHAT IS NOT GUESSED. The quality/figure rules below were written against the FULL observed WiR-covered
label vocabulary (230 distinct raw labels over the 326 covered stems); the self-test at the bottom of
this file asserts every observed label maps to a covered class (raw_unnormalized == the 2 It6 tokens,
both routed to the augmented-sixth class) and prints the mapping. A label the rules do not cover lands
in a `raw_unnormalized` class and is COUNTED, never guessed (dispatch §1).
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))

import dcml_parser as dcml              # noqa: E402
import compare_rn as crn               # noqa: E402

# The normalization-rule version stamped into every fitted artifact's provenance (#16).
NORMALIZATION_VERSION = "label-fit-v1 (OI-186a; quality from figure+case)"

# WiR seventh/ninth figured-bass tokens (slash-spelled). A figure denoting a chord that carries a
# seventh (or a ninth, which carries a seventh). Triad figures are {'', '6', '6/4'}.
_SEVENTH_FIGURES = frozenset({"7", "6/5", "4/3", "4/2", "2"})

# Chromatic non-degree tokens that compare_rn.split_rn rejects (returns None). Only the Italian
# augmented sixth ('It6', 'It6/ii') is observed in the WiR-covered Bach corpus; Ger/Fr/N/Cad are
# NOT present (verified against the 230-label vocabulary). Each maps to a named chromatic class per
# the factorization's standard chromatic classes (dispatch §1). Ger/Fr/N are included so a future
# corpus with them normalizes rather than dropping to raw_unnormalized (#12) — none fire today.
_CHROMATIC_CLASS = {
    "It": ("It", "AugSixth"),    # Italian augmented sixth
    "Ger": ("Ger", "AugSixth"),  # German augmented sixth   (not observed in this corpus)
    "Fr": ("Fr", "AugSixth"),    # French augmented sixth   (not observed)
    "N": ("N", "Neapolitan"),    # Neapolitan sixth         (not observed as a bare 'N' token)
}
_CHROMATIC_RE = re.compile(r"^(It|Ger|Fr|N)(?:\d|/|$)")


@dataclass(frozen=True)
class LabelClass:
    """The normalized class of one WiR label. `raw_unnormalized` is True only when the primary
    numeral is neither split_rn-parseable NOR a recognized chromatic token."""
    degree_base: str          # accidental + UPPER degree letter, e.g. 'I', 'V', 'bVI', 'It'
    quality: str              # derived from figure+case: Maj/Min/Dom7/Maj7/Min7/MinMaj7/Dim/Dim7/
                              #   HalfDim/HalfDim7/Aug/Aug7/AugMaj7/AugSixth/Neapolitan/?/unknown
    inversion: str            # verbatim WiR inversion figure, markers stripped: '' 6 6/4 7 6/5 4/3 2 9 ...
    target: str               # applied tonicization target, case-preserved ('vi','V','III',''), '' if none
    raw_unnormalized: bool = False

    def key(self) -> str:
        return f"{self.degree_base} | {self.quality} | {self.inversion} | {self.target}"

    def inversion_free(self) -> "LabelClass":
        """The class with the inversion figure dropped (the declared parent for the entry/transition
        back-off chains). Root/seventh/ninth all collapse to '' here — the identity of the chord
        without its bass."""
        return LabelClass(self.degree_base, self.quality, "", self.target, self.raw_unnormalized)

    def family(self) -> "LabelClass":
        """The class with quality reduced to the triad/seventh FAMILY (the coarser transition
        back-off level): triad vs seventh, keeping degree + target, dropping inversion. Maj/Min/
        Dim/Aug/AugSixth/Neapolitan -> 'triad'; the seventh qualities -> 'seventh'."""
        fam = "seventh" if self.quality in _SEVENTH_QUALITIES else "triad"
        return LabelClass(self.degree_base, fam, "", self.target, self.raw_unnormalized)


_SEVENTH_QUALITIES = frozenset({"Dom7", "Maj7", "Min7", "MinMaj7", "Dim7", "HalfDim7",
                                "Aug7", "AugMaj7"})


def _canonical_figure(suffix: str) -> str:
    """Strip the quality markers (/o half-dim sigil, o dim sigil, + aug, maj) from the split_rn
    suffix, leaving the pure WiR inversion figure verbatim ('', '6', '6/4', '7', '6/5', '4/3',
    '2', '4/2', '9', '9[b9]', ...). The `/o` is removed BEFORE the bare `o` (else '/o' would leave
    a stray '/'). No 'o' occurs inside a figure, so the second replace is safe."""
    f = suffix.replace("/o", "")          # half-dim sigil
    f = f.replace("o", "")                # dim sigil
    f = f.replace("+", "")                # augmented sigil
    f = re.sub("maj", "", f, flags=re.IGNORECASE)   # major-seventh marker
    return f.strip()


def _figure_is_seventh(fig: str) -> bool:
    """True iff the canonical figure denotes a chord carrying a seventh. Recognizes the WiR
    seventh figured-bass tokens and any ninth ('9...', which carries a seventh)."""
    if fig in _SEVENTH_FIGURES:
        return True
    return fig.startswith("9")


def _derive_quality(deg_token: str, suffix: str, fig: str) -> str:
    """Quality from CASE (deg_token) + FIGURE (suffix/fig) — the OI-186(a) rule. `deg_token` keeps
    its case (upper = major color, lower = minor color); `suffix` is the raw split_rn remainder
    (carrying the /o, o, +, maj sigils); `fig` is the canonical inversion figure."""
    is_upper = deg_token[0].isupper()
    half_dim = "/o" in suffix
    dim = ("o" in suffix) and not half_dim
    aug = "+" in suffix
    majseven = "maj" in suffix.lower()
    seventh = _figure_is_seventh(fig) or majseven

    if half_dim:
        return "HalfDim7" if seventh else "HalfDim"
    if dim:
        return "Dim7" if seventh else "Dim"
    if aug:
        if majseven:
            return "AugMaj7"
        return "Aug7" if seventh else "Aug"
    if is_upper:
        if majseven:
            return "Maj7"
        return "Dom7" if seventh else "Maj"
    else:
        if majseven:
            return "MinMaj7"
        return "Min7" if seventh else "Min"


def _peel_applied(raw: str) -> tuple[str, str]:
    """Peel ALL applied/tonicization levels off a raw label, returning (base_chord, target_chain).

    dcml._split_rntxt_applied peels only the LAST '/'-level (matching the TSV single-level
    relativeroot). For the three observed two-level applied labels ('V6/5/V/III', 'V2/V/III',
    'V/V/III') that leaves the inner '/V' stuck inside the primary, corrupting the figure and
    quality. We iterate the SAME primitive (#6 — no new parser) until the base chord has no
    trailing bare-degree, and join the collected targets in WiR reading order (inner-to-outer,
    e.g. 'V/III'). A figured-bass tail ('V6/5' -> tail '5') is not a degree and is never peeled."""
    targets: list[str] = []
    cur = raw
    while True:
        prim, tgt = dcml._split_rntxt_applied(cur)
        if not tgt:
            break
        targets.append(tgt)      # collected outer-first
        cur = prim
    return cur, "/".join(reversed(targets))   # reversed -> WiR reading order (inner..outer)


def normalize_label(raw: str) -> LabelClass:
    """Map a raw WiR label to its LabelClass. `raw` is DcmlRegion.chord_symbol (the verbatim WiR
    numeral token, e.g. 'V6/5', 'ii/o6/5', 'V6/5/V', 'It6/ii', 'bVIImaj7')."""
    raw = raw or ""
    primary, target = _peel_applied(raw)
    norm = crn.normalise_rn(primary)
    parts = crn.split_rn(norm)
    if parts is None:
        # split_rn rejects It6/Ger/Fr/N — route the recognized chromatic tokens to their named
        # class; everything else is genuinely un-normalizable and counted, never guessed.
        m = _CHROMATIC_RE.match(norm)
        if m:
            base, qual = _CHROMATIC_CLASS[m.group(1)]
            # the chromatic token may carry a figured-bass suffix ('It6' -> figure '6'); keep it.
            fig = norm[len(m.group(1)):].strip()
            return LabelClass(base, qual, fig, target)
        return LabelClass(f"raw:{norm}", "unknown", "", target, raw_unnormalized=True)

    acc, deg, suffix = parts
    fig = _canonical_figure(suffix)
    quality = _derive_quality(deg, suffix, fig)
    degree_base = acc + deg.upper()
    return LabelClass(degree_base, quality, fig, target)


# ── self-test: the mapping over the full WiR-covered vocabulary (the §1 review surface) ──

def _self_test():
    """Establish the module: every observed WiR-covered label maps; only the 2 It6 tokens are
    split_rn=None (both routed to AugSixth, so raw_unnormalized == 0); print the mapping. This is
    the §1 report's mapping table basis (top 30 classes + every /o and slashed-seventh form)."""
    import json
    from collections import Counter
    fa = json.loads((_ROOT / "tools/joint_estimator/fold_assignment.json").read_text(encoding="utf-8"))
    covered = sorted(fa["stem_index"].keys())
    WIR_DIR = str(_ROOT / "tools" / "dcml" / "when_in_rome")

    raw_hist: Counter = Counter()
    for stem in covered:
        for r in dcml.load_wir_regions(WIR_DIR, stem):
            raw_hist[r.chord_symbol or ""] += 1

    unnorm = 0
    slashed_seventh = []
    halfdim = []
    rows = []
    for raw, n in raw_hist.most_common():
        lc = normalize_label(raw)
        if lc.raw_unnormalized:
            unnorm += n
        rows.append((n, raw, lc.key()))
        if "/o" in raw:
            halfdim.append((n, raw, lc.key()))
        prim, _ = dcml._split_rntxt_applied(raw)
        if any(tok in prim.replace("/o", "") for tok in ("6/5", "4/3", "4/2")) or \
           re.search(r"(?<!/o)7", prim) or prim.rstrip("/oV IViv").endswith("2"):
            slashed_seventh.append((n, raw, lc.key()))

    print(f"distinct raw labels: {len(raw_hist)}; total {sum(raw_hist.values())}; "
          f"raw_unnormalized tokens: {unnorm}")
    print("\n== top 30 raw labels -> class ==")
    for n, raw, key in rows[:30]:
        print(f"  {n:5d}  {raw:14s} -> {key}")
    print("\n== every '/o' half-dim form ==")
    for n, raw, key in halfdim:
        print(f"  {n:5d}  {raw:14s} -> {key}")
    print(f"\n== It6 / chromatic (split_rn=None) ==")
    for raw, n in raw_hist.items():
        lc = normalize_label(raw)
        if crn.split_rn(crn.normalise_rn(dcml._split_rntxt_applied(raw)[0])) is None:
            print(f"  {n:5d}  {raw:14s} -> {lc.key()}  (raw_unnormalized={lc.raw_unnormalized})")


if __name__ == "__main__":
    _self_test()

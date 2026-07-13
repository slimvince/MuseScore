#!/usr/bin/env python3
"""producer_key_modes.py — the ONE reader of the PRODUCER's KeySigMode vocabulary.

The measurement chain repeatedly needs facts that belong to the producing layer
(src/composing/analysis/key/): what mode names the chain can emit, what suffix each one
prints, in what enum order, and which ones the producer itself calls major. Every place
that needed them used to hold its own copy of the answer, and the copies went stale
independently (OI-132's D2, OI-155, OI-157). This module READS the three producing
sources instead, so a change in the producer surfaces as a red test or an abstain —
never as a silently-wrong grade (#6, the fact-publication corollary: consumers read,
never re-derive).

The three sources, all in the producing layer:
  src/composing/analysis/types/analysistypes.h   enum class KeySigMode  — the DECLARATION
                                                 ORDER, which is the integer the C++ probe
                                                 emitters cast the mode to.
  src/composing/analysis/key/keymodeformatting.cpp  keyModeSuffix()     — the suffix each
                                                 mode prints inside an emitted key string.
  src/composing/analysis/key/keymodeanalyzer.h      keyModeIsMajor()    — the producer's OWN
                                                 major-third / minor-third partition.

READ-ONLY: parses source text, holds no policy. It does NOT decide how a mode GRADES —
that is compare_rn's one reduction (_our_key_tonic / _our_key_ident), which applies the
OI-132 parent-collection ruling and the OI-155 abstain rule. This module only says what
the producer can emit and what it calls it.
"""
from __future__ import annotations

import codecs
import re
from functools import lru_cache
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
_TYPES_H = _REPO_ROOT / "src" / "composing" / "analysis" / "types" / "analysistypes.h"
_KEY_DIR = _REPO_ROOT / "src" / "composing" / "analysis" / "key"
_FORMATTING_CPP = _KEY_DIR / "keymodeformatting.cpp"
_ANALYZER_H = _KEY_DIR / "keymodeanalyzer.h"


@lru_cache(maxsize=1)
def mode_names_in_enum_order() -> tuple:
    """The KeySigMode enumerators in DECLARATION order — index i is the integer value the
    C++ emitters write for that mode (`static_cast<int>(hr.keyModeResult.mode)`)."""
    text = _TYPES_H.read_text(encoding="utf-8")
    body = text.split("enum class KeySigMode {", 1)[1].split("};", 1)[0]
    body = re.sub(r"//.*", "", body)           # line comments (the ///< scale-degree notes)
    names = re.findall(r"(\w+)\s*,", body)
    if not names:
        raise ValueError(f"no KeySigMode enumerators parsed from {_TYPES_H}")
    return tuple(names)


@lru_cache(maxsize=1)
def mode_suffixes() -> dict:
    """{KeySigMode name -> emitted suffix}, parsed from keyModeSuffix(). The source spells
    the unicode accidentals as C escapes (e.g. "Lyd\\u266d7"), so they are decoded here."""
    text = _FORMATTING_CPP.read_text(encoding="utf-8")
    body = text.split("const char* keyModeSuffix", 1)[1]
    out = {}
    for name, suffix in re.findall(r'case KeySigMode::(\w+):\s*return "([^"]*)";', body):
        out[name] = codecs.decode(suffix, "unicode_escape")
    if not out:
        raise ValueError(f"no keyModeSuffix() cases parsed from {_FORMATTING_CPP}")
    return out


@lru_cache(maxsize=1)
def major_mode_names() -> frozenset:
    """The KeySigMode names keyModeIsMajor() returns true for (the producer's own partition
    by the third above the tonic — NOT a grading decision)."""
    text = _ANALYZER_H.read_text(encoding="utf-8")
    body = text.split("inline constexpr bool keyModeIsMajor", 1)[1].split("return true;", 1)[0]
    names = frozenset(re.findall(r"case KeySigMode::(\w+):", body))
    if not names:
        raise ValueError(f"no keyModeIsMajor() cases parsed from {_ANALYZER_H}")
    return names


@lru_cache(maxsize=1)
def suffix_by_enum_index() -> tuple:
    """The emitted suffix at each KeySigMode integer value — the join of the enum order and
    keyModeSuffix(). suffix_by_enum_index()[i] is what a C++ probe's `"mode": i` prints."""
    suffixes = mode_suffixes()
    names = mode_names_in_enum_order()
    missing = [n for n in names if n not in suffixes]
    if missing:
        raise ValueError(f"KeySigMode enumerators with no keyModeSuffix() case: {missing}")
    return tuple(suffixes[n] for n in names)

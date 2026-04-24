#!/usr/bin/env python3
"""
fix_keysig.py — Fix key-signature mismatches in corpus MusicXML files.

For the ~46 corpus files where the MusicXML key signature doesn't match
music21's detected key (Baroque Dorian notation + 5 other outliers), this
script patches the <fifths> and <mode> elements in-place so that our
declared-mode constraint points at the right tonic.

Skips the 16 "dominant-detection" files (music21 finds V instead of I) —
those are algorithmic interpretation differences, not data errors.

Usage:
    python tools/fix_keysig.py --dry-run   # show what would change
    python tools/fix_keysig.py             # apply changes in-place
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# ── Key string → (fifths, mode) ──────────────────────────────────────────────
# Music21 uses note names like "d minor", "B- major", "f# minor".
# We need to map these to MusicXML <fifths> (circle-of-fifths offset) and <mode>.

NOTE_TO_FIFTHS = {
    # Major tonics (Ionian)
    'c':  0, 'g':  1, 'd':  2, 'a':  3, 'e':  4, 'b':  5,
    'f#': 6, 'c#': 7,
    'f': -1, 'bb':-2, 'eb':-3, 'ab':-4, 'db':-5, 'gb':-6, 'cb':-7,
    # Flat-notation aliases
    'b-':-2, 'e-':-3, 'a-':-4, 'd-':-5, 'g-':-6, 'c-':-7,
}
# Relative-minor tonic → fifths of its relative major
MINOR_ROOT_TO_FIFTHS = {
    'a':  0, 'e':  1, 'b':  2, 'f#': 3, 'c#': 4, 'g#': 5, 'd#': 6,
    'd': -1, 'g': -2, 'c': -3, 'f': -4, 'bb':-5, 'eb':-6,
    'b-':-5, 'e-':-6,
}


def key_string_to_fifths_mode(key: str) -> tuple[int, str] | None:
    """Convert music21 key string ('d minor', 'B- major') → (fifths, mode)."""
    key = key.strip().lower()
    parts = key.split()
    if len(parts) < 2:
        return None
    root, mode = parts[0], parts[1]
    # Normalise flat symbol
    root = root.replace('-', 'b')
    if mode == 'major':
        fifths = NOTE_TO_FIFTHS.get(root)
    else:
        fifths = MINOR_ROOT_TO_FIFTHS.get(root)
    if fifths is None:
        return None
    return fifths, mode


# ── Dominant-detection files: skip these (algorithmic, not data errors) ──────
# These are files where music21 detects the dominant key rather than the tonic.
# We identify them by the detected key being 1 fifth above the key signature.
def is_dominant_detection(fifths_declared: int, detected_key: str) -> bool:
    result = key_string_to_fifths_mode(detected_key)
    if result is None:
        return False
    fifths_detected, mode_detected = result
    mode_declared_is_major = True  # if detected is major, compare as ionian tonics
    # The dominant is 1 fifth above the tonic (fifths + 1)
    return (fifths_detected == fifths_declared + 1 and
            mode_detected == 'major')


def patch_xml(xml_text: str, new_fifths: int, new_mode: str) -> str:
    """Replace the first <fifths>…</fifths> and <mode>…</mode> in the XML."""
    xml_text = re.sub(r'(<fifths>)\s*-?\d+\s*(</fifths>)',
                      lambda m: f'{m.group(1)}{new_fifths}{m.group(2)}',
                      xml_text, count=1)
    if re.search(r'<mode>', xml_text):
        xml_text = re.sub(r'(<mode>)\s*\w+\s*(</mode>)',
                          lambda m: f'{m.group(1)}{new_mode}{m.group(2)}',
                          xml_text, count=1)
    else:
        # Insert <mode> after the first </fifths>
        xml_text = xml_text.replace('</fifths>',
                                    f'</fifths>\n          <mode>{new_mode}</mode>',
                                    1)
    return xml_text


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dry-run', action='store_true',
                        help='Print changes without writing files')
    args = parser.parse_args()

    for candidate in [Path('tools/corpus'), Path('tools/tools/corpus'),
                      Path('../tools/corpus')]:
        if candidate.exists():
            corpus_dir = candidate
            break
    else:
        print('ERROR: cannot find corpus directory', file=sys.stderr)
        sys.exit(1)

    FIFTHS_TO_IONIAN = {-7:'Cb',-6:'Gb',-5:'Db',-4:'Ab',-3:'Eb',-2:'Bb',
                        -1:'F', 0:'C', 1:'G', 2:'D', 3:'A', 4:'E', 5:'B',
                         6:'F#', 7:'C#'}
    IONIAN_AEOLIAN = {'C':'a','G':'e','D':'b','A':'f#','E':'c#','B':'g#',
                      'F#':'d#','Cb':'ab','Gb':'eb','Db':'bb','Ab':'f',
                      'Eb':'c','Bb':'g','F':'d'}
    def norm(s): return (s.replace('B-','Bb').replace('E-','Eb')
                          .replace('A-','Ab').replace('D-','Db')
                          .replace('G-','Gb').replace('C-','Cb'))

    fixed = skipped_dominant = already_ok = errors = 0

    for xml_path in sorted(corpus_dir.glob('*.xml')):
        if '_m21' in xml_path.name:
            continue
        m21_path = xml_path.parent / (xml_path.name[:-4] + '.music21.json')
        if not m21_path.exists():
            continue

        xml = xml_path.read_text(encoding='utf-8', errors='ignore')
        fifths_m = re.search(r'<fifths>\s*(-?\d+)\s*</fifths>', xml)
        mode_m   = re.search(r'<mode>\s*(\w+)\s*</mode>', xml)
        if not fifths_m:
            continue
        fifths_cur = int(fifths_m.group(1))
        mode_cur   = mode_m.group(1).lower() if mode_m else 'major'
        ion = FIFTHS_TO_IONIAN.get(fifths_cur, '?')
        rel = IONIAN_AEOLIAN.get(ion, '?')

        with open(m21_path, encoding='utf-8') as f:
            detected = norm(json.load(f).get('detectedKey', '?'))
        det_root = detected.split()[0].lower().replace('-', 'b')
        expected = {norm(ion).lower(), norm(rel).lower()}

        if det_root in expected:
            already_ok += 1
            continue

        # Skip dominant-detection cases
        if is_dominant_detection(fifths_cur, detected):
            skipped_dominant += 1
            continue

        # Compute target key sig
        result = key_string_to_fifths_mode(detected)
        if result is None:
            print(f'  SKIP (cannot parse): {xml_path.name[:50]}  detected={detected!r}',
                  file=sys.stderr)
            errors += 1
            continue

        new_fifths, new_mode = result
        bwv = (re.search(r'(bwv[\w.]+)\.mxl', xml_path.name) or
               type('',(),{'group':lambda s,n:xml_path.stem[:15]})()).group(1)

        if args.dry_run:
            old_key = f'{ion} {mode_cur}'
            print(f'  {bwv:<12}  {old_key:>14}  ->  fifths={new_fifths} mode={new_mode}'
                  f'  (detected: {detected})')
        else:
            new_xml = patch_xml(xml, new_fifths, new_mode)
            xml_path.write_text(new_xml, encoding='utf-8')
            print(f'  Fixed: {bwv}  ({ion} {mode_cur} -> {detected})')

        fixed += 1

    action = 'Would fix' if args.dry_run else 'Fixed'
    print(f'\n{action}: {fixed}  |  Already correct: {already_ok}'
          f'  |  Dominant-detection (skipped): {skipped_dominant}'
          f'  |  Errors: {errors}')


if __name__ == '__main__':
    main()

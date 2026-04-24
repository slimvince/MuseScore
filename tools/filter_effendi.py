from __future__ import annotations

import glob
import os
import xml.etree.ElementTree as ET


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def count_elements(root: ET.Element, name: str) -> int:
    return sum(1 for element in root.iter() if local_name(element.tag) == name)


def qualifies(path: str) -> tuple[bool, str]:
    try:
        tree = ET.parse(path)
        root = tree.getroot()

        harmonies = count_elements(root, "harmony")
        if harmonies == 0:
            return False, "no harmony tags"

        parts = count_elements(root, "part")
        if parts != 1:
            return False, f"{parts} parts"

        notes = count_elements(root, "note")
        if notes < 10:
            return False, f"only {notes} notes"

        return True, f"{harmonies} harmony, {notes} notes"
    except Exception as exc:
        return False, str(exc)


def main() -> int:
    files = sorted(glob.glob("tools/corpus_effendi_src/*.xml"))
    passing: list[str] = []

    for path in files:
        ok, reason = qualifies(path)
        status = "PASS" if ok else "SKIP"
        print(f"{status}: {os.path.basename(path)} - {reason}")
        if ok:
            passing.append(path)

    print(f"\n{len(passing)}/{len(files)} files qualify")

    with open("tools/effendi_qualifying.txt", "w", encoding="utf-8") as out:
        for path in passing:
            out.write(path + "\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
import os
import tarfile
import urllib.request
import xml.etree.ElementTree as ET
import zipfile

import pandas as pd


MXL_TAR_URL = "https://zenodo.org/api/records/15571083/files/mxl.tar.gz/content"


candidates = pd.read_csv(r"C:\s\MS\tools\pdmx\jazz_candidates.csv")
top5 = candidates.head(5)

os.makedirs(r"C:\s\MS\tools\pdmx\spot_check", exist_ok=True)

targets = {}
for _, row in top5.iterrows():
    mxl_path = row["mxl"]
    if pd.isna(mxl_path):
        print(f"SKIP (no mxl): {row['title']}")
        continue

    member_name = str(mxl_path).lstrip("./")
    targets[member_name] = row

found = set()

with urllib.request.urlopen(MXL_TAR_URL) as response:
    with tarfile.open(fileobj=response, mode="r|gz") as tar:
        for member in tar:
            if member.name not in targets:
                continue

            row = targets[member.name]
            fname = os.path.basename(member.name)
            local = rf"C:\s\MS\tools\pdmx\spot_check\{fname}"

            print(
                f"Downloading: {row['title']} ({row['n_tracks']} tracks, "
                f"rating={row['rating']:.2f})"
            )

            extracted = tar.extractfile(member)
            if extracted is None:
                print("  ERROR: could not extract member from tar")
                found.add(member.name)
                continue

            mxl_bytes = extracted.read()
            with open(local, "wb") as handle:
                handle.write(mxl_bytes)

            try:
                with zipfile.ZipFile(local, "r") as z:
                    score_member = None
                    if "META-INF/container.xml" in z.namelist():
                        container_root = ET.fromstring(z.read("META-INF/container.xml"))
                        rootfile = container_root.find(".//rootfile")
                        if rootfile is not None:
                            score_member = rootfile.attrib.get("full-path")

                    if not score_member:
                        xml_files = [
                            f for f in z.namelist()
                            if (f.endswith(".xml") or f.endswith(".musicxml"))
                            and not f.startswith("META-INF/")
                        ]
                        if xml_files:
                            score_member = xml_files[0]

                    if not score_member:
                        print("  No score XML inside zip")
                        found.add(member.name)
                        continue

                    xml_content = z.read(score_member).decode("utf-8", errors="ignore")

                harmony_count = xml_content.count("<harmony>")
                parts_count = xml_content.count("<part id=")
                note_count = xml_content.count("<note>")

                print(f"  harmony elements: {harmony_count}")
                print(f"  parts: {parts_count}")
                print(f"  notes: {note_count}")
                print(f"  USABLE: {harmony_count > 5}")
            except Exception as e:
                print(f"  ERROR: {e}")

            found.add(member.name)
            if len(found) == len(targets):
                break

missing = [name for name in targets if name not in found]
for name in missing:
    print(f"MISSING in mxl.tar.gz: {targets[name]['title']}")
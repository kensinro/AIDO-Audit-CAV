from __future__ import annotations
import csv, hashlib
from pathlib import Path

def sha256_file(path, chunk_size=1024*1024):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        while True:
            b = f.read(chunk_size)
            if not b:
                break
            h.update(b)
    return h.hexdigest()

def build_manifest(directory, manifest_name="PACKAGE_MANIFEST_SHA256.csv"):
    directory = Path(directory)
    rows = []
    for p in sorted(directory.rglob("*")):
        if p.is_file() and p.name != manifest_name and "__pycache__" not in p.parts:
            rows.append({"file":p.relative_to(directory).as_posix(),"sha256":sha256_file(p),"bytes":p.stat().st_size})
    return rows

def verify_manifest(directory, manifest_name="PACKAGE_MANIFEST_SHA256.csv"):
    directory = Path(directory)
    failures = []
    with (directory/manifest_name).open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            p = directory/row["file"]
            if not p.exists():
                failures.append((row["file"], "MISSING"))
                continue
            if sha256_file(p) != row["sha256"]:
                failures.append((row["file"], "SHA256_MISMATCH"))
            if p.stat().st_size != int(row["bytes"]):
                failures.append((row["file"], "BYTE_COUNT_MISMATCH"))
    return failures

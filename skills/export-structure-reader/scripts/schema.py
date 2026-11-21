#!/usr/bin/env python3
"""Print the structure of a data export without printing personal values.

Usage: python3 -I schema.py <folder-or-zip>
Handles JSON (objects, lists, or {"data": [...]}) and CSV. Prints file names,
row counts, field names, value types, and string lengths only.
"""
import csv, io, json, os, re, stat, sys, zipfile
from collections import Counter, defaultdict

MAX_MEMBER_BYTES = 200 * 1024 * 1024  # skip any file or zip member larger than this

def mask(key):
    """Return the key, or <key len=N> if it could hold personal data."""
    k = str(key)
    if "@" in k or " " in k or len(re.findall(r"\d", k)) > 3 or len(k) > 40:
        return f"<key len={len(k)}>"
    return k

def mpath(p):
    return "/".join(mask(x) for x in str(p).split("/"))

HEADER_WORDS = {"id", "name", "email", "created_at", "updated_at", "type", "status", "count"}

def clear_header_cell(c):
    """True if a cell is clearly a column name, not a person's name or a value."""
    if c.lower() in HEADER_WORDS:
        return True
    if "_" in c.strip("_"):
        return True
    if re.search(r"[a-z][A-Z]", c):
        return True
    return False

def looks_like_header(row):
    """A first CSV row counts as a header only if every cell looks like a column name,
    and a row of short plain words counts only if some cell is a clear header."""
    if not row or any(c.strip() == "" for c in row):
        return False
    if len(set(row)) != len(row):
        return False
    for c in row:
        if len(c) > 40 or "@" in c:
            return False
        if len(re.findall(r"\d", c)) > 3:
            return False
        if re.fullmatch(r"[\d\W_]+", c):
            return False
    if not all(re.fullmatch(r"[A-Za-z][A-Za-z0-9_ ]{0,39}", c) for c in row):
        return False
    return any(clear_header_cell(c) for c in row)

def typename(v):
    if v is None: return "null"
    if isinstance(v, bool): return "bool"
    if isinstance(v, (int, float)): return type(v).__name__
    if isinstance(v, str): return "str"
    if isinstance(v, list): return "list"
    if isinstance(v, dict): return "dict"
    return type(v).__name__

def rows_of(obj):
    if isinstance(obj, dict) and "data" in obj and isinstance(obj["data"], list):
        return obj["data"]
    if isinstance(obj, list):
        return obj
    if isinstance(obj, dict):
        return [obj]
    return []

def describe(name, rows):
    fields = defaultdict(Counter)
    nested = defaultdict(set)
    for r in rows:
        if not isinstance(r, dict):
            fields["<value>"][typename(r)] += 1
            continue
        for k, v in r.items():
            mk = mask(k)
            fields[mk][typename(v)] += 1
            if isinstance(v, dict):
                nested[mk].update(mask(x) for x in v.keys())
    print(f"\n== {name}  rows={len(rows)}")
    for k in sorted(fields):
        types = ", ".join(f"{t}:{c}" for t, c in fields[k].most_common())
        extra = f"  keys={sorted(nested[k])[:25]}" if nested[k] else ""
        print(f"  {k}: {types}{extra}")

def handle(name, data):
    lower = name.lower()
    try:
        if lower.endswith(".json"):
            describe(mpath(name), rows_of(json.loads(data.decode("utf-8"))))
        elif lower.endswith(".csv"):
            all_rows = list(csv.reader(io.StringIO(data.decode("utf-8", "replace"))))
            if not all_rows:
                describe(mpath(name), [])
            elif looks_like_header(all_rows[0]):
                header = all_rows[0]
                body = [dict(zip(header, r)) for r in all_rows[1:]]
                describe(mpath(name), body)
            else:
                print(f"\n== {mpath(name)}  <headerless or ambiguous csv: {len(all_rows[0])} columns>")
        else:
            print(f"\n== {mpath(name)}  (skipped: {len(data)} bytes, unsupported type)")
    except Exception as e:
        print(f"\n== {mpath(name)}  (could not parse: {type(e).__name__})")

def main(path):
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as z:
            for info in sorted(z.infolist(), key=lambda i: i.filename):
                n = info.filename
                if n.endswith("/"):
                    continue
                mode = info.external_attr >> 16
                if stat.S_ISLNK(mode):
                    print(f"\n== {mpath(n)}  (skipped: symlink)")
                elif info.file_size > MAX_MEMBER_BYTES:
                    print(f"\n== {mpath(n)}  (skipped: larger than {MAX_MEMBER_BYTES} bytes)")
                else:
                    handle(n, z.read(info))
    else:
        for root, _, files in os.walk(path):
            for f in sorted(files):
                p = os.path.join(root, f)
                rel = os.path.relpath(p, path)
                if os.path.islink(p):
                    print(f"\n== {mpath(rel)}  (skipped: symlink)")
                elif os.path.getsize(p) > MAX_MEMBER_BYTES:
                    print(f"\n== {mpath(rel)}  (skipped: larger than {MAX_MEMBER_BYTES} bytes)")
                else:
                    with open(p, "rb") as fh:
                        handle(rel, fh.read())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])

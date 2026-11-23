#!/usr/bin/env python3
"""Check the guide: relative links, heading anchors and the verification line.

Usage: python3 scripts/check.py [--max-age-days N]
Exit code 1 if any check fails. Standard library only.
"""
import datetime, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEVELS = {"tested", "read", "web"}
STATUS = re.compile(r"^> Last verified: (\d{4}-\d{2}-\d{2}) · Level: (\w+) · Basis: .+$", re.M)
EXEMPT = {ROOT / "README.md", ROOT / "CONTRIBUTING.md"}


def slug(heading: str) -> str:
    h = re.sub(r"[`*]", "", heading.strip().lower())
    return re.sub(r"\s", "-", re.sub(r"[^\w\s-]", "", h))


def main() -> int:
    max_age = None
    if "--max-age-days" in sys.argv:
        max_age = int(sys.argv[sys.argv.index("--max-age-days") + 1])
    bad = 0
    today = datetime.date.today()
    for p in sorted(ROOT.rglob("*.md")):
        if ".git" in p.parts:
            continue
        rel = p.relative_to(ROOT)
        text = p.read_text()
        for m in re.finditer(r"\]\(([^)\s]+)\)", text):
            t = m.group(1)
            if t.startswith(("http", "mailto")):
                continue
            path, _, anchor = t.partition("#")
            f = (p.parent / path).resolve() if path else p
            if not f.exists():
                print(f"BROKEN  {rel} -> {t}"); bad += 1; continue
            if anchor and f.suffix == ".md":
                heads = {slug(l.lstrip("#")) for l in f.read_text().split("\n") if l.startswith("#")}
                if anchor not in heads:
                    print(f"ANCHOR  {rel} -> {t}"); bad += 1
        if p in EXEMPT:
            continue
        m = STATUS.search(text)
        if not m:
            print(f"STATUS  {rel}: missing 'Last verified' line"); bad += 1; continue
        if m.group(2) not in LEVELS:
            print(f"LEVEL   {rel}: level must be one of {sorted(LEVELS)}"); bad += 1
        age = (today - datetime.date.fromisoformat(m.group(1))).days
        if max_age is not None and age > max_age:
            print(f"STALE   {rel}: verified {age} days ago"); bad += 1
    print("PASS" if not bad else f"FAIL ({bad})")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

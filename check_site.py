#!/usr/bin/env python3
"""Lightweight sanity checks for this small GitHub Pages site."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
REQUIRED_FILES = [
    "_config.yml",
    "index.html",
    "404.html",
    "_layouts/default.html",
    "_includes/index.md",
    "_includes/scripts.html",
    "css/solo.css",
]
DISALLOWED_PATTERNS = [
    re.compile(r"http://api\.forismatic\.com"),
    re.compile(r"format=jsonp", re.IGNORECASE),
]


def fail(message):
    print(f"ERROR: {message}")
    return 1


def main():
    errors = 0

    for relative_path in REQUIRED_FILES:
        path = ROOT / relative_path
        if not path.exists():
            errors += fail(f"Missing required file: {relative_path}")
        elif path.is_file() and path.stat().st_size == 0:
            errors += fail(f"Required file is empty: {relative_path}")

    for path in ROOT.rglob("*"):
        if ".git" in path.parts or "node_modules" in path.parts or not path.is_file():
            continue
        if path.name == Path(__file__).name:
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for pattern in DISALLOWED_PATTERNS:
            if pattern.search(text):
                errors += fail(f"Disallowed legacy script/API reference in {path.relative_to(ROOT)}")

    layout = (ROOT / "_layouts/default.html").read_text(encoding="utf-8")
    for expected in ["<html lang=\"en\">", "meta name=\"description\"", "rel=\"canonical\""]:
        if expected not in layout:
            errors += fail(f"Layout missing expected markup: {expected}")

    homepage = (ROOT / "_includes/index.md").read_text(encoding="utf-8")
    for expected in ["Hello", "Email", "LinkedIn", "GitHub", "Thought prompt"]:
        if expected not in homepage:
            errors += fail(f"Homepage missing expected content: {expected}")

    scripts = (ROOT / "_includes/scripts.html").read_text(encoding="utf-8")
    for expected in ["quotes", "quoteForToday", "textContent", "shownQuoteIndexes", "randomUnshownQuote"]:
        if expected not in scripts:
            errors += fail(f"Quote script missing expected implementation detail: {expected}")

    quote_count = len(re.findall(r"\{\s*text:\s*\"", scripts))
    if quote_count < 50:
        errors += fail(f"Expected at least 50 local quotes, found {quote_count}")

    if errors:
        print(f"\n{errors} check(s) failed.")
        return 1

    print("All site sanity checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

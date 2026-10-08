#!/usr/bin/env python3
"""Check that src/llms.txt is in sync with src/SUMMARY.md.

src/llms.txt is maintained by hand. This script fails (exit code 1) when:
  1. a portal link in llms.txt points to a page that does not exist in src/,
  2. a page listed in SUMMARY.md is missing from llms.txt,
  3. the "Current SDK version" in llms.txt is not the newest version in
     SUMMARY.md, or the release notes page of that version is not linked.

Usage (from the repository root): python3 tools/check_llms_txt.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
LLMS_TXT = SRC / "llms.txt"
SUMMARY = SRC / "SUMMARY.md"

PORTAL_URL = "https://steinbergmedia.github.io/vst3_dev_portal/pages/"

# Pages from SUMMARY.md that are intentionally not listed in llms.txt
# (pure index pages or redirect stubs without own content).
NOT_LISTED = {
    "pages/Getting+Started/Index.md",
    "pages/Tutorials/Building+the+examples/Index.md",
    "pages/Technical+Documentation/Locations+Format/Snapshots.md",
    "pages/What+is+the+VST+3+SDK/iOS+Inter-App+Audio+support.md",
}

# Release notes pages are covered by the "Change History" link,
# only the newest version is checked (see check_version).
VERSION_PAGE = re.compile(r"^pages/Versions/Version\+([0-9.]+)\.md$")


def url_to_source(url):
    """Map a rendered portal URL to its Markdown source path (relative to src/)."""
    path = url[len(PORTAL_URL):]
    if path == "index.html":
        return "pages/README.md"
    return "pages/" + path[: -len(".html")] + ".md"


def version_key(version):
    return tuple(int(part) for part in version.split("."))


def main():
    llms = LLMS_TXT.read_text(encoding="utf-8")
    summary = SUMMARY.read_text(encoding="utf-8")
    errors = []

    # 1. every portal link must point to an existing page
    linked = set()
    for url in re.findall(r"\]\((" + re.escape(PORTAL_URL) + r"[^)]+\.html)\)", llms):
        source = url_to_source(url)
        if (SRC / source).is_file():
            linked.add(source)
        else:
            errors.append(f"broken link (no file src/{source}): {url}")

    # 2. every page from SUMMARY.md must be listed
    summary_pages = re.findall(r"\]\((pages/[^)]+\.md)\)", summary)
    for page in summary_pages:
        if page in linked or page in NOT_LISTED or VERSION_PAGE.match(page):
            continue
        errors.append(f"page from SUMMARY.md is missing in llms.txt: {page}")

    # 3. the current SDK version must be the newest one
    versions = [m.group(1) for p in summary_pages if (m := VERSION_PAGE.match(p))]
    if versions:
        newest = max(versions, key=version_key)
        match = re.search(r"Current SDK version: ([0-9.]+)", llms)
        if not match:
            errors.append('"Current SDK version: x.y.z" not found in llms.txt')
        elif match.group(1) != newest:
            errors.append(
                f"llms.txt says current SDK version {match.group(1)}, "
                f"but the newest version in SUMMARY.md is {newest}"
            )
        if f"pages/Versions/Version+{newest}.md" not in linked:
            errors.append(f"release notes of the newest version {newest} are not linked")

    if errors:
        print("src/llms.txt is not in sync with src/SUMMARY.md:")
        for error in errors:
            print(f"  - {error}")
        print("Please update src/llms.txt (see tools/UPDATE_LLMS_TXT.md).")
        return 1

    print(f"src/llms.txt OK ({len(linked)} pages linked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

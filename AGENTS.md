# Notes for AI coding agents

This repository is the Markdown source of the VST 3 Developer Portal (https://steinbergmedia.github.io/vst3_dev_portal). It is built with mdbook. There is no application code.

## Layout

- `src/SUMMARY.md`: table of contents. A page that is not listed here is not part of the portal.
- `src/pages/`: the pages. Folder and file names use `+` instead of spaces.
- `src/.vst3_tutorials/`: copy of the vst3_tutorials repository (git subtree), included with `{{#include}}`.
- `src/llms.txt`: overview of the portal for LLMs and AI coding agents (see below).
- `theme/`: custom mdbook theme.
- `tools/check_llms_txt.py`: checks that `src/llms.txt` is in sync with `src/SUMMARY.md`.

## Build and check

Use mdbook 0.4.x with mdbook-toc 0.14.x (mdbook-toc 0.15.x needs mdbook 0.5.x and fails). Tested: mdbook 0.4.52, mdbook-toc 0.14.2, mdbook-mermaid 0.10.0, mdbook-linkcheck 0.7.7.

```text
python3 tools/check_llms_txt.py
mdbook build
```

`mdbook serve` serves the portal at http://localhost:3000 but does not run linkcheck.

## Branches, commits and pull requests

- Create new branches from `deploy`. Pull requests target `deploy`.
- The maintainers mirror `deploy` to GitHub. Do not push to GitHub directly.
- Commit messages are in English and start with a tag: `[update]`, `[fix]`, `[new]`, `[typo]` or `[rename]`.
- Do not add tool or vendor attribution (for example `Co-Authored-By` trailers or "generated with" lines) to commits, pull requests or files. This repository is public.

## Page conventions

New pages follow the existing pages: a breadcrumb quote at the top, `[[_TOC_]]` under "On this page", and "Related pages". Interface pages in `Technical Documentation/Change+History/<version>/` list tags such as `\[plug imp\]` or `\[host imp\]`, `\[released: x.y.z\]` and `\[optional\]`, and link to the API reference at https://steinbergmedia.github.io/vst3_doc/.

## llms.txt

`src/llms.txt` is maintained by hand. Update it when pages in `src/SUMMARY.md` are added, renamed or removed, when the content of a listed page changes in a way that affects its description, and for every new SDK version. Follow [tools/UPDATE_LLMS_TXT.md](tools/UPDATE_LLMS_TXT.md).

`tools/check_llms_txt.py` only checks the structure. It does not check that descriptions and key facts are correct. Do not report the file as up to date only because the script passes.

# This is the source of the VST 3 Developer Portal

The source is written in Markdown and then build with [mdbook](https://github.com/rust-lang/mdBook) to generate HTML pages.

The current official generated VST 3 documentation is here: [https://steinbergmedia.github.io/vst3_dev_portal](https://steinbergmedia.github.io/vst3_dev_portal/pages/index.html)

## Requirements

- [mdbook](https://github.com/rust-lang/mdBook)
- [mdbook-mermaid](https://github.com/badboy/mdbook-mermaid)
- [mdbook-toc](https://github.com/badboy/mdbook-toc)
- [mdbook-linkcheck](https://github.com/Michael-F-Bryan/mdbook-linkcheck)

Install all of the above, so that the executables are in your environments path variable.

Use mdbook 0.4.x (not 0.5.x) and a matching mdbook-toc 0.14.x or older. mdbook-toc 0.15.x only works with mdbook 0.5.x. Tested versions:

``` text
cargo install mdbook --version 0.4.52 --locked
cargo install mdbook-toc --version 0.14.2 --locked
```

## Build

To build the HTML pages run [mdbook](https://github.com/rust-lang/mdBook) from the checkout folder of this repository

``` text
mdbook build
```

or alternatively you can build and serve the html pages locally with

``` text
mdbook serve
```

then you can locate you webbrowser to [http://localhost:3000](http://localhost:3000), the HTML pages will automatically be updated if you change the source files.

## llms.txt

The file [src/llms.txt](src/llms.txt) gives LLMs and AI coding agents a short overview of the portal with a link and a short description for each page (see [llmstxt.org](https://llmstxt.org)). It is published at `https://steinbergmedia.github.io/vst3_dev_portal/llms.txt`.

The file is maintained by hand. Please update it as described in [tools/UPDATE_LLMS_TXT.md](tools/UPDATE_LLMS_TXT.md) when you:

- add, rename or remove a page in [src/SUMMARY.md](src/SUMMARY.md),
- release a new SDK version (update "Current SDK version" and the release notes links in the "Optional" section).

To check that `src/llms.txt` is in sync with `src/SUMMARY.md`, run:

``` text
python3 tools/check_llms_txt.py
```

The GitHub workflow runs this check before the build and fails if the file is not in sync. If a page should intentionally not be listed in `src/llms.txt`, add it to `NOT_LISTED` in [tools/check_llms_txt.py](tools/check_llms_txt.py).

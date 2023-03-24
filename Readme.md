# This is the source of the VST 3 Developer Portal

The source is written in Markdown and then build with [mdbook](https://github.com/rust-lang/mdBook) to generate HTML pages.

The current official generated VST 3 documentation is here: [https://steinbergmedia.github.io/vst3_dev_portal](https://steinbergmedia.github.io/vst3_dev_portal/pages/index.html)

## Requirements

- [mdbook](https://github.com/rust-lang/mdBook)
- [mdbook-mermaid](https://github.com/badboy/mdbook-mermaid)
- [mdbook-toc](https://github.com/badboy/mdbook-toc)
- [mdbook-linkcheck](https://github.com/Michael-F-Bryan/mdbook-linkcheck)

Install all of the above, so that the executables are in your environments path variable.

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

# How to update src/llms.txt

`src/llms.txt` gives LLMs and AI coding agents an overview of the portal: a short summary, a list of key VST 3 facts, and a link with a one-line description for each page. Format: https://llmstxt.org

Do this for every SDK release and whenever pages are added, renamed, removed or changed in a way that affects their description.

## 1. Find what changed

Find the last commit that changed `src/llms.txt`, and list all changes in `src/` since then:

```text
LAST=$(git log -1 --format=%H -- src/llms.txt)
git log --oneline $LAST..HEAD -- src
git diff --stat $LAST..HEAD -- src ':!src/llms.txt'
```

Look at all changed pages, not only new ones. A changed page can make its description in `llms.txt` wrong.

## 2. Read the pages and update the entries

- Read each new or changed page. Write the description from the page content, not from its title.
- Descriptions: one line, plain English, say what the page explains. Use the interface name in backticks.
- Interface pages (section "Interface reference by SDK version"): use `[plug-in]` if the page says `\[plug imp\]`, and `[host]` if it says `\[host imp\]`. If an interface replaces an older one (`\[replaces ...\]`), say so in both entries.
- Put a new page in the same section as its neighbors in `src/SUMMARY.md`, in the same order.
- Links point to the rendered HTML page: `https://steinbergmedia.github.io/vst3_dev_portal/pages/<path>.html`, where `<path>` is the source path below `src/pages/` without `.md`. Exception: `src/pages/README.md` is `pages/index.html`.
- Pages without own content (index pages, redirect stubs) can be left out. Add them to `NOT_LISTED` in `tools/check_llms_txt.py`.

## 3. For a new SDK version

- Update "Current SDK version: x.y.z (yyyy/mm/dd)" in the summary at the top. Use the date from `src/SUMMARY.md`.
- In the "Optional" section, list the two newest versions with a short summary of their main changes (from `src/pages/Versions/Version+x.y.z.md`).
- Check the "Key facts" list against the release notes. For example, a new interface can replace an interface named there.

## 4. Check

```text
python3 tools/check_llms_txt.py
mdbook build
```

The script only checks the structure: broken links, missing pages, and the current SDK version. It does not check that the descriptions are correct. The GitHub workflow runs it before the build, so a failing check also stops the deployment of the portal.

Links to new pages return 404 on the public site until the change is deployed. Check them against `src/`, not online.

## 5. Report

In the pull request, say which entries you added or changed, and which pages you read. Keep "the script passes" and "the content was checked" apart.

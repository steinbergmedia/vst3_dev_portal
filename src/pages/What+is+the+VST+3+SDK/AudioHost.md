>/ [VST Home](../) / [What is the VST 3 SDK?](Index.md)
>
># AudioHost Application

**On this page:**

[[_TOC_]]

---

## AudioHost

As Cross-platform source code:
Simple cross-platform (only tested on Linux) host application allowing you to register a VST 3 plug-in with Jack Server. First, you have to download the Jack Audio SDK and application server (<http://www.jackaudio.org>).

- Windows (not tested):

``` c++
 audiohost.exe "C:\PATH_TO_PLUGIN"
```

- macOS (not tested)
- Linux: 

``` c++
audiohost PATH_TO_PLUGIN
```

On Windows and macOS, you can also drag and drop a **VST 3 plug-in** on the executable via Explorer/Finder.

Check the folder *"public.sdk/samples/vst-hosting/audiohost"* of the SDK!

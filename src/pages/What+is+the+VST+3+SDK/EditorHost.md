>/ [VST Home](../) / [What is the VST 3 SDK?](Index.md)
>
># EditorHost Application

**On this page:**

[[_TOC_]]

---

## EditorHost

As Cross-platform source code:
Simple cross-platform (Win/macOS/Linux) host application allowing you to open the editor of a **VST 3** plug-in (with HiDPI support on Windows/macOS). Call it from the command line: 

- Windows:

``` c++
 editorhost.exe "C:\PATH_TO_PLUGIN"
```

- macOS/Linux:

``` c++
editorhost PATH_TO_PLUGIN
```

On Windows and macOS you can also drag and drop a **VST 3** plug-in on the executable via Explorer/Finder.

Check the folder *"public.sdk/samples/vst-hosting/editorhost"* of the SDK!

>/ [VST Home](../../Index.md) / [Frequently Asked Questions](../FAQ/Index.md)
>
># GUI-Editor

[[_TOC_]]

---

## Q: The host doesn't open my plug-in UI, why?

If you are not using **[VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md)**, please check that you provide the correct object derived from [EditorView](https://steinbergmedia.github.io/vst3_doc/vstsdk/classSteinberg_1_1Vst_1_1EditorView.html) or [CPlugInView](https://steinbergmedia.github.io/vst3_doc/vstsdk/classSteinberg_1_1CPluginView.html#a7c25891fe7dde6dc274a0ac9f20890a4) and that you overwrite the function [isPlatformTypeSupported()](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugView.html#abcfa60e135807caa316f3915622d9488).
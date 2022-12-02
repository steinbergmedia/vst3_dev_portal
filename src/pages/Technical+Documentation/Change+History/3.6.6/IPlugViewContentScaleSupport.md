>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># \[3.6.6\] PlugView Content Scaling

**On this page:**

[[_TOC_]]

**Related pages:**

[Resize View Call Sequence](../../Workflow+Diagrams/Resize+View+Call+Sequence.md)

---

## Introduction

Plug-in view content scale support: [Vst::IPlugViewContentScaleSupport](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugViewContentScaleSupport.html)

- \[plug impl\]
- [extends [IPlugView](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugView.html)]
- \[released: 3.6.6\]
- \[optional\]

This interface communicates the content scale factor from the host to the plug-in view on systems where plug-ins cannot get this information directly like Microsoft Windows.

The host calls [setContentScaleFactor](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugViewContentScaleSupport.html#af5b0fea85beba3cdcfeb8de66779f478) directly after the plug-in view is attached and when the scale factor changes (system change or window moved to another screen with different scaling settings).

The host can call [setContentScaleFactor](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugViewContentScaleSupport.html#af5b0fea85beba3cdcfeb8de66779f478) in a different context, for example: scaling the plug-in editor for better readability.

When a plug-in handles this (by returning kResultTrue), it needs to scale the width and height of its view by the scale factor and inform the host via a [IPlugFrame::resizeView()](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugFrame.html#a94f218315acd695606fff41166294d56), the host will then call [IPlugView::onSize()](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugView.html#a3e741e55c2c047a4cc10f102661f5654).

>ⓘ **Note**\
>Note that the host is allowed to call [setContentScaleFactor()](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugViewContentScaleSupport.html#af5b0fea85beba3cdcfeb8de66779f478) at any time the [IPlugView](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugView.html) is valid.

>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># [3.7.0] Process Context Requirements

**On this page:**

[[_TOC_]]

---

## Introduction

Extended [IAudioProcessor](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html) interface for a component: [Vst::IProcessContextRequirements](https://steinbergmedia.github.io/vst3_doc/vstinterfaces//classSteinberg_1_1Vst_1_1IProcessContextRequirements.html)

- [plug imp]
- [extends [IAudioProcessor](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html)]
- [released: 3.7.0]
- [mandatory]

To get accurate process context information ([Vst::ProcessContext](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessContext.html)), it is now required to implement this interface and return the desired bit mask of flags which your audio effect needs. If you do not implement this interface, you may not get any information at all of the process function.

The host asks for this information once between initialize and setActive. It cannot be changed afterwards.

This gives the host the opportunity to better optimize the audio process graph when it knows which plug-ins need which information.

>⚠️ **Warning**\
>Plug-Ins built with an earlier SDK version (< 3.7) will still get the old information, but the information may not be as accurate as when using this interface.

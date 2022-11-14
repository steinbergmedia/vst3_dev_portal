>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># \[3.7.0\] Control Voltage Bus Flag

**On this page:**

[[_TOC_]]

**Related pages:**

- [\[3.0.0\] Multiple Dynamic I/O Support](../3.0.0/Multiple+Dynamic+IO.md)

---

## Introduction

 Extended struct BusInfo flags for a component: [Vst::IComponent::getBusInfo](https://steinbergmedia.github.io/vst3_doc/vstsdk/classSteinberg_1_1Vst_1_1Component.html#acf3030d7cf275010945d97a071abd2d8)

- \[plug imp\]
- [extends [IComponent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponent.html)]
- \[released: 3.7.0\]

The kIsControlVoltage flag allows the plug-in to inform the host that an audio bus does not contain ordinary audio data, but data used for control changes at sample rate.

The data is in the same format as the audio data \[-1.0, 1.0].

A host has to prevent unintended routing to speakers to prevent damage.

Only valid for audio media type busses.

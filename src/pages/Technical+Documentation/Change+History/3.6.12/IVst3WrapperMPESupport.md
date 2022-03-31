>/ [VST Home](../../../index.md) / [Technical Documentation](../../Index.md)
>
># [3.6.12] MPE support for Wrappers

**On this page:**

[[_TOC_]]

**Related pages:**

- [[3.5.0] Note Expression](../3.5.0/INoteExpressionController.md)
- [[3.6.11] NoteExpression Physical UI Mapping](../3.6.11/INoteExpressionPhysicalUIMapping.md)
- [About MIDI in VST 3](../../About+MIDI/Index.md)

---

## Introduction

Wrapper **MPE** Support interface: [Vst::IVst3WrapperMPESupport](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IVst3WrapperMPESupport.html)

- [host imp]
- [passed as 'context' to [IPluginBase::initialize()](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPluginBase.html#a3c81be4ff2e7bbb541d3527264f26eed) ]
- [released: 3.6.12]
- [optional]

Implemented on wrappers that support **MPE** ([MIDI Polyphonic Expression](https://www.midi.org/midi-articles/midi-polyphonic-expression-mpe)) to [Note Expression](../3.5.0/INoteExpressionController.md) translation.

>ⓘ **Note**<br>
>By default, **MPE** input processing is enabled, the masterChannel will be zero, the memberBeginChannel will be one and the memberEndChannel will be 14.

>ⓘ **Note**<br>
>As **MPE** is a subset of the VST 3 [Note Expression](../3.5.0/INoteExpressionController.md) feature, mapping from the three **MPE** expressions is handled via the [INoteExpressionPhysicalUIMapping](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1INoteExpressionPhysicalUIMapping.html) interface.
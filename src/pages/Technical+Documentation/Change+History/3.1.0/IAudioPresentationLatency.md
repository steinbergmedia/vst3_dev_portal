>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># \[3.0.1\] Parameter MIDI Mapping

**On this page:**

[[_TOC_]]

---

## Introduction

Extended [IAudioProcessor](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html) interface for a component: [Vst::IAudioPresentationLatency](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioPresentationLatency.html).

- \[plug imp\]
- [extends [IAudioProcessor](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html)]
- \[released: 3.1.0\]
- \[optional\]

Inform the plug-in about how long from the moment of generation/acquiring (from file or from Input) it will take for its input to arrive, and how long it will take for its output to be presented (to output or to speaker).Note for Input Presentation Latency: when reading from file, the first plug-in will have an input presentation latency set to zero. When monitoring audio input from an audio device, the initial input latency is the input latency of the audio device itself.

Note for Output Presentation Latency: when writing to a file, the last plug-in will have an output presentation latency set to zero. When the output of this plug-in is connected to an audio device, the initial output latency is the output latency of the audio device itself.

A value of zero either means no latency or an unknown latency.

Each plug-in adding a latency (returning a none zero value for [IAudioProcessor::getLatencySamples](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html#af8884671ccefe68e0a86e72413a0fcf8)) will modify the input presentation latency of the next plug-ins in the mixer routing graph and will modify the output presentation latency of the previous plug-ins.

![Tech_doc_31](../../../../resources/tech_doc_31.png)

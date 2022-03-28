>/ [VST Home](/Index.md) / [Technical Documentation](/pages/Technical+Documentation/Index.md)
>
># [3.0.0] Silence flags

**On this page:**

[[_TOC_]]

**Related pages**

- [How to use the silence flags](/pages/Tutorials/How+to+use+the+silence+flags.md)

---

## Introduction

Managing large plug-in sets and multiple virtual instruments on typical studio computer systems can often be difficult because of CPU performance limits. **VST 3** helps to improve overall performance by applying processing to plug-ins only when audio signals are present on their respective inputs. Instead of always processing input signals, **VST 3** plug-ins can apply their processing economically and only when it is needed.

The feature is supported by the [IAudioProcessor](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html) interface of the plug-in.

The silence flags is part of the [AudioBusBuffers](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1AudioBusBuffers.html) ([silenceFlags](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1AudioBusBuffers.html#a2c73b926e22ddb05193b6edd16a008f8)) passed from the host to the plug-in and back to the host in the process call:

- MyPluginProcessor::process (ProcessData& data)
- for the inputs: check this flag: **data.inputs[0]silenceFlags**
- for the outputs: set this when the plug-in generates or notsilence: **data.outputs[0].silenceFlags**

The silence flags are a bitmask where each bit corresponds to one channel of a bus (for example L and R for stereo bus).

```admonish info
The host has the responsibility to clear the input buffers (set to zero) when it enables the silence flags (the output silence flags will be set by the host to no silence (=0)), on the other side the plug-in, if it produces silence output, has the responsibility to clear (set to zero) its output buffers and to correctly set the output silence flags.
```

Check tutorial about [How to use the silence flags](/pages/Tutorials/How+to+use+the+silence+flags.md).
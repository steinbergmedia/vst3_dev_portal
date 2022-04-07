>/ [VST Home](../../../index.md) / [Technical Documentation](../../Index.md)
>
># [3.6.8] Request Bus Activation

**On this page:**

[[_TOC_]]

**Related pages:**
- [(3.0.0) Multiple Dynamic I/O Support](../3.0.0/Multiple+Dynamic+IO.md)

---

## Introduction

Extended host callback interface for an edit controller: [Vst::IComponentHandlerBusActivation](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandlerBusActivation.html)

- [host imp]
- [extends [IComponentHandler](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html)]
- [released: 3.6.8]
- [optional]

Allows the plug-in to request the host to activate or deactivate a specific bus. If the host accepts this request, it will call later on [IComponent::activateBus](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponent.html#a3ab7d06aaefe03da1fcd1819f1261050). This is particularly useful for instruments with more than 1 outputs, where the user could request from the plug-in UI a given output bus activation.

See also [IComponentHandler](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html)

## Example

``` c++
// somewhere in your code when you need to inform the host to enable a specific Bus.
FUnknownPtr<IComponentHandlerBusActivation> busActivation (componentHandler);
if (busActivation)
{
    // here we want to activate our audio input Side-chain (the 2cd input bus: index 1)
    busActivation->requestBusActivation (kAudio, kInput, 1, true);
}
```

>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># \[3.8.1\] Transport Control

**On this page:**

[[_TOC_]]

**Related pages:**

- [Example plug-in: Transport Control](../../../What+is+the+VST+3+SDK/Plug-in+Examples.md#transport-control)

---

## Introduction

This interface [Vst:: ITransportControl](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1ITransportControl.html) allows a plug-in to request transport-related actions from the host.

Typical use cases include:
- Jumping (locating) to a position
- Starting or stopping playback or recording
- Adjusting loop/cycle regions
- Enabling or disabling cycle playback

All calls must be made from the **UI thread**. Hosts may accept or deny requests depending on their internal policies or the
current editing mode (e.g., offline rendering, write-protected state, etc.).

- \[host imp\]
- [extends [Vst:: IComponentHandler](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html)]
- \[released: 3.8.1\]
- \[optional\]

## Example

**In mycontroller.cpp**

``` c++
bool mycontroller::startPlayback ()
{
    // the hostContext was given in the function  ComponentBase::initialize (FUnknown* context)
    if (!hostContext)
        return false;

    Vst::ITransportControl* transportControl = nullptr;
    hostContext->queryInterface (Vst::ITransportControl::iid, (void**)&transportControl);

	if (transportControl && transportControl->isActionSupported (Vst::ITransportControl::PlaybackStart) == kResultTrue)
	{
        transportControl->requestAction (Vst::ITransportControl::PlaybackStart);
        return true;
    }
    return false;
}
```
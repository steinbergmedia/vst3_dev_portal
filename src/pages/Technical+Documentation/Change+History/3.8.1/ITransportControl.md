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

- \[host imp\]
- [extends [Vst:: IComponentHandler](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html)]
- \[released: 3.8.1\]
- \[optional\]

Typical use cases include:
- Jumping (locating) to a position
- Starting or stopping playback or recording
- Adjusting loop/cycle regions
- Enabling or disabling cycle playback

All calls must be made from the **UI thread**. Hosts may accept or deny requests depending on their internal policies or the current editing mode (e.g., offline rendering, write-protected state, etc.).

| Enumerator | Description |
| :- | :- |
| Locate | Locate transport to a new position. Requires a valid `TransportPosition`. |
| PlaybackStart | Start playback at the current position. |
| PlaybackStop | Stop playback and keep the current position. |
| LocateAndPlaybackStart | Locate to the specified position and start playback (position required). |
| PlaybackStopAndLocate | Stop playback and locate to the specified position (position required). |
| RecordOnPlaybackStart | Start recording and playback at the current position. |
| LocateAndRecordOnPlaybackStart | Locate to the specified position and start recording and playback (position required). |
| RecordOff | Stop recording and continue playback. |
| RecordOffPlaybackStop | Stop recording and playback and keep the current position. |
| RecordOffPlaybackStopAndLocate | Stop recording and playback, then locate to the specified position (position required). |
| SetCycleStart | Sets the first sample included in the cycle region (position required). |
| SetCycleEnd | Sets the sample position immediately after the end of the cycle region (exclusive end position, position required). The cycle length in samples is `end - start`. For example, `SetCycleStart(100)` and `SetCycleEnd(200)` define a cycle of 100 samples. Sample positions included in the cycle are `{100 ... 199}`, while sample position `200` is outside the cycle. |
| CycleOn | Enable looping/cycle mode. |
| CycleOff | Disable looping/cycle mode. |

## Example

**In mycontroller.cpp**

``` c++
bool mycontroller::startPlayback ()
{
    // the hostContext was given in the function ComponentBase::initialize (FUnknown* context)
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
>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># [3.6.12] Legacy MIDI CC Out Event

**On this page:**

[[_TOC_]]

---

## Introduction

Legacy MIDI CC Out event specific data: [midiCCOut](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1Event.html#a3f45fbed968cf574aa1f9b859f0a0972)

Used in Event (union)

- [released: 3.6.12]

This kind of event is reserved for generating MIDI CC as output event for kEvent Bus during the process call.

## Example

**In myprocessor.cpp**

``` c++
#include "public.sdk/source/vst/vsteventshelper.h"
 
//-----------------------------------------------------------------------------
tresult PLUGIN_API MyProcessor::process (ProcessData& data)
{
    int16 channel = 10;
    float value = 0.4f;
    //...
    Event evtMIDICC;
    Helpers::initLegacyMIDICCOutEvent (evtMIDICC, kCtrlModWheel, channel, value);
    data.outputEvents->addEvent (evtMIDICC);
    //...
}
```

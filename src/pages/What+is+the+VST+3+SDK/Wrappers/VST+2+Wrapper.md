>/ ... / [AAX, AUv3, AU and VST 2 Wrappers](Index.md)
>
># VST 3 - VST 2.x Wrapper

**On this page:**

[[_TOC_]]

---

Helper Class wrapping a **VST 3** plug-in to a **VST 2.4** plug-in

## Introduction

The **VST 3 SDK** comes with a helper class which wraps one **VST 3** audio processor and edit controller to a **VST 2.x** plug-in.

## How does it work?

You just need to add public.sdk/source/vst/vst2wrapper/vst2wrapper.sdk.cpp to your project and add the following code somewhere in your sources:

``` c++
//-----------------------------------------------------------------
#include "public.sdk/source/vst/vst2wrapper/vst2wrapper.h"

//-----------------------------------------------------------------
::AudioEffect* createEffectInstance (audioMasterCallback audioMaster)
{
    return Steinberg::Vst::Vst2Wrapper::create (GetPluginFactory(), kAudioProcessorCID, kVst2UniqueID, audioMaster);
}
```

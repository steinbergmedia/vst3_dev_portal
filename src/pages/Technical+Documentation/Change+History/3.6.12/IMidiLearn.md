>/ [VST Home](../../../index.md) / [Technical Documentation](../../Index.md)
>
># [3.6.12] MIDI Learn

**On this page:**

[[_TOC_]]

**Related pages:**

- [(3.0.1) Parameter MIDI Mapping](../../Change+History/3.0.1/IMidiMapping.md)

---

## Introduction

MIDI Learn Interface: [Vst::IMidiLearn](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IMidiLearn.html)

- [plug imp]
- [extends [IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html)]
- [released: 3.6.12]
- [optional]

If this interface is implemented by the edit controller, the host will call this method whenever there is live MIDI-CC input for the plug-in.This way, the plug-in can change its MIDI-CC parameter mapping and inform the host via the [IComponentHandler::restartComponent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html#a1f283573728cf0807224c5ebdf3ec3a6) with the [kMidiCCAssignmentChanged](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/namespaceSteinberg_1_1Vst.html#a17867782006f9fdb2b72c16b0420bed5ae2e3ed4527f88e577a2aeb595bd853fd) flag. Use this if you want to implement custom MIDI-Learn functionality in your plug-in.

## Example

**In mycontroller.h**

```
//------------------------------------------------------------------------
// here an example of how a VST 3 Plug-in could support this IMidiLearn interface.
// we need to define somewhere the iids:
  
//in MyController class declaration
class MyController : public Vst::EditController, public Vst::IMidiLearn
{
    // ...
    //--- IMidiLearn ---------------------------------
    tresult PLUGIN_API onLiveMIDIControllerInput (int32 busIndex, int16 channel,
                                                  CtrlNumber midiCC) SMTG_OVERRIDE;
    // ...
  
    OBJ_METHODS (MyController, Vst::EditController)
    DEFINE_INTERFACES
        // ...
        DEF_INTERFACE (Vst::IMidiLearn)
    END_DEFINE_INTERFACES (Vst::EditController)
    //...
}
```

**In mycontroller.cpp**

```
#include "pluginterfaces/vst/ivstmidilearn.h
 
namespace Steinberg {
    namespace Vst {
        DEF_CLASS_IID (IMidiLearn)
    }
}
  
//------------------------------------------------------------------------
tresult PLUGIN_API MyController::onLiveMIDIControllerInput (int32 busIndex, int16 channel, CtrlNumber midiCC)
{
    // if we are not in doMIDILearn (triggered by a UI button for example) or wrong channel then return
    if (!doMIDILearn || busIndex != 0 || channel != 0 || midiLearnParamID == InvalidParamID)
        return kResultFalse;
 
    // adapt our internal MIDICC -> parameterID mapping
    midiCCMapping[midiCC] = midiLearnParamID;
 
    // new mapping then inform the host that our MIDI assignment has changed
    if (auto componentHandler = getComponentHandler ())
    {
        componentHandler->restartComponent (kMidiCCAssignmentChanged);
    }
    return kResultTrue;
}
```
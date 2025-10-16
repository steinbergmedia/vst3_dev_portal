>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># \[3.8.0\] MIDI Learn 2 (MIDI 2.0 support)

**On this page:**

[[_TOC_]]

**Related pages:**

- [\[3.0.1\] Parameter MIDI Mapping (MIDI 1.0 support)](../../Change+History/3.0.1/IMidiMapping.md)
- [\[3.6.12\] MIDI Learn (MIDI 1.0 support)](../../Change+History/3.6.12/IMidiLearn.md)
- [\[3.8.0\] Parameter MIDI Mapping 2 (MIDI 2.0 support)](../../Change+History/3.8.0/IMidiMapping2.md)

---

## Introduction

MIDI Learn Interface: [Vst:: IMidiLearn2](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IMidiLearn2.html).

- \[plug imp\]
- [extends [Vst:: IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html)]
- \[released: 3.8.0\]
- \[optional\]
- \[replaces Vst::IMidiLearn\]

If this interface is implemented by the edit controller, the host will call this method whenever there is live MIDI-CC input for the plug-in. This way, the plug-in can change its MIDI-CC parameter mapping and notify the host using the [Vst:: IComponentHandler::restartComponent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html#a1f283573728cf0807224c5ebdf3ec3a6) with the [kMidiCCAssignmentChanged](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/namespaceSteinberg_1_1Vst.html#a17867782006f9fdb2b72c16b0420bed5ae2e3ed4527f88e577a2aeb595bd853fd) flag.

Use this if you want to implement custom MIDI-Learn functionality in your plug-in.

## Example

**In mycontroller.h**

``` c++
//------------------------------------------------------------------------
// here an example of how a VST 3 plug-in could support this IMidiLearn2 interface.
// we need to define somewhere the iids:
  
//in MyController class declaration
class MyController : public Vst::EditController, public Vst::IMidiLearn2
{
    // ...
    //--- IMidiLearn2 ---------------------------------
    tresult PLUGIN_API onLiveMidi2ControllerInput (BusIndex index, MidiChannel channel,
                                                   Midi2Controller midiCC) SMTG_OVERRIDE;
    
	tresult PLUGIN_API onLiveMidi1ControllerInput (BusIndex index, MidiChannel channel,
	                                               CtrlNumber midiCC) SMTG_OVERRIDE;
    // ...
  
    OBJ_METHODS (MyController, Vst::EditController)
    DEFINE_INTERFACES
        // ...
        DEF_INTERFACE (Vst::IMidiLearn2)
    END_DEFINE_INTERFACES (Vst::EditController)
    //...
}
```

**In mycontroller.cpp**

``` c++
#include "pluginterfaces/vst/ivstmidimapping2.h
 
namespace Steinberg {
    namespace Vst {
        DEF_CLASS_IID (IMidiLearn2)
    }
}
  
//------------------------------------------------------------------------
tresult PLUGIN_API  MyController::onLiveMidi2ControllerInput (BusIndex index, MidiChannel channel, Midi2Controller midiCC)
{
    // if we are not in doMIDILearn (triggered by a UI button for example) or wrong channel then return
    if (!doMIDILearn || index != 0 || channel != 0 || midiLearnParamID == InvalidParamID)
        return kResultFalse;
 
    auto currentMapping = midiCCMapping.find ({CCType::CC, midiCC});
    if (currentMapping == midiCCMapping.end () || currentMapping->second != midiLearnParamID)
    {
        removeCurrentMidiLearnParamAssignment ();
        midiCCMapping[{CCType::CC, midiCC}] = midiLearnParamID;
        
        if (auto _componentHandler = getComponentHandler ())
            _componentHandler->restartComponent (kMidiCCAssignmentChanged);
    }
    return kResultTrue;
}

//------------------------------------------------------------------------
tresult PLUGIN_API  MyController::onLiveMidi1ControllerInput (BusIndex index, MidiChannel channel, CtrlNumber midiCC)
{
    // if we are not in doMIDILearn (triggered by a UI button for example) or wrong channel then return
    if (!doMIDILearn || index != 0 || channel != 0 || midiLearnParamID == InvalidParamID)
        return kResultFalse;
 
    CCKey key { midiCC.registered ? CCType::RPN : CCType::NRPN, (midiCC.bank << 7) | midiCC.index };
    auto currentMapping = midiCCMapping.find (key);
    if (currentMapping == midiCCMapping.end () || currentMapping->second != midiLearnParamID)
    {
        removeCurrentMidiLearnParamAssignment ();
        midiCCMapping[key] = midiLearnParamID;

        if (auto _componentHandler = getComponentHandler ())
            _componentHandler->restartComponent (kMidiCCAssignmentChanged);
    }
    return kResultTrue;
}

```

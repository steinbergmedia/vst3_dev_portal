>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># \[3.8.0\] Parameter MIDI Mapping 2 (MIDI 2.0 support)

**On this page:**

[[_TOC_]]

**Related pages**

- [About MIDI in VST 3](../../About+MIDI/Index.md)
- [\[3.8.0\] MIDI Learn 2 (MIDI 2.0 support)](../../Change+History/3.8.0/IMidiLearn2.md)
- [\[3.0.1\] Parameter MIDI Mapping (MIDI 1.0 support)](../../Change+History/3.0.1/IMidiMapping.md)

---

## Introduction

How the mapping works between **MIDI CC**s and **parameters**.

**MIDI** Mapping Interface: [Vst:: IMidiMapping2](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IMidiMapping2.html)

- \[plug imp\]
- [extends [Vst:: IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html)]
- \[released: 3.8.0\]
- \[optional\]
- \[replaces Vst::IMidiMapping\]

**MIDI 2.0** and **MIDI 1.0** controllers are not transmitted directly to a **VST** component. **MIDI** as hardware protocol has restrictions that can be avoided in software. Controller data in particular come along with unclear and often ignored semantics. On top of this, they can interfere with regular parameter automation and the host is unaware of what happens in the plug-in when passing **MIDI** controllers directly.

So any functionality that is to be controlled by **MIDI** controllers must be exported as regular parameter. The host will transform incoming **MIDI** controller data using this interface and transmit them as regular parameter change. This allows the host to automate them in the same way as other parameters. *CtrlNumber* can be a typical **MIDI** controller value extended to some others values like pitchbend or aftertouch (see [ControllerNumbers](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/namespaceSteinberg_1_1Vst.html#a70ee68a13248febed5047cfa0fddf4e6)). If the mapping has changed, the plug-in must call [Vst:: IComponentHandler::restartComponent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html#a1f283573728cf0807224c5ebdf3ec3a6) ([kMidiCCAssignmentChanged](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/namespaceSteinberg_1_1Vst.html#a17867782006f9fdb2b72c16b0420bed5ae2e3ed4527f88e577a2aeb595bd853fd)) to inform the host about this change.

## Example

**In myeditcontroller.h**

``` c++
//--------------------------------------
class MyEditController: public EditControllerEx1, public IMidiMapping, public IMidiMapping2
{
    //...
    //--- IMidiMapping -------------------------------
	tresult PLUGIN_API getMidiControllerAssignment (int32 busIndex, int16 channel,
	                                                CtrlNumber midiControllerNumber,
	                                                ParamID& id /*out*/) SMTG_OVERRIDE;
    //--- IMidiMapping2 ------------------------------
    uint32 PLUGIN_API getNumMidi2ControllerAssignments (BusDirections direction) SMTG_OVERRIDE;
    tresult PLUGIN_API getMidi2ControllerAssignments (
        BusDirections direction, const Midi2ControllerParamIDAssignmentList& list) SMTG_OVERRIDE;
    uint32 PLUGIN_API getNumMidi1ControllerAssignments (BusDirections direction) SMTG_OVERRIDE;
    tresult PLUGIN_API getMidi1ControllerAssignments (
        BusDirections direction, const Midi1ControllerParamIDAssignmentList& list) SMTG_OVERRIDE;

    //---Interface---------
    OBJ_METHODS (MyEditController, EditControllerEx1)
    DEFINE_INTERFACES
        DEF_INTERFACE (IMidiMapping)
        DEF_INTERFACE (IMidiMapping2)
    END_DEFINE_INTERFACES (MyEditController)
    REFCOUNT_METHODS (MyEditController)

    Midi1ControllerParamIDAssignmentList mMidi1List;
    Midi2ControllerParamIDAssignmentList mMidi2List;
};
```

**In myeditcontroller.cpp**

``` c++
//--------------------------------------
tresult PLUGIN_API MyEditController::getMidiControllerAssignment (int32 busIndex, int16 midiChannel, CtrlNumber midiControllerNumber, ParamID& tag)
{
    // for my first Event bus and for MIDI channel 0 and for MIDI CC Volume only
    if (busIndex == 0 && midiChannel == 0 && midiControllerNumber == kCtrlVolume)
    {
        tag = kGainId;
        return kResultTrue;
    }
    return kResultFalse;
}

//-----------------------------------------------------------------------------
// New API IMidiMapping2
//-----------------------------------------------------------------------------
uint32 PLUGIN_API MyEditController::getNumMidi2ControllerAssignments (BusDirections direction)
{
    if (direction == kInput)
    	return 1;
    return 0;
}

//-----------------------------------------------------------------------------
tresult PLUGIN_API MyEditController::getMidi2ControllerAssignments (
    BusDirections direction, const Midi2ControllerParamIDAssignmentList& list)
{
    if (direction == kInput)
    {
    	list = mMidi2List;
        return kResultTrue;
    }
    return kResultFalse;
}

//-----------------------------------------------------------------------------
uint32 PLUGIN_API MyEditController::getNumMidi1ControllerAssignments (BusDirections direction)
{
    if (direction == kInput)
    	return 1;
    return 0;
}

//-----------------------------------------------------------------------------
tresult PLUGIN_API MyEditController::getMidi1ControllerAssignments (
    BusDirections direction, const Midi1ControllerParamIDAssignmentList& list)
{
    if (direction == kInput)
    {
    	list = mMidi1List;
        return kResultTrue;
    }
    return kResultFalse;
}

```

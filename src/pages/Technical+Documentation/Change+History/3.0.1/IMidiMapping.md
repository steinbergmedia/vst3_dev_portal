>/ [VST Home](../../../Index.md) / [Technical Documentation](../../Index.md)
>
># [3.0.1] Parameter MIDI Mapping

**On this page:**

[[_TOC_]]

**Related pages**

- [About MIDI in VST 3](../../About+MIDI/Index.md)
- [[3.6.12] MIDI Learn](../../Change+History/3.6.12/IMidiLearn.md)

---

## Introduction

How the mapping works between **MIDI CC**s and **parameters**.

**MIDI** Mapping Interface: [Vst::IMidiMapping](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IMidiMapping.html)

- [plug imp]
- [extends [IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html)]
- [released: 3.0.1]
- [optional]

**MIDI** controllers are not transmitted directly to a **VST** component. **MIDI** as hardware protocol has restrictions that can be avoided in software. Controller data in particular come along with unclear and often ignored semantics. On top of this, they can interfere with regular parameter automation and the host is unaware of what happens in the plug-in when passing **MIDI** controllers directly.

So any functionality that is to be controlled by **MIDI** controllers must be exported as regular parameter. The host will transform incoming **MIDI** controller data using this interface and transmit them as regular parameter change. This allows the host to automate them in the same way as other parameters. *CtrlNumber* can be a typical **MIDI** controller value extended to some others values like pitchbend or aftertouch (see [ControllerNumbers](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/namespaceSteinberg_1_1Vst.html#a70ee68a13248febed5047cfa0fddf4e6)). If the mapping has changed, the plug-in must call [IComponentHandler::restartComponent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html#a1f283573728cf0807224c5ebdf3ec3a6) ([kMidiCCAssignmentChanged](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/namespaceSteinberg_1_1Vst.html#a17867782006f9fdb2b72c16b0420bed5ae2e3ed4527f88e577a2aeb595bd853fd)) to inform the host about this change.

## Example

**In myeditcontroller.h**

```
//--------------------------------------
class MyEditController: public EditControllerEx1, public IMidiMapping
{
    //...
    //---IMidiMapping---------------------------
    tresult PLUGIN_API getMidiControllerAssignment (int32 busIndex, int16 channel, CtrlNumber midiControllerNumber, ParamID& id) SMTG_OVERRIDE;
    //---Interface---------
    OBJ_METHODS (MyEditController, EditControllerEx1)
    DEFINE_INTERFACES
        DEF_INTERFACE (IMidiMapping)
    END_DEFINE_INTERFACES (MyEditController)
    REFCOUNT_METHODS (MyEditController)
};
```

**In myeditcontroller.cpp**

```
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
```
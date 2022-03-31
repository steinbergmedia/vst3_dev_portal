>/ [VST Home](../../../index.md) / [Technical Documentation](../../Index.md)
>
># [3.6.11] NoteExpression Physical UI Mapping

**On this page:**

[[_TOC_]]

**Related pages:**

- [[3.5.0] Note Expression](../../Change+History/3.5.0/INoteExpressionController.md)

---

# Introduction
Extended plug-in interface [IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html) for note expression event support: [Vst::INoteExpressionPhysicalUIMapping](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1INoteExpressionPhysicalUIMapping.html)

- [plug imp]
- [extends [IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html)]
- [released: 3.6.11]
- [optional]

With this plug-in interface, the host can retrieve the preferred physical mapping associated to note expression supported by the plug-in.When the mapping changes (for example, when switching presets) the plug-in needs to inform the host about it via [IComponentHandler::restartComponent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html#a1f283573728cf0807224c5ebdf3ec3a6) ([kNoteExpressionChanged](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/namespaceSteinberg_1_1Vst.html#a17867782006f9fdb2b72c16b0420bed5aa11fe6e24349c6d2f7e0035dbc01c10b)).

## Example

**In mycontroller.h**

```
//------------------------------------------------------------------------
// here an example of how a VST 3 Plug-in could support this INoteExpressionPhysicalUIMapping interface.
// we need to define somewhere the iids:
  
//in MyController class declaration
class MyController : public Vst::EditController, public Vst::INoteExpressionPhysicalUIMapping
{
    // ...
    //--- INoteExpressionPhysicalUIMapping ---------------------------------
    tresult PLUGIN_API getPhysicalUIMapping (int32 busIndex, int16 channel, PhysicalUIMapList& list) SMTG_OVERRIDE;
    // ...
  
    OBJ_METHODS (MyController, Vst::EditController)
    DEFINE_INTERFACES
        // ...
        DEF_INTERFACE (Vst::INoteExpressionPhysicalUIMapping)
    END_DEFINE_INTERFACES (Vst::EditController)
    //...
}
```

**In mycontroller.cpp**

```
#include "pluginterfaces/vst/ivstnoteexpression.h"
 
namespace Steinberg {
    namespace Vst {
        DEF_CLASS_IID (INoteExpressionPhysicalUIMapping)
    }
}
  
//------------------------------------------------------------------------
tresult PLUGIN_API MyController::getPhysicalUIMapping (int32 busIndex, int16 channel, PhysicalUIMapList& list)
{
    if (busIndex == 0 && channel == 0)
    {
        for (uint32 i = 0; i < list.count; ++i)
        {
            NoteExpressionTypeID type = kInvalidTypeID;
            if (kPUIXMovement == list.map[i].physicalUITypeID)
                list.map[i].noteExpressionTypeID = kCustomStart + 1;
            else if (kPUIYMovement == list.map[i].physicalUITypeID)
                list.map[i].noteExpressionTypeID = kCustomStart + 2;
        }
        return kResultTrue;
    }
    return kResultFalse;
}
```
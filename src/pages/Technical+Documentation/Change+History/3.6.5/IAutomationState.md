>/ [VST Home](/Index.md) / [Technical Documentation](/pages/Technical+Documentation/Index.md)
>
># [3.6.5] Automation State

**On this page:**

[[_TOC_]]

---

## Introduction

Extended plug-in interface [IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html): [Vst::IAutomationState](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAutomationState.html)

- [plug imp]
- [extends [IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html)]
- [released: 3.6.5]
- [optional]

Hosts can inform the plug-in about its current automation state (Read/Write/Nothing).

## Example

**in mycontroller.h**

```
//------------------------------------------------------------------------
class MyController: public EditControllerEx1, public IAutomationState
{
    //...
    //---IAutomationState---------------------------------
    tresult PLUGIN_API setAutomationState (int32 state) SMTG_OVERRIDE;
 
    //...
    DEFINE_INTERFACES
        //...
        DEF_INTERFACE (IAutomationState)
    END_DEFINE_INTERFACES (EditControllerEx1)
    //...
};
```

**In mycontroller.cpp**

```
//------------------------------------------------------------------------
tresult PLUGIN_API MyController::setAutomationState (int32 state)
{
    switch (state)
    {
        case kNoAutomation:
            break;
        case kReadState:
            break;
        case kWriteState:
            break;
        case kReadWriteState:
            break;
        default:
    }
    return kResultTrue;
}
```
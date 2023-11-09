>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># \[3.1.0\] KnobMode, Open Help & Open Aboutbox

**On this page:**

[[_TOC_]]

---

## Introduction

Edit controller component interface extension: [Vst::IEditController2](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController2.html).

- \[plug imp\]
- [extends [IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html)]
- \[released: 3.1.0\]
- \[optional\]

Extension to allow the host to inform the plug-in about the host knob mode ([setKnobMode](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController2.html#ad38ac70a9efcc0cfee8ac0cc2b80e648)), and to open the plug-in's about box ([openAboutBox](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController2.html#aa52846d39014c3ca95224fa98930e7a8)) or help documentation ([openHelp](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController2.html#a749ceb08d2f33b5b12cdc59172d8a7c3)).

## Example

**In mycontroller.h**

``` c++
class MyEditController : public ComponentBase, public IEditController, public IEditController2
{
public:
 
    //...
    //---from IEditController2-------
    tresult PLUGIN_API setKnobMode (KnobMode mode) SMTG_OVERRIDE { hostKnobMode = mode; return kResultTrue; }
    tresult PLUGIN_API openHelp (TBool /*onlyCheck*/) SMTG_OVERRIDE;
    tresult PLUGIN_API openAboutBox (TBool /*onlyCheck*/) SMTG_OVERRIDE {return kResultFalse;}
    //...
 
    DEFINE_INTERFACES
        DEF_INTERFACE (IEditController)
        DEF_INTERFACE (IEditController2)
    END_DEFINE_INTERFACES (ComponentBase)
};
```

**In mycontroller.cpp**

``` c++
tresult PLUGIN_API MyEditController::openHelp (TBool onlyCheck)
{
    if (onlyCheck)
    {
        // the host just wants to know if i have a help documentation
        return kResultTrue;
    }
    // here i can open my documentation
    // could in my UI documentation or external pdf file
 
    return kResultTrue;
}
```

See also [IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html), [EditController](https://steinbergmedia.github.io/vst3_doc/vstsdk/classSteinberg_1_1Vst_1_1EditController.html).

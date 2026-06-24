>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># \[3.7.0\] Parameter Function Name

**On this page:**

[[_TOC_]]

---

## Introduction

Edit controller component interface extension: [Vst:: IParameterFunctionName](https://steinbergmedia.github.io/vst3_doc/vstinterfaces//classSteinberg_1_1Vst_1_1IParameterFunctionName.html).

- \[plug imp\]
- [extends [Vst:: IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html)]
- \[released: 3.7.0\]
- \[optional\]

This interface allows the host to get a parameter associated to a specific meaning (a functionName) for a given unit. The host can use this information, for example, for drawing a Gain Reduction meter in its own UI. In order to get the plain value of this parameter, the host should use the [Vst:: IEditController::normalizedParamToPlain](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html#a849747dc98909312b4cdbdeea82dbae0). The host can automatically map parameters to dedicated UI controls, such as the wet-dry mix knob or the Randomize button.
If a parameter provided by this interface is marked with the kReadOnly flag, the host should ignore this parameter.

## Current defined function names

| Type | Name | Comment |
|---|---|---|
| Gain Reduction | kCompGainReduction | |
|                | kCompGainReductionMax| |
|                | kCompGainReductionPeakHold| |
|                | kCompResetGainReductionMax| |
| Randomize      | kRandomize |  Assigns randomized values across the full parameter range.|
|                | kRandomizeAroundCurrent | Assigns randomized values around the current parameter values (e.g. ±5% of the current value).
| Panner         | kPanPosCenterX | Gravity point X-axis \[0, 1\]=>\[L-R\] (for stereo: middle between left and right).|
|                | kPanPosCenterY | Gravity point Y-axis \[0, 1\]=>\[Front-Rear\].|
|                | kPanPosCenterZ | Gravity point Z-axis \[0, 1\]=>\[Bottom-Top\].|
| Other          | kLowLatencyMode| Useful for live situation where low latency is required: 0 means LowLatency disable,  1 means LowLatency enable|
|                | kDryWetMix     | Allowing to mix the original (Dry) Signal with the processed one (Wet): 0.0 means Dry Signal only, 0.5 means 50% Dry Signal + 50% Wet Signal, 1.0 means Wet Signal only |

## Example

**In mycontroller.h**

``` c++
//------------------------------------------------------------------------
// here an example of how a VST 3 plug-in could support this IParameterFunctionName interface.
// we need to define somewhere the iids:
  
//in MyController class declaration
class MyController : public Vst::EditController, public Vst::IParameterFunctionName
{
    // ...
    tresult PLUGIN_API getParameterIDFromFunctionName (UnitID unitID, FIDString functionName,
                                                    Vst::ParamID& paramID) override;
    // ...
  
    OBJ_METHODS (MyController, Vst::EditController)
    DEFINE_INTERFACES
        // ...
        DEF_INTERFACE (Vst::IParameterFunctionName)
    END_DEFINE_INTERFACES (Vst::EditController)
    //...
}
```

**In mycontroller.cpp**

``` c++
#include "pluginterfaces/vst/ivstparameterfunctionname.h"
 
namespace Steinberg {
    namespace Vst {
        DEF_CLASS_IID (IParameterFunctionName)
    }
}
  
//------------------------------------------------------------------------
tresult PLUGIN_API MyController::getParameterIDFromFunctionName (UnitID unitID, FIDString functionName,
                                                                 Vst::ParamID& paramID)
{
    using namespace Vst;
  
    paramID = kNoParamId;
  
    if (unitID == kRootUnitId && FIDStringsEqual (functionName, kCompGainReduction))
        paramID = kMyGainReductionId;
  
    return (paramID != kNoParamId) ? kResultOk : kResultFalse;
}
```

**Example of host implementation**

``` c++
if (auto functionName = Steinberg::U::cast<Vst::IParameterFunctionName> (mEditController->getIEditController ())
{
    Vst::ParamID paramID;
    if (functionName->getParameterIDFromFunctionName (Vst::FunctionNameType::kCompGainReduction, paramID) == kResultTrue)
    {
        // paramID could be cached for performance issue
        Vst::ParamValue norm = mEditController->getIEditController ()->getParamNormalized (paramID);
        Vst::ParamValue plain = mEditController->getIEditController ()->normalizedParamToPlain (paramID, norm);
        // plain is something like -6 (-6dB)
    }
}
```

>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># \[3.8.1\] NoteOn Orchestral Articulation Info

**On this page:**

[[_TOC_]]

**Related pages:**

- [\[3.5.0\] Note Expression](../3.5.0/INoteExpressionController.md)
- [About MIDI in VST 3](../../About+MIDI/Index.md)
- [\[midi.org\] Orchestral Articulation Profile Introduction](https://midi.org/wp-content/uploads/2024/03/Orchestral-APE-Profile-Intro-Final.pdf)
- [\[midi.org\] new profile specifications adopted](https://midi.org/6-new-profile-specifications-adopted)
- [\[AMEI\] M2-123-UM Document](https://amei-music.github.io/midi2.0-docs/amei-pdf/M2-123-UM_v1-0_Note-On_Orchestral_Articulation_Profile.pdf)

---

## Introduction

Edit controller component interface extension: [Vst:: NoteOnOrchestralArticulation:: IInfo](https://steinbergmedia.github.io/vst3_doc/vstinterfaces//classSteinberg_1_1Vst_1_1IInfo.html).

- \[plug imp\]
- [extends [Vst:: IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html)]
- \[released: 3.8.1\]
- \[optional\]

This interface allows the host to retrieve the number of variations supported by the plug-in for Note On Orchestral Articulations (called from the UI thread). The variation indices for subclasses follow the subclass index definitions specified by the MIDI-CI Profile for Note On Selection of Orchestral Articulation ([M2-123-UM](https://amei-music.github.io/midi2.0-docs/amei-pdf/M2-123-UM_v1-0_Note-On_Orchestral_Articulation_Profile.pdf)).

## Example

**In mycontroller.h**

``` c++

//------------------------------------------------------------------------
// here an example of how a VST 3 plug-in could support this IParameterFunctionName interface.
// we need to define somewhere the iids (in mycontroller.cpp):

#include "pluginterfaces/vst/ivstnoteonorchestralarticulationinfo.h"

//in MyController class declaration
class MyController : public Vst::EditController, public Vst::NoteOnOrchestralArticulation::IInfo
{
    // ...
    tresult PLUGIN_API getVariationsInfo (Vst::NoteOnOrchestralArticulation::ClassificationVariations& info /*out*/) override;
    // ...
  
    OBJ_METHODS (MyController, Vst::EditController)
    DEFINE_INTERFACES
        // ...
        DEF_INTERFACE (Vst::NoteOnOrchestralArticulation::IInfo)
    END_DEFINE_INTERFACES (Vst::EditController)
    //...
}
```

**In mycontroller.cpp**

``` c++ 
namespace Steinberg {
    namespace Vst {
        DEF_CLASS_IID (NoteOnOrchestralArticulation::IInfo)
    }
}
  
//------------------------------------------------------------------------
tresult PLUGIN_API MyController::getVariationsInfo  (Vst::NoteOnOrchestralArticulation::ClassificationVariations& info) 
{
    using namespace Vst;

    // subclass: Normal Sustains & Strikes (Part 1) (index 0)
    info.classification[kCoreSoundSustainAndStrikes].variation[0] = 2;

    // subclass: Legato and Legato Slurred (index 2)
    info.classification[kCoreSoundSustainAndStrikes].variation[2] = 3;

    // subclass: Pizzicato (index 10 (0xA))
    info.classification[kStaccatosAndShorts].variation[10] = 3;
}
```

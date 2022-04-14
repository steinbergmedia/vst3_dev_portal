>/ [VST Home](../) / [Frequently Asked Questions](Index.md)
>
># Compatibility with VST 2.x or VST 1

[[_TOC_]]

---

## Q: How can I update my VST 2 version of my plug-in to a VST 3 version and be sure that Cubase will load it instead of my old one?

You have to provide a special UID for your [kVstAudioEffectClass](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/ivstaudioprocessor_8h.html#ae55c95a44e931e1cd78998c94bc65ee1) and [kVstComponentControllerClass](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/ivsteditcontroller_8h.html#a49d6f6f53c7630ea334474e9998c0a99) components, based on its **VST 2** UniqueID (4 characters) and its plug-in name like this:

``` c++
static void convertVST2UID_To_FUID (FUID& newOne, int32 myVST2UID_4Chars, const char* pluginName, bool forControllerUID = false)
{
    char uidString[33];
 
    int32 vstfxid;
    if (forControllerUID)
        vstfxid = (('V' << 16) | ('S' << 8) | 'E');
    else
        vstfxid = (('V' << 16) | ('S' << 8) | 'T');
 
    char vstfxidStr[7] = {0};
    sprintf (vstfxidStr, "%06X", vstfxid);
 
    char uidStr[9] = {0};
    sprintf (uidStr, "%08X", myVST2UID_4Chars);
 
    strcpy (uidString, vstfxidStr);
    strcat (uidString, uidStr);
 
    char nameidStr[3] = {0};
    size_t len = strlen (pluginName);
 
    // !!!the pluginName has to be lower case!!!!
    for (uint16 i = 0; i <= 8; i++)
    {
        uint8 c = i < len ? pluginName[i] : 0;
        sprintf (nameidStr, "%02X", c);
        strcat (uidString, nameidStr);
    }
    newOne.fromString (uidString);
}
```

Note that if you are developing a new plug-in and if you are using the **VST 2** wrapper included in the SDK you do not need to use convertVST2UID_To_FUID, a **VST 2** specific vendor call allows the host ([Steinberg](https://www.steinberg.net/) hosts since **Cubase** 4.0) to get from a **VST 2** version a **VST 3** UID.

``` c++
// extracted code from vst2wrapper.cpp
//-----------------------------------------------------------------------------
VstIntPtr Vst2Wrapper::vendorSpecific (VstInt32 lArg, VstIntPtr lArg2, void* ptrArg, float floatArg)
{
    switch (lArg)
    {
        case 'stCA':
        case 'stCa':
            switch (lArg2)
            {
                case 'FUID':
                    if (ptrArg)
                    {
                        if (vst3EffectClassID.isValid ())
                        {
                            memcpy ((char*)ptrArg, vst3EffectClassID, 16);
                            return 1;
                        }
                    }
                break;
        // ....
```

## Q: How can I support projects which were saved with the VST 2 version of my plug-in?

The host will call [IComponent::setState()](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponent.html#a77ac39bcc5c4b15818b1a87de2573805) and [IEditController::setComponentState()](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html#a4c2e1cafd88143fda2767a9c7ba5d48f) with the complete FXB/FXP stream. You have to extract your old state from that, for this the SDK provides a helper function [VST3::tryVst2StateLoad](https://steinbergmedia.github.io/vst3_doc/vstsdk/namespaceVST3.html#aadc6b99109a9b056a0176f49f9220822).

Here the code to add in the **VST 3** version when a **VST 3 plug-in** replaces a **VST 2** plug-in in a Steinberg sequencer project:

``` c++
#include "public.sdk/source/vst/utility/vst2persistence.h"
 
//------------------------------------------------------------------------
tresult PLUGIN_API MyVST3Effect::setState (IBStream* state)
{
    if (auto vst2State = VST3::tryVst2StateLoad (*state))
    {
        if ((vst2State->programs.empty ()) ||
            (static_cast<int32_t> (vst2State->programs.size ()) <= vst2State->currentProgram))
            return kResultFalse;
 
        //....
    }
    return kResultFalse;
}
```

For complete example source code you could check the function:\
tresult *PLUGIN_API Processor::setState (IBStream* state)* in the file *public.sdk/samples/vst/mda-vst3/source/mdaBaseProcessor.cpp*

For Automation compatibility, you have to ensure that **VST 3** parameter IDs have the same value than the indexes of their associated parameters in **VST 2**. Only with this condition the host can play back the automation. The parameter value has the same meaning in **VST 2** and **VST 3**.

## Q: In VST 2 the editor was able to access the processing part, named effect, directly. How can I do this in VST 3?

You cannot and more importantly must not do this. The processing part and user interface part communicate via a messaging system.\
See [Q: How should I communicate between the 'Processing' and the 'User Interface'?](#q-how-should-i-communicate-between-the-processing-and-the-user-interface) for details.

## Q: Does VST 3 implement methods like beginEdit and endEdit known from VST 2?

Yes and it is essential to support this for automation. For details, please see [Parameters and Automation](../Technical+Documentation/Parameters+Automation/Index.md)

## Q: Does VST 3 include variable Input/Output processing like processVariableIo of VST 2?

Not in version 3.1.0, we plan something in this direction later. (Note: this variableIO processing was for example for time stretching plug-ins).

## Q: What is the equivalent to the VST 2 kPlugCategOfflineProcess?

VST 3 doesn't support offline processing like it did in VST 2 (this interface was exclusively used by **WaveLab**). But it is possible to use **VST 3 plug-ins** in an offline context (this means that the process function can be called faster than real time : for example, during an export or a batch processing). If the plug-in doesn't support faster than realtime, it should add [kOnlyRealTime](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/group__plugType.html#gae58eb0aafa16197f12c1a61428fd5584) to its category.

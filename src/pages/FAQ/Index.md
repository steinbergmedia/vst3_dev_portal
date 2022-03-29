>/ [VST Home](/Index.md)
>
># Frequently Asked Questions

Provides some answers to some common questions.Kindly note that we do not provide individual SDK support. If you have any questions the FAQ below cannot answer, please refer to the [VST 3 SDK Forum](s).

At the bottom of this page you will find the FAQ about [licensing issues](../).

[[_TOC_]]

---

## Communication

### Q: How should I communicate between the 'Processing' and the 'User Interface'?

With the term 'Processing' we mean the code implementing the [Steinberg::Vst::IAudioProcessor](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html) interface, and with 'User Interface' the editor component implementing the [Steinberg::Vst::IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html) interface.

If you need to communicate the changes of parameters to the user interface, such as metering changes and peaks, you need to define the parameter as an exported type. The parameter then is associated with an ID. In the process function you can inform the host of changes by using the [outputParameterChanges](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessData.html#af08c4f7dfd9e456cc98ba0eb325993ae) (from [ProcessData](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessData.html)). You add the parameter (ID) to a list that will be used by the host to send them back to the user interface at the correct time.

If you should need to exchange more data than just parameter changes, such as tempo, sample rate, FFT, Pitch Analysis, or any other data resulting from your processing, you can use the [IMessage](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IMessage.html) interface (see AGain example). However, you need to be careful and send the data from a 'timer' thread and not directly from the process function, for example, when sending from a 'process' call.

See [Communication between the components](../Technical+Documentation/API+Documentation/Index.md#communication-between-the-components) **<- changed Link**.

### Q: I want to implement an audio meter in my user interface. How do I do this?

See [Q: How should I communicate between the 'Processing' and the 'User Interface'?](#q-how-should-i-communicate-between-the-processing-and-the-user-interface)

### Q: How does the host send automation data to my VST 3 plug-in?

Automation data is sent to the audio processing method as part of the data passed as a parameter to the [IAudioProcessor::process](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html#a6b98eb31cf38ba96a28b303c13c64e13) (processData) method.

```
IAudioProcessor::process (processData)
{
    IParameterChanges* paramChanges = processData.inputParameterChanges;
    //...
}
```

Automation data is transmitted as a list of parameter changes. This list always contains enough information to transmit the original automation curve from the host in a sample accurate way. Check the [AGain](../What+is+the+VST+3+SDK/Plug-in+Examples.md#again) **<- changed Link** example to see how it can be implemented.

See also [Parameters and Automation](../Technical+Documentation/Parameters+Automation/Index.md)

### Q: How report to the host that the plug-in has new parameter titles?

Due to preset loading or user interaction the plug-in may change its parameters names (title) (but not the number of them or their IDs). To inform the host about this change, the plug-in should call from the editController its component handler function [restartComponent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html#a1f283573728cf0807224c5ebdf3ec3a6) with flag **kParamTitlesChanged**:

```
componentHandler->restartComponent (kParamTitlesChanged);
```

The host will rescan the parameter list and update the titles.

```admonish info
Note: With the flag **kParamValuesChanged** only the parameters values will be updated.
```

### Q: How receive MIDI Controllers from the host?

**MIDI** controllers are not transmitted directly to a **VST** component. **MIDI** as hardware protocol has restrictions that can be avoided in software. Controller data in particular come along with unclear and often ignored semantics. On top of this they can interfere with regular parameter automation and the host is unaware of what happens in the plug-in when passing **MIDI** controllers directly.

So any functionality that is to be controlled by **MIDI** controllers must be exported as regular parameter. The host will transform incoming **MIDI** controller data using this interface and transmit them as normal parameter change. This allows the host to automate them in the same way as other parameters.

To inform the host about this **MIDI CC**s to plug-in parameters mapping, the plug-in should implement the [IMidiMapping](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IMidiMapping.html) interface.
If the mapping has changed, the plug-in should call [IComponentHandler::restartComponent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html#a1f283573728cf0807224c5ebdf3ec3a6) (kMidiCCAssignmentChanged) to inform the host about this change.

### Q: How my parameter changes (from UI interaction) are send to the processor if the host does not process?

When a parameter is changed in the plug-in UI by user action, the plug sends this change to the host with [performEdit](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html#a135d4e76355ef0ba0a4162a0546d5f93) (do not forget to call [beginEdit](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html#a8456ad739430267a12dda11a53fe9223) and [endEdit](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html#ae380206486b11f000cad7c0d9b6e877c)), then the host has the responsibility to transfer this parameter change to the processor part: => if the audio engine is running (playing) this will be done in the next available process call => if the audio engine is not running, the host has to flush parameter changes from time to time by sending them to processor by calling process (with audio buffer set to null), in this case the plug-in should only update the parameters changes without processing any audio. This is very important that the host supports this flush mechanism else by saving plug-ins state (project/preset) the host will not get the correct updated one.

## Processing

### Q: How does Audio Processing Bypass work?

In order to implement audio process bypassing, the plug-in can export a parameter which is additionally and exclusively flagged as having the attribute kIsBypass. When the user activates the plug-in bypass in the host, like all parameter changes, this is sent as part of the parameter data passed to the [IAudioProcessor::process](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html#a6b98eb31cf38ba96a28b303c13c64e13) method.

The implementation of the bypass feature is entirely the responsibility of the plug-in:

The [IIAudioProcessor::process](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html#a6b98eb31cf38ba96a28b303c13c64e13) method will continue to be called. The plug-in must take care of artifact-free switching (ramping/fade-in/fade-out, parallel processing or algorithm changes) and must also provide a delayed action if the plug-in has a latency and be sure that the output buffers are providing a copy of the input buffers (eventually delayed). No need to copy the input buffers to the output buffers when the pointers are the same and the plug-in has no latency!

This is the choice of the plug-in to handle/process the bypass (like any other parameters) sample accurate (by using the sampleOffset of the parameter change) or audio block based (not recommended when the audio block length is too large > 1024).

During bypass the process is still called, but if not, for some reason, the host may call a flush (using process call with null audio buffer).

```admonish info
Note: The plug-in needs to save in its state the bypass parameter like any other parameters.
```

Q: Must the host deliver valid initialized Audio buffers if the associated bus is deactivated?

In a correctly implemented host, if an input or output bus exists in the host, and it has become disconnected from the plug-in, the plug-in will receive disconnection information (bus activation).

Additionally, a plug-in with a disconnected input bus will continue to receive default silence buffers, just as a plug-in with a disconnected output bus will continue to receive default nirvana buffers. When these deactivated busses are the last busses (for input or output), the host could not provide associated [AudioBusBuffers](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1AudioBusBuffers.html), in this case the plug-in should check [numInputs](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessData.html#a852a74fc4e461ef086bac048313d2de9) and [numOutputs](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessData.html#a1338255f88bad5cf4fb714c71f92b61a) and doesn't process these busses.

### Q: Can the maximum sample block size change while the plug-in is processing?

The max. sample block size ([maxSamplesPerBlock](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessSetup.html#a41cd06a0c942a1b3f283092b893d0de3)) can change during the lifetime of a plug-in, but NOT while the audio component is active. Therefore max. sample block size ([maxSamplesPerBlock](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessSetup.html#a41cd06a0c942a1b3f283092b893d0de3)) can never change during or between processing calls while the plug-in is active.

If the host changes the maximum sample block size it specifically calls the following:

```
Steinberg::Vst::IAudioProcessor::process (...);
Steinberg::Vst::IAudioProcessor::setProcessing (false);
Steinberg::Vst::IAudioProcessor::setActive (false);
 
Steinberg::Vst::IAudioProcessor::setupProcessing (...);
 
Steinberg::Vst::IAudioProcessor::setActive (true);
Steinberg::Vst::IAudioProcessor::setProcessing (true);
Steinberg::Vst::IAudioProcessor::process (...);
```

Note that the [ProcessData](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessData.html)->[numSamples](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessData.html#aeb42971a4bd34d7baa27cff8d7e3cf26) which indicates how many samples are used in a process call can change from call to call, but never bigger than the [maxSamplesPerBlock](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessSetup.html#a41cd06a0c942a1b3f283092b893d0de3).

### Q: Can the sample rate change while the plug-in is processing?

No. Same as [Q: Can the maximum sample block size change while the plug-in is processing?](#q-can-the-maximum-sample-block-size-change-while-the-plug-in-is-processing)

### Q: Can the host call the process function without Audio buffers?

Yes, the host can call [IAudioProcessor::process](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html#a6b98eb31cf38ba96a28b303c13c64e13) without buffers (numInputs and numOutputs are zeroed), in order to flush parameters (from host to plug-in).

### Q: What is a Side-Chain?

See [[3.0.0] Multiple Dynamic I/O Support](../Technical+Documentation/Change+History/3.0.0/Multiple+Dynamic+IO.md)

### Q: How can I implement a Side-chain path into my plug-in?

See [[3.0.0] Multiple Dynamic I/O Support](../Technical+Documentation/Change+History/3.0.0/Multiple+Dynamic+IO.md)

### Q: My plug-in is capable of processing all possible channel configurations.

See [[3.0.0] Multiple Dynamic I/O Support](../Technical+Documentation/Change+History/3.0.0/Multiple+Dynamic+IO.md)

### Q: How are speaker arrangement settings handled for FX plug-ins?

See [[3.0.0] Multiple Dynamic I/O Support](../Technical+Documentation/Change+History/3.0.0/Multiple+Dynamic+IO.md)

### Q: My plug-in has mono input and stereo output. How does VST 3 handle this?

See [[3.0.0] Multiple Dynamic I/O Support](../Technical+Documentation/Change+History/3.0.0/Multiple+Dynamic+IO.md)

### Q: How does it work with silence flags?

See [[3.0.0] Silence flags Support](../Technical+Documentation/Change+History/3.0.0/Silence+flags.md) and tutorial about [how to use Silence flags](../Tutorials/Advanced+VST+3+techniques.md) **<- Link?**.

### Q: How report to the host that the plug-in latency has changed?

The plug-in should call from the editController its component handler [restartComponent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html#a1f283573728cf0807224c5ebdf3ec3a6) function with flag kLatencyChanged:

```
componentHandler->restartComponent (kLatencyChanged);
```

The host will call [Vst::IAudioProcessor->getLatencySamples()](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html#af8884671ccefe68e0a86e72413a0fcf8) in order to check the new latency and adapt its latency compensation if supported.

### Q: How report to the host that the plug-in arrangement has changed?

See [[3.0.0] Multiple Dynamic I/O Support](../Technical+Documentation/Change+History/3.0.0/Multiple+Dynamic+IO.md)

### Q: Can IAudioProcessor::setProcessing be called without any IAudioProcessor::process call?

Yes, it depends how the DAW is supporting its processing, the following call sequence is legal:

```
Vst::IAudioProcessor::process (...);
Vst::IAudioProcessor::setProcessing (false);
Vst::IAudioProcessor::setProcessing (true);
// here no call to process, maybe something happen in between in the DAW
Vst::IAudioProcessor::setProcessing (false);
Vst::IAudioProcessor::setProcessing (true);
Vst::IAudioProcessor::process (...);
```

### Q: How to make sure that a plug-in is always processed?

If your plug-in always generates sound without need of any audio input, you can add the category "Generator" as subCategories (for example use [kFxGenerator](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/group__plugType.html#ga09060af560cf34b87e14d5dbd839ad52)) or you can return kInfiniteTail in the function [IAudioProcessor::getTailSamples](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html#abb6b16a66b2356a4038a778b815dbbf3)

### Q: Can IComponent::getState()/setState() be called during processing?

Yes, setState and getState are called normally from the UI Thread when the plug-in is used in a realtime context, in an offline context set/getState can be called in the same thread as the process call. Check the workflow diagram Audio Processor Call Sequence for more info about in which state which interfaces are called.

### Q: How can a plug-in be informed that it is currently processed in offline processing?

When a plug-in is used in an offline processing context (which is the case with Cubase 9.5/Nuendo 8 feature: Direct Offline Processing), its component will be initialized with [IComponent::setIoMode](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponent.html#a4618e7358890d549f990010bea4a4137) (Vst::kOfflineProcessing) (see The Simple Mode).
The offline processing mode (passed in the process call) is used when:

- the user exports audio (downmix)
- direct offline processing feature <br>
With [IComponent::setIoMode](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponent.html#a4618e7358890d549f990010bea4a4137) (Vst::kOfflineProcessing) you are able to differentiate between export and DOP (Direct Offline Processing).

[![getting_started_vid_1](https://i.ytimg.com/vi/62yMkHRfd2I/maxresdefault.jpg)](https://www.youtube.com/watch?v=62yMkHRfd2I)


Direct Offline Processing since Cubase 9.5

### Q: What should I NOT call in the realtime process function?

A good practice is to avoid any library calls from this critical realtime process. If you have to use them, check if they are designed for realtime operation and do not contain any locking mechanism. Avoid any filesystem access, networks and UI calls, memory allocation and deallocation, be careful when using STL containers which can allocate memory behind the scene, prefer patterns like non-blocking memory pools, and delegate tasks to UI/Timer thread for doing memory/file-network access jobs. Check [Audio Processor Call Sequence](https://developer.steinberg.help/display/VST/Audio+Processor+Call+Sequence) too.

## GUI-Editor

### Q: The host doesn't open my plug-in UI, why?

If you are not using **[VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md)**, please check that you provide the correct object derived from [EditorView](https://steinbergmedia.github.io/vst3_doc/vstsdk/classSteinberg_1_1Vst_1_1EditorView.html) or [CPlugInView](https://steinbergmedia.github.io/vst3_doc/vstsdk/classSteinberg_1_1CPluginView.html#a7c25891fe7dde6dc274a0ac9f20890a4) and that you overwrite the function [isPlatformTypeSupported()](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugView.html#abcfa60e135807caa316f3915622d9488).

## Compatibility with VST 2.x or VST 1

### Q: How can I update my VST 2 version of my plug-in to a VST 3 version and be sure that Cubase will load it instead of my old one?

You have to provide a special UID for your [kVstAudioEffectClass](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/ivstaudioprocessor_8h.html#ae55c95a44e931e1cd78998c94bc65ee1) and [kVstComponentControllerClass](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/ivsteditcontroller_8h.html#a49d6f6f53c7630ea334474e9998c0a99) components, based on its **VST 2** UniqueID (4 characters) and its plug-in name like this:

```
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

```
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

### Q: How can I support projects which were saved with the VST 2 version of my plug-in?

The host will call [IComponent::setState()](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponent.html#a77ac39bcc5c4b15818b1a87de2573805) and [IEditController::setComponentState()](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html#a4c2e1cafd88143fda2767a9c7ba5d48f) with the complete FXB/FXP stream. You have to extract your old state from that, for this the SDK provides a helper function [VST3::tryVst2StateLoad](https://steinbergmedia.github.io/vst3_doc/vstsdk/namespaceVST3.html#aadc6b99109a9b056a0176f49f9220822).

Here the code to add in the **VST 3** version when a **VST 3 plug-in** replaces a **VST 2** plug-in in a Steinberg sequencer project:

```
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

For complete example source code you could check the function: tresult *PLUGIN_API Processor::setState (IBStream* state)* in the file *public.sdk/samples/vst/mda-vst3/source/mdaBaseProcessor.cpp*

For Automation compatibility, you have to ensure that **VST 3** parameter IDs have the same value than the indexes of their associated parameters in **VST 2**. Only with this condition the host can play back the automation. The parameter value has the same meaning in **VST 2** and **VST 3**.

### Q: In VST 2 the editor was able to access the processing part, named effect, directly. How can I do this in VST 3?

You cannot and more importantly must not do this. The processing part and user interface part communicate via a messaging system.<br>
See [Q: How should I communicate between the 'Processing' and the 'User Interface'?](#q-how-should-i-communicate-between-the-processing-and-the-user-interface) for details.

### Q: Does VST 3 implement methods like beginEdit and endEdit known from VST 2?

Yes and it is essential to support this for automation. For details, please see [Parameters and Automation](../Technical+Documentation/Parameters+Automation/Index.md)

### Q: Does VST 3 include variable Input/Output processing like processVariableIo of VST 2?

Not in version 3.1.0, we plan something in this direction later. (Note: this variableIO processing was for example for time stretching plug-ins).

### Q: What is the equivalent to the VST 2 kPlugCategOfflineProcess?

VST 3 doesn't support offline processing like it did in VST 2 (this interface was exclusively used by **WaveLab**). But it is possible to use **VST 3 plug-ins** in an offline context (this means that the process function can be called faster than real time : for example, during an export or a batch processing). If the plug-in doesn't support faster than realtime, it should add [kOnlyRealTime](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/group__plugType.html#gae58eb0aafa16197f12c1a61428fd5584) to its category.

## Persistence

### Q: How does persistence work?

An instantiated plug-in often has state information that must be saved in order to properly re-instantiate that plug-in at a later time. A VST 3 plug-in has two states which are saved and reloaded: its component state and its controller state.

The sequence of actions for saving is:

- component->getState (compState)
- controller->getState (ctrlState)

The sequence of actions for loading is:

- component->setState (compState)
- controller->setComponentState (compState)
- controller->setState (ctrlState)

In the latter sequence you can see that the controller part will receive the component state. This allows the 2 parts to synchronize their states.

### Q: What's the difference between IEditController::setComponentState and IEditController::setState?

After a preset is loaded, the host calls [Vst::IEditController::setComponentState](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html#a4c2e1cafd88143fda2767a9c7ba5d48f) and [Vst::IComponent::setState](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponent.html#a77ac39bcc5c4b15818b1a87de2573805). Both delivering the same information. [Vst::IEditController::setState](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html#a77ac39bcc5c4b15818b1a87de2573805) is called by the host so that the plug-in is able to update its controller dependent parameters, e.g. position of scroll bars. Prior to this, there should have been a call by the host to [Vst::IEditController::getState](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html#a10db03106be8ba89d23859fa6be5d9f6), where the plug-in writes these various parameters into the stream.

See also [Q: How does persistence work?](#q-how-does-persistence-work)

## Miscellaneous

### Q: How is a normalized value converted to a discrete integer value in VST 3?

A detailed description of parameter handling is provided here: **Parameters** **<- Link?**.

### Q: What is the return value tresult?

Almost all **VST 3** interfaces return a *tresult* value. This integer value allows to return to the caller more differentiated error/success information than just a boolean value with its true and false.

The various possible values are defined in *funknown.h*. They are the same values as used in COM. Be careful when checking a *tresult* return value, because on success **kResultOk** is returned which has the integer value *0*:

```
// this is WRONG!!!!!
if (component->setActive (true))
{
}
 
// this is CORRECT!!!!!
if (component->setActive (true) == kResultOK)
{
}
// or
// this is CORRECT too!!!!!
if (component->setActive (true) != kResultOK)
{
    // error message....
}
```

### Q: Which version of Steinberg Sequencers support VST 3?

In order to load **VST 3 plug-ins** you need at least :

- For VST 3.0.0 **Cubase**/**Nuendo** 4.1.2 is needed.
- For VST 3.0.1 features **Cubase** 4.2 is needed.
- For VST 3.5.0 features **Cubase** 6.0 is needed.
- see [other VST 3 Hosts](/What+is+VST/Use+cases.md#examples-of-vst-3-host-applications)

Q: Why do plug-ins need subcategories?
When you export your plug-in in the factory instance (check *againentry.cpp*: DEF_CLASS2), you have to define a subcategory string (can be a combination of more than one string: like "**Fx|Dynamics|EQ**" for example).

Currently the subcategory string is used by **Cubase**/**Nuendo** to organize the plug-ins menu like this:

```
Computation of Folder Name (SubCategories => folder in menu)
      "Fx"                        => "Other"
      "Fx|Delay"                  => "Delay"
      "Fx|Mastering|Delay"        => "Mastering"
      "Spatial|Fx"                => "Spatial"
      "Fx|Spatial"                => "Spatial"
      "Instrument|Fx"             => if used as VSTi "" else if used as Insert "Other"
      "Instrument|Sampler"        => "Sampler"
      "Fx|Mastering|Surround"     => "Mastering\Surround"
      "Fx|Mastering|Delay|Stereo" => "Mastering\Stereo"
      "Fx|Mastering|Mono"         => "Mastering\Mono"
```

This string should only be a hint what type of plug-in it is. It's not possible to define all types. If you have wishes for new categories, please discuss them in the VST [Developer Forum](https://developer.steinberg.help/display/VST/VST+3+Forum) (<https://sdk.steinberg.net>) and we can add them to future versions of the SDK.

### Q: Is it possible to define a plug-in as Fx and Instrument?

Yes it is possible, you can use the CString [kFxInstrument](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/group__plugType.html#gabe030351fd22d14dad35c817e1849f59) ("Fx|Instrument") as subcategories (check DEF_CLASS2). In this case Steinberg Sequencers will allow the user to load it as an effect and as an instrument. The plug-in as instrument (in case of current Steinberg Sequencers <= 5.5) will not enable the Audio Input busses.

### Q: Is it possible to ask a plug-in about which speaker arrangements are supported?

No, not before the plug-in is instantiated, there is no way to ask the factory about which arrangements are supported for a given plug-in. The host can instantiate the plug-in and before start processing then set some different speaker Arrangements and check if the plug-in supports them.

### Q: Which version of Steinberg Sequencers support [VST 3 Note Expression](../Technical+Documentation/Change+History/3.5.0/INoteExpressionController.md)?

In order to use Note Expression with **VST 3 plug-ins** you need at least Cubase/Nuendo 6.0.

### Q: When compiling for Mac AudioUnit, I have a compiler error in AUCarbonViewBase.cpp. What can i do?

Due to an issue in the Mac CoreAudio SDK, not yet fixed by Apple, you have to apply a small patch to the file AUCarbonViewBase.cpp (located in CoreAudio/AudioUnits/AUPublic/AUCarbonViewBase):
=> Change:

```
HISize originalSize = { mBottomRight.h, mBottomRight.v };
to
HISize originalSize = { static_cast<CGFloat>(mBottomRight.h),
                        static_cast<CGFloat>(mBottomRight.v) };
```

### Q: How can i develop a SurroundPanner plug-in which is integrated in Nuendo as Panner?

In order to make a surroundPanner plug-in selectable as panner (Post-fader) in Nuendo, this plug-in should have as subCategories: [kSpatial](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/group__plugType.html#gaa334568999d986b4e50627646e51a8b4) or [kSpatialFx](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/group__plugType.html#ga9439d03e5e14fb7a35976d2e37f34e31) (in order to use it as insert too). For example:

```
DEF_CLASS2 (INLINE_UID_FROM_FUID(Steinberg::Vst::SPannerProcessor::cid),
            PClassInfo::kManyInstances,
            kVstAudioEffectClass,
            stringPluginName,
            Vst::kDistributable,
            Vst::PlugType::kSpatial ,
            FULL_VERSION_STR, // plug-in version (to be changed)
            kVstVersionString,
            Steinberg::Vst::SPannerProcessor::createInstance)
```

Be sure that you overwrite the function "tresult PLUGIN_API setBusArrangements ..." which allows you to get the current bus arrangements.

### Q: How can i validate my plug-in?

You have the Validator command line which can be automatically called after you compile your plug-in (when you use the cmake defined by the SDK). This will apply some standard validations. The 2cd validation tool is the [VST 3 plug-in Test Host](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md): check its menu entry: View => Open plug-in Unit Tests Window

### Q: How can i allow to create Symbolic Link on Windows?

In order to be able to create Symbolic Link on Windows you have to set the correct group policy, this will allow you to build the **VST 3** plug-ins and create a symbolic link (cmake option SMTG_CREATE_PLUGIN_LINK) for each plug-in into the folder C:\Program Files\Common Files\VST3. For this you have to start the "Edit group policy" from the Windows Search (Windows icon):
>gpedit.msc

Navigate to<br>
*Computer configuration => Windows Settings => Security Settings => Local Policies => User Rights Assignment => Create symbolic links*

Here you can set which users can create symbolic links:

![faq_1](/resources/faq_1.png)

## License


### Q: I would like to share the source code of my VST 3 plug-in/host on GitHub or other such platform.

- You can choose the [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) license and feel free to share your plug-ins/host's source code including or referencing the VST 3 SDK's sources on GitHub.
- You are allowed to provide a binary form of your plug-ins/host too, provided that you provide its source code as [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) too.
- Note that you have to follow the [Steinberg VST usage guidelines](../VST+3+Licensing/Usage+guidelines.md).

### Q: I would like to distribute my VST 3 plug-in/host as freeware/shareware in binary form only.

- You can distribute your VST 3 plug-in/host in a binary form. This always requires that you to choose the "Proprietary Steinberg VST 3" license.
- Even though you distribute your VST 3 plug-in/host as freeware/shareware you need to adhere to the requirements of the "Proprietary Steinberg VST 3" license. 
- Download the [license agreement](../VST+3+Licensing/What+are+the+licensing+options.md) (it is part of the [SDK](../Getting+Started/Links.md) too), sign it and return it to Steinberg.

### Q: I would like to sell my VST 3 plug-in/host in binary form only.

If you work for-profit and distribute your VST 3 plug-in/host in binary form, you need to choose the "Proprietary Steinberg VST 3" license.
Download the [license agreement](../VST+3+Licensing/What+are+the+licensing+options.md) (it is part of the [SDK](../Getting+Started/Links.md) too), sign it and return it to Steinberg.

### Q: I would like to adapt the VST 3 SDK's sources to my VST 3 plug-in/host's needs.

You can adapt and modify the VST 3 SDK's source for your needs, but if you want to distribute these sources under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) you have to distribute your VST 3 plug-in/host's sources under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) too.
It is allowed to modify the VST 3 SDK's when you distribute your VST 3 plug-in/host in binary form and choose the "Proprietary Steinberg VST 3" license.
If you are of the opinion that we should include your changes in the SDK, please contact us (use the [sdk.steinberg.net](https://forums.steinberg.net/c/developer/103/none)).

### Q: I would like to reuse a distributed modified version of the VST 3 SDK for my own VST 3 plug-ins/host.

Yes, but you have to make sure that your VST 3 plug-in/host sources are under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) too!

### Q: I would like to distribute my VST 3 plug-in/host in binary form based on a modified version of VST 3 SDK which is under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).

- Yes, but you have to make sure that your VST 3 plug-in/host sources are under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) too!
- Note that you have to follow the [Steinberg VST usage guidelines](../VST+3+Licensing/What+are+the+licensing+options.md).
- If you do not want to be [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html), you have to build your VST 3 plug-in/host based on the original or any private modified version of the VST 3 SDK and choose the "Proprietary Steinberg VST 3" license.

### Q: I would like to sell my VST 3 plug-in/host in binary form which is based on a 3rd party SDK like JUCE.

- If you work for-profit and distribute your plug-in/host in binary form, you need to choose the "Proprietary Steinberg VST3" license.
- Download the [license agreement](../VST+3+Licensing/What+are+the+licensing+options.md) (it is part of the [SDK](../Getting+Started/Links.md) too), sign it and return it to Steinberg.
- Note that you have to follow the [Steinberg VST usage guidelines](../VST+3+Licensing/What+are+the+licensing+options.md).

### Q: I would like to distribute my VST 3 plug-in/host in binary form which is based on a 3rd party SDK like JUCE and used its [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) license.

- Yes, but you have to make sure that your VST 3 plug-in/host sources are under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) too!
- Note that you have to follow the [Steinberg VST usage guidelines](../VST+3+Licensing/What+are+the+licensing+options.md).

### Q: Do I have to sign and send to Steinberg the "Proprietary Steinberg VST 3" license agreement for each new version of the VST 3 SDK?

- No, the license agreement has its own versioning, you just have to be sure that you have already signed the correct version of it.
- As of SDK version **3.6.8**, the license has the version **2.0** (only some minor change/formatting of the text of the license agreement were done in the last SDK versions [3.6.9 up to 3.7.1])
    - **If** you use a **VST 3 SDK version >= 3.6.8**, you have to be sure that you sent Steinberg a signed license agreement (*version 2.x*) from one of the last VST 3 SDKs (>= 3.6.8).
    - **If** you use a **VST 3 SDK version < 3.6.8**, you have to be sure that you sent Steinberg a signed license agreement (**version 1**) included in the VST 3 SDK that you use.
    - **If** you do not know if you already sent it, it is recommended to send it again and in this case it is possible to use the license agreement of the **last VST 3 SDK**, too!
    - **If** you have signed a license agreement (**version 2.x**) and a new released **VST 3 SDK** uses a new license agreement (**version 3.x**), then you have to signed it again.
- The previous explanation also applies to used 3rd parties SDK like JUCE/iPlug/SynthEdit... just check which VST 3 SDK version is used by the 3rd party SDK you work with and sign the correct license agreement or the last available one.

### Q: I would like to share the source code of my VST 2 plug-in/host on GitHub or other web-based exchange platform.

- It is allowed but be sure that you do NOT include the Steinberg VST 2 files: like *aeffect.h* and *aeffectx.h*. These files are under a different license which does not allow redistribution!

### Q: I am a developer/company and I want to develop and distribute a VST 2 plug-in and/or host in binary form.

- If you have signed the VST 2 license agreement (before October 2018), you can.
- If not, you are not allowed to distribute it!
- See [here](../Main+benefits+of+VST+3/Index.html)!
>/ [VST Home](../) / [Frequently Asked Questions](../FAQ/Index.md)
>
># Communication

[[_TOC_]]

---

## Q: How should I communicate between the 'Processing' and the 'User Interface'?

With the term 'Processing' we mean the code implementing the [Steinberg::Vst::IAudioProcessor](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html) interface, and with 'User Interface' the editor component implementing the [Steinberg::Vst::IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html) interface.

If you need to communicate the changes of parameters to the user interface, such as metering changes and peaks, you need to define the parameter as an exported type. The parameter then is associated with an ID. In the process function you can inform the host of changes by using the [outputParameterChanges](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessData.html#af08c4f7dfd9e456cc98ba0eb325993ae) (from [ProcessData](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessData.html)). You add the parameter (ID) to a list that will be used by the host to send them back to the user interface at the correct time.

If you should need to exchange more data than just parameter changes, such as tempo, sample rate, FFT, Pitch Analysis, or any other data resulting from your processing, you can use the [IMessage](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IMessage.html) interface (see AGain example). However, you need to be careful and send the data from a 'timer' thread and not directly from the process function, for example, when sending from a 'process' call.

See [Communication between the components](../Technical+Documentation/API+Documentation/Index.md#communication-between-the-components).

## Q: I want to implement an audio meter in my user interface. How do I do this?

See [Q: How should I communicate between the 'Processing' and the 'User Interface'?](#q-how-should-i-communicate-between-the-processing-and-the-user-interface)

## Q: How does the host send automation data to my VST 3 plug-in?

Automation data is sent to the audio processing method as part of the data passed as a parameter to the [IAudioProcessor::process](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html#a6b98eb31cf38ba96a28b303c13c64e13) (processData) method.

``` c++
IAudioProcessor::process (processData)
{
    IParameterChanges* paramChanges = processData.inputParameterChanges;
    //...
}
```

Automation data is transmitted as a list of parameter changes. This list always contains enough information to transmit the original automation curve from the host in a sample accurate way. Check the [AGain](../What+is+the+VST+3+SDK/Plug-in+Examples.md#again) example to see how it can be implemented.

See also [Parameters and Automation](../Technical+Documentation/Parameters+Automation/Index.md)

## Q: How report to the host that the plug-in has new parameter titles?

Due to preset loading or user interaction the plug-in may change its parameters names (title) (but not the number of them or their IDs). To inform the host about this change, the plug-in should call from the editController its component handler function [restartComponent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html#a1f283573728cf0807224c5ebdf3ec3a6) with flag **kParamTitlesChanged**:

``` c++
componentHandler->restartComponent (kParamTitlesChanged);
```

The host will rescan the parameter list and update the titles.

>ⓘ **Note**\
>With the flag **kParamValuesChanged** only the parameters values will be updated.

## Q: How receive MIDI Controllers from the host?

**MIDI** controllers are not transmitted directly to a **VST** component. **MIDI** as hardware protocol has restrictions that can be avoided in software. Controller data in particular come along with unclear and often ignored semantics. On top of this they can interfere with regular parameter automation and the host is unaware of what happens in the plug-in when passing **MIDI** controllers directly.

So any functionality that is to be controlled by **MIDI** controllers must be exported as regular parameter. The host will transform incoming **MIDI** controller data using this interface and transmit them as normal parameter change. This allows the host to automate them in the same way as other parameters.

To inform the host about this **MIDI CC**s to plug-in parameters mapping, the plug-in should implement the [IMidiMapping](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IMidiMapping.html) interface.
If the mapping has changed, the plug-in should call [IComponentHandler::restartComponent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html#a1f283573728cf0807224c5ebdf3ec3a6) (kMidiCCAssignmentChanged) to inform the host about this change.

## Q: How my parameter changes (from UI interaction) are sent to the processor if the host does not process?

When a parameter is changed in the plug-in UI by user action, the plug sends this change to the host with [performEdit](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html#a135d4e76355ef0ba0a4162a0546d5f93) (do not forget to call [beginEdit](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html#a8456ad739430267a12dda11a53fe9223) and [endEdit](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html#ae380206486b11f000cad7c0d9b6e877c)), then the host has the responsibility to transfer this parameter change to the processor part: => if the audio engine is running (playing) this will be done in the next available process call => if the audio engine is not running, the host has to flush parameter changes from time to time by sending them to processor by calling process (with audio buffer set to null), in this case the plug-in should only update the parameters changes without processing any audio. This is very important that the host supports this flush mechanism else by saving plug-ins state (project/preset) the host will not get the correct updated one.

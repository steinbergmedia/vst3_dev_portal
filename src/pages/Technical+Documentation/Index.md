>/ [VST Home](../)
>
># Technical Documentation

Browse the **VST 3 SDK**'s technical documentation. The full **VST 3 API** reference is only available in the [VST 3 Package](../Getting+Started/Links.md#getting-vst-3-sdk) that you can download or find online here:

>[![getting_started_vid_2](../../resources/steinberg_media_git_screenshot.png)](https://steinbergmedia.github.io/vst3_doc)
>
>**<https://steinbergmedia.github.io/vst3_doc>**

---

- [VST 3 API Documentation](API+Documentation/Index.md)
- [VST Module Architecture](VST+Module+Architecture/Index.md)
- [Parameters and Automation](Parameters+Automation/Index.md)
- [VST 3 Units](VST+3+Units/Index.md)
- [Presets & Program Lists](Presets+Program+Lists/Index.md)
- [Complex Plug-in Structures / Multi-timbral Instruments](Complex+Structures/Index.md)
- [VST 3 Workflow Diagrams](Workflow+Diagrams/Index.md)
- [VST 3 Locations / Format](Locations+Format/Index.md)
- [About MIDI in VST 3](About+MIDI/Index.md)
- [Change History](Change+History/Index.md)
- [(3.0.0) Interfaces supported by the plug-in](Change+History/3.0.0/Plug+in+Interfaces.md)
- [(3.0.0) Multiple Dynamic I/O Support](Change+History/3.0.0/Multiple+Dynamic+IO.md)
- [(3.0.0) Silence flags](Change+History/3.0.0/Silence+flags.md)
- [(3.0.0) Interfaces supported by the host](Change+History/3.0.0/Host+Interfaces.md)
- [(3.0.1) Parameter MIDI Mapping](Change+History/3.0.1/IMidiMapping.md)
- [(3.0.2) Parameter Finder](Change+History/3.0.2/IParameterFinder.md)
- [(3.1.0) Audio Presentation Latency](Change+History/3.1.0/IAudioPresentationLatency.md)
- [(3.1.0) UI Group Editing, Dirty State & Open Editor Request](Change+History/3.1.0/IComponentHandler2.md)
- [(3.1.0) KnobMode, Open Help & Open Aboutbox](Change+History/3.1.0/IEditController2.md)
- [(3.5.0) Note Expression](Change+History/3.5.0/INoteExpressionController.md)
- [(3.5.0) Key Switch](Change+History/3.5.0/IKeyswitchController.md)
- [(3.5.0) Remote Presentation of Parameters](Change+History/3.5.0/IXmlRepresentationController.md)
- [(3.5.0) Context Menu](Change+History/3.5.0/IComponentHandler3.md)
- [(3.5.0) Enhanced Linked Parameters](Change+History/3.5.0/IEditControllerHostEditing.md)
- [(3.6.0) iOS Inter-App Audio](Change+History/3.6.0/IAA.md)
- [(3.6.0) Preset Meta-Information](Change+History/3.6.0/IStreamAttributes.md)
- [(3.6.5) Channel Context Info](Change+History/3.6.5/IInfoListener.md)
- [(3.6.5) Unit-Bus Assignment Change](Change+History/3.6.5/IUnitHandler2.md)
- [(3.6.5) Prefetchable](Change+History/3.6.5/IPrefetchableSupport.md)
- [(3.6.5) Automation State](Change+History/3.6.5/IAutomationState.md)
- [(3.6.6) PlugView Content Scaling](Change+History/3.6.6/IPlugViewContentScaleSupport.md)
- [(3.6.8) Request Bus Activation](Change+History/3.6.8/IComponentHandlerBusActivation.md)
- [(3.6.10) UI Snapshots](Change+History/3.6.10/UI+Snapshots.md)
- [(3.6.11) NoteExpression Physical UI Mapping](Change+History/3.6.11/INoteExpressionPhysicalUIMapping.md)
- [(3.6.12) Legacy MIDI CC Out Event](Change+History/3.6.12/LegacyMIDICCOutEvent.md)
- [(3.6.12) MIDI Learn](Change+History/3.6.12/IMidiLearn.md)
- [(3.6.12) Host Query Interface Support](Change+History/3.6.12/IPlugInterfaceSupport.md)
- [(3.6.12) MPE support for Wrappers](Change+History/3.6.12/IVst3WrapperMPESupport.md)
- [(3.7.0) Parameter Function Name](Change+History/3.7.0/IParameterFunctionName.md)
- [(3.7.0) Progress Display](Change+History/3.7.0/IProgress.md)
- [(3.7.0) Process Context Requirements](Change+History/3.7.0/IProcessContextRequirements.md)
- [(3.7.0) Control Voltage Bus Flag](Change+History/3.7.0/Control+Voltage.md)

## [VST 3 API Documentation](API+Documentation/Index.md)

The **VST 3 API** is an interface collection designed for realtime audio processing components. Such a component can be an audio effect or an audio instrument.

## [VST Module Architecture](VST+Module+Architecture/Index.md)

**VST-MA** is a component model system which is used in all [Steinberg](https://www.steinberg.net/) host applications as the basic layer for plug-in support.

## [Parameters and Automation](Parameters+Automation/Index.md)

Description of how parameters are defined and used in **VST 3**

## [VST 3 Units](VST+3+Units/Index.md)

A unit is a logical section of the plug-in.

## [Presets & Program Lists](Presets+Program+Lists/Index.md)

How presets and program lists are handled in **VST 3**.

## [Complex Plug-in Structures / Multi-timbral Instruments](Complex+Structures/Index.md)

How to handle complex plug-in structures and multi-timbrality.

## [VST 3 Workflow Diagrams](Workflow+Diagrams/Index.md)

Some useful graphical call sequences a **VST 3** compliant host should follow.

## [VST 3 Locations / Format](Locations+Format/Index.md)

Formats definition of a **VST 3** Plug-in and its preset and where they are located on different platforms.

## [About MIDI in VST 3](About+MIDI/Index.md)

Unlike in **VST 2**, **MIDI** is not included in **VST 3**.

---

## [(3.0.0) Interfaces supported by the plug-in](Change+History/3.0.0/Plug+in+Interfaces.md)

List of interfaces supported/implemented by the plug-in in VST 3.0.0

## [(3.0.0) Interfaces supported by the host](Change+History/3.0.0/Host+Interfaces.md)

List of interfaces supported/implemented by the host in VST 3.0.0

## [(3.0.1) Parameter MIDI Mapping](Change+History/3.0.1/IMidiMapping.md)

How the mapping works between MIDI CCs and parameters.

## [(3.0.2) Parameter Finder](Change+History/3.0.2/IParameterFinder.md)

How the host can retrieve the parameter where the mouse cursor is located.

## [(3.1.0) Audio Presentation Latency](Change+History/3.1.0/IAudioPresentationLatency.md)

Inform the plug-in about how long from the moment of generation/acquiring (from file or from Input) it will take for its input to arrive, and how long it will take for its output to be presented (to output or to speaker).

## [(3.1.0) UI Group Editing, Dirty State & Open Editor Request](Change+History/3.1.0/IComponentHandler2.md)

Improvement of the plug-in's integration in the host (dirty state, request Open Editor, group editing).

## [(3.1.0) KnobMode, openHelp & openAboutBox](Change+History/3.1.0/IEditController2.md)

Extension to allow the host to inform the plug-in about the host knob mode.

## [(3.5.0) Note Expression](Change+History/3.5.0/INoteExpressionController.md)

A new way to control / modify / change a specific played note during playback.

## [(3.5.0) Key Switch](Change+History/3.5.0/IKeyswitchController.md)

Allows information exchange between the plug-in and host about which key switches are currently used.

## [(3.5.0) Remote Presentation of Parameters](Change+History/3.5.0/IXmlRepresentationController.md)

How to better support remote (UI and hardware) for parameters.

## [(3.5.0) Context Menu](Change+History/3.5.0/IComponentHandler3.md)

A plug-in can ask the host to create a context menu for a given exported parameter ID or a generic context menu.

## [(3.5.0) Enhanced Linked Parameters](Change+History/3.5.0/IEditControllerHostEditing.md)

This allows the host to start a parameter editing action which can generate other parameter changes (like linked parameters) and this in one session (between a beginEdit and endEdit).

## [(3.6.0) iOS Inter-App Audio](Change+History/3.6.0/IAA.md)

iOS InterApp-Audio application out of your **VST 3 plug-in**.

## [(3.6.0) Preset Meta-Information](Change+History/3.6.0/IStreamAttributes.md)

Interface to access preset meta information from stream, used, for example, in [setState](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponent.html#a77ac39bcc5c4b15818b1a87de2573805) in order to inform the plug-in about the current context in which the preset loading occurs.

## [(3.6.5) Channel Context Info](Change+History/3.6.5/IInfoListener.md)

Allows the host to inform the plug-in about the context in which the plug-in is instantiated, mainly channel based info (color, name, index, ...).

## [(3.6.5) Unit-Bus Assignment Change](Change+History/3.6.5/IUnitHandler2.md)

The plug-in has the possibility to inform the host with [notifyUnitByBusChange](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IUnitHandler2.html#ad1f48213839cc5b28a612a2baaba6584) that something has changed in the bus - unit assignment.

## [(3.6.5) Prefetchable](Change+History/3.6.5/IPrefetchableSupport.md)

Indicates if the plug-in supports prefetch (dynamically).

## [(3.6.5) Automation State](Change+History/3.6.5/IAutomationState.md)

Hosts can inform the plug-in about its current automation state (Read/Write/Nothing).

## [(3.6.6) PlugView Content Scaling](Change+History/3.6.6/IPlugViewContentScaleSupport.md)

This interface communicates the content scale factor from the host to the plug-in view on systems where plug-ins cannot get this information directly like Microsoft Windows.

## [(3.6.8) Request Bus Activation](Change+History/3.6.8/IComponentHandlerBusActivation.md)

Allows the plug-in to request the host to activate or deactivate a specific bus.

## [(3.6.10) UI Snapshots](Change+History/3.6.10/UI+Snapshots.md)

A **VST 3** bundle can contain pre-rendered snapshot images for a **VST 3** host as a visual representation of the plug-in UI.

## [(3.6.11) NoteExpression Physical UI Mapping](Change+History/3.6.11/INoteExpressionPhysicalUIMapping.md)

With this plug-in interface, the host can retrieve the preferred physical mapping associated to note expression supported by the plug-in.

## [(3.6.12) Legacy MIDI CC Out Event](Change+History/3.6.12/LegacyMIDICCOutEvent.md)

This kind of event is reserved for generating MIDI CC as output event for kEvent Bus during the process call.

## [(3.6.12) MIDI Learn](Change+History/3.6.12/IMidiLearn.md)

If this interface is implemented by the edit controller, the host will call this method whenever there is live MIDI-CC input for the plug-in.

## [(3.6.12) Host Query Interface Support](Change+History/3.6.12/IPlugInterfaceSupport.md)

Allows a plug-in to ask the host if a given plug-in interface is supported/used by the host.

## [(3.6.12) MPE support for Wrappers](Change+History/3.6.12/IVst3WrapperMPESupport.md)

Implemented on wrappers that support **MPE** ([MIDI Polyphonic Expression](https://www.midi.org/midi-articles/midi-polyphonic-expression-mpe)) to [Note Expression](Change+History/3.5.0/INoteExpressionController.md) translation.

## [(3.7.0) Parameter Function Name](Change+History/3.7.0/IParameterFunctionName.md)

This interface allows the host to get a parameter associated to a specific meaning (a functionName) for a given unit

## [(3.7.0) Progress Display](Change+History/3.7.0/IProgress.md)

Allows the plug-in to request the host to create a progress for some specific tasks which take some time.

## [(3.7.0) Process Context Requirements](Change+History/3.7.0/IProcessContextRequirements.md)

To get accurate process context information ([Vst::ProcessContext](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessContext.html)), it is now required to implement this interface.

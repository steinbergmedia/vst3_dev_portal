>/ [VST Home](../../index.md) / [Technical Documentation](../Index.md)
>
># About MIDI in VST 3

**On this page:**

[[_TOC_]]

**Related pages:**

- [[3.0.1] Parameter MIDI Mapping](../Change+History/3.0.1/IMidiMapping.md)
- [[3.5.0] Note Expression](../Change+History/3.5.0/INoteExpressionController.md)
- [[3.5.0] Key Switch](../Change+History/3.5.0/IKeyswitchController.md)
- [[3.6.11] NoteExpression Physical UI Mapping](../Change+History/3.6.11/INoteExpressionPhysicalUIMapping.md)
- [[3.6.12] Legacy MIDI CC Out Event](../Change+History/3.6.12/LegacyMIDICCOutEvent.md)
- [[3.6.12] MPE support for Wrappers](../Change+History/3.6.12/IVst3WrapperMPESupport.md)

---

Unlike in **VST 2, MIDI** is not included in **VST 3**.

But **VST 3** offers suitable concepts that can be translated to and from MIDI using [Event](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1Event.html):

![tech_doc_27](../../../resources/tech_doc_27.png)

## Related Concepts in MIDI and VST 3

Relationship of concepts in **MIDI 1.0** to **VST 3**

| MIDI 1.0 | VST 3 | Defined in |
| :- | :- | :- |
| Port | Bus of [Steinberg::Vst::MediaType](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/group__vstBus.html#ga576e5da9bdc49812cf65f803bb303ad5), [Steinberg::Vst::MediaTypes::kEvent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/group__vstBus.html#gga576e5da9bdc49812cf65f803bb303ad5ae6a97de99980aeac9312e818af337d6f) | *ivstcomponent.h* |
| Channel | Channel of a Bus, [Unit by Bus](../VST+3+Units/Index.md) and Channel | *ivstcomponent.h*, *ivstunits.h* |
| Note-On | [Steinberg::Vst::NoteOnEvent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1NoteOnEvent.html) | *ivstevents.h* |
| Note-Off | [Steinberg::Vst::NoteOffEvent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1NoteOffEvent.html) | *ivstevents.h* |
| Poly Key Pressure | [Steinberg::Vst::PolyPressureEvent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1PolyPressureEvent.html) | *ivstevents.h* |
| Control Change | [Parameter](../Parameters+Automation/Index.md), [IMidiMapping](../Change+History/3.0.1/IMidiMapping.md) | *ivstcomponent.h*, *ivstmidicontrollers.h* |
| Channel Pressure | [Parameter](../Parameters+Automation/Index.md), [IMidiMapping](../Change+History/3.0.1/IMidiMapping.md) | *ivstcomponent.h*, *ivstmidicontrollers.h* |
| Pitch Bend | [Parameter](../Parameters+Automation/Index.md), [IMidiMapping](../Change+History/3.0.1/IMidiMapping.md) | *ivstcomponent.h*, *ivstmidicontrollers.h* |
| Program Change | [Parameter](../Parameters+Automation/Index.md), [kIsProgramChange](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ParameterInfo.html#ae3a5143ca8d0e271dbc259645a4ae645a517665185bca1f4f3d77ce0a6468b8e3), [Steinberg::Vst::ProgramListInfo](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProgramListInfo.html) | *ivstcomponent.h*, *ivstunits.h* |
| MPE (MIDI Polyphonic Expression) | [NoteExpression](../Change+History/3.5.0/INoteExpressionController.md), [PhysicalUI](../Change+History/3.6.11/INoteExpressionPhysicalUIMapping.md) | *ivstnoteexpression.h*, *ivstphysicalui.h* |
| System Exclusive | [Steinberg::Vst::DataEvent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1DataEvent.html) of Type [Steinberg::Vst::DataEvent::kMidiSysEx](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1DataEvent.html#afb6eb4f28419b652027fad41104a6d22ab06d86440be6a85eccce4df100ce8e79) | *ivstevents.h* |

<br>Additional relationships of concepts introduced in MIDI 2.0 (<https://www.midi.org/>) to **VST 3**

| MIDI 2.0 | VST 3 | Defined in/Comments |
| :- | :- | :- |
| Group (of Channels) | Bus of [Steinberg::Vst::MediaType](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/group__vstBus.html#ga576e5da9bdc49812cf65f803bb303ad5), [Steinberg::Vst::MediaTypes::kEvent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/group__vstBus.html#gga576e5da9bdc49812cf65f803bb303ad5ae6a97de99980aeac9312e818af337d6f) | *ivstcomponent.h* |
| Registered Per-Note Controller | [NoteExpression](../Change+History/3.5.0/INoteExpressionController.md), [PhysicalUI](../Change+History/3.6.11/INoteExpressionPhysicalUIMapping.md) | *ivstnoteexpression.h*, *ivstphysicalui.h* |
| Assignable Per-Note Controller | [NoteExpression](../Change+History/3.5.0/INoteExpressionController.md) | *ivstnoteexpression.h* |
| System Exclusive 8-Bit | indirect support | The host can translate to 7-Bit, [Steinberg::Vst::DataEventof](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1DataEvent.html) Type [Steinberg::Vst::DataEvent::kMidiSysEx](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1DataEvent.html#afb6eb4f28419b652027fad41104a6d22ab06d86440be6a85eccce4df100ce8e79) |
| Registered Controller | not supported | The host can do detailed tuning via [NoteExpression](../Change+History/3.5.0/INoteExpressionController.md) |
| Assignable Controller | not supported | The host should offer mapping to parameters |
| Relative Registered Controller | not supported | The host is free to translate this to parameters |
| Relative Assignable Controller | not supported | The host is free to translate this to parameters |
| Per-Note Pitch Bend | not supported | The host can do detailed tuning via [NoteExpression](../Change+History/3.5.0/INoteExpressionController.md) |
| Mixed Data Set | not supported | not supported |

## MIDI 2.0 Per-Note Controllers

There are many subtle differences between **MIDI 2.0** Per-Note Controllers and [**VST 3** NoteExpression](../Change+History/3.5.0/INoteExpressionController.md). The good thing is that plug-in developers do not have to do anything about it. It is the host's duty to translate from MIDI 2.0 to **VST 3**.

## MIDI 2.0 Increased Resolution, compared to MIDI 1.0

**MIDI 2.0** achieved a significant increase in resolution of many important values, like Velocity, Pressure, and Controllers compared to **MIDI 1.0**. Nevertheless, **VST 3** still has superior resolution than **MIDI 2.0**. Plug-ins and hosts supporting **VST 3** should make use of these capabilities and should not stick to a 0-127 mindset.

See the following tables to compare the resolution of specific values in **MIDI 1.0**, **MIDI 2.0**, and **VST 3**.

| Value | MIDI 1.0 | MIDI 2.0 | VST 3 |
| :- | :- | :- | :- |
| Velocity (On & Off) | 7 Bit integer | 16 Bit integer | 32 Bit float |
| Poly Pressure :- |7 Bit integer | 32 Bit integer | 32 Bit float |
| Channel Pressure / Parameters | 7 Bit integer | 32 Bit integer | 64 Bit float |
| Controllers / Parameters | 7-14 Bit integer | 32 Bit integer | 64 Bit float |
| Pitch Bend / Parameters | 14 Bit integer | 32 Bit integer | 64 Bit float |
| Note Attribute Tuning :- |not available | 16 Bit fixed point (7.9) | 32 Bit float |
| Per-Note Controllers / [NoteExpression](../Change+History/3.5.0/INoteExpressionController.md) | not available | 32 Bit integer | 64 Bit float |
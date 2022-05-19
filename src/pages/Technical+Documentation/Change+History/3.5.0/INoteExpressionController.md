>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># [3.5.0] Note Expression

**On this page:**

[[_TOC_]]

**Related pages:**

- [(3.5.0) Key Switch](../3.5.0/IKeyswitchController.md)
- [(3.6.11) NoteExpression Physical UI Mapping](../3.6.11/INoteExpressionPhysicalUIMapping.md)
- [About MIDI in VST 3](../../About+MIDI/Index.md)

---

A new way to control / modify / change a specific played note during playback.

## Introduction

Edit controller component interface extension: [Vst::INoteExpressionController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1INoteExpressionController.html)

- [plug imp]
- [extends [IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html)]
- [released: 3.5.0]
- [optional]

Note Expression is a new way of event controller editing in hosts supporting this VST 3.5 feature (in **Cubase** since version 6).

[![getting_started_vid_5](https://i.ytimg.com/vi/7sX8_VDS1AU/maxresdefault.jpg)](https://www.youtube.com/watch?v=7sX8_VDS1AU)

[![getting_started_vid_6](https://i.ytimg.com/vi/VqfYm4MzfAU/maxresdefault.jpg)](https://www.youtube.com/watch?v=VqfYm4MzfAU)

With **VST 3** Note Expression, the plug-in is able to break free from the limitations of MIDI controller events by providing access to new **VST 3** controller events that provide articulation information for each individual note (event) in a polyphonic arrangement according to its noteId.

A major limitation of **MIDI** is the nature of controller information; controllers are only channel messages (Pitchbend, Modulation, ...) and cannot be assigned to a specific playing note, with the exception of poly pressure (polyphonic aftertouch), which allows change only for a given pitch (not a given note!).

Articulating each note in a chord individually creates a much more natural feel, just like multiple players playing the same instrument at the same time but each adding their own personality to the notes played.

For example **Cubase 6** introduces the first **VST 3 Note Expression** compatible virtual instrument: **HALion Sonic SE**. **HALion Sonic SE** not only supports "standard" note expression control for Tuning (Pitch), Volume and Pan, it also offers additional custom pre-assigned note expression types of event ([kCustomStart](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/namespaceSteinberg_1_1Vst.html#a7d66c573aff27d890ec154f45b61f310a1c30475ef992f89f37c2fe0aafcc6283) in [Steinberg::Vst::NoteExpressionTypeIDs](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/namespaceSteinberg_1_1Vst.html#a7d66c573aff27d890ec154f45b61f310)).

## How does it work?

The best way to understand how to support note expression from the plug-in side is to check out the step by step implementation example below. For more details, check out the *Note Expression Synth* example included in the SDK.

Step by Step:
We want a mono-timbral (1 channel) instrument plug-in with 1 event bus and support for the detune ([kTuningTypeID](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/namespaceSteinberg_1_1Vst.html#a7d66c573aff27d890ec154f45b61f310ac196000d5497502327e2b4f69e5037be)) note expression:

1. The instrument Plug-in must have at least one input event bus:

``` c++
//------------------------------------------------------------------
tresult PLUGIN_API MyExampleProcessor::initialize (FUnknown* context)
{
    //---always initialize the parent-------
    tresult result = AudioEffect::initialize (context);
    if (result == kResultTrue)
    {
        // we want a Stereo Output
        addAudioOutput (STR16 ("Stereo Output"), SpeakerArr::kStereo);

        // create Event In bus (1 bus with only 1 channel)
        addEventInput (STR16 ("Event Input"), 1);
    }
    return result;
}
```

2. The controller must provide the [Vst::INoteExpressionController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1INoteExpressionController.html) interface, like below:

``` c++
//------------------------------------------------------------------
class MyExampleController: public EditController, public INoteExpressionController
{
public:
    // ...
    //---from INoteExpressionController
    virtual int32 PLUGIN_API getNoteExpressionCount (int32 busIndex, int16 channel) SMTG_OVERRIDE;
    virtual tresult PLUGIN_API getNoteExpressionInfo (int32 busIndex, int16 channel, int32 noteExpressionIndex, NoteExpressionTypeInfo& info) SMTG_OVERRIDE;
    virtual tresult PLUGIN_API getNoteExpressionStringByValue (int32 busIndex, int16 channel, NoteExpressionTypeID id, NoteExpressionValue valueNormalized, String128 string) SMTG_OVERRIDE;
    virtual tresult PLUGIN_API getNoteExpressionValueByString (int32 busIndex, int16 channel, NoteExpressionTypeID id, const TChar* string, NoteExpressionValue& valueNormalized) SMTG_OVERRIDE;
    // ...

    OBJ_METHODS (MyExampleController, EditController)
    DEFINE_INTERFACES
        DEF_INTERFACE (INoteExpressionController)
    END_DEFINE_INTERFACES (EditController)

    REFCOUNT_METHODS(EditController)
    //...
};
```

3. Now we have to implement the [Steinberg::Vst::INoteExpressionController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1INoteExpressionController.html) interface, in our example [Steinberg::Vst::INoteExpressionController::getNoteExpressionCount](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1INoteExpressionController.html#a197a1b66cc45ba1935d9ce0894b1ee02) should return 1 as we only want to support tuning:

``` c++
//------------------------------------------------------------------
int32 PLUGIN_API MyExampleController::getNoteExpressionCount (int32 busIndex, int16 channel)
{
    // we accept only the first bus and 1 channel
    if (busIndex == 0 && channel == 0)
        return 1;
    return 0;
}
```

4. Then we have to implement [Steinberg::Vst::INoteExpressionController::getNoteExpressionInfo](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1INoteExpressionController.html#ab12d543cbd83560a9f098ed4a5c76af8) which describes what note expression the plug-in supports:

``` c++
//  ------------------------------------------------------------------
tresult PLUGIN_API MyExampleController::getNoteExpressionInfo (int32 busIndex, int16 channel, int32 noteExpressionIndex,
                            NoteExpressionTypeInfo& info)
{
    // we accept only the first bus and 1 channel and only 1 Note Expression (tuning)
    if (busIndex == 0 && channel == 0 && noteExpressionIndex == 0)
    {
        memset (&info, 0, sizeof (NoteExpressionTypeInfo));

        // set the tuning type
        info.typeId = kTuningTypeID;

        // set some strings
        USTRING ("Tuning").copyTo (info.title, 128);
        USTRING ("Tun").copyTo (info.shortTitle, 128);
        USTRING ("Half Tone").copyTo (info.units, 128);

        info.unitID = -1; // no unit wanted
        info.associatedParameterID = -1; // no associated parameter wanted

        info.flags = NoteExpressionTypeInfo::kIsBipolar; // event is bipolar (centered)

        // for Tuning the convert functions are : plain = 240 * (norm - 0.5); norm = plain / 240 + 0.5;
        // we want to support only +/- one octave
        double kNormTuningOneOctave = 12.0 / 240.0;

        info.valueDesc.minimum = 0.5 - kNormTuningOneOctave;
        info.valueDesc.maximum = 0.5 + kNormTuningOneOctave;
        info.valueDesc.defaultValue = 0.5; // middle of [0, 1] => no detune (240 * (0.5 - 0.5) = 0)
        info.valueDesc.stepCount = 0; // we want continuous (no step)

        return kResultTrue;
    }

    return kResultFalse;
}
```

5. For displaying note expression values, we have to implement the conversion functions:
    - [Steinberg::Vst::INoteExpressionController::getNoteExpressionStringByValue](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1INoteExpressionController.html#a457f017fc3566d143914e44523425d23): normalized value -> string

``` c++
//------------------------------------------------------------------
tresult PLUGIN_API  MyExampleController::getNoteExpressionStringByValue (int32 busIndex, int16 channel, NoteExpressionTypeID id, NoteExpressionValue valueNormalized, String128 string)
{
    // here we use the id (not the index)
    if (busIndex == 0 && channel == 0 && id == kTuningTypeID)  
    {
        // here we have to convert a normalized value to a Tuning string representation
        UString128 wrapper;
        valueNormalized = (240 * valueNormalized) - 120; // compute half Tones
        wrapper.printFloat (valueNormalized, 2);
        wrapper.copyTo (string, 128);

        return kResultTrue;
    }

    return kResultFalse;
}
```

    - [Steinberg::Vst::INoteExpressionController::getNoteExpressionValueByString](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1INoteExpressionController.html#ab79e988315e33b4c30c8f2bd47a0cffc): string -> normalized value

``` c++
//------------------------------------------------------------------
tresult PLUGIN_API  MyExampleController::getNoteExpressionValueByString (int32 busIndex, int16 channel, NoteExpressionTypeID id,
                            const TChar* string, NoteExpressionValue& valueNormalized);
{
    // here we use the id (not the index)
    if (busIndex == 0 && channel == 0 && id == kTuningTypeID)
    {
        // here we have to convert a given tuning string (half Tone) to a normalized value
        String wrapper ((TChar*)string);
        ParamValue tmp;
        if (wrapper.scanFloat (tmp))
        {
            valueNormalized = (tmp + 120) / 240;
            return kResultTrue;
        }
    }

    return kResultFalse;
}
```

6. Last step, in the processor component we have to adapt the process call to interpret the note expression event ([Steinberg::Vst::NoteExpressionValueEvent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1NoteExpressionValueEvent.html)) sent from the host to the plug-in:

``` c++
//------------------------------------------------------------------
tresult MyExampleProcessor::process (ProcessData& data)
{
    // ....
    // get the input event queue
    IEventList* inputEvents = data.inputEvents;
    if (inputEvents)
    {
        Event e;
        int32 numEvents = inputEvents->getEventCount ();

        // for each events check it..
        for (int32 i = 0; i < numEvents; i++)
        {
            if (inputEvents->getEvent (i, e) == kResultTrue)
            {
                switch (e.type)
                {
                    //-----------------------
                    case Event::kNoteOnEvent:
                    {
                        // here a note On, we may need to play something a keep a trace of the e.noteOn. noteId
                        break;
                    }
                    //-----------------------
                    case Event::kNoteOffEvent:
                    {
                        // here we have to release the voice associated to this id : e.noteOff.noteId
                        // Note that kNoteExpressionValueEvent event could be sent after the note is in released
                        break;
                    }
                    //-----------------------
                    case Event::kNoteExpressionValueEvent:
                    {
                        // here are the Note Expression interpretation

                        // we check and use only tuning expression
                        if (e.noteExpressionValue.typeId == kTuningTypeID)
                        {
                            // we have to find the voice which be changed (the note could be in released state)
                            VoiceClass* voice = findVoice (e. noteExpressionValue.noteId);
                            if (voice)
                            {
                                // we apply to it the wanted value (for a given type of note expression (detune, volume....)
                                voice->setNoteExpressionValue (e. noteExpressionValue.typeId, e. noteExpressionValue.value);
                            }
                            // if the associated id is not anymore marked as playing voice (end of release reached) we ignore the Note Expression Event
                        }

                        break;
                    }
                }
            }
        }
    }
    // ...
}
```

That is it!

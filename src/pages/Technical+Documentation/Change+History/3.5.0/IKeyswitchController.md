>/ [VST Home](../../../index.md) / [Technical Documentation](../../Index.md)
>
># [3.5.0] Key Switch

**On this page:**

[[_TOC_]]

**Related pages:**

- [[3.5.0] Note Expression](../3.5.0/INoteExpressionController.md)

---

Allows information exchange between the plug-in and host about which key switches are currently used.

## Introduction

Extended plug-in interface [IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html) for key switches support: [Vst::IKeyswitchController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IKeyswitchController.html)

- [plug imp]
- [extends [IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html)]
- [released: 3.5.0]
- [optional]

Some instrument plug-ins support key switching functionality, which allows the user to switch between different layered sounds while playing notes. To achieve this, the user has to press a specific key associated to the wanted layer before playing new notes.

A typical example is a sample-based player plug-in with a violin sound, which can include different layers or articulations: pizzicato, legato, tremolo, etc. By pressing or by keeping pressed a specific key, for example C-1, before playing new notes, the plug-in will choose to play pizzicato, by using D-1, it will play legato, and so on.

With [VST Expression Map](https://www.steinberg.net/de/technology/) (introduced by Steinberg in Cubase 5), these key switches can be used in the Score Editor, to associate a symbol (articulation) to a note. Each time this note is played, the corresponding key switch will be used (sent to the plug-in as noteOn event).

[![getting_started_vid_7](https://i.ytimg.com/vi/D5dj1v6EL2M/maxresdefault.jpg)](https://www.youtube.com/watch?v=D5dj1v6EL2M)

In order to help the creation of such a map, VST 3.5 defines a new interface [Steinberg::Vst::IKeyswitchController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IKeyswitchController.html). If an (instrument) plug-in supports such an interface, the host can get the current set of used key switches from the plug-in (megatrigg / articulation: [Steinberg::Vst::KeyswitchInfo](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1KeyswitchInfo.html)) for a given channel of an event bus, and then automatically use them (like in **Cubase 6**) to create a [VST Expression Map](https://o.steinberg.net/en/support/content_and_accessories/expression_maps_for_vst_expression.html).

## How does it work?

Here the step by step example.
We want a plug-in with 1 event bus, which is mono-timbral (1 channel), and which supports 2 key switches:

1. The instrument plug-in should have one input event bus (could be more):

    ```
    //  ------------------------------------------------------------------    ------
    tresult PLUGIN_API MyExampleProcessor::initialize (FUnknown*    context)
    {
        //---always initialize the parent-------
        tresult result = AudioEffect::initialize (context);
        if (result == kResultTrue)
        {
            // we want a Stereo Output
            addAudioOutput (STR16 ("Stereo Output"),    SpeakerArr::kStereo);
    
            // create Event In bus (1 bus with only 1 channel)
            addEventInput (STR16 ("Event Input"), 1);
        }
        return result;
    }
    ```

2. The controller should have the interface [Steinberg::Vst::IKeyswitchController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IKeyswitchController.html), here in the class declaration:

    ```
    //  ------------------------------------------------------------------    -----------
    class MyExampleController: public EditController, public    IKeyswitchController
    {
    public:
        //...
        //---from IKeyswitchController
        virtual int32 PLUGIN_API getKeyswitchCount (int32 busIndex,     int16 channel);
        virtual tresult PLUGIN_API getKeyswitchInfo (int32 busIndex,    int16 channel, int32 keySwitchIndex, KeyswitchInfo& info);
        //...
    
        OBJ_METHODS (MyExampleController, EditController)
        DEFINE_INTERFACES
            DEF_INTERFACE (IKeyswitchController)
        END_DEFINE_INTERFACES (EditController)
    
        REFCOUNT_METHODS(EditController)
        //...
    };
    ```

3. Now we have to implement the interface [Steinberg::Vst::IKeyswitchController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IKeyswitchController.html) (only 2 functions), in our example [Steinberg::Vst::IKeyswitchController::getKeyswitchCount](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IKeyswitchController.html#aa98a707edb1b58d05da0c50e38983a4e) should return 2 (2 key switches):

    ```
    //  ------------------------------------------------------------------    ------
    int32 MyExampleController::getKeyswitchCount (int32 busIndex,   int16 channel)
    {
        // we accept only the first bus and 1 channel
        if (busIndex == 0 && channel == 0)
            return 2;
        return 0;
    }
    ```

4. Then, we have to implement [Steinberg::Vst::IKeyswitchController::getKeyswitchInfo](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IKeyswitchController.html#a8193190849039a70d08b084241d29e38), which allows to inform the host about what the plug-in supports:

    ```
    //  ------------------------------------------------------------------    ------
    tresult PLUGIN_API MyExampleController::getKeyswitchInfo (int32     busIndex, int16 channel, int32 keySwitchIndex, KeyswitchInfo&   info)
    {
        // we accept only the first bus and 1 channel and only 2    keyswitches
        if (busIndex == 0 && channel == 0 && (keySwitchIndex == 0 ||    keySwitchIndex == 1)
        {
            memset (&info, 0, sizeof (KeyswitchInfo));
    
            // in this case we want that Keyswitch should be    maintained pressed for playing
            info.typeId = kKeyRangeTypeID;

            // we could use keyRemapped to make easier the use of the   keyswitch (near the available instrument key range)
            // take care that there are no overlap between  keyswitches and real key (playing sound)
    
            if (keySwitchIndex == 0)
            {
                USTRING ("Accentuation").copyTo (info.title, 128);
                USTRING ("Acc").copyTo (info.shortTitle, 128);
    
                // if the user keeps pressed C-1 or C#-1 or C-0 then    the Accentuation sound should be played
                info.keyswitchMin = 12; // C-1
                info.keyswitchMax = 13; // C#-1
                info.keyRemapped  = 24; // C-0
            }
            else
            {
                USTRING ("Softly").copyTo (info.title, 128);
                USTRING ("Soft").copyTo (info.shortTitle, 128);

                // if the user keeps pressed D-1 or D#-1 or D-0 then    the Softly sound should be played
                info.keyswitchMin = 14; // D-1
                info.keyswitchMax = 15; // D#-1
                info.keyRemapped  = 26; // D-0
            }
    
            info.unitID = -1; // not used
            info.flags = 0;  // not used

            return kResultTrue;
        }
        return kResultFalse;
    }
    ```

5. Last step, in the processor component, we have to adapt the process call to switch to the wanted articulation:

    ```
    //  ------------------------------------------------------------------    ------
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
                            // here a note On
                            // check if this is a Keyswitch
                            switch (e.noteOn.pitch)
                            {
                                // Accentuation Keyswitch
                                case 12:
                                case 13:
                                case 24:
                                    currentLayer = kAccentuationLayer;
                                    break;
    
                                // Softly Keyswitch
                                case 14:
                                case 15:
                                case 26:
                                    currentLayer = kSoftlyLayer;
                                    break;
    
                                default:
                                    // play the note in the     currentLayer
                                    // ...
                            }
                        }   break;

                        //-----------------------
                        case Event::kNoteOffEvent:
                        {
                            // check if keyswitch is released
                            switch (e.noteOff.pitch)
                            {
                                // Accentuation Keyswitch
                                case 12:
                                case 13:
                                case 24:
                                case 14:
                                case 15:
                                case 26:
                                    currentLayer = kDefaultLayer;
                                    break;
                                default:
                                    // released note...
                                    //...
                            }
                        }   break;
                        //....
                    }
                }
            }
        }
        //...
    }
    ```

That is it!
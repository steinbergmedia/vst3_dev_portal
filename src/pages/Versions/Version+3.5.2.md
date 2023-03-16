>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.5.2 (2012/09/25)

## Version 3.5.2 (2012/09/25)

- Interface Changes:
  - Note Expression supports a new event type: NoteExpressionTextEvent
- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - Fix Visual Studio 2010 projects (filters added)
  - Adaptation for XCode4 (The again sample project uses [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) 3.6 which needs the 10.6 SDK for the 32 bit build, in later Xcode tools this SDK is not available. If you use VSTGUI 3.6 you need to use a Xcode version which has the 10.6 SDK or earlier included.)
- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - VST 3 - Audio Unit Wrapper:
    - fix noteOn and noteOff offset
    - fix RestoreState with IO bus changes
    - MIDI PolyPressure support added
    - non-automatable parameters have now FlagAudioUnitParameterFlag_NonRealTime AU flag
    - fix under Logic where sample rate was not set for mono track
  - VST 3 - VST 2.x Wrapper:
    - fix getMidiProgramCategory
- New Flags/Enums:
  - New predefined Speaker Arrangements: 9.0/9.1/10.0/10.1/11.0/11.1/13.0/13.1 based on Auro 3D definition (<https://www.auro-3d.com/>).
- Helpers Classes:
  - New in Base:
    - class Steinberg::Region
    - class Steinberg::IStreamWrapper
    - Helper Steinberg::HexBinary: HexBinary encoding and decoding
- Some documentation changes
  - [Steinberg::Vst::IParameterFinder](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IParameterFinder.html): To enable important functionalities (like AI Knob) a recommendation to implement this interface was added.
  - The VST 3 plug-in locations priority has been changed: Application level should be scanned from host after Global level.
- Licensing change for example source code files

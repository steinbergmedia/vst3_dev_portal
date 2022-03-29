>/ ... / [Change History](../Index.md)
>
># Version 3.1.0 (2010/06/25)

## Version 3.1.0 (2010/06/25)

- Restructuring of the SDK :
    - new Base Module (many useful classes, such as templates and containers)
    - Renamed the file public.sdk/source/main/pluginfactory.cpp to public.sdk/source/main/pluginfactoryvst3.cpp
    - Renamed the file public.sdk/source/main/pluginfactory.h to public.sdk/source/main/pluginfactoryvst3.h
    - Renaming Microsoft Visual Projects
- New Interfaces:
    - Steinberg::Vst::IEditController2 : support for setKnobMode/openHelp/openAboutBox
    - Steinberg::Vst::IComponentHandler2 : support for parameter group editing from Plug-in UI, dirty state and request host to open the Plug-in editor
    - Steinberg::Vst::IAudioPresentationLatency : informs the Plug-in about the Audio Presentation Latencies (in/out)
- New Event Structure:
    - Steinberg::Vst::PolyPressureEvent : Polypressure event support
- New Flags/Enums:
    - New Plug-in Types used for subCategories : PlugType::kMono, PlugType::kStereo, PlugType::kSurround
    - New parameter flag ParameterInfo::kIsList : flags the parameter as a list of discrete string values
    - New IoModes enum : Steinberg::Vst::IoModes::kOfflineProcessing used with setIoMode when the Plug-in is used in an offline processing context
- Plug-ins Wrappers:
    - New VST 3 - VST 2.x Wrapper : by just adding small initializing code, you can provide a VST 2.x version of your **VST 3 Plug-in**
    - New VST 3 - Audio Unit Wrapper with just a few build settings, you can provide AU support with your VST 3 Plug-in
- Samples:
    - New **VST 3 Plug-ins** examples: ADelay Plug-in, mda **VST 3 Plug-ins** (thanks Paul Kellet and Arne Scheffler)
    - Remove Visual Studio 2003 projects
    - Clean up AGain and add separate version supporting side-chain
- New features of the VST 3 Plug-in Test Host :
    - MIDI Input support
    - better ASIO support
    - Mac 64 bit support (Cocoa view support also in 32 bit)
- Fixes in Validator
- Some documentation changes
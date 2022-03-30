>/ ... / [Change History](../Index.md)
>
># Version 3.0.1 (2008/03/19)

## Version 3.0.1 (2008/03/19)

- New Interface:
    - [Steinberg::Vst::IMidiMapping](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IMidiMapping.html) : allowing to support MIDI Controllers and Pitchbend
- New Flags/Enums:
    - Add new restart flag: Steinberg::Vst::kMidiCCAssignmentChanged
- Restructuring of the SDK :
    - Move RestartFlags from vstTypes.h to ivsteditcontroller.h
    - Restructured helper classes by adding new files vstbus.cpp and vstparameters.cpp
    - Change the default refcount implementation of Steinberg::FUnknown (IMPLEMENT_REFCOUNT) to use atomic operations
    - Change InitModule/ExitModule to be called from host and not in DllMain (Cubase 4.2 needed)
    - Rename Steinberg::Vst::IUnitData to Steinberg::Vst::IProgramListData and introduce new interface Steinberg::Vst::IUnitData
- Helpers Classes:
    - Add new helper class EditControllerEx1 : extend of EditController with Unit support
    - Add new helper class Steinberg::Vst::SingleComponentEffect for single component effects
- Samples:
    - AGain example has been extended : supports IMidiMapping, [Side-chain](../3.0.0/Multiple+Dynamic+IO.html#what-is-a-side-chain) and Unit
    - Add Visual Studio 2008 solution
- Documentation
    - Rework
    - Add some new FAQs
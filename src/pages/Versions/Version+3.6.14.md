>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.6.14 (2019/11/29)

## Version 3.6.14 (2019/11/29)

- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) 4.9
  - new control: VSTGUI::CListControl in play with VSTGUI::CStringList
  - custom font support: VSTGUI now supports using fonts embedded in its Bundle/Package at Resources/Fonts. Note that this works on Windows only when building with the Windows 10 SDK and it does also only work on Windows 10. There is no such restriction on macOS or Linux.
- cmake:
  - minor refactoring
  - add file SMTG_VST3_SDK.cmake
  - better FindJack support
  - better Cross-compiler support for Linux
- [Samples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - add more checks and 64 bit processing support in HostChecker plug-in
  - add AAX version of "HostChecker Plug-in"
  - add new test in Validator:
    - threaded process, bypass persistence
    - new option to run more tests (optExtensiveTests, "Run extensive tests [may take a long time]")
    - improvement to MidiMappingTest performance
- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - The InterAppAudio Wrapper is deprecated and may be removed in the next SDK update. Please switch to AudioUnit V3 on iOS.
  - AAX Wrapper (VST 3 - AAX Wrapper):
    - add SMPTE support
- Helpers classes:
  - clear programLists, programIndexMap and units in EditControllerEx1 when terminating
- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v2.8.10
  - menu change on Windows
  - add new tests

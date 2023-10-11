>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.6.13 (2019/04/08)

## Version 3.6.13 (2019/04/08)

- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) 4.8
  - new VSTGUI::CSegmentButton selection mode kSingleToggle and styles kHorizontalInverse and kVerticalInverse
- Interfaces changes:
  - new PluginType kInstrumentPiano (instrument for piano sounds)
- cmake:
  - minor refactoring
  - add Visual Studio 2020 support
- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - add some more checks in HostChecker plug-in
  - add some debug output for editorhost
- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - AAX Wrapper ([VST 3 - AAX Wrapper](../What+is+the+VST+3+SDK/Wrappers/AAX+Wrapper.md)):
    - loading of preset should not overwrite the current Bypass state
- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md):
  - support of IPlugInterfaceSupport
  - support of MPE
  - possibility to open the same plug-in editor twice

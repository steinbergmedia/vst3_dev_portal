>/ ... / [Change History](../Index.md)
>
># Version 3.6.13 (2019/04/08)

## Version 3.6.13 (2019/04/08)

- [VSTGUI](/pages/What+is+the+VST+3+SDK/VSTGUI.md) 4.8
    - new VSTGUI::CSegmentButton selection mode kSingleToggle and styles kHorizontalInverse and kVerticalInverse.
- Interfaces changes:
    - new PluginType kInstrumentPiano (instrument for piano sounds)
- cmake:
    - minor refactoring
    - add Visual Studio 2020 support
- [Samples](/pages/What+is+the+VST+3+SDK/Plug-in+Examples.md):
    - add some more checks in HostChecker plug-in
    - add some debug output for editorhost
- [Plug-in Wrappers](/pages/What+is+the+VST+3+SDK/Wrappers/Index.md):
    - AAX Wrapper (VST 3 - AAX Wrapper):
        - loading of preset should not overwrite the current Bypass state
- VST3PluginTestHost: VST 3 Plug-in Test Host
    - support of IPlugInterfaceSupport
    - support of MPE
    - possibility to open 2 times the same plug-in editor
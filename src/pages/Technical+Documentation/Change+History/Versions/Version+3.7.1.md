>/ ... / [Change History](../Index.md)
>
># Version 3.7.1 (2020/11/17)

## Version 3.7.1 (2020/11/17)

- New Flags/Enums:
    - NoteIDUserRange: Reserved note identifier (noteId) range for a plug-in. Guaranteed not used by the host.
- cmake:
    - Rename files with SMTG_ prefix
    - Rename functions with smtg_ prefix
    - Reorganize files
    - Make VSTSDK more Mingw32 compatible
    - Support AUv3 building without team ID
    - Fix path handling in smtg_add_plugin_resource
- [Plug-in Wrappers](/pages/What+is+the+VST+3+SDK/Wrappers/Index.md):
    - AAX Wrapper (AAXWrapper):
        - Add support of offline processing
    - Audio Unit v3 (AUv3) (AUv3Wrapper):
        - Add support of offline processing
        - Fix output bus activation
        - Fix when the component is not loaded from UI-Thread
- Helpers classes:
    - GetPluginFactory() def-file vs. declspec
- [VST3PluginTestHost](/pages/What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.0:
    - New control voltage bus info column
    - New links in help menu
    - New enable MPE Support
    - Dark-Light scheme Support
    - Fix "Valid State Transition" test always fails a 64-bit-only plugin #50
    - Fix automation unit test
- [VST3 Project Generator](/pages/What+is+the+VST+3+SDK/Project+Generator.md) v2020.10:
    - New support of [VSTGUI](/pages/What+is+the+VST+3+SDK/VSTGUI.md)
    - Enable Symbolic link on Windows
    - Add VST3PluginTestHost.exe as Debugging->Command on Windows
    - Improve generate cmake file
    - Fix freeze after having choosing a wrong cmake.exe path
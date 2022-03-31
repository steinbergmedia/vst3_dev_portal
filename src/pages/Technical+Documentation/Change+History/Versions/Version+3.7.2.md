>/ ... / [Change History](../Index.md)
>
># Version 3.7.2 (2021/03/30)

## Version 3.7.2 (2021/03/30)

- [VSTGUI](../../../What+is+the+VST+3+SDK/VSTGUI.md) 4.10
    - minimum requirement C++14.
    - [VSTGUI](https://steinbergmedia.github.io/vst3_doc/vstgui/html/namespace_v_s_t_g_u_i.html) now needs to be initialized and terminated explicitly. See [VSTGUI::init()](https://steinbergmedia.github.io/vst3_doc/vstgui/html/group__new__in__4__10.html)
    - UIDescription files are now written in JSON format and the old XML format is deprecated
    - It's now possible to conditionally remove the XML parser and the expat library from building (set VSTGUI_ENABLE_XML_PARSER to 0)
- Licensing has changed to version 2.1! Please read the new license agreement /pages/VST+3+Licensing/Index.md). (if you have already signed the version 2.0 of the license agreement you do not have to sign it again).
- New Flags/Enums:
    - New predefined 3D speaker arrangement:
        - k220 (L R C Ls Rs Lc Rc Cs Sl Sr Tc Tfl Tfc Tfr Trl Trc Trr Tsl Tsr Bfl Bfc Bfr)
    - Some arrangements renamed:
        - "7.1 Music (Dolby)"=>"7.1"
        - "7.0 Music (Dolby)"=>"7.0"
        - "7.1 Cine (SDDS)"=>"7.1 SDDS"
        - "7.0 Cine (SDDS)"=>"7.0 SDDS"
- cmake:
    - Code styling changed
    - Each library defined which is the minimal requirementfor C++ version (11 for pluginterfaces) by usingtarget_compile_features
    - New flag: SMTG_CXX_STANDARD in order to overwrite thedefault used version of C++ (11)
    - New flag: SMTG_CUSTOM_BINARY_LOCATION: Customize outputlocation for binaries
    - New flag: SMTG_CXX_STANDARD: C++ standard version usedfor plugins: 14, 17, 20
    - New flag: SMTG_ENABLE_ADDRESS_SANITIZER: Enable AddressSanitizer
    - Add check for C11 atomic header
    - Add support for enabling Sanitizer
    - Add new file SMTG_SetDebugExecutable.cmake: allows topreconfigure the debug executable to run 
    - Fix LOCAL_JACK_LIB in SMTG_FindJack.cmake on Windows
    - Fix link plug-in to common location on Windows
    - Fix: Failing unit test with validator results inplug-in resources/snapshots not being copied
- [Plug-in Wrappers](../../../What+is+the+VST+3+SDK/Wrappers/Index.md):
    - AAX Wrapper
        - Fix Export Symbols for AAX on macOS
    - Audio Unit v2
        - Fix AUv2 with Xcode 12
- [Samples](../../../What+is+the+VST+3+SDK/Plug-in+Examples.md):
    - New VST 3 hosting example:
        - [VST3 Inspector app](../../../What+is+the+VST+3+SDK/Index.md): example showing how to parse the available VST3 plugins factories, using VSTGUI.
    - C++14 minimum requirements for validator, audiohost, editorhost, Inspector app
- Helpers classes:
    - New file handling module initialization: public.sdk\source\main\moduleinit.cpp, public.sdk\source\main\moduleinit.h
    - #include <windows.h> instead of #include <Windows.h>
    - Fix incorrect string copy regression in HostAttributeList::getString
    - Fix some Validation tests:  SliceProcessingTest,ValidStateTransitionTest.
    - Fix module_linux.cpp building in C++20 mode
- [VST3PluginTestHost](../../../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.1.0:
    - New context menu entry for instantiated plugin: "Export Presets Parameters as XML" which allows to load automatically VST3 presets and export them as XML files.
- [VST3 Project Generator](../../../What+is+the+VST+3+SDK/Project+Generator.md) v2021.03:
    - This project is now open source on <https://github.com/steinbergmedia/vst3projectgenerator>
    - Universal binary for macOS (Intel/M1)
    - Add another default location to search for cmake on macOS
    - Use cmake for bundle ID setup
    - Make sure keyboard focus navigation is correct
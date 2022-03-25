>/ [VST Home](/Index.md) / [Technical Documentation](../Index.md)
>
># Change History

**On this page:**

[[_TOC_]]

---

All released versions of the VST 3 SDK with changes and dates.

## Version 3.7.4 (2021/12/14)

- Interface changes:
    - Add support of _M_ARM64EC on Windows
    - New defines: SMTG_CPU_ARM_64EC, SMTG_CPP14 and SMTG_CPP17
    - New [VST3 plug-in location](../Locations+Format/Plugin+Locations.md) user local on Windows: %LOCALAPPDATA%/Programs/Common/VST3/
    - Use SMTG_CONSTEXPR where needed
- [VSTGUI](/pages/What+is+the+VST+3+SDK/VSTGUI.md) 4.10.§
    - different fixes
- Licensing has changed to version 2.2.2! Please read the new license agreement [VST 3 Licensing Issues](/pages/VST+3+Licensing/Index.md). (if you have already signed the version 2.0 of the license agreement you do not have to sign it again).
- cmake:
    - Refactoring: rename function/macro by adding target when target   is used: i.e. smtg_run_vst_validator =>   smtg_target_run_vst_validator
    - ⚠️Breaking Change: change smtg_add_vst3_resource to   smtg_target_add_plugin_resources allowing to add multiple     resources in a call
    - ⚠️Breaking Change: change smtg_add_vst3_snapshot to   smtg_target_add_plugin_snapshots allowing to add multiple     resources in a call
    - make Universal Binary on Mac default ON when Xcode12
    - Add support of new VST3 Location on Windows: new option SMTG_PLUGIN_TARGET_USER_PROGRAM_FILES_COMMON
    - Fix some code Signing issue with XCode
- [Plug-in Wrappers](/pages/What+is+the+VST+3+SDK/Wrappers/Index.md):
    - VST2 Wrapper:
        - Fix termination of objects might still need data destroyed in _DeinitModule()
    - Audio Unit:
        - Update AU SDK as external (version 1.1)
        - Fix offline rendering info for AUWrapper
- [Samples](/pages/What+is+the+VST+3+SDK/Plug-in+Examples.md):
    - Add to validator self-tests
    - Add to validator a new function addErrorWarningTextToOutput
- Helpers classes:
    - New file pluginterfaces/base/funknownimpl.h (C++11 required): it provides classes for working with FUnknown.
    - Add Unitests for all hosting helpers classes
    - Show example const_exp (C++17) in plugin factory: public.sdk/source/main/pluginfactory_constexpr.h
    - Add documentation to mpeprocessor classes
- [VST3PluginTestHost](/pages/What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.2.20:
    - Adapted to scan the new VST3 plug-in location on Windows
    - This is the last version supporting 32bits plug-ins on Windows. The next update will support only 64bits plug-ins.
- [VST3 Project Generator](/pages/What+is+the+VST+3+SDK/Project+Generator.md) v2021.12:
    - Add platform Architecture setting (cmake) in project generator on Windows

## Version 3.7.3 (2021/08/10)

- Interface changes:
    - update documentation of IPlugViewContentScaleSupport
- [VSTGUI](/pages/What+is+the+VST+3+SDK/VSTGUI.md) 4.10.1
    - different fixes
- Licensing has changed to version 2.2.1! Please read the new license agreement [VST 3 Licensing Issues](/pages/VST+3+Licensing/Index.md). (if you have already signed the version 2.0 of the license agreement you do not have to sign it again).
- New Flags/Enums:
    - New RestartFlags flag kKeyswitchChanged: informing that Key switches has changed (info, count)
    - New FunctionNameType for Panner: like kPanPosCenterX
- cmake:
    - Fix wrong link path on Windows arm 64
    - Add -Werror=return-type to get the same error on mac as on Windows or Linux
    - Fix undefined variable vst3sdk_SOURCE_DIR when using fetchcontent for the SDK
    - Fix wrong symbol visibility when project created via project generator
- [New Tutorial for advanced techniques](/pages/Tutorials/Advanced+VST+3+techniques.md)
- [Plug-in Wrappers](/pages/What+is+the+VST+3+SDK/Wrappers/Index.md):
    - AAX Wrapper:
        - Refactoring of initModule/DeInitModule
        - GetParameterIndex wrong index when read-only parameters used
    - VST2 Wrapper:
        - Fix issue calling too many InitModule
        - Refactoring of initModule/DeInitModule
    - Audio Unit v3:
        - Support AUv3 in macOS 11
        - Simplify AUv3Wrapper code
        - Fix Logic/GarageBand not showing editor on macOS 11
- Rename folder in zip SDK: VST3_SDK => vst3sdk
- [Samples](/pages/What+is+the+VST+3+SDK/Plug-in+Examples.md):
    - Added checks in HostChecker plug-in:
        - Check IParameterChanges for multiple queues with same ID
        - Check IParameterChanges for multiple points at same position
        - Add restartComponent (kKeyswitchChanged) / restartComponent (kNoteExpressionChanged)  / restartComponent (kParamValuesChanged)
    - Add support of ivstparameterfunctionname in Panner sample
    - New VST 3 plug-ins example:
        - New "AGain Sample Accurate" showing sample accurate parameter changes processing
    - Fix editorHost when launch without arguments
    - Fix crash in VST3Inspector when no VST3 plugins available
    - Fix warnings for mda plug-ins
    - Fix the build with gcc 11
- Helpers classes:
    - New utility files:
        - audiobuffers.h
        - processdataslicer.h
        - rttransfer.h
        - sampleaccurate.h
        - testing.cpp/.h

## Version 3.7.2 (2021/03/30)

- [VSTGUI](/pages/What+is+the+VST+3+SDK/VSTGUI.md) 4.10
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
- [Plug-in Wrappers](/pages/What+is+the+VST+3+SDK/Wrappers/Index.md):
    - AAX Wrapper
        - Fix Export Symbols for AAX on macOS
    - Audio Unit v2
        - Fix AUv2 with Xcode 12
- [Samples](/pages/What+is+the+VST+3+SDK/Plug-in+Examples.md):
    - New VST 3 hosting example:
        - [VST3 Inspector app](/pages/What+is+the+VST+3+SDK/Index.md): example showing how to parse the available VST3 plugins factories, using VSTGUI.
    - C++14 minimum requirements for validator, audiohost, editorhost, Inspector app
- Helpers classes:
    - New file handling module initialization: public.sdk\source\main\moduleinit.cpp, public.sdk\source\main\moduleinit.h
    - #include <windows.h> instead of #include <Windows.h>
    - Fix incorrect string copy regression in HostAttributeList::getString
    - Fix some Validation tests:  SliceProcessingTest,ValidStateTransitionTest.
    - Fix module_linux.cpp building in C++20 mode
- [VST3PluginTestHost](/pages/What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.1.0:
    - New context menu entry for instantiated plugin: "Export Presets Parameters as XML" which allows to load automatically VST3 presets and export them as XML files.
- [VST3 Project Generator](/pages/What+is+the+VST+3+SDK/Project+Generator.md) v2021.03:
    - This project is now open source on <https://github.com/steinbergmedia/vst3projectgenerator>
    - Universal binary for macOS (Intel/M1)
    - Add another default location to search for cmake on macOS
    - Use cmake for bundle ID setup
    - Make sure keyboard focus navigation is correct

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

## Version 3.7.0 (2020/07/29)

- Interface changes:
    - New [IProcessContextRequirements](../Change+History/3.7.0/IProcessContextRequirements.md) (implemented by plug-in).
        - This is a new required interface a plug-in needs to implement when building with VST SDK 3.7 or newer.
    - New [IProgress](../Change+History/3.7.0/IProgress.md) (implemented by host)
    - New [IParameterFunctionName](../Change+History/3.7.0/IParameterFunctionName.md) (implemented by plug-in)
- New Flags/Enums:
    - New kIsHidden flag. With this flag, the parameter should NOT be displayed by the host and cannot be changed from outside the plug-in.
    - New predefined 2D speaker arrangements:
        - k90Cine, k91Cine (L R C Lfe Ls Rs Lc Rc Sl Sr)
        - k100Cine, k101Cine (L R C Lfe Ls Rs Lc Rc Cs Sl Sr)
    - New predefined 3D speaker arrangements:
        - k90_4, k91_4 (L R C Lfe Ls Rs Lc Rc Sl Sr Tfl Tfr Trl Trr)
        - k90_6, k91_6 (L R C Lfe Ls Rs Lc Rc Sl Sr Tfl Tfr Trl Trr Tsl Tsr)
    - New Bus flag: kIsControlVoltage for audio busses
- Documentation:
    - add documentation about VST 3 and MIDI 2.0:
        - [MIDI 2.0 Increased Resolution, compared to MIDI 1.0](../About+MIDI/Index.md)
        - [MIDI 2.0 Per-Note Controllers](../About+MIDI/Index.md)
- cmake:
    - New cmake files
    - Fix on Windows creation of VST3 folder using powershell with admin rights
- [Samples](/pages/What+is+the+VST+3+SDK/Plug-in+Examples.md):
    - New VST 3 plug-ins examples:
        - SyncDelay using [Steinberg::Vst::IProcessContextRequirements](../Change+History/3.7.0/IProcessContextRequirements.md)
        - Panner using PlugType::kSpatialFx as SubCategory, it shows how to build a Panner plug-in Mono to Stereo
    - Added checks in HostChecker plug-in:
        - support of kIsHidden flag
        - support of [IProgress](../Change+History/3.7.0/IProgress.md) (implemented by host)
        - support of [IParameterFunctionName](../Change+History/3.7.0/IParameterFunctionName.md)
        - check if Silent flag for Main and [Side-chain](/pages/FAQ/Index.md) **<- Link to be completed later** Inputs are used
- [Plug-in Wrappers](/pages/What+is+the+VST+3+SDK/Wrappers/Index.md):
    - Fix for AAX/VST2 BaseWrapper setChunk attribute Vst::StateType::kProject was not set for component.
- Helpers classes:
    - Added functions to load FXB/FXP states and to write FXB states for compatibility with VST2.x (see public.sdk/source/vst/utility/vst2persistence.h)
    - Fix compilation with MinGW-w64 GCC compiler
    - New helper: openurl.h allowing to open a URL in the default associated application
- [VST3PluginTestHost](/pages/What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v2.9.0: VST 3 Plug-in Test Host
    - Added support of:
        - IProgress
        - IProcessContextRequirements
        - IParameterFunctionName
    - Fix crashes when closing 2 or more instances of GUI of same plug-in in particular order
    - Fix support of SingleComponentEffect plug-ins that implement IMidiMapping
- [VST3 Project Generator](/pages/What+is+the+VST+3+SDK/Project+Generator.md) v1.0.0:
    - New easy to use VST 3 Project Generator

## Version 3.6.14 (2019/11/29)

- [VSTGUI](/pages/What+is+the+VST+3+SDK/VSTGUI.md) 4.9
    - new control: VSTGUI::CListControl in play with VSTGUI::CStringList
    - custom font support: VSTGUI now supports using fonts embedded in its Bundle/Package at Resources/Fonts. Note that this works on Windows only when building with the Windows 10 SDK and it does also only work on Windows 10. There is no such restriction on macOS or Linux.
- cmake:
    - minor refactoring
    - add file SMTG_VST3_SDK.cmake
    - better FindJack support
    - better Cross-compiler support for Linux
- [Samples](/pages/What+is+the+VST+3+SDK/Plug-in+Examples.md):
    - add more checks and 64 bit processing support in HostChecker plug-in
    - add AAX version of "HostChecker Plug-in"
    - add new test in Validator:
        - threaded process, bypass persistence
        - new option to run more tests (optExtensiveTests, "Run extensive tests [may take a long time]")
        - improvement to MidiMappingTest performance
- [Plug-in Wrappers](/pages/What+is+the+VST+3+SDK/Wrappers/Index.md):
    - The InterAppAudio Wrapper is deprecated and may be removed in the next SDK update. Please switch to AudioUnit V3 on iOS.
    - AAX Wrapper (VST 3 - AAX Wrapper):
        - add SMPTE support
- Helpers classes:
    - clear programLists, programIndexMap and units in EditControllerEx1 when terminating
- [VST3PluginTestHost](/pages/What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v2.8.10: VST 3 Plug-in Test Host
    - menu change on Windows
    - add new tests

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

## Version 3.6.12 (2018/12/03)

- [VSTGUI](/pages/What+is+the+VST+3+SDK/VSTGUI.md) 4.7
    - redesigned drag and drop (drags with bitmaps are now supported on Windows)
    - standalone library support for Windows 7
    - new ImageStitcher tool
    - the GDI+ draw backend was removed, the Direct2D backend is the replacement
    - fix crash with splash screen
    - fix compilation for VSTGUI Tools on win32
    - clean up
- Interfaces changes:
    - New LegacyMIDICCOutEvent (plug-in): allow a plug-in to generate MIDI CC as output event.
    - New IMidiLearn (plug-in): allow a plug-in to get the currently live playing MIDI CC to implement custom MIDI learning.
    - New IPlugInterfaceSupport (host): allow a plug-in to ask the host if a given plug-in interface is supported/used by the host. 
    - New IVst3WrapperMPESupport (wrapper): allow a plug-in to setup MPE support in wrappers.
- cmake:
    - minor refactoring (like renaming WIN to SMTG_WIN)
    - fix WIN_ARCHITECTURE_NAME for Windows 32bits
    - fix SMTG_PACKAGE_ICON_PATH selection
    - split WIN_PDB into WIN_PDB32 and WIN_PDB64
- [Samples](/pages/What+is+the+VST+3+SDK/Plug-in+Examples.md):
    - New LegacyMIDICCOut VST3 plug-in showing the use of LegacyMIDICCOutEvent
    - Add IMidiLearn support for NoteExpressionSynth
    - Add Audio Unit v3 NoteExpressionSynth example with MPE support
- [Plug-in Wrappers](/pages/What+is+the+VST+3+SDK/Wrappers/Index.md):
    - Audio Unit v3 (AUv3) Wrapper (VST 3 - Audio Unit v3 Wrapper):
        - out of the box MPE support. As MPE is a limited subset of the Note Expression feature, the three expressions are simply mapped to the note expressions returned via the [INoteExpressionPhysicalUIMapping](../Change+History/3.6.11/INoteExpressionPhysicalUIMapping.md) interface.
        - note that you must have certificates to sign on macOS/iOS for AUv3
        - complete folder restructuring for easy adaption
    - AAX Wrapper ([VST 3 - AAX Wrapper](/pages/What+is+the+VST+3+SDK/Wrappers/AAX+Wrapper.md) **<- Link?**):
        - fix automation update after loading a preset
    - VST2 Wrapper:
    - fix double release of editor
- Helpers classes:
    - New file with some helpers for event: vsteventshelper.h

## Version 3.6.11 (2018/10/22)

- [VSTGUI](/pages/What+is+the+VST+3+SDK/VSTGUI.md) 4.7
    - update to VSTGUI 4.7
    - move from GTK++ to XCB for Linux support
    - redesigned drag'n drop
    - drags with bitmaps are now supported on Windows
    - standalone library support for Windows 7
    - new ImageStitcher tool
    - the GDI+ draw backend was removed, the Direct2D backend is the replacement
- New icon for [VST3]() **<- Link?** bundles: VST_Logo_Steinberg.ico and VST_Logo_Steinberg.icns (located in VST_SDK/VST3_SDK/doc/artwork folder)
- Interface changes:
    - VST2 interface not available anymore!
    - New [Steinberg::Vst::INoteExpressionPhysicalUIMapping](../Change+History/3.6.11/INoteExpressionPhysicalUIMapping.md) (plug-in): allowing the host to retrieve the preferred physical mapping associated to note expression supported by the plug-in.
- cmake:
    - further improvement for users projects
- [Plug-in Wrappers](/pages/What+is+the+VST+3+SDK/Wrappers/Index.md):
    - AAX Wrapper (VST 3 - AAX Wrapper):
        - fix UI resizing
        - fix issue for default blocksize
    - VST2 Wrapper:
        - fix for instruments which were not visible as instrument
- Helpers classes:
    -  make virtual some functions of class parameter (set/getUnitID, getInfo, set/getPrecision)

## Version 3.6.10 (2018/06/11)

- New definition of plug-in format for Windows including icon support ([VST3]() **<- Link?** Bundle: [VST 3 Locations / Format](../Locations+Format/Plugin+Locations.md))
- Support of [Snapshots]() **<- Link?** inside the [VST3]() **<- Link?** Bundle
- cmake:
    - adapt cmake files for better integration of users projects
    - fix support Universal Binary for AudioUnit
- Plug-in wrappers:
    - refactoring AAX/VST2 Wrappers
    - AAX Wrapper (VST 3 - AAX Wrapper):
        - fix Bypass behaviour
        - fix initial signal latency
        - fix indexing of parameter, conflicting with VST2
- Helpers classes:
    - fix activateBus issue in class SingleComponentEffect
    - fix Ring Buffer class issue

## Version 3.6.9 (2018/03/01)

- [VSTGUI](/pages/What+is+the+VST+3+SDK/VSTGUI.md) 4.6
    - update to VSTGUI 4.6
    - including a new UI element: KeyboardView supporting Note Expression
- Interfaces changes:
    - rename some defines:
        - PLATFORM_64 => SMTG_PLATFORM_64
        - WINDOWS => SMTG_OS_WINDOWS
        - MAC => SMTG_OS_MACOS
        - LINUX => SMTG_OS_LINUX
    - extract Speaker Arrangement from vsttypes.h to vstspeaker.h
    - new kNoParamId constant for uninitialized parameter id
- cmake:
    - reorganization of cmake files
- Samples:
    - fix Validator State test
    - NoteExpressionSynth uses the new KeyboardView
    - New HelloWorld VST3 plug-ins (template): [Creating a plug-in from the Helloworld template](/pages/Tutorials/Creating+a+plug-in+from+the+Helloworld+template.md)
- Plug-in wrappers:
    - VST 3 - Audio Unit Wrapper : fix and adaptation for newer XCode versions
    - Audio Unit v3 (AUv3) Wrapper (VST 3 - Audio Unit v3 Wrapper): some fixes, add cmake
    - AAX Wrapper (VST 3 - AAX Wrapper): add bypass and VU parameter support
    - interappaudio: improvements, fixes, add cmake
- Helpers classes:
    - New Ring Buffer class (ringbuffer.h)

## Version 3.6.8 (2017/11/08)
- Changes in the Licensing Agreement! Please check it ([VST 3 Licensing Issues](/pages/VST+3+Licensing/Index.md) **<- Link?**).
- [New Steinberg VST usage guidelines](/pages/VST+3+Licensing/Usage+guidelines.md) PDF
- This SDK version required compilers supporting C++11. It requires on Windows Visual Studio 2015 minimum!
- Linux support in Beta
- Interfaces changes:
    - New Steinberg::Vst::IComponentHandlerBusActivation (host): allowing a plug-in to request the host to activate or deactivate a specific bus (useful for instrument with multiple outputs)
- New Flags/Enums:
    - New predefined Ambisonic Speaker Arrangements: 1st, 2cd and 3rd order (ACN ordering and SN3D normalization): kAmbi1stOrderACN, kAmbi2cdOrderACN, kAmbi3rdOrderACN with their associated speakers: kSpeakerACN0...kSpeakerACN15
    - New predefined 3D speaker arrangements: k70_4, k71_4
- Samples:
    - New VST 3 [Host implementation examples]() **<- Link?**:
    - Folder reorganization: hosting examples are in a separate folder: public.sdk/samples/vst-hosting
    - New AudioHost (AudioHost - cross-platform standalone) showing how integrate a [VST3]() **<- Link?** plug-in in a Jack world! This required Jack Audio (<http://www.jackaudio.org>), only tested under Linux but should work on Windows 32bits and Mac.
- Plug-in wrappers:
    - New Audio Unit v3 (AUv3) Wrapper (VST 3 - Audio Unit v3 Wrapper)
    - New AAX wrapper (VST 3 - AAX Wrapper): Note that in order to use this AAX wrapper for your plug-in, you have to download the AAX SDK (contact AVID), tested with AAX SDK Version 2.3.0.

## Version 3.6.7 (2017/03/03)
- Preview Linux support (check <https://sdk.steinberg.net for discussion>): [Setup Linux for building VST 3 Plug-ins](/pages/Getting+Started/How+to+setup+my+system.md)
- Licensing has changed! Please read the new [VST 3 Licensing Issues](/pages/VST+3+Licensing/Index.md).
- Use cmake as project generator: [How to use cmake for Building VST 3 Plug-ins](/pages/Tutorials/Using+cmake+for+building+plug-ins.md)
- This is the last version of the SDK supporting C++98, future versions will used C++11.
- Samples:
    - New VST 3 host implementation example:
        - New HostEditor application: Cross-platform (Win/macOS/Linux) standalone which opens the UI of a [VST3]() **<- Link?** plug-in
    - Updated validator application to support Linux
    - AGain plug-in updated:
        - it uses VSTGUI 4 instead of VSTGUI 3
        - it supports 64bit processing (template based)
    - All [VSTGUI](/pages/What+is+the+VST+3+SDK/VSTGUI.md) 4 based samples support HiDPI on Windows now
    - Fix Program Change persistence in mda plug-ins example
    - Removed Xcode and Visual Studio projects, please use cmake now!
    - On Windows, we link [VST3]() **<- Link?** plug-ins with the MultiThreaded DLL runtime libraries (it will use Universal C Runtime Libraries, for older Windows version than Win 8.1 you may have to install these libraries from: <https://support.microsoft.com/en-us/kb/2999226>)
- VSTGUI 3.x is not supported anymore (removed from the SDK), but you can still download it from github: <https://github.com/steinbergmedia/vstgui>
- Plug-in wrappers:
    - VST 3 - Audio Unit Wrapper :
        - fix AU Wrapper MIDI Program Change issue (data1 instead of data2)
    - VST 3 - VST 2.x Wrapper :
        - fix resize issue on macOS
        - fix mapping between [VST3]() **<- Link?** ParamID and VST2 paramID when bypass parameter is used

## Version 3.6.6 (2016/06/17)

- Interfaces changes:
    - New Steinberg::IPlugViewContentScaleSupport: Plug-in view content scale support
- New Flags/Enums:
    - New RestartFlags: kRoutingInfoChanged informing the host that the Routing Info (IComponent) has changed
- Samples:
    - New VST 3 plug-ins examples:
        - New **VST 3 Plug-in** Program Change showing how handling its own Program List is working
    - Remove Visual Projects version 8 and 9
- Plug-in wrappers:
    - VST 3 - Audio Unit Wrapper :
        - update to last Audio Core update
    - VST 3 - VST 2.x Wrapper :
        - add support of version (VST3 -> VST2)
- Helpers classes:
    - add support for bypass including delay compensation (vstbypassprocessor.h)
    - add helpers for events/parameters iterator (vstaudioprocessoralgo.h)
    - add helpers for SpeakerArr:
        - Speaker getSpeaker (const SpeakerArrangement& arr, int32 index)
        - bool isSubsetOf (const SpeakerArrangement& arrSubSet, const SpeakerArrangement& arr)
- VSTGUI 4.3
    - update to VSTGUI 4.3.1 (available here too: <http://sourceforge.net/projects/vstgui/files/vstgui/VSTGUI%204.3/)>
    - the [VSTGUI](/pages/What+is+the+VST+3+SDK/VSTGUI.md) repository was moved to github: <https://github.com/steinbergmedia/vstgui>
    - Please use github if you want to contribute to VSTGUI.
- VST3PluginTestHost: VST 3 Plug-in Test Host
    - fix support of SingleComponent
- new Developer Forum:
    - finally we get our VST forum at start, please check <https://sdk.steinberg.net> and use it as new communication platform, the VST mailing list will be kept as archive mailing list.

## Version 3.6.5 (2015/08/28)

- Interfaces changes:
    - New [Steinberg::Vst::ChannelContext::IInfoListener](../Change+History/3.6.5/IInfoListener.md) interface: informing the plug-in about the channel in which it is instanciated (name, color...)
    - New Steinberg::Vst::IPrefetchableSupport interface: allowing a plug-in to inform the host that it does not support prefetch/ASIO Guard (could be dynamically)
    - New Steinberg::Vst::IUnitHandler2 interface: allowing a plug-in to inform the host that an assignment Unit-Bus defined by IUnitInfo::getUnitByBus has changed
    - New Steinberg::Vst::IAutomationState interface: informing the plug-in about its current automation state
use "#pragma once" instead of "#ifndef"
- Samples:
    - New VST 3 [Plug-ins examples]() **<- Link?**:
        - New **VST 3 Plug-in** ChannelContext showing how Steinberg::Vst::ChannelContext::IInfoListener interface is working
        - New **VST 3 Plug-in** PrefetchableSupport showing how Steinberg::Vst::IPrefetchableSupport interface is working
    - "VST3 Host Checker" plug-in updated with new checks
- Plug-in wrappers:
    - [VST 3 - Audio Unit Wrapper]() **<- Link?**:
        - support MIDI output
        - fix crash with namespace conflict with Mac OS X 10.10
        - add PresetAttributes::StateType support in AUWrapper::restoreState
- New Flags/Enums:
    - New predefined 3D Speaker Arrangements: k91Atmos
- VST3PluginTestHost: VST 3 Plug-in Test Host
    - add some new unit tests: Bypass parameter support is mandatory for FX Plug-in (not Instrument)!

## Version 3.6.0 (2013/11/22)

- Interfaces Changes:
    - Preset meta information via Steinberg::Vst::IStreamAttributes
    - New Event Types: Steinberg::Vst::ChordEvent, Steinberg::Vst::ScaleEvent
- Plug-in Wrappers:
    - [3.6.0] iOS Inter-App Audio support
    - VST 3 - VST 2.x Wrapper :
        - fix when changing from host between single and double precision processing
        - fix setProgram and processMidiEvent for kProgramChangeStatus where the wrong idx was used for programChange Parameter
    - VST 3 - Audio Unit Wrapper :
        - adopt to new AUPlugIn API in Mac OS X 10.7
        - virtual destructor for NSDataIBStream
- New Flags/Enums:
    - New predefined 3D Speaker Arrangements: k81MPEG3D, k222
- Helpers Classes:
    - fix compilation for UNICODE_OFF enable
- Samples:
    - New VST 3 HostChecker Plug-in
- VSTGUI 4.2
    - Update to the final 4.2 release including iOS support
- VST3PluginTestHost: VST 3 Plug-in Test Host
    - New feature: Overwrite Plug-in Name in [VST3]() **<- Link?** Presets
- Licensing has changed! Please read the new license agreement [VST 3 Licensing Issues](/pages/VST+3+Licensing/Index.md).
- Xcode 5 note: To successfully build the examples for Mac OS X you need to change the SDKROOT variable in base/mac/config/settings/sdk_deployment_10_6.xcconfig to macosx10.8.

## Version 3.5.2 (2012/09/25)

- Interfaces Changes:
    - Note Expression supports a new event type: NoteExpressionTextEvent
- Samples:
    - Fix Visual Studio 2010 projects (filters added)
    - Adaptation for XCode4 (The again sample project uses [VSTGUI](/pages/What+is+the+VST+3+SDK/VSTGUI.md) **<- Link?** 3.6 which needs the 10.6 SDK for the 32 bit build, in later Xcode tools this SDK is not available. If you use VSTGUI 3.6 you need to use a Xcode version which has the 10.6 SDK or earlier included.)
- Plug-in Wrappers:
    - VST 3 - Audio Unit Wrapper :
        - fix noteOn and noteOff offset
        - fix RestoreState with IO bus changes
        - MIDI PolyPressure support added
        - non-automatable parameters have now FlagAudioUnitParameterFlag_NonRealTime AU flag
        - fix under Logic where sample rate was not set for mono track
    - VST 3 - VST 2.x Wrapper :
        - fix getMidiProgramCategory
- New Flags/Enums:
    - New predefined Speaker Arrangements: 9.0/9.1/10.0/10.1/11.0/11.1/13.0/13.1 based on Auro 3D definition (<www.auro-technologies.com>).
- Helpers Classes:
    - New in Base:
        - class Steinberg::Region
        - class Steinberg::IStreamWrapper
        - Helper Steinberg::HexBinary : HexBinary encoding and decoding
- Some documentation changes
    - [Steinberg::Vst::IParameterFinder](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IParameterFinder.html) : To enable important functionalities (like AI Knob) a recommendation to implement this interface was added.
    - The [VST3]() **<- Link?** Plug-in locations priority has been changed: Application level should be scanned from host after Global level.
- Licensing change for example source code files

## Version 3.5.1 (2011/11/11)

- Interfaces Changes:
    - due to a missing calling convention in IContextMenu interfaces, we had to generate new iids for this set of interfaces, [Steinberg]() **<- Link?** hosts will be updated (from 6.0.5) in order to support correctly this interface set. The old interfaces when already used will continue to be supported in [Steinberg]() **<- Link?** hosts. Sorry for this issue...
- Helpers Classes:
    - EditController is now one of the base classes of SingleComponentEffect
        - If you have used the SingleComponentEffect before, make sure that you must exclude vsteditcontroller.cpp now if it was in your project
    - EditControllerEx1 has a new function: setProgramName
    - ProgramList has a new function: setProgramName
- Samples:
    - Add Visual Studio 2010 projects
    - Remove Visual Studio 2003 projects
    - Fix AGain Single Component Effect
- VSTGUI 4.0
    - Update to the final 4.0 release
- Plug-in Wrappers:
    - VST 3 - VST 2.x Wrapper :
        - fix an issue with destroying the editor
    - VST 3 - Audio Unit Wrapper :
        - fix initial editor size issue
        - optimization for GetParameterInfo
- VST3PluginTestHost: VST 3 Plug-in Test Host
    - New feature: Convert [VST3]() **<- Link?** Preset to VST2 preset (fxp or fxb)

## Version 3.5.0 (2011/02/04)

- New Interfaces:
    - Steinberg::Vst::INoteExpressionController : [[3.5.0] Note Expression](../Change+History/3.5.0/INoteExpressionController.md) Support.
    - Steinberg::Vst::IKeyswitchController : [[3.5.0] Key Switch Support](../Change+History/3.5.0/IKeyswitchController.md) (used for building VST Expression Map in Cubase 6 for example).
    - Steinberg::Vst::IXmlRepresentationController : [[3.5.0] Remote Representation](../Change+History/3.5.0/IXmlRepresentationController.md) of Parameters Support (allows to define different parameter mappings for different remotes device).
    - Steinberg::Vst::IEditControllerHostEditing : Parameter editing from host/remote control (better support of linked parameters when editing from remote control)
    - Steinberg::Vst::IComponentHandler3 / Steinberg::Vst::IContextMenu / Steinberg::Vst::IContextMenuTarget : [[3.5.0] Context Menu Support](../Change+History/3.5.0/IComponentHandler3.md) **<- Link?** (allows the Plug-in to create a context menu for a given parameter, partially filled by the host).
- New Flags/Enums:
    - Add new restart flag: Steinberg::Vst::kIoTitlesChanged : informing the host about titles changes of busses.
- Helpers Classes:
    - New Steinberg::Vst::XmlRepresentationHelper : helper for constructing a remote representation (xml based). See [[3.5.0] Remote Representation of Parameters Support](../Change+History/3.5.0/IXmlRepresentationController.md).
    - Steinberg::Vst::EditControllerEx1 : support of ProgramPitchNames added.
- Samples:
    - New VST 3 instrument examples:
        - Instrument "Note Expression Synth" supporting Note Expression Events
        - Effect showing support of pitchnames (ProgramPitchNames)
- Validator:
    - More command line options
    - Possibility to add custom tests by the Plug-in
- VSTGUI 4.0
    - preview version of VSTGUI with optimal VST 3 support
- Plug-in Wrappers:
    - VST 3 - Audio Unit Wrapper fixes and support of Program changes
- Some documentation changes

## Version 3.1.0 (2010/06/25)

- Restructuring of the SDK :
    - new [Base Module]() **<- Link?** (many useful classes, such as templates and containers)
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
    - New Plug-in Types used for subCategories : PlugType::kMono, PlugType::kStereo, PlugType::kSurround ([FAQ]() **<- Link?**)
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

## Version 3.0.2 (2009/01/15)

- New Interface:
    - [Steinberg::Vst::IParameterFinder](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IParameterFinder.html) : Extension for [IPlugView](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugView.html) to find view parameters (lookup value under mouse support)
- Samples:
    - Adaptation of AGain example for support of interface IParameterFinder
- Some documentation changes

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
    - Rename Steinberg::Vst::IUnitData to Steinberg::Vst::IProgramListData and introduce new interface [Steinberg::Vst::IUnitData]() **<- Link?**
- Helpers Classes:
    - Add new helper class EditControllerEx1 : extend of EditController with Unit support
    - Add new helper class Steinberg::Vst::SingleComponentEffect for single component effects
- Samples:
    - AGain example has been extended : supports IMidiMapping, Side-chain and Unit
    - Add Visual Studio 2008 solution
- Documentation
    - Rework
    - Add some new FAQs

## Version 3.0.0 (2008/01/17)
- Public Release of VST SDK 3.0
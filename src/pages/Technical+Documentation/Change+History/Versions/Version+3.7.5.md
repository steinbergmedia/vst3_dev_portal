>/ ... / [Change History](../Index.md)
>
># Version 3.7.5 (2022/05/16)

## Version 3.7.5 (2022/05/16)

- Interface changes:
  - New [moduleinfo.json](../../VST+Module+Architecture/ModuleInfo-JSON.md) file: The moduleinfo.json describes the contents of the plug-in in a JSON5 compatible format. It contains the factory info (see PFactoryInfo), the contained classes (see PClassInfo), the included snapshots and a list of compatibility of the included classes. This compatibility list allows, for example, that a VST 3 plug-in could replace a given VST 2 plug-in.
  - New interface *IPluginCompatibility* in *pluginterfaces/base/iplugincompatibility.h* to be used when a moduleinfo.json file cannot be used.
  - Fix issue building with Visual Studio 2022 (https://github.com/steinbergmedia/vst3sdk/issues/90)
  - Fix warnings for Windows ARM64EC target
  - Fix constexpr issue by using SMTG_CONSTEXPR
- [VSTGUI](../../../What+is+the+VST+3+SDK/VSTGUI.md) 4.11
  - Using DirectComposition on Windows now with support for CLayeredViewContainer
  - Removed 32-bit Carbon support
  - Reworked Event handling
  - different fixes
- New Flags/Enums:
  - New predefined 3D speaker arrangement:
    - **k50_5_3** => L R C Ls Rs Tfl Tfc Tfr Trl Trr Bfl Bfc Bfr
    - **k51_5_3** => L R C LFE Ls Rs Tfl Tfc Tfr Trl Trr Bfl Bfc Bfr
    - ITU 4+5+1 Sound System E
      - **k50_4_1** => L R C Ls Rs Tfl Tfr Trl Trr Bfc
      - **k51_4_1** => L R C LFE Ls Rs Tfl Tfr Trl Trr Bfc
    - ITU 3+7+0 Sound System F
      - **k70_3** => L R C Ls Rs Sl Sr Tsl Tsr Trc
      - **k72_3** => L R C LFE Ls Rs Sl Sr Tsl Tsr Trc LFE2
- Documentation
  - New tutorial explaining [How to use the silence flags](../../../Tutorials/how+to+use+the+silence+flags.md).
  - Move VST3 documentation to md files.
- cmake
  - Minimum cmake version is now 3.19
  - New function *smtg_target_setup_as_vst3_example*
  - Change *smtg_target_set_bundle* for mac
  - New option: **SMTG_CREATE_MODULE_INFO**: Create the moduleinfo.json file (default ON)
  - use VERSION and DESCRIPTION wih project() for generating automatically with cmake version file.
  - Fix https://github.com/steinbergmedia/vst3sdk/pull/91
- [Plug-in Wrappers](../../../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - Audio Unit:
    - Fix AUv3 validation issue (https://github.com/steinbergmedia/vst3_public_sdk/issues/39)
- [Samples](../../../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - New VST 3 plug-ins example:
    - New *multiple_programchanges* showing support of multiple program change parameters.
  - Add new *Processing Load* simulation parameter in **HostChecker** which allows to create a CPU load.
  - Refactoring the examples cmake for using the new versioning handling and *smtg_target_setup_as_vst3_example*
- [Validator](../../../What+is+the+VST+3+SDK/Index.md#validator-command-line):
  - Add test for *IPluginCompatibility* interface
- Helpers classes:
  - New file in public.sdk/samples/vst-utilities for moduleinfo support.
  - New files in public.sdk/source/vst/moduleinfo for creating and parsing moduleinfo.
  - Fix https://github.com/steinbergmedia/vst3_public_sdk/issues/37
- [VST3PluginTestHost](../../../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.3.0:
  - The 32bits version of plugintesthost is not availble anymore
- [VST3 Project Generator](../../../What+is+the+VST+3+SDK/Project+Generator.md) v2022.05:
  - Adapt VST3 Inspector for Compatibility json file support

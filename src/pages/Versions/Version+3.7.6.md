>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.7.6(2022/08/??)

## Version 3.7.6 (2022/08/??)

- Interface changes:
  - new [architecture folder for Windows Arm64EC and Arm64 Classic](../Technical+Documentation/Locations+Format/Plugin+Format.html#for-the-windows-platform)
  
- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) 4.??
  
- New Flags/Enums:
  - Fix ITU 3+7+0 Sound System F
    - **k70_3** => L R C Ls Rs Sl Sr Tfl Tfr Trc
    - **k72_3** => L R C LFE Ls Rs Sl Sr Tfl Tfr Trc LFE2
- Documentation
  - new tutorial: [Guideline for replacing a VST2 Plug-in by a VST3 Plug-in](../Tutorials/Guideline+for+VST3+replacing+VST2.md)
- cmake
  - New file *SMTG_AddVST3AuV2.cmake*:
    - Allow adding AUv2 target to a VST 3 plug-in
    - Review AU Objective-C Namespace handling
  - Add check if **PROJECT_VERSION** is set in *project()*, if not then FATAL_ERROR.
  - Display error text when Spaces in Xcode path which is not supported by cmake.
  - New function *smtg_check_language_cxx* in *SMTG_DetectPlatform.cmake* allows checking if C++ compiler is available.

- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - Audio Unit:
    - Rework AUWrapper Objective-C code

- [Samples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - Add more structured Units and parameters to Hostchecker plug-in.

- Helpers classes:
  - Refactoring by using IPtr in *public.sdk/source/vst/vsteditcontroller.h* and *public.sdk/source/common/pluginview.h*

- [VST3 Project Generator](../What+is+the+VST+3+SDK/Project+Generator.md) v2022.05:
  - Fix: Prevent crash when PATH contains empty substring [PR#3](https://github.com/steinbergmedia/vst3projectgenerator/pull/3)

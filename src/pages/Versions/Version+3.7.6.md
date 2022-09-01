>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.7.6(2022/09/05)

## Version 3.7.6 (2022/09/05)

### General change:

The integer types used throughout the SDK are now based on the standard types defined in ```<cstdint>``` and the UTF-16 character type is now char16_t from c++11.
This is not an ABI change, all types have the same size as before, and old compiled plug-ins will still load without any issue in all hosts on all supported systems.
But implementations may have to be adopted especially on Windows where the tchar/char16 type was directly used for Windows API's.
There are simple casting functions in pluginterfaces/base/fstrdefs.h (see wscast) for easy adoption.

- Interface changes:
  - new [architecture folder for Windows Arm64EC and Arm64 Classic](../Technical+Documentation/Locations+Format/Plugin+Format.html#for-the-windows-platform)
  
- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) Bugfix update [4.11.1](https://github.com/steinbergmedia/vstgui/releases/tag/vstgui4_11_1)
  
- New Flags/Enums:
  - Fix ITU 3+7+0 Sound System F
    - **k70_3** => L R C Ls Rs Sl Sr Tfl Tfr Trc
    - **k72_3** => L R C LFE Ls Rs Sl Sr Tfl Tfr Trc LFE2
- Documentation
  - new tutorial: [Guideline for replacing a VST2 Plug-in by a VST3 Plug-in](../Tutorials/Guideline+for+VST3+replacing+VST2.md)
- cmake
  - New file *SMTG_AddVST3AuV2.cmake*:
    - Add AUv2 target for a VST 3 plug-in
    - Reworked AU Objective-C Namespace handling
  - Add check if **PROJECT_VERSION** is set in *project()*, if not then FATAL_ERROR.
  - Display error text when Spaces in Xcode path which is not supported by cmake.
  - New function *smtg_check_language_cxx* in *SMTG_DetectPlatform.cmake* allows checking if C++ compiler is available.

- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - Audio Unit:
  	- Simplify the creation of an AUv2 wrapped plug-in by a simple cmake function (see smtg_target_add_auv2)
    - Reworked AUWrapper Objective-C code

- [Samples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - Add more structured Units and parameters to Hostchecker plug-in.

- [Validator](../What+is+the+VST+3+SDK/Index.md#validator-command-line):
  - Fix validator output on Windows, cout was not flushed in case of crash

- Helpers classes:
  - Refactoring by using IPtr in *public.sdk/source/vst/vsteditcontroller.h* and *public.sdk/source/common/pluginview.h*

- [VST3 Project Generator](../What+is+the+VST+3+SDK/Project+Generator.md) v2022.05:
  - Fix: Prevent crash when PATH contains empty substring [PR#3](https://github.com/steinbergmedia/vst3projectgenerator/pull/3)

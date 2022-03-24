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
    - New VST3 plug-in location user local on Windows: %LOCALAPPDATA%/Programs/Common/VST3/
    - Use SMTG_CONSTEXPR where needed
- VSTGUI 4.10.§
    - different fixes
- Licensing has changed to version 2.2.2! Please read the new license agreement VST 3 Licensing Issues. (if you have already signed the version 2.0 of the license agreement you do not have to sign it again).
- cmake:
    - Refactoring: rename function/macro by adding target when target   is used: i.e. smtg_run_vst_validator =>   smtg_target_run_vst_validator
    - ⚠️Breaking Change: change smtg_add_vst3_resource to   smtg_target_add_plugin_resources allowing to add multiple     resources in a call
    - ⚠️Breaking Change: change smtg_add_vst3_snapshot to   smtg_target_add_plugin_snapshots allowing to add multiple     resources in a call
    - make Universal Binary on Mac default ON when Xcode12
    - Add support of new VST3 Location on Windows: new option SMTG_PLUGIN_TARGET_USER_PROGRAM_FILES_COMMON
    - Fix some code Signing issue with XCode
- Plug-in Wrappers:
    - VST2 Wrapper:
        - Fix termination of objects might still need data destroyed in _DeinitModule()
    - Audio Unit:
        - Update AU SDK as external (version 1.1)
        - Fix offline rendering info for AUWrapper
- Samples:
    - Add to validator self-tests
    - Add to validator a new function addErrorWarningTextToOutput
- Helpers classes:
    - New file pluginterfaces/base/funknownimpl.h (C++11 required): it provides classes for working with FUnknown.
    - Add Unitests for all hosting helpers classes
    - Show example const_exp (C++17) in plugin factory: public.sdk/source/main/pluginfactory_constexpr.h
    - Add documentation to mpeprocessor classes
- VST3PluginTestHost v3.2.20:
    - Adapted to scan the new VST3 plug-in location on Windows
    - This is the last version supporting 32bits plug-ins on Windows. The next update will support only 64bits plug-ins.
- VST3 Project Generator v2021.12:
    - Add platform Architecture setting (cmake) in project generator on Windows
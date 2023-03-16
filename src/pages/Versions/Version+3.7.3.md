>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.7.3 (2021/08/10)

## Version 3.7.3 (2021/08/10)

- Interface changes:
  - update documentation of IPlugViewContentScaleSupport
- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) 4.10.1
  - different fixes
- Licensing has changed to version 2.2.1! Please read the new license agreement [VST 3 Licensing Issues](../VST+3+Licensing/Index.md). (if you have already signed the version 2.0 of the license agreement you do not have to sign it again).
- New Flags/Enums:
  - New RestartFlags flag kKeyswitchChanged: informing that Key switches has changed (info, count)
  - New FunctionNameType for Panner: like kPanPosCenterX
- cmake:
  - Fix wrong link path on Windows arm 64
  - Add -Werror=return-type to get the same error on mac as on Windows or Linux
  - Fix undefined variable vst3sdk_SOURCE_DIR when using fetchcontent for the SDK
  - Fix wrong symbol visibility when project created via project generator
- [New Tutorial for advanced techniques](../Tutorials/Advanced+VST+3+techniques.md)
- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - AAX Wrapper:
    - Refactoring of initModule/DeInitModule
    - GetParameterIndex wrong index when read-only parameters used
  - VST 2 Wrapper:
    - Fix issue calling too many InitModule
    - Refactoring of initModule/DeInitModule
  - Audio Unit v3:
    - Support AUv3 in macOS 11
    - Simplify AUv3Wrapper code
    - Fix Logic/GarageBand not showing editor on macOS 11
- Rename folder in zip SDK: VST3_SDK => vst3sdk
- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - Added checks in HostChecker plug-in:
    - Check IParameterChanges for multiple queues with same ID
    - Check IParameterChanges for multiple points at same position
    - Add restartComponent (kKeyswitchChanged) / restartComponent (kNoteExpressionChanged) / restartComponent (kParamValuesChanged)
  - Add support of ivstparameterfunctionname in Panner sample
  - New VST 3 plug-ins example:
    - New "AGain Sample Accurate" showing sample accurate parameter changes processing
  - Fix editorHost when launch without arguments
  - Fix crash in VST3Inspector when no VST 3 plug-ins available
  - Fix warnings for mda plug-ins
  - Fix the build with gcc 11
- Helpers classes:
  - New utility files:
    - audiobuffers.h
    - processdataslicer.h
    - rttransfer.h
    - sampleaccurate.h
    - testing.cpp/.h

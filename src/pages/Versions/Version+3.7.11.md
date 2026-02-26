>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.7.11 (2024/04/22)

## Version 3.7.11 (2024/04/22)

- Interface changes:
  - New [Vst:: IRemapParamID](../Technical+Documentation/Change+History/3.7.11/IRemapParamID.md): allows the plug-in to ask the host to remap some parameter ID if needed.

- New Flags/Enums:
  - New RestartFlags: [kParamIDMappingChanged](../Technical+Documentation/Change+History/3.7.11/IRemapParamID.md).

- Documentation
  - new doc for [Vst:: IRemapParamID](../Technical+Documentation/Change+History/3.7.11/IRemapParamID.md).

- CMake
  - references to **VST 2** are removed from the SDK.
 
- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - **VST 2** Wrapper is removed from the SDK.

- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - New VST 3 plug-in example:
    - New [Test Remap ParamID](../What+is+the+VST+3+SDK/Plug-in+Examples.md#test-remap-paramid) showing how a VST 3 plug-in could replace an another VST 3 plug-in (in this case AGain) and remap the parameters ID.

>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.7.7 (2022/12/12)

## Version 3.7.7 (2022/12/12)

- Interface changes:
  - Refactor SDK version macros in *vsttypes.h* so that the C API generator can use it.
  - Better Support of MinGW in *fplatform.h*.

- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) update [4.12](https://github.com/steinbergmedia/vstgui/releases/tag/vstgui4_12)
  
- Documentation
  - New tutorial: [Creating a cmake plug-in project from scratch](../Tutorials/Creating+a+plug-in+from+scratch.md)
  - New tutorial: [Switching to another VSTGUI submodule or branch](../Tutorials/Switching+to+another-VSTGUI+submodule+or+branch.md)

- cmake
  - Adapting cmake for making possible to extract an example from the SDK.
  - Fix folder name for Windows *Arm64EC*.
  - Remove **${SDK_ROOT}** from *smtg_target_configure_version_file*.
  - Replace **SDK_ROOT** with **vst3sdk_SOURCE_DIR**.
  - Better support of MinGW.
  - Improve *SMTG_AAXSupport.cmake* and *SMTG_CoreAudioSupport.cmake*
  - Fix initialization of **CMAKE_OSX_DEPLOYMENT_TARGET**.

- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - Audio Unit:
    - AUv3Wrapper: fix crash building parameter groups ([PR#43](https://github.com/steinbergmedia/vst3_public_sdk/pull/43)).
    - AUv3Wrapper: fix crash for empty parameter groups ([PR#44](https://github.com/steinbergmedia/vst3_public_sdk/pull/44)).

- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.4:
  - **MIDI 2** support on macOS with higher resolution for *Velocity On/Off*, *Aftertouch*, *Polypressure*, *ControlChange* and *PitchBend*.

- [VST3 Project Generator](../What+is+the+VST+3+SDK/Project+Generator.md) v2022.11:
  - Support of multiple namespaces for generated plug-in source code (XX::YY::ZZ), request **C++17** minimum.
  - Fix support of space character in paths.
  
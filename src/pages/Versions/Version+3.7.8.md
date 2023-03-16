>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.7.8 (2023/03/??)

## Version 3.7.8 (2023/03/??)

- Interface changes:
  - add new Microsoft unified *Arm64X* binary definition for **VST 3** plug-ins.
- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) update [4.12](https://github.com/steinbergmedia/vstgui/releases/tag/vstgui4_12)???
  
- Documentation

- cmake
  - **Breaking Change**: options renamed to more meaningful words:
    - SMTG_ADD_VST3_HOSTING_SAMPLES => **SMTG_ENABLE_VST3_HOSTING_EXAMPLES**
    - SMTG_ADD_VST3_PLUGINS_SAMPLES => **SMTG_ENABLE_VST3_PLUGIN_EXAMPLES**
    - SMTG_ADD_VSTGUI => **SMTG_ENABLE_VSTGUI_SUPPORT**

- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - Audio Unit:
    - AUv3Wrapper:
      - Remove duplicate -loadAudioFile: method declaration ([PR#46](https://github.com/steinbergmedia/vst3_public_sdk/pull/46)).
      - Fix iOS build errors ([PR#47](https://github.com/steinbergmedia/vst3_public_sdk/pull/46))
      - Fix resets all parameter values when restartComponent (kParamTitlesChanged) is called ([Issue#45](https://github.com/steinbergmedia/vst3_public_sdk/issues/45))
    - AUv2Wrapper: fix "AUv2 editor does not always work"([Issues#108](https://github.com/steinbergmedia/vst3sdk/issues/108))

- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - Improve silence flag handling in some plug-ins examples.

- Helpers classes:
  - Fix Build error on Linux with gcc 12 (moduleinfoparser.cpp) ([Issue#99](https://github.com/steinbergmedia/vst3_public_sdk/pull/46)).
  - Fix Controller CID output from validator cut on non-Windows platform ([Issue#109](https://github.com/steinbergmedia/vst3sdk/issues/109)).
  - Add security check ([PR#51](https://github.com/steinbergmedia/vst3_public_sdk/pull/51)).

- [Validator](../What+is+the+VST+3+SDK/Index.md#validator-command-line):
  - Add info when a unit has too many parameters

- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.4: ???

- [VST3 Project Generator](../What+is+the+VST+3+SDK/Project+Generator.md) v2022.11: ??
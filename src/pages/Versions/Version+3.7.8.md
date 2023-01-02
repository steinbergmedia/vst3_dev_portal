>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.7.8 (2023/03/??)

## Version 3.7.8 (2023/03/??)

- Interface changes:
  - add new Microsoft unified *Arm64X* binary definition for **VST 3** plug-ins.
- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) update [4.12](https://github.com/steinbergmedia/vstgui/releases/tag/vstgui4_12)???
  
- Documentation

- cmake

- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - Audio Unit:
    - AUv3Wrapper: Remove duplicate -loadAudioFile: method declaration ([PR#46](https://github.com/steinbergmedia/vst3_public_sdk/pull/46)).
    - AUv3Wrapper: fix iOS build errors ([PR#47](https://github.com/steinbergmedia/vst3_public_sdk/pull/46))

- Helpers classes:
  - Build error on Linux with gcc 12 (moduleinfoparser.cpp) ([Issue#99](https://github.com/steinbergmedia/vst3_public_sdk/pull/46)).

- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.4: ???

- [VST3 Project Generator](../What+is+the+VST+3+SDK/Project+Generator.md) v2022.11: ??
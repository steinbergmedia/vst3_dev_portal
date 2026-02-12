  >/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.8.1 (2026/??/??)

## Version 3.8.1 (2026/??/??)

- Interface changes:
  - TODO

- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) update [4.15.0](https://github.com/steinbergmedia/vstgui/releases/tag/vstgui4_15_0)
  
- Documentation
  - TODO

- cmake
  - Remove AUWrapper target from main *CMakeLists.txt*.

- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - Audio Unit:
    - **AUv2Wrapper**:
      - Fix auwrapper.mm: wrong arguments to CFStringGetCharacters ([PR#80](https://github.com/steinbergmedia/vst3_public_sdk/pull/80)).

- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - Fix: incorrect note expression info in the example note expression plugin ([Issue#78](https://github.com/steinbergmedia/vst3_public_sdk/issues/78)).

- Helper Classes:
  - Fix: Validator test which does not respect the Audio Processor Call Sequence ([Issue#148](https://github.com/steinbergmedia/vst3sdk/issues/148)).
  - Fix: unused parameter in module_mac.mm ([Issue#83](https://github.com/steinbergmedia/vst3_public_sdk/issues/83)).
  - Update: linux VST3 system paths: add */usr/lib64/vst3* in *vst/source/hosting/module_linux.cpp* ([PR#82](https://github.com/steinbergmedia/vst3_public_sdk/pull/82)).
  
- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.10.10:
  
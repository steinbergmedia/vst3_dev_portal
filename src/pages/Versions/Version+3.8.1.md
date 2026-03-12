  >/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.8.1 (2026/??/??)

## Version 3.8.1 (2026/??/??)

- Interface changes:
  - TODO

- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) update [4.15.0](https://github.com/steinbergmedia/vstgui/releases/tag/vstgui4_15_0)
  
- CMake
  - Remove AUWrapper target from main *CMakeLists.txt*.
  - Better detection of Windows 32-bit build for non-Visual Studio generators ([PR#14](https://github.com/steinbergmedia/vst3_cmake/pull/14)).

- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - Audio Unit:
    - **AUv2Wrapper**:
      - Fix auwrapper.mm:
        - wrong arguments to CFStringGetCharacters ([PR#80](https://github.com/steinbergmedia/vst3_public_sdk/pull/80)).
        - AUWrapper::restartComponent kLatencyChanged handling ([PR#79](https://github.com/steinbergmedia/vst3_public_sdk/pull/79)).

- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - Fix: incorrect note expression info in the example [Note Expression Synth](../What+is+the+VST+3+SDK/Plug-in+Examples.md#note-expression-synth) Plug-in ([Issue#78](https://github.com/steinbergmedia/vst3_public_sdk/issues/78)).
  - Fix: missing call to *notifyProgramListChange* after changing exported programs count in the [Test Multiple Program Changes](../What+is+the+VST+3+SDK/Plug-in+Examples.md#test-multiple-program-changes) Plug-in.

- Helper Classes:
  - Fix: Validator test which does not respect the Audio Processor Call Sequence ([Issue#148](https://github.com/steinbergmedia/vst3sdk/issues/148)).
  - Fix: unused parameter in module_mac.mm ([Issue#83](https://github.com/steinbergmedia/vst3_public_sdk/issues/83)).
  - Update: linux VST3 system paths: add */usr/lib64/vst3* in *vst/source/hosting/module_linux.cpp* ([PR#82](https://github.com/steinbergmedia/vst3_public_sdk/pull/82)).
  - Fix: compilation with some compilers (e.g. Clang 17), missing include *exception.h* in *threadchecker* file ([Issue#84](https://github.com/steinbergmedia/vst3_public_sdk/issues/84)).
  - Fix set window title on macOS: *editorhost/source/platform/mac/window.mm* ([Issues#134](https://github.com/steinbergmedia/vst3sdk/issues/134)).
  
- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.10.10:
  
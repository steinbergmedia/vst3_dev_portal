  >/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.7.13 (2025/02/28)

## Version 3.7.13 (2025/02/28)

- Interface changes:
  - Fix -Wundef warnings ([PR#17](https://github.com/steinbergmedia/vst3_public_sdk/pull/17)). 
  - Fix enabling/disabling warnings in public header files ([Issue#18](https://github.com/steinbergmedia/vst3_pluginterfaces/issues/18)).
  - Add the possibility to disable #pragma warning on Windows (Visual Studio) with *SMTG_DISABLE_DEFAULT_DIAGNOSTICS*.

- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) update [4.14.2](https://github.com/steinbergmedia/vstgui/releases/tag/vstgui4_14_2)

- Documentation
  - Update doc about *pluginterfaces/gui/iplugview.h*. See [VST3 forum](https://forums.steinberg.net/t/iplugview-contentscalesupport-and-macos/930318).
  - Add more information for each **VST 3** API function about threading and state context.

- CMake
  - Update cmake_minimum_required to *3.25.0*
  - Fix linker warning on Mac ([PR#11](https://github.com/steinbergmedia/vst3_cmake/pull/11)).
  - *smtg_target_add_plugin_resource* groups and structures the resources files into the IDE.
  - Fix white space issue with resources [Forum](https://forums.steinberg.net/t/white-space-issue-with-resources-3-7-12/955129).

- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - Audio Unit:
    - **AU/AUv3 Wrappers**:
      - Fix crash running AGain AUv3 when using auval (*public.sdk/source/vst/auv3wrapper/Shared/AUv3Wrapper.mm*).
    - **AU Wrapper**:
      - Fix auwrapper MIDI output bugs ([PR#76](https://github.com/steinbergmedia/vst3_public_sdk/pull/76)) (*public.sdk/ssource/vst/auwrapper/auwrapper.h*).
      - Fix MIDI CC input in AU wrapper ([PR#74](https://github.com/steinbergmedia/vst3_public_sdk/pull/74/)). (*public.sdk/source/vst/auwrapper/auwrapper.mm*).

- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - Add support of [Vst:: IAudioProcessor::setProcessing](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html#af252fd721b195b793f3a5dfffc069401) in most of the plug-ins, demonstrating how this function can be used (e.g., cleaning delay lines, killing voices, etc.).
  - Update **Hostchecker** plug-in:
    - Redesign the UI.
    - Add check of COM correct behavior when calling queryInterface ().
    - Add check for ProcessContext::systemtime of continuity.

- Helper Classes:
  - Fix in *openurl.cpp* **openURLInDefaultApplication** returns wrong result on macOS and Linux.
  - Fix *vst3_public_sdk/source/vst/hosting/module_linux.cpp*: Plug-in bundles with an extra dot in the name fail to load with the Hosting::Module class ([Issue#73](https://github.com/steinbergmedia/vst3_public_sdk/issues/73)).
  - Fix -Wundef warnings ([PR#75](https://github.com/steinbergmedia/vst3_public_sdk/pull/75)). 
  - Fix **HostApplication::queryInterface** -- mPlugInterfaceSupport Query Interface should use "_iid", not "iid"([Issue#131](https://github.com/steinbergmedia/vst3sdk/issues/131)).
  - Fix seek to the end + add new function *take* allowing to take the memory out of the stream: *public.sdk/source/vst/utility/memoryibstream.h*.
  - Fix memory leak with timer in *public.sdk/source/vst/utility/dataexchange.cpp*.
  - Add new validation function: **validateBundleStructure** in *public.sdk/source/vst/hosting/module_win32.cpp*, *public.sdk/source/vst/hosting/module_mac.cpp*, *public.sdk/source/vst/hosting/module_linux.cpp*.

- [VST 3 Project Generator](../What+is+the+VST+3+SDK/Project+Generator.md) v2025.02:
  - Fix: Only add SMTG_PREFIX_FOR_FILENAMES_CLI argument when not empty.

- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.9:
  - Fix add parameter changes to output parameter queue so that the edit controller will see the change.
  - Fix use parameter step count for program change calculation.

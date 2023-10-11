>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.7.8 (2023/05/15)

## Version 3.7.8 (2023/05/15)

- Interface changes:
  - **Breaking Change**: the [moduleinfo.json](../Technical+Documentation/VST+Module+Architecture/ModuleInfo-JSON.md) file, introduced in the VST 3.7.5, is now located in the **Contents/Resources** folder in order to be compliant with code signing on macOS.
  - Add new Microsoft unified *Arm64X* binary definition for **VST 3** plug-ins.
  - New category: **kFxVocals** for tools dedicated to vocals.
  - New Flags/Enums:
    - New predefined Ambisonics speaker arrangements:
      - **kAmbi4thOrderACN** with new speakers: **kSpeakerACN16** to **kSpeakerACN24**,
      - **kAmbi5thOrderACN**, **kAmbi6thOrderACN**, **kAmbi7thOrderACN**: breaking speaker-bit compability by starting from index 0. Including some helper functions to map speaker index between order 1 to 4 and order 5 to 7 (*convertSpeaker_Ambi_1234Order_to_Ambi567Order* and *convertSpeaker_Ambi_567Order_to_Ambi1234Order*).

- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) update [4.12.3](https://github.com/steinbergmedia/vstgui/releases/tag/vstgui4_12_3)

- cmake
  - Fix "When vst3sdk is a submodule, example plugins are not built - a switch to choose would be very useful" ([Issue#94](https://github.com/steinbergmedia/vst3sdk/issues/94)).
  - Fix CMake fails with bad $-escape ([Issue#100](https://github.com/steinbergmedia/vst3sdk/issues/100)).
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
    - AUv2Wrapper:
      - Fix "AUv2 editor does not always work" ([Issues#108](https://github.com/steinbergmedia/vst3sdk/issues/108))
      - Fix endless **SMTG_AUView setFrame** recursion call in AUv2 Wrapper

- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - Improve silence flag handling in some plug-ins examples.
  - **Hello World VST 3** plug-in example is moved to [github](https://github.com/steinbergmedia/vst3_example_plugin_hello_world)!

- Helpers classes:
  - Fix Build error on Linux with gcc 12 (moduleinfoparser.cpp) ([PR#49](https://github.com/steinbergmedia/vst3_public_sdk/pull/49)).
  - Fix cannot fully build on linux due to missing Steinberg::SystemClipboard::copyTextToClipboard() implementation ([Issue#102](https://github.com/steinbergmedia/vst3sdk/issues/102)).
  - Fix Controller CID output from validator cut on non-Windows platform ([Issue#109](https://github.com/steinbergmedia/vst3sdk/issues/109)).
  - Add security check ([PR#51](https://github.com/steinbergmedia/vst3_public_sdk/pull/51)).
  - Fix moduleinfotool.exe with UTF8 Normalization issue on Windows.
  - Improve robustness of FStreamer::readString8 ([PR#5](https://github.com/steinbergmedia/vst3_base/pull/5)).
  - Fix warning: loop variable 'flag' binds to a temporary value produced by a range of type 'std::optional<JSON::Object>::value_type'
  - Fix warnings that cannot be silenced on MinGW 8.1 ([PR#14](https://github.com/steinbergmedia/vst3_pluginterfaces/pull/14)).
  - Remove warnings that cannot be silenced on Linux ([PR#6](https://github.com/steinbergmedia/vst3_base/pull/6).
  - Fix language standard check in module_linux.cpp ([PR#53](https://github.com/steinbergmedia/vst3_public_sdk/pull/53)).
  - Fix Qualify std::move call in module.cpp to silence a -Wunqualified-std-cast-call warning ([PR#53](https://github.com/steinbergmedia/vst3_public_sdk/pull/53)).
  - Fix Include <cstdint> in moduleinfo.h to ensure that sized int types are visible ([PR#53](https://github.com/steinbergmedia/vst3_public_sdk/pull/53)).

- [Validator](../What+is+the+VST+3+SDK/Index.md#validator-command-line):
  - Add info when a unit has too many parameters

- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.5:
  - New Native Arm64EC version for Windows on Arm: allowing to load VST 3 Plug-ins built for Arm64EC.
  - New Windows built-in ASIO Driver for x64 and Arm64EC.

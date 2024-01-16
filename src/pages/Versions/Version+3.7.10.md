>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.7.10 (2024/01/18)

## Version 3.7.10 (2024/01/18)

- Interface changes:
  - Minimum requirement is now **C++17**.
  - New subCategories for PlugType:
    - **kFxBass** / **kFxChannelStrip** / **kFxDrums** / **kFxGuitar** / **kFxMicrophone**

- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) update [4.13.3](https://github.com/steinbergmedia/vstgui/releases/tag/vstgui4_13_3)

- Documentation
  - Clarify range of [param ID](../Technical+Documentation/Parameters+Automation/Index.md#parameters).
  - Add note for [Module Info and Plug-in Compatibility](../Technical+Documentation/Change+History/3.7.5/ModuleInfo.md#iplugincompatibility).

- cmake
  - Fix *smtg_target_make_plugin_package* can create invalid VST 3 plug-ins ([Forum](https://forums.steinberg.net/t/weird-cmake-error/862347)).
  - Fix regression for non-bundle Windows plug-ins (non-bundle VST 3 on Windows will be declared deprecated in a future update of VST 3 SDK).

- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - New VST 3 plug-ins example:
    - New [Utf16Name](../What+is+the+VST+3+SDK/Plug-in+Examples.md#utf16name) showing use of UTF16 characters in plug-in and company name.
  - Fix EditorHost issue when moving windows between different DPI screens ([Forum](https://forums.steinberg.net/t/vst3-sdk-editorhost-displays-only-25-of-juce-gui-on-4k-monitor/873310/2) / [Juce Fourm](https://forum.juce.com/t/steinberg-editorhost-on-4k-monitor-is-not-good/58366/7)).

- [Validator](../What+is+the+VST+3+SDK/Index.md#validator-command-line):
  - Add test checking that IPluginBase is provided by the controller and the processor.
  - Add support on Windows for UTF8 path.

- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.7:
  - Fix global buffer overflow (AddressSanitizer) issue.
  - On Windows "*Steinberg built-in Driver*" is used by default if present.

- [VST3 Project Generator](../What+is+the+VST+3+SDK/Project+Generator.md) v2024.01:
  - Fix: ProjetGenerator should not allow new project inside the SDK folder.
  - Adapt template project: remove audio input for Instrument and add a default processing implementation as example.
  
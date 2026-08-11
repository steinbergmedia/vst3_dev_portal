  >/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.7.14 (2025/06/23)

## Version 3.7.14 (2025/06/23)

- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) update [4.14.3](https://github.com/steinbergmedia/vstgui/releases/tag/vstgui4_14_3)

- Documentation
  - Updated Doxygen version.
  - Fix tutorial dataexchange example.

- CMake
  - Fix createlink does not work on macOS 15.4. 

- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - Fix mda plug-ins: mda Synthesizers should convert % parameter strings using 0 to 100, not 0 to 1 ([Issue#135](https://github.com/steinbergmedia/vst3sdk/issues/135)).
  - Fix mda plug-in: mdaPianoController.cpp incorrectly implements 4 presets instead of 7 ([Issue#133](https://github.com/steinbergmedia/vst3sdk/issues/133)).
  - Add variable program count support to *Test Multiple Program Changes* Plug-in.

- Helper Classes:
  - Fix missing implementation of FUID::generate() for Windows on Arm ([Issue#20](https://github.com/steinbergmedia/vst3_pluginterfaces/issues/20)).

- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.10:
  - Fix support of parameters with UTF16 characters (not only ASCII).

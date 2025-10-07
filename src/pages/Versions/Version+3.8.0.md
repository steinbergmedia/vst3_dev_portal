  >/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.8.0 (2025/10/15)

## Version 3.8.0 (2025/10/15)

- [New licensing model for VST 3](../VST+3+Licensing/Index.md): 
  - VST 3 is now open source, released under the [MIT license](https://tlo.mit.edu/understand-ip/exploring-mit-open-source-license-comprehensive-guide).

- Interface changes:
  - Support for **MIDI 2.0**: new interfaces [IMidiLearn2](../Technical+Documentation/Change+History/3.8.0/IMidiLearn2.md) and [IMidiMapping2](../Technical+Documentation/Change+History/3.8.0/IMidiMapping2.md). These new interfaces replace the previous interfaces *IMidiLearn* and *IMidiMapping*.
  - Add missing ControllerNumbers enum for **MIDI 1.0** System messages.

- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) update [4.15.0](https://github.com/steinbergmedia/vstgui/releases/tag/vstgui4_15_0)
  - TODO Wayland support

- Documentation
  - Adapt document to [new licensing model](../VST+3+Licensing/Index.md).
  - Update [Steinberg VST usage guidelines](../VST+3+Licensing/Usage+guidelines.md) document.

- cmake
  - Fix SMTG_PlatformToolset.cmake: __cplusplus was not assigned to correct version [pull#13](https://github.com/steinbergmedia/vst3_cmake/pull/13).
  
- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - Add support of new ControllerNumbers enums in *legacymidiccout* Plug-in.
  - Add support of the new interfaces [IMidiLearn2](../Technical+Documentation/Change+History/3.8.0/IMidiLearn2.md) and [IMidiMapping2](../Technical+Documentation/Change+History/3.8.0/IMidiMapping2.md) in *Note Expression Synth* Plug-in.
  - EditorHost Wayland support TODO

- Helper Classes:
  - Fix: Validator ScanParametersTest::run() - Doesn't Print Parameter Type Correctly [Issue#142](https://github.com/steinbergmedia/vst3sdk/issues/142).
  - Fix: validator.exe and moduleinfotool.exe Debug Version Throws Abort When Checking for Symlink ([Issue#145](https://github.com/steinbergmedia/vst3sdk/issues/145)).
  - Fix: Undefined Behavior (UB) in Validation Test Suite causes test case to fail ([Issue#77](https://github.com/steinbergmedia/vst3sdk/issues/77)).

- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.10.10:
  - Fix: potential crash at start on Windows platform [Forum](https://forums.steinberg.net/t/win10-64bit-vst3plugintesthost-quits-silenty-on-start/1007817/5).

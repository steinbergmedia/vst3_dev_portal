  >/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.8.0 (2025/10/15)

## Version 3.8.0 (2025/10/15)

- [New licensing model for VST 3](../VST+3+Licensing/Index.md): 
  - VST 3 is now open source, released under the [MIT license](https://tlo.mit.edu/understand-ip/exploring-mit-open-source-license-comprehensive-guide).

- Interface changes:
  - new ControllerNumbers enum for MIDI 1 System message:
    - *kSystemSongSelect / kSystemSongPointer*
    - *kSystemCableSelect*
    - *kSystemTuneRequest*
    - *kSystemMidiClockStart / kSystemMidiClockContinue / kSystemMidiClockStop*
    - *kSystemActiveSensing*
  - new NoteExpression Event: *NoteExpressionIntValueEvent* (and new EventTypes *kNoteExpressionIntValueEvent*) with uint64 as payload.

- TODO [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) update [4.14.3](https://github.com/steinbergmedia/vstgui/releases/tag/vstgui4_14_3)
  - Wayland support

- Documentation
  - Adapt licensing document.

- cmake
  
- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - Add support of new ControllerNumbers enums in legacymidiccout.
  
- Helper Classes:
  - Wayland support TODO
  - Fix: Validator ScanParametersTest::run() - Doesn't Print Parameter Type Correctly [Issue#142](https://github.com/steinbergmedia/vst3sdk/issues/142).
  - Fix: validator.exe and moduleinfotool.exe Debug Version Throws Abort When Checking for Symlink ([Issue#145](https://github.com/steinbergmedia/vst3sdk/issues/145)).
  - Fix: Undefined Behavior (UB) in Validation Test Suite causes test case to fail ([Issue#77](https://github.com/steinbergmedia/vst3sdk/issues/77)).

- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.10:
  - TODO 

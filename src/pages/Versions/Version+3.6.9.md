>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.6.9 (2018/03/01)

## Version 3.6.9 (2018/03/01)

- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) 4.6
  - update to VSTGUI 4.6
  - including a new UI element: KeyboardView supporting Note Expression
- Interfaces changes:
  - rename some defines:
    - PLATFORM_64 => SMTG_PLATFORM_64
    - WINDOWS => SMTG_OS_WINDOWS
    - MAC => SMTG_OS_MACOS
    - LINUX => SMTG_OS_LINUX
  - extract Speaker Arrangement from vsttypes.h to vstspeaker.h
  - new kNoParamId constant for uninitialized parameter id
- cmake:
  - reorganization of cmake files
- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - fix [Validator](../What+is+the+VST+3+SDK/Index.md#validator-command-line) State test
  - NoteExpressionSynth uses the new KeyboardView
  - New HelloWorld **VST 3** plug-ins (template): [Creating a plug-in from the Helloworld template](../Tutorials/Creating+a+plug-in+from+the+Helloworld+template.md)
- [Plug-in wrappers](../What+is+the+VST+3+SDK/Wrappers/index.md):
  - VST 3 - Audio Unit Wrapper: fix and adaptation for newer XCode versions
  - Audio Unit v3 (AUv3) Wrapper (VST 3 - Audio Unit v3 Wrapper): some fixes, add cmake
  - AAX Wrapper (VST 3 - AAX Wrapper): add bypass and VU parameter support
  - interappaudio: improvements, fixes, add cmake
- Helpers classes:
  - New Ring Buffer class (ringbuffer.h)

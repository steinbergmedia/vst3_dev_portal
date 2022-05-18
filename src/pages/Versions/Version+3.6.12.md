>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.6.12 (2018/12/03)

## Version 3.6.12 (2018/12/03)

- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) 4.7
  - redesigned drag and drop (drags with bitmaps are now supported on Windows)
  - standalone library support for Windows 7
  - new ImageStitcher tool
  - the GDI+ draw backend was removed, the Direct2D backend is the replacement
  - fix crash with splash screen
  - fix compilation for VSTGUI Tools on win32
  - clean up
- Interfaces changes:
  - New LegacyMIDICCOutEvent (plug-in): allow a plug-in to generate MIDI CC as output event.
  - New IMidiLearn (plug-in): allow a plug-in to get the currently live playing MIDI CC to implement custom MIDI learning.
  - New IPlugInterfaceSupport (host): allow a plug-in to ask the host if a given plug-in interface is supported/used by the host.
  - New IVst3WrapperMPESupport (wrapper): allow a plug-in to set up MPE support in wrappers.
- cmake:
  - minor refactoring (like renaming WIN to SMTG_WIN)
  - fix WIN_ARCHITECTURE_NAME for Windows 32bits
  - fix SMTG_PACKAGE_ICON_PATH selection
  - split WIN_PDB into WIN_PDB32 and WIN_PDB64
- [Samples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - New LegacyMIDICCOut VST 3 plug-in showing the use of LegacyMIDICCOutEvent
  - Add IMidiLearn support for NoteExpressionSynth
  - Add Audio Unit v3 NoteExpressionSynth example with MPE support
- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - Audio Unit v3 (AUv3) Wrapper (VST 3 - Audio Unit v3 Wrapper):
    - out of the box MPE support. As MPE is a limited subset of the Note Expression feature, the three expressions are simply mapped to the note expressions returned via the [INoteExpressionPhysicalUIMapping](../Technical+Documentation/Change+History/3.6.11/INoteExpressionPhysicalUIMapping.md) interface.
    - note that you must have certificates to sign on macOS/iOS for AUv3
    - complete folder restructuring for easy adaption
  - AAX Wrapper ([VST 3 - AAX Wrapper](../What+is+the+VST+3+SDK/Wrappers/AAX+Wrapper.md)):
    - fix automation update after loading a preset
  - VST 2 Wrapper:
  - fix double release of editor
- Helpers classes:
  - New file with some helpers for event: vsteventshelper.h

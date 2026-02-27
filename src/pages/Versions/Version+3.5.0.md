>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.5.0 (2011/02/04)

## Version 3.5.0 (2011/02/04)

- Interface Changes:
  - Vst::INoteExpressionController: [\[3.5.0\] Note Expression](../Technical+Documentation/Change+History/3.5.0/INoteExpressionController.md) Support.
  - Vst::IKeyswitchController: [\[3.5.0\] Key Switch Support](../Technical+Documentation/Change+History/3.5.0/IKeyswitchController.md) (used for building VST Expression Map in Cubase 6 for example).
  - Vst::IXmlRepresentationController: [\[3.5.0\] Remote Representation](../Technical+Documentation/Change+History/3.5.0/IXmlRepresentationController.md) of Parameters Support (allows to define different parameter mappings for different remotes device).
  - Vst::IEditControllerHostEditing: Parameter editing from host/remote control (better support of linked parameters when editing from remote control)
  - Vst::IComponentHandler3 / Vst::IContextMenu / Vst::IContextMenuTarget: [\[3.5.0\] Context Menu Support](../Technical+Documentation/Change+History/3.5.0/IComponentHandler3.md) (allows the plug-in to create a context menu for a given parameter, partially filled by the host).

- New Flags/Enums:
  - Add new restart flag: Vst::kIoTitlesChanged: informing the host about titles changes of busses.

- Helper Classes:
  - New Vst::XmlRepresentationHelper: helper for constructing a remote representation (xml based). See [\[3.5.0\] Remote Representation of Parameters Support](../Technical+Documentation/Change+History/3.5.0/IXmlRepresentationController.md).
  - Vst::EditControllerEx1: support of ProgramPitchNames added.

- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - New VST 3 instrument examples:
    - Instrument [Note Expression Synth](../What+is+the+VST+3+SDK/Plug-in+Examples.md#note-expression-synth) Plug-in supporting Note Expression Events.
    - Effect showing support of ProgramPitchNames [PitchNames](../What+is+the+VST+3+SDK/Plug-in+Examples.md#pitchnames).

- [Validator](../What+is+the+VST+3+SDK/Index.md#validator-command-line):
  - More command line options.
  - Possibility to add custom tests by the plug-in.

- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) 4.0
  - preview version of VSTGUI with optimal **VST 3** support.

- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - VST 3 - Audio Unit Wrapper fixes and support of Program changes.
  
- Some documentation changes.

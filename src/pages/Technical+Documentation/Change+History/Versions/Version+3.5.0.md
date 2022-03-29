>/ ... / [Change History](../Index.md)
>
># Version 3.5.0 (2011/02/04)

## Version 3.5.0 (2011/02/04)

- New Interfaces:
    - Steinberg::Vst::INoteExpressionController : [[3.5.0] Note Expression](../3.5.0/INoteExpressionController.md) Support.
    - Steinberg::Vst::IKeyswitchController : [[3.5.0] Key Switch Support](../3.5.0/IKeyswitchController.md) (used for building VST Expression Map in Cubase 6 for example).
    - Steinberg::Vst::IXmlRepresentationController : [[3.5.0] Remote Representation](../3.5.0/IXmlRepresentationController.md) of Parameters Support (allows to define different parameter mappings for different remotes device).
    - Steinberg::Vst::IEditControllerHostEditing : Parameter editing from host/remote control (better support of linked parameters when editing from remote control)
    - Steinberg::Vst::IComponentHandler3 / Steinberg::Vst::IContextMenu / Steinberg::Vst::IContextMenuTarget : [[3.5.0] Context Menu Support](../3.5.0/IComponentHandler3.md) (allows the Plug-in to create a context menu for a given parameter, partially filled by the host).
- New Flags/Enums:
    - Add new restart flag: Steinberg::Vst::kIoTitlesChanged : informing the host about titles changes of busses.
- Helpers Classes:
    - New Steinberg::Vst::XmlRepresentationHelper : helper for constructing a remote representation (xml based). See [[3.5.0] Remote Representation of Parameters Support](../3.5.0/IXmlRepresentationController.md).
    - Steinberg::Vst::EditControllerEx1 : support of ProgramPitchNames added.
- Samples:
    - New VST 3 instrument examples:
        - Instrument "Note Expression Synth" supporting Note Expression Events
        - Effect showing support of pitchnames (ProgramPitchNames)
- Validator:
    - More command line options
    - Possibility to add custom tests by the Plug-in
- VSTGUI 4.0
    - preview version of VSTGUI with optimal VST 3 support
- Plug-in Wrappers:
    - VST 3 - Audio Unit Wrapper fixes and support of Program changes
- Some documentation changes
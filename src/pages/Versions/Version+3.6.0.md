>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.6.0 (2013/11/22)

## Version 3.6.0 (2013/11/22)

- Interface Changes:
  - Preset meta information via Steinberg::Vst::IStreamAttributes
  - New Event Types: Steinberg::Vst::ChordEvent, Steinberg::Vst::ScaleEvent
- Plug-in Wrappers:
  - [3.6.0] iOS Inter-App Audio support
  - VST 3 - VST 2.x Wrapper :
    - fix when changing from host between single and double precision processing
    - fix setProgram and processMidiEvent for kProgramChangeStatus where the wrong idx was used for programChange Parameter
  - VST 3 - Audio Unit Wrapper :
    - updopt to new AUPlugIn API in Mac OS X 10.7
    - virtual destructor for NSDataIBStream
- New Flags/Enums:
  - New predefined 3D Speaker Arrangements: k81MPEG3D, k222
- Helpers Classes:
  - fix compilation for UNICODE_OFF enable
- Samples:
  - New VST 3 HostChecker Plug-in
- VSTGUI 4.2
  - Update to the final 4.2 release including iOS support
- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md): VST 3 Plug-in Test Host
  - New feature: Overwrite Plug-in Name in VST 3 Presets
- Licensing has changed! Please read the new license agreement [VST 3 Licensing Issues](../VST+3+Licensing/Index.md).
- Xcode 5 note: To successfully build the examples for Mac OS X you need to change the SDKROOT variable in base/mac/config/settings/sdk_deployment_10_6.xcconfig to macosx10.8.

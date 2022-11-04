>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.6.5 (2015/08/28)

## Version 3.6.5 (2015/08/28)

- Interface changes:
  - New [Steinberg::Vst::ChannelContext::IInfoListener](../Technical+Documentation/Change+History/3.6.5/IInfoListener.md) interface: informing the plug-in about the channel in which it is instantiated (name, color...)
  - New Steinberg::Vst::IPrefetchableSupport interface: allowing a plug-in to inform the host that it does not support prefetch/ASIO Guard (could be dynamically)
  - New Steinberg::Vst::IUnitHandler2 interface: allowing a plug-in to inform the host that an assignment Unit-Bus defined by IUnitInfo::getUnitByBus has changed
  - New Steinberg::Vst::IAutomationState interface: informing the plug-in about its current automation state
  - use "#pragma once" instead of "#ifndef"
- Samples:
  - New **VST 3 Plug-ins** examples:
    - New **VST 3 Plug-in** ChannelContext showing how Steinberg::Vst::ChannelContext::IInfoListener interface is working
    - New **VST 3 Plug-in** PrefetchableSupport showing how Steinberg::Vst::IPrefetchableSupport interface is working
  - "VST 3 Host Checker" plug-in updated with new checks
- Plug-in wrappers:
  - VST 3 - Audio Unit Wrapper:
    - support MIDI output
    - fix crash with namespace conflict with Mac OS X 10.10
    - add PresetAttributes::StateType support in AUWrapper::restoreState
- New Flags/Enums:
  - New predefined 3D Speaker Arrangements: k91Atmos
- [VST3PluginTestHost](..//What+is+the+VST+3+SDK/Plug-in+Test+Host.md): VST 3 Plug-in Test Host
  - add some new unit tests: Bypass parameter support is mandatory for FX Plug-in (not Instrument)!

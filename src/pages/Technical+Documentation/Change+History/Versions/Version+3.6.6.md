>/ ... / [Change History](../Index.md)
>
># Version 3.6.6 (2016/06/17)

## Version 3.6.6 (2016/06/17)

- Interfaces changes:
    - New Steinberg::IPlugViewContentScaleSupport: Plug-in view content scale support
- New Flags/Enums:
    - New RestartFlags: kRoutingInfoChanged informing the host that the Routing Info (IComponent) has changed
- Samples:
    - New VST 3 plug-ins examples:
        - New **VST 3 Plug-in** Program Change showing how handling its own Program List is working
    - Remove Visual Projects version 8 and 9
- Plug-in wrappers:
    - VST 3 - Audio Unit Wrapper :
        - update to last Audio Core update
    - VST 3 - VST 2.x Wrapper :
        - add support of version (VST 3 -> VST 2)
- Helpers classes:
    - add support for bypass including delay compensation (vstbypassprocessor.h)
    - add helpers for events/parameters iterator (vstaudioprocessoralgo.h)
    - add helpers for SpeakerArr:
        - Speaker getSpeaker (const SpeakerArrangement& arr, int32 index)
        - bool isSubsetOf (const SpeakerArrangement& arrSubSet, const SpeakerArrangement& arr)
- VSTGUI 4.3
    - update to VSTGUI 4.3.1 (available here too: <http://sourceforge.net/projects/vstgui/files/vstgui/VSTGUI%204.3/)>
    - the [VSTGUI](../../../What+is+the+VST+3+SDK/VSTGUI.md) repository was moved to github: <https://github.com/steinbergmedia/vstgui>
    - Please use github if you want to contribute to VSTGUI.
- VST3PluginTestHost: VST 3 Plug-in Test Host
    - fix support of SingleComponent
- new Developer Forum:
    - finally we get our VST forum at start, please check <https://sdk.steinberg.net> and use it as new communication platform, the VST mailing list will be kept as archive mailing list.
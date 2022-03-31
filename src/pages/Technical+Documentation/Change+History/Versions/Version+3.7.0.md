>/ ... / [Change History](../Index.md)
>
># Version 3.7.0 (2020/07/29)

## Version 3.7.0 (2020/07/29)

- Interface changes:
    - New [IProcessContextRequirements](../3.7.0/IProcessContextRequirements.md) (implemented by plug-in).
        - This is a new required interface a plug-in needs to implement when building with VST SDK 3.7 or newer.
    - New [IProgress](../3.7.0/IProgress.md) (implemented by host)
    - New [IParameterFunctionName](../3.7.0/IParameterFunctionName.md) (implemented by plug-in)
- New Flags/Enums:
    - New kIsHidden flag. With this flag, the parameter should NOT be displayed by the host and cannot be changed from outside the plug-in.
    - New predefined 2D speaker arrangements:
        - k90Cine, k91Cine (L R C Lfe Ls Rs Lc Rc Sl Sr)
        - k100Cine, k101Cine (L R C Lfe Ls Rs Lc Rc Cs Sl Sr)
    - New predefined 3D speaker arrangements:
        - k90_4, k91_4 (L R C Lfe Ls Rs Lc Rc Sl Sr Tfl Tfr Trl Trr)
        - k90_6, k91_6 (L R C Lfe Ls Rs Lc Rc Sl Sr Tfl Tfr Trl Trr Tsl Tsr)
    - New Bus flag: kIsControlVoltage for audio busses
- Documentation:
    - add documentation about VST 3 and MIDI 2.0:
        - [MIDI 2.0 Increased Resolution, compared to MIDI 1.0](../About+MIDI/Index.md)
        - [MIDI 2.0 Per-Note Controllers](../About+MIDI/Index.md)
- cmake:
    - New cmake files
    - Fix on Windows creation of VST 3 folder using powershell with admin rights
- [Samples](../../../What+is+the+VST+3+SDK/Plug-in+Examples.md):
    - New VST 3 plug-ins examples:
        - SyncDelay using [Steinberg::Vst::IProcessContextRequirements](../3.7.0/IProcessContextRequirements.md)
        - Panner using PlugType::kSpatialFx as SubCategory, it shows how to build a Panner plug-in Mono to Stereo
    - Added checks in HostChecker plug-in:
        - support of kIsHidden flag
        - support of [IProgress](../3.7.0/IProgress.md) (implemented by host)
        - support of [IParameterFunctionName](../3.7.0/IParameterFunctionName.md)
        - check if Silent flag for Main and [Side-chain](../3.0.0/Multiple+Dynamic+IO.html#what-is-a-side-chain) Inputs are used
- [Plug-in Wrappers](../../../What+is+the+VST+3+SDK/Wrappers/Index.md):
    - Fix for AAX/VST 2 BaseWrapper setChunk attribute Vst::StateType::kProject was not set for component.
- Helpers classes:
    - Added functions to load FXB/FXP states and to write FXB states for compatibility with VST2.x (see public.sdk/source/vst/utility/vst2persistence.h)
    - Fix compilation with MinGW-w64 GCC compiler
    - New helper: openurl.h allowing to open a URL in the default associated application
- [VST3PluginTestHost](../../../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v2.9.0: VST 3 Plug-in Test Host
    - Added support of:
        - IProgress
        - IProcessContextRequirements
        - IParameterFunctionName
    - Fix crashes when closing 2 or more instances of GUI of same plug-in in particular order
    - Fix support of SingleComponentEffect plug-ins that implement IMidiMapping
- [VST3 Project Generator](../../../What+is+the+VST+3+SDK/Project+Generator.md) v1.0.0:
    - New easy to use VST 3 Project Generator
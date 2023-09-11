>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.7.9 (2023/10/??)

## Version 3.7.9 (2023/10/??)

- Interface changes:
  - New Flags/Enums:
    - New speakers: kSpeakerLw and kSpeakerRw for Left and Right Wide
    - New predefined 3D speaker arrangements (compatible Dolby Atmos):
      - **k90_4_W** => L R C Ls Rs Sl Sr Tfl Tfr Trl Trr Lw Rw
      - **k91_4_W** => L R C Lfe Ls Rs Sl Sr Tfl Tfr Trl Trr Lw Rw
      - **k90_6_W** => L R C Ls Rs Sl Sr Tfl Tfr Trl Trr Tsl Tsr Lw Rw
      - **k91_6_W** => L R C Lfe Ls Rs Sl Sr Tfl Tfr Trl Trr Tsl Tsr Lw Rw

- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) update [4.12.3](https://github.com/steinbergmedia/vstgui/releases/tag/vstgui4_12_3)

- cmake
  - 

- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - Audio Unit:
    - AUv3Wrapper:
      - TODO Fix iOS build errors ([PR#47](https://github.com/steinbergmedia/vst3_public_sdk/pull/46))
    - AUv2Wrapper:
      - 

- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - 

- Helpers classes:
  - 

- [Validator](../What+is+the+VST+3+SDK/Index.md#validator-command-line):
  - 

- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.5:
  - 

- [VST3 Project Generator](../What+is+the+VST+3+SDK/Project+Generator.md) v2023.09:
  - Rename SMTG_ADD_VSTGUI to SMTG_ENABLE_VSTGUI_SUPPORT
  
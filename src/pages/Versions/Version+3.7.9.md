>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.7.9 (2023/10/09)

## Version 3.7.9 (2023/10/09)

- Interface changes:
  - New [Vst::IDataExchangeHandler / Vst::IDataExchangeReceiver](../Technical+Documentation/Data+Exchange/Index.md): API to send data from the realtime processing function to the controller in a safe and efficient way.
  - New [Vst::IComponentHandlerSystemTime](../Technical+Documentation/Change+History/3.7.9/IComponentHandlerSystemTime.md): API to query the system time from the controller.
  - New on Linux: [Query IRunLoop from the host context of IPlugFactory3](../Technical+Documentation/Provide+A+Runloop+On+Linux/Index.md).
  - New Flags/Enums:
    - New speakers: kSpeakerLw and kSpeakerRw for Left and Right Wide
    - New predefined 3D speaker arrangements (compatible Dolby Atmos):
      - **k90_4_W** => L R C Ls Rs Sl Sr Tfl Tfr Trl Trr Lw Rw
      - **k91_4_W** => L R C Lfe Ls Rs Sl Sr Tfl Tfr Trl Trr Lw Rw
      - **k90_6_W** => L R C Ls Rs Sl Sr Tfl Tfr Trl Trr Tsl Tsr Lw Rw
      - **k91_6_W** => L R C Lfe Ls Rs Sl Sr Tfl Tfr Trl Trr Tsl Tsr Lw Rw

- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) update [4.13.0](https://github.com/steinbergmedia/vstgui/releases/tag/vstgui4_13_0)

- Documentation
  - New tutorial: [Data Exchange Tutorial - How to send data from the realtime process to the edit controller](../Tutorials/Data+Exchange.md).
  - New doc page about [Provide a RunLoop on Linux](../Technical+Documentation/Provide+A+Runloop+On+Linux/Index.md).

- cmake
  - Change minimal cmake version to 3.5.0.
  - Partially fix for Windows, create destination installation folders if they don't exist [(Issue#8)](https://github.com/steinbergmedia/vst3_cmake/issues/8).

- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - AAX Wrapper ([VST 3 - AAX Wrapper](../What+is+the+VST+3+SDK/Wrappers/AAX+Wrapper.md)):
    - fix some warnings
  - Audio Unit:
    - AUv3Wrapper:
      - Fix iOS build errors ([PR#47](https://github.com/steinbergmedia/vst3_public_sdk/pull/47))
      - Make **AUv3** follow **VST3** threading model [(PR#62)](https://github.com/steinbergmedia/vst3_public_sdk/pull/62)
      - Fix "Missing field initializer" warnings in AUv3Wrapper [(Issue#55)](https://github.com/steinbergmedia/vst3_public_sdk/pull/55/commits/e2765e6d4365f1e81e719eb19e3e2a786f4281c8)

- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - New VST 3 plug-ins example **DataExchange** showing the use of the VST Data Exchange API: public.sdk\samples\vst\dataexchange.
  - Update Hostchecker plug-in to check new interfaces: [Vst::IDataExchangeHandler / Vst::IDataExchangeReceiver](../Technical+Documentation/Data+Exchange/Index.md) / [Vst::IComponentHandlerSystemTime](../Technical+Documentation/Change+History/3.7.9/IComponentHandlerSystemTime.md).

- Helpers classes:
  - New helper for system time public.sdk\source\vst\utility\systemtime.cpp.
  - New VST Data Exchange API Helper implementing IDataExchangeHandler: public.sdk/source/vst/utility/dataexchange.cpp.
  - Fix "Missing field initializer" warning in vstparameters.h [(PR#60)](https://github.com/steinbergmedia/vst3_public_sdk/pull/60).
  - Fix buffer overflow/memory corruption ([Issue#15](https://github.com/steinbergmedia/vst3_pluginterfaces/issues/15)).
  - Fix undefined behavior - load of misaligned address ([Issue#64](https://github.com/steinbergmedia/vst3_pluginterfaces/issues/64)).
  - vstgui4 seems incomplete on Linux ([Issue#104](https://github.com/steinbergmedia/vst3sdk/issues/104)).

- [Validator](../What+is+the+VST+3+SDK/Index.md#validator-command-line):
  - Allow moduleinfo.json and IPluginCompatibility to coexist, not seen as error but warning (not recommanded!) [(Issue#63)](https://github.com/steinbergmedia/vst3_public_sdk/issues/63).

- [VST3 Project Generator](../What+is+the+VST+3+SDK/Project+Generator.md) v2023.09:
  - Rename SMTG_ADD_VSTGUI to **SMTG_ENABLE_VSTGUI_SUPPORT**.
  
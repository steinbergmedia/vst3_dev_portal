>/ ... / [Change History](../Index.md)
>
># Version 3.6.8 (2017/11/08)

## Version 3.6.8 (2017/11/08)
- Changes in the Licensing Agreement! Please check it ([VST 3 Licensing Issues](/pages/VST+3+Licensing/Index.md) **<- Link?**).
- [New Steinberg VST usage guidelines](/pages/VST+3+Licensing/Usage+guidelines.md) PDF
- This SDK version required compilers supporting C++11. It requires on Windows Visual Studio 2015 minimum!
- Linux support in Beta
- Interfaces changes:
    - New Steinberg::Vst::IComponentHandlerBusActivation (host): allowing a plug-in to request the host to activate or deactivate a specific bus (useful for instrument with multiple outputs)
- New Flags/Enums:
    - New predefined Ambisonic Speaker Arrangements: 1st, 2cd and 3rd order (ACN ordering and SN3D normalization): kAmbi1stOrderACN, kAmbi2cdOrderACN, kAmbi3rdOrderACN with their associated speakers: kSpeakerACN0...kSpeakerACN15
    - New predefined 3D speaker arrangements: k70_4, k71_4
- Samples:
    - New VST 3 [Host implementation examples]() **<- Link?**:
    - Folder reorganization: hosting examples are in a separate folder: public.sdk/samples/vst-hosting
    - New AudioHost (AudioHost - cross-platform standalone) showing how integrate a [VST3]() **<- Link?** plug-in in a Jack world! This required Jack Audio (<http://www.jackaudio.org>), only tested under Linux but should work on Windows 32bits and Mac.
- Plug-in wrappers:
    - New Audio Unit v3 (AUv3) Wrapper (VST 3 - Audio Unit v3 Wrapper)
    - New AAX wrapper (VST 3 - AAX Wrapper): Note that in order to use this AAX wrapper for your plug-in, you have to download the AAX SDK (contact AVID), tested with AAX SDK Version 2.3.0.
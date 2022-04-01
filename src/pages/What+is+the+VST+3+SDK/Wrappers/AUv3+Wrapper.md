>/ ... / [AAX, AUv3, AU and VST 2 Wrappers](../Wrappers/Index.md)
>
># VST 3 - AudioUnit v3 Wrapper

**On this page:**

[[_TOC_]]

**Related pages:**

- [Audio Unit v3 Plug-Ins | Apple Developer Documentation](https://developer.apple.com/documentation/audiotoolbox/audio_unit_v3_plug-ins?language=objc)

---

Helper Class wrapping a VST 3 plug-in to an Audio Unit v3 plug-in

## Introduction

The VST 3 SDK comes with a helper class which wraps one **VST 3** audio processor and edit controller to an AUv3 plug-in.

The wrapped AudioUnit does support MPE when the **VST 3** plug-in has Note Expression support. You need to implement [Steinberg::Vst::INoteExpressionPhysicalUIMapping](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1INoteExpressionPhysicalUIMapping.html) to map your Note Expression to the limited three expressions defined by MPE.

## How does it work?

- Structure:
    - App (container app which initializes the AU through small Playback Engine)
    - Extension (extension which is loaded by hosts, also initializes the AU)
- How to use the VST 3 → AU v3 Wrapper with the sample code:
    - make sure you have correct code signing set up
    - build & run targets
- How to use the VST 3 → AUv3 Wrapper with your own VST plug-in:
    - duplicate either the folder again_auv3 or note_expression_synth_auv3 in public.sdk/samples/vst, rename it and edit CMakelist.txt to add your sources, resources and modified target names etc.
    - open audiounitconfig.h and change the definitions in this file.
    - also change the other files in that folder to your requirements. Code signing is required, but you can build and test with a developer only identity.
    - build & run targets
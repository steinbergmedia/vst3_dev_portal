>/ ... / [AAX, AUv3, AU and VST 2 Wrappers](Index.md)
>
># VST 3 - AudioUnit v2 Wrapper

**On this page:**

[[_TOC_]]

**Related pages:**

- [Audio Unit v3 Plug-Ins | Apple Developer Documentation](https://developer.apple.com/documentation/audiotoolbox/audio_unit_v3_plug-ins?language=objc)

---

Helper Class wrapping a **VST 3** plug-in to an **Audio Unit v2** plug-in

## Introduction

The **VST 3 SDK** comes with an AudioUnit wrapper, which can wrap one **VST 3** audio processor and edit controller as an AudioUnit effect/instrument.

The wrapper is a small dynamic library which loads the **VST 3** plug-in. As AudioUnits store some important information in their resource fork, this library must be compiled for every **VST 3** plug-in.

## How does it work?

- You first need to build the SDK ([check here](../../Tutorials/Building+the+examples/Building+the+examples+included+in+the+SDK+macOS.md)) and then you should - have the xcode project.
- You may need to download the CoreAudio SDK from Apple and point cmake to it when building the SDK with it ([see here](../../Tutorials/Using+cmake+for+building+plug-ins.md)).
- create a copy of the again AU wrapper example project directory (public.sdk/source/vst/auwrapper/again/)
- rename the copy to your needs
- edit the target settings of the project and change
  - Product Name
  - Library search path so that it points to the directory where libauwrapper.a exists
  - architecture setting so that it only includes architectures that the **VST 3** plug-in supports
- search in the project for AUWRAPPER_CHANGE and change the settings to your needs, especially in:
  - edit audiounitconfig.h, see comments there
  - edit Info.plist, see comments there
- edit the "Make Links Script" for easier debugging/development
- build your project
- done ... that is all!

For the release version, you must place a copy or an alias of your **VST 3** plug-in in the resource folder of the bundle named "plugin.vst3"

>/ ... / [AAX, AUv3, AU and VST 2 Wrappers](../Wrappers/Index.md)
>
># VST 3 - AAX Wrapper

**On this page:**

[[_TOC_]]

---

Helper Class wrapping a VST 3 plug-in to a AAX plug-in

## Introduction

The VST 3 SDK comes with a helper class which wraps one VST 3 audio processor and edit controller to an AAX plug-in.

## How does it work?

- Check the AGainAAX example
- AAX SDK 2.3 or higher is expected in folder external.avid.aax (located at the same level as the folder public.sdk)
- Here is the step based on the AgainAAX example:
    - In the cpp file againaax.cpp, you can define the plug-in properties : IO audio, product ID, ...
    - On Windows, copy built linker output again_aax.aaxplugin to "c:\Program Files\Common Files\Avid\Audio\Plug-Ins\again_aax.aaxplugin\Contents\x64" (the debug build does this automatically, but needs appropriate access rights (Administrator rights of your visual))
    - On OSX, copy built bundle build/Debug/again.aaxplugin to "/Library/Application Support/Avid/Audio/Plug-Ins"
- A developer version of Pro Tools is needed to load the plug-in, the release version of Pro Tools requires plug-ins to be Pace-signed (PACE Anti-Piracy Inc.: <https://www.ilok.com>)
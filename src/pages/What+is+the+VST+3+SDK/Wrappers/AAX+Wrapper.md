>/ ... / [AAX, AUv3 and AU Wrappers](Index.md)
>
># VST 3 - AAX Wrapper

**On this page:**

[[_TOC_]]

---

## Introduction

Helper Class wrapping a **VST 3** plug-in to an **AAX** plug-in.

The **VST SDK** includes a helper class that wraps a **VST 3** audio processor and edit controller into an **AAX** plug-in.

## How does it work?

 - Check the AGainAAX example.
 - For more information on how to get the AAX SDK, you can visit the [Avid Technology AAX SDK page](https://developer.avid.com/aax).
 - AAX SDK 2.7 or higher is expected in folder *external.avid.aax* (located at the same level as the folder *public.sdk*).

- Here is the step based on the AGainAAX example:
  - In the cpp file *againaax.cpp*, you can define the plug-in properties: IO audio, product ID, ...
  - On Windows, copy built linker output again_aax.aaxplugin to "*C:\Program Files\Common Files\Avid\Audio\Plug-Ins\again_aax.aaxplugin\Contents\x64*" (the debug build does this automatically, but needs appropriate access rights (Administrator rights of your visual)).
  - On OSX, copy built bundle *build/Debug/again.aaxplugin* to "*/Library/Application Support/Avid/Audio/Plug-Ins*".

- AAX plug-ins must be digitally signed with [PACE Anti-Piracy](https://paceap.com/code-signing-platform/)'s signing tools before they can be used in a commercial version of Pro Tools.
- To test the plug-in without signing it, you can use a special version of Pro Tools: **Pro Tools Developer**, which could requested here: https://developer.avid.com/aax.
- A [iLok](https://www.ilok.com) as an [Avid](https://my.avid.com) account is required for running Pro Tools and have access to the AAX SDK.

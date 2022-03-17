/ [VST Home](../Index.md)

## What is the VST 3 SDK?

---

### VST 3 SDK explained

The **VST 3** SDK (Virtual Studio Technology Software Development Kit) is a collection of software development tools included in one package. This allows plug-in developers to create plug-ins in **VST 3** format and host developers to load **VST 3** plug-ins into a DAW or audio editor.

### What is included

The **VST 3** SDK package contains:

---

**The VST 3 API**

This is a **C++ interface** defining how a **VST 3** plug-in communicates with a host and vice versa. The heart of **VST 3**.

Check the folder *"pluginterfaces/vst"* of the SDK!

---

**VST 3 Implementation Helper Classes**

Some helper classes are provided, implementing some **VST 3** interfaces for hosting and for creating **VST 3** plug-ins. Simply derived your plug-in C++ classes from these helper classes.

<img 
    style="display: block; 
           margin-left: auto;
           margin-right: auto;
           width: 50%;
           filter: drop-shadow(10px 10px 10px #aaaaaa);"
    src="../resources/what_is_1.png">
</img>

Check the folder **"public.sdk"** of the SDK!

---

### [AAX, AUv3, AU and VST 2 wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md)

These wrappers allows you to create versions of your **VST 3** plug-in in other plug-in formats with minimum effort:
- [AAX](http://apps.avid.com/aax-portal/) format used by Pro Tools®
- [AUv3](https://developer.apple.com/documentation/audiotoolbox) and **AU** (Audio Unit) on Apple platform
- **VST 2** ([deprecated](https://www.steinberg.net/en/newsandevents/news/newsdetail/article/vst-2-coming-to-an-end-4727.html))

Check the folder *"public.sdk/source/vst/aaxwrapper"* of the SDK!

### [VST 3 Plug-ins Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md)

The SDK includes some Plug-ins implementation examples. The Legendary **AGain** and **ADelay**, thanks Paul Kellet the Open-source **mda** Plug-ins, a basic "Note Expression Synth" supporting "**Note Expression Event**", an example of **pitchnames** support Plug-in, a **VST3 Host Checker** which checks if a host is VST3 compliant and more...

## Table Styling in Markdown

<img 
    style="display: block;
           float: left;
           margin-left: auto;
           margin-right: auto;
           width: 45%;
           filter: drop-shadow(10px 10px 10px #aaaaaa);"
    src="../resources/what_is_2.jpg">
</img>
<img 
    style="display: block;
           float: right;
           margin-left: auto;
           margin-right: auto;
           width: 45%;
           filter: drop-shadow(10px 10px 10px #aaaaaa);"
    src="../resources/what_is_3.jpg">
</img>
<img 
    style="display: block;
           float: left;
           margin-left: auto;
           margin-right: auto;
           width: 45%;
           filter: drop-shadow(10px 10px 10px #aaaaaa);"
    src="../resources/what_is_4.jpg">
</img>

<img 
    style="display: block;
           float: right;
           margin-left: auto;
           margin-right: auto; 
           width: 45%;
           filter: drop-shadow(10px 10px 10px #aaaaaa);"
    src="../resources/what_is_5.jpg">
</img>

Check the folder *"public.sdk/samples/vst"* of the SDK!
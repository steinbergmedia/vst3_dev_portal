>/ [VST Home](../)
>
># What is the VST 3 SDK?

**On this page:**

[[_TOC_]]

---

## VST 3 SDK explained

The **VST 3 SDK** (Virtual Studio Technology Software Development Kit) is a collection of software development tools included in one package. This allows plug-in developers to create plug-ins in **VST 3** format and host developers to load **VST 3** plug-ins into a DAW or audio editor.

## What is included

The **VST 3 SDK** package contains:

### The VST 3 API

This is a **C++ interface** defining how a **VST 3** plug-in communicates with a host and vice versa. The heart of **VST 3**.

>Check the folder *"pluginterfaces/vst"* of the SDK!

### VST 3 Implementation Helper Classes

Some helper classes are provided, implementing some **VST 3** interfaces for hosting and for creating **VST 3** plug-ins. Simply derived your plug-in C++ classes from these helper classes.

![what_if_1](../../resources/what_is_1.png)

>Check the folder *"public.sdk"* of the SDK!

## [VST 3 Plug-ins Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md)

The SDK includes some Plug-ins implementation examples.

## [VST 3 Plug-in Test Host](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md)

The SDK provides a test application called **VST3PluginTestHost** for Apple macOS X (x86_64/M1) and Microsoft Windows (64bits).

## [VST 3 Project Generator](../What+is+the+VST+3+SDK/Project+Generator.md)

This open source application (Win/macOS) allows you to generate easily a new **VST 3** plug-in project by just entering in a GUI some parameters.

## [Validator command line](../What+is+the+VST+3+SDK/Validator.md)

The ***validator*** is a small command line host application (source code included) which can be used to check your plug-in for **VST 3** conformity.

## [AudioHost](../What+is+the+VST+3+SDK/AudioHost.md)

Simple cross-platform (only tested on Linux) host application allowing you to register a **VST 3** plug-in with Jack Server.

## [EditorHost](../What+is+the+VST+3+SDK/EditorHost.md)

Simple cross-platform (Win/macOS/Linux) host application allowing you to open the editor of a **VST 3** plug-in.

## [VST 3 Inspector](../What+is+the+VST+3+SDK/VST3Inspector.md)

Simple cross-platform (Win/macOS/Linux) host application, built with VSTGUI, which scans the **VST 3** Folder, collects information from the factory about each **VST 3** plug-in and display it in its UI.

## [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md)

This is a user interface toolkit mainly for audio plug-ins (VST, AudioUnit, etc). Based on the XML definition of the plug-in UI, **VSTGUI** includes an embedded editor (UIDescription Editor) which allows the developer to create a plug-in UI just by drag & drop of the UI element.

## [AAX, AUv3, AU and VST 2 wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md)

These wrappers allow you to create versions of your **VST 3** plug-in in other plug-in formats with minimum effort.

## [iOS Inter-App Audio support](../What+is+the+VST+3+SDK/iOS+Inter-App+Audio+support.md)

iOS InterApp-Audio application out of your **VST 3** plug-in

## [VST 3 Licensing](../VST+3+Licensing/Index.md)

Please sign this **Steinberg VST 3 Plug-In SDK Licensing Agreement** if you want to develop, release or host **VST 3** plug-Ins.

## System requirements

| Operating System                  | Architecture                  | Compiler              | Notes                             |
| --------------------------------- | ----------------------------- | --------------------- | --------------------------------- |
| Windows 11                        | x86, x86_64, arm64, arm64EC                   | MSVC 2022  |                                   |
| Windows 8.1 -10                        | x86, x86_64                   | MSVC 2019, MSVC 2022  |                                   |
| macOS 10.13 - 12                  | x86, x86_64, Apple Silicon    | Xcode 10 - 13.3       |                                   |
| iOS 13 - 15                       | arm64                         | Xcode 11 - 13.3       |                                   |
| Linux - Raspberry Pi OS (Buster)  | arm32                         | GCC 8.3 and higher    | Visual Studio Code                |
| Linux - Ubuntu 22.04 LTS          | x86, x86_64                   | GCC 11.2 and higher   | Visual Studio Code, Qt Creator    |
| Linux - Ubuntu 20.04 LTS          | x86, x86_64                   | GCC 8.3 and higher    | Visual Studio Code, Qt Creator    |

## [Download link](../Getting+Started/Links.md)

Important links you will need for working with **VST 3**

## [Change history](../Versions/Index.md)

All released versions of the **VST 3 SDK** with changes and dates.

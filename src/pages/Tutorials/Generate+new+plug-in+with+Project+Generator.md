>/ [VST Home](../) / [Tutorials](Index.md)
>
># Generate a new plug-in with the Project Generator App

**On this page:**

[[_TOC_]]

---

## Goal

This tutorial explains how to create a new audio plug-in by using the ***[VST 3 Project Generator](../What+is+the+VST+3+SDK/Project+Generator.md)*** included in the **VST 3 SDK** and how to add some basic features.

The artifact will be an audio plug-in that can compute a gain to an audio signal and can be loaded into VST 3 hosts like **Cubase**, **WaveLab**, ...

---

## Part 1: Getting and installing the VST 3 SDK

For downloading the SDK, see the section "[How to set up my system for VST 3](../Getting+Started/How+to+setup+my+system.md)".

You have the following possibilities to start a new project:

- You can use the [**helloworld** template](Creating+a+plug-in+from+the+Helloworld+template.md) included in the **VST 3 SDK** and duplicate the folder into a new folder. Adapt each file where the comment mentions it.
- Or, which is **easier** and **recommended**, you can use the [**VST 3 Project Generator**](../What+is+the+VST+3+SDK/Project+Generator.md) application included in the **VST 3 SDK**. The following steps show how to use it.

---

## Part 2: Using the [VST 3 plug-in **Project Generator** application](../What+is+the+VST+3+SDK/Project+Generator.md)

The [**VST3 Project Generator**](../What+is+the+VST+3+SDK/Project+Generator.md) application included in the **VST 3 SDK**  is available for Windows and for macOS.

Start the application located in the *VST3_Project_Generator* folder of the **VST 3 SDK**.

Check that the **Preferences** tab has the required information: see [Setting the Preferences](../What+is+the+VST+3+SDK/Project+Generator.md#setting-the-preferences).

In the **Create Plug-in Project** tab you have to enter information about the plug-in that you want create:

![tutorials_4](../../resources/tutorials_4.png)

Check the [Create Plug-in Project](../What+is+the+VST+3+SDK/Project+Generator.md#setting-and-creating-a-plug-in-project) tab of the [VST 3 Project Generator](../What+is+the+VST+3+SDK/Project+Generator.md) dialog for more detailed documentation.

Once you have entered all information, click **Create**. A script is started which creates a project with updated files in the Output directory. After this step, the IDE ([Visual Studio](https://visualstudio.microsoft.com/de/) or [XCode](https://developer.apple.com/xcode/)) is launched.

Compile the project and test your new plug-in. The plug-in is created in the *Output Directory*, in order to make it visible to a **VST 3** host you may have to copy or symbolic-link it to the official **VST 3** [Locations / Format](../Technical+Documentation/Locations+Format/Index.md).

For example, if you chose **Audio Effect** as Type, a simple Stereo→Stereo plug-in is created.

A good way to understand how a **VST 3** plug-in works is to add breakpoints in each function in the processor and controller files:

``` c++
tresult PLUGIN_API MyPluginController::initialize (FUnknown*context);
tresult PLUGIN_API MyPluginController::terminate ();
//...
tresult PLUGIN_API MyPluginProcessor::initialize (FUnknown*context);
//...
```

and start a **VST 3** host from the debugger.

---

That´s it, now you could start to code, see next tutorial [Code your first plug-in](Code+your+first+plug-in.md).

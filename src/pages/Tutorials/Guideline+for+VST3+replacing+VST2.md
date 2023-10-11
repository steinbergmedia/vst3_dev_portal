>/ [VST Home](../) / [Tutorials](Index.md)
>
># Guideline for replacing a VST 2 plug-in by a VST 3 plug-in

**On this page:**

[[_TOC_]]

---

## Goal

Here, you can find some informations about how to write a **VST 3** version of a plug-in which already exists as **VST 2** version.
How to guaranty that a Host will correctly replace the old **VST 2** by the new **VST 3** version of your plug-in.

For a **VST 3** Host the important information is the UID of your (processor) plug-in, with this information it will find the correct **VST 3** version to use.

2 scenarios are possible: The **VST 3** and the **VST 2** version of your plug-in have the same UID or not.

---

## VST 2 and VST 3 version of your Plug-in have the same UID

It is possible to reuse for a **VST 3** plug-in the same generated UID of a **VST 2** version (based on 4 characters + its name), this should work with most **VST 3** Hosts. Check the function which generates a **VST 3** UID from a **VST 2** UID [here](../FAQ/Compatibility+with+VST+2.x+or+VST+1.md#q-how-can-i-update-my-vst-2-version-of-my-plug-in-to-a-vst-3-version-and-be-sure-that-cubase-will-load-it-instead-of-my-old-one) and reuse this value as UID for the **VST 3** plug-in (processor component UID)

---

## VST 2 and VST 3 version of your Plug-in have not the same UID

For this use case since **VST 3 SDK** version 3.7.5 we have 2 possibilities for a **VST 3** plug-in to inform the Host about which **VST 2** plug-in it could replace:

### Using the [moduleinfo.json](../Technical+Documentation/VST+Module+Architecture/ModuleInfo-JSON.md) file

The **Compatibility** json array in the [moduleinfo.json](../Technical+Documentation/VST+Module+Architecture/ModuleInfo-JSON.md) allows to list the UIDs which could be replaced by the **VST 3** plug-in.

### Using the *IPluginCompatibility* interface

The plug-in should implement this interface (*pluginterfaces/base/iplugincompatibility.h*) when a [moduleinfo.json](../Technical+Documentation/VST+Module+Architecture/ModuleInfo-JSON.md) file cannot be used (when no bundle is available for example). Check [here](../Technical+Documentation/Change+History/3.7.5/ModuleInfo.md).

---

## Preset/Project compatibility VST 2 <-> VST 3

Check the FAQ [here](../FAQ/Compatibility+with+VST+2.x+or+VST+1.md#q-how-can-i-support-projects-which-were-saved-with-the-vst-2-version-of-my-plug-in) which shows how to use the helper function **VST3::tryVst2StateLoad** and read a **VST 2** state into a **VST 3** plug-in.

It is possible to write back for **VST 2** backward compatibility by using the helper function **VST3::writeVst2State** (*public.sdk/source/vst/utility/vst2persistence.h*).

---

## Parameters compatibility

**VST 2** was using index to identify parameter, **VST 3** uses an ID. It means that to be compatible the **VST 3** parameter **ID** should be kept to same index value as the **VST 2** one (starting from 0).

If the parameter range or behavior is not changed, previously parameter automation in host should be played back correctly.

If you change the meaning of a parameter (range, conversion normalized to plain value), it is recommanded to create a new **ID** for this parameter.

You could add in the **VST 3** plug-in a structure to your parameters by using [Unit](../Technical+Documentation/VST+3+Units/Index.md).

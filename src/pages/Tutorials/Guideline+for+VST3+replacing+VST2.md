>/ [VST Home](../) / [Tutorials](Index.md)
>
># Guideline for replacing a VST 2 plug-in by a VST 3 plug-in

**On this page:**

[[_TOC_]]

**Related pages:**

- [IRemapParamID](../Technical+Documentation/Change+History/3.7.11/IRemapParamID.md)
- [Compatibility with VST 2.x or VST 1](../FAQ/Compatibility+with+VST+2.x+or+VST+1.md)

---

## Goal

Here, you can find some informations about how to write a **VST 3** version of a plug-in that already exists as a **VST 2** version.
This guide will help ensure that a host correctly replaces the old **VST 2** version with the new **VST 3** version of your plug-in.

For a **VST 3** Host, the important information is the UID of your (processor) plug-in. With this information, it will find the correct **VST 3** version to use.

Two scenarios are possible: the **VST 3** and **VST 2** version of your plug-in have the same UID, or they do not.

---

## VST 2 and VST 3 version of your plug-in have the same UID

It is possible to reuse the same generated UID of a **VST 2** version for a **VST 3** plug-in (based on 4 characters + its name), this should work with most **VST 3** Hosts. Check the function which generates a **VST 3** UID from a **VST 2** UID [here](../FAQ/Compatibility+with+VST+2.x+or+VST+1.md#q-how-can-i-update-my-vst-2-version-of-my-plug-in-to-a-vst-3-version-and-be-sure-that-cubase-will-load-it-instead-of-my-old-one) and reuse this value as UID for the **VST 3** plug-in (processor component UID).

---

## VST 2 and VST 3 version of your plug-in have not the same UID

For this use case, since **VST SDK** version 3.7.5 we have two possibilities for a **VST 3** plug-in to inform the host about which **VST 2** plug-in it could replace:

### Using the [moduleinfo.json](../Technical+Documentation/VST+Module+Architecture/ModuleInfo-JSON.md) file

The **Compatibility** json array in the [moduleinfo.json](../Technical+Documentation/VST+Module+Architecture/ModuleInfo-JSON.md) allows listing the UIDs that could be replaced by the **VST 3** plug-in.

### Using the *IPluginCompatibility* interface

The plug-in should implement this interface (*pluginterfaces/base/iplugincompatibility.h*) when a [moduleinfo.json](../Technical+Documentation/VST+Module+Architecture/ModuleInfo-JSON.md) file cannot be used (when no bundle is available, for example). Check [here](../Technical+Documentation/Change+History/3.7.5/ModuleInfo.md).

---

## Preset/Project compatibility VST 2 <-> VST 3

Check the FAQ [here](../FAQ/Compatibility+with+VST+2.x+or+VST+1.md#q-how-can-i-support-projects-which-were-saved-with-the-vst-2-version-of-my-plug-in) which shows how to use the helper function **VST3::tryVst2StateLoad** to read a **VST 2** state into a **VST 3** plug-in.

It is possible to write back for **VST 2** backward compatibility by using the helper function **VST3::writeVst2State** (*public.sdk/source/vst/utility/vst2persistence.h*).

---

## Parameters compatibility

**VST 2** was using index to identify parameter, while **VST 3** uses an ID. To ensure compatibility, the **VST 3** parameter **ID** should be kept the same as the **VST 2** index value (starting from 0).

If this is not possible to keep the indexes and IDs the same, you can use the new **VST 3** API [IRemapParamID](../Technical+Documentation/Change+History/3.7.11/IRemapParamID.md), added in version 3.7.11, for remapping parameters between an older plug-in (VST 3 or VST2) to a newer one.

If the parameter range or behavior is not changed, previous parameter automation in host should be played back correctly.

If you change the meaning of a parameter (range, conversion from normalized to plain value), it is recommanded to create a new **ID** for this parameter.

You can add structure to your parameters in the **VST 3** plug-in by using [Unit](../Technical+Documentation/VST+3+Units/Index.md).

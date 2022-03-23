>/ [VST Home](/Index.md) / [Technical Documentation](../Index.md)
>
># Presets & Program Lists

**On this page:**

[[_TOC_]]

**Related pages:**

- [VST 3 Units](../VST+3+Units/Index.md)
- [Complex Plug-in Structures / Multi-timbral Instruments](../Complex+Structures/Index.md)

---

How presets and program lists are handled in **VST 3**

See [VST 3 Locations / Format](../Locations+Format/Index.md) **<- Link to be completed later** for preset format definition.

## Simple Plug-ins

![tech_doc_17](/resources/tech_doc_17.png)

For a simple plug-in, the data of a preset is nothing more than its state. In this case:


- It is the job of the host to manage the preset handling for the plug-in.

- The plug-in itself does not need to provide any means in its GUI for loading presets at all and it does not need to define any program lists.

- Factory presets must be installed as files at the required location (See [Preset Locations](../Locations+Format/Index.md)) **<- link to be completed later**.
>/ [VST Home](../../../index.md) / [Technical Documentation](../../Index.md)
>
># [3.6.12] Host Query Interface support

**On this page:**

[[_TOC_]]

---

## Introduction

Host callback interface for an edit controller: [Vst::IPlugInterfaceSupport](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IPlugInterfaceSupport.html)

- [host imp]
- [released: 3.6.12]
- [optional]

Allows a plug-in to ask the host if a given plug-in interface is supported/used by the host. It is implemented by the hostContext given when the component is initialized.

## Example

```
//------------------------------------------------------------------------
tresult PLUGIN_API MyPluginController::initialize (FUnknown* context)
{
    // ...
    FUnknownPtr<IPlugInterfaceSupport> plugInterfaceSupport (context);
    if (plugInterfaceSupport)
    {
        if (plugInterfaceSupport->isPlugInterfaceSupported (IMidiMapping::iid) == kResultTrue)
            // IMidiMapping is used by the host
    }
    // ...
}
```

See also [IPluginBase](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPluginBase.html)
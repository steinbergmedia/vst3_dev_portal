>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># \[3.6.5\] Channel Context Info

**On this page:**

[[_TOC_]]

---

## Introduction

Channel context interface: [Vst::IInfoListener](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1ChannelContext_1_1IInfoListener.html).

- \[plug imp\]
- [extends [IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html)]
- \[released: 3.6.5\]
- \[optional\]

Allows the host to inform the plug-in about the context in which the plug-in is instantiated, mainly channel based info (color, name, index, ...). Index can be defined inside a namespace (for example, index start from 1 to N for Type Input/Output Channel (Index namespace) and index start from 1 to M for Type Audio Channel).
As soon as the plug-in provides this [Vst::IInfoListener](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1ChannelContext_1_1IInfoListener.html) interface, the host will call setChannelContextInfos for each change occurring to this channel (new name, new color, new indexation, ...).

## Example

``` c++
//------------------------------------------------------------------------
tresult PLUGIN_API MyPlugin::setChannelContextInfos (IAttributeList* list)
{
    if (list)
    {
        // optional we can ask for the Channel Name Length
        int64 length;
        if (list->getInt (ChannelContext::kChannelNameLengthKey, length) == kResultTrue)
        {
            ...
        }
         
        // get the Channel Name where we, as Plug-in, are instantiated
        String128 name;
        if (list->getString (ChannelContext::kChannelNameKey, name, sizeof (name)) == kResultTrue)
        {
            ...
        }
  
        // get the Channel UID
        if (list->getString (ChannelContext::kChannelUIDKey, name, sizeof (name)) == kResultTrue)
        {
            ...
        }
         
        // get Channel Index
        int64 index;
        if (list->getInt (ChannelContext::kChannelIndexKey, index) == kResultTrue)
        {
            ...
        }
         
        // get the Channel Color
        int64 color;
        if (list->getInt (ChannelContext::kChannelColorKey, color) == kResultTrue)
        {
            uint32 channelColor = (uint32)color;
            String str;
            str.printf ("%x%x%x%x", ChannelContext::GetAlpha (channelColor),
            ChannelContext::GetRed (channelColor),
            ChannelContext::GetGreen (channelColor),
            ChannelContext::GetBlue (channelColor));
            String128 string128;
            Steinberg::UString (string128, 128).fromAscii (str);
            ...
        }
  
        // get Channel Index Namespace Order of the current used index namespace
        if (list->getInt (ChannelContext::kChannelIndexNamespaceOrderKey, index) == kResultTrue)
        {
            ...
        }
     
        // get the channel Index Namespace Length
        if (list->getInt (ChannelContext::kChannelIndexNamespaceLengthKey, length) == kResultTrue)
        {
            ...
        }
         
        // get the channel Index Namespace
        String128 namespaceName;
        if (list->getString (ChannelContext::kChannelIndexNamespaceKey, namespaceName, sizeof (namespaceName)) == kResultTrue)
        {
            ...
        }
  
        // get Plug-in Channel Location
        int64 location;
        if (list->getInt (ChannelContext::kChannelPluginLocationKey, location) == kResultTrue)
        {
            String128 string128;
            switch (location)
            {
                case ChannelContext::kPreVolumeFader:
                    Steinberg::UString (string128, 128).fromAscii ("PreVolFader");
                break;
                case ChannelContext::kPostVolumeFader:
                    Steinberg::UString (string128, 128).fromAscii ("PostVolFader");
                break;
                case ChannelContext::kUsedAsPanner:
                    Steinberg::UString (string128, 128).fromAscii ("UsedAsPanner");
                break;
                default: Steinberg::UString (string128, 128).fromAscii ("unknown!");
                break;
            }
        }
         
        // do not forget to call addRef () if you want to keep this list
    }
}
```

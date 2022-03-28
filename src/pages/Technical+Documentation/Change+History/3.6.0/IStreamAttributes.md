>/ [VST Home](/Index.md) / [Technical Documentation](/pages/Technical+Documentation/Index.md)
>
># [3.6.0] Preset Meta-Information

**On this page:**

[[_TOC_]]

---

## Introduction

Meta attributes of a stream: [Vst::IStreamAttributes](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IStreamAttributes.html)

- [host imp]
- [extends [IBStream](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IBStream.html)]
- [released: 3.6.0]
- [optional]

Interface to access preset meta information from stream, used, for example, in [setState](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponent.html#a77ac39bcc5c4b15818b1a87de2573805) in order to inform the plug-in about the current context in which the preset loading occurs(Project context or Preset load (see [StateType](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/namespaceSteinberg_1_1Vst_1_1StateType.html))) or used to get the full file path of the loaded preset (if available).

## Example

```
#include "pluginterfaces/base/ustring.h"
#include "pluginterfaces/vst/vstpresetkeys.h"
// ...
 
tresult PLUGIN_API MyPluginProcessor::setState (IBStream* state)
{
    FUnknownPtr<IStreamAttributes> stream (state);
    if (stream)
    {
        IAttributeList* list = stream->getAttributes ();
        if (list)
        {
            // get the current type (project/Default..) of this state
            String128 string;
            if (list->getString (PresetAttributes::kStateType, string, 128 * sizeof (TChar)) == kResultTrue)
            {
                UString128 tmp (string);
                char ascii[128];
                tmp.toAscii (ascii, 128);
                if (!strncmp (ascii, StateType::kProject, strlen (StateType::kProject)))
                {
                    // we are in project loading context...
                }
            }
 
            // get the full file path of this state
            TChar fullPath[1024];
            if (list->getString (PresetAttributes::kFilePathStringType, fullPath, 1024 * sizeof (TChar)) == kResultTrue)
            {
                // here we have the full path ...
            }
        }
    }
    //...read the state here.....
    return kResultTrue;
}
```
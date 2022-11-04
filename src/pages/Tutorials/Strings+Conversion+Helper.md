>/ [VST Home](../) / [Tutorials](Index.md)
>
># Strings Conversion Helper

**On this page:**

[[_TOC_]]

---

## Goal

The SDK provides some helpers functions to convert from **UTF16** (use in **VST 3** interfaces) to **UTF8** (used by std::string).

Here some code examples:

---

## Convert a String128 string to an UTF-8 string

``` c++
#include "public.sdk/source/vst/utility/stringconvert.h"

//...
FUnknownPtr<IHostApplication> hostApp (hostContext);
if (hostApp)
{
    Vst::String128 name;
    if (hostApp->getName (name) == kResultTrue)
    {
        // Here we convert a Vst::String128 to a std::string (UTF8)
        std::string str = VST3::StringConvert::convert (name);
        //...
    }
}
```

---

## Convert an UTF-8 string to a String128 string

``` c++
#include "public.sdk/source/vst/utility/stringconvert.h"

//...
std::string str ("My Title");
Vst::String128 vstStr;
VST3::StringConvert::convert (str, vstStr);
```

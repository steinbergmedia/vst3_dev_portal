>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># \[3.7.5\] Module Info and Plug-in Compatibility

**On this page:**

[[_TOC_]]

**Related pages:**

- [Moduleinfo](../../../Technical+Documentation/VST+Module+Architecture/ModuleInfo-JSON.md)
- [Compatibility with VST 2.x or VST 1](../../../FAQ/Compatibility+with+VST+2.x+or+VST+1.md)

---

## Introduction

A new [moduleinfo.json](../../../Technical+Documentation/VST+Module+Architecture/ModuleInfo-JSON.md) file added to the plug-in bundle (in the *Resources* folder) describes the contents of the plug-in in a [JSON5](http://json5.org) compatible format. This includes a compatibility list which allows, for example, a **VST 3** plug-in to replace a given **VST 2** plug-in (check [here](../../../FAQ/Compatibility+with+VST+2.x+or+VST+1.md), to learn how to create UID for old **VST 1**/**VST 2** plug-ins).

- \[plug imp\]
- \[released: 3.7.5\]

## Plug-in’s module info file: moduleinfo.json

Check [moduleinfo.json](../../../Technical+Documentation/VST+Module+Architecture/ModuleInfo-JSON.md) for more information about the content of this file.

## IPluginCompatibility

If the plug-in could not deliver the [moduleinfo.json](../../../Technical+Documentation/VST+Module+Architecture/ModuleInfo-JSON.md) because it is not organized as a bundle-like package, it is possible to add the new interface *IPluginCompatibility* to the plug-in factory.

>ⓘ **Note**\
If the compatibility feature is required, it is recommended to use either *moduleinfo.json* or *IPluginCompatibility*.

>ⓘ **Note**\
It is not recommended to implement *IPluginCompatibility* if you do not provide compatibility with any previous plug-in version. If you expose this object, the host expects you to provide compatibility information with it; otherwise, it is useless.

### Example

**In plugentry.cpp**:

``` c++
//------------------------------------------------------------------------
class PluginCompatibility : public FObject, public IPluginCompatibility
{
  public:
    //...
    tresult PLUGIN_API getCompatibilityJSON (IBStream* stream) override
    {
        // here plug-in with UID BD58B550F9E5634E9D2EFF39EA0927B1 could replace 
        // plug-in with UID AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA and
        // plug-in with UID BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
      /* write the JSON compatibility array into the stream
      [
          {
              "New": "BD58B550F9E5634E9D2EFF39EA0927B1",
              "Old": [
                  "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
                  "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
              ],
          }
      ]
      */
	    return kResultTrue;
    }
    //... 
};

//------------------------------------------------------------------------
static FUnknown* createCompatibilityInstance (void* context)
{
	return (IPluginCompatibility*)new PluginCompatibility;
}

//------------------------------------------------------------------------
BEGIN_FACTORY_DEF (stringCompanyName, stringCompanyWeb, stringCompanyEmail)

    //...
    DEF_CLASS2 (INLINE_UID_FROM_FUID(PluginCompatibilityUID),
				PClassInfo::kManyInstances,
				kPluginCompatibilityClass,
				stringPluginName,
				Vst::kDistributable,
				"",
				FULL_VERSION_STR,
				kVstVersionString,
				createCompatibilityInstance)
```

### Example of host implementation

Check function **void Validator::testModule** in public.sdk/samples/vst-hosting/validator/source/validator.cpp.

``` c++
plugCompatibility = factory.createInstance<IPluginCompatibility> (classInfo.ID ());
```

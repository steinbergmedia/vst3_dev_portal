>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># [3.6.5] Prefetchable

**On this page:**

[[_TOC_]]

---

## Introduction

Indicates if the plug-in supports prefetch (dynamically): [Vst::IPrefetchableSupport](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IPrefetchableSupport.html)

- [plug imp]
- [extends [IComponent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponent.html)]
- [released: 3.6.5]
- [optional]

The plug-in should implement this interface if it needs to dynamically change between prefetchable or not. By default (without implementing this interface), the host decides in which mode the plug-in is processed. For more info about the prefetch processing mode check the P[rocessModes::kPrefetch](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/namespaceSteinberg_1_1Vst.html#ae514554bd822c5370bf9496c70302e31a3b1caa5d658939c027cbb7759358a88a) documentation

## Example

``` c++
//------------------------------------------------------------------------
tresult PLUGIN_API myPlug::getPrefetchableSupport (PrefetchableSupport& prefetchable)
{
    prefetchable = kIsNeverPrefetchable;
 
    switch (myPrefetchableMode)
    {
        case 0: prefetchable = kIsNeverPrefetchable; break;
        case 1: prefetchable = kIsYetPrefetchable; break;
        case 2: prefetchable = kIsNotYetPrefetchable; break;
    }
    return kResultOk;
}
```

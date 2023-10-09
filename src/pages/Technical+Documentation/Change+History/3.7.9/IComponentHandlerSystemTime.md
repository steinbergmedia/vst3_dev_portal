>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># \[3.7.9\] Get Current SystemTime

**On this page:**

[[_TOC_]]

---

## Introduction

 Extended plug-in interface [IComponentHandler](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html) for an edit controller, [IComponentHandlerSystemTime](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandlerSystemTime.html) allows the plug-in to ask for the current systemTime (this should be the kind of time reference than the one used in ProcessContext::systemTime).

- \[host imp\]
- [extends [IComponentHandler](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html)]
- \[released: 3.7.9\]
- \[optional\]

## Example

``` c++
//--------------------------------------
// we are in the editcontroller:
  
int64 systemTime = 0;

FUnknownPtr<IComponentHandlerSystemTime> handlerSystemTime (componentHandler);
if (handlerSystemTime)
    handlerSystemTime->getSystemTime (systemTime);

```
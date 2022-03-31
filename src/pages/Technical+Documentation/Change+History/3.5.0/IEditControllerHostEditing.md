>/ [VST Home](../../../index.md) / [Technical Documentation](../../Index.md)
>
># [3.5.0] Enhanced Linked Parameters

**On this page:**

[[_TOC_]]

---

## Introduction

Parameter editing from host: [Vst::IEditControllerHostEditing](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditControllerHostEditing.html)

- [plug imp]
- [extends [IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html)]
- [released: 3.5.0]
- [optional]

This allows the host to start a parameter editing action which can generate other parameter changes (like linked parameters) and this in one session (between a beginEdit and endEdit).If this interface is implemented by the edit controller, and when performing edits from outside the plug-in (host / remote) of a not automatable, not read-only, and not hidden flagged parameter (kind of helper parameter), the host will start with a [beginEditFromHost](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditControllerHostEditing.html#a97cc85e97b22ff0d4fb9b5109a1a2bf2) before calling [setParamNormalized](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html#aded549c5b0f342a23dee18cc41ece6b8) and end with an [endEditFromHost](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditControllerHostEditing.html#a589c94be69d4ee5ed29cf62e437fecbb). Here the sequence that the host will call:

## Example

```
//------------------------------------------------------------------------
plugEditController->beginEditFromHost (id);
plugEditController->setParamNormalized (id, value);
plugEditController->setParamNormalized (id, value + 0.1);
// ...
plugEditController->endEditFromHost (id);
```

See also [IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html)
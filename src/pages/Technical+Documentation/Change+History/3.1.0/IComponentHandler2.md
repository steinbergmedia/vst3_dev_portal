>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># \[3.1.0\] Dirty State, Open Editor Request and UI Group Editing Support

**On this page:**

[[_TOC_]]

---

## Introduction

Improvement of the plug-in's integration in the host (dirty state, request Open Editor, group editing).

Extended host callback interface [Vst::IComponentHandler2](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler2.html) for an edit controller.

- \[host imp\]
- [extends [IComponentHandler](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html)]
- \[released: 3.1.0\]
- \[optional\]

## Dirty State Support

This allows the plug-in to tell the host that its internal state is dirty or not. If set to true, it means that after saving, there have been further changes, in addition to the parameter changes. In this case, the host should save before quitting.

``` c++
void MyPluginController::informHostAboutMyDirtyState (bool dirty)
{
    FUnknownPtr<IComponentHandler2> componentHandler2 (componentHandler);
    if (componentHandler2)
        componentHandler2->setDirty (dirty);
}
```

## Open Editor Request Support

Requesting the host to open the plug-in´s editor the next time it's possible. You should use this instead of showing an alert and blocking the program flow (especially on loading projects).

``` c++
void MyPluginController::requestHostToOpenEditor()
{
    FUnknownPtr<IComponentHandler2> componentHandler2 (componentHandler);
    if (componentHandler2)
        componentHandler2->requestOpenEditor ();
}
```

## UI Group Editing

This part handles parameter group editing from the plug-in UI. It wraps a set of IComponentHandler::beginEdit / Steinberg::Vst::IComponentHandler::performEdit / Steinberg::Vst::IComponentHandler::endEdit functions (see IComponentHandler) which should use the same timestamp in the host when writing automation. This allows for better synchronizing of multiple parameter changes at once.

### Examples of different use cases

``` c++
//--------------------------------------
// we are in the editcontroller...
// in case of multiple switch buttons (with associated ParamID 1 and 3)
// on mouse down:
hostHandler2->startGroupEdit ();
hostHandler->beginEdit (1);
hostHandler->beginEdit (3);
hostHandler->performEdit (1, 1.0);
hostHandler->performEdit (3, 0.0); // the opposite of paramID 1 for example
//....
// on mouse up:
hostHandler->endEdit (1);
hostHandler->endEdit (3);
hostHandler2->finishGroupEdit ();
//....
//....
//--------------------------------------
// in case of multiple faders (with associated ParamID 1 and 3)
// on mouse down:
hostHandler2->startGroupEdit ();
hostHandler->beginEdit (1);
hostHandler->beginEdit (3);
hostHandler2->finishGroupEdit ();
//....
// on mouse move:
hostHandler2->startGroupEdit ();
hostHandler->performEdit (1, x); // x the wanted value
hostHandler->performEdit (3, x);
hostHandler2->finishGroupEdit ();
//....
// on mouse up:
hostHandler2->startGroupEdit ();
hostHandler->endEdit (1);
hostHandler->endEdit (3);
hostHandler2->finishGroupEdit ();
```

See also [IComponentHandler](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html), [IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html)

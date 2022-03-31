>/ [VST Home](../../../index.md) / [Technical Documentation](../../Index.md)
>
># [3.0.0] Interfaces supported by the plug-in

**On this page:**

[[_TOC_]]

**Related pages**

- [[3.0.0] Interfaces supported by the host](../Change+History/3.0.0/Host+Interfaces.md)

---

List of interfaces supported/implemented by the plug-in in VST 3.0.0

## [IComponent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponent.html)

Component base interface.

- [plug imp]
- [released: 3.0.0]
- [mandatory]

This is the basic interface for a VST component and must always be supported. It contains the common parts of any kind of processing class. The parts that are specific to a media type are defined in a separate interface. An implementation component must provide both the specific interface and [IComponent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponent.html).

See also [IPluginBase](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPluginBase.html)

## [IAudioProcessor](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html)

Audio processing interface.

- [plug imp]
- [extends IComponent]
- [released: 3.0.0]
- [mandatory]

This interface must always be supported by audio processing plug-ins.

## [IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html)

Edit controller component interface.

- [plug imp]
- [released: 3.0.0]
- [mandatory]

The controller part of an effect or instrument with parameter handling (export, definition, conversion...).

See also [IComponent::getControllerClassId](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponent.html#a8aa65685068ad033af57b1497926b689), [IMidiMapping](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IMidiMapping.html)

## [IConnectionPoint](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IConnectionPoint.html)

Connect a component with another one.

- [plug imp]
- [host imp]
- [released: 3.0.0]
- [mandatory]

This interface is used for the communication of separate components. Note that some hosts will place a proxy object between the components so that they are not directly connected.

See also [Communication between the components](../../API+Documentation/Index.html#communication-between-the-components)

## [IUnitInfo](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IUnitInfo.html)

Edit controller extension to describe the plug-in structure.

- [plug imp]
- [extends [IEditController](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html)]
- [released: 3.0.0]
- [optional]

[IUnitInfo](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IUnitInfo.html) describes the internal structure of the plug-in.

The root unit is the component itself, so getUnitCount must return 1 at least.
The root unit id has to be 0 (kRootUnitId).
Each unit can reference one program list - this reference must not change.
Each unit that uses a program list references one program of the list.
See also [VST 3 Units](../../VST+3+Units/Index.md), [IUnitHandler](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IUnitHandler.html)

## [IProgramListData](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IProgramListData.html)

Component extension to access program list data.

- [plug imp]
- [extends [IComponent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponent.html)]
- [released: 3.0.0]
- [optional]

A component can support program list data via this interface or/and unit preset data ([IUnitData](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IUnitData.html)).

See also [IUnitData](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IUnitData.html), [Complex Plug-in Structures / Multi-timbral Instruments](../../Complex+Structures/Index.md)

## [IUnitData](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IUnitData.html)

Component extension to access unit data.

- [plug imp]
- [extends IComponent]
- [released: 3.0.0]
- [optional]

A component can support unit preset data via this interface or program list data ([IProgramListData](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IProgramListData.html)).

See also [Presets & Program Lists](../../Presets+Program+Lists/Index.md)

## [IPlugView](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugView.html)

Plug-in definition of a view.

- [plug imp]
- [released: 3.0.0]

### Sizing of a view

After the creation of a IPlugView, the plug-in must make sure that it returns the correct size if the host asks for it (IPlugView::getSize ()).

Usually, the size of a plug-in view is fixed. But both the host and the plug-in can cause a view to be resized:

- **Host**: If IPlugView::canResize () returns **kResultTrue**, the host will set up the window so that the user can resize it. While the user resizes the window, IPlugView::checkSizeConstraint () is called, allowing the plug-in to change the size to a valid supported rectangle size. The host then resizes the window to this rect and has to call IPlugView::onSize ().

- **Plug-in**: The plug-in can call IPlugFrame::resizeView () and cause the host to resize the window.
Afterwards, in the same callstack, the host has to call IPlugView::onSize () if a resize is needed (size was changed).

>ⓘ **Note**<br>
>Note that if the host calls IPlugView::getSize () before calling IPlugView::onSize () (if needed), it will get the old size, not the current one!

Here the calling sequence:

- plug-in->host: IPlugFrame::resizeView (newSize)
- host->plug-in (optional): IPlugView::getSize () returns the currentSize (not the newSize!)
- host->plug-in: if newSize is different from the current size: IPlugView::onSize (newSize)
- host->plug-in (optional): IPlugView::getSize () returns the newSize

>ⓘ **Note**<br>
>Please only resize the platform representation of the view when IPlugView::onSize () is called.

### Keyboard handling

The plug-in view receives keyboard events from the host. A view implementation must not handle keyboard events by the means of platform callbacks, but let the host pass them to the view. The host depends on a proper return value when [IPlugView::onKeyDown](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugView.html#a759b576f046e699c84dc07d579600b1b) is called, otherwise the plug-in view may cause a malfunction of the host's key command handling.

See also [IPlugFrame](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugFrame.html), [Platform UI Types](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/group__platformUIType.html)
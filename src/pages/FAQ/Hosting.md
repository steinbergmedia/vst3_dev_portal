>/ [VST Home](../) / [Frequently Asked Questions](Index.md)
>
># Hosting

[[_TOC_]]

---

## Q: What is the purpose of *restartComponent*? Is it generally OK to return *kNotImplemented*?

By default the host could return *kNotImplemented* if it does not implement a specific flag. But it is highly recommended to implement these flags:

- kLatencyChanged
- kParamValuesChanged
- kParamTitlesChanged
- kIoChanged

## Q: Can the host expect ClassID to be globally unique or should it expect different modules to reuse class IDs?

You must treat the Class ID as globally unique.
If it happens that the same classID is already registered by the host then the host could ignore it or try to compare the version (string based) and keep the newest version (done by Cubase for example). It should be only one VST3 plugin registered in the host at a time. The host could decide to show the duplicate classID to the user if wanted.

## Q: Do all version updates for a certain plugin require a new classID?

No, normally a new version should and could replace directly an older version by using the same classID, see previous question. This is the correct way to do it.

It may happen that some plugins will use new classIDs. If these plugins are done to replace older versions, the new [Moduleinfo](../Technical+Documentation/VST+Module+Architecture/ModuleInfo-JSON.md) or *IPluginCompatibility* interface, if used by the plug-in, allows the host to select the new plug-in as replacement for an older one (if not present or not) when loading a project using an old version.

## Q: Should the host support plugins that don't have *EditController* (*IComponent::getControllerClassId*() fails or subsequent *IPluginFactory::createInstance*() fails)?

The host have to check that the *IAudioProcessor* implements the *IEditController* interface too. A plug-in can implement both interfaces in the same object (Single Component Effect)

See [Here](../Technical+Documentation/API+Documentation/Index.md#creation-and-initialization-from-host-point-of-view) for more info.

The Host should be able to handle the case when no *IEditController* is available.

## Q: Should the host support plugins that don't have IPlugView (*IEditController::createView*() fails or *IPlugView::isPlatformTypeSupported*() returns false)?

A plug-in don't need to have a custom editor. See the examples in the SDK. Many of them don't have a custom editor. This was true for VST2 too. So the host have to support these plugins without dedicated UI, but it could provide a generic UI.

## Q: What is allowed to change for a given parameter (*ParamID*)? Name, number of steps, automatable or not, which unit it is part of?

See [Here](../Technical+Documentation/Parameters+Automation/Index.md#parameter-titles-default-values-or-flags-have-changed).

## Q: Is it allowed to change any/all the ParameterFlags on *kParamTitlesChanged*?

Yes, this is the way it should be done: *kParamTitlesChanged* => recheck title-unit, stepcount, default value and flags.

## Q: Is ParameterInfo::stepCount only allowed to be changed on *kReloadComponent*?

No see previous question.

## Q: Can the host get away with returning kNotImplemented for *restartComponent*(*kReloadComponent*)?

It is allowed for a host to return *kNotImplemented* if it does not support it! The plugin has then to react accordingly.

## Q: Do it is common among big / important plugins to rely on *kReloadComponent* for normal usage?

No, this is not the typical use case. But could be used by plugins changing its internal-external representation (change of parameter´s count, number of IO...). You could in a first host implementation postponed it to a future version.

## Q: In what ways (if any) can units change? Number of units, names of units, which and parameters buses belong to which units?

Unit names can change when restartComponent is called with *kParamTitlesChanged*.
When restartComponent is called with *kReloadComponent* then the whole structure should be regenerated.

## Q: IPlugViewContentScaleSupport - could / should this be used to set individual zoom levels for the GUI of specific plugins / instances, or should it only be used to convey OS scaling level (like in the editorhost example)?

Theoretically it is possible to use this for individual zoom levels, but most plug-ins won't work like this and on macOS many plug-ins don't implement this interface at all (or ignore it).

## Q: If it's only intended to convey OS-scale factor, then why an extra interface when the plugin can get the scale factor from the OS?

The design of this interface was done before it was possible on Windows for a plug-in to access the OS-scale.

But it could be used by the host to try to rescale a given plug-in or all plug-in. This is what is used in Cubase by changing the overall App scaling in the preference up to 50% to the system scale.

## Q: In the examples that implement host-specific interfaces, _FUnknown::addRef()_ and _FUnknown::release()_ tends to be implemented as a no-op, _e.g. {return 1000;}_ - this seems safer as the plugin can't delete or leak objects that live in the host. Is there any case when the host needs to implement true _addRef()_ and _release()_, which actually control the lifetime of the object?

You can only do this reference count no-ops for objects that are alive the whole lifetime of the host and will always outlive the plug-ins.

## Q: What should the host do if a plug-in does not call _ComponentHandler::restartComponent()_ from the main/UI thread?

You could report directly to the developer of this plug-in about this wrong behaviour, restartComponent has to be called from UI Thread! As security fallback the host could postpone this call in the UI Thread and handles it in the next UI idle.

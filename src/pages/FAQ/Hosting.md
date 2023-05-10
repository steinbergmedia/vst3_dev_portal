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

---

## Q: Can the host expect ClassID to be globally unique or should it expect different modules to reuse class IDs?

You must treat the Class ID as globally unique.
If it happens that the same classID is already registered by the host then the host could ignore it or try to compare the version (string based) and keep the newest version (done by Cubase for example). It should be only one **VST 3** plug-in registered in the host at a time. The host could decide to show the duplicate classID to the user if wanted.

---

## Q: Do all version updates for a certain plug-in require a new classID?

No, normally a new version should and could replace directly an older version by using the same classID, see previous question. This is the correct way to do it.

It may happen that some plug-ins will use new classIDs. If these plug-ins are done to replace older versions, the new [Moduleinfo](../Technical+Documentation/VST+Module+Architecture/ModuleInfo-JSON.md) or *IPluginCompatibility* interface, if used by the plug-in, allows the host to select the new plug-in as replacement for an older one (if not present or not) when loading a project using an old version.

---

## Q: Should the host support plug-ins that don't have *EditController* (*IComponent::getControllerClassId*() fails or subsequent *IPluginFactory::createInstance*() fails)?

The host have to check that the *IAudioProcessor* implements the *IEditController* interface too. A plug-in can implement both interfaces in the same object (Single Component Effect)

See [Here](../Technical+Documentation/API+Documentation/Index.md#creation-and-initialization-from-host-point-of-view) for more info.

The Host should be able to handle the case when no *IEditController* is available.

---

## Q: Should the host support plug-ins that don't have IPlugView (*IEditController::createView*() fails or *IPlugView::isPlatformTypeSupported*() returns false)?

A plug-in don't need to have a custom editor. See the examples in the SDK. Many of them don't have a custom editor. This was true for **VST 2** too. So the host have to support these plug-ins without dedicated UI, but it could provide a generic UI.

---

## Q: What is allowed to change for a given parameter (*ParamID*)? Name, number of steps, automatable or not, which unit it is part of?

See [Here](../Technical+Documentation/Parameters+Automation/Index.md#parameter-titles-default-values-or-flags-have-changed).

---

## Q: Is it ok to change any/all the ParameterFlags on *kParamTitlesChanged*?

Yes, this is the way it should be done: *kParamTitlesChanged* => recheck title-unit, stepcount, default value and flags.

---

## Q: Is ParameterInfo::stepCount only allowed to be changed on *kReloadComponent*?

No, see previous question.

---

## Q: Some plug-ins have parameters that are not automatable (*kCanAutomate*). They are calling beginEdit/performEdit/endEdit when users manipulate them via the GUI. Is the host supposed to react to the performEdit by sending the value to the process call of the IAudioProcessor?

Yes, the host must transfer the parameter change from the controller to the processor.
The information automatable (*kCanAutomate*) is only there to allow the host and users to create an associated automation track for this parameter.

---

## Q: Can the host get away with returning kNotImplemented for *restartComponent*(*kReloadComponent*)?

A host is permitted to return *kNotImplemented* if it does not support it! The plug-in then has to react accordingly.

---

## Q: Is it common for big / important plug-ins to rely on *kReloadComponent* for normal usage?

No, this is not the typical use case. However, it could be used by plug-ins changing its internal-external representation (change of parameter´s count, number of IO...). For an initial host implementation, you can postpone it until a future version is released.

---

## Q: In what ways (if any) can units change, in terms of the number or names of units, the allocation of parameter buses to units, etc.?

Plug-in Unit names can change when restartComponent is called with *kParamTitlesChanged*.
When restartComponent is called with *kReloadComponent* then the whole structure should be regenerated.

---

## Q: IPlugViewContentScaleSupport - could / should this be used to set individual zoom levels for the GUI of specific plug-ins / instances, or should it only be used to convey OS scaling level (like in the editorhost example)?

Theoretically it is possible to use this for individual zoom levels, but most plug-ins won't work like this and on macOS many plug-ins don't implement this interface at all (or ignore it).

---

## Q: If it's only intended to convey OS-scale factor, then why an extra interface when the plug-in can get the scale factor from the OS?

The design of this interface was done before it was possible on Windows for a plug-in to access the OS-scale.

But this interface could be used by the host to try to rescale a given plug-in or all plug-ins. This is what is used in Cubase by changing the overall App scaling in the preference up to 50% to the system scale.

---

## Q: In the examples that implement host-specific interfaces, _FUnknown::addRef()_ and _FUnknown::release()_ tend to be implemented as a no-op, _e.g. {return 1000;}_ - this appears to be safer as the plug-in cannot delete or leak objects that live in the host. Is there any case when the host needs to implement true _addRef()_ and _release()_, which actually control the lifetime of the object?

You can only use these reference count no-ops for objects that are alive during the entire lifetime of the host and that will outlive the plug-ins.

---

## Q: What should the host do if a plug-in does not call _ComponentHandler::restartComponent()_ from the main/UI thread?

You can report the wrong behavior of the plug-in to the developer. *restartComponent* has to be called from UI Thread. As a security fallback, the host could postpone this call in the UI Thread and handle it in the next UI idle phase.

---

## Q: Some plug-ins return kResultFalse when the host calls *setComponentState*. Should the host just ignore the returned result code?

Yes, just ignore the result in this case. However, we recommend to inform the plug-in developer about this issue.

>/ [VST Home](../) / [Frequently Asked Questions](Index.md)
>
># Persistence

[[_TOC_]]

---

## Q: How does persistence work?

An instantiated plug-in often has state information that must be saved in order to properly re-instantiate that plug-in at a later time. A **VST 3** plug-in has two states which are saved and reloaded: its component state and its controller state.

The sequence of actions for saving is:

- component->getState (compState)
- controller->getState (ctrlState)

The sequence of actions for loading is:

- component->setState (compState)
- controller->setComponentState (compState)
- controller->setState (ctrlState)

In the latter sequence you can see that the controller part will receive the component state. This allows the 2 parts to synchronize their states.

## Q: What's the difference between IEditController::setComponentState and IEditController::setState?

After a preset is loaded, the host calls [Vst::IEditController::setComponentState](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html#a4c2e1cafd88143fda2767a9c7ba5d48f) and [Vst::IComponent::setState](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponent.html#a77ac39bcc5c4b15818b1a87de2573805). Both delivering the same information. [Vst::IEditController::setState](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html#a77ac39bcc5c4b15818b1a87de2573805) is called by the host so that the plug-in is able to update its controller dependent parameters, e.g. position of scroll bars. Prior to this, there should have been a call by the host to [Vst::IEditController::getState](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IEditController.html#a10db03106be8ba89d23859fa6be5d9f6), where the plug-in writes these various parameters into the stream.

See also [Q: How does persistence work?](#q-how-does-persistence-work)

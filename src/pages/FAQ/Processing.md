>/ [VST Home](../../index.md) / [Frequently Asked Questions](../FAQ/Index.md)
>
># Processing

[[_TOC_]]

---

## Q: How does Audio Processing Bypass work?

In order to implement audio process bypassing, the plug-in can export a parameter which is additionally and exclusively flagged as having the attribute kIsBypass. When the user activates the plug-in bypass in the host, like all parameter changes, this is sent as part of the parameter data passed to the [IAudioProcessor::process](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html#a6b98eb31cf38ba96a28b303c13c64e13) method.

The implementation of the bypass feature is entirely the responsibility of the plug-in:

The [IIAudioProcessor::process](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html#a6b98eb31cf38ba96a28b303c13c64e13) method will continue to be called. The plug-in must take care of artifact-free switching (ramping/fade-in/fade-out, parallel processing or algorithm changes) and must also provide a delayed action if the plug-in has a latency and be sure that the output buffers are providing a copy of the input buffers (eventually delayed). No need to copy the input buffers to the output buffers when the pointers are the same and the plug-in has no latency!

This is the choice of the plug-in to handle/process the bypass (like any other parameters) sample accurate (by using the sampleOffset of the parameter change) or audio block based (not recommended when the audio block length is too large > 1024).

During bypass the process is still called, but if not, for some reason, the host may call a flush (using process call with null audio buffer).

>ⓘ **Note**\
The plug-in needs to save in its state the bypass parameter like any other parameters.

Q: Must the host deliver valid initialized Audio buffers if the associated bus is deactivated?

In a correctly implemented host, if an input or output bus exists in the host, and it has become disconnected from the plug-in, the plug-in will receive disconnection information (bus activation).

Additionally, a plug-in with a disconnected input bus will continue to receive default silence buffers, just as a plug-in with a disconnected output bus will continue to receive default nirvana buffers. When these deactivated busses are the last busses (for input or output), the host could not provide associated [AudioBusBuffers](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1AudioBusBuffers.html), in this case the plug-in should check [numInputs](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessData.html#a852a74fc4e461ef086bac048313d2de9) and [numOutputs](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessData.html#a1338255f88bad5cf4fb714c71f92b61a) and doesn't process these busses.

## Q: Can the maximum sample block size change while the plug-in is processing?

The max. sample block size ([maxSamplesPerBlock](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessSetup.html#a41cd06a0c942a1b3f283092b893d0de3)) can change during the lifetime of a plug-in, but NOT while the audio component is active. Therefore max. sample block size ([maxSamplesPerBlock](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessSetup.html#a41cd06a0c942a1b3f283092b893d0de3)) can never change during or between processing calls while the plug-in is active.

If the host changes the maximum sample block size it specifically calls the following:

```
Steinberg::Vst::IAudioProcessor::process (...);
Steinberg::Vst::IAudioProcessor::setProcessing (false);
Steinberg::Vst::IAudioProcessor::setActive (false);
 
Steinberg::Vst::IAudioProcessor::setupProcessing (...);
 
Steinberg::Vst::IAudioProcessor::setActive (true);
Steinberg::Vst::IAudioProcessor::setProcessing (true);
Steinberg::Vst::IAudioProcessor::process (...);
```

Note that the [ProcessData](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessData.html)->[numSamples](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessData.html#aeb42971a4bd34d7baa27cff8d7e3cf26) which indicates how many samples are used in a process call can change from call to call, but never bigger than the [maxSamplesPerBlock](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1ProcessSetup.html#a41cd06a0c942a1b3f283092b893d0de3).

## Q: Can the sample rate change while the plug-in is processing?

No. Same as [Q: Can the maximum sample block size change while the plug-in is processing?](#q-can-the-maximum-sample-block-size-change-while-the-plug-in-is-processing)

## Q: Can the host call the process function without Audio buffers?

Yes, the host can call [IAudioProcessor::process](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html#a6b98eb31cf38ba96a28b303c13c64e13) without buffers (numInputs and numOutputs are zeroed), in order to flush parameters (from host to plug-in).

## Q: What is a Side-Chain?

See [(3.0.0) Multiple Dynamic I/O Support](../Technical+Documentation/Change+History/3.0.0/Multiple+Dynamic+IO.md)

## Q: How can I implement a Side-chain path into my plug-in?

See [(3.0.0) Multiple Dynamic I/O Support](../Technical+Documentation/Change+History/3.0.0/Multiple+Dynamic+IO.md)

## Q: My plug-in is capable of processing all possible channel configurations.

See [(3.0.0) Multiple Dynamic I/O Support](../Technical+Documentation/Change+History/3.0.0/Multiple+Dynamic+IO.md)

## Q: How are speaker arrangement settings handled for FX plug-ins?

See [(3.0.0) Multiple Dynamic I/O Support](../Technical+Documentation/Change+History/3.0.0/Multiple+Dynamic+IO.md)

## Q: My plug-in has mono input and stereo output. How does VST 3 handle this?

See [(3.0.0) Multiple Dynamic I/O Support](../Technical+Documentation/Change+History/3.0.0/Multiple+Dynamic+IO.md)

## Q: How does it work with silence flags?

See [(3.0.0) Silence flags Support](../Technical+Documentation/Change+History/3.0.0/Silence+flags.md) and tutorial about [how to use Silence flags](../Tutorials/How+to+use+the+silence+flags.md).

## Q: How report to the host that the plug-in latency has changed?

The plug-in should call from the editController its component handler [restartComponent](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html#a1f283573728cf0807224c5ebdf3ec3a6) function with flag kLatencyChanged:

```
componentHandler->restartComponent (kLatencyChanged);
```

The host will call [Vst::IAudioProcessor->getLatencySamples()](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html#af8884671ccefe68e0a86e72413a0fcf8) in order to check the new latency and adapt its latency compensation if supported.

## Q: How report to the host that the plug-in arrangement has changed?

See [(3.0.0) Multiple Dynamic I/O Support](../Technical+Documentation/Change+History/3.0.0/Multiple+Dynamic+IO.md)

## Q: Can IAudioProcessor::setProcessing be called without any IAudioProcessor::process call?

Yes, it depends how the DAW is supporting its processing, the following call sequence is legal:

```
Vst::IAudioProcessor::process (...);
Vst::IAudioProcessor::setProcessing (false);
Vst::IAudioProcessor::setProcessing (true);
// here no call to process, maybe something happen in between in the DAW
Vst::IAudioProcessor::setProcessing (false);
Vst::IAudioProcessor::setProcessing (true);
Vst::IAudioProcessor::process (...);
```

## Q: How to make sure that a plug-in is always processed?

If your plug-in always generates sound without need of any audio input, you can add the category "Generator" as subCategories (for example use [kFxGenerator](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/group__plugType.html#ga09060af560cf34b87e14d5dbd839ad52)) or you can return kInfiniteTail in the function [IAudioProcessor::getTailSamples](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html#abb6b16a66b2356a4038a778b815dbbf3)

## Q: Can IComponent::getState()/setState() be called during processing?

Yes, setState and getState are called normally from the UI Thread when the plug-in is used in a realtime context, in an offline context set/getState can be called in the same thread as the process call. Check the workflow diagram Audio Processor Call Sequence for more info about in which state which interfaces are called.

## Q: How can a plug-in be informed that it is currently processed in offline processing?

When a plug-in is used in an offline processing context (which is the case with Cubase 9.5/Nuendo 8 feature: Direct Offline Processing), its component will be initialized with [IComponent::setIoMode](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponent.html#a4618e7358890d549f990010bea4a4137) (Vst::kOfflineProcessing) (see The Simple Mode).
The offline processing mode (passed in the process call) is used when:

- the user exports audio (downmix)
- direct offline processing feature\
With [IComponent::setIoMode](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponent.html#a4618e7358890d549f990010bea4a4137) (Vst::kOfflineProcessing) you are able to differentiate between export and DOP (Direct Offline Processing).

[![getting_started_vid_1](https://i.ytimg.com/vi/62yMkHRfd2I/maxresdefault.jpg)](https://www.youtube.com/watch?v=62yMkHRfd2I)

Direct Offline Processing since Cubase 9.5

## Q: What should I NOT call in the realtime process function?

A good practice is to avoid any library calls from this critical realtime process. If you have to use them, check if they are designed for realtime operation and do not contain any locking mechanism. Avoid any filesystem access, networks and UI calls, memory allocation and deallocation, be careful when using STL containers which can allocate memory behind the scene, prefer patterns like non-blocking memory pools, and delegate tasks to UI/Timer thread for doing memory/file-network access jobs. Check [Audio Processor Call Sequence](../Technical+Documentation/Workflow+Diagrams/Audio+Processor+Call+Sequence.md) too.

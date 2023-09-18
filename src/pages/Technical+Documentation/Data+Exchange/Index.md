>/ [VST Home](../../) / [Technical Documentation](../Index.md)
>
># Data Exchange

**On this page:**

[[_TOC_]]

**Related pages:**

- [Data Exchange Tutorial](../../Tutorials/Data+Exchange.md)

---

## Introduction

In a modern plug-in the UI representation and the audio processing do not share any data directly.
This eliminates undefined behaviour as they run in different threads and any directly shared data would 
need to be protected by a mutex. But a mutex has no defined running time and may block the audio 
thread for too long creating an audible glitch which must be prevented.

The other issue with sharing data between the UI and the audio processing is that the audio is 
processed earlier than the time when the audio is streamed thru the monitor boxes or headphones.
Without synchronization the visual representation will be shown earlier than the sound it represents.
To synchronize the visual representation and the processing of the audio signal, the UI has to queue 
the visual data until the time is reached the audio is heard.

This problem is already solved for parameters which are automated by the host. The host delays 
sending the parameter change to the edit controller so that it is in sync with the heard audio.

But parameters are limited in how much data they can transfer, this may be enough for a simple peak
VU meter display, but presenting a FFT curve with it is a nightmare.

Version 3.7.9 of the SDK contains the new *Data Exchange* API to send data from the realtime
processing function to the controller in a safe and efficient way.

As this API needs support from the host and not all hosts will provide this API in the beginning
the SDK contains a backwards compatibility layer that either uses the API directly if available or 
uses an alternative method based on the IMessage API to emulate the API. See the 
[tutorial](../../Tutorials/Data+Exchange.md) on how to use it.

## The Data Exchange API

The API consists of two interfaces, the **IDataExchangeHandler** which needs to be implemented by the 
host and the **IDataExchangeReceiver** which needs to be implemented by the plug-in.

### IDataExchangeHandler

The **IDataExchangeHandler** implements a direct and thread-safe connection from the realtime
audio context of the audio processor to the non-realtime audio context of the edit controller.
This should be used when the edit controller needs continous data from the audio process for
visualization or other use-cases. To circumvent the bottleneck on the main thread it is possible
to configure the connection in a way that the calls to the edit controller will happen on a
background thread, see **IDataExchangeReceiver** below.

#### Opening a queue

The main operation for a plug-in is to open a queue via the handler before the plug-in is activated
(but it must be connected to the edit controller via the [IConnectionPoint](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IConnectionPoint.html) when the plug-in is using
the recommended separation of edit controller and audio processor). The best place to do this is in
the [IAudioProcessor::setupProcessing](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html#aefb5731b94dbc899a4a7e9cd1c96e6a2) method as this is also the place where the plug-in knows the
sample rate and maximum block size which the plug-in may need to calculate the queue block size.
When a queue is opened the edit controller gets a notification about it and the controller can
decide if it wishes to receive the data on the main thread or the background thread.

#### Sending data

In the [IAudioProcessor::process](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html#a6b98eb31cf38ba96a28b303c13c64e13) call the plug-in can now lock a block from the handler, fill it and
when done free the block via the handler which then sends the block to the edit controller. The edit
controller then receives the block either on the main thread or on a background thread depending on
the setup of the queue.
The host guarantees that all blocks are send before the plug-in is deactivated.

#### Closing a queue

The audio processor must close an opened queue and this has to be done after the processor was
deactivated and before it is disconnected from the edit controller (see [IConnectionPoint](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IConnectionPoint.html)).

#### What to do when the queue is full and no block can be locked?
The plug-in needs to be prepared for this situation as constraints in the overall system may cause
the queue to get full. If you need to get this information to the controller you can declare a
hidden parameter which you set to a special value and send this parameter change in your audio
process method.

### IDataExchangeReceiver

The **IDataExchangeReceiver** interface must be implemented by the edit controller of the plug-in.
The host will call the *queueOpened* method when an exchange queue is opened by the processor and later
when the processor closes the queue the host will call the *queueClosed* method.

While the queue is open, the host will call the *onDataExchangeBlocksReceived* method whenever the 
processor has send data.

The edit controller can decide in the call to *queueOpened* if the host should deliver the data on a 
background thread or on the UI thread.

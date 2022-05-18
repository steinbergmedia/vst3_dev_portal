>/ [VST Home](../) / [Tutorials](Index.md)
>
># How to use the silence flags

**On this page:**

[[_TOC_]]

---

This tutorial explains how to use silence flags.

---

## What about Silence flags?

It is sometime useful for plug-ins processing to know if the audio inputs really contain audio or only silence (buffer filled with 0!), it is useful too for the host to know if the plug-in will produce silence audio outputs, for example in case of an instrument plug-in which has nothing to play (no input events are coming), then the host will be able to inform following plug-ins in the processing chain this information. This helps to reduce the amount of computing and improve overall performance.

But how does it works? The following part will show you how to get this information in the process call and how to propagate it to the audio outputs of the plug-in.

The silence flags is part of the [AudioBusBuffers](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1AudioBusBuffers.html) ([silenceFlags](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1AudioBusBuffers.html#a2c73b926e22ddb05193b6edd16a008f8)) passed from the host to the plug-in and back to the host in the process call.

## Plug-in receives a silent audio input

``` c++
//-----------------------------------------------------------------------
tresult PLUGIN_API AGain::process (ProcessData& data)
{
    //...

    //---check if silence---------------
    // silence flags are a bitmask where each bit corresponds to one channel of a bus
    // (for example L and R for stereo bus).
    // Here we check only if the whole first input is silent (in case of Stereo: the L and R are silent)
    if (data.inputs[0].silenceFlags != 0) // if flags is not zero => then it means that we have silent!
    {
        // in the example we are applying a gain to the input signal
        // As we know that the input is only filled with zero, the output will be then filled with zero too!
        for (int32 i = 0; i < numChannels; i++)
        {
            // do not need to clear the output buffer if they are the same than input buffer,
            // as we know that the input are filled with zero, else we need to clear the output buffers
            if (in[i] != out[i])
            {
                memset (out[i], 0, sampleFramesSize); // this is faster than applying a gain to each sample!
            }
        }

        // now we have to inform the host that our output is silent too
        // this is done simply by setting the silenceFlags of the output bus:
        data.outputs[0].silenceFlags = ((uint64)1 << numChannels) - 1; // which is 3 (in binary 0011) for stereo

        // here we are finish we could return
        return kResultTrue;
    }
```
        
>ⓘ **Note**\
>The host has the responsibility to clear the input buffers (set to zero) when it enables the silence flags (the output silence flags will be set by the host to no silence (=0)).

## Plug-in generates silent output

``` c++
//-----------------------------------------------------------------------
tresult PLUGIN_API AGain::process (ProcessData& data)
{
    //...

    //---check if silence---------------
    // See above


    // under certain condition our output buffer could be silent:
    // for example here our gain could be set to 0 or smaller than a threshold.
    // We have to inform the host that our output is silent too
    // this is done simply by setting the silenceFlags of the output bus:
    if (gain < 0.0000001)
    {
        for (int32 i = 0; i < numChannels; i++)
        {
            // be sure to set to zero our outputs
            memset (out[i], 0, sampleFramesSize);
        }
        // this will set to 1 all channels
        data.outputs[0].silenceFlags = ((uint64)1 << numChannels) - 1; // which is 3 (in binary 0011) for stereo
    }
    else
    {
        //...
    }
```

>ⓘ **Note**\
>The plug-in, if it produces silence output, has the responsibility to clear (set to zero) its output buffers and to correctly set the output silence flags.

## In bypass

In Bypass mode the plug-in has to be sure that its outputs have the same stand than its inputs:

``` c++
//-----------------------------------------------------------------------
tresult PLUGIN_API AGain::process (ProcessData& data)
{
    //...

    //---check if silence---------------
    // See above


    //---in bypass mode outputs should be like inputs-----
    if (bBypass)
    {
        for (int32 i = 0; i < numChannels; i++)
        {
            // do not need to be copied if the buffers are the same
            if (in[i] != out[i])
            {
                memcpy (out[i], in[i], sampleFramesSize);
            }
        }
        // the input silence flags has to be forward to the output here!
        // very important for the host in order to inform next plug-in in the processing chain
        data.outputs[0].silenceFlags = data.inputs[0].silenceFlags;
    }
    else
    {
        //...
    }
```

## Plug-in generates audio output

``` c++
//-----------------------------------------------------------------------
tresult PLUGIN_API AGain::process (ProcessData& data)
{
    //...

    //---check if silence---------------
    // See above


    //---in bypass mode outputs should be like inputs-----
    if (bBypass)
    {
        //... see above
        data.outputs[0].silenceFlags = data.inputs[0].silenceFlags;
    }
    else
    {
        // here we will generate an audio output from the input which contains not only zero
        // which is the main use case of a plug-in
        //...

        // then we have to inform the host that our output is not silent
        // simply by setting the silenceFlags to zero
        data.outputs[0].silenceFlags = 0;
    }
    //...
```

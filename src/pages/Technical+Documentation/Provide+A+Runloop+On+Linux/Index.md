
>/ [VST Home](../../) / [Technical Documentation](../Index.md)
>
># Provide a RunLoop on Linux

**On this page:**

[[_TOC_]]

On Linux there is no global event run loop like on Windows and macOS. For this reason the plug-in can query for an ```IRunLoop``` interface which the host application must provide in two different ways.

## Query IRunLoop from IPlugFrame

The host application must provide the ```Vst::IRunLoop``` via ```Vst::IPluginFrame``` (by calling ```Vst::IPluView::setFrame(...)```).

```cpp
// Plug-in implementation
tresult PLUGIN_API MyPlugView::setFrame (Vst::IPlugFrame* frame)
{
    ...
    Steinberg::FUnknownPtr<Steinberg::Linux::IRunLoop> runLoop (plugFrame);
    if (runLoop)
    {
        runLoop->registerEventHandler (...);
    }
    ...
}
```

## Query IRunLoop from the host context of IPlugFactory3

A plug-in also needs a way to query for an ```Vst::IRunLoop``` without ```Vst::IPlugFrame```. This allows to register timers in case the editor is closed or unavailable. 

These timers can be used inside Vst::IAudioProcessor for extra computations or sending messages within the UI thread.

The host application must call Vst::IPlugFactory3::setHostContext(...) for this and provide a ```context```. This can be used to query an ```Vst::IRunLoop``` interface.

```cpp
// Plug-in implementation
tresult PLUGIN_API MyPlugFactory::setHostContext (FUnknown* context)
{
    ...
    Steinberg::FUnknownPtr<Steinberg::Linux::IRunLoop> runLoop (context);
    if (runLoop)
    {
        runLoop->registerTimer (...);
    }
    ...
}
```

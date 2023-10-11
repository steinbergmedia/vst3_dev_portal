
>/ [VST Home](../../) / [Technical Documentation](../Index.md)
>
># Provide a RunLoop on Linux

**On this page:**

[[_TOC_]]

---

On *Linux*, there is no global event run loop like on *Windows* and *macOS*. For this reason, the plug-in can query for an [Linux::IRunLoop](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1Linux_1_1IRunLoop.html) which must be provided by the host application in two different ways.

## Query IRunLoop from IPlugFrame

The host application must provide the [Linux::IRunLoop](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1Linux_1_1IRunLoop.html) via [IPlugFrame](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugFrame.html) (by calling [IPlugView::setFrame](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugView.html#ab0f059918bbf55ce110fc410240de423)).

```cpp
// Plug-in implementation
tresult PLUGIN_API MyPlugView::setFrame (Steinberg::IPlugFrame* frame)
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



A plug-in also needs a way to query for an [Linux::IRunLoop](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1Linux_1_1IRunLoop.html) without [IPlugFrame](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugFrame.html). This allows to register timers in case the editor is closed or unavailable. 

These timers can be used inside [Vst::IAudioProcessor](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IAudioProcessor.html) for extra computations or sending messages within the UI thread.

The host application must call [Vst::IPlugFactory3::setHostContext (context)](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPluginFactory3.html#a7fa0087a5cb612e3aeeefa4c91f638c7) for this and provide a ```context```. This ```context``` can be used to query an [Linux::IRunLoop](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1Linux_1_1IRunLoop.html) interface.

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

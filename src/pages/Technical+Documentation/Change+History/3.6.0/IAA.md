>/ [VST Home](../../../index.md) / [Technical Documentation](../../Index.md)
>
># [3.6.0] iOS Inter-App Audio

**On this page:**

[[_TOC_]]

---

iOS InterApp-Audio application out of your **VST 3 plug-in**

## Introduction

The **VST 3 SDK** provides an easy way to create an iOS InterApp-Audio application out of your **VST 3 plug-in**.

The SDK comes with an iOS **VST 3** host application that can run standalone or as an Inter-App Audio slave. If your plug-in does not use any specific Windows or Mac OS X API's, it should be reasonably easy to get your plug-in running on iOS.

If you use [**VSTGUI4**](../What+is+the+VST+3+SDK/VSTGUI.md) with the VST3Editor class as your UI, you mainly only have to create a new UI description for the different device sizes.

## How does it work?

### Create and Setup the Xcode Project

- Create a new iOS Application in Xcode. Use the "Empty Application" template.
- Use "C++11" as "C++ Language Dialect".
- Activate "Objective-C Automatic Reference Counting".
- Change the Bundle Identifier according to your registered AppID at Apple (see the Apple Documentation).
- Activate the "Inter-App Audio" capability for the project.
- Activate the "Background Modes" capability for the project and check the "Audio and Airplay" mode.
- Change the "Header Search Path" configuration to add a path to the root of the VST 3 SDK.

### Add your Audio Component description to the Info.plist

- Add a new Array with the name "AudioComponents".
- Add a new Dictionary to the array.
- Add the following keys to the dictionary: manufacturer, name, type, subtype, version.
- Set the values of these keys:
- The manufacturer value must be the one registered with Apple (the one you use for AudioUnits).
- The type value must be either 'aurx' (Effect), 'aurm' (Effect with MIDI), 'aurg' (Generator) or 'auri' (Instrument).
- The version value must be 1.

### Add files to the project

- all the sources from your **VST 3 plug-in** project
- all files from *public.sdk/source/vst/interappaudio/*
- all files from *public.sdk/source/vst/hosting*
- all files from *base/source/* (if not already done previously)
- *public.sdk/source/vst/auwrapper/NSDataIBStream.mm* (if not already done previously)

### If using VSTGUI

- add *vstgui_ios.mm*
- add *vstgui_uidescription_ios.mm*

## Code changes

**Xcode** created some files for you when you created the project. One of it is the App Delegate. You need to change the base class from `NSResponder<UIApplicationDelegate>` to `VSTInterAppAudioAppDelegateBase` (you need to import its header file which is here:\
*public.sdk/source/vst/interappaudio/VSTInterAppAudioAppDelegateBase.h)* and then remove all methods from it. If you want to add some custom behavior to your app, you should do it in your App Delegate class implementation. For example, if you want to only allow landscape mode, you have to add this method:

``` c++
//-----------------------------------------------------------------
- (NSUInteger)application:(UIApplication *)application supportedInterfaceOrientationsForWindow:(UIWindow *)window
{
    return UIInterfaceOrientationMaskLandscapeLeft|UIInterfaceOrientationMaskLandscapeRight;
}
```

Make sure to call the super method if you override one of themethods implemented by **VSTInterAppAudioAppDelegateBase** (theheader shows which methods are implemented).

## UI Handling

### Creating a different UI when running on iOS

To create a different view for iOS, you can check the host context for the **IInterAppAudioWrapper** interface:

``` c++
//-----------------------------------------------------------------
IPlugView* PLUGIN_API MyEditController::createView (FIDString _name)
{
    ConstString name (_name);
    if (name == ViewType::kEditor)
    {
        FUnknownPtr<IInterAppAudioHost> interAudioApp (getHostContext ());
        if (interAudioApp)
        {
            // create and return the view for iOS
        }
        else
        {
            // create and return the view for Windows/macOSX
        }
    }
    return 0;
}
```

### Using [**VSTGUI**](../What+is+the+VST+3+SDK/VSTGUI.md)

[**VSTGUI**](../What+is+the+VST+3+SDK/VSTGUI.md) 4.3 or higher includes support for iOS. You can use it the same like you use it for Windows or Mac OS X. See the [**VSTGUI**](../What+is+the+VST+3+SDK/VSTGUI.md) documentation for some limitations.

### Using a native UIView

If you want to create a native UIView as your plug-in editor, you have to create your own IPlugView derivate and attach the UIView in the IPlugView::attached method. An example of this can be seen in *"public.sdk/samples/vst/adelay/interappaudio/iosEditor.mm"*

### Host UI Integration

The example project in *"public.sdk/samples/vst/InterAppAudio"* uses a custom solution to show the UI for controlling and switching to the host application. You should take this as an example if you want to add it this way. You can also use the UI Apple provides with its example source for Inter-App Audio.

But you can also implement the host UI integration into your plug-in view. Your edit controller will get an interface to **IInterAppAudioHost** via its initialize method which you can use to get the host icon and send commands or switch to the host. If you use this method to show the host controls you should implement the **IInterAppAudioConnectionNotification** interface in your edit controller to conditionally show or hide the controls depending on the connection state.

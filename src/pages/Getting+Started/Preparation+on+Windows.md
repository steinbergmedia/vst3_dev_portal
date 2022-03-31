>/ [VST Home](../index.md) / [Getting Started](../Getting+Started/Index.md)
>
># Preparation on Windows

Generated VST3 Microsoft Visual Studio Projects using the [cmake](https://cmake.org/) included in the SDK will create by default symbolic links for each built plug-in in the [official VST3 folder](../Technical+Documentation/Locations+Format/Plugin+Locations.md), in order to allow this on Windows you have to adapt the Group Policy of Windows. See Here!

If you do not want to create this link, call cmake with this parameter:

```
-DSMTG_CREATE_PLUGIN_LINK=0
```

You could choose the new user location for VST3 plug-ins, call cmake with this parameter:

```
-DSMTG_PLUGIN_TARGET_USER_PROGRAM_FILES_COMMON=1
```

**Note for Windows:** In order to be able to create a symbolic link, you have to set the correct group policy. Proceed as follows:

- Enter ***Edit group policy*** in the Windows search field:

![getting_started_2](../../resources/getting_started_2.jpg)

- Navigate to:

>*Computer Configuration => Windows Settings => Security Settings =>Local Policies => User Rights Assignment => Create symbolic links*

Here you can set which users can create symbolic links.

![getting_started_3](../../resources/getting_started_3.jpg)

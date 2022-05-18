>/ [VST Home](../) / [Getting Started](Index.md)
>
># Preparation on Windows

Generated VST 3 Microsoft Visual Studio Projects using the [cmake](https://cmake.org/) included in the SDK will create by default symbolic links for each built plug-in in the [official VST 3 folder](../Technical+Documentation/Locations+Format/Plugin+Locations.md) (**C:\Program Files\Common Files\VST3**). In this folder it is not directly possible to write these symbolic links if you are allowed to do this (not Administrator for example), to solve this problem you have 3 solutions:

## Solution 1

If you do not want to create these links, call [cmake](https://cmake.org/) with this parameter:

``` c++
-DSMTG_CREATE_PLUGIN_LINK=0
```

## Solution 2

You could choose (which is the default) the [new user location](../Technical+Documentation/Locations+Format/Plugin+Locations.html) for VST 3 plug-ins which should have no right access issue as normal user, call [cmake](https://cmake.org/) with this parameter:

``` c++
-DSMTG_PLUGIN_TARGET_USER_PROGRAM_FILES_COMMON=1
```

## Solution 3

In order to allow create these symbolic links on Windows you have to adapt the [Group Policy of Windows](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/how-to-configure-security-policy-settings) which is only available by default in **Windows Pro** but not in **Windows Home**. In **Windows Home** you have to install it before changing the right access to this folder (**C:\Program Files\Common Files\VST3**). For this there are some internet webpages showing you how to do this, for example this one: <https://www.itechtics.com/enable-gpedit-msc-windows-11>.

As soon as the group Policy editor is available you have to start it by:
- Enter **run** in the Windows search field and start the run App and enter **gpedit.msc**

or

- Enter ***Edit group policy*** in the Windows search field:

![getting_started_2](../../resources/getting_started_2.jpg)

Now the **Local Group Policy Editor** is started:

- Navigate to:

>*Computer Configuration => Windows Settings => Security Settings =>Local Policies => User Rights Assignment => Create symbolic links*

Here you can set which users can create symbolic links, add your user name.

![getting_started_3](../../resources/getting_started_3.jpg)

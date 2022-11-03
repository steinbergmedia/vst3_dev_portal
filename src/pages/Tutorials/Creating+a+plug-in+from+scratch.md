>/ [VST Home](../) / [Tutorials](Index.md)
>
># Creating a cmake plug-in project from scratch

**On this page:**

[[_TOC_]]

---

## Goal

This tutorial provides a step-by-step guide for building a VST 3 plug-in's ```CMakeLists.txt``` from scratch. It covers the necessary steps, like defining a plug-in version number, adding C++ source files, linking to the ```sdk``` target, and setting platform-specific options.

> You can also use the [```VST 3 project generator```](https://github.com/steinbergmedia/vst3projectgenerator) which generates the ```CMakeLists.txt```.

---

## Building the ```CMakeLists.txt```

Make a new directory, and name it like your new plug-in, e.g. ```MyPlugin```. Afterwards, create a ```CMakeLists.txt``` file inside the new directory, and open it in a text editor. Add the following lines to it.

Set the minimum required version of cmake. In this example, ```3.15.0``` is sufficient.

```cmake
cmake_minimum_required(VERSION 3.15.0)
```

> See also: https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html

Name the project ```MyPlugin```, add a ```VERSION``` and an optional ```DESCRIPTION```.

```cmake
project(MyPlugin
    VERSION 1.0.0
    DESCRIPTION "MyPlugin Effect"
)
```

> See also: https://cmake.org/cmake/help/latest/command/project.html

Set the variable ```vst3sdk_SOURCE_DIR``` to the VST 3 SDK's directory. The directory ***must*** contain the root ```CMakeLists.txt``` of the SDK.  Add the SDK as a subdirectory, and call ```smtg_enable_vst3_sdk``` right after this.

```cmake
set(vst3sdk_SOURCE_DIR /path/to/vst3sdk)

add_subdirectory(${vst3sdk_SOURCE_DIR} ${PROJECT_BINARY_DIR}/vst3sdk)
smtg_enable_vst3_sdk()
```

Add a plug-in library and its source files by using the ```smtg_add_vst3plugin``` function.

```cmake
smtg_add_vst3plugin(MyPlugin
    source/version.h
    source/myplugin_cids.h
    source/myplugin_processor.h
    source/myplugin_processor.cpp
    source/myplugin_controller.h
    source/myplugin_controller.cpp
    source/myplugin_entry.cpp
)
```

Link the VST 3 SDK ```sdk``` to the plug-in library.

```cmake
target_link_libraries(MyPlugin
    PRIVATE
        sdk
)
```

Configure the plug-in version by calling ```smtg_target_configure_version_file```. This generates a temporary ```projectversion.h``` header, which is automatically included in your project.

```cmake
smtg_target_configure_version_file(MyPlugin)
```

Define platform-specific settings. 

For macOS, this includes
* setting the ```BUNDLE_IDENTIFIER``` to ```org.mycompany.myplugin```,
* setting a proper ```COMPANY_NAME``` to ```My Company``` and
* an executable ```.../VST3PluginTestHost.app``` to start the plug-in with in debug

For Windows, it needs
* a resource file ```resource/win32resource.rc```,
* setting the ```VS_STARTUP_PROJECT``` to ```MyPlugin``` and
* an executable ```.../VST3PluginTestHost.exe``` to start the plug-in with in debug


```cmake
if(SMTG_MAC)
    smtg_target_set_bundle(MyPlugin
        BUNDLE_IDENTIFIER org.mycompany.MyPlugin
        COMPANY_NAME My Company
    )
    smtg_target_set_debug_executable(MyPlugin
        "/Applications/VST3PluginTestHost.app"
        "--pluginfolder;$(BUILT_PRODUCTS_DIR)"
    )
elseif(SMTG_WIN)
    target_sources(MyPlugin
        PRIVATE 
            resource/win32resource.rc
    )
    if(MSVC)
        set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT MyPlugin)

        smtg_target_set_debug_executable(MyPlugin
            "$(ProgramW6432)/Steinberg/VST3PluginTestHost/VST3PluginTestHost.exe"
            "--pluginfolder \"$(OutDir)/\""
        )
    endif()
endif()
```

---

## Add plug-in GUI editor by using VSTGUI

In order to add a ```VSTGUI``` editor to the plug-in, link to the ```vstgui_support``` target.

```cmake
target_link_libraries(MyPlugin
        PRIVATE
            vstgui_support
    )
```

Add a ```myplugin_editor.uisdesc``` file as a resource. This file needs to be created manually.

```cmake
    smtg_target_add_plugin_resources(MyPlugin
        RESOURCES
            "resource/myplugin_editor.uidesc"
    )
```

> A plug-in with a basic ```*.uidesc``` file can be created by using the ```VST 3 project generator```.

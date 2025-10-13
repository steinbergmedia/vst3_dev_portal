>/ [VST Home](../../../) / [Technical Documentation](../../Index.md)
>
># \[3.8.0\] Wayland support

**On this page:**

[[_TOC_]]

**Related pages:**

- [Steinberg:: IPlugFrame](../../../Technical+Documentation/Change+History/3.0.0/Host+Interfaces.md#steinberg-iplugframe)
- [Steinberg:: IPlugView](../../../Technical+Documentation/Change+History/3.0.0/Plug+in+Interfaces.md#steinberg-iplugview)
- External links:
    - [About Wayland](https://wayland.freedesktop.org/)
    - [Wayland on gitlab](https://gitlab.freedesktop.org/wayland)
---

## Introduction

The following interfaces allow to query information about the host plug-in frame when running in a Wayland session.
 
 A native Wayland host application is both a Wayland client and a Wayland compositor. 
 The host application connects to the system compositor and creates application windows etc. using this compositor connection.
 
 A plug-in does not connect to the system compositor, but connects to the host application by calling *IWaylandHost::openWaylandConnection()*.
 
 The **IWaylandHost** interface can be created via *IHostApplication::createInstance*.
 
 As the interface may be required early, the host should pass *IHostApplication* to the plug-in using *IPluginFactory3::setHostContext*.
 
 When opening a plug-in window, the host calls *IPlugView::attached()* with the parent pointer set to the *wl_surface* of the parent frame (with an unknown surface role).
 
 The plug-in creates a *wl_surface* and must assign the *wl_subsurface* role using the given parent pointer. The plug-in is responsible for resizing the subsurface accordingly.
 
 In order to create additional windows (dialogs, menus, tooltips etc.), the plug-in can use the **IWaylandFrame** interface, which is implemented by the host's *IPlugFrame* object.
 
 The plug-in can use *IWaylandFrame::getParentSurface()* to query an *xdg_surface*, which can in turn be used as a parent in *xdg_surface_get_popup*.
 
 Likewise, the plug-in can use *IWaylandFrame::getParentToplevel()* to query an *xdg_toplevel*, which can be used in *xdg_toplevel_set_parent*.

### IWaylandHost
Implemented as a singleton in the host application.

- \[host imp\]
- \[released: 3.8.0\]
- \[optional\]

The plug-in controller could create it in the initialized state by using *IHostApplication::createInstance*.

### IWaylandFrame
Interface to query additional information about the host plug-in frame in a Wayland session.

- \[host imp\]
- [extends [Steinberg:: IPlugFrame](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugFrame.html)]
- \[released: 3.8.0\]
- \[optional\]
 
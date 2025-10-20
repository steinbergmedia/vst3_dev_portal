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
    - [VSTGUI Wayland Support](https://github.com/steinbergmedia/vstgui/tree/master/vstgui/lib/platform/linux)
---

## Introduction

The following interfaces allow querying information about the host plug-in frame when running in a Wayland session.

A native Wayland host application acts as both a Wayland client and a Wayland compositor. 
The host application connects to the system compositor and creates application windows etc. using this compositor connection.

A plug-in does not connect to the system compositor, but connects to the host application by calling [IWaylandHost::openWaylandConnection()](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1IWaylandHost.html#aac1c5eb544d1edda1f83947f67f05648).
 
 The [IWaylandHost](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1IWaylandHost.html) interface can be created via [Vst:: IHostApplication::createInstance](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IHostApplication.html#a931e5a2ff8867bd8dfdbae1e42b78106).
 
 As the interface may be required early, the host should pass [Vst:: IHostApplication](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IHostApplication.html) to the plug-in using [Steinberg:: IPluginFactory3::setHostContext (context)](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPluginFactory3.html#a7fa0087a5cb612e3aeeefa4c91f638c7).
 
 When opening a plug-in window, the host calls [IPlugView::attached()](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugView.html#a9fbc345c1e87f7e6210a8a49fdb96793) with the parent pointer set to the [wl_surface](https://wayland.freedesktop.org/docs/html/apa.html#protocol-spec-wl_surface) of the parent frame (with an unknown surface role).
 
 The plug-in creates a [wl_surface](https://wayland.freedesktop.org/docs/html/apa.html#protocol-spec-wl_surface) and must assign the [wl_subsurface](https://wayland.freedesktop.org/docs/html/apa.html#protocol-spec-wl_subsurface) role using the given parent pointer. The plug-in is responsible for resizing the subsurface accordingly.
 
 In order to create additional windows (dialogs, menus, tooltips etc.), the plug-in can use the [IWaylandFrame](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1IWaylandFrame.html) interface, which is implemented by the host's [Steinberg:: IPlugFrame](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugFrame.html) object.
 
 The plug-in can use [IWaylandFrame::getParentSurface()](https://steinbergmedia.github.io/vst3_doc/doc/vstinterfaces/classSteinberg_1_1IWaylandFrame.html#a055c5ea82125e5669e662779a0b0c0ba) to query an [xdg_surface](https://wayland-book.com/xdg-shell-basics/xdg-surface.html), which can in turn be used as a parent in [xdg_surface_get_popup](https://wayland-book.com/xdg-shell-basics/xdg-surface.html).
 
 Likewise, the plug-in can use [IWaylandFrame::getParentToplevel()](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1IWaylandFrame.html#a7f589ebeefa8cfdf33f5f2899a20c105) to query an [xdg_toplevel](https://wayland-book.com/xdg-shell-basics/xdg-toplevel.html), which can be used in *xdg_toplevel_set_parent*.

### IWaylandHost
Implemented as a singleton in the host application.

- \[host imp\]
- \[released: 3.8.0\]
- \[optional\]

The plug-in controller could create it in the initialized state by using [Vst:: IHostApplication::createInstance](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IHostApplication.html#a931e5a2ff8867bd8dfdbae1e42b78106).

### IWaylandFrame
Interface to query additional information about the host plug-in frame in a Wayland session.

- \[host imp\]
- [extends [Steinberg:: IPlugFrame](https://steinbergmedia.github.io/vst3_doc/base/classSteinberg_1_1IPlugFrame.html)]
- \[released: 3.8.0\]
- \[optional\]
 
  >/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.8.0 (2025/10/20)

## Version 3.8.0 (2025/10/20)

- [New licensing model for VST 3](../VST+3+Licensing/Index.md): 
  - VST 3 is now open source, released under the [MIT license](https://tlo.mit.edu/understand-ip/exploring-mit-open-source-license-comprehensive-guide).

- Interface changes:
  - Support for **MIDI 2.0**: new interfaces [IMidiLearn2](../Technical+Documentation/Change+History/3.8.0/IMidiLearn2.md) and [IMidiMapping2](../Technical+Documentation/Change+History/3.8.0/IMidiMapping2.md). These new interfaces replace the previous interfaces *IMidiLearn* and *IMidiMapping*.
  - Add missing ControllerNumbers enum for **MIDI 1.0** System messages.
  - Preview [Wayland](https://wayland.freedesktop.org/) support on Linux (originally written and contributed to VST SDK by PreSonus Software Ltd. and integrated in *Studio One Pro 7.2* and higher on Linux):
    - new interfaces [IWaylandHost, IWaylandFrame](../Technical+Documentation/Change+History/3.8.0/IWaylandHost.md).
    - new Platform UI Type: *kPlatformTypeWaylandSurfaceID*.

- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) update [4.15.0](https://github.com/steinbergmedia/vstgui/releases/tag/vstgui4_15_0)
  - new **Task Concurrency API**: It facilitates scheduling tasks for execution on background threads, either concurrently or sequentially. This API also enables the scheduling of tasks on the main thread from any other thread.
  - add support for custom view layouts (see **IViewLayouter** and **CViewContainer::setViewLayouter**).
  - add a grid view layouter that is similar to CSS Grid (see **GridLayouter**).
  - add Scripting for UIDescription (see **uidescription-scripting/uiscripting.md**)
  - add new text editor view (see **lib/ctexteditor.h**)
  - a scroll view can now have a top and a left edge view (see **CScrollView::setEdgeView**)
  - preliminary [Wayland](https://wayland.freedesktop.org/) support on Linux.

- Documentation
  - Adapt document to [new licensing model](../VST+3+Licensing/Index.md).
  - Update [Steinberg VST usage guidelines](../VST+3+Licensing/Usage+guidelines.md) document.

- cmake
  - Fix *SMTG_AddSMTGLibrary.cmake* (macOS/Linux): Remove old symlink before creating a new one.
  - Fix *SMTG_PlatformToolset.cmake* for Visual Studio Compiler: __cplusplus was not assigned to correct version ([pull#13](https://github.com/steinbergmedia/vst3_cmake/pull/13)).
  
- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - Add support of new ControllerNumbers enums in *legacymidiccout* Plug-in.
  - Add support of the new interfaces [IMidiLearn2](../Technical+Documentation/Change+History/3.8.0/IMidiLearn2.md) and [IMidiMapping2](../Technical+Documentation/Change+History/3.8.0/IMidiMapping2.md) in *Note Expression Synth* Plug-in.
  - EditorHost [Wayland](https://wayland.freedesktop.org/) support.

- Helper Classes:
  - Fix: Validator ScanParametersTest::run() - Doesn't Print Parameter Type Correctly ([Issue#142](https://github.com/steinbergmedia/vst3sdk/issues/142)).
  - Fix: validator.exe and moduleinfotool.exe Debug Version Throws Abort When Checking for Symlink ([Issue#145](https://github.com/steinbergmedia/vst3sdk/issues/145)).
  - Fix: Undefined Behavior (UB) in Validation Test Suite causes test case to fail ([Issue#77](https://github.com/steinbergmedia/vst3sdk/issues/77)).

- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.10.10:
  - Fix: potential crash at start on Windows platform ([Forum](https://forums.steinberg.net/t/win10-64bit-vst3plugintesthost-quits-silenty-on-start/1007817/5)).

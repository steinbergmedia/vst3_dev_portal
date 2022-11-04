>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.5.1 (2011/11/11)

## Version 3.5.1 (2011/11/11)

- Interface Changes:
  - due to a missing calling convention in IContextMenu interfaces, we had to generate new iids for this set of interfaces, Steinberg hosts will be updated (from 6.0.5) in order to support correctly this interface set. The old interfaces when already used will continue to be supported in Steinberg hosts. Sorry for this issue...
- Helpers Classes:
  - EditController is now one of the base classes of SingleComponentEffect
    - If you have used the SingleComponentEffect before, make sure that you must exclude vsteditcontroller.cpp now if it was in your project
  - EditControllerEx1 has a new function: setProgramName
  - ProgramList has a new function: setProgramName
- Samples:
  - Add Visual Studio 2010 projects
  - Remove Visual Studio 2003 projects
  - Fix AGain Single Component Effect
- VSTGUI 4.0
  - Update to the final 4.0 release
- Plug-in Wrappers:
  - VST 3 - VST 2.x Wrapper:
    - fix an issue with destroying the editor
  - VST 3 - Audio Unit Wrapper:
    - fix initial editor size issue
    - optimization for GetParameterInfo
- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md): VST 3 Plug-in Test Host
  - New feature: Convert VST 3 Preset to VST 2 preset (fxp or fxb)

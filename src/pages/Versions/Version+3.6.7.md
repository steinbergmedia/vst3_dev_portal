>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.6.7 (2017/03/03)

## Version 3.6.7 (2017/03/03)

- Preview Linux support (check <https://sdk.steinberg.net for discussion>): [Setup Linux for building VST 3 Plug-ins](../Getting+Started/How+to+setup+my+system.md)
- Licensing has changed! Please read the new [VST 3 Licensing Issues](../VST+3+Licensing/Index.md).
- Use cmake as project generator: [How to use cmake for Building VST 3 Plug-ins](../Tutorials/Using+cmake+for+building+plug-ins.md)
- This is the last version of the SDK supporting C++98, future versions will use C++11.
- Samples:
  - New VST 3 host implementation example:
    - New HostEditor application: Cross-platform (Win/macOS/Linux) standalone which opens the UI of a VST 3 plug-in
  - Updated validator application to support Linux
  - AGain plug-in updated:
    - it uses VSTGUI 4 instead of VSTGUI 3
    - it supports 64bit processing (template based)
  - All [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) 4 based samples support HiDPI on Windows now
  - Fix Program Change persistence in mda plug-ins example
  - Removed Xcode and Visual Studio projects, please use cmake now!
  - On Windows, we link VST 3 plug-ins with the MultiThreaded DLL runtime libraries (it will use Universal C Runtime Libraries, for older Windows version than Win 8.1 you may have to install these libraries from: <https://support.microsoft.com/en-us/kb/2999226>)
- VSTGUI 3.x is not supported anymore (removed from the SDK), but you can still download it from github: <https://github.com/steinbergmedia/vstgui>
- Plug-in wrappers:
  - VST 3 - Audio Unit Wrapper :
    - fix AU Wrapper MIDI Program Change issue (data1 instead of data2)
  - VST 3 - VST 2.x Wrapper :
    - fix resize issue on macOS
    - fix mapping between VST 3 ParamID and VST 2 paramID when bypass parameter is used

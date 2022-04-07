>/ ... / [Change History](../Index.md)
>
># Version 3.6.11 (2018/10/22)

## Version 3.6.11 (2018/10/22)

- [VSTGUI](../../../What+is+the+VST+3+SDK/VSTGUI.md) 4.7
    - update to VSTGUI 4.7
    - move from GTK++ to XCB for Linux support
    - redesigned drag'n drop
    - drags with bitmaps are now supported on Windows
    - standalone library support for Windows 7
    - new ImageStitcher tool
    - the GDI+ draw backend was removed, the Direct2D backend is the replacement
- New icon for VST 3 bundles: VST_Logo_Steinberg.ico and VST_Logo_Steinberg.icns (located in VST_SDK/VST3_SDK/doc/artwork folder)
- Interface changes:
    - VST 2 interface not available anymore!
    - New [Steinberg::Vst::INoteExpressionPhysicalUIMapping](../3.6.11/INoteExpressionPhysicalUIMapping.md) (plug-in): allowing the host to retrieve the preferred physical mapping associated to note expression supported by the plug-in.
- cmake:
    - further improvement for users projects
- [Plug-in Wrappers](../../../What+is+the+VST+3+SDK/Wrappers/Index.md):
    - AAX Wrapper (VST 3 - AAX Wrapper):
        - fix UI resizing
        - fix issue for default blocksize
    - VST 2 Wrapper:
        - fix for instruments which were not visible as instrument
- Helpers classes:
    -  make virtual some functions of class parameter (set/getUnitID, getInfo, set/getPrecision)
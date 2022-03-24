>/ ... / [VST 3 Locations / Format](../Locations+Format/Index.md)
>
># Plug-in Format Structure

**On this page:**

[[_TOC_]]

**Related pages:**

- [VST 3 Locations / Format](../Locations+Format/Index.md)
- [Snapshots](../Locations+Format/Snapshots.md)

---

## For the macOS platform

On the macOS platform, **VST 3 Plug-in** is a standard macOS bundle, its file extension is "**.vst3**" and has the following folder structure:

| Folder | Description |
| :- | :- |
| MyPlugin.vst3/Contents/Resources/ | folder contains all additional resource files useful for the plug-in |
| MyPlugin.vst3/Contents/MacOS/ | folder contains the plug-in’s macOS universal binary (Mach-O) |
| MyPlugin.vst3/Contents/Info.plist | the plug-in’s property list
| MyPlugin.vst3/Contents/PkgInfo | specifies the type and creator codes of the bundle (optional) |

### For the Windows platform

On the Windows platform, a VST 3 Plug-in is organized as a bundle like package format (simple folder), its file extension is ".vst3" and has the following folder structure:

| Folder | Description |
| :- | :- |
| MyPlugin.vst3/Contents/Resources/ | folder contains all additional resource files useful for the plug-in |
| MyPlugin.vst3/Contents/x86-win/MyPlugin.vst3 | folder contains the plug-in binary (32 bit dll for the i386 architecture) |
| MyPlugin.vst3/Contents/x86_64-win/MyPlugin.vst3 | folder contains the plug-in binary (64 bit dll for the x86_64 architecture) |
| MyPlugin.vst3/Contents/arm-win/MyPlugin.vst3 | Proposal: folder contains the plug-in binary (32 bit dll for the arm architecture) |
| MyPlugin.vst3/Contents/arm_64-win/MyPlugin.vst3 | Proposal: folder contains the plug-in binary (64 bit dll for the arm64 architecture) |
| MyPlugin.vst3/desktop.ini | used to set custom icon in Windows Explorer |
| MyPlugin.vst3/Plugin.ico | customized plug-in icon

```admonish info
In previous SDKs, the VST 3 Plug-in was defined as a single dll file with the .vst3 extension. This is deprecated since VST 3.6.10.
```

The file desktop.ini should contain:

**desktop.ini**

```
[.ShellClassInfo]
IconResource=Plugin.ico,0
```

and you should then change their attributes with this command line (s for system to make sure that Windows will use it for the folder/bundle, **r** for read-only and **h** for hidden (optional)):

```
attrib +s +r +h desktop.ini
attrib +r +h Plugin.ico
```

### For the Linux platform

On Linux, a **VST 3 Plug-in** is organized as a bundle like package format, its file extension is "**.vst3**", it follows this folder structure:

| Folder | Description |
| :- | :- |
| MyPlugin.vst3/Contents/Resources/ | folder contains all additional resource files useful for the plug-in |
| MyPlugin.vst3/Contents/i386-linux | folder contains the plug-in binary (32 bit shared library .so for Kernel Architecture i386) |
| MyPlugin.vst3/Contents/x86_64-linux | folder contains the plug-in binary (64 bit shared library .so for Kernel Architecture x86_64) |
| MyPlugin.vst3/Contents/XXX-linux | with XXX the architecture name based on the output of command-line "uname -m" (machine hardware) + "-linux"</p> for example:</p> • armv3l-linux<br> • armv4b-linux<br> • armv4l-linux<br> • armv5tel-linux<br> • armv5tejl-linux<br> • armv6l-linux<br> • armv7l-linux<br> • armv8l-linux |

### Merged Bundle

Note that all the bundles can be merged to one, which allows to have a cross-platform bundle/folder.

For example:

```
MyPlugin.vst3/
    |_ Contents/
    |   |__ Resources/
    |   |   |__ Snapshots/
    |   |   |   |__ 84E8DE5F92554F5396FAE4133C935A18_snapshot.png
    |   |   |   |__ 84E8DE5F92554F5396FAE4133C935A18_snapshot_2.0x.png
    |   |   |__ Documentation/
    |   |   |   |__ Manual.pdf
    |   |   |   |__ WhatsNew.pdf
    |   |   |__ Help/
    |   |       |__ helpdoc.xml
    |   |   |__ MyPlugin.srf
    |   |
    |   |__ armv7l-linux/
    |   |   |__ MyPlugin.so
    |   |
    |   |__ i686-linux/
    |   |   |__ MyPlugin.so
    |   |
    |   |__ i386-linux/
    |   |   |__ MyPlugin.so
    |   |
    |   |__ x86_64-linux/
    |   |   |__ MyPlugin.so
    |   |
    |   |__ MacOS/
    |   |   |__ MyPlugin
    |   |
    |   |__ x86-win/
    |   |   |__ MyPlugin.vst3
    |   |
    |   |__ x86_64-win/
    |   |   |__ MyPlugin.vst3
    |   |
    |   |__ Info.plist  (macOS Only)
    |   |__ PkgInfo     (macOS Only)
    |
    |____desktop.ini    (Windows only)
    |___ Plugin.ico     (Windows only)
```
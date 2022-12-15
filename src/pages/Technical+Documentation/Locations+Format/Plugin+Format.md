>/ ... / [VST 3 Locations / Format](Index.md)
>
># Plug-in Format Structure

**On this page:**

[[_TOC_]]

**Related pages:**

- [VST 3 Locations / Format](Index.md)
- [Snapshots](Snapshots.md)

---

## For the macOS platform

On the macOS platform, **VST 3** plug-in is a standard macOS bundle, its file extension is "**.vst3**" and has the following folder structure:

| Folder                                 | Description                                                   |
| :-                                     | :-                                                            |
| MyPlugin.vst3/Contents/Resources/      | folder contains all additional resource files useful for the plug-in |
| MyPlugin.vst3/Contents/MacOS/          | folder contains the plug-in’s macOS universal binary (Mach-O) |
| MyPlugin.vst3/Contents/moduleinfo.json | the plug-in’s moduleinfo                                   |
| MyPlugin.vst3/Contents/Info.plist      | the plug-in’s property list                                   |
| MyPlugin.vst3/Contents/PkgInfo         | specifies the type and creator codes of the bundle (optional) |

## For the Windows platform

On the Windows platform, a **VST 3** plug-in is organized as a bundle like package format (simple folder), its file extension is "**.vst3**" and has the following folder structure:

| Folder                                             | Description                  |
| :-                                                 | :-                           |
| MyPlugin.vst3/Contents/Resources/                  | folder contains all additional resource files useful for the plug-in |
| MyPlugin.vst3/Contents/**x86-win**/MyPlugin.vst3       | folder contains the plug-in binary (32 bit dll for i386 architecture) |
| MyPlugin.vst3/Contents/**x86_64-win**/MyPlugin.vst3    | folder contains the plug-in binary (64 bit dll for x86_64 architecture) |
| MyPlugin.vst3/Contents/**arm64ec-win**/MyPlugin.vst3   | folder contains the plug-in binary (64 bit dll for Arm64EC architecture).<br> Recommended archi for Windows on Arm64! |
| MyPlugin.vst3/Contents/**arm-win**/MyPlugin.vst3       | folder contains the plug-in binary (32 bit dll for Arm classic architecture) |
| MyPlugin.vst3/Contents/**arm64-win**/MyPlugin.vst3     | folder contains the plug-in binary (64 bit dll for Arm64 classic architecture) |
| MyPlugin.vst3/Contents/**arm64x-win**/MyPlugin.vst3    | folder contains the plug-in binary for both Arm64 code and Arm64EC code together (64 bit dll for Arm64 classic architecture) |
| MyPlugin.vst3/Contents/moduleinfo.json             | the plug-in’s moduleinfo |
| MyPlugin.vst3/desktop.ini                          | used to set custom icon in Windows Explorer |
| MyPlugin.vst3/Plugin.ico                           | customized plug-in icon |

>ⓘ **Note**\
>In previous SDKs, the **VST 3** plug-in was defined as a single dll file with the **.vst3** extension. This is deprecated since **VST 3.6.10**.

The file **desktop.ini** should contain:

**desktop.ini**

``` text
[.ShellClassInfo]
IconResource=Plugin.ico,0
```

and you should then change their attributes with this command line (s for system to make sure that Windows will use it for the folder/bundle, **r** for read-only and **h** for hidden (optional)):

``` msdos
attrib +s +r +h desktop.ini
attrib +r +h Plugin.ico
```

### Limitation for loading Plug-in DLL in a Host (inside the same process)

See [Microsoft Blogs about this](https://devblogs.microsoft.com/windows-music-dev/load-x64-plug-ins-like-vsts-from-your-arm-code-using-arm64ec/):

| OS            | PC Architecture   | Host Process App	| Compatible Plug-in Architectures  |
| :-            | :-                | :-                | :-                                |
| Windows 10    | Intel x86         | Intel x86         | Intel x86                         |
| Windows 10/11	| Intel x64	        | Intel x64	        | Intel x64*                        |
| Windows 10/11	| Intel x64	        | Intel x86	        | Intel x86                         |
| Windows 11	| Arm64	            | Arm64 Classic     | Arm64 Classic, Arm64X             |
| Windows 11	| Arm64	            | Arm64EC	        | Arm64X, Arm64EC, Intel x64        |
| Windows 11	| Arm64	            | Intel x64	        | Arm64EC, Intel x64, Arm64X        |

>"TLDR: Please offer both Arm64EC and x64 versions of your DAWs and plug-ins, and please stay up to date with the latest developer tooling and SDKs." ([Pete Brown - Microsoft](https://devblogs.microsoft.com/windows-music-dev/load-x64-plug-ins-like-vsts-from-your-arm-code-using-arm64ec/))

>ⓘ **Note**\
 With out of process (Inter-Process Commnunication) a host could overriden these limitations, by allowing, for example, a host Arm64 Classic to handle an Arm64EC Plug-in.

>ⓘ **Note**\
To learn more about Arm64X (new type of binary that can contain both the classic Arm64 code and Arm64EC code together), check [here](https://learn.microsoft.com/en-us/windows/arm/arm64x-pe).

## For the Linux platform

On Linux, a **VST 3** plug-in is organized as a bundle like package format, its file extension is "**.vst3**", it follows this folder structure:
 
| Folder                                 | Description                        |
| :-                                     | :-                                 |
| MyPlugin.vst3/Contents/Resources/      | folder contains all additional resource files useful for the plug-in |
| MyPlugin.vst3/Contents/i386-linux      | folder contains the plug-in binary (32 bit shared library .so for Kernel Architecture i386) |
| MyPlugin.vst3/Contents/x86_64-linux    | folder contains the plug-in binary (64 bit shared library .so for Kernel Architecture x86_64) |
| MyPlugin.vst3/Contents/XXX-linux       | with XXX the architecture name based on the output of command-line "uname -m" (machine hardware) + "-linux" for example: • armv3l-linux<br> • armv4b-linux<br> • armv4l-linux<br> • armv5tel-linux<br> • armv5tejl-linux<br> • armv6l-linux<br> • armv7l-linux<br> • armv8l-linux |
| MyPlugin.vst3/Contents/moduleinfo.json | the plug-in’s moduleinfo |

## Merged Bundle

Note that all the bundles can be merged to one, which allows to have a cross-platform bundle/folder.

**For example:**

``` text
MyPlugin.vst3/
    |_ Contents/
    |   |__ Resources/
    |   |   |__ Documentation/
    |   |   |   |__ Manual.pdf
    |   |   |   |__ WhatsNew.pdf
    |   |   |__ Help/
    |   |   |   |__ helpdoc.xml
    |   |   |__ Snapshots/
    |   |   |   |__ 84E8DE5F92554F5396FAE4133C935A18_snapshot.png
    |   |   |   |__ 84E8DE5F92554F5396FAE4133C935A18_snapshot_2.0x.png
    |   |   |__ VST XMLs
    |   |   |   |__ AGain/
    |   |   |       |__84E8DE5F92554F5396FAE4133C935A18/
    |   |   |           |__Generic 8 Cells.xml
    |   |   |           |__WK-Audio ID 8 Cells.xml
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
    |   |__ x86_64-win/
    |   |   |__ MyPlugin.vst3
    |   |
    |   |__ arm_64_ec-win/
    |   |   |__ MyPlugin.vst3
    |   |
    |   |__ moduleinfo.json
    |   |__ Info.plist  (macOS Only)
    |   |__ PkgInfo     (macOS Only)
    |
    |____desktop.ini    (Windows only)
    |___ Plugin.ico     (Windows only)
```

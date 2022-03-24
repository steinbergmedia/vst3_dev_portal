>/ [VST Home](/Index.md) / [Technical Documentation](../Index.md)
>
># VST 3 Locations / Format

**On this page:**

[[_TOC_]]

**Related pages:**

- [[3.5.0] Remote Presentation of Parameters](../Change+History/3.5.0/IXmlRepresentationController.md)

---

Formats definition of a **VST 3 Plug-in** and its preset and where they are located on different platforms.

## [Plug-in Format Structure](../Locations+Format/Plugin+Format.md)

### For the macOS platform

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

## [Snapshots](../Locations+Format/Snapshots.md)

Since VST 3.6.10, a **VST 3** bundle can contain pre-rendered snapshot images for a **VST 3** host as a visual representation of the plug-in UI.<br>
- This snapshot must have a predefined format and file name so that a host can recognize it.
- The image format must be PNG
- The image needs to be located inside the bundle directory in the folder **Resources/Snapshots/**
The file name must start with the unique ID of the audio processor printed in the form **84E8DE5F92554F5396FAE4133C935A18** followed by the string **_snapshot** and optionally followed by the HiDPI scale factor **_2.0x** and ending with the file extension **.png**.
    - For example, again's snapshot must be named:
        - **84E8DE5F92554F5396FAE4133C935A18_snapshot.png**
        - **84E8DE5F92554F5396FAE4133C935A18_snapshot_2.0x.png** for the 2x scaled HiDPI variant.
    - If the HiDPI scale factor is omitted, a scale factor of 1 is used.

## [Plug-in Locations](../Locations+Format/Plugin+Locations.md)

A **VST 3** Plug-in should be installed at specific folder location, the following tables specify these predefined locations for different operating system.

```admonish info
VST 3 doesn't require a Plug-in registration like it is used with DirectX.
```
```admonish warning
Links, Symbolic links or Shortcuts could be used from these predefined folders.
```
3 levels of folder location are defined:

- **User**: available only for the current logged user
- **Global**: available for all users of the system
- **Application**: available only inside an specific Audio Application (local Plug-ins)

```admonish info
The host should scan at first higher level of priority, first found Plug-in (for a given Processor UID) has to be used.
```

#### On macOS platform

On the macOS platform, the host application expects **VST 3 Plug-ins** to be located in:

| Priority | Location | Path | Comment |
| :- | :- | :- | :- |
| 1 |  User | /Users/$USERNAME/Library/Audio/Plug-ins/VST3/ |
| 2 |  Global | /Library/Audio/Plug-ins/VST3/ |
| 3 |  Global | /Network/Library/Audio/Plug-ins/VST3/ |
| 4 |  Application | $APPFOLDER/Contents/VST3/ |

```admonish info
Note: The host recursively scans these folders at startup in this order (Global/Application).
```

### On Windows platform

On the Windows platform, the host application expects VST 3 Plug-ins to be located in:

| Priority | Location | Path | Comment |
| :- | :- | :- | :- |
| 1 | User | %LOCALAPPDATA%/Programs/Common/VST3/ | FOLDERID_UserProgramFilesCommon</p> native bitdepth:</p> • 32bit Plug-in on 32bit OS,<br> • 64bit on 64bit OS<br> Mainly used for development use case. |
| 2 | Global | /Program Files/Common Files/VST3/ | FOLDERID_ProgramFilesCommon</p> native bitdepth:</p> • 32bit Plug-in on 32bit OS,<br> • 64bit on 64bit OS |
| 2 | Global | /Program Files (x86)/Common Files/VST3/ | 32bit Plug-ins on 64bit Windows |
| 3 | Application | $APPFOLDER/VST3/ | |

```admonish info
Note: The host recursively scans these folders at startup in this order (Global/Application).
```

### On Linux platform

On the Linux platform, the host application expects **VST 3 Plug-ins** to be located in:

| Priority | Location | Path | Comment |
| :- | :- | :- | :- |
| 1 | User | $HOME/.vst3/ |
| 2 | Global | /usr/lib/vst3/ |
| 3 | Global | /usr/local/lib/vst3/ |
| 4 | Application | $APPFOLDER/vst3/ |	

```admonish info
Note: The host recursively scans these folders at startup in this order (User/Global/Application).
```

## [Preset Format](../Locations+Format/Preset+Format.md)

The file extension has to be "**.vstpreset**", for example: *myBestDefault.vstpreset*

Specification of a **VST 3** Preset file:

![tech_doc_21](/resources/tech_doc_21.jpg)

Check the [Steinberg::Vst::PresetFile](https://steinbergmedia.github.io/vst3_doc/vstsdk/classSteinberg_1_1Vst_1_1PresetFile.html#a9db1b48345e92320b0dffc446d5e3483) source code which allows to read and write such presets.

## [Preset Locations](../Locations+Format/Preset+Locations.md)

**VST 3** presets are located at predefined locations on the computer, depending on the operating system.

- 3 levels of preset scope are defined:
    - User: available only for the current logged user
    - Public: available for all users of the system
    - Apps: available only inside a specific audio application
- 4 types of preset are defined:
    - User: presets created by the user
    - User_Factory: like User type, but more hidden
    - Shared_Factory: factory presets installed by the plug-in  installer
    - App_Factory: presets installed by an audio application installer, only visible for this specific audio application

```admonish caution
**$COMPANY** and **$PLUGIN-NAME** folder names contain only allowedcharacters for file naming (replace characters "**\\*?/:<>|\**"by "_").
```

```admonish info
**Note**: Each path defined below should be scanned in the given priority, presets extracted and added to the preset list.
```

### For Mac platform

| Priority | Type | Scope | Writable | Path | Comment |
| :- | :- | :- | :- | :- | :- |
| 1 | User | User | X | Users/$USERNAME/Library/Audio/Presets/$COMPANY/$PLUGIN-NAME/ |
| 2 | Shared_Factory | Public | - | Library/Audio/Presets/$COMPANY/$PLUGIN-NAME/ | Computer shared FactoryROM |
| 3 | Shared_Factory | Public | - | Network/Library/Audio/Presets/$COMPANY/$PLUGIN-NAME/ | Network shared FactoryROM |
| 4 | App_Factory | Apps | - | [$APPFOLDER]/VST3 Presets/$COMPANY/$PLUGIN-NAME/ | Host Application (Cubase, ...) |

### For Windows XP/2000 platform

| Priority | Type | Scope | Writable | Path | Comment |
| :- | :- | :- | :- | :- | :- |
| 1 | User | User | X | [my documents]/vst3 presets/$company/$plugin-name/ | csidl_personal |
| 2 | User_Factory | User | X | [documents and settings/$username/application data]/vst3 presets/$company/$plugin-name/ | csidl_appdata |
| 3 | Shared_Factory | Public | - | [documents and settings/$allusers/application data]/vst3 presets/$company/$plugin-name/ | csidl_common_appdata |
| 4 | App_Factory | Apps | - | [$APPFOLDER]/VST3 Presets/$COMPANY/$PLUGIN-NAME/ | Host Application (Cubase, ...) |

### For Windows Vista/7/8/10 

| Priority | Type | Scope | Writable | Path | Comment |
| :- | :- | :- | :- | :- | :- |
| 1 | User | User | X | [Users/$USERNAME/Documents]/VST3 Presets/$COMPANY/$PLUGIN-NAME/ | FOLDERID_Documents |
| 2 | User_Factory | User | X | [Users/$USERNAME/AppData/Roaming]/VST3 Presets/$COMPANY/$PLUGIN-NAME/ | FOLDERID_RoamingAppData |
| 3 | Shared_Factory | Public | - | [ProgramData]/VST3 Presets/$COMPANY/$PLUGIN-NAME/ | FOLDERID_ProgramData |
| 4 | App_Factory | Apps | - | [$APPFOLDER]/VST3 Presets/$COMPANY/$PLUGIN-NAME/ | Host Application (Cubase, ...) |

### For Linux platform

| Priority | Type | Scope | Writable | Path | Comment |
| :- | :- | :- | :- | :- | :- |
| 1 | User | User | X | $HOME/.vst3/presets/$COMPANY/$PLUGIN-NAME/ | |
| 2 | Shared_Factory | Public | - | /usr/share/vst3/presets/$COMPANY/$PLUGIN-NAME/ | |
| 3 | Shared_Factory | Public | - | /usr/local/share/vst3/presets/$COMPANY/$PLUGIN-NAME/| |
| 4 | App_Factory | Apps | - | [$APPFOLDER]/vst3/presets/$COMPANY/$PLUGIN-NAME/ | Host Application |

## [[3.5.0] Remote Presentation of Parameters](../Change+History/3.5.0/IXmlRepresentationController.md)
See [Remote Representation Locations](../Change+History/3.5.0/IXmlRepresentationController.md) **<- Link to be completed later**
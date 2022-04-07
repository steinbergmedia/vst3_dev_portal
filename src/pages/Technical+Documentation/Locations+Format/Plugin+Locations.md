>/ ... / [VST 3 Locations / Format](../Locations+Format/Index.md)
>
># Plug-in Locations

**On this page:**

[[_TOC_]]

**Related pages:**

- [VST 3 Locations / Format](../Locations+Format/Index.md)
- [Plug-in Format Structure](../Locations+Format/Plugin+Format.md)

---

## Introduction

A **VST 3** Plug-in should be installed at specific folder location, the following tables specify these predefined locations for different operating system.

>ⓘ **Note**\
>**VST 3** doesn't require a Plug-in registration like it is used with DirectX.

>⚠️ **Warning**\
>Links, Symbolic links or Shortcuts could be used from these predefined folders.

3 levels of folder location are defined:

- **User**: available only for the current logged user
- **Global**: available for all users of the system
- **Application**: available only inside an specific Audio Application (local Plug-ins)

>ⓘ **Note**\
>The host should scan at first higher level of priority, first found Plug-in (for a given Processor UID) has to be used.

### On macOS platform

On the macOS platform, the host application expects **VST 3 Plug-ins** to be located in:

| Prio  | Location      | Path                                          |
| :-    | :-            | :-                                            |
| 1     |  User         | /Users/$USERNAME/Library/Audio/Plug-ins/VST3/ |
| 2     |  Global       | /Library/Audio/Plug-ins/VST3/                 |
| 3     |  Global       | /Network/Library/Audio/Plug-ins/VST3/         |
| 4     |  Application  | $APPFOLDER/Contents/VST3/                     |

>ⓘ **Note**\
>The host recursively scans these folders at startup in this order (Global/Application).

### On Windows platform

On the Windows platform, the host application expects **VST 3 Plug-ins** to be located in:

| Prio  | Location      | Path                                          | Comment   |
| :-    | :-            | :-                                            | :-        |
| 1     | User          | %LOCALAPPDATA%/Programs/Common/VST3/          | FOLDERID_UserProgramFilesCommon native bitdepth:<br> • 32bit Plug-in on 32bit OS,<br> • 64bit on 64bit OS<br> Mainly used for development use case. |
| 2     | Global         | /Program Files/Common Files/VST3/            | FOLDERID_ProgramFilesCommon native bitdepth:<br> • 32bit Plug-in on 32bit OS,<br> • 64bit on 64bit OS |
| 2     | Global        | /Program Files (x86)/Common Files/VST3/       | 32bit Plug-ins on 64bit Windows |
| 3     | Application   | $APPFOLDER/VST3/                              | |

>ⓘ **Note**\
>The host recursively scans these folders at startup in this order (Global/Application).

### On Linux platform

On the Linux platform, the host application expects **VST 3 Plug-ins** to be located in:

| Prio  | Location      | Path                  |
| :-    | :-            | :-                    |
| 1     | User          | $HOME/.vst3/          |
| 2     | Global        | /usr/lib/vst3/        |
| 3     | Global        | /usr/local/lib/vst3/  |
| 4     | Application   | $APPFOLDER/vst3/      |

>ⓘ **Note**\
>The host recursively scans these folders at startup in this order (User/Global/Application).

>/ ... / [VST 3 Locations / Format](../Locations+Format/Index.md)
>
># Preset Locations

**On this page:**

[[_TOC_]]

**Related pages:**

- [VST 3 Locations / Format](../Locations+Format/Index.md)

---

## Introduction

**VST 3** presets are located at predefined locations on the computer, depending on the operating system.

- 3 levels of preset scope are defined:
    - **User**: available only for the current logged user
    - **Public**: available for all users of the system
    - **Apps**: available only inside a specific audio application
- 4 types of preset are defined:
    - **User**: presets created by the user
    - **User_Factory**: like User type, but more hidden
    - **Shared_Factory**: factory presets installed by the plug-in  installer
    - **App_Factory**: presets installed by an audio application installer, only visible for this specific audio application


>⚠️ **Warning**<br>
>**$COMPANY** and **$PLUGIN-NAME** folder names contain only allowed characters for file naming (replace characters "**\\*?/:<>|\**"by "_").


>ⓘ **Note**<br>
>Each path defined below should be scanned in the given priority, presets extracted and added to the preset list.

### For Mac platform

| Prio | Type | Scope | Write | Path | Comment |
| :- | :- | :- | :- | :- | :- |
| 1 | User | User | X | Users/$USERNAME/Library/Audio/Presets/$COMPANY/$PLUGIN-NAME/ |
| 2 | Shared_Factory | Public | - | Library/Audio/Presets/$COMPANY/$PLUGIN-NAME/ | Computer shared FactoryROM |
| 3 | Shared_Factory | Public | - | Network/Library/Audio/Presets/$COMPANY/$PLUGIN-NAME/ | Network shared FactoryROM |
| 4 | App_Factory | Apps | - | [$APPFOLDER]/VST3 Presets/$COMPANY/$PLUGIN-NAME/ | Host Application (Cubase, ...) |

### For Windows XP/2000 platform

| Prio | Type | Scope | Write | Path | Comment |
| :- | :- | :- | :- | :- | :- |
| 1 | User | User | X | [my documents]/vst3 presets/$company/$plugin-name/ | csidl_personal |
| 2 | User_Factory | User | X | [documents and settings/$username/application data]/vst3 presets/$company/$plugin-name/ | csidl_appdata |
| 3 | Shared_Factory | Public | - | [documents and settings/$allusers/application data]/vst3 presets/$company/$plugin-name/ | csidl_common_appdata |
| 4 | App_Factory | Apps | - | [$APPFOLDER]/VST3 Presets/$COMPANY/$PLUGIN-NAME/ | Host Application (Cubase, ...) |

### For Windows Vista/7/8/10 

| Prio | Type | Scope | Write | Path | Comment |
| :- | :- | :- | :- | :- | :- |
| 1 | User | User | X | [Users/$USERNAME/Documents]/VST3 Presets/$COMPANY/$PLUGIN-NAME/ | FOLDERID_Documents |
| 2 | User_Factory | User | X | [Users/$USERNAME/AppData/Roaming]/VST3 Presets/$COMPANY/$PLUGIN-NAME/ | FOLDERID_RoamingAppData |
| 3 | Shared_Factory | Public | - | [ProgramData]/VST3 Presets/$COMPANY/$PLUGIN-NAME/ | FOLDERID_ProgramData |
| 4 | App_Factory | Apps | - | [$APPFOLDER]/VST3 Presets/$COMPANY/$PLUGIN-NAME/ | Host Application (Cubase, ...) |

### For Linux platform

| Prio| Type | Scope | Write | Path | Comment |
| :- | :- | :- | :- | :- | :- |
| 1 | User | User | X | $HOME/.vst3/presets/$COMPANY/$PLUGIN-NAME/ | |
| 2 | Shared_Factory | Public | - | /usr/share/vst3/presets/$COMPANY/$PLUGIN-NAME/ | |
| 3 | Shared_Factory | Public | - | /usr/local/share/vst3/presets/$COMPANY/$PLUGIN-NAME/| |
| 4 | App_Factory | Apps | - | [$APPFOLDER]/vst3/presets/$COMPANY/$PLUGIN-NAME/ | Host Application |
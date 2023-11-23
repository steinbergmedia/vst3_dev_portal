>/ [VST Home](../../) / [Technical Documentation](../Index.md)
>
># Moduleinfo

An optional *moduleinfo.json* file can be part of the [module file package](../Locations+Format/Plugin+Format.md), located in the *Resources* folder.

The file contains the same information as the [Module Factory](Index.md#module-factory), plus an optional list of compatible classes.
The file is encoded in [JSON5](http://json5.org) format.

The Compatibility json array is used to declare a class to be treated as a replacement for another class or classes.

When used this way, the host does not need to load the component to know which classes the module provides.

This optional *moduleinfo.json* file was added in the **VST 3 SDK** version 3.7.5 and was located in the **Contents** folder of the bundle. In order to be compliant with code signing on macOS, this file is now (since version 3.7.8) located in the **Contents/Resources** folder.

## SDK

The **VST 3 SDK** contains a command-line utility called *moduleinfotool* that is used to create and validate the *moduleinfo.json* file from a VST plug-in.
See **public.sdk/vst-utilities/moduleinfotool**.

The *moduleinfotool* uses the ModuleInfoLib which can be used by hosts to read and parse the *moduleinfo.json* file.
See **public.sdk/source/vst/moduleinfo**

For plug-ins built with the **VST 3 SDK**, the *moduleinfo.json* file will be automatically created during the build process.

## Example

An example *moduleinfo.json* looks like this:

```json
{
  "Name": "helloworld",
  "Version": "3.7.5.0",
  "Factory Info": {
    "Vendor": "Steinberg Media Technologies",
    "URL": "http://www.steinberg.net",
    "E-Mail": "mailto:info@steinberg.de",
    "Flags": {
      "Unicode": true,
      "Classes Discardable": false,
      "Component Non Discardable": false,
    },
  },
  "Classes": [
    {
      "CID": "BD58B550F9E5634E9D2EFF39EA0927B1",
      "Category": "Audio Module Class",
      "Name": "Hello World",
      "Vendor": "Steinberg Media Technologies",
      "Version": "1.0.0.1",
      "SDKVersion": "VST 3.7.5",
      "Sub Categories": [
        "Fx",
      ],
      "Class Flags": 1,
      "Cardinality": 2147483647,
      "Snapshots": [
        {
          "Scale Factor": 1,
          "Path": "Contents/Resources/Snapshots/BD58B550F9E5634E9D2EFF39EA0927B1_snapshot.png",
        },
        {
          "Scale Factor": 2,
          "Path": "Contents/Resources/Snapshots/BD58B550F9E5634E9D2EFF39EA0927B1_snapshot_2.0x.png",
        },
      ],
    },
    {
      "CID": "A0B1A6F4005D9B47967177E37A671891",
      "Category": "Component Controller Class",
      "Name": "Hello WorldController",
      "Vendor": "Steinberg Media Technologies",
      "Version": "1.0.0.1",
      "SDKVersion": "VST 3.7.5",
      "Class Flags": 0,
      "Cardinality": 2147483647,
      "Snapshots": [
      ],
    },
  ],
  "Compatibility": [
    {
		"New": "BD58B550F9E5634E9D2EFF39EA0927B1",
		"Old": [
		  "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
		  "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
		],
	},
  ],
}
```

Check [here](../../FAQ/Compatibility+with+VST+2.x+or+VST+1.md) to learn how to create UID for old VST 2 plug-in.
